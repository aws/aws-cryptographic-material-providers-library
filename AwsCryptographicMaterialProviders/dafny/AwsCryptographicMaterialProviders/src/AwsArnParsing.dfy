// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../../../../ComAmazonawsDynamodb/Model/ComAmazonawsDynamodbTypes.dfy"

module AwsArnParsing {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyMaterialProvidersTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UTF8

  const MAX_AWS_KMS_IDENTIFIER_LENGTH := 2048 as uint64

  datatype AwsResource = AwsResource(
    resourceType: string,
    value: string
  ) {
    predicate method Valid()
    {
      SequenceIsSafeBecauseItIsInMemory(value);
      && 0 < |value| as uint64
    }

    function method ToString(): string
    {
      // By the ARN specification both `:` and `/` are valid.
      // But this class does not aim to preserve this choice.
      // So I pick `/` because this is the only valid value for AWS KMS.
      resourceType + "/" + value
    }
  }

  datatype AwsArn = AwsArn(
    arnLiteral: string,
    partition: string,
    service: string,
    region: string,
    account: string,
    resource: AwsResource
  ) {
    predicate method Valid()
    {
      SequenceIsSafeBecauseItIsInMemory(partition);
      SequenceIsSafeBecauseItIsInMemory(service);
      SequenceIsSafeBecauseItIsInMemory(region);
      SequenceIsSafeBecauseItIsInMemory(account);
      && arnLiteral == "arn"
      && 0 < |partition| as uint64
      && 0 < |service| as uint64
      && 0 < |region| as uint64
      && 0 < |account| as uint64
      && resource.Valid()
    }

    function method ToString(): string
      requires this.Valid()
    {
      ToArnString(None)
    }

    function method ToArnString(customRegion: Option<string>): string
      requires this.Valid()
      decreases if customRegion.None? then 1 else 0
    {
      match customRegion {
        case None => ToArnString(Some(region))
        case Some(customRegion) => Join(
          [
            arnLiteral,
            partition,
            service,
            customRegion,
            account,
            resource.ToString()
          ],
          ":")
      }
    }
  }

  predicate method ValidAwsKmsResource(resource: AwsResource)
  {
    && resource.Valid()
    && (
         || resource.resourceType == "key"
         || resource.resourceType == "alias"
       )
  }

  predicate method ValidAwsKmsArn(arn: AwsArn)
  {
    && arn.Valid()
    && arn.service == "kms"
    && ValidAwsKmsResource(arn.resource)
  }

  type AwsKmsArn = a : AwsArn | ValidAwsKmsArn(a)
    witness *

  type AwsKmsResource = r : AwsResource | ValidAwsKmsResource(r)
    witness *

  datatype AwsKmsIdentifier =
    | AwsKmsArnIdentifier(a: AwsKmsArn)
    | AwsKmsRawResourceIdentifier(r: AwsKmsResource)
  {
    function method ToString(): string
    {
      match this {
        case AwsKmsArnIdentifier(a: AwsKmsArn) => a.ToString()
        case AwsKmsRawResourceIdentifier(r: AwsKmsResource)  => r.ToString()
      }
    }
  }

  function method ParseAwsKmsRawResources(identifier: string): (result: Result<AwsKmsResource, string>)
  {
    var info := Split(identifier, '/');

    :- Need(info[0 as uint32] != "key", "Malformed raw key id: " + identifier);
    SequenceIsSafeBecauseItIsInMemory(info);

    if |info| as uint64 == 1 then
      ParseAwsKmsResources("key/" + identifier)
    else
      ParseAwsKmsResources(identifier)
  }

  function method ParseAwsKmsResources(identifier: string): (result: Result<AwsKmsResource, string>)
  {
    var info := Split(identifier, '/');
    SequenceIsSafeBecauseItIsInMemory(info);

    :- Need(|info| as uint64 > 1, "Malformed resource: " + identifier);

    var resourceType := info[0 as uint32];
    var value := Join(info[1 as uint32 ..], "/");

    var resource := AwsResource(resourceType, value);

    :- Need(ValidAwsKmsResource(resource), "Malformed resource: " + identifier);

    Success(resource)
  }

  predicate method ValidAmazonDynamodbResource(resource: AwsResource)
  {
    // There are other valid resources aside from table in dynamodb
    // but for now we only care about table:
    // https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html#amazondynamodb-resources-for-iam-policies
    && resource.Valid()
    && resource.resourceType == "table"
  }

