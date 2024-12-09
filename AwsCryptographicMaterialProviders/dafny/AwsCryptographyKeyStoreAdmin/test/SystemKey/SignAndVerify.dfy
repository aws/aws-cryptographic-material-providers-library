// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"
include "../../src/SystemKey/ContentHandler.dfy"

// Tests that the SystemKey.ContentHandler can:
// - Sign an arbitrary content
// - Verify an arbitrary content
// - Fail to verify tampered content

module {:options "/functionSyntax:4" } TestContentHandler {
  import opened Wrappers
  import Fixtures
  import AdminFixtures
  import KMS = Com.Amazonaws.Kms
  import ContentHandler = SystemKey.ContentHandler
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
    ContentHandler.Content(
      ContentToSHA := MutationCommitmentContentToSHA,
      PartitionValue := "a-branch-key-id",
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := "a-uuid")

  const TamperedMutationCommitmentContent :=
    ContentHandler.Content(
      ContentToSHA := MutationCommitmentContentToSHA,
      PartitionValue := "a-branch-key-id",
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := "b-uuid")

  const kmsId: string := Fixtures.publicKeyArn

  lemma TestValuesAreValid()
    ensures MutationCommitmentContent.ValidState()
    ensures KMS.Types.IsValid_KeyIdType(kmsId)
    ensures TamperedMutationCommitmentContent.ValidState()
  {}

  method ActualSign(
    input: ContentHandler.SignInput,
    logPrefix: string
  )
    returns (output: Result<KMS.Types.CiphertextType, ContentHandler.SignError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    assert input.ValidState();
    var output? := ContentHandler.SignContent(input);
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
    input: ContentHandler.VerifyInput,
    logPrefix: string
  )
    returns (output: Result<bool, ContentHandler.VerifyError>)
    requires input.ValidState()
    ensures input.ValidState()
    modifies input.KmsTuple.Modifies
    modifies input.Crypto.Modifies
  {
    assert input.ValidState();
    var output? := ContentHandler.VerifyContent(input);
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

  const SignCommitmentLogPrefix := "\nTestContentHandler :: SignCommitment "
  method {:test} SignCommitment()
  {
    // print "running ";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    assert fresh(kmsTuple.Modifies);
    var crypto :- expect ContentHandler.ProvideCryptoClient();
    assert fresh(crypto) && fresh(crypto.Modifies);
    var input := ContentHandler.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert input.ValidState();
    var output? := ActualSign(input, SignCommitmentLogPrefix); //ContentHandler.SignContent(input);
    expect output?.Success?, "System Key failed to SignContent when it should have succeeded.";
    // print "\nTestContentHandler.SignCommitment: ";
  }

  const TestContentHandlerCommitmentLogPrefix := "\nTestContentHandler :: TestContentHandlerCommitment "
  method {:test} TestContentHandlerCommitment()
  {
    // print "running ";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    var crypto :- expect ContentHandler.ProvideCryptoClient();
    var signInput := ContentHandler.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert signInput.ValidState();
    var signOutput? := ActualSign(signInput, TestContentHandlerCommitmentLogPrefix); //ContentHandler.SignContent(input);
    expect signOutput?.Success?, "System Key failed to SignContent when it should have succeeded.";
    var verifyInput := ContentHandler.VerifyInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      CiphertextBlob := signOutput?.value,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    var verifyOutput? := ActualVerify(verifyInput, TestContentHandlerCommitmentLogPrefix);
    expect verifyOutput?.Success?, "System Key failed to VerifyContent when it should have succeeded.";
    // print "\nTestContentHandler.TestContentHandlerCommitment: ";
  }

  const SignAndFailVerifyCommitmentLogPrefix := "\nTestContentHandler :: SignAndFailVerifyCommitment "
  method {:test} SignAndFailVerifyCommitment()
  {
    // print "running ";
    var kmsTuple :- expect AdminFixtures.ProvideKMSTuple();
    var crypto :- expect ContentHandler.ProvideCryptoClient();
    var signInput := ContentHandler.SignInput(
      MaterialIdentifier := kmsId,
      Content := MutationCommitmentContent,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    assert signInput.ValidState();
    var signOutput? := ActualSign(signInput, SignAndFailVerifyCommitmentLogPrefix);
    expect signOutput?.Success?, "System Key failed to SignContent when it should have succeeded.";


    var verifyInput := ContentHandler.VerifyInput(
      MaterialIdentifier := kmsId,
      Content := TamperedMutationCommitmentContent,
      CiphertextBlob := signOutput?.value,
      KmsTuple := kmsTuple,
      Crypto := crypto);
    var verifyOutput? := ActualVerify(verifyInput, SignAndFailVerifyCommitmentLogPrefix);
    expect verifyOutput?.Success?, "System Key should have not errored on VerifyContent when it has been tampered.";
    expect verifyOutput?.value == false, "System Key should have returned false on VerifyContent when it has been tampered.";
    // print "\nTestContentHandler.SignAndFailVerifyCommitment: ";
  }

}
