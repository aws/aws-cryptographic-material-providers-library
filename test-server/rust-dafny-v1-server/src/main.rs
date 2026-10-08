//! Runnable entry point for the Dafny-generated Rust Primitives Language_Server.
//!
//! Binds an rpcv2Cbor HTTP endpoint on the port given as the first CLI
//! argument (default 8114).

use std::net::SocketAddr;

use aws_primitives_dafny_test_server::wire::app;

#[tokio::main]
async fn main() {
    let port = std::env::args()
        .nth(1)
        .and_then(|s| s.parse::<u16>().ok())
        .unwrap_or(8114);

    let addr = SocketAddr::from(([127, 0, 0, 1], port));
    let listener = tokio::net::TcpListener::bind(addr)
        .await
        .unwrap_or_else(|e| panic!("failed to bind {addr}: {e}"));
    eprintln!("listening at http://127.0.0.1:{port}");
    axum::serve(listener, app()).await.expect("server error");
}
