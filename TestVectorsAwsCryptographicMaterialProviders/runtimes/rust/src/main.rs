#![allow(
    deprecated,
    non_upper_case_globals,
    unused,
    non_snake_case,
    non_camel_case_types,
    unexpected_cfgs
)]

#![allow(warnings, unconditional_panic)]
#![allow(nonstandard_style)]
#![allow(clippy::never_loop)]
#![allow(clippy::absurd_extreme_comparisons)]

pub mod client;
pub mod conversions;
pub mod deps;
pub mod error;
pub mod operation;
pub mod types;
pub mod validation;
pub mod wrapped;

#[cfg(feature = "fips")]
use aws_lc_fips_sys as aws_lc_sys_impl;

#[cfg(not(feature = "fips"))]
use aws_lc_sys as aws_lc_sys_impl;


pub(crate) mod standard_library_conversions;
pub(crate) mod standard_library_externs;
pub use client::Client;

pub use crate::deps::aws_cryptography_primitives;
pub use crate::deps::aws_cryptography_keyStore;
pub use crate::deps::com_amazonaws_dynamodb;
pub use crate::deps::com_amazonaws_kms;

pub(crate) mod implementation_from_dafny;

pub mod aes_gcm;
pub mod aes_kdf_ctr;
pub mod concurrent_call;
pub mod dafny_libraries;
pub mod ddb;
pub mod digest;
pub mod ecdh;
pub mod ecdsa;
pub mod hmac;
pub mod kms;
pub mod local_cmc;
pub mod oslang;
pub mod random;
pub mod rsa;
pub mod sets;
pub mod software_externs;
pub mod storm_tracker;
pub mod test_vec_dir;
pub mod time;
pub mod uuid;

pub(crate) use crate::implementation_from_dafny::r#_Wrappers_Compile;
pub(crate) use crate::implementation_from_dafny::software;
pub(crate) use crate::implementation_from_dafny::AesKdfCtr;
pub(crate) use crate::implementation_from_dafny::ConcurrentCall;
pub(crate) use crate::implementation_from_dafny::DafnyLibraries;
pub(crate) use crate::implementation_from_dafny::ExternDigest;
pub(crate) use crate::implementation_from_dafny::ExternRandom;
pub(crate) use crate::implementation_from_dafny::Signature;
pub(crate) use crate::implementation_from_dafny::Time;
pub(crate) use crate::implementation_from_dafny::ECDH;
pub(crate) use crate::implementation_from_dafny::HMAC;
pub(crate) use crate::implementation_from_dafny::UTF8;
pub(crate) use crate::implementation_from_dafny::UUID;
pub(crate) use crate::implementation_from_dafny::_StormTracker_Compile;
pub(crate) use crate::implementation_from_dafny::_LocalCMC_Compile;
pub(crate) use crate::implementation_from_dafny::_TestWrappedMaterialProvidersMain_Compile;

fn main2() {
    let args: Vec<String> = std::env::args().collect();
    let dafny_strings = args.iter().map(|x| dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&x)).collect::<Vec<_>>();
    let dafny_args = dafny_runtime::Sequence::from_array_owned(dafny_strings);
    crate::implementation_from_dafny::r#_WrappedMaterialProvidersMain_Compile::_default::Main(&dafny_args);
}

// RUST_MIN_STACK does not work for `main`, so we need a new thread
fn main() {
    std::thread::Builder::new().stack_size(64 * 1024 * 1024).spawn(main2).unwrap().join().unwrap();
}
