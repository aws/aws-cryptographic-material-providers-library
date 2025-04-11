// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"

include "KeyStoreErrorMessages.dfy"

module {:options "/functionSyntax:4" } KmsArn {
  import opened Wrappers
  import AwsArnParsing
  import ErrorMessages = KeyStoreErrorMessages
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
            Types.KeyStoreException(message := ErrorMessages.KMS_CONFIG_KMS_ARN_INVALID)
       );
    var arn :- AwsArnParsing.ParseAwsKmsArn(input).MapFailure(
                 error => Types.KeyStoreException(message := ErrorMessages.KMS_CONFIG_KMS_ARN_INVALID + ". " + error));
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
    //# This ARN MUST NOT be an Alias.
    if arn.resource.resourceType != "key" then
      Failure(Types.KeyStoreException(message := ErrorMessages.ALIAS_NOT_ALLOWED))
    else
      Success(arn)
  }

}
