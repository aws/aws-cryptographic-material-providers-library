// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyPrimitivesTypes.dfy"

module {:extern "AESEncryption"} AESEncryption {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyPrimitivesTypes

  // The following are used to tie plaintext and ciphertext with the AAD that was used to produce them.
  // These assumptions can be used in the postconditions of externs, and be referenced elsewhere
  // in order to ensure that the AAD used is as expected.
  predicate {:axiom} PlaintextDecryptedWithAAD(plaintext: seq<uint8>, aad: seq<uint8>)
  predicate {:axiom} EncryptionOutputEncryptedWithAAD(output: Types.AESEncryptOutput, aad: seq<uint8>)
  predicate {:axiom} CiphertextGeneratedWithPlaintext (ciphertext: seq<uint8>, plaintext: seq<uint8>)
  predicate {:axiom} EncryptedWithKey(ciphertext: seq<uint8>, key: seq<uint8>)
  predicate {:axiom} DecryptedWithKey(key: seq<uint8>, plaintext: seq<uint8>)

  function method EncryptionOutputFromByteSeq(s: seq<uint8>, encAlg: Types.AES_GCM): (encArt: Types.AESEncryptOutput)
    requires 0 < encAlg.tagLength
    requires encAlg.tagLength as nat <= |s|
    ensures |encArt.cipherText + encArt.authTag| == |s|
    ensures |encArt.authTag| == encAlg.tagLength as int
  {
    assert |s| - encAlg.tagLength as int <= |s|;
    SequenceIsSafeBecauseItIsInMemory(s);

    var pivot_point := |s| as uint64 - encAlg.tagLength as uint64;
    var cipherText := s[..pivot_point];
    var authTag := s[pivot_point..];

    Types.AESEncryptOutput(cipherText := cipherText, authTag := authTag)
  }

  method {:extern "AESEncryption.AES_GCM", "AESEncryptExtern"} {:axiom} AESEncryptExtern(
    encAlg: Types.AES_GCM,
    iv: seq<uint8>,
    key: seq<uint8>,
    msg: seq<uint8>,
    aad: seq<uint8>
  )
    returns (res : Result<Types.AESEncryptOutput, Types.OpaqueError>)
    requires |iv| == encAlg.ivLength as int
    requires |key| == encAlg.keyLength as int
    ensures res.Success? ==> EncryptionOutputEncryptedWithAAD(res.value, aad)
    ensures res.Success? ==> CiphertextGeneratedWithPlaintext(res.value.cipherText, msg)
    ensures res.Success? ==> EncryptedWithKey(res.value.cipherText, key)

  method AESEncrypt(input: Types.AESEncryptInput)
    returns (res : Result<Types.AESEncryptOutput, Types.Error>)
    ensures res.Success? ==>
              && |res.value.cipherText| == |input.msg|
              && |res.value.authTag| == input.encAlg.tagLength as int
    ensures res.Success? ==> EncryptionOutputEncryptedWithAAD(res.value, input.aad)
    ensures res.Success? ==> CiphertextGeneratedWithPlaintext(res.value.cipherText, input.msg)
    ensures res.Success? ==> EncryptedWithKey(res.value.cipherText, input.key)
    // This is useful information to have to prove correctness
    ensures res.Success? ==> |res.value.authTag| == input.encAlg.tagLength as nat
  {
    SequenceIsSafeBecauseItIsInMemory(input.iv);
    SequenceIsSafeBecauseItIsInMemory(input.key);
    :- Need(
      && |input.iv| as uint64 == input.encAlg.ivLength as uint64
      && |input.key| as uint64  == input.encAlg.keyLength as uint64 ,
      Types.AwsCryptographicPrimitivesError(message := "Request does not match algorithm.")
    );

    var AESEncryptInput(encAlg, iv, key, msg, aad) := input;

    var value :- AESEncryptExtern(encAlg, iv, key, msg, aad);

    SequenceIsSafeBecauseItIsInMemory(value.cipherText);
    SequenceIsSafeBecauseItIsInMemory(value.authTag);
    SequenceIsSafeBecauseItIsInMemory(msg);
    :- Need(
      |value.cipherText| as uint64 == |msg| as uint64,
      Types.AwsCryptographicPrimitivesError(message := "AESEncrypt did not return cipherText of expected length")
    );
    :- Need(
      |value.authTag| as uint64 == encAlg.tagLength as uint64,
      Types.AwsCryptographicPrimitivesError(message := "AESEncryption did not return valid tag")
    );

    return Success(value);
  }

  method {:extern "AESEncryption.AES_GCM", "AESDecryptExtern"} {:axiom} AESDecryptExtern(
    encAlg: Types.AES_GCM,
    key: seq<uint8>,
    cipherTxt: seq<uint8>,
    authTag: seq<uint8>,
    iv: seq<uint8>,
    aad: seq<uint8>
  )
    returns (res: Result<seq<uint8>, Types.OpaqueError>)
    requires |key| == encAlg.keyLength as int
    requires |iv| == encAlg.ivLength as int
    requires |authTag| == encAlg.tagLength as int
    ensures res.Success? ==> PlaintextDecryptedWithAAD(res.value, aad)
    ensures res.Success? ==> CiphertextGeneratedWithPlaintext(cipherTxt, res.value)
    ensures res.Success? ==> DecryptedWithKey(key, res.value)

  method AESDecrypt(
    input: Types.AESDecryptInput
  )
    returns (res: Result<seq<uint8>, Types.Error>)
    ensures res.Success? ==> |res.value| == |input.cipherTxt|
    ensures res.Success? ==> PlaintextDecryptedWithAAD(res.value, input.aad)
    ensures res.Success? ==> CiphertextGeneratedWithPlaintext(input.cipherTxt, res.value)
    ensures res.Success? ==> DecryptedWithKey(input.key, res.value)
  {
    SequenceIsSafeBecauseItIsInMemory(input.iv);
    SequenceIsSafeBecauseItIsInMemory(input.key);
    SequenceIsSafeBecauseItIsInMemory(input.authTag);
    :- Need(
      && |input.key| as uint64 == input.encAlg.keyLength as uint64
      && |input.iv| as uint64 == input.encAlg.ivLength as uint64
      && |input.authTag| as uint64 == input.encAlg.tagLength as uint64,
      Types.AwsCryptographicPrimitivesError(message := "Request does not match algorithm.")
    );

    var AESDecryptInput(encAlg, key, cipherTxt, authTag, iv, aad) := input;
    var value :- AESDecryptExtern(encAlg, key, cipherTxt, authTag, iv, aad);

    SequenceIsSafeBecauseItIsInMemory(value);
    SequenceIsSafeBecauseItIsInMemory(cipherTxt);
    :- Need(
      |cipherTxt| as uint64 == |value| as uint64,
      Types.AwsCryptographicPrimitivesError(message := "AESDecrypt did not return plaintext of expected length")
    );

    return Success(value);
  }

  // The next four functions are for the benefit of the extern implementation to call,
  // avoiding direct references to generic datatype constructors
  // since their calling pattern is different between different versions of Dafny
  // (i.e. after 4.2, explicit type descriptors are required).

  function method CreateAESEncryptExternSuccess(output: Types.AESEncryptOutput): Result<Types.AESEncryptOutput, Types.OpaqueError> {
    Success(output)
  }

  function method CreateAESEncryptExternFailure(error: Types.OpaqueError): Result<Types.AESEncryptOutput, Types.OpaqueError> {
    Failure(error)
  }

  function method CreateAESDecryptExternSuccess(bytes: seq<uint8>): Result<seq<uint8>, Types.OpaqueError> {
    Success(bytes)
  }

  function method CreateAESDecryptExternFailure(error: Types.OpaqueError): Result<seq<uint8>, Types.OpaqueError> {
    Failure(error)
  }
}
