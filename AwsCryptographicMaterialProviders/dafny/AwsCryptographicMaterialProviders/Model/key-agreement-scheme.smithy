namespace aws.cryptography.materialProviders

use aws.polymorph#javadoc

// Key Agreement Schemes
@javadoc("Supported ECDH Key Agreement Schemes.")
union KeyAgreementScheme {
    StaticConfiguration: StaticConfigurations
}

@javadoc("Supported configurations for the StaticConfiguration Key Agreement Scheme.")
union StaticConfigurations {
    AWS_KMS_ECDH: KmsEcdhStaticConfigurations,
    RAW_ECDH: RawEcdhStaticConfigurations
}

@javadoc("Allowed configurations when using KmsEcdhStaticConfigurations.")
union KmsEcdhStaticConfigurations {
    KmsPublicKeyDiscovery: KmsPublicKeyDiscoveryInput,
    KmsPrivateKeyToStaticPublicKey: KmsPrivateKeyToStaticPublicKeyInput,
}

@javadoc("List of configurations when using RawEcdhStaticConfigurations.")
union RawEcdhStaticConfigurations {
    PublicKeyDiscovery: PublicKeyDiscoveryInput,
    RawPrivateKeyToStaticPublicKey: RawPrivateKeyToStaticPublicKeyInput,
    EphemeralPrivateKeyToStaticPublicKey: EphemeralPrivateKeyToStaticPublicKeyInput 
}


@javadoc("Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.")
structure KmsPublicKeyDiscoveryInput {
    @required
    @javadoc("AWS KMS key identifier belonging to the recipient.")
    recipientKmsIdentifier: KmsKeyId
}

@javadoc("Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.")
structure KmsPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("AWS KMS Key Identifier belonging to the sender.")
    senderKmsIdentifier: KmsKeyId,
    @javadoc("Sender Public Key. This is the raw public ECC key in DER format that belongs to the senderKmsIdentifier.")
    senderPublicKey: Blob,
    @required
    @javadoc("Recipient Public Key. This MUST be a raw public ECC key in DER format.")
    recipientPublicKey: Blob,
}

@javadoc("Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.")
structure EphemeralPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("The recipient's public key. MUST be DER encoded.")
    recipientPublicKey: Blob,
}

@javadoc("Inputs for creating a PublicKeyDiscovery Configuration.")
structure PublicKeyDiscoveryInput {
    @required
    @javadoc("The sender's private key. MUST be PEM encoded.")
    recipientStaticPrivateKey: Blob,
}

@javadoc("Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.")
structure RawPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("The sender's private key. MUST be PEM encoded.")
    senderStaticPrivateKey: Blob,
    @required
    @javadoc("The recipient's public key. MUST be DER encoded.")
    recipientPublicKey: Blob,
}
