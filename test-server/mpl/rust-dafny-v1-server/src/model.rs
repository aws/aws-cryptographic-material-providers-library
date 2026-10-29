//! Native Rust mirror of the MPL TestServer operation shapes, with serde
//! renames matching each model member name and `serde_bytes` on blob members.

use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

// ─── Enums ──────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum AesWrappingAlg {
    #[serde(rename = "ALG_AES128_GCM_IV12_TAG16")]
    Aes128,
    #[serde(rename = "ALG_AES192_GCM_IV12_TAG16")]
    Aes192,
    #[serde(rename = "ALG_AES256_GCM_IV12_TAG16")]
    Aes256,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum CommitmentPolicy {
    #[serde(rename = "ESDK_FORBID_ENCRYPT_ALLOW_DECRYPT")]
    EsdkForbidEncryptAllowDecrypt,
    #[serde(rename = "ESDK_REQUIRE_ENCRYPT_ALLOW_DECRYPT")]
    EsdkRequireEncryptAllowDecrypt,
    #[serde(rename = "ESDK_REQUIRE_ENCRYPT_REQUIRE_DECRYPT")]
    EsdkRequireEncryptRequireDecrypt,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum AlgorithmSuiteId {
    #[serde(rename = "ALG_AES_128_GCM_IV12_TAG16_NO_KDF")]
    AlgAes128GcmIv12Tag16NoKdf,
    #[serde(rename = "ALG_AES_192_GCM_IV12_TAG16_NO_KDF")]
    AlgAes192GcmIv12Tag16NoKdf,
    #[serde(rename = "ALG_AES_256_GCM_IV12_TAG16_NO_KDF")]
    AlgAes256GcmIv12Tag16NoKdf,
    #[serde(rename = "ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256")]
    AlgAes128GcmIv12Tag16HkdfSha256,
    #[serde(rename = "ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256")]
    AlgAes192GcmIv12Tag16HkdfSha256,
    #[serde(rename = "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256")]
    AlgAes256GcmIv12Tag16HkdfSha256,
    #[serde(rename = "ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256")]
    AlgAes128GcmIv12Tag16HkdfSha256EcdsaP256,
    #[serde(rename = "ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384")]
    AlgAes192GcmIv12Tag16HkdfSha384EcdsaP384,
    #[serde(rename = "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384")]
    AlgAes256GcmIv12Tag16HkdfSha384EcdsaP384,
    #[serde(rename = "ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY")]
    AlgAes256GcmHkdfSha512CommitKey,
    #[serde(rename = "ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384")]
    AlgAes256GcmHkdfSha512CommitKeyEcdsaP384,
}

// ─── CreateRawAesKeyring ────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CreateRawAesKeyringRequest {
    #[serde(rename = "keyNamespace")]
    pub key_namespace: String,
    #[serde(rename = "keyName")]
    pub key_name: String,
    #[serde(rename = "wrappingKey", with = "serde_bytes")]
    pub wrapping_key: Vec<u8>,
    #[serde(rename = "wrappingAlg")]
    pub wrapping_alg: AesWrappingAlg,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CreateRawAesKeyringResponse {
    #[serde(rename = "keyringId")]
    pub keyring_id: String,
}

// ─── CreateDefaultCmm ───────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CreateDefaultCmmRequest {
    #[serde(rename = "keyringId")]
    pub keyring_id: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CreateDefaultCmmResponse {
    #[serde(rename = "cmmId")]
    pub cmm_id: String,
}

// ─── GetEncryptionMaterials ─────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GetEncryptionMaterialsRequest {
    #[serde(rename = "cmmId")]
    pub cmm_id: String,
    #[serde(rename = "encryptionContext", default)]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "commitmentPolicy")]
    pub commitment_policy: CommitmentPolicy,
    #[serde(
        rename = "algorithmSuiteId",
        default,
        skip_serializing_if = "Option::is_none"
    )]
    pub algorithm_suite_id: Option<AlgorithmSuiteId>,
    #[serde(
        rename = "maxPlaintextLength",
        default,
        skip_serializing_if = "Option::is_none"
    )]
    pub max_plaintext_length: Option<u64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GetEncryptionMaterialsResponse {
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "encryptedDataKeys")]
    pub encrypted_data_keys: Vec<EncryptedDataKeyShape>,
    #[serde(rename = "plaintextDataKey", with = "serde_bytes")]
    pub plaintext_data_key: Vec<u8>,
    #[serde(
        rename = "signingKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub signing_key: Option<Vec<u8>>,
    #[serde(
        rename = "symmetricSigningKeys",
        default,
        skip_serializing_if = "Option::is_none"
    )]
    pub symmetric_signing_keys: Option<Vec<serde_bytes::ByteBuf>>,
}

