//! Hand-rolled MPL TestServer Language_Server for the Dafny-generated Rust
//! runtime.
//!
//! Speaks the rpcv2Cbor wire contract and delegates each operation to the
//! MaterialProviders client in `releases/rust/mpl` (`aws-mpl-legacy`).

pub mod error;
pub mod handlers;
pub mod model;
pub mod wire;
