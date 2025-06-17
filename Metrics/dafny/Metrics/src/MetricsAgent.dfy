// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"

module {:options "/functionSyntax:4" } MetricsAgent {
  import opened Wrappers
  import Types = AwsCryptographyMetricsTypes

  trait {:termination false} VerifiableInterface
    extends Types.IMetricsAgent
  {

    ghost predicate PutCountEnsuresPublicly(input: Types.PutCountInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    ghost predicate PutDateEnsuresPublicly(input: Types.PutDateInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    ghost predicate PutTimeEnsuresPublicly(input: Types.PutTimeInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    ghost predicate PutPropertyEnsuresPublicly(input: Types.PutPropertyInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
  }
}
