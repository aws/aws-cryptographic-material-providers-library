// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#![allow(deprecated, non_upper_case_globals, unused, non_snake_case, non_camel_case_types)]

pub(crate) mod standard_library_externs;

pub(crate) mod implementation_from_dafny;
pub(crate) use crate::implementation_from_dafny::r#_Wrappers_Compile;

pub(crate) mod oslang;
pub(crate) mod sets;
pub(crate) mod time;
pub(crate) mod uuid;
pub(crate) mod dafny_libraries;
pub(crate) use crate::implementation_from_dafny::UTF8;
pub(crate) mod concurrent_call;

pub(crate) use crate::implementation_from_dafny::ConcurrentCall;
pub(crate) use crate::implementation_from_dafny::Time;
pub(crate) use crate::implementation_from_dafny::UUID;
pub(crate) use crate::dafny_libraries::DafnyLibraries;