// ─── DecryptMaterials ───────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DecryptMaterialsRequest {
    #[serde(rename = "cmmId")]
    pub cmm_id: String,
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptedDataKeys")]
    pub encrypted_data_keys: Vec<EncryptedDataKeyShape>,
    #[serde(rename = "encryptionContext", default)]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "commitmentPolicy")]
    pub commitment_policy: CommitmentPolicy,
    #[serde(
        rename = "reproducedEncryptionContext",
        default,
        skip_serializing_if = "Option::is_none"
    )]
    pub reproduced_encryption_context: Option<BTreeMap<String, String>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DecryptMaterialsResponse {
    #[serde(rename = "plaintextDataKey", with = "serde_bytes")]
    pub plaintext_data_key: Vec<u8>,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(
        rename = "verificationKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub verification_key: Option<Vec<u8>>,
    #[serde(
        rename = "symmetricSigningKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub symmetric_signing_key: Option<Vec<u8>>,
}

// ─── Materials ──────────────────────────────────────────────────────────────

/// Wire form of the MPL's `EncryptionMaterials`.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EncryptionMaterialsShape {
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "encryptedDataKeys")]
    pub encrypted_data_keys: Vec<EncryptedDataKeyShape>,
    #[serde(rename = "requiredEncryptionContextKeys")]
    pub required_encryption_context_keys: Vec<String>,
    #[serde(
        rename = "plaintextDataKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub plaintext_data_key: Option<Vec<u8>>,
    #[serde(
        rename = "signingKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub signing_key: Option<Vec<u8>>,
    #[serde(
        rename = "symmetricSigningKeys",
        default,
        skip_serializing_if = "Option::is_none"
    )]
    pub symmetric_signing_keys: Option<Vec<serde_bytes::ByteBuf>>,
}

/// Wire form of the MPL's `DecryptionMaterials`.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DecryptionMaterialsShape {
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "requiredEncryptionContextKeys")]
    pub required_encryption_context_keys: Vec<String>,
    #[serde(
        rename = "plaintextDataKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub plaintext_data_key: Option<Vec<u8>>,
    #[serde(
        rename = "verificationKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub verification_key: Option<Vec<u8>>,
    #[serde(
        rename = "symmetricSigningKey",
        default,
        skip_serializing_if = "Option::is_none",
        with = "serde_bytes_opt"
    )]
    pub symmetric_signing_key: Option<Vec<u8>>,
}

// ─── InitializeEncryptionMaterials / InitializeDecryptionMaterials ──────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InitializeEncryptionMaterialsRequest {
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "requiredEncryptionContextKeys")]
    pub required_encryption_context_keys: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InitializeEncryptionMaterialsResponse {
    pub materials: EncryptionMaterialsShape,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InitializeDecryptionMaterialsRequest {
    #[serde(rename = "algorithmSuiteId")]
    pub algorithm_suite_id: AlgorithmSuiteId,
    #[serde(rename = "encryptionContext")]
    pub encryption_context: BTreeMap<String, String>,
    #[serde(rename = "requiredEncryptionContextKeys")]
    pub required_encryption_context_keys: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InitializeDecryptionMaterialsResponse {
    pub materials: DecryptionMaterialsShape,
}

// ─── OnEncrypt / OnDecrypt ──────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OnEncryptRequest {
    #[serde(rename = "keyringId")]
    pub keyring_id: String,
    pub materials: EncryptionMaterialsShape,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OnEncryptResponse {
    pub materials: EncryptionMaterialsShape,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OnDecryptRequest {
    #[serde(rename = "keyringId")]
    pub keyring_id: String,
    pub materials: DecryptionMaterialsShape,
    #[serde(rename = "encryptedDataKeys")]
    pub encrypted_data_keys: Vec<EncryptedDataKeyShape>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OnDecryptResponse {
    pub materials: DecryptionMaterialsShape,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EncryptedDataKeyShape {
    #[serde(rename = "keyProviderId")]
    pub key_provider_id: String,
    #[serde(rename = "keyProviderInfo", with = "serde_bytes")]
    pub key_provider_info: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub ciphertext: Vec<u8>,
}

/// `serde_bytes` for `Option<Vec<u8>>` blob members.
mod serde_bytes_opt {
    use serde::{Deserialize, Deserializer, Serializer};

    pub fn serialize<S: Serializer>(v: &Option<Vec<u8>>, s: S) -> Result<S::Ok, S::Error> {
        match v {
            Some(bytes) => s.serialize_bytes(bytes),
            None => s.serialize_none(),
        }
    }

    pub fn deserialize<'de, D: Deserializer<'de>>(d: D) -> Result<Option<Vec<u8>>, D::Error> {
        let opt: Option<serde_bytes::ByteBuf> = Option::deserialize(d)?;
        Ok(opt.map(serde_bytes::ByteBuf::into_vec))
    }
}