  predicate method ValidAmazonDynamodbArn(arn: AwsArn)
  {
    && arn.Valid()
    && arn.service == "dynamodb"
    && ValidAmazonDynamodbResource(arn.resource)
  }

  type AmazonDynamodbTableArn = a : AwsArn | ValidAmazonDynamodbArn(a)
    witness *

  type AmazonDynamodbResource = r : AwsResource | ValidAmazonDynamodbResource(r)
    witness *

  datatype AmazonDynamodbTableName = AmazonDynamodbTableArn(a: AmazonDynamodbTableArn)
  {
    function method GetTableName(): string
    {
      match this {
        case AmazonDynamodbTableArn(a: AmazonDynamodbTableArn) => a.resource.value
      }
    }
  }

  function method ParseAmazonDynamodbResources(identifier: string): (result: Result<AmazonDynamodbResource, string>)
  {
    var info := SplitOnce?(identifier, '/');

    :- Need(info.Some?, "Malformed resource: " + identifier);

    var resourceType := info.value.0;
    var value := info.value.1;

    // https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.NamingRules
    :- Need(DDB.IsValid_TableName(value), "Table Name invalid: " + identifier);

    var resource := AwsResource(resourceType, value);

    :- Need(ValidAmazonDynamodbResource(resource), "Malformed resource: " + identifier);

    Success(resource)
  }

  lemma ParseAwsKmsResourcesCorrect(identifier: string)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The resource section MUST be non-empty and MUST be split by a
    //# single `/` any additional `/` are included in the resource id
    ensures ParseAwsKmsResources(identifier).Success? ==>
              var info := Split(identifier, '/');
              var r := ParseAwsKmsResources(identifier);
              && |info| > 1
              && Join([r.value.resourceType, r.value.value], "/") == identifier
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The resource type MUST be either `alias` or `key`
    ensures ParseAwsKmsResources(identifier).Success? ==>
              var resourceType := Split(identifier, '/')[0];
              "key" == resourceType || "alias" == resourceType
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The resource id MUST be a non-empty string
    ensures ParseAwsKmsResources(identifier).Success? ==>
              var info := Split(identifier, '/');
              |Join(info[1..], "/")| > 0
  {}

  lemma ParseAmazonDynamodbResourcesCorrect(identifier: string)
    ensures ParseAmazonDynamodbResources(identifier).Success? ==>
              var info := SplitOnce?(identifier, '/');
              var r := ParseAmazonDynamodbResources(identifier);
              &&  info.Some?
              && Join([r.value.resourceType, r.value.value], "/") == identifier
    ensures ParseAmazonDynamodbResources(identifier).Success? ==>
              var resourceType := SplitOnce?(identifier, '/').value.0;
              resourceType == "table"
    ensures ParseAmazonDynamodbResources(identifier).Success? ==>
              var info := SplitOnce?(identifier, '/');
              DDB.IsValid_TableName(info.value.1)
  {}

  function method ParseAwsKmsArn(identifier: string): (result: Result<AwsKmsArn, string>)
    ensures result.Success? ==>
              && "arn" <= identifier
              && |Split(identifier, ':')| == 6
              && |Split(identifier, ':')[1]| > 0
              && Split(identifier, ':')[2] == "kms"
              && |Split(identifier, ':')[3]| > 0
              && |Split(identifier, ':')[4]| > 0
  {
    var components := Split(identifier, ':');
    SequenceIsSafeBecauseItIsInMemory(components);


    :- Need(6 == |components| as uint64, "Malformed arn: " + identifier);

    var resource :- ParseAwsKmsResources(components[5 as uint32]);

    var arn := AwsArn(
                 components[0 as uint32],
                 components[1 as uint32],
                 components[2 as uint32],
                 components[3 as uint32],
                 components[4 as uint32],
                 resource
               );

    :- Need(ValidAwsKmsArn(arn), "Malformed Arn:" + identifier);

    Success(arn)
  }

