// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Test vector projects just run as a CLI
// So all the tests are in the Main.
// By creating a single file here,
// it is easy to kick off a test run.
include "../src/Index.dfy"

module TestWrappedMaterialProvidersMain {
  import WrappedMaterialProvidersMain
  import TestManifests
  import CompleteVectors
  import opened MplManifestOptions

  // Test execution directory is different for different runtimes.
  // Runtime should define an extern to return the expected test execution directory.
  method  GetTestVectorExecutionDirectory() returns (res: string) 
  {
    return "";
  }

  // This MUST go before TestEncryptManifest
  method {:test} TestGenerateEncryptManifest() {
    var directory := GetTestVectorExecutionDirectory();
    var result := CompleteVectors.WriteStuff(
      EncryptManifest(
        encryptManifestOutput := directory + "dafny/TestVectorsAwsCryptographicMaterialProviders/test/"
      ));
    if result.Failure? {
      print result.error;
    }
    expect result.Success?;
  }

  // This MUST go before TestDecryptManifest
  method {:test} TestEncryptManifest() {
    var directory := GetTestVectorExecutionDirectory();
    var result := TestManifests.StartEncrypt(
      Encrypt(
        manifestPath := directory + "dafny/TestVectorsAwsCryptographicMaterialProviders/test/",
        decryptManifestOutput := directory + "dafny/TestVectorsAwsCryptographicMaterialProviders/"
      )
    );
    if result.Failure? {
      print result.error;
    }
    expect result.Success?;
  }

  method {:test} TestDecryptManifest() {
    var directory := GetTestVectorExecutionDirectory();
    var result := TestManifests.StartDecrypt(
      Decrypt(
        manifestPath := directory + "dafny/TestVectorsAwsCryptographicMaterialProviders/"
      )
    );
    if result.Failure? {
      print result;
    }
    expect result.Success?;
  }

}
