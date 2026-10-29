//! Operation handlers — dispatch to the Dafny-generated AtomicPrimitives client.

use std::sync::OnceLock;

use aws_mpl_legacy::aws_cryptography_primitives::client::Client;
use aws_mpl_legacy::aws_cryptography_primitives::types::crypto_config::CryptoConfig;
use aws_mpl_legacy::aws_cryptography_primitives::types::error::Error;
use aws_mpl_legacy::aws_cryptography_primitives::types::{
    AesGcm, DigestAlgorithm as DafnyDigest, EcdsaSignatureAlgorithm,
};
use aws_smithy_types::Blob;

use crate::error::ServerError;
use crate::model::*;

fn client() -> &'static Client {
    static CLIENT: OnceLock<Client> = OnceLock::new();
    CLIENT.get_or_init(|| {
        Client::from_conf(CryptoConfig::builder().build().expect("CryptoConfig"))
            .expect("AtomicPrimitives client")
    })
}

fn prim_err(e: Error) -> ServerError {
    ServerError::primitives(e.to_string())
}

fn missing(field: &str) -> ServerError {
    ServerError::primitives(format!("AtomicPrimitives returned no {field}"))
}

fn blob(bytes: Vec<u8>) -> Blob {
    Blob::new(bytes)
}

fn aes_gcm(alg: AesAlgorithm) -> AesGcm {
    let key_length = match alg {
        AesAlgorithm::Aes128Gcm => 16,
        AesAlgorithm::Aes192Gcm => 24,
        AesAlgorithm::Aes256Gcm => 32,
    };
    AesGcm::builder()
        .key_length(key_length)
        .tag_length(16)
        .iv_length(12)
        .build()
        .expect("AesGcm")
}

fn digest_alg(alg: DigestAlgorithm) -> DafnyDigest {
    match alg {
        DigestAlgorithm::Sha256 => DafnyDigest::Sha256,
        DigestAlgorithm::Sha384 => DafnyDigest::Sha384,
        DigestAlgorithm::Sha512 => DafnyDigest::Sha512,
    }
}

fn ecdsa_alg(alg: EcdsaAlgorithm) -> EcdsaSignatureAlgorithm {
    match alg {
        EcdsaAlgorithm::EcdsaP256 => EcdsaSignatureAlgorithm::EcdsaP256,
        EcdsaAlgorithm::EcdsaP384 => EcdsaSignatureAlgorithm::EcdsaP384,
    }
}

fn to_i32(value: u32, field: &str) -> Result<i32, ServerError> {
    i32::try_from(value).map_err(|_| ServerError::generic(format!("{field} out of range")))
}

// ─── AES ────────────────────────────────────────────────────────────────────

pub async fn aes_encrypt(req: AesEncryptRequest) -> Result<AesEncryptResponse, ServerError> {
    let out = client()
        .aes_encrypt()
        .enc_alg(aes_gcm(req.algorithm))
        .iv(blob(req.iv))
        .key(blob(req.key))
        .msg(blob(req.message))
        .aad(blob(req.aad))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(AesEncryptResponse {
        ciphertext: out
            .cipher_text
            .ok_or_else(|| missing("cipherText"))?
            .into_inner(),
        auth_tag: out.auth_tag.ok_or_else(|| missing("authTag"))?.into_inner(),
    })
}

pub async fn aes_decrypt(req: AesDecryptRequest) -> Result<AesDecryptResponse, ServerError> {
    let plaintext = client()
        .aes_decrypt()
        .enc_alg(aes_gcm(req.algorithm))
        .key(blob(req.key))
        .cipher_txt(blob(req.ciphertext))
        .auth_tag(blob(req.auth_tag))
        .iv(blob(req.iv))
        .aad(blob(req.aad))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(AesDecryptResponse {
        plaintext: plaintext.into_inner(),
    })
}

// ─── Random ─────────────────────────────────────────────────────────────────

pub async fn generate_random_bytes(
    req: GenerateRandomBytesRequest,
) -> Result<GenerateRandomBytesResponse, ServerError> {
    let data = client()
        .generate_random_bytes()
        .length(to_i32(req.length, "length")?)
        .send()
        .await
        .map_err(prim_err)?;
    Ok(GenerateRandomBytesResponse {
        data: data.into_inner(),
    })
}

// ─── Digest / HMAC / HKDF ───────────────────────────────────────────────────

pub async fn digest(req: DigestRequest) -> Result<DigestResponse, ServerError> {
    let digest = client()
        .digest()
        .digest_algorithm(digest_alg(req.algorithm))
        .message(blob(req.data))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(DigestResponse {
        digest: digest.into_inner(),
    })
}

pub async fn hmac(req: HmacRequest) -> Result<HmacResponse, ServerError> {
    let digest = client()
        .h_mac()
        .digest_algorithm(digest_alg(req.algorithm))
        .key(blob(req.key))
        .message(blob(req.message))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(HmacResponse {
        digest: digest.into_inner(),
    })
}

pub async fn hkdf(req: HkdfRequest) -> Result<HkdfResponse, ServerError> {
    let okm = client()
        .hkdf()
        .digest_algorithm(digest_alg(req.algorithm))
        .salt(blob(req.salt))
        .ikm(blob(req.ikm))
        .info(blob(req.info))
        .expected_length(to_i32(req.expected_length, "expectedLength")?)
        .send()
        .await
        .map_err(prim_err)?;
    Ok(HkdfResponse {
        okm: okm.into_inner(),
    })
}

// ─── KBKDF-CTR-HMAC ────────────────────────────────────────────────────────

/// AtomicPrimitives' KdfCounterMode builds its own fixed input from
/// `purpose` and `nonce`, so it cannot derive from the model's verbatim `info`.
pub async fn kbkdf_ctr_hmac(
    _req: KbkdfCtrHmacRequest,
) -> Result<KbkdfCtrHmacResponse, ServerError> {
    Err(ServerError::generic(
        "KbkdfCtrHmac is not supported by this Language_Server",
    ))
}

// ─── ECDSA ──────────────────────────────────────────────────────────────────

pub async fn ecdsa_generate_key_pair(
    req: EcdsaGenerateKeyPairRequest,
) -> Result<EcdsaGenerateKeyPairResponse, ServerError> {
    let out = client()
        .generate_ecdsa_signature_key()
        .signature_algorithm(ecdsa_alg(req.algorithm))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(EcdsaGenerateKeyPairResponse {
        verification_key: out
            .verification_key
            .ok_or_else(|| missing("verificationKey"))?
            .into_inner(),
        signing_key: out
            .signing_key
            .ok_or_else(|| missing("signingKey"))?
            .into_inner(),
    })
}

pub async fn ecdsa_sign(req: EcdsaSignRequest) -> Result<EcdsaSignResponse, ServerError> {
    let signature = client()
        .ecdsa_sign()
        .signature_algorithm(ecdsa_alg(req.algorithm))
        .signing_key(blob(req.signing_key))
        .message(blob(req.message))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(EcdsaSignResponse {
        signature: signature.into_inner(),
    })
}

pub async fn ecdsa_verify(req: EcdsaVerifyRequest) -> Result<EcdsaVerifyResponse, ServerError> {
    let valid = client()
        .ecdsa_verify()
        .signature_algorithm(ecdsa_alg(req.algorithm))
        .verification_key(blob(req.verification_key))
        .message(blob(req.message))
        .signature(blob(req.signature))
        .send()
        .await
        .map_err(prim_err)?;
    Ok(EcdsaVerifyResponse { valid })
}