  function method ParseAmazonDynamodbTableArn(identifier: string): (result: Result<AmazonDynamodbTableArn, string>)
    ensures result.Success? ==>
              && "arn" <= identifier
              && |Split(identifier, ':')| == 6
              && |Split(identifier, ':')[1]| > 0
              && Split(identifier, ':')[2] == "dynamodb"
              && |Split(identifier, ':')[3]| > 0
              && |Split(identifier, ':')[4]| > 0
  {
    var components := Split(identifier, ':');
    SequenceIsSafeBecauseItIsInMemory(components);

    :- Need(6 == |components| as uint64, "Malformed arn: " + identifier);

    var resource :- ParseAmazonDynamodbResources(components[5 as uint32]);

    var arn := AwsArn(
                 components[0 as uint32],
                 components[1 as uint32],
                 components[2 as uint32],
                 components[3 as uint32],
                 components[4 as uint32],
                 resource
               );

    :- Need(ValidAmazonDynamodbArn(arn), "Malformed Arn:" + identifier);

    Success(arn)
  }

  lemma ParseAwsKmsArnCorrect(identifier: string)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# MUST start with string `arn`
    ensures ParseAwsKmsArn(identifier).Success? ==> "arn" <= identifier

    ensures ParseAwsKmsArn(identifier).Success? ==> |Split(identifier, ':')| == 6

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The partition MUST be a non-empty
    ensures ParseAwsKmsArn(identifier).Success? ==> |Split(identifier, ':')[1]| > 0

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The service MUST be the string `kms`
    ensures ParseAwsKmsArn(identifier).Success? ==> Split(identifier, ':')[2] == "kms"

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The region MUST be a non-empty string
    ensures ParseAwsKmsArn(identifier).Success? ==> |Split(identifier, ':')[3]| > 0

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn
    //= type=implication
    //# The account MUST be a non-empty string
    ensures ParseAwsKmsArn(identifier).Success? ==> |Split(identifier, ':')[4]| > 0
  {}

  lemma ParseAmazonDynamodbTableArnCorrect(identifier: string)
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==> "arn" <= identifier
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==> |Split(identifier, ':')| == 6
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==> |Split(identifier, ':')[1]| > 0
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==>  Split(identifier, ':')[2] == "dynamodb"
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==> |Split(identifier, ':')[3]| > 0
    ensures ParseAmazonDynamodbTableArn(identifier).Success? ==> |Split(identifier, ':')[4]| > 0
  {}

  function method ParseAwsKmsIdentifier(identifier: string): (result: Result<AwsKmsIdentifier, string>)
  {
    if "arn:" <= identifier then
      var arn :- ParseAwsKmsArn(identifier);
      Success(AwsKmsArnIdentifier(arn))
    else
      var r :- ParseAwsKmsRawResources(identifier);
      Success(AwsKmsRawResourceIdentifier(r))
  }

  function method ParseAmazonDynamodbTableName(identifier: string): (result: Result<DDB.TableName, string>)
  {
    var arn :- ParseAmazonDynamodbTableArn(identifier);
    var tableArn := AmazonDynamodbTableArn(arn);
    var tableName := tableArn.GetTableName();
    Success(tableName)
  }

  //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-arn
  //= type=implication
  //# This function MUST take a single AWS KMS ARN
  //# If the input is an invalid AWS KMS ARN this function MUST error.
  predicate method IsMultiRegionAwsKmsArn(arn: AwsKmsArn)
  {
    IsMultiRegionAwsKmsResource(arn.resource)
  }

  lemma IsMultiRegionAwsKmsArnCorrectness(arn: AwsKmsArn)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-arn
    //= type=implication
    //# If resource type is “alias”,
    //# this is an AWS KMS alias ARN and MUST return false.
    ensures !IsMultiRegionAwsKmsArn(arn) <== arn.resource.resourceType == "alias"
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-arn
    //= type=implication
    //# If resource type is “key” and resource ID starts with “mrk-“,
    //# this is a AWS KMS multi-Region key ARN and MUST return true.
    ensures !IsMultiRegionAwsKmsArn(arn) <==
            (&& arn.resource.resourceType == "key"
             && !("mrk-" <= arn.resource.value))
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-arn
    //= type=implication
    //# If resource type is “key” and resource ID does not start with “mrk-“,
    //# this is a (single-region) AWS KMS key ARN and MUST return false.
    ensures IsMultiRegionAwsKmsArn(arn) <==
            (&& arn.resource.resourceType == "key"
             && "mrk-" <= arn.resource.value)
  {
  }

