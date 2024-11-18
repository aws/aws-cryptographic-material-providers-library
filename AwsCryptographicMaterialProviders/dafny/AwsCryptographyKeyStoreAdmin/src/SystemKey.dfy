// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "KmsUtils.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/Index.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsUtils.dfy"

module {:options "/functionSyntax:4" } SystemKey {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import KMS = Com.Amazonaws.Kms
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KmsUtils
  import AtomicPrimitives
  import CanonicalEncryptionContext
  import MPL = MaterialProviders
  import Base64
  import UTF8
  import AwsKmsUtils
  import Structure

  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=ZGlnZXN0&oenc=65001&oeol=CR
  const DIGEST_UTF8_BYTES: seq<uint8> := [100,105,103,101,115,116]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=c2lnbg&oenc=65001&oeol=CR
  const SIGN_UTF8_BYTES: seq<uint8> := [115,105,103,110]

  lemma UTF8BytesAreValid()
    ensures
      && UTF8.IsASCIIString("digest")
      && UTF8.EncodeAscii("digest") == DIGEST_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(DIGEST_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString("sign")
      && UTF8.EncodeAscii("sign") == SIGN_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(SIGN_UTF8_BYTES)
  {}

  type SignError = e: Types.Error | (e.KeyStoreAdminException? || e.ComAmazonawsKms?) witness *
  type VerifyError = e: Types.Error | (e.KeyStoreAdminException? || e.ComAmazonawsKms? || e.MutationVerificationException?) witness *
  type SerializeError =  e: Types.Error | e. KeyStoreAdminException? witness *

  datatype Content = | Content(
    nameonly ContentToSHA: MPL.Types.EncryptionContext,
    nameonly PartionValue: string,
    nameonly SortValue: string,
    nameonly UUIDValue: string
  )
  {
    ghost predicate ValidState()
    {
      && 0 < |ContentToSHA|
      && 0 < |PartionValue|
      && 0 < |SortValue|
      && 0 < |UUIDValue|
    }
  }

  datatype SignInput = | SignInput (
    nameonly MaterialIdentifier: KMS.Types.KeyIdType,
    nameonly Content: Content,
    nameonly KmsTuple: KmsUtils.KMSTuple,
    nameonly Crypto: AtomicPrimitives.AtomicPrimitivesClient
  )
  {
    ghost predicate ValidState()
    {
      && KmsTuple.ValidState()
      && Crypto.ValidState()
      && Content.ValidState()
    }
  }

  datatype VerifyInput = | VerifyInput (
    nameonly MaterialIdentifier: KMS.Types.KeyIdType,
    nameonly Content: Content,
    nameonly CiphertextBlob: KMS.Types.CiphertextType,
    nameonly KmsTuple: KmsUtils.KMSTuple,
    nameonly Crypto: AtomicPrimitives.AtomicPrimitivesClient
  )
  {
    ghost predicate ValidState()
    {
      && KmsTuple.ValidState()
      && Crypto.ValidState()
      && Content.ValidState()
    }
  }

  method ProvideCryptoClient(
    // Crypto?: Option<AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient> := None
    Crypto?: Option<AtomicPrimitives.AtomicPrimitivesClient> := None
  )
    returns (output: Result<AtomicPrimitives.AtomicPrimitivesClient, AtomicPrimitives.Types.Error>)
    requires Crypto?.Some? ==> Crypto?.value.ValidState()
    modifies (if Crypto?.Some? then Crypto?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var Crypto: AtomicPrimitives.AtomicPrimitivesClient; //AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient;
    if (Crypto?.None?) {
      Crypto :- AtomicPrimitives.AtomicPrimitives();
    } else {
      Crypto := Crypto?.value;
    }
    // If the customer gave us the Crypto Client, it is fresh
    // If we create the Crypto Client, it is fresh
    assume {:axiom} fresh(Crypto) && fresh(Crypto.Modifies);
    return Success(Crypto);
  }

  method SignContent(
    input: SignInput
  )
    returns (output: Result<KMS.Types.CiphertextType, SignError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    // =- 1. EncryptionContextDigest
    // =- 2. Base64 Encode
    // =- 3.a Base64 encoded content in EC, along with parition key and sort key
    var kms_ec: KMS.Types.EncryptionContextType :- ContentToKmsEncryptionContext(
      input.Content,
      input.Crypto);
    hide *;
    // =- 3.b "Sign" as the plaintext
    var kmsReq := KMS.Types.EncryptRequest(
      KeyId := input.MaterialIdentifier,
      // KMS Plaintext type is Blob, so UTF8 Bytes is fine
      Plaintext := SIGN_UTF8_BYTES,
      EncryptionContext := Some(kms_ec),
      GrantTokens := Some(input.KmsTuple.grantTokens)
    );
    var kmsRes? := input.KmsTuple.kmsClient.Encrypt(kmsReq);
    // TODO-Mutations-GA : better error message for failure
    var kmsRes :- kmsRes?.MapFailure(e => Types.ComAmazonawsKms(e));
    :- Need(
      kmsRes.CiphertextBlob.Some?,
      // TODO-Mutations-GA : better error message for failure
      Types.KeyStoreAdminException(message := "KMS returned an invalid response.")
    );
    // =- 4. return KMS cipher-text result
    return Success(kmsRes.CiphertextBlob.value);
  }

  method VerifyContent(
    input: VerifyInput
  )
    returns (output: Result<bool, VerifyError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    // =- 1. EncryptionContextDigest
    // =- 2. Base64 Encode
    // =- 3.a Base64 encoded content in EC, along with parition key and sort key
    var kms_ec: KMS.Types.EncryptionContextType :- ContentToKmsEncryptionContext(
      input.Content,
      input.Crypto);
    hide *;
    var kmsReq := KMS.Types.DecryptRequest(
      KeyId := Some(input.MaterialIdentifier),
      CiphertextBlob := input.CiphertextBlob,
      EncryptionContext := Some(kms_ec),
      GrantTokens := Some(input.KmsTuple.grantTokens)
    );
    var kmsRes? := input.KmsTuple.kmsClient.Decrypt(kmsReq);
    // TODO-Mutations-GA : better error message for failure
    // Particularly, if the error is InvalidCiphertextException
    // than the content has been tampered with
    // and we should return  MutationVerificationException.
    // Otherwise, it is some other KMS issue, and we return a KeyStoreAdminException
    var kmsRes :- kmsRes?.MapFailure(e => Types.ComAmazonawsKms(e));
    :- Need(
      kmsRes.Plaintext.Some?,
      // TODO-Mutations-GA : better error message for failure
      Types.KeyStoreAdminException(message := "KMS returned an invalid response.")
    );
    // =- 4. Assert plain-text is "Sign"
    :- Need(
      kmsRes.Plaintext.value == SIGN_UTF8_BYTES,
      // TODO-Mutations-GA : better error message for failure
      Types.KeyStoreAdminException(message := "KMS returned an invalid response.")
    );
    return Success(true);

  }

  method {:vcs_split_on_every_assert} ContentToKmsEncryptionContext(
    Content: Content,
    Crypto: AtomicPrimitives.AtomicPrimitivesClient
  )
    returns (output: Result<KMS.Types.EncryptionContextType, SerializeError>)
    requires Crypto.ValidState() && Content.ValidState()
    ensures Crypto.ValidState()
    modifies Crypto.Modifies
    ensures output.Failure? ==> output.error.KeyStoreAdminException?
  {
    hide *;
    //=- 1. EncryptionContextDigest
    var digestResult: Result<seq<uint8>, CanonicalEncryptionContext.CanonizeDigestError> :=
      CanonicalEncryptionContext.EncryptionContextDigest(Crypto, Content.ContentToSHA);
    if (digestResult.Failure?) {
      var error: Types.Error;
      error := match digestResult.error {
        case AwsCryptographyPrimitives(e) =>
          // we cannot reliably serialize a Primitive error without work
          Types.KeyStoreAdminException(message:="Could not SHA-384 Content.")
        case AwsCryptographicMaterialProvidersException(e) =>
          Types.KeyStoreAdminException(message:="Could not SHA-384 Content. " + e)
      };
      return Failure(error);
    }
    //=- 2. Base64 Encode
    var encodeResult: Result<MPL.Types.Utf8Bytes, string> :=
      UTF8.Encode(Base64.Encode(digestResult.value));
    if (encodeResult.Failure?) {
      var error := Types.KeyStoreAdminException(
        message:="Could not serialize Digest of content. " + encodeResult.error
      );
      return Failure(error);
    }
    //=- 3. Base64 encoded content in EC, along with parition key and sort key
    // Dafny forgets that DIGEST_UTF8_BYTES is valid
    assert UTF8.ValidUTF8Seq(DIGEST_UTF8_BYTES) by {
      UTF8BytesAreValid();
      // TODO-Mutations-FF : What do we need to do convince Dafny this is true?
      assume {:axiom} UTF8.ValidUTF8Seq(DIGEST_UTF8_BYTES);
    }
    var ec_utf8 := map[DIGEST_UTF8_BYTES := encodeResult.value];
    // Dafny forgets that DIGEST_UTF8_BYTES is valid and all the other keys are valid.
    assert forall k | k in ec_utf8.Keys :: UTF8.ValidUTF8Seq(k);
    //=- 4. Stringify Content for KMS
    var ecResult: Result<KMS.Types.EncryptionContextType, AwsKmsUtils.StringifyError> :=
      AwsKmsUtils.StringifyEncryptionContext(ec_utf8);
    if (ecResult.Failure?) {
      // Right now, all the Errors from the MPL's StringifyEncryptionContext are the MPL error
      var error := Types.KeyStoreAdminException(message := ecResult.error.message);
      return Failure(error);
    }
    var rtn: KMS.Types.EncryptionContextType := ecResult.value
    + map[
      Structure.M_UUID := Content.UUIDValue,
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := Content.PartionValue,
      Structure.TYPE_FIELD := Content.SortValue
    ];
    return Success(rtn);
  }
}
