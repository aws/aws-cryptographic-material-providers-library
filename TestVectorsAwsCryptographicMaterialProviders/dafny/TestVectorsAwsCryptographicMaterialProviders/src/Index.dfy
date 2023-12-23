// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "LibraryIndex.dfy"
include "MplManifestOptions.dfy"
include "TestManifests.dfy"
include "CompleteVectors.dfy"

module {:options "-functionSyntax:4"} WrappedMaterialProvidersMain {
  import opened Wrappers
  import MplManifestOptions
  import Seq
  import GetOpt
  import CompleteVectors
  import TestManifests

  method Main(args: seq<string>) 
  {
    // The expectation is that the first argument
    // is the filename or runtime
    expect 0 < |args|;

    var vectorRunnerCommands := [
      GetOpt.Command(GetOpt.Options("decrypt", "decrypt test options", [
        GetOpt.Opt("manifest-path", "local path to manifest location", unused := GetOpt.Required),
        GetOpt.Opt("test-name", "test only one vector")])),
      GetOpt.Command(GetOpt.Options("encrypt", "encrypt test options", [
        GetOpt.Opt("manifest-path", "local path to manifest location", unused := GetOpt.Required),
        GetOpt.Opt("decrypt-manifest-output", "local output location for encrypt manifest", unused := GetOpt.Required),
        GetOpt.Opt("test-name", "test only one vector")])),
      GetOpt.Command(GetOpt.Options("encrypt-manifest", "writes encrypt manifest test vectors", [
        GetOpt.Opt("encrypt-manifest-output", "local path to write encrypt manifest test vector to", unused := GetOpt.Required)]))
    ];

    var vectorRunnerOptions := GetOpt.Options("testvectors", "test the mpl testvectors", vectorRunnerCommands);
    var parsedOptions? := GetOpt.GetOptions(vectorRunnerOptions, args);

    var cmd? := ParseCLICmds(parsedOptions?);

    if cmd?.Success? {
      var cmd := cmd?.value;
      if
      case cmd.Decrypt? =>
      // var _ :- expect EsdkTestManifests.StartDecryptVectors(op);
      case cmd.Encrypt? =>
        var result := TestManifests.StartEncrypt(cmd);
        if result.Failure? {
          print result.error;
        }
        expect result.Success?;
      case cmd.EncryptManifest? =>
        var result := CompleteVectors.WriteStuff(cmd);
        if result.Failure? {
          print result.error;
        }
        expect result.Success?;
    } else {
      print cmd?.error;
    }
  }

  function ParseCLICmds(parsedArgs: Result<GetOpt.Parsed, string>)
    : (output: Result<MplManifestOptions.ManifestOptions, string>)
  {
    :- Need(parsedArgs.Success?, "Unable to parse CLI commands");

    match parsedArgs.value.command
    case "decrypt" => ParseDecryptCommand(parsedArgs.value.params)
    case "encrypt" => ParseEncryptCommand(parsedArgs.value.params)
    case "encrypt-manifest" => ParseEncryptManifestCommand(parsedArgs.value.params)
    case _ => Failure("unknown command")
  }

  function ParseDecryptCommand(params: seq<GetOpt.OneArg>)
    : (output: Result<MplManifestOptions.ManifestOptions, string>)
  {
    var manifestPath? := GetOpt.OptValue(params, "manifest-path");
    var testName? := GetOpt.OptValue(params, "test-name");

    if !manifestPath?.Some? then Failure("manifest-path requires a value")
    else
      :- Need(0 < |manifestPath?.value|, "Invalid manifest-path length");
      Success(MplManifestOptions.Decrypt(
        manifestPath := if Seq.Last(manifestPath?.value) == '/' then manifestPath?.value else manifestPath?.value + "/",
        testName := if testName?.Some? then Some(testName?.value) else None
      ))
  }

  function ParseEncryptCommand(params: seq<GetOpt.OneArg>)
    : (output: Result<MplManifestOptions.ManifestOptions, string>)
  {
    var manifestPath? := GetOpt.OptValue(params, "manifest-path");
    var decryptManifestOutput? := GetOpt.OptValue(params, "decrypt-manifest-output");
    var testName? := GetOpt.OptValue(params, "test-name");
    
    if !manifestPath?.Some? then Failure("manifest-path requires a value")
    else if !decryptManifestOutput?.Some? then Failure("decrypt-manifest-output requires a value")
    else
      :- Need(0 < |manifestPath?.value|, "Invalid manifest-path length");
      Success(MplManifestOptions.Encrypt(
        manifestPath := if Seq.Last(manifestPath?.value) == '/' then manifestPath?.value else manifestPath?.value + "/",
        decryptManifestOutput := decryptManifestOutput?.value,
        testName := if testName?.Some? then Some(testName?.value) else None
      ))
  }

  function ParseEncryptManifestCommand(params: seq<GetOpt.OneArg>)
    : (output: Result<MplManifestOptions.ManifestOptions, string>)
  {
    var encryptManifestOutput? := GetOpt.OptValue(params, "encrypt-manifest-output");

    if !encryptManifestOutput?.Some? then Failure("encrypt-manifest-output")
    else
      :- Need(0 < |encryptManifestOutput?.value|, "Invalid manifest-path length");
      Success(MplManifestOptions.EncryptManifest(
          encryptManifestOutput := if Seq.Last(encryptManifestOutput?.value) == '/' then encryptManifestOutput?.value else encryptManifestOutput?.value + "/" 
      ))
  }

  predicate CommandOption?(s: string)
  {
    || s == "decrypt"
    || s == "encrypt"
    || s == "encrypt-manifest"
  }

  predicate DecryptOptions?(op: map<string, string>)
  {
    && 1 <= |op| <= 2
    && "-manifest-path" in op
    && 0 < |op["-manifest-path"]|
    && (|op| == 2 ==> "-test-name" in op)
  }

  predicate EncryptOptions?(op: map<string, string>)
  {
    && 3 <= |op| <= 4
    && "-manifest-path" in op
    && 0 < |op["-manifest-path"]|
    && "-decrypt-manifest-output" in op
    && (|op| == 4 ==> "-test-name" in op)
  }

  predicate EncryptManifestOptions?(op: map<string, string>)
  {
    && 1 <= |op| <= 2
    && "-encrypt-manifest-output" in op
    && 0 < |op["-encrypt-manifest-output"]|
  }

  predicate DecryptSingleOptions?(op: map<string, string>)
  {
    && 3 == |op|
    && "-keys-path" in op
    && "-key-description" in op
    && "-base64-bytes" in op
  }

  predicate DecryptRequiredOptions?(s: string)
  {
    || s == "manifest-path"
  }

  function Options2Map(args: seq<string>)
    : (map<string, string>)
    requires |args| % 2 == 0
  {
    if |args| == 0 then
      map[]
    else
      var key, value := args[0], args[1];
      map[key := value] + Options2Map(args[2..])
  }

}