  //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-identifier
  //= type=implication
  //# This function MUST take a single AWS KMS identifier
  predicate method IsMultiRegionAwsKmsIdentifier(identifier: AwsKmsIdentifier)
  {
    match identifier {
      case AwsKmsArnIdentifier(arn) =>
        IsMultiRegionAwsKmsArn(arn)
      case AwsKmsRawResourceIdentifier(r) =>
        IsMultiRegionAwsKmsResource(r)
    }
  }

  lemma IsMultiRegionAwsKmsIdentifierCorrect(s: string)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-identifier
    //= type=implication
    //# If the input starts with "arn:",
    //# this MUST return the output of [identifying an an AWS KMS multi-Region ARN](aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-arn)
    //# called with this input.
    ensures "arn:" <= s && ParseAwsKmsArn(s).Success?
            ==>
              var arn := ParseAwsKmsArn(s);
              var arnIdentifier := AwsKmsArnIdentifier(arn.value);
              IsMultiRegionAwsKmsIdentifier(arnIdentifier) == IsMultiRegionAwsKmsArn(arn.value)

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-identifier
    //= type=implication
    //# If the input starts with “alias/“,
    //# this an AWS KMS alias and not a multi-Region key id and MUST return false.
    ensures "alias/" <= s && ParseAwsKmsResources(s).Success?
            ==>
              var resource := ParseAwsKmsResources(s);
              var resourceIdentifier := AwsKmsRawResourceIdentifier(resource.value);
              !IsMultiRegionAwsKmsIdentifier(resourceIdentifier)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-identifier
    //= type=implication
    //# If the input starts with “mrk-“,
    //# this is a multi-Region key id and MUST return true.
    ensures "mrk-" <= s && ParseAwsKmsResources(s).Success?
            ==>
              var resource := ParseAwsKmsResources(s);
              var resourceIdentifier := AwsKmsRawResourceIdentifier(resource.value);
              IsMultiRegionAwsKmsIdentifier(resourceIdentifier)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-key-arn.md#identifying-an-an-aws-kms-multi-region-identifier
    //= type=implication
    //# If
    //# the input does not start with any of the above, this is not a multi-
    //# Region key id and MUST return false.
    ensures (
              && !("arn:" <= s )
              && !("alias/" <= s )
              && !("mrk-" <= s )
              && ParseAwsKmsIdentifier(s).Success?
            )
            ==>
              var resourceIdentifier := ParseAwsKmsIdentifier(s);
              !IsMultiRegionAwsKmsIdentifier(resourceIdentifier.value)
  {}

  predicate method IsMultiRegionAwsKmsResource(resource: AwsKmsResource)
  {
    resource.resourceType == "key" && "mrk-" <= resource.value
  }

  function method GetRegion(
    identifier: AwsKmsIdentifier
  ): (res: Option<string>)
  {
    match identifier {
      case AwsKmsArnIdentifier(a) => Some(a.region)
      case AwsKmsRawResourceIdentifier(_) => None()
    }
  }

  function method IsAwsKmsIdentifierString(
    s: string
  ): (res: Result<AwsKmsIdentifier, string>)
  {
    :- Need(UTF8.IsASCIIString(s), "Not a valid ASCII string.");
    SequenceIsSafeBecauseItIsInMemory(s);
    :- Need(0 < |s| as uint64 <= MAX_AWS_KMS_IDENTIFIER_LENGTH, "Identifier exceeds maximum length.");
    ParseAwsKmsIdentifier(s)
  }

  type AwsKmsIdentifierString = s: string |
      IsAwsKmsIdentifierString(s).Success?
    witness *

  function method Error(s : string) : Types.Error {
    Types.AwsCryptographicMaterialProvidersException(message := s)
  }

  function method ValidateDdbTableArn(tableArn: string)
    : (res: Result<(), Types.Error>)
    ensures res.Success? ==>
              && ParseAmazonDynamodbTableArn(tableArn).Success?
              && UTF8.IsASCIIString(tableArn)
              && DDB.IsValid_TableName(ParseAmazonDynamodbTableName(tableArn).value)
  {
    var _ :- ParseAmazonDynamodbTableName(tableArn).MapFailure(Error);

    :- Need(UTF8.IsASCIIString(tableArn),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Table Arn is not ASCII"));
    :- Need(DDB.IsValid_TableName(ParseAmazonDynamodbTableName(tableArn).value),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Table Name is too long"));
    Success(())
  }
}
