// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &aws_sdk_dynamodb::operation::describe_endpoints::DescribeEndpointsOutput
) -> ::std::rc::Rc<
    crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeEndpointsResponse,
>{
    ::std::rc::Rc::new(crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeEndpointsResponse::DescribeEndpointsResponse {
        Endpoints: ::dafny_runtime::dafny_runtime_conversions::vec_to_dafny_sequence(&value.endpoints,
    |e| crate::deps::com_amazonaws_dynamodb::conversions::endpoint::to_dafny(e)
,
)
,
    })
}
 
