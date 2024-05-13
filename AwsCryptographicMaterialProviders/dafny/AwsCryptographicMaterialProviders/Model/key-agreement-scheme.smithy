namespace aws.cryptography.materialProviders

use aws.polymorph#javadoc

// Key Agreement Schemes
@javadoc("Supported ECDH KeyAgreement Schemes")
union KeyAgreementScheme {
    StaticConfiguration: StaticConfigurations
}

@javadoc("Supported configurations for the StaticConfiguration Key Agreement Scheme")
union StaticConfigurations {
    AWS_KMS_ECDH: KmsEcdhStaticConfigurations,
    RAW_ECDH: RawEcdhStaticConfigurations
}

@javadoc("Allowed configurations when using a KmsEcdhStaticConfigurations")
union KmsEcdhStaticConfigurations {
    KmsPublicKeyDiscovery: KmsPublicKeyDiscoveryInput,
    KmsPrivateKeyToStaticPublicKey: KmsPrivateKeyToStaticPublicKeyInput,
}

@javadoc("List of configurations when using a RawEcdhStaticConfigurations")
union RawEcdhStaticConfigurations {
    PublicKeyDiscovery: PublicKeyDiscoveryInput,
    RawPrivateKeyToStaticPublicKey: RawPrivateKeyToStaticPublicKeyInput,
    EphemeralPrivateKeyToStaticPublicKey: EphemeralPrivateKeyToStaticPublicKeyInput 
}

union KmsRecipientConfiguration {
    RecipientKmsKeyId: KmsKeyId,
    RecipientPublicKey: Secret
}


@javadoc("Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration")
structure KmsPublicKeyDiscoveryInput {
    @required
    @javadoc("AWS KMS key identifier belonging to the recipient")
    recipientKmsIdentifier: KmsKeyId
}

@javadoc("Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.")
structure KmsPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("AWS KMS Key Identifier belonging to the sender")
    senderKmsIdentifier: KmsKeyId,
    @required
    @javadoc("Recipient configuration. This can be either a KMS key identifier or a raw public key")
    recipientConfiguration: KmsRecipientConfiguration,
}

@javadoc("Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.")
structure EphemeralPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("The recipient's public key")
    recipientPublicKey: Secret,
}

@javadoc("Inputs for creating a PublicKeyDiscovery Configuration.")
structure PublicKeyDiscoveryInput {
    @required
    @javadoc("The sender's private key")
    senderStaticPrivateKey: Secret,
}

@javadoc("Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.")
structure RawPrivateKeyToStaticPublicKeyInput {
    @required
    @javadoc("The sender's private key")
    senderStaticPrivateKey: Secret,
    @required
    @javadoc("The recipient's public key")
    recipientPublicKey: Secret,
}
