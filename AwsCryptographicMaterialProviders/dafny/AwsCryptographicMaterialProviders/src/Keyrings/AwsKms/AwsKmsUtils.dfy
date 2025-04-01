// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "AwsKmsMrkMatchForDecrypt.dfy"
include "../../AwsArnParsing.dfy"

module AwsKmsUtils {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened Actions
  import opened A = AwsKmsMrkMatchForDecrypt
  import opened AwsArnParsing
  import opened Seq
  import Types = AwsCryptographyMaterialProvidersTypes
  import KMS = Types.ComAmazonawsKmsTypes
  import UTF8

  function method OkForDecrypt(id : AwsKmsIdentifier, arn : string) : Outcome<Types.Error>
  {
    if !id.AwsKmsArnIdentifier? then
      Fail(Types.AwsCryptographicMaterialProvidersException( message := "KeyID cannot be used for Decrypt : " + arn))
    else if id.a.resource.resourceType != "key" then
      Fail(Types.AwsCryptographicMaterialProvidersException( message := "Alias cannot be used for Decrypt : " + arn))
    else
      Pass
  }

  // This allows us to refine the error
  type StringifyError = e: Types.Error | e.AwsCryptographicMaterialProvidersException? witness *

  predicate method StringifyResultIsErrorFree(
    input: map<UTF8.ValidUTF8Bytes, Result<(string, string), StringifyError>>
  ): (output: bool)
  {
    if exists r | r in input.Values :: r.Failure? then false else true
  }

