#![allow(deprecated, non_upper_case_globals, unused, non_snake_case, non_camel_case_types)]

#![allow(warnings, unconditional_panic)]
#![allow(nonstandard_style)]
#![allow(clippy::never_loop)]
#![allow(clippy::absurd_extreme_comparisons)]

pub mod client;
pub mod conversions;
pub mod types;

pub(crate) mod standard_library_externs;
pub(crate) mod standard_library_conversions;
pub use client::Client;

pub(crate) mod implementation_from_dafny;
pub(crate) use crate::implementation_from_dafny::r#_Wrappers_Compile;

pub(crate) mod dafny_libraries;
pub(crate) mod ddb;
pub(crate) mod escape;
pub(crate) mod oslang;
pub(crate) mod sets;
pub(crate) mod time;
pub(crate) mod uuid;
pub(crate) use crate::implementation_from_dafny::UTF8;
pub(crate) mod concurrent_call;
//pub(crate) mod dafny_libraries;

pub(crate) use crate::implementation_from_dafny::DafnyLibraries;
pub(crate) use crate::implementation_from_dafny::ConcurrentCall;
pub(crate) use crate::implementation_from_dafny::Time;
pub(crate) use crate::implementation_from_dafny::UUID;
pub(crate) use crate::implementation_from_dafny::software;
pub(crate) use crate::client::Client as DdbClient;
