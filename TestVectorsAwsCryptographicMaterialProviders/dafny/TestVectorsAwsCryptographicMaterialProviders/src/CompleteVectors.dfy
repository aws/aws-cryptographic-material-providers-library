// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "TestVectors.dfy"
include "JSONHelpers.dfy"

include "./VectorsComposition/AllAlgorithmSuites.dfy"
include "./VectorsComposition/AllHierarchy.dfy"
include "./VectorsComposition/AllKms.dfy"
include "./VectorsComposition/AllKmsMrkAware.dfy"
include "./VectorsComposition/AllKmsMrkAwareDiscovery.dfy"
include "./VectorsComposition/AllKmsRsa.dfy"
include "./VectorsComposition/AllRawAES.dfy"
include "./VectorsComposition/AllRawRSA.dfy"
include "./VectorsComposition/KeyDescriptionJson.dfy"
include "./VectorsComposition/AllDefaultCmm.dfy"
include "./VectorsComposition/AllCachingCmm.dfy"
include "./VectorsComposition/AllRequiredEncryptionContextCmm.dfy"

module {:options "-functionSyntax:4"} CompleteVectors {

  import AllAlgorithmSuites
  import AllHierarchy
  import AllKms
  import AllKmsMrkAware
  import AllKmsMrkAwareDiscovery
  import AllKmsRsa
  import AllRawAES
  import AllRawRSA
  import KeyDescriptionJson
  import AllDefaultCmm
  import AllCachingCmm
  import AllRequiredEncryptionContextCmm

  import opened JSON.Values
  import UUID
  import JSONHelpers
  import JSON.API
  import SortedSets
  import FileIO

  // TODO Add a path to write manifest to
  // TODO Add negative encrypt tests
  // TODO Add negative decrypt tests
  // TODO Add additional manifest data to decrypt manifest
  // TODO support required encryption context
  // TODO serialize commitment policy
  // TODO serialize maxPlaintextLength

  const AllPositiveKeyringTests
    := {}
    + AllKms.Tests
    + AllKmsMrkAware.Tests
    + AllKmsMrkAwareDiscovery.Tests
    + AllRawAES.Tests
    + AllRawRSA.Tests
    + AllHierarchy.Tests
    + AllKmsRsa.Tests
    + AllDefaultCmm.Tests
    + AllCachingCmm.Tests

  method WriteStuff() {

    var tests := SortedSets.ComputeSetToSequence(AllPositiveKeyringTests);
    // So that we can build the tests
    var testsJSON: seq<(string, JSON)> := [];

    for i := 0 to |tests|
    {
      var name :- expect UUID.GenerateUUID();
      testsJSON := testsJSON + [(name, tests[i])];
    }

    var mplEncryptManifest := Object(
      [
        ("tests", Object(testsJSON))
      ]);

    var mplEncryptManifestBytes :- expect API.Serialize(mplEncryptManifest);
    var mplEncryptManifestBv := JSONHelpers.BytesBv(mplEncryptManifestBytes);

    var _ :- expect FileIO.WriteBytesToFile(
      "dafny/TestVectorsAwsCryptographicMaterialProviders/test/test.json",
      mplEncryptManifestBv
    );
  }

}
