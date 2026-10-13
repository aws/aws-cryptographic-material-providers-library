//! Operation handlers and multi-type object registry, delegating to the
//! Dafny-generated Rust MaterialProviders client (`aws-mpl-legacy`).
//!
//! Keyrings and CMMs are held in typed registries behind UUID handles; a handle
//! is only looked up in the registry of the kind the operation expects. A
//! library failure becomes an `MPLClientError`; a malformed request or bad
//! handle a `GenericServerError`.

use std::collections::{BTreeMap, HashMap};
use std::sync::Mutex;

use aws_mpl_legacy::client::Client;
use aws_mpl_legacy::types::cryptographic_materials_manager::CryptographicMaterialsManagerRef;
use aws_mpl_legacy::types::keyring::KeyringRef;
use aws_mpl_legacy::types::{
    AesWrappingAlg as DafnyAesWrappingAlg, AlgorithmSuiteId as DafnyAlgorithmSuiteId,
    AlgorithmSuiteInfo, CommitmentPolicy as DafnyCommitmentPolicy, DecryptionMaterials,
    EncryptedDataKey, EncryptionMaterials, EsdkAlgorithmSuiteId, EsdkCommitmentPolicy,
    MaterialProvidersConfig,
};
use aws_smithy_types::Blob;

use crate::error::ServerError;
use crate::model::*;

// The Dafny-generated crate has a shared `types` materials struct and an
// operation-level copy with the same public members (returned by
// Initialize*Materials); these macros read either.
macro_rules! encryption_materials_to_shape {
    ($materials:expr) => {{
        let materials = $materials;
        Ok::<_, ServerError>(EncryptionMaterialsShape {
            algorithm_suite_id: suite_of(
                materials
                    .algorithm_suite
                    .as_ref()
                    .and_then(|i| i.id.as_ref()),
            )?,
            encryption_context: to_btree_map(materials.encryption_context.clone()),
            encrypted_data_keys: edks_to_shapes(materials.encrypted_data_keys.clone()),
            required_encryption_context_keys: materials
                .required_encryption_context_keys
                .clone()
                .unwrap_or_default(),
            plaintext_data_key: materials.plaintext_data_key.clone().map(Blob::into_inner),
            signing_key: materials.signing_key.clone().map(Blob::into_inner),
            symmetric_signing_keys: materials.symmetric_signing_keys.clone().map(|keys| {
                keys.into_iter()
                    .map(|k| serde_bytes::ByteBuf::from(k.into_inner()))
                    .collect()
            }),
        })
    }};
}

macro_rules! decryption_materials_to_shape {
    ($materials:expr) => {{
        let materials = $materials;
        Ok::<_, ServerError>(DecryptionMaterialsShape {
            algorithm_suite_id: suite_of(
                materials
                    .algorithm_suite
                    .as_ref()
                    .and_then(|i| i.id.as_ref()),
            )?,
            encryption_context: to_btree_map(materials.encryption_context.clone()),
            required_encryption_context_keys: materials
                .required_encryption_context_keys
                .clone()
                .unwrap_or_default(),
            plaintext_data_key: materials.plaintext_data_key.clone().map(Blob::into_inner),
            verification_key: materials.verification_key.clone().map(Blob::into_inner),
            symmetric_signing_key: materials
                .symmetric_signing_key
                .clone()
                .map(Blob::into_inner),
        })
    }};
}

/// Shared server state: the MPL client plus typed registries.
pub struct AppState {
    client: Client,
    /// AlgorithmSuiteInfo per entry of `ESDK_SUITES`, in the same order.
    suite_info: Vec<AlgorithmSuiteInfo>,
    keyrings: Mutex<HashMap<String, KeyringRef>>,
    cmms: Mutex<HashMap<String, CryptographicMaterialsManagerRef>>,
}

