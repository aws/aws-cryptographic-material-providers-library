namespace aws.cryptography.primitives

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
    // TODO: come back and double check this is the spec kms uses
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

structure GenerateECCKeyPairInput {
    @required
    eccCurve: ECDHCurveSpec 
}

structure GenerateECCKeyPairOutput {
    @required
    eccCurve: ECDHCurveSpec,
    @required
    privateKey: Blob,
    @required
    publicKey: Blob 
}

structure GetPublicKeyFromPrivateKeyInput {
    @required
    privateKey: Blob,
}

structure GetPublicKeyFromPrivateKeyOutput {
    @required
    privateKey: Blob,
    @required
    publicKey: Blob 
}

structure ValidatePublicKeyInput {
    @required
    privateKey: Blob,
    @required
    publicKey: Blob 
}

structure ValidatePublicKeyOutput {
    @required
    success: Boolean,
}

structure DeriveSharedSecretInput {
    @required
    privateKey: Blob,
    @required
    publicKey: Blob 
}

structure DeriveSharedSecretOutput {
    @required
    sharedSecret: Blob
}
