//! Native Rust mirror of the Primitives TestServer operation shapes, with serde
//! renames matching each model member name and `serde_bytes` on blob members so
//! they travel as CBOR byte strings (rpcv2Cbor), not arrays.

use serde::{Deserialize, Serialize};

// ─── Enums ──────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum AesAlgorithm {
    #[serde(rename = "AES_128_GCM")]
    Aes128Gcm,
    #[serde(rename = "AES_192_GCM")]
    Aes192Gcm,
    #[serde(rename = "AES_256_GCM")]
    Aes256Gcm,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum DigestAlgorithm {
    #[serde(rename = "SHA_256")]
    Sha256,
    #[serde(rename = "SHA_384")]
    Sha384,
    #[serde(rename = "SHA_512")]
    Sha512,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum EcdsaAlgorithm {
    #[serde(rename = "ECDSA_P256")]
    EcdsaP256,
    #[serde(rename = "ECDSA_P384")]
    EcdsaP384,
}

// ─── AES ────────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AesEncryptRequest {
    pub algorithm: AesAlgorithm,
    #[serde(with = "serde_bytes")]
    pub iv: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub key: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub message: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub aad: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AesEncryptResponse {
    #[serde(with = "serde_bytes")]
    pub ciphertext: Vec<u8>,
    #[serde(rename = "authTag", with = "serde_bytes")]
    pub auth_tag: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AesDecryptRequest {
    pub algorithm: AesAlgorithm,
    #[serde(with = "serde_bytes")]
    pub key: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub ciphertext: Vec<u8>,
    #[serde(rename = "authTag", with = "serde_bytes")]
    pub auth_tag: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub iv: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub aad: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AesDecryptResponse {
    #[serde(with = "serde_bytes")]
    pub plaintext: Vec<u8>,
}

// ─── Random ─────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerateRandomBytesRequest {
    pub length: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerateRandomBytesResponse {
    #[serde(with = "serde_bytes")]
    pub data: Vec<u8>,
}

// ─── Digest ─────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DigestRequest {
    pub algorithm: DigestAlgorithm,
    #[serde(with = "serde_bytes")]
    pub data: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DigestResponse {
    #[serde(with = "serde_bytes")]
    pub digest: Vec<u8>,
}

// ─── HMAC ───────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HmacRequest {
    pub algorithm: DigestAlgorithm,
    #[serde(with = "serde_bytes")]
    pub key: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub message: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HmacResponse {
    #[serde(with = "serde_bytes")]
    pub digest: Vec<u8>,
}

// ─── HKDF ───────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HkdfRequest {
    pub algorithm: DigestAlgorithm,
    #[serde(with = "serde_bytes")]
    pub salt: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub ikm: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub info: Vec<u8>,
    #[serde(rename = "expectedLength")]
    pub expected_length: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HkdfResponse {
    #[serde(with = "serde_bytes")]
    pub okm: Vec<u8>,
}

// ─── KBKDF-CTR-HMAC ────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct KbkdfCtrHmacRequest {
    pub algorithm: DigestAlgorithm,
    #[serde(with = "serde_bytes")]
    pub ikm: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub info: Vec<u8>,
    #[serde(rename = "expectedLength")]
    pub expected_length: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct KbkdfCtrHmacResponse {
    #[serde(with = "serde_bytes")]
    pub okm: Vec<u8>,
}

// ─── ECDSA ──────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaGenerateKeyPairRequest {
    pub algorithm: EcdsaAlgorithm,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaGenerateKeyPairResponse {
    #[serde(rename = "verificationKey", with = "serde_bytes")]
    pub verification_key: Vec<u8>,
    #[serde(rename = "signingKey", with = "serde_bytes")]
    pub signing_key: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaSignRequest {
    pub algorithm: EcdsaAlgorithm,
    #[serde(rename = "signingKey", with = "serde_bytes")]
    pub signing_key: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub message: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaSignResponse {
    #[serde(with = "serde_bytes")]
    pub signature: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaVerifyRequest {
    pub algorithm: EcdsaAlgorithm,
    #[serde(rename = "verificationKey", with = "serde_bytes")]
    pub verification_key: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub message: Vec<u8>,
    #[serde(with = "serde_bytes")]
    pub signature: Vec<u8>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EcdsaVerifyResponse {
    pub valid: bool,
}
