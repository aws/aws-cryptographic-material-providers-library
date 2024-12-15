// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#![deny(warnings, unconditional_panic)]
#![deny(nonstandard_style)]
#![deny(clippy::all)]

#[allow(non_snake_case)]
pub mod DafnyLibraries {
    pub mod FileIO {
        use std::fs::File;
        use std::io::Read;
        use std::io::Write;
        use std::path::Path;

        pub fn INTERNAL_ReadBytesFromFile(
            file: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) -> (
            bool,
            ::dafny_runtime::Sequence<u8>,
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) {
            let file_name = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::dafny_string_to_string(file);
            let path = Path::new(&file_name);

            let mut file = match File::open(path) {
                Err(why) => {
                    let err_msg = format!(
                        "couldn't open {} for reading from {}: {}",
                        path.display(),
                        curr_dir(),
                        why
                    );
                    let err_msg = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&err_msg);
                    return (true, dafny_runtime::Sequence::default(), err_msg);
                }
                Ok(file) => file,
            };

            let mut result = Vec::new();
            match file.read_to_end(&mut result) {
                Err(why) => {
                    let err_msg = format!("couldn't read from {}: {}", path.display(), why);
                    let err_msg = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&err_msg);
                    (true, dafny_runtime::Sequence::default(), err_msg)
                }
                Ok(_) => (
                    false,
                    dafny_runtime::Sequence::from_array_owned(result),
                    dafny_runtime::Sequence::default(),
                ),
            }
        }

        fn curr_dir() -> String {
            let path = std::env::current_dir();
            match path {
                Ok(path) => format!("{}", path.display()),
                Err(_) => "unknown".to_string(),
            }
        }

        pub fn INTERNAL_AppendBytesToFile(
            path: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            bytes: &::dafny_runtime::Sequence<u8>,
        ) -> (
            bool,
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) {
            SendBytesToFile(path, bytes, true)
        }

        pub fn INTERNAL_WriteBytesToFile(
            path: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            bytes: &::dafny_runtime::Sequence<u8>,
        ) -> (
            bool,
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) {
            SendBytesToFile(path, bytes, false)
        }

        pub fn SendBytesToFile(
            path: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            bytes: &::dafny_runtime::Sequence<u8>,
            append: bool
        ) -> (
            bool,
            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) {
            let file_name = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::dafny_string_to_string(path);
            let path = Path::new(&file_name);

            let maybe_file = std::fs::OpenOptions::new()
                .append(append)
                .write(true)
                .create(true)
                .truncate(!append)
                .open(path);
            let mut file = match maybe_file {
                Err(why) => {
                    let err_msg = format!(
                        "couldn't open {} for writing from {}: {}",
                        path.display(),
                        curr_dir(),
                        why
                    );
                    let err_msg = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&err_msg);
                    return (true, err_msg);
                }
                Ok(file) => file,
            };

            let bytes = bytes.to_array();
            match file.write_all(&bytes) {
                Err(why) => {
                    let err_msg =
                        format!("couldn't write all bytes to {}: {}", path.display(), why);
                    let err_msg = dafny_runtime::dafny_runtime_conversions::unicode_chars_false::string_to_dafny_string(&err_msg);
                    (true, err_msg)
                }
                Ok(_) => (false, dafny_runtime::Sequence::default()),
            }
        }
    }
}
