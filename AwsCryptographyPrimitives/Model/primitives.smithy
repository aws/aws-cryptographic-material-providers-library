namespace aws.cryptography.primitives

@range(min: 0)
integer PositiveInteger

@aws.polymorph#localService(
  sdkId: "AtomicPrimitives",
  config: CryptoConfig,
)
service AwsCryptographicPrimitives {
  version: "2020-10-24",
  operations: [
    GenerateRandomBytes,
    Digest,
    HMac,
    HkdfExtract,
    HkdfExpand,
    Hkdf,
    KdfCounterMode,
    AesKdfCounterMode,
    AESEncrypt,
    AESDecrypt,
    GenerateRSAKeyPair,
    GetRSAKeyModulusLength,
    RSADecrypt,
    RSAEncrypt,
    GenerateECDSASignatureKey,
    ECDSASign,
    ECDSAVerify,
    GenerateECCKeyPair,
    GetPublicKeyFromPrivateKey,
    ValidatePublicKey,
    DeriveSharedSecret,
    CompressPublicKey,
    DecompressPublicKey,
    ParsePublicKey
  ],
  errors: [AwsCryptographicPrimitivesError]
}

structure CryptoConfig {}

///////////////////
// Errors

@error("client")
structure AwsCryptographicPrimitivesError {
  @required
  message: String,
}
