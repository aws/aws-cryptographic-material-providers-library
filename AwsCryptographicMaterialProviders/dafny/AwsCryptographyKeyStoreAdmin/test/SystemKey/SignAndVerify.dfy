// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"
include "../../src/SystemKey.dfy"

// Tests that the System Key can:
// - Sign an arbitrary content
// - Verify an arbitrary content
// - Fail to verify tampered content

module {:options "/functionSyntax:4" } SignAndVerify {
  import opened Wrappers
  import Fixtures
  import AdminFixtures
  import KMS = Com.Amazonaws.Kms
  import SystemKey
  import Structure
  import UTF8

  const MutationCommitmentContentToSHA :=
    map[
      UTF8.EncodeAscii(Structure.HIERARCHY_VERSION) := UTF8.EncodeAscii(Structure.HIERARCHY_VERSION_VALUE),
      UTF8.EncodeAscii(Structure.KEY_CREATE_TIME) := UTF8.EncodeAscii("now"),
      UTF8.EncodeAscii(Structure.M_ORIGINAL) := UTF8.EncodeAscii("system-key-does-not-validate-original-content"),
      UTF8.EncodeAscii(Structure.M_TERMINAL) := UTF8.EncodeAscii("system-key-does-not-validate-terminal-content"),
      UTF8.EncodeAscii(Structure.M_INPUT) := UTF8.EncodeAscii("system-key-does-not-validate-input-content")
    ]

  const MutationCommitmentContent :=
    SystemKey.Content(
      ContentToSHA := MutationCommitmentContentToSHA,
      PartionValue := "a-branch-key-id",
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := "a-uuid")

  const TamperedMutationCommitmentContent :=
    SystemKey.Content(
      ContentToSHA := MutationCommitmentContentToSHA,
      PartionValue := "a-branch-key-id",
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := "b-uuid")

  const kmsId: string := Fixtures.publicKeyArn

  lemma TestValuesAreValid()
    ensures MutationCommitmentContent.ValidState()
    ensures KMS.Types.IsValid_KeyIdType(kmsId)
    ensures TamperedMutationCommitmentContent.ValidState()
  {}

  method ActualSign(
    input: SystemKey.SignInput,
    logPrefix: string
  )
    returns (output: Result<KMS.Types.CiphertextType, SystemKey.SignError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    assert input.ValidState();
    // assume {:axiom} false; // Tony cannot figure out why the Modifies clause is violated
    var output? := SystemKey.SignContent(input);
    // These prints are helpful for debugging
    // print logPrefix + " Attempted to Sign was succesful? " + if output?.Success? then "Yes" else "No" + " .\n";
    // if (output?.Failure?) {
    //   print logPrefix + " Error\t";
    //   print output?.error;
    //   print "\n";
    // } else {
    //   print logPrefix + " Result:\t";
    //   print output?.value;
    //   print "\n";
    // }
    return output?;
  }

  method ActualVerify(
    input: SystemKey.VerifyInput,
    logPrefix: string
  )
    returns (output: Result<bool, SystemKey.VerifyError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    assert input.ValidState();
    // assume {:axiom} false; // Tony cannot figure out why the Modifies clause is violated
    var output? := SystemKey.VerifyContent(input);
    // These prints are helpful for debugging
    // print logPrefix + " Attempted to Verify was succesful? " + if output?.Success? then "Yes" else "No" + " .\n";
    // if (output?.Failure?) {
    //   print logPrefix + " Error\t";
    //   print output?.error;
    //   print "\n";
    // } else {
    //   print logPrefix + " Result:\t";
    //   print output?.value;
    //   print "\n";
    // }
    return output?;
  }

  const SignCommitmentLogPrefix := "\nSignAndVerify :: SignCommitment "
  method {:test} SignCommitment()
  {
    print " running";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    assert fresh(kmsTuple.Modifies);
    var crypto :- expect SystemKey.ProvideCryptoClient();
    assert fresh(crypto) && fresh(crypto.Modifies);
    var input := SystemKey.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert input.ValidState();
    var output? := ActualSign(input, SignCommitmentLogPrefix); //SystemKey.SignContent(input);
    expect output?.Success?, "System Key failed to SignContent when it should have succeeded.";
    print "SignAndVerify.SignCommitment: ";
  }

  const SignAndVerifyCommitmentLogPrefix := "\nSignAndVerify :: SignAndVerifyCommitment "
  method {:test} SignAndVerifyCommitment()
  {
    print " running";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    var crypto :- expect SystemKey.ProvideCryptoClient();
    var signInput := SystemKey.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert signInput.ValidState();
    var signOutput? := ActualSign(signInput, SignAndVerifyCommitmentLogPrefix); //SystemKey.SignContent(input);
    expect signOutput?.Success?, "System Key failed to SignContent when it should have succeeded.";
    var verifyInput := SystemKey.VerifyInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      CiphertextBlob := signOutput?.value,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    var verifyOutput? := ActualVerify(verifyInput, SignAndVerifyCommitmentLogPrefix);
    expect verifyOutput?.Success?, "System Key failed to VerifyContent when it should have succeeded.";
    print "SignAndVerify.SignAndVerifyCommitment: ";
  }

  const SignAndFailVerifyCommitmentLogPrefix := "\nSignAndVerify :: SignAndFailVerifyCommitment "
  method {:test} SignAndFailVerifyCommitment()
  {
    print " running";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    var crypto :- expect SystemKey.ProvideCryptoClient();
    var signInput := SystemKey.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert signInput.ValidState();
    var signOutput? := ActualSign(signInput, SignAndFailVerifyCommitmentLogPrefix); //SystemKey.SignContent(input);
    expect signOutput?.Success?, "System Key failed to SignContent when it should have succeeded.";

    var verifyInput := SystemKey.VerifyInput(
      MaterialIdentifier := kmsId,
      Content := TamperedMutationCommitmentContent,
      CiphertextBlob := signOutput?.value,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    var verifyOutput? := ActualVerify(verifyInput, SignAndFailVerifyCommitmentLogPrefix);
    expect verifyOutput?.Failure?, "System Key should have failed to VerifyContent when it succeeded.";
    print "SignAndVerify.SignAndFailVerifyCommitment: ";
  }

}
