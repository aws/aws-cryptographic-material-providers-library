// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "TestVectors.dfy"
include "JSONHelpers.dfy"

include "./VectorsComposition/AllAlgorithmSuites.dfy"
include "../../../../StandardLibrary/src/Time.dfy"

include "./VectorsComposition/AllDefaultCmm.dfy"
include "./VectorsComposition/AllHierarchy.dfy"
include "./VectorsComposition/AllKms.dfy"
include "./VectorsComposition/AllKmsMrkAware.dfy"
include "./VectorsComposition/AllKmsMrkAwareDiscovery.dfy"
include "./VectorsComposition/AllKmsRsa.dfy"
include "./VectorsComposition/AllKmsEcdh.dfy"
include "./VectorsComposition/AllRawAES.dfy"
include "./VectorsComposition/AllRawECDH.dfy"
include "./VectorsComposition/AllRawRSA.dfy"
include "./VectorsComposition/AllMulti.dfy"
include "./VectorsComposition/AllRequiredEncryptionContextCmm.dfy"
include "MplManifestOptions.dfy"
include "WriteJsonManifests.dfy"

module {:options "-functionSyntax:4"} CompleteVectors {

  import AllHierarchy
  import AllKms
  import AllKmsMrkAware
  import AllKmsMrkAwareDiscovery
  import AllKmsRsa
  import AllKmsEcdh
  import AllRawAES
  import AllRawRSA
  import AllRawECDH
  import AllDefaultCmm
  import AllRequiredEncryptionContextCmm
  import AllMulti

  import AllAlgorithmSuites
  import opened JSON.Values
  import JSON.Errors
  import opened Wrappers
  import opened StandardLibrary.UInt
  import UUID
  import JSONHelpers
  import JSON.API
  import SortedSets
  import FileIO
  import MplManifestOptions
  import WriteJsonManifests
  import TestVectors
  import KeyVectors
  import Time

  // TODO serialize commitment policy

  const AllPositiveKeyringTests
  := {}
  // + AllDefaultCmm.Tests
  // + AllHierarchy.Tests
  // + AllKms.Tests
  // + AllKmsMrkAware.Tests
  // + AllKmsMrkAwareDiscovery.Tests
  // + AllKmsRsa.Tests
  + AllRawAES.Tests
  // + AllRawRSA.Tests
  // + AllMulti.Tests
  + AllRequiredEncryptionContextCmm.Tests
  // + AllRawECDH.Tests
  // + AllKmsEcdh.Tests

  method WriteStuff(op: MplManifestOptions.ManifestOptions)
    returns (output: Result<(), string>)
    requires op.EncryptManifest?
  {
    var time := Time.GetAbsoluteTime();

    var tests := SortedSets.ComputeSetToSequence(AllPositiveKeyringTests);
    // So that we can build the tests
    var testsJSON: seq<(string, JSON)> := [];

    for i := 0 to |tests|
    {
      var name :- UUID.GenerateUUID();
      var test :- WriteJsonManifests.EncryptTestVectorToJson(tests[i]);
      testsJSON := testsJSON + [(name, test)];
    }

    var mplEncryptManifest := Object(
      [
        ("manifest", Object([
         ("version", Number(Int(4))),
         ("type", String("awses-mpl-encrypt"))
         ])),
        ("keys", String("file://keys.json")),
        ("tests", Object(testsJSON))
      ]);

    var mplEncryptManifestBytes :- API.Serialize(mplEncryptManifest)
    .MapFailure(( e: Errors.SerializationError ) => e.ToString());
    var _ :- WriteVectorsFile(
      op.encryptManifestOutput + "manifest.json",
      mplEncryptManifestBytes
    );

    Time.PrintTimeSince(time);
    output := Success(());
  }

  method WriteDecryptManifest(
    op: MplManifestOptions.ManifestOptions,
    keys: KeyVectors.KeyVectorsClient,
    tests: seq<TestVectors.DecryptTestVector>
  )
    returns (output: Result<(), string>)
    requires op.Encrypt?
    requires keys.ValidState()
    ensures keys.ValidState()
  {
    // So that we can build the tests
    var testsJSON: seq<(string, JSON)> := [];

    for i := 0 to |tests|
    {
      var name :- UUID.GenerateUUID();
      var test :- WriteJsonManifests.DecryptTestVectorToJson(tests[i]);
      testsJSON := testsJSON + [(name, test)];
    }

    var mplDecryptManifest := Object(
      [
        ("manifest", Object([
         ("version", Number(Int(4))),
         ("type", String("awses-mpl-decrypt"))
         ])),
        ("client", String("mpl-dafny")),
        ("keys", String("file://keys.json")),
        ("tests", Object(testsJSON))
      ]);

    var mplDecryptManifestBytes :- API.Serialize(mplDecryptManifest)
    .MapFailure(( e: Errors.SerializationError ) => e.ToString());
    var _ :- WriteVectorsFile(
      op.decryptManifestOutput + "manifest.json",
      mplDecryptManifestBytes
    );

    var keysJsonFileName := "keys.json";
    // Write the keys to disk
    var keysJsonBytes :- API.Serialize(keys.config.keysJson)
    .MapFailure(( e: Errors.SerializationError ) => e.ToString());
    var _ :- WriteVectorsFile(
      op.decryptManifestOutput + keysJsonFileName,
      keysJsonBytes
    );

    output := Success(());
  }

  method WriteVectorsFile(location: string, bytes: seq<uint8>)
    returns (output: Result<(), string>)
  {
    var bv := JSONHelpers.BytesBv(bytes);
    output := FileIO.WriteBytesToFile(location, bv);
  }

}
