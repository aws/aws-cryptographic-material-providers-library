// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[derive(::std::clone::Clone, ::std::fmt::Debug, ::std::cmp::PartialEq)]
pub enum Error {
    GlobalTableAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::GlobalTableAlreadyExistsException,
},

TableInUseException {
    error: aws_sdk_dynamodb::types::error::TableInUseException,
},

ReplicaAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::ReplicaAlreadyExistsException,
},

ExportNotFoundException {
    error: aws_sdk_dynamodb::types::error::ExportNotFoundException,
},

RequestLimitExceeded {
    error: aws_sdk_dynamodb::types::error::RequestLimitExceeded,
},

PointInTimeRecoveryUnavailableException {
    error: aws_sdk_dynamodb::types::error::PointInTimeRecoveryUnavailableException,
},

InternalServerError {
    error: aws_sdk_dynamodb::types::error::InternalServerError,
},

IdempotentParameterMismatchException {
    error: aws_sdk_dynamodb::types::error::IdempotentParameterMismatchException,
},

ContinuousBackupsUnavailableException {
    error: aws_sdk_dynamodb::types::error::ContinuousBackupsUnavailableException,
},

TableAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::TableAlreadyExistsException,
},

TransactionConflictException {
    error: aws_sdk_dynamodb::types::error::TransactionConflictException,
},

InvalidEndpointException {
    error: aws_sdk_dynamodb::types::error::InvalidEndpointException,
},

ResourceInUseException {
    error: aws_sdk_dynamodb::types::error::ResourceInUseException,
},

InvalidRestoreTimeException {
    error: aws_sdk_dynamodb::types::error::InvalidRestoreTimeException,
},

BackupInUseException {
    error: aws_sdk_dynamodb::types::error::BackupInUseException,
},

ItemCollectionSizeLimitExceededException {
    error: aws_sdk_dynamodb::types::error::ItemCollectionSizeLimitExceededException,
},

ProvisionedThroughputExceededException {
    error: aws_sdk_dynamodb::types::error::ProvisionedThroughputExceededException,
},

LimitExceededException {
    error: aws_sdk_dynamodb::types::error::LimitExceededException,
},

ImportNotFoundException {
    error: aws_sdk_dynamodb::types::error::ImportNotFoundException,
},

TransactionInProgressException {
    error: aws_sdk_dynamodb::types::error::TransactionInProgressException,
},

GlobalTableNotFoundException {
    error: aws_sdk_dynamodb::types::error::GlobalTableNotFoundException,
},

DuplicateItemException {
    error: aws_sdk_dynamodb::types::error::DuplicateItemException,
},

BackupNotFoundException {
    error: aws_sdk_dynamodb::types::error::BackupNotFoundException,
},

ImportConflictException {
    error: aws_sdk_dynamodb::types::error::ImportConflictException,
},

IndexNotFoundException {
    error: aws_sdk_dynamodb::types::error::IndexNotFoundException,
},

InvalidExportTimeException {
    error: aws_sdk_dynamodb::types::error::InvalidExportTimeException,
},

ResourceNotFoundException {
    error: aws_sdk_dynamodb::types::error::ResourceNotFoundException,
},

ReplicaNotFoundException {
    error: aws_sdk_dynamodb::types::error::ReplicaNotFoundException,
},

TransactionCanceledException {
    error: aws_sdk_dynamodb::types::error::TransactionCanceledException,
},

TableNotFoundException {
    error: aws_sdk_dynamodb::types::error::TableNotFoundException,
},

ConditionalCheckFailedException {
    error: aws_sdk_dynamodb::types::error::ConditionalCheckFailedException,
},

ExportConflictException {
    error: aws_sdk_dynamodb::types::error::ExportConflictException,
},
    Opaque {
        obj: ::dafny_runtime::Object<dyn ::std::any::Any>,
    },
}

impl ::std::cmp::Eq for Error {}

impl ::std::fmt::Display for Error {
    fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

impl ::std::error::Error for Error {}
