//! rpcv2Cbor HTTP wire layer.

use crate::error::ServerError;
use crate::handlers::AppState;
use crate::model::*;
use axum::body::{Body, Bytes};
use axum::extract::{Path, State};
use axum::http::{header, HeaderMap, StatusCode};
use axum::response::Response;
use axum::routing::post;
use axum::Router;
use serde::de::DeserializeOwned;
use serde::Serialize;
use std::sync::Arc;

/// Build the router. Shared with tests so they can drive the real wire in-process.
pub fn app(state: Arc<AppState>) -> Router {
    Router::new()
        .route("/service/:service/operation/:operation", post(dispatch))
        .with_state(state)
}

async fn dispatch(
    State(state): State<Arc<AppState>>,
    Path((service, operation)): Path<(String, String)>,
    headers: HeaderMap,
    body: Bytes,
) -> Response {
    if service != "MPLTestServer" {
        return error_response(&ServerError::generic(format!(
            "unknown service: {service}; expected MPLTestServer"
        )));
    }
    let protocol_ok = headers
        .get("smithy-protocol")
        .and_then(|value| value.to_str().ok())
        == Some("rpc-v2-cbor");
    if !protocol_ok {
        return error_response(&ServerError::generic(
            "missing or invalid smithy-protocol header; expected rpc-v2-cbor",
        ));
    }
    let content_type_ok = headers
        .get(header::CONTENT_TYPE)
        .and_then(|value| value.to_str().ok())
        == Some("application/cbor");
    if !content_type_ok {
        return error_response(&ServerError::generic(
            "missing or invalid content-type; expected application/cbor",
        ));
    }

    let outcome = match operation.as_str() {
        "CreateRawAesKeyring" => match decode::<CreateRawAesKeyringRequest>(&body) {
            Ok(req) => state
                .create_raw_aes_keyring(req)
                .await
                .and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        "CreateDefaultCmm" => match decode::<CreateDefaultCmmRequest>(&body) {
            Ok(req) => state
                .create_default_cmm(req)
                .await
                .and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        "InitializeEncryptionMaterials" => {
            match decode::<InitializeEncryptionMaterialsRequest>(&body) {
                Ok(req) => state
                    .initialize_encryption_materials(req)
                    .await
                    .and_then(|resp| encode(&resp)),
                Err(e) => Err(e),
            }
        }
        "InitializeDecryptionMaterials" => {
            match decode::<InitializeDecryptionMaterialsRequest>(&body) {
                Ok(req) => state
                    .initialize_decryption_materials(req)
                    .await
                    .and_then(|resp| encode(&resp)),
                Err(e) => Err(e),
            }
        }
        "OnEncrypt" => match decode::<OnEncryptRequest>(&body) {
            Ok(req) => state.on_encrypt(req).await.and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        "OnDecrypt" => match decode::<OnDecryptRequest>(&body) {
            Ok(req) => state.on_decrypt(req).await.and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        "GetEncryptionMaterials" => match decode::<GetEncryptionMaterialsRequest>(&body) {
            Ok(req) => state
                .get_encryption_materials(req)
                .await
                .and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        "DecryptMaterials" => match decode::<DecryptMaterialsRequest>(&body) {
            Ok(req) => state
                .decrypt_materials(req)
                .await
                .and_then(|resp| encode(&resp)),
            Err(e) => Err(e),
        },
        other => Err(ServerError::generic(format!("unknown operation: {other}"))),
    };

    match outcome {
        Ok(body) => build(StatusCode::OK, body),
        Err(e) => error_response(&e),
    }
}

fn decode<T: DeserializeOwned>(bytes: &[u8]) -> Result<T, ServerError> {
    ciborium::from_reader(bytes)
        .map_err(|e| ServerError::generic(format!("failed to decode CBOR request: {e}")))
}

fn encode<T: Serialize>(value: &T) -> Result<Vec<u8>, ServerError> {
    let mut buf = Vec::new();
    ciborium::into_writer(value, &mut buf)
        .map_err(|e| ServerError::generic(format!("failed to encode CBOR response: {e}")))?;
    Ok(buf)
}

fn error_response(error: &ServerError) -> Response {
    build(StatusCode::BAD_REQUEST, error.to_cbor())
}

fn build(status: StatusCode, body: Vec<u8>) -> Response {
    Response::builder()
        .status(status)
        .header("smithy-protocol", "rpc-v2-cbor")
        .header(header::CONTENT_TYPE, "application/cbor")
        .body(Body::from(body))
        .expect("response builder")
}
