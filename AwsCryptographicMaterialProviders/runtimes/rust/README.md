# AWS Encryption SDK for Rust

[![build status](https://github.com/aws/aws-cryptographic-material-providers-library/actions/workflows/daily_ci.yml/badge.svg?branch=mainline)](https://github.com/aws/aws-cryptographic-material-providers-library/actions/workflows/daily_ci.yml)
[![crates.io](https://img.shields.io/crates/v/aws-mpl-legacy.svg)](https://crates.io/crates/aws-mpl-legacy)
[![docs](https://docs.rs/aws-mpl-legacy/badge.svg)](https://docs.rs/aws-mpl-legacy)
[![rustc](https://img.shields.io/badge/rust-1.81%2B-orange.svg)](https://img.shields.io/badge/rust-1.81%2B-orange.svg)

This is the official [AWS Cryptographic Material Providers Legacy Library for Rust](https://crates.io/crates/aws-mpl-legacy).

## [CHANGELOG](https://github.com/aws/aws-cryptographic-material-providers-library/tree/main/AwsCryptographicMaterialProviders/runtimes/rust/CHANGELOG.md)

## Overview

The AWS Cryptographic Material Providers Library abstracts lower level cryptographic materials management of encryption and decryption materials.
It uses cryptographic best practices to protect the data keys that protect your data.
The data key is protected with a key encryption key called a _wrapping key_.
The encryption method returns the data key and one or more encrypted data keys.
Supported libraries use this information to perform envelope encryption.
The data key is used to protect your data,
and the encrypted data keys are stored alongside your data
so you don't need to keep track of the data keys separately.
You can use AWS KMS keys in [AWS Key Management Service](https://aws.amazon.com/kms/)(AWS KMS) as wrapping keys.
The AWS Cryptographic Material Providers Library
also provides APIs to define and use wrapping keys from other key providers.

The AWS Cryptographic Material Providers Library provides methods for encrypting and decrypting cryptographic materials used in higher level client side encryption libraries.

## License

This library is licensed under the Apache 2.0 License.
