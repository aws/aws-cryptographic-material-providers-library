// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[derive(::std::clone::Clone, ::std::fmt::Debug, ::std::cmp::PartialEq)]
pub enum Error {
    GlobalTableNotFoundException {
    error: aws_sdk_dynamodb::types::error::GlobalTableNotFoundException,
},

InternalServerError {
    error: aws_sdk_dynamodb::types::error::InternalServerError,
},

InvalidEndpointException {
    error: aws_sdk_dynamodb::types::error::InvalidEndpointException,
},

ExportNotFoundException {
    error: aws_sdk_dynamodb::types::error::ExportNotFoundException,
},

LimitExceededException {
    error: aws_sdk_dynamodb::types::error::LimitExceededException,
},

ResourceNotFoundException {
    error: aws_sdk_dynamodb::types::error::ResourceNotFoundException,
},

ContinuousBackupsUnavailableException {
    error: aws_sdk_dynamodb::types::error::ContinuousBackupsUnavailableException,
},

TableNotFoundException {
    error: aws_sdk_dynamodb::types::error::TableNotFoundException,
},

ImportConflictException {
    error: aws_sdk_dynamodb::types::error::ImportConflictException,
},

ResourceInUseException {
    error: aws_sdk_dynamodb::types::error::ResourceInUseException,
},

IndexNotFoundException {
    error: aws_sdk_dynamodb::types::error::IndexNotFoundException,
},

ReplicaNotFoundException {
    error: aws_sdk_dynamodb::types::error::ReplicaNotFoundException,
},

ConditionalCheckFailedException {
    error: aws_sdk_dynamodb::types::error::ConditionalCheckFailedException,
},

ItemCollectionSizeLimitExceededException {
    error: aws_sdk_dynamodb::types::error::ItemCollectionSizeLimitExceededException,
},

ProvisionedThroughputExceededException {
    error: aws_sdk_dynamodb::types::error::ProvisionedThroughputExceededException,
},

RequestLimitExceeded {
    error: aws_sdk_dynamodb::types::error::RequestLimitExceeded,
},

TransactionConflictException {
    error: aws_sdk_dynamodb::types::error::TransactionConflictException,
},

BackupInUseException {
    error: aws_sdk_dynamodb::types::error::BackupInUseException,
},

TableInUseException {
    error: aws_sdk_dynamodb::types::error::TableInUseException,
},

ReplicaAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::ReplicaAlreadyExistsException,
},

BackupNotFoundException {
    error: aws_sdk_dynamodb::types::error::BackupNotFoundException,
},

IdempotentParameterMismatchException {
    error: aws_sdk_dynamodb::types::error::IdempotentParameterMismatchException,
},

TransactionCanceledException {
    error: aws_sdk_dynamodb::types::error::TransactionCanceledException,
},

TransactionInProgressException {
    error: aws_sdk_dynamodb::types::error::TransactionInProgressException,
},

DuplicateItemException {
    error: aws_sdk_dynamodb::types::error::DuplicateItemException,
},

ExportConflictException {
    error: aws_sdk_dynamodb::types::error::ExportConflictException,
},

InvalidExportTimeException {
    error: aws_sdk_dynamodb::types::error::InvalidExportTimeException,
},

PointInTimeRecoveryUnavailableException {
    error: aws_sdk_dynamodb::types::error::PointInTimeRecoveryUnavailableException,
},

TableAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::TableAlreadyExistsException,
},

ImportNotFoundException {
    error: aws_sdk_dynamodb::types::error::ImportNotFoundException,
},

GlobalTableAlreadyExistsException {
    error: aws_sdk_dynamodb::types::error::GlobalTableAlreadyExistsException,
},

InvalidRestoreTimeException {
    error: aws_sdk_dynamodb::types::error::InvalidRestoreTimeException,
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
