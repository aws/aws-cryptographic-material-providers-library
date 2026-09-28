//! Runnable entry point for the Dafny-generated Rust MPL Language_Server.
//!
//! Binds an rpcv2Cbor HTTP endpoint on the port given as the first CLI
//! argument (default 8105).

use std::net::SocketAddr;
use std::sync::Arc;

use aws_mpl_dafny_test_server::handlers::AppState;
use aws_mpl_dafny_test_server::wire::app;

#[tokio::main]
async fn main() {
    let port = std::env::args()
        .nth(1)
        .and_then(|s| s.parse::<u16>().ok())
        .unwrap_or(8105);

    let state = Arc::new(AppState::new().await);
    let addr = SocketAddr::from(([127, 0, 0, 1], port));
    let listener = tokio::net::TcpListener::bind(addr)
        .await
        .unwrap_or_else(|e| panic!("failed to bind {addr}: {e}"));
    eprintln!("listening at http://127.0.0.1:{port}");
    axum::serve(listener, app(state))
        .await
        .expect("server error");
}
