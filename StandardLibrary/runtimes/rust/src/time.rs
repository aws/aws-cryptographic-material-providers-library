// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#![deny(warnings, unconditional_panic)]
#![deny(nonstandard_style)]
#![deny(clippy::all)]

use crate::_Wrappers_Compile as Wrappers;
use std::time::SystemTime;

impl crate::Time::_default {
    #[allow(non_snake_case)]
    pub fn CurrentRelativeTime() -> i64 {
        match SystemTime::now().duration_since(SystemTime::UNIX_EPOCH) {
            Ok(n) => n.as_secs() as i64,
            Err(_) => 0,
        }
    }

    #[allow(non_snake_case)]
    pub fn GetCurrentTimeStamp() -> ::std::rc::Rc<
        Wrappers::Result<
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        >,
    > {
        let now_utc = chrono::Utc::now();
        let formatted = format!("{}", now_utc.format("%Y-%m-%dT%H:%M:%S%.fZ"));
        ::std::rc::Rc::new(
                Wrappers::Result::Success{value :
                dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&formatted)
                }
            )
    }
}