  predicate method StringKeysAreUnique(
    input: map<UTF8.ValidUTF8Bytes, Result<(string, string), StringifyError>>
  ): (output: bool)
    requires StringifyResultIsErrorFree(input)
  {
    forall k, k' | k in input && k' in input
      :: k != k' ==> input[k].value.0 != input[k'].value.0
  }

  opaque function method {:resource_limit 1600000 } StringifyEncryptionContext(
    utf8EncCtx: Types.EncryptionContext
  ):
    (res: Result<KMS.EncryptionContextType, Types.Error>)
    ensures |utf8EncCtx| == 0 ==> res.Success? && |res.value| == 0
    ensures res.Failure? ==> res.error.AwsCryptographicMaterialProvidersException?
    ensures
      && !StringifyResultIsErrorFree(
        map utf8Key | utf8Key in utf8EncCtx.Keys :: utf8Key := StringifyEncryptionContextPair(utf8Key, utf8EncCtx[utf8Key])
      )
      ==>
        res.Failure?
    ensures
      var stringifyResults :=
        map utf8Key | utf8Key in utf8EncCtx.Keys :: utf8Key := StringifyEncryptionContextPair(utf8Key, utf8EncCtx[utf8Key]);
      && StringifyResultIsErrorFree(stringifyResults)
      && !StringKeysAreUnique(stringifyResults)
      ==>
        res.Failure?
  {
    if |utf8EncCtx| == 0 then
      var kmsType: KMS.EncryptionContextType := map[];
      var rest3 := Success(kmsType);
      rest3

    else
      var stringifyResults: map<UTF8.ValidUTF8Bytes, Result<(string, string), StringifyError>> :=
        map utf8Key | utf8Key in utf8EncCtx.Keys :: utf8Key := StringifyEncryptionContextPair(utf8Key, utf8EncCtx[utf8Key]);
      if !StringifyResultIsErrorFree(stringifyResults)
      then
        var rest2 := Failure(
                       Types.AwsCryptographicMaterialProvidersException( message := "Encryption context contains invalid UTF8")
                     );
        rest2

      else
        assert forall r | r in stringifyResults.Values :: r.Success?;
        var stringKeysUnique := StringKeysAreUnique(stringifyResults);
        if !stringKeysUnique then
          var rest1 := Failure(Types.AwsCryptographicMaterialProvidersException(
                                 message := "Encryption context keys are not unique"));  // this should never happen...
          rest1

        else
          ghost var kmsType: KMS.EncryptionContextType := map r | r in stringifyResults.Values :: r.value.0 := r.value.1;
          var rest := Success(map r | r in stringifyResults.Values :: r.value.0 := r.value.1);
          assert rest.value == kmsType;
          rest
  }

  opaque function method StringifyEncryptionContextPair(utf8Key: UTF8.ValidUTF8Bytes, utf8Value: UTF8.ValidUTF8Bytes):
    (res: Result<(string, string), StringifyError>)
    ensures (UTF8.Decode(utf8Key).Success? && UTF8.Decode(utf8Value).Success?) <==> res.Success?
  {
    var key :- UTF8
               .Decode(utf8Key)
               .MapFailure(WrapStringToError);
    var value :- UTF8
                 .Decode(utf8Value)
                 .MapFailure(WrapStringToError);

    Success((key, value))
  }

  function method WrapStringToError(e: string)
    :(ret: StringifyError)
  {
    Types.AwsCryptographicMaterialProvidersException( message := e )
  }

  function method ValidateKmsKeyId(keyId: string)
    : (res: Result<(), Types.Error>)
    ensures res.Success? ==>
              && AwsArnParsing.ParseAwsKmsIdentifier(keyId).Success?
              && UTF8.IsASCIIString(keyId)
              && 0 < |keyId| <= AwsArnParsing.MAX_AWS_KMS_IDENTIFIER_LENGTH
  {
    var _ :- AwsArnParsing.ParseAwsKmsIdentifier(keyId).MapFailure(WrapStringToError);

    :- Need(UTF8.IsASCIIString(keyId),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Key identifier is not ASCII"));
    :- Need(0 < |keyId| <= AwsArnParsing.MAX_AWS_KMS_IDENTIFIER_LENGTH,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Key identifier is too long"));
    Success(())
  }

  function method GetValidGrantTokens(grantTokens: Option<Types.GrantTokenList>)
    : (res: Result<Types.GrantTokenList, Types.Error>)
    ensures res.Success? ==>
              var tokens := res.value;
              && 0 <= |tokens| <= 10
              && forall token | token in tokens :: 1 <= |token| <= 8192
    ensures res.Success? && grantTokens.Some? ==> res.value == grantTokens.value
  {
    var tokens: Types.GrantTokenList := grantTokens.UnwrapOr([]);
    :- Need(0 <= |tokens| <= 10,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Grant token list can have no more than 10 tokens"));
    :- Need(forall token | token in tokens :: 1 <= |token| <= 8192,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Grant token list contains a grant token with invalid length"));
    Success(tokens)
  }

  method GetEcdhPublicKey(
    client: KMS.IKMSClient,
    awsKmsKey: AwsKmsIdentifierString
  ) returns (res :Result<KMS.PublicKeyType, Types.Error>)
    requires client.ValidState()
    modifies client.Modifies
    ensures client.ValidState()
    ensures res.Success? ==>
              && 0 < |client.History.GetPublicKey|
              && Last(client.History.GetPublicKey).input
                 == KMS.GetPublicKeyRequest(
                      KeyId := awsKmsKey,
                      GrantTokens := None
                    )
              && Last(client.History.GetPublicKey).output.Success?
              && var getPublicKeyResponse := Last(client.History.GetPublicKey).output.value;
              && getPublicKeyResponse.KeyId.Some?
              && getPublicKeyResponse.KeyId.value == awsKmsKey
              && getPublicKeyResponse.KeyUsage.Some?
              && getPublicKeyResponse.KeyUsage.value == KMS.KeyUsageType.KEY_AGREEMENT
              && getPublicKeyResponse.PublicKey.Some?
              && var publicKey := getPublicKeyResponse.PublicKey.value;
              && KMS.IsValid_PublicKeyType(publicKey)
  {
    var getPublicKeyRequest := KMS.GetPublicKeyRequest(
      KeyId := awsKmsKey,
      GrantTokens := None
    );

    var maybePublicKeyResponse := client.GetPublicKey(
      getPublicKeyRequest
    );

    var getPublicKeyResponse :- maybePublicKeyResponse
    .MapFailure(e => Types.ComAmazonawsKms( ComAmazonawsKms := e ));

    :- Need(
      && getPublicKeyResponse.KeyId.Some?
      && getPublicKeyResponse.KeyId.value == awsKmsKey
      && getPublicKeyResponse.KeyUsage.Some?
      && getPublicKeyResponse.KeyUsage.value == KMS.KeyUsageType.KEY_AGREEMENT
      && getPublicKeyResponse.PublicKey.Some?,
      Types.AwsCryptographicMaterialProvidersException(
        message := "Invalid response from KMS GetPublicKey")
    );

    return Success(getPublicKeyResponse.PublicKey.value);
  }

  function method ParseKeyNamespaceAndName(keyNamespace: string, keyName: string)
    : (res: Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>)
    ensures res.Success? ==>
              var (namespace, name) := res.value;
              && |namespace| < UINT16_LIMIT
              && |name| < UINT16_LIMIT
  {
    var namespace :- UTF8.Encode(keyNamespace)
                     .MapFailure(e => Types.AwsCryptographicMaterialProvidersException(
                                     message := "Key namespace could not be UTF8-encoded" + e ));
    :- Need(|namespace| < UINT16_LIMIT,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Key namespace too long"));

    var name :- UTF8.Encode(keyName)
                .MapFailure(e => Types.AwsCryptographicMaterialProvidersException(
                                message := "Key name could not be UTF8-encoded" + e ));
    :- Need(|name| < UINT16_LIMIT,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Key name too long"));

    Success((namespace, name))
  }

  function method ValidateDiscoveryFilter(filter: Types.DiscoveryFilter)
    : (res: Result<(), Types.Error>)
    ensures res.Success? ==>
              && |filter.accountIds| > 0
              && (forall accountId | accountId in filter.accountIds :: |accountId| > 0)
              && |filter.partition| > 0
  {
    :- Need(|filter.accountIds| > 0,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Discovery filter must have at least one account ID"));
    :- Need(forall accountId | accountId in filter.accountIds :: |accountId| > 0,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Discovery filter account IDs cannot be blank"));
    :- Need(|filter.partition| > 0,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Discovery filter partition cannot be blank"));
    Success(())
  }

  class OnDecryptMrkAwareEncryptedDataKeyFilter
    extends DeterministicActionWithResult<Types.EncryptedDataKey, bool, Types.Error>
  {
    const awsKmsKey: AwsArnParsing.AwsKmsIdentifier
    const providerId: UTF8.ValidUTF8Bytes

    function Modifies(): set<object> {{}}

    constructor(
      awsKmsKey: AwsArnParsing.AwsKmsIdentifier,
      providerId: UTF8.ValidUTF8Bytes
    )
      ensures
        && this.awsKmsKey == awsKmsKey
        && this.providerId == providerId
    {
      this.awsKmsKey := awsKmsKey;
      this.providerId := providerId;
    }

    predicate Ensures(
      edk: Types.EncryptedDataKey,
      res: Result<bool, Types.Error>
    )
    {
      && (
        && res.Success?
        && res.value
        ==>
          edk.keyProviderId == providerId)
    }

    method Invoke(edk: Types.EncryptedDataKey)
      returns (res: Result<bool, Types.Error>)
      ensures Ensures(edk, res)
    {

      if edk.keyProviderId != providerId {
        return Success(false);
      }

      if !UTF8.ValidUTF8Seq(edk.keyProviderInfo) {
        // The Keyring produces UTF8 keyProviderInfo.
        // If an `aws-kms` encrypted data key's keyProviderInfo is not UTF8
        // this is an error, not simply an EDK to filter out.
        return Failure(
            Types.AwsCryptographicMaterialProvidersException( message := "Invalid AWS KMS encoding, provider info is not UTF8."));
      }

      var keyId :- UTF8
      .Decode(edk.keyProviderInfo)
      .MapFailure(WrapStringToError);
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-mrk-keyring.md#ondecrypt
      //# -  The provider info MUST be a [valid AWS KMS ARN](aws-kms-key-
      //# arn.md#a-valid-aws-kms-arn) with a resource type of `key` or
      //# OnDecrypt MUST fail.
      var arn :- AwsArnParsing.ParseAwsKmsArn(keyId).MapFailure(WrapStringToError);

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-mrk-keyring.md#ondecrypt
      //# -  The the function [AWS KMS MRK Match for Decrypt](aws-kms-mrk-match-
      //# for-decrypt.md#implementation) called with the configured AWS KMS
      //# key identifier and the provider info MUST return `true`.
      return Success(AwsKmsMrkMatchForDecrypt(
                       awsKmsKey,
                       AwsArnParsing.AwsKmsArnIdentifier(arn)
                     ));
    }
  }

}
