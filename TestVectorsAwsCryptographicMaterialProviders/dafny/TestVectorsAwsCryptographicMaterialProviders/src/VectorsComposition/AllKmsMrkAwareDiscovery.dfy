// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"
include "AllKmsMrkAware.dfy"

module {:options "-functionSyntax:4"} AllKmsMrkAwareDiscovery {
  import Types = AwsCryptographyMaterialProvidersTypes
  import Seq
  import opened Wrappers
  import opened JSON.Values
  import opened KeyDescriptionJson
  import AllKmsMrkAware
  import AllAlgorithmSuites

  // These values MUST correspond to the KMS keys above
  // At this time, this list is simplistic
  const AwsPartitions := [ "aws" ]
  const AWSAccounts := [ "658956600833" ]
  const AllDiscoveryFilters: set<Option<Types.DiscoveryFilter>> := {
    Some(Types.DiscoveryFilter(
           partition := "aws",
           accountIds := [ "658956600833" ]
         )),
    None
  }

  const AllKmsMrkAwareDiscovery :=
    set
      keyId <- AllKmsMrkAware.AllAwsKMSMrkKeys,
      filter <- AllDiscoveryFilters
      ::
        PositiveKeyDescriptionJSON(
          description := "Discovery KMS MRK " + keyId +
          "->" + if filter.Some? then
            "Filter " + filter.value.partition + " " + Seq.Flatten(filter.value.accountIds)
          else
            "No Filter"
        ,
          encrypt := Object([
                              ("type", String("aws-kms-mrk-aware")),
                              ("key", String(keyId))
                            ]),
          decrypt := if filter.Some? then
            Object([
                     ("type", String("aws-kms-mrk-aware-discovery")),
                     ("default-mrk-region", String("us-west-2")),
                     ("aws-kms-discovery-filter", Object(
                      [
                      ("partition", String(filter.value.partition)),
                      ("account-ids", Array(
                      Seq.Map(s => String(s), filter.value.accountIds)))
                      ]))
                   ])
          else
            Object([
                     ("type", String("aws-kms-mrk-aware-discovery")),
                     ("default-mrk-region", String("us-west-2"))])
        )

  const Tests :=
    set
      keyDescription <- AllKmsMrkAwareDiscovery,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