/// Every ESDK suite with its two-byte message-format id, for
/// `GetAlgorithmSuiteInfo`.
const ESDK_SUITES: [(AlgorithmSuiteId, EsdkAlgorithmSuiteId, [u8; 2]); 11] = [
    (
        AlgorithmSuiteId::AlgAes128GcmIv12Tag16NoKdf,
        EsdkAlgorithmSuiteId::AlgAes128GcmIv12Tag16NoKdf,
        [0x00, 0x14],
    ),
    (
        AlgorithmSuiteId::AlgAes192GcmIv12Tag16NoKdf,
        EsdkAlgorithmSuiteId::AlgAes192GcmIv12Tag16NoKdf,
        [0x00, 0x46],
    ),
    (
        AlgorithmSuiteId::AlgAes256GcmIv12Tag16NoKdf,
        EsdkAlgorithmSuiteId::AlgAes256GcmIv12Tag16NoKdf,
        [0x00, 0x78],
    ),
    (
        AlgorithmSuiteId::AlgAes128GcmIv12Tag16HkdfSha256,
        EsdkAlgorithmSuiteId::AlgAes128GcmIv12Tag16HkdfSha256,
        [0x01, 0x14],
    ),
    (
        AlgorithmSuiteId::AlgAes192GcmIv12Tag16HkdfSha256,
        EsdkAlgorithmSuiteId::AlgAes192GcmIv12Tag16HkdfSha256,
        [0x01, 0x46],
    ),
    (
        AlgorithmSuiteId::AlgAes256GcmIv12Tag16HkdfSha256,
        EsdkAlgorithmSuiteId::AlgAes256GcmIv12Tag16HkdfSha256,
        [0x01, 0x78],
    ),
    (
        AlgorithmSuiteId::AlgAes128GcmIv12Tag16HkdfSha256EcdsaP256,
        EsdkAlgorithmSuiteId::AlgAes128GcmIv12Tag16HkdfSha256EcdsaP256,
        [0x02, 0x14],
    ),
    (
        AlgorithmSuiteId::AlgAes192GcmIv12Tag16HkdfSha384EcdsaP384,
        EsdkAlgorithmSuiteId::AlgAes192GcmIv12Tag16HkdfSha384EcdsaP384,
        [0x03, 0x46],
    ),
    (
        AlgorithmSuiteId::AlgAes256GcmIv12Tag16HkdfSha384EcdsaP384,
        EsdkAlgorithmSuiteId::AlgAes256GcmIv12Tag16HkdfSha384EcdsaP384,
        [0x03, 0x78],
    ),
    (
        AlgorithmSuiteId::AlgAes256GcmHkdfSha512CommitKey,
        EsdkAlgorithmSuiteId::AlgAes256GcmHkdfSha512CommitKey,
        [0x04, 0x78],
    ),
    (
        AlgorithmSuiteId::AlgAes256GcmHkdfSha512CommitKeyEcdsaP384,
        EsdkAlgorithmSuiteId::AlgAes256GcmHkdfSha512CommitKeyEcdsaP384,
        [0x05, 0x78],
    ),
];

fn mpl_err(e: impl std::fmt::Display) -> ServerError {
    ServerError::mpl(e.to_string())
}

impl AppState {
    /// Build the client and resolve every suite's AlgorithmSuiteInfo once.
    pub async fn new() -> Self {
        let client = Client::from_conf(
            MaterialProvidersConfig::builder()
                .build()
                .expect("MaterialProvidersConfig"),
        )
        .expect("MaterialProviders client");
        let mut suite_info = Vec::with_capacity(ESDK_SUITES.len());
        for (_, esdk, binary) in ESDK_SUITES {
            let info = client
                .get_algorithm_suite_info()
                .binary_id(Blob::new(binary.to_vec()))
                .send()
                .await
                .expect("GetAlgorithmSuiteInfo");
            assert_eq!(
                info.id,
                Some(DafnyAlgorithmSuiteId::Esdk(esdk)),
                "binary id table entry for {esdk:?}"
            );
            // The operation returns its own AlgorithmSuiteInfo type; materials
            // carry the shared `types` one, with the same members.
            suite_info.push(
                AlgorithmSuiteInfo::builder()
                    .set_id(info.id)
                    .set_binary_id(info.binary_id)
                    .set_message_version(info.message_version)
                    .set_encrypt(info.encrypt)
                    .set_kdf(info.kdf)
                    .set_commitment(info.commitment)
                    .set_signature(info.signature)
                    .set_symmetric_signature(info.symmetric_signature)
                    .set_edk_wrapping(info.edk_wrapping)
                    .build()
                    .expect("AlgorithmSuiteInfo"),
            );
        }
        Self {
            client,
            suite_info,
            keyrings: Mutex::new(HashMap::new()),
            cmms: Mutex::new(HashMap::new()),
        }
    }

    // ─── Construction ───────────────────────────────────────────────────────

