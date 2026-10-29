//! rpcv2Cbor HTTP wire layer.
//!
//! Routes `POST /service/{Service}/operation/{Operation}`, validates the
//! `smithy-protocol` header, decodes the CBOR request body into the operation's
//! input, dispatches to a handler, and encodes the CBOR response or a modeled
//! error.

use crate::error::ServerError;
use crate::handlers;
use crate::model::*;
use axum::body::{Body, Bytes};
use axum::extract::Path;
use axum::http::{header, HeaderMap, StatusCode};
use axum::response::Response;
use axum::routing::post;
use axum::Router;
use serde::de::DeserializeOwned;
use serde::Serialize;
use std::future::Future;

/// Build the router. Shared with tests so they can drive the real wire in-process.
pub fn app() -> Router {
    Router::new().route("/service/:service/operation/:operation", post(dispatch))
}

async fn dispatch(
    Path((service, operation)): Path<(String, String)>,
    headers: HeaderMap,
    body: Bytes,
) -> Response {
    if service != "PrimitivesTestServer" {
        return error_response(&ServerError::generic(format!(
            "unknown service: {service}; expected PrimitivesTestServer"
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
        "AesEncrypt" => {
            dispatch_op::<AesEncryptRequest, _, _, _>(&body, handlers::aes_encrypt).await
        }
        "AesDecrypt" => {
            dispatch_op::<AesDecryptRequest, _, _, _>(&body, handlers::aes_decrypt).await
        }
        "GenerateRandomBytes" => {
            dispatch_op::<GenerateRandomBytesRequest, _, _, _>(
                &body,
                handlers::generate_random_bytes,
            )
            .await
        }
        "Digest" => dispatch_op::<DigestRequest, _, _, _>(&body, handlers::digest).await,
        "Hmac" => dispatch_op::<HmacRequest, _, _, _>(&body, handlers::hmac).await,
        "Hkdf" => dispatch_op::<HkdfRequest, _, _, _>(&body, handlers::hkdf).await,
        "KbkdfCtrHmac" => {
            dispatch_op::<KbkdfCtrHmacRequest, _, _, _>(&body, handlers::kbkdf_ctr_hmac).await
        }
        "EcdsaGenerateKeyPair" => {
            dispatch_op::<EcdsaGenerateKeyPairRequest, _, _, _>(
                &body,
                handlers::ecdsa_generate_key_pair,
            )
            .await
        }
        "EcdsaSign" => dispatch_op::<EcdsaSignRequest, _, _, _>(&body, handlers::ecdsa_sign).await,
        "EcdsaVerify" => {
            dispatch_op::<EcdsaVerifyRequest, _, _, _>(&body, handlers::ecdsa_verify).await
        }
        other => Err(ServerError::generic(format!("unknown operation: {other}"))),
    };

    match outcome {
        Ok(body) => build(StatusCode::OK, body),
        Err(e) => error_response(&e),
    }
}

async fn dispatch_op<Req, Resp, F, Fut>(body: &[u8], handler: F) -> Result<Vec<u8>, ServerError>
where
    Req: DeserializeOwned,
    Resp: Serialize,
    F: FnOnce(Req) -> Fut,
    Fut: Future<Output = Result<Resp, ServerError>>,
{
    let req = decode::<Req>(body)?;
    let resp = handler(req).await?;
    encode(&resp)
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
