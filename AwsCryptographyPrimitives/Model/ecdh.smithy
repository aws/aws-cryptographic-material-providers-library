namespace aws.cryptography.primitives

@documentation("Supported ECDH Curve specifications.")
@enum([
  {
    name: "ECC_NIST_P256",
    value: "ECC_NIST_P256",
  },
  {
    name: "ECC_NIST_P384",
    value: "ECC_NIST_P384",
  },
  {
    name: "ECC_NIST_P521",
    value: "ECC_NIST_P521",
  },
  {
    name: "SM2",
    value: "SM2",
  },
])
string ECDHCurveSpec

operation GenerateECCKeyPair {
    input: GenerateECCKeyPairInput,
    output: GenerateECCKeyPairOutput,
    errors: []
}

operation GetPublicKeyFromPrivateKey {
    input: GetPublicKeyFromPrivateKeyInput,
    output: GetPublicKeyFromPrivateKeyOutput,
    errors: []
}

operation ValidatePublicKey {
    input: ValidatePublicKeyInput,
    output: ValidatePublicKeyOutput,
    errors: []
}

operation DeriveSharedSecret {
    input: DeriveSharedSecretInput,
    output: DeriveSharedSecretOutput,
    errors: []
}

operation CompressPublicKey {
    input: CompressPublicKeyInput,
    output: CompressPublicKeyOutput,
    errors: []
}

operation DecompressPublicKey {
    input: DecompressPublicKeyInput,
    output: DecompressPublicKeyOutput,
    errors: []
}

operation ParsePublicKey {
    input: ParsePublicKeyInput,
    output: ParsePublicKeyOutput,
    errors: []
}

structure GenerateECCKeyPairInput {
    @required
    eccCurve: ECDHCurveSpec 
}

structure GenerateECCKeyPairOutput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    privateKey: ECCPrivateKey,
    @required
    publicKey: ECCPublicKey 
}

structure GetPublicKeyFromPrivateKeyInput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    privateKey: ECCPrivateKey,
}

structure GetPublicKeyFromPrivateKeyOutput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    privateKey: ECCPrivateKey,
    @required
    publicKey: Blob 
}

structure ValidatePublicKeyInput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    publicKey: Blob 
}

structure ValidatePublicKeyOutput {
    @required
    success: Boolean,
}

structure DeriveSharedSecretInput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    privateKey: ECCPrivateKey,
    @required
    publicKey: ECCPublicKey 
}

structure DeriveSharedSecretOutput {
    @required
    sharedSecret: Blob
}

structure CompressPublicKeyInput {
    @required
    publicKey: ECCPublicKey,
    @required
    eccCurve: ECDHCurveSpec
}

structure CompressPublicKeyOutput {
    @required
    compressedPublicKey: Blob
} 

structure DecompressPublicKeyInput {
    @required
    compressedPublicKey: Blob,
    @required
    eccCurve: ECDHCurveSpec
}

structure DecompressPublicKeyOutput {
    @required
    publicKey: ECCPublicKey
}

structure ECCPrivateKey {
    @required
    pem: Blob
}

structure ECCPublicKey {
    @required
    der: Blob
}

structure ParsePublicKeyInput {
    @required
    publicKey: Blob
}

structure ParsePublicKeyOutput {
    @required
    publicKey: ECCPublicKey
}