    pub async fn create_raw_aes_keyring(
        &self,
        req: CreateRawAesKeyringRequest,
    ) -> Result<CreateRawAesKeyringResponse, ServerError> {
        let alg = match req.wrapping_alg {
            AesWrappingAlg::Aes128 => DafnyAesWrappingAlg::AlgAes128GcmIv12Tag16,
            AesWrappingAlg::Aes192 => DafnyAesWrappingAlg::AlgAes192GcmIv12Tag16,
            AesWrappingAlg::Aes256 => DafnyAesWrappingAlg::AlgAes256GcmIv12Tag16,
        };
        let keyring = self
            .client
            .create_raw_aes_keyring()
            .key_namespace(req.key_namespace)
            .key_name(req.key_name)
            .wrapping_key(Blob::new(req.wrapping_key))
            .wrapping_alg(alg)
            .send()
            .await
            .map_err(mpl_err)?;
        let id = uuid::Uuid::new_v4().to_string();
        self.keyrings
            .lock()
            .expect("keyrings mutex")
            .insert(id.clone(), keyring);
        Ok(CreateRawAesKeyringResponse { keyring_id: id })
    }

    pub async fn create_default_cmm(
        &self,
        req: CreateDefaultCmmRequest,
    ) -> Result<CreateDefaultCmmResponse, ServerError> {
        let keyring = self.get_keyring(&req.keyring_id)?;
        let cmm = self
            .client
            .create_default_cryptographic_materials_manager()
            .keyring(keyring)
            .send()
            .await
            .map_err(mpl_err)?;
        let id = uuid::Uuid::new_v4().to_string();
        self.cmms
            .lock()
            .expect("cmms mutex")
            .insert(id.clone(), cmm);
        Ok(CreateDefaultCmmResponse { cmm_id: id })
    }

    // ─── Materials initialization + keyring interface ───────────────────────

    pub async fn initialize_encryption_materials(
        &self,
        req: InitializeEncryptionMaterialsRequest,
    ) -> Result<InitializeEncryptionMaterialsResponse, ServerError> {
        let materials = self
            .client
            .initialize_encryption_materials()
            .algorithm_suite_id(suite_id(req.algorithm_suite_id))
            .encryption_context(to_hash_map(req.encryption_context))
            .required_encryption_context_keys(req.required_encryption_context_keys)
            .send()
            .await
            .map_err(mpl_err)?;
        Ok(InitializeEncryptionMaterialsResponse {
            materials: encryption_materials_to_shape!(&materials)?,
        })
    }

    pub async fn initialize_decryption_materials(
        &self,
        req: InitializeDecryptionMaterialsRequest,
    ) -> Result<InitializeDecryptionMaterialsResponse, ServerError> {
        let materials = self
            .client
            .initialize_decryption_materials()
            .algorithm_suite_id(suite_id(req.algorithm_suite_id))
            .encryption_context(to_hash_map(req.encryption_context))
            .required_encryption_context_keys(req.required_encryption_context_keys)
            .send()
            .await
            .map_err(mpl_err)?;
        Ok(InitializeDecryptionMaterialsResponse {
            materials: decryption_materials_to_shape!(&materials)?,
        })
    }

    pub async fn on_encrypt(
        &self,
        req: OnEncryptRequest,
    ) -> Result<OnEncryptResponse, ServerError> {
        let keyring = self.get_keyring(&req.keyring_id)?;
        let materials = self.shape_to_encryption_materials(req.materials);
        let output = keyring
            .on_encrypt()
            .materials(materials)
            .send()
            .await
            .map_err(mpl_err)?;
        let materials = output
            .materials
            .ok_or_else(|| ServerError::mpl("OnEncrypt returned no materials"))?;
        Ok(OnEncryptResponse {
            materials: encryption_materials_to_shape!(&materials)?,
        })
    }

    pub async fn on_decrypt(
        &self,
        req: OnDecryptRequest,
    ) -> Result<OnDecryptResponse, ServerError> {
        let keyring = self.get_keyring(&req.keyring_id)?;
        let materials = self.shape_to_decryption_materials(req.materials);
        let output = keyring
            .on_decrypt()
            .materials(materials)
            .encrypted_data_keys(edks_from_shapes(req.encrypted_data_keys))
            .send()
            .await
            .map_err(mpl_err)?;
        let materials = output
            .materials
            .ok_or_else(|| ServerError::mpl("OnDecrypt returned no materials"))?;
        Ok(OnDecryptResponse {
            materials: decryption_materials_to_shape!(&materials)?,
        })
    }

    // ─── CMM ────────────────────────────────────────────────────────────────

