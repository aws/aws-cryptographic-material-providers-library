// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../StandardLibrary/src/Index.dfy"
module {:extern "software.amazon.cryptography.primitives.internaldafny.types" } AwsCryptographyPrimitivesTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types

  datatype AES_CTR = | AES_CTR (
    nameonly keyLength: SymmetricKeyLength ,
    nameonly nonceLength: Uint8Bits
  )
  datatype AES_GCM = | AES_GCM (
    nameonly keyLength: SymmetricKeyLength ,
    nameonly tagLength: Uint8Bytes ,
    nameonly ivLength: Uint8Bits
  )
  datatype AESDecryptInput = | AESDecryptInput (
    nameonly encAlg: AES_GCM ,
    nameonly key: seq<uint8> ,
    nameonly cipherTxt: seq<uint8> ,
    nameonly authTag: seq<uint8> ,
    nameonly iv: seq<uint8> ,
    nameonly aad: seq<uint8>
  )
  datatype AESEncryptInput = | AESEncryptInput (
    nameonly encAlg: AES_GCM ,
    nameonly iv: seq<uint8> ,
    nameonly key: seq<uint8> ,
    nameonly msg: seq<uint8> ,
    nameonly aad: seq<uint8>
  )
  datatype AESEncryptOutput = | AESEncryptOutput (
    nameonly cipherText: seq<uint8> ,
    nameonly authTag: seq<uint8>
  )
  datatype AesKdfCtrInput = | AesKdfCtrInput (
    nameonly ikm: seq<uint8> ,
    nameonly expectedLength: PositiveInteger ,
    nameonly nonce: Option<seq<uint8>> := Option.None
  )
  class IAwsCryptographicPrimitivesClientCallHistory {
    ghost constructor() {
      GenerateRandomBytes := [];
      Digest := [];
      HMac := [];
      HkdfExtract := [];
      HkdfExpand := [];
      Hkdf := [];
      KdfCounterMode := [];
      AesKdfCounterMode := [];
      AESEncrypt := [];
      AESDecrypt := [];
      GenerateRSAKeyPair := [];
      GetRSAKeyModulusLength := [];
      RSADecrypt := [];
      RSAEncrypt := [];
      GenerateECDSASignatureKey := [];
      ECDSASign := [];
      ECDSAVerify := [];
      GenerateECCKeyPair := [];
      GetPublicKeyFromPrivateKey := [];
      ValidatePublicKey := [];
      DeriveSharedSecret := [];
      CompressPublicKey := [];
      DecompressPublicKey := [];
      ParsePublicKey := [];
    }
    ghost var GenerateRandomBytes: seq<DafnyCallEvent<GenerateRandomBytesInput, Result<seq<uint8>, Error>>>
    ghost var Digest: seq<DafnyCallEvent<DigestInput, Result<seq<uint8>, Error>>>
    ghost var HMac: seq<DafnyCallEvent<HMacInput, Result<seq<uint8>, Error>>>
    ghost var HkdfExtract: seq<DafnyCallEvent<HkdfExtractInput, Result<seq<uint8>, Error>>>
    ghost var HkdfExpand: seq<DafnyCallEvent<HkdfExpandInput, Result<seq<uint8>, Error>>>
    ghost var Hkdf: seq<DafnyCallEvent<HkdfInput, Result<seq<uint8>, Error>>>
    ghost var KdfCounterMode: seq<DafnyCallEvent<KdfCtrInput, Result<seq<uint8>, Error>>>
    ghost var AesKdfCounterMode: seq<DafnyCallEvent<AesKdfCtrInput, Result<seq<uint8>, Error>>>
    ghost var AESEncrypt: seq<DafnyCallEvent<AESEncryptInput, Result<AESEncryptOutput, Error>>>
    ghost var AESDecrypt: seq<DafnyCallEvent<AESDecryptInput, Result<seq<uint8>, Error>>>
    ghost var GenerateRSAKeyPair: seq<DafnyCallEvent<GenerateRSAKeyPairInput, Result<GenerateRSAKeyPairOutput, Error>>>
    ghost var GetRSAKeyModulusLength: seq<DafnyCallEvent<GetRSAKeyModulusLengthInput, Result<GetRSAKeyModulusLengthOutput, Error>>>
    ghost var RSADecrypt: seq<DafnyCallEvent<RSADecryptInput, Result<seq<uint8>, Error>>>
    ghost var RSAEncrypt: seq<DafnyCallEvent<RSAEncryptInput, Result<seq<uint8>, Error>>>
    ghost var GenerateECDSASignatureKey: seq<DafnyCallEvent<GenerateECDSASignatureKeyInput, Result<GenerateECDSASignatureKeyOutput, Error>>>
    ghost var ECDSASign: seq<DafnyCallEvent<ECDSASignInput, Result<seq<uint8>, Error>>>
    ghost var ECDSAVerify: seq<DafnyCallEvent<ECDSAVerifyInput, Result<bool, Error>>>
    ghost var GenerateECCKeyPair: seq<DafnyCallEvent<GenerateECCKeyPairInput, Result<GenerateECCKeyPairOutput, Error>>>
    ghost var GetPublicKeyFromPrivateKey: seq<DafnyCallEvent<GetPublicKeyFromPrivateKeyInput, Result<GetPublicKeyFromPrivateKeyOutput, Error>>>
    ghost var ValidatePublicKey: seq<DafnyCallEvent<ValidatePublicKeyInput, Result<ValidatePublicKeyOutput, Error>>>
    ghost var DeriveSharedSecret: seq<DafnyCallEvent<DeriveSharedSecretInput, Result<DeriveSharedSecretOutput, Error>>>
    ghost var CompressPublicKey: seq<DafnyCallEvent<CompressPublicKeyInput, Result<CompressPublicKeyOutput, Error>>>
    ghost var DecompressPublicKey: seq<DafnyCallEvent<DecompressPublicKeyInput, Result<DecompressPublicKeyOutput, Error>>>
    ghost var ParsePublicKey: seq<DafnyCallEvent<ParsePublicKeyInput, Result<ParsePublicKeyOutput, Error>>>
  }
  trait {:termination false} IAwsCryptographicPrimitivesClient
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: IAwsCryptographicPrimitivesClientCallHistory
    predicate GenerateRandomBytesEnsuresPublicly(input: GenerateRandomBytesInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method GenerateRandomBytes ( input: GenerateRandomBytesInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateRandomBytes
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateRandomBytesEnsuresPublicly(input, output)
      ensures History.GenerateRandomBytes == old(History.GenerateRandomBytes) + [DafnyCallEvent(input, output)]

    predicate DigestEnsuresPublicly(input: DigestInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method Digest ( input: DigestInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Digest
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DigestEnsuresPublicly(input, output)
      ensures History.Digest == old(History.Digest) + [DafnyCallEvent(input, output)]

    // Functions are deterministic, no need for historical call events or ensures indirection
    // The public method to be called by library consumers
    function method HMac ( input: HMacInput )
      : (output: Result<seq<uint8>, Error>)
    // Functions that are transparent do not need ensures

    predicate HkdfExtractEnsuresPublicly(input: HkdfExtractInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method HkdfExtract ( input: HkdfExtractInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`HkdfExtract
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfExtractEnsuresPublicly(input, output)
      ensures History.HkdfExtract == old(History.HkdfExtract) + [DafnyCallEvent(input, output)]

    predicate HkdfExpandEnsuresPublicly(input: HkdfExpandInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method HkdfExpand ( input: HkdfExpandInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`HkdfExpand
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfExpandEnsuresPublicly(input, output)
      ensures History.HkdfExpand == old(History.HkdfExpand) + [DafnyCallEvent(input, output)]

    predicate HkdfEnsuresPublicly(input: HkdfInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method Hkdf ( input: HkdfInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Hkdf
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfEnsuresPublicly(input, output)
      ensures History.Hkdf == old(History.Hkdf) + [DafnyCallEvent(input, output)]

    predicate KdfCounterModeEnsuresPublicly(input: KdfCtrInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method KdfCounterMode ( input: KdfCtrInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`KdfCounterMode
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures KdfCounterModeEnsuresPublicly(input, output)
      ensures History.KdfCounterMode == old(History.KdfCounterMode) + [DafnyCallEvent(input, output)]

    predicate AesKdfCounterModeEnsuresPublicly(input: AesKdfCtrInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method AesKdfCounterMode ( input: AesKdfCtrInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AesKdfCounterMode
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AesKdfCounterModeEnsuresPublicly(input, output)
      ensures History.AesKdfCounterMode == old(History.AesKdfCounterMode) + [DafnyCallEvent(input, output)]

    predicate AESEncryptEnsuresPublicly(input: AESEncryptInput , output: Result<AESEncryptOutput, Error>)
    // The public method to be called by library consumers
    method AESEncrypt ( input: AESEncryptInput )
      returns (output: Result<AESEncryptOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AESEncrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AESEncryptEnsuresPublicly(input, output)
      ensures History.AESEncrypt == old(History.AESEncrypt) + [DafnyCallEvent(input, output)]

    predicate AESDecryptEnsuresPublicly(input: AESDecryptInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method AESDecrypt ( input: AESDecryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AESDecrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AESDecryptEnsuresPublicly(input, output)
      ensures History.AESDecrypt == old(History.AESDecrypt) + [DafnyCallEvent(input, output)]

    predicate GenerateRSAKeyPairEnsuresPublicly(input: GenerateRSAKeyPairInput , output: Result<GenerateRSAKeyPairOutput, Error>)
    // The public method to be called by library consumers
    method GenerateRSAKeyPair ( input: GenerateRSAKeyPairInput )
      returns (output: Result<GenerateRSAKeyPairOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateRSAKeyPair
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateRSAKeyPairEnsuresPublicly(input, output)
      ensures History.GenerateRSAKeyPair == old(History.GenerateRSAKeyPair) + [DafnyCallEvent(input, output)]

    // Functions are deterministic, no need for historical call events or ensures indirection
    // The public method to be called by library consumers
    function method GetRSAKeyModulusLength ( input: GetRSAKeyModulusLengthInput )
      : (output: Result<GetRSAKeyModulusLengthOutput, Error>)
    // Functions that are transparent do not need ensures

    predicate RSADecryptEnsuresPublicly(input: RSADecryptInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method RSADecrypt ( input: RSADecryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`RSADecrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures RSADecryptEnsuresPublicly(input, output)
      ensures History.RSADecrypt == old(History.RSADecrypt) + [DafnyCallEvent(input, output)]

    predicate RSAEncryptEnsuresPublicly(input: RSAEncryptInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method RSAEncrypt ( input: RSAEncryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`RSAEncrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures RSAEncryptEnsuresPublicly(input, output)
      ensures History.RSAEncrypt == old(History.RSAEncrypt) + [DafnyCallEvent(input, output)]

    predicate GenerateECDSASignatureKeyEnsuresPublicly(input: GenerateECDSASignatureKeyInput , output: Result<GenerateECDSASignatureKeyOutput, Error>)
    // The public method to be called by library consumers
    method GenerateECDSASignatureKey ( input: GenerateECDSASignatureKeyInput )
      returns (output: Result<GenerateECDSASignatureKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateECDSASignatureKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateECDSASignatureKeyEnsuresPublicly(input, output)
      ensures History.GenerateECDSASignatureKey == old(History.GenerateECDSASignatureKey) + [DafnyCallEvent(input, output)]

    predicate ECDSASignEnsuresPublicly(input: ECDSASignInput , output: Result<seq<uint8>, Error>)
    // The public method to be called by library consumers
    method ECDSASign ( input: ECDSASignInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ECDSASign
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ECDSASignEnsuresPublicly(input, output)
      ensures History.ECDSASign == old(History.ECDSASign) + [DafnyCallEvent(input, output)]

    predicate ECDSAVerifyEnsuresPublicly(input: ECDSAVerifyInput , output: Result<bool, Error>)
    // The public method to be called by library consumers
    method ECDSAVerify ( input: ECDSAVerifyInput )
      returns (output: Result<bool, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ECDSAVerify
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ECDSAVerifyEnsuresPublicly(input, output)
      ensures History.ECDSAVerify == old(History.ECDSAVerify) + [DafnyCallEvent(input, output)]

    predicate GenerateECCKeyPairEnsuresPublicly(input: GenerateECCKeyPairInput , output: Result<GenerateECCKeyPairOutput, Error>)
    // The public method to be called by library consumers
    method GenerateECCKeyPair ( input: GenerateECCKeyPairInput )
      returns (output: Result<GenerateECCKeyPairOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateECCKeyPair
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateECCKeyPairEnsuresPublicly(input, output)
      ensures History.GenerateECCKeyPair == old(History.GenerateECCKeyPair) + [DafnyCallEvent(input, output)]

    predicate GetPublicKeyFromPrivateKeyEnsuresPublicly(input: GetPublicKeyFromPrivateKeyInput , output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
    // The public method to be called by library consumers
    method GetPublicKeyFromPrivateKey ( input: GetPublicKeyFromPrivateKeyInput )
      returns (output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetPublicKeyFromPrivateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetPublicKeyFromPrivateKeyEnsuresPublicly(input, output)
      ensures History.GetPublicKeyFromPrivateKey == old(History.GetPublicKeyFromPrivateKey) + [DafnyCallEvent(input, output)]

    predicate ValidatePublicKeyEnsuresPublicly(input: ValidatePublicKeyInput , output: Result<ValidatePublicKeyOutput, Error>)
    // The public method to be called by library consumers
    method ValidatePublicKey ( input: ValidatePublicKeyInput )
      returns (output: Result<ValidatePublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ValidatePublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ValidatePublicKeyEnsuresPublicly(input, output)
      ensures History.ValidatePublicKey == old(History.ValidatePublicKey) + [DafnyCallEvent(input, output)]

    predicate DeriveSharedSecretEnsuresPublicly(input: DeriveSharedSecretInput , output: Result<DeriveSharedSecretOutput, Error>)
    // The public method to be called by library consumers
    method DeriveSharedSecret ( input: DeriveSharedSecretInput )
      returns (output: Result<DeriveSharedSecretOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DeriveSharedSecret
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DeriveSharedSecretEnsuresPublicly(input, output)
      ensures History.DeriveSharedSecret == old(History.DeriveSharedSecret) + [DafnyCallEvent(input, output)]

    predicate CompressPublicKeyEnsuresPublicly(input: CompressPublicKeyInput , output: Result<CompressPublicKeyOutput, Error>)
    // The public method to be called by library consumers
    method CompressPublicKey ( input: CompressPublicKeyInput )
      returns (output: Result<CompressPublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CompressPublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CompressPublicKeyEnsuresPublicly(input, output)
      ensures History.CompressPublicKey == old(History.CompressPublicKey) + [DafnyCallEvent(input, output)]

    predicate DecompressPublicKeyEnsuresPublicly(input: DecompressPublicKeyInput , output: Result<DecompressPublicKeyOutput, Error>)
    // The public method to be called by library consumers
    method DecompressPublicKey ( input: DecompressPublicKeyInput )
      returns (output: Result<DecompressPublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DecompressPublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DecompressPublicKeyEnsuresPublicly(input, output)
      ensures History.DecompressPublicKey == old(History.DecompressPublicKey) + [DafnyCallEvent(input, output)]

    predicate ParsePublicKeyEnsuresPublicly(input: ParsePublicKeyInput , output: Result<ParsePublicKeyOutput, Error>)
    // The public method to be called by library consumers
    method ParsePublicKey ( input: ParsePublicKeyInput )
      returns (output: Result<ParsePublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ParsePublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ParsePublicKeyEnsuresPublicly(input, output)
      ensures History.ParsePublicKey == old(History.ParsePublicKey) + [DafnyCallEvent(input, output)]

  }
  datatype CompressPublicKeyInput = | CompressPublicKeyInput (
    nameonly publicKey: ECCPublicKey ,
    nameonly eccCurve: ECDHCurveSpec
  )
  datatype CompressPublicKeyOutput = | CompressPublicKeyOutput (
    nameonly compressedPublicKey: seq<uint8>
  )
  datatype CryptoConfig = | CryptoConfig (

                          )
  datatype DecompressPublicKeyInput = | DecompressPublicKeyInput (
    nameonly compressedPublicKey: seq<uint8> ,
    nameonly eccCurve: ECDHCurveSpec
  )
  datatype DecompressPublicKeyOutput = | DecompressPublicKeyOutput (
    nameonly publicKey: ECCPublicKey
  )
  datatype DeriveSharedSecretInput = | DeriveSharedSecretInput (
    nameonly eccCurve: ECDHCurveSpec ,
    nameonly privateKey: ECCPrivateKey ,
    nameonly publicKey: ECCPublicKey
  )
  datatype DeriveSharedSecretOutput = | DeriveSharedSecretOutput (
    nameonly sharedSecret: seq<uint8>
  )
  datatype DigestAlgorithm =
    | SHA_512
    | SHA_384
    | SHA_256
  datatype DigestInput = | DigestInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly message: seq<uint8>
  )
  datatype ECCPrivateKey = | ECCPrivateKey (
    nameonly pem: seq<uint8>
  )
  datatype ECCPublicKey = | ECCPublicKey (
    nameonly der: seq<uint8>
  )
  datatype ECDHCurveSpec =
    | ECC_NIST_P256
    | ECC_NIST_P384
    | ECC_NIST_P521
    | SM2
  datatype ECDSASignatureAlgorithm =
    | ECDSA_P384
    | ECDSA_P256
  datatype ECDSASignInput = | ECDSASignInput (
    nameonly signatureAlgorithm: ECDSASignatureAlgorithm ,
    nameonly signingKey: seq<uint8> ,
    nameonly message: seq<uint8>
  )
  datatype ECDSAVerifyInput = | ECDSAVerifyInput (
    nameonly signatureAlgorithm: ECDSASignatureAlgorithm ,
    nameonly verificationKey: seq<uint8> ,
    nameonly message: seq<uint8> ,
    nameonly signature: seq<uint8>
  )
  datatype GenerateECCKeyPairInput = | GenerateECCKeyPairInput (
    nameonly eccCurve: ECDHCurveSpec
  )
  datatype GenerateECCKeyPairOutput = | GenerateECCKeyPairOutput (
    nameonly eccCurve: ECDHCurveSpec ,
    nameonly privateKey: ECCPrivateKey ,
    nameonly publicKey: ECCPublicKey
  )
  datatype GenerateECDSASignatureKeyInput = | GenerateECDSASignatureKeyInput (
    nameonly signatureAlgorithm: ECDSASignatureAlgorithm
  )
  datatype GenerateECDSASignatureKeyOutput = | GenerateECDSASignatureKeyOutput (
    nameonly signatureAlgorithm: ECDSASignatureAlgorithm ,
    nameonly verificationKey: seq<uint8> ,
    nameonly signingKey: seq<uint8>
  )
  datatype GenerateRandomBytesInput = | GenerateRandomBytesInput (
    nameonly length: PositiveInteger
  )
  datatype GenerateRSAKeyPairInput = | GenerateRSAKeyPairInput (
    nameonly lengthBits: RSAModulusLengthBitsToGenerate
  )
  datatype GenerateRSAKeyPairOutput = | GenerateRSAKeyPairOutput (
    nameonly publicKey: RSAPublicKey ,
    nameonly privateKey: RSAPrivateKey
  )
  datatype GetPublicKeyFromPrivateKeyInput = | GetPublicKeyFromPrivateKeyInput (
    nameonly eccCurve: ECDHCurveSpec ,
    nameonly privateKey: ECCPrivateKey
  )
  datatype GetPublicKeyFromPrivateKeyOutput = | GetPublicKeyFromPrivateKeyOutput (
    nameonly eccCurve: ECDHCurveSpec ,
    nameonly privateKey: ECCPrivateKey ,
    nameonly publicKey: seq<uint8>
  )
  datatype GetRSAKeyModulusLengthInput = | GetRSAKeyModulusLengthInput (
    nameonly publicKey: seq<uint8>
  )
  datatype GetRSAKeyModulusLengthOutput = | GetRSAKeyModulusLengthOutput (
    nameonly length: RSAModulusLengthBits
  )
  datatype HkdfExpandInput = | HkdfExpandInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly prk: seq<uint8> ,
    nameonly info: seq<uint8> ,
    nameonly expectedLength: PositiveInteger
  )
  datatype HkdfExtractInput = | HkdfExtractInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly salt: Option<seq<uint8>> := Option.None ,
    nameonly ikm: seq<uint8>
  )
  datatype HkdfInput = | HkdfInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly salt: Option<seq<uint8>> := Option.None ,
    nameonly ikm: seq<uint8> ,
    nameonly info: seq<uint8> ,
    nameonly expectedLength: PositiveInteger
  )
  datatype HMacInput = | HMacInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly key: seq<uint8> ,
    nameonly message: seq<uint8>
  )
  datatype KdfCtrInput = | KdfCtrInput (
    nameonly digestAlgorithm: DigestAlgorithm ,
    nameonly ikm: seq<uint8> ,
    nameonly expectedLength: PositiveInteger ,
    nameonly purpose: Option<seq<uint8>> := Option.None ,
    nameonly nonce: Option<seq<uint8>> := Option.None
  )
  datatype ParsePublicKeyInput = | ParsePublicKeyInput (
    nameonly publicKey: seq<uint8>
  )
  datatype ParsePublicKeyOutput = | ParsePublicKeyOutput (
    nameonly publicKey: ECCPublicKey
  )
  type PositiveInteger = x: int32 | IsValid_PositiveInteger(x) witness *
  predicate method IsValid_PositiveInteger(x: int32) {
    ( 0 <= x  )
  }
  datatype RSADecryptInput = | RSADecryptInput (
    nameonly padding: RSAPaddingMode ,
    nameonly privateKey: seq<uint8> ,
    nameonly cipherText: seq<uint8>
  )
  datatype RSAEncryptInput = | RSAEncryptInput (
    nameonly padding: RSAPaddingMode ,
    nameonly publicKey: seq<uint8> ,
    nameonly plaintext: seq<uint8>
  )
  type RSAModulusLengthBits = x: int32 | IsValid_RSAModulusLengthBits(x) witness *
  predicate method IsValid_RSAModulusLengthBits(x: int32) {
    ( 81 <= x  )
  }
  type RSAModulusLengthBitsToGenerate = x: int32 | IsValid_RSAModulusLengthBitsToGenerate(x) witness *
  predicate method IsValid_RSAModulusLengthBitsToGenerate(x: int32) {
    ( 81 <= x <= 4096 )
  }
  datatype RSAPaddingMode =
    | PKCS1
    | OAEP_SHA1
    | OAEP_SHA256
    | OAEP_SHA384
    | OAEP_SHA512
  datatype RSAPrivateKey = | RSAPrivateKey (
    nameonly lengthBits: RSAModulusLengthBits ,
    nameonly pem: seq<uint8>
  )
  datatype RSAPublicKey = | RSAPublicKey (
    nameonly lengthBits: RSAModulusLengthBits ,
    nameonly pem: seq<uint8>
  )
  type SymmetricKeyLength = x: int32 | IsValid_SymmetricKeyLength(x) witness *
  predicate method IsValid_SymmetricKeyLength(x: int32) {
    ( 1 <= x <= 32 )
  }
  type Uint8Bits = x: int32 | IsValid_Uint8Bits(x) witness *
  predicate method IsValid_Uint8Bits(x: int32) {
    ( 0 <= x <= 255 )
  }
  type Uint8Bytes = x: int32 | IsValid_Uint8Bytes(x) witness *
  predicate method IsValid_Uint8Bytes(x: int32) {
    ( 0 <= x <= 32 )
  }
  datatype ValidatePublicKeyInput = | ValidatePublicKeyInput (
    nameonly eccCurve: ECDHCurveSpec ,
    nameonly publicKey: seq<uint8>
  )
  datatype ValidatePublicKeyOutput = | ValidatePublicKeyOutput (
    nameonly success: bool
  )
  datatype Error =
      // Local Error structures are listed here
    | AwsCryptographicPrimitivesError (
        nameonly message: string
      )
      // Any dependent models are listed here

      // The Collection error is used to collect several errors together
      // This is useful when composing OR logic.
      // Consider the following method:
      // 
      // method FN<I, O>(n:I)
      //   returns (res: Result<O, Types.Error>)
      //   ensures A(I).Success? ==> res.Success?
      //   ensures B(I).Success? ==> res.Success?
      //   ensures A(I).Failure? && B(I).Failure? ==> res.Failure?
      // 
      // If either A || B is successful then FN is successful.
      // And if A && B fail then FN will fail.
      // But what information should FN transmit back to the caller?
      // While it may be correct to hide these details from the caller,
      // this can not be the globally correct option.
      // Suppose that A and B can be blocked by different ACLs,
      // and that their representation of I is only eventually consistent.
      // How can the caller distinguish, at a minimum for logging,
      // the difference between the four failure modes?
    // || (!access(A(I)) && !access(B(I)))
    // || (!exit(A(I)) && !exit(B(I)))
    // || (!access(A(I)) && !exit(B(I)))
    // || (!exit(A(I)) && !access(B(I)))
    | CollectionOfErrors(list: seq<Error>, nameonly message: string)
      // The Opaque error, used for native, extern, wrapped or unknown errors
    | Opaque(obj: object, alt_text : string)
  type OpaqueError = e: Error | e.Opaque? witness *
}
abstract module AbstractAwsCryptographyPrimitivesService
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyPrimitivesTypes
  import Operations : AbstractAwsCryptographyPrimitivesOperations
  function method DefaultCryptoConfig(): CryptoConfig
  method AtomicPrimitives(config: CryptoConfig := DefaultCryptoConfig())
    returns (res: Result<AtomicPrimitivesClient, Error>)
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies)
              && fresh(res.value.History)
              && res.value.ValidState()

  // Helper functions for the benefit of native code to create a Success(client) without referring to Dafny internals
  function method CreateSuccessOfClient(client: IAwsCryptographicPrimitivesClient): Result<IAwsCryptographicPrimitivesClient, Error> {
    Success(client)
  }
  function method CreateFailureOfError(error: Error): Result<IAwsCryptographicPrimitivesClient, Error> {
    Failure(error)
  }
  class AtomicPrimitivesClient extends IAwsCryptographicPrimitivesClient
  {
    constructor(config: Operations.InternalConfig)
      requires Operations.ValidInternalConfig?(config)
      ensures
        && ValidState()
        && fresh(History)
        && this.config == config
    const config: Operations.InternalConfig
    predicate ValidState()
      ensures ValidState() ==>
                && Operations.ValidInternalConfig?(config)
                && History !in Operations.ModifiesInternalConfig(config)
                && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    predicate GenerateRandomBytesEnsuresPublicly(input: GenerateRandomBytesInput , output: Result<seq<uint8>, Error>)
    {Operations.GenerateRandomBytesEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GenerateRandomBytes ( input: GenerateRandomBytesInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateRandomBytes
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateRandomBytesEnsuresPublicly(input, output)
      ensures History.GenerateRandomBytes == old(History.GenerateRandomBytes) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GenerateRandomBytes(config, input);
      History.GenerateRandomBytes := History.GenerateRandomBytes + [DafnyCallEvent(input, output)];
    }

    predicate DigestEnsuresPublicly(input: DigestInput , output: Result<seq<uint8>, Error>)
    {Operations.DigestEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method Digest ( input: DigestInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Digest
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DigestEnsuresPublicly(input, output)
      ensures History.Digest == old(History.Digest) + [DafnyCallEvent(input, output)]
    {
      output := Operations.Digest(config, input);
      History.Digest := History.Digest + [DafnyCallEvent(input, output)];
    }


    // The public method to be called by library consumers
    function method HMac ( input: HMacInput )
      : (output: Result<seq<uint8>, Error>)
      // Functions that are transparent do not need ensures
    {
      Operations.HMac(config, input)
    }

    predicate HkdfExtractEnsuresPublicly(input: HkdfExtractInput , output: Result<seq<uint8>, Error>)
    {Operations.HkdfExtractEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method HkdfExtract ( input: HkdfExtractInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`HkdfExtract
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfExtractEnsuresPublicly(input, output)
      ensures History.HkdfExtract == old(History.HkdfExtract) + [DafnyCallEvent(input, output)]
    {
      output := Operations.HkdfExtract(config, input);
      History.HkdfExtract := History.HkdfExtract + [DafnyCallEvent(input, output)];
    }

    predicate HkdfExpandEnsuresPublicly(input: HkdfExpandInput , output: Result<seq<uint8>, Error>)
    {Operations.HkdfExpandEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method HkdfExpand ( input: HkdfExpandInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`HkdfExpand
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfExpandEnsuresPublicly(input, output)
      ensures History.HkdfExpand == old(History.HkdfExpand) + [DafnyCallEvent(input, output)]
    {
      output := Operations.HkdfExpand(config, input);
      History.HkdfExpand := History.HkdfExpand + [DafnyCallEvent(input, output)];
    }

    predicate HkdfEnsuresPublicly(input: HkdfInput , output: Result<seq<uint8>, Error>)
    {Operations.HkdfEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method Hkdf ( input: HkdfInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Hkdf
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures HkdfEnsuresPublicly(input, output)
      ensures History.Hkdf == old(History.Hkdf) + [DafnyCallEvent(input, output)]
    {
      output := Operations.Hkdf(config, input);
      History.Hkdf := History.Hkdf + [DafnyCallEvent(input, output)];
    }

    predicate KdfCounterModeEnsuresPublicly(input: KdfCtrInput , output: Result<seq<uint8>, Error>)
    {Operations.KdfCounterModeEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method KdfCounterMode ( input: KdfCtrInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`KdfCounterMode
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures KdfCounterModeEnsuresPublicly(input, output)
      ensures History.KdfCounterMode == old(History.KdfCounterMode) + [DafnyCallEvent(input, output)]
    {
      output := Operations.KdfCounterMode(config, input);
      History.KdfCounterMode := History.KdfCounterMode + [DafnyCallEvent(input, output)];
    }

    predicate AesKdfCounterModeEnsuresPublicly(input: AesKdfCtrInput , output: Result<seq<uint8>, Error>)
    {Operations.AesKdfCounterModeEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method AesKdfCounterMode ( input: AesKdfCtrInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AesKdfCounterMode
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AesKdfCounterModeEnsuresPublicly(input, output)
      ensures History.AesKdfCounterMode == old(History.AesKdfCounterMode) + [DafnyCallEvent(input, output)]
    {
      output := Operations.AesKdfCounterMode(config, input);
      History.AesKdfCounterMode := History.AesKdfCounterMode + [DafnyCallEvent(input, output)];
    }

    predicate AESEncryptEnsuresPublicly(input: AESEncryptInput , output: Result<AESEncryptOutput, Error>)
    {Operations.AESEncryptEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method AESEncrypt ( input: AESEncryptInput )
      returns (output: Result<AESEncryptOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AESEncrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AESEncryptEnsuresPublicly(input, output)
      ensures History.AESEncrypt == old(History.AESEncrypt) + [DafnyCallEvent(input, output)]
    {
      output := Operations.AESEncrypt(config, input);
      History.AESEncrypt := History.AESEncrypt + [DafnyCallEvent(input, output)];
    }

    predicate AESDecryptEnsuresPublicly(input: AESDecryptInput , output: Result<seq<uint8>, Error>)
    {Operations.AESDecryptEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method AESDecrypt ( input: AESDecryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`AESDecrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures AESDecryptEnsuresPublicly(input, output)
      ensures History.AESDecrypt == old(History.AESDecrypt) + [DafnyCallEvent(input, output)]
    {
      output := Operations.AESDecrypt(config, input);
      History.AESDecrypt := History.AESDecrypt + [DafnyCallEvent(input, output)];
    }

    predicate GenerateRSAKeyPairEnsuresPublicly(input: GenerateRSAKeyPairInput , output: Result<GenerateRSAKeyPairOutput, Error>)
    {Operations.GenerateRSAKeyPairEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GenerateRSAKeyPair ( input: GenerateRSAKeyPairInput )
      returns (output: Result<GenerateRSAKeyPairOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateRSAKeyPair
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateRSAKeyPairEnsuresPublicly(input, output)
      ensures History.GenerateRSAKeyPair == old(History.GenerateRSAKeyPair) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GenerateRSAKeyPair(config, input);
      History.GenerateRSAKeyPair := History.GenerateRSAKeyPair + [DafnyCallEvent(input, output)];
    }


    // The public method to be called by library consumers
    function method GetRSAKeyModulusLength ( input: GetRSAKeyModulusLengthInput )
      : (output: Result<GetRSAKeyModulusLengthOutput, Error>)
      // Functions that are transparent do not need ensures
    {
      Operations.GetRSAKeyModulusLength(config, input)
    }

    predicate RSADecryptEnsuresPublicly(input: RSADecryptInput , output: Result<seq<uint8>, Error>)
    {Operations.RSADecryptEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method RSADecrypt ( input: RSADecryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`RSADecrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures RSADecryptEnsuresPublicly(input, output)
      ensures History.RSADecrypt == old(History.RSADecrypt) + [DafnyCallEvent(input, output)]
    {
      output := Operations.RSADecrypt(config, input);
      History.RSADecrypt := History.RSADecrypt + [DafnyCallEvent(input, output)];
    }

    predicate RSAEncryptEnsuresPublicly(input: RSAEncryptInput , output: Result<seq<uint8>, Error>)
    {Operations.RSAEncryptEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method RSAEncrypt ( input: RSAEncryptInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`RSAEncrypt
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures RSAEncryptEnsuresPublicly(input, output)
      ensures History.RSAEncrypt == old(History.RSAEncrypt) + [DafnyCallEvent(input, output)]
    {
      output := Operations.RSAEncrypt(config, input);
      History.RSAEncrypt := History.RSAEncrypt + [DafnyCallEvent(input, output)];
    }

    predicate GenerateECDSASignatureKeyEnsuresPublicly(input: GenerateECDSASignatureKeyInput , output: Result<GenerateECDSASignatureKeyOutput, Error>)
    {Operations.GenerateECDSASignatureKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GenerateECDSASignatureKey ( input: GenerateECDSASignatureKeyInput )
      returns (output: Result<GenerateECDSASignatureKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateECDSASignatureKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateECDSASignatureKeyEnsuresPublicly(input, output)
      ensures History.GenerateECDSASignatureKey == old(History.GenerateECDSASignatureKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GenerateECDSASignatureKey(config, input);
      History.GenerateECDSASignatureKey := History.GenerateECDSASignatureKey + [DafnyCallEvent(input, output)];
    }

    predicate ECDSASignEnsuresPublicly(input: ECDSASignInput , output: Result<seq<uint8>, Error>)
    {Operations.ECDSASignEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method ECDSASign ( input: ECDSASignInput )
      returns (output: Result<seq<uint8>, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ECDSASign
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ECDSASignEnsuresPublicly(input, output)
      ensures History.ECDSASign == old(History.ECDSASign) + [DafnyCallEvent(input, output)]
    {
      output := Operations.ECDSASign(config, input);
      History.ECDSASign := History.ECDSASign + [DafnyCallEvent(input, output)];
    }

    predicate ECDSAVerifyEnsuresPublicly(input: ECDSAVerifyInput , output: Result<bool, Error>)
    {Operations.ECDSAVerifyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method ECDSAVerify ( input: ECDSAVerifyInput )
      returns (output: Result<bool, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ECDSAVerify
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ECDSAVerifyEnsuresPublicly(input, output)
      ensures History.ECDSAVerify == old(History.ECDSAVerify) + [DafnyCallEvent(input, output)]
    {
      output := Operations.ECDSAVerify(config, input);
      History.ECDSAVerify := History.ECDSAVerify + [DafnyCallEvent(input, output)];
    }

    predicate GenerateECCKeyPairEnsuresPublicly(input: GenerateECCKeyPairInput , output: Result<GenerateECCKeyPairOutput, Error>)
    {Operations.GenerateECCKeyPairEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GenerateECCKeyPair ( input: GenerateECCKeyPairInput )
      returns (output: Result<GenerateECCKeyPairOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GenerateECCKeyPair
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GenerateECCKeyPairEnsuresPublicly(input, output)
      ensures History.GenerateECCKeyPair == old(History.GenerateECCKeyPair) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GenerateECCKeyPair(config, input);
      History.GenerateECCKeyPair := History.GenerateECCKeyPair + [DafnyCallEvent(input, output)];
    }

    predicate GetPublicKeyFromPrivateKeyEnsuresPublicly(input: GetPublicKeyFromPrivateKeyInput , output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
    {Operations.GetPublicKeyFromPrivateKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GetPublicKeyFromPrivateKey ( input: GetPublicKeyFromPrivateKeyInput )
      returns (output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetPublicKeyFromPrivateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetPublicKeyFromPrivateKeyEnsuresPublicly(input, output)
      ensures History.GetPublicKeyFromPrivateKey == old(History.GetPublicKeyFromPrivateKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GetPublicKeyFromPrivateKey(config, input);
      History.GetPublicKeyFromPrivateKey := History.GetPublicKeyFromPrivateKey + [DafnyCallEvent(input, output)];
    }

    predicate ValidatePublicKeyEnsuresPublicly(input: ValidatePublicKeyInput , output: Result<ValidatePublicKeyOutput, Error>)
    {Operations.ValidatePublicKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method ValidatePublicKey ( input: ValidatePublicKeyInput )
      returns (output: Result<ValidatePublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ValidatePublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ValidatePublicKeyEnsuresPublicly(input, output)
      ensures History.ValidatePublicKey == old(History.ValidatePublicKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.ValidatePublicKey(config, input);
      History.ValidatePublicKey := History.ValidatePublicKey + [DafnyCallEvent(input, output)];
    }

    predicate DeriveSharedSecretEnsuresPublicly(input: DeriveSharedSecretInput , output: Result<DeriveSharedSecretOutput, Error>)
    {Operations.DeriveSharedSecretEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method DeriveSharedSecret ( input: DeriveSharedSecretInput )
      returns (output: Result<DeriveSharedSecretOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DeriveSharedSecret
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DeriveSharedSecretEnsuresPublicly(input, output)
      ensures History.DeriveSharedSecret == old(History.DeriveSharedSecret) + [DafnyCallEvent(input, output)]
    {
      output := Operations.DeriveSharedSecret(config, input);
      History.DeriveSharedSecret := History.DeriveSharedSecret + [DafnyCallEvent(input, output)];
    }

    predicate CompressPublicKeyEnsuresPublicly(input: CompressPublicKeyInput , output: Result<CompressPublicKeyOutput, Error>)
    {Operations.CompressPublicKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CompressPublicKey ( input: CompressPublicKeyInput )
      returns (output: Result<CompressPublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CompressPublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CompressPublicKeyEnsuresPublicly(input, output)
      ensures History.CompressPublicKey == old(History.CompressPublicKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CompressPublicKey(config, input);
      History.CompressPublicKey := History.CompressPublicKey + [DafnyCallEvent(input, output)];
    }

    predicate DecompressPublicKeyEnsuresPublicly(input: DecompressPublicKeyInput , output: Result<DecompressPublicKeyOutput, Error>)
    {Operations.DecompressPublicKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method DecompressPublicKey ( input: DecompressPublicKeyInput )
      returns (output: Result<DecompressPublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DecompressPublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DecompressPublicKeyEnsuresPublicly(input, output)
      ensures History.DecompressPublicKey == old(History.DecompressPublicKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.DecompressPublicKey(config, input);
      History.DecompressPublicKey := History.DecompressPublicKey + [DafnyCallEvent(input, output)];
    }

    predicate ParsePublicKeyEnsuresPublicly(input: ParsePublicKeyInput , output: Result<ParsePublicKeyOutput, Error>)
    {Operations.ParsePublicKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method ParsePublicKey ( input: ParsePublicKeyInput )
      returns (output: Result<ParsePublicKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ParsePublicKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ParsePublicKeyEnsuresPublicly(input, output)
      ensures History.ParsePublicKey == old(History.ParsePublicKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.ParsePublicKey(config, input);
      History.ParsePublicKey := History.ParsePublicKey + [DafnyCallEvent(input, output)];
    }

  }
}
abstract module AbstractAwsCryptographyPrimitivesOperations {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyPrimitivesTypes
  type InternalConfig
  predicate ValidInternalConfig?(config: InternalConfig)
  function ModifiesInternalConfig(config: InternalConfig): set<object>
  predicate GenerateRandomBytesEnsuresPublicly(input: GenerateRandomBytesInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method GenerateRandomBytes ( config: InternalConfig , input: GenerateRandomBytesInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GenerateRandomBytesEnsuresPublicly(input, output)


  predicate DigestEnsuresPublicly(input: DigestInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method Digest ( config: InternalConfig , input: DigestInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures DigestEnsuresPublicly(input, output)


  // Functions are deterministic, no need for historical call events or ensures indirection
  // The private method to be refined by the library developer


  function method HMac ( config: InternalConfig , input: HMacInput )
    : (output: Result<seq<uint8>, Error>)
  // Functions that are transparent do not need ensures


  predicate HkdfExtractEnsuresPublicly(input: HkdfExtractInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method HkdfExtract ( config: InternalConfig , input: HkdfExtractInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures HkdfExtractEnsuresPublicly(input, output)


  predicate HkdfExpandEnsuresPublicly(input: HkdfExpandInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method HkdfExpand ( config: InternalConfig , input: HkdfExpandInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures HkdfExpandEnsuresPublicly(input, output)


  predicate HkdfEnsuresPublicly(input: HkdfInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method Hkdf ( config: InternalConfig , input: HkdfInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures HkdfEnsuresPublicly(input, output)


  predicate KdfCounterModeEnsuresPublicly(input: KdfCtrInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method KdfCounterMode ( config: InternalConfig , input: KdfCtrInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures KdfCounterModeEnsuresPublicly(input, output)


  predicate AesKdfCounterModeEnsuresPublicly(input: AesKdfCtrInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method AesKdfCounterMode ( config: InternalConfig , input: AesKdfCtrInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures AesKdfCounterModeEnsuresPublicly(input, output)


  predicate AESEncryptEnsuresPublicly(input: AESEncryptInput , output: Result<AESEncryptOutput, Error>)
  // The private method to be refined by the library developer


  method AESEncrypt ( config: InternalConfig , input: AESEncryptInput )
    returns (output: Result<AESEncryptOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures AESEncryptEnsuresPublicly(input, output)


  predicate AESDecryptEnsuresPublicly(input: AESDecryptInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method AESDecrypt ( config: InternalConfig , input: AESDecryptInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures AESDecryptEnsuresPublicly(input, output)


  predicate GenerateRSAKeyPairEnsuresPublicly(input: GenerateRSAKeyPairInput , output: Result<GenerateRSAKeyPairOutput, Error>)
  // The private method to be refined by the library developer


  method GenerateRSAKeyPair ( config: InternalConfig , input: GenerateRSAKeyPairInput )
    returns (output: Result<GenerateRSAKeyPairOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GenerateRSAKeyPairEnsuresPublicly(input, output)


  // Functions are deterministic, no need for historical call events or ensures indirection
  // The private method to be refined by the library developer


  function method GetRSAKeyModulusLength ( config: InternalConfig , input: GetRSAKeyModulusLengthInput )
    : (output: Result<GetRSAKeyModulusLengthOutput, Error>)
  // Functions that are transparent do not need ensures


  predicate RSADecryptEnsuresPublicly(input: RSADecryptInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method RSADecrypt ( config: InternalConfig , input: RSADecryptInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures RSADecryptEnsuresPublicly(input, output)


  predicate RSAEncryptEnsuresPublicly(input: RSAEncryptInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method RSAEncrypt ( config: InternalConfig , input: RSAEncryptInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures RSAEncryptEnsuresPublicly(input, output)


  predicate GenerateECDSASignatureKeyEnsuresPublicly(input: GenerateECDSASignatureKeyInput , output: Result<GenerateECDSASignatureKeyOutput, Error>)
  // The private method to be refined by the library developer


  method GenerateECDSASignatureKey ( config: InternalConfig , input: GenerateECDSASignatureKeyInput )
    returns (output: Result<GenerateECDSASignatureKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GenerateECDSASignatureKeyEnsuresPublicly(input, output)


  predicate ECDSASignEnsuresPublicly(input: ECDSASignInput , output: Result<seq<uint8>, Error>)
  // The private method to be refined by the library developer


  method ECDSASign ( config: InternalConfig , input: ECDSASignInput )
    returns (output: Result<seq<uint8>, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures ECDSASignEnsuresPublicly(input, output)


  predicate ECDSAVerifyEnsuresPublicly(input: ECDSAVerifyInput , output: Result<bool, Error>)
  // The private method to be refined by the library developer


  method ECDSAVerify ( config: InternalConfig , input: ECDSAVerifyInput )
    returns (output: Result<bool, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures ECDSAVerifyEnsuresPublicly(input, output)


  predicate GenerateECCKeyPairEnsuresPublicly(input: GenerateECCKeyPairInput , output: Result<GenerateECCKeyPairOutput, Error>)
  // The private method to be refined by the library developer


  method GenerateECCKeyPair ( config: InternalConfig , input: GenerateECCKeyPairInput )
    returns (output: Result<GenerateECCKeyPairOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GenerateECCKeyPairEnsuresPublicly(input, output)


  predicate GetPublicKeyFromPrivateKeyEnsuresPublicly(input: GetPublicKeyFromPrivateKeyInput , output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
  // The private method to be refined by the library developer


  method GetPublicKeyFromPrivateKey ( config: InternalConfig , input: GetPublicKeyFromPrivateKeyInput )
    returns (output: Result<GetPublicKeyFromPrivateKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GetPublicKeyFromPrivateKeyEnsuresPublicly(input, output)


  predicate ValidatePublicKeyEnsuresPublicly(input: ValidatePublicKeyInput , output: Result<ValidatePublicKeyOutput, Error>)
  // The private method to be refined by the library developer


  method ValidatePublicKey ( config: InternalConfig , input: ValidatePublicKeyInput )
    returns (output: Result<ValidatePublicKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures ValidatePublicKeyEnsuresPublicly(input, output)


  predicate DeriveSharedSecretEnsuresPublicly(input: DeriveSharedSecretInput , output: Result<DeriveSharedSecretOutput, Error>)
  // The private method to be refined by the library developer


  method DeriveSharedSecret ( config: InternalConfig , input: DeriveSharedSecretInput )
    returns (output: Result<DeriveSharedSecretOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures DeriveSharedSecretEnsuresPublicly(input, output)


  predicate CompressPublicKeyEnsuresPublicly(input: CompressPublicKeyInput , output: Result<CompressPublicKeyOutput, Error>)
  // The private method to be refined by the library developer


  method CompressPublicKey ( config: InternalConfig , input: CompressPublicKeyInput )
    returns (output: Result<CompressPublicKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures CompressPublicKeyEnsuresPublicly(input, output)


  predicate DecompressPublicKeyEnsuresPublicly(input: DecompressPublicKeyInput , output: Result<DecompressPublicKeyOutput, Error>)
  // The private method to be refined by the library developer


  method DecompressPublicKey ( config: InternalConfig , input: DecompressPublicKeyInput )
    returns (output: Result<DecompressPublicKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures DecompressPublicKeyEnsuresPublicly(input, output)


  predicate ParsePublicKeyEnsuresPublicly(input: ParsePublicKeyInput , output: Result<ParsePublicKeyOutput, Error>)
  // The private method to be refined by the library developer


  method ParsePublicKey ( config: InternalConfig , input: ParsePublicKeyInput )
    returns (output: Result<ParsePublicKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures ParsePublicKeyEnsuresPublicly(input, output)
}
