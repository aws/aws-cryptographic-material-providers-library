// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#![deny(warnings, unconditional_panic)]
#![deny(nonstandard_style)]
#![deny(clippy::all)]

use crate::*;

impl software::amazon::cryptography::services::dynamodb::internaldafny::_default {
    #[allow(non_snake_case)]
    pub fn DynamoDBClient()
    -> ::std::rc::Rc<_Wrappers_Compile::Result<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::services::dynamodb::internaldafny::types::IDynamoDBClient>, ::std::rc::Rc<crate::software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>>>
    {
        let config = aws_types::SdkConfig::builder().build();
        // let config = SdkConfig::builder().region(Region::new("us-east-1")).build();
        // let config = aws_config::load_from_env().await;
        let _client = aws_sdk_dynamodb::Client::new(&config);
        todo!("software::amazon::cryptography::services::ddb::internaldafny::DynamoDBClient not implemented");
        //        std::rc::Rc::new(Wrappers::Result::Success {
        //            value: ::dafny_runtime::Object::new(client),
        //        })
    }

    #[allow(non_snake_case)]
    pub fn DDBClientForRegion(region: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>)
        -> ::std::rc::Rc<_Wrappers_Compile::Result<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::services::dynamodb::internaldafny::types::IDynamoDBClient>, ::std::rc::Rc<crate::software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>>>
        {
        let region =
            dafny_runtime::dafny_runtime_conversions::unicode_chars_false::dafny_string_to_string(
                region,
            );
        let config = aws_types::sdk_config::SdkConfig::builder()
            .region(aws_sdk_dynamodb::config::Region::new(region))
            .build();
        let _client = aws_sdk_dynamodb::Client::new(&config);
        todo!("software::amazon::cryptography::services::ddb::internaldafny::DDBClientForRegion not implemented");
        // std::rc::Rc::new(
        //     Wrappers::Result::Success{value :
        //         ::dafny_runtime::Object::new()
        //     }
        // )
    }
}