    pub async fn get_encryption_materials(
        &self,
        req: GetEncryptionMaterialsRequest,
    ) -> Result<GetEncryptionMaterialsResponse, ServerError> {
        let cmm = self.get_cmm(&req.cmm_id)?;
        let mut call = cmm
            .get_encryption_materials()
            .encryption_context(to_hash_map(req.encryption_context))
            .commitment_policy(commitment_policy(req.commitment_policy));
        if let Some(suite) = req.algorithm_suite_id {
            call = call.algorithm_suite_id(suite_id(suite));
        }
        if let Some(length) = req.max_plaintext_length {
            let length = i64::try_from(length)
                .map_err(|_| ServerError::generic("maxPlaintextLength exceeds i64"))?;
            call = call.max_plaintext_length(length);
        }
        let materials = call
            .send()
            .await
            .map_err(mpl_err)?
            .encryption_materials
            .ok_or_else(|| ServerError::mpl("GetEncryptionMaterials returned no materials"))?;
        let shape = encryption_materials_to_shape!(&materials)?;
        Ok(GetEncryptionMaterialsResponse {
            algorithm_suite_id: shape.algorithm_suite_id,
            encryption_context: shape.encryption_context,
            encrypted_data_keys: shape.encrypted_data_keys,
            plaintext_data_key: shape
                .plaintext_data_key
                .ok_or_else(|| ServerError::mpl("no plaintext data key in materials"))?,
            signing_key: shape.signing_key,
            symmetric_signing_keys: shape.symmetric_signing_keys,
        })
    }

    pub async fn decrypt_materials(
        &self,
        req: DecryptMaterialsRequest,
    ) -> Result<DecryptMaterialsResponse, ServerError> {
        let cmm = self.get_cmm(&req.cmm_id)?;
        let mut call = cmm
            .decrypt_materials()
            .algorithm_suite_id(suite_id(req.algorithm_suite_id))
            .commitment_policy(commitment_policy(req.commitment_policy))
            .encrypted_data_keys(edks_from_shapes(req.encrypted_data_keys))
            .encryption_context(to_hash_map(req.encryption_context));
        if let Some(reproduced) = req.reproduced_encryption_context {
            call = call.reproduced_encryption_context(to_hash_map(reproduced));
        }
        let materials = call
            .send()
            .await
            .map_err(mpl_err)?
            .decryption_materials
            .ok_or_else(|| ServerError::mpl("DecryptMaterials returned no materials"))?;
        let shape = decryption_materials_to_shape!(&materials)?;
        Ok(DecryptMaterialsResponse {
            plaintext_data_key: shape
                .plaintext_data_key
                .ok_or_else(|| ServerError::mpl("no plaintext data key in materials"))?,
            encryption_context: shape.encryption_context,
            verification_key: shape.verification_key,
            symmetric_signing_key: shape.symmetric_signing_key,
        })
    }

    // ─── Registry ───────────────────────────────────────────────────────────

    fn get_keyring(&self, keyring_id: &str) -> Result<KeyringRef, ServerError> {
        if keyring_id.is_empty() {
            return Err(ServerError::generic("keyringId must be non-empty"));
        }
        self.keyrings
            .lock()
            .expect("keyrings mutex")
            .get(keyring_id)
            .cloned()
            .ok_or_else(|| ServerError::generic(format!("unknown keyringId: {keyring_id}")))
    }

    fn get_cmm(&self, cmm_id: &str) -> Result<CryptographicMaterialsManagerRef, ServerError> {
        if cmm_id.is_empty() {
            return Err(ServerError::generic("cmmId must be non-empty"));
        }
        self.cmms
            .lock()
            .expect("cmms mutex")
            .get(cmm_id)
            .cloned()
            .ok_or_else(|| ServerError::generic(format!("unknown cmmId: {cmm_id}")))
    }

    // ─── Materials from the wire ────────────────────────────────────────────

    fn info(&self, suite: AlgorithmSuiteId) -> AlgorithmSuiteInfo {
        self.suite_info[suite_index(suite)].clone()
    }

