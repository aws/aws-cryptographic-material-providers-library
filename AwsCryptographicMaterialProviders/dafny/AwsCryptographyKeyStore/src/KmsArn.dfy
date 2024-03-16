// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"

include "ErrorMessages.dfy"

module {:options "/functionSyntax:4" } KmsArn {
  import opened Wrappers
  import AwsArnParsing
  import ErrorMessages
  import KMS = ComAmazonawsKmsTypes
  import Types = AwsCryptographyKeyStoreTypes

  // For the Key Store, a ValidKmsArn is a `key`, not an `alias`
  predicate ValidKmsArn?(input: string)
  {
    && KMS.IsValid_KeyIdType(input)
    && var maybeParsed := AwsArnParsing.ParseAwsKmsArn(input);
    && maybeParsed.Success?
    && maybeParsed.value.resource.resourceType == "key"
  }

  function IsValidKeyArn(
    input: string
  ): (res: Result<AwsArnParsing.AwsKmsArn, Types.Error>)
    ensures res.Success? ==> ValidKmsArn?(input)
  {
    :- Need(KMS.IsValid_KeyIdType(input),
            Types.KeyStoreException(message := ErrorMessages.KMS_KEY_ARN_INVALID)
       );
    var maybeParsedArn: Result<AwsArnParsing.AwsKmsArn, string> := AwsArnParsing.ParseAwsKmsArn(input);
    if maybeParsedArn.Failure? then
      Failure(Types.KeyStoreException(message := ErrorMessages.KMS_KEY_ARN_INVALID + ". " + maybeParsedArn.error))
    else (
           if maybeParsedArn.value.resource.resourceType != "key" then
             Failure(Types.KeyStoreException(message := ErrorMessages.KMS_CONFIG_ALIAS_IS_NOT_ALLOWED))
           else
             Success(maybeParsedArn.value)
         )
  }

}