    fn shape_to_encryption_materials(
        &self,
        shape: EncryptionMaterialsShape,
    ) -> EncryptionMaterials {
        EncryptionMaterials::builder()
            .algorithm_suite(self.info(shape.algorithm_suite_id))
            .encrypted_data_keys(edks_from_shapes(shape.encrypted_data_keys))
            .encryption_context(to_hash_map(shape.encryption_context))
            .required_encryption_context_keys(shape.required_encryption_context_keys)
            .set_plaintext_data_key(shape.plaintext_data_key.map(Blob::new))
            .set_signing_key(shape.signing_key.map(Blob::new))
            .set_symmetric_signing_keys(
                shape
                    .symmetric_signing_keys
                    .map(|keys| keys.into_iter().map(|k| Blob::new(k.into_vec())).collect()),
            )
            .build()
            .expect("EncryptionMaterials builder has no required members")
    }

    fn shape_to_decryption_materials(
        &self,
        shape: DecryptionMaterialsShape,
    ) -> DecryptionMaterials {
        DecryptionMaterials::builder()
            .algorithm_suite(self.info(shape.algorithm_suite_id))
            .encryption_context(to_hash_map(shape.encryption_context))
            .required_encryption_context_keys(shape.required_encryption_context_keys)
            .set_plaintext_data_key(shape.plaintext_data_key.map(Blob::new))
            .set_verification_key(shape.verification_key.map(Blob::new))
            .set_symmetric_signing_key(shape.symmetric_signing_key.map(Blob::new))
            .build()
            .expect("DecryptionMaterials builder has no required members")
    }
}

// ─── Materials to the wire ──────────────────────────────────────────────────

fn suite_of(id: Option<&DafnyAlgorithmSuiteId>) -> Result<AlgorithmSuiteId, ServerError> {
    match id {
        Some(DafnyAlgorithmSuiteId::Esdk(esdk)) => ESDK_SUITES
            .iter()
            .find(|(_, candidate, _)| candidate == esdk)
            .map(|(wire, _, _)| *wire)
            .ok_or_else(|| ServerError::generic(format!("unrecognized ESDK suite {esdk:?}"))),
        _ => Err(ServerError::generic(
            "the MPL returned a non-ESDK algorithm suite, which the model cannot carry",
        )),
    }
}

fn edks_from_shapes(edks: Vec<EncryptedDataKeyShape>) -> Vec<EncryptedDataKey> {
    edks.into_iter()
        .map(|edk| {
            EncryptedDataKey::builder()
                .key_provider_id(edk.key_provider_id)
                .key_provider_info(Blob::new(edk.key_provider_info))
                .ciphertext(Blob::new(edk.ciphertext))
                .build()
                .expect("EncryptedDataKey builder has no required members")
        })
        .collect()
}

fn edks_to_shapes(edks: Option<Vec<EncryptedDataKey>>) -> Vec<EncryptedDataKeyShape> {
    edks.unwrap_or_default()
        .into_iter()
        .map(|edk| EncryptedDataKeyShape {
            key_provider_id: edk.key_provider_id.unwrap_or_default(),
            key_provider_info: edk
                .key_provider_info
                .map(Blob::into_inner)
                .unwrap_or_default(),
            ciphertext: edk.ciphertext.map(Blob::into_inner).unwrap_or_default(),
        })
        .collect()
}

// ─── Mapping helpers ────────────────────────────────────────────────────────

fn to_hash_map(map: BTreeMap<String, String>) -> HashMap<String, String> {
    map.into_iter().collect()
}

fn to_btree_map(map: Option<HashMap<String, String>>) -> BTreeMap<String, String> {
    map.unwrap_or_default().into_iter().collect()
}

fn suite_index(suite: AlgorithmSuiteId) -> usize {
    ESDK_SUITES
        .iter()
        .position(|(wire, _, _)| std::mem::discriminant(wire) == std::mem::discriminant(&suite))
        .expect("every wire suite is in ESDK_SUITES")
}

fn suite_id(suite: AlgorithmSuiteId) -> DafnyAlgorithmSuiteId {
    DafnyAlgorithmSuiteId::Esdk(ESDK_SUITES[suite_index(suite)].1)
}

fn commitment_policy(policy: CommitmentPolicy) -> DafnyCommitmentPolicy {
    DafnyCommitmentPolicy::Esdk(match policy {
        CommitmentPolicy::EsdkForbidEncryptAllowDecrypt => {
            EsdkCommitmentPolicy::ForbidEncryptAllowDecrypt
        }
        CommitmentPolicy::EsdkRequireEncryptAllowDecrypt => {
            EsdkCommitmentPolicy::RequireEncryptAllowDecrypt
        }
        CommitmentPolicy::EsdkRequireEncryptRequireDecrypt => {
            EsdkCommitmentPolicy::RequireEncryptRequireDecrypt
        }
    })
}
