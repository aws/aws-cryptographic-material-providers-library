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
  // TODO: - Replace all /Users/lucmcdon/work... below with call to this function
  //       - Write this extern in Python to return absolute path (import os; return os.getcwd() should do it)
  //       - Write this extern in NET/Java to return empty sring
  // method {:extern} GetTestDirectory() returns (res: Result<string, Types.OpaqueError>)

  // This MUST go before TestEncryptManifest
  method {:test} TestGenerateEncryptManifest() {
    var result := CompleteVectors.WriteStuff(
      EncryptManifest(
        encryptManifestOutput := "/Users/lucmcdon/workplace/aws-cryptographic-material-providers-library/TestVectorsAwsCryptographicMaterialProviders/dafny/TestVectorsAwsCryptographicMaterialProviders/test/"
      ));
    if result.Failure? {
      print result.error;
    }
    expect result.Success?;
  }

  // This MUST go before TestDecryptManifest
  method {:test} TestEncryptManifest() {
    var result := TestManifests.StartEncrypt(
      Encrypt(
        manifestPath := "/Users/lucmcdon/workplace/aws-cryptographic-material-providers-library/TestVectorsAwsCryptographicMaterialProviders/dafny/TestVectorsAwsCryptographicMaterialProviders/test/",
        decryptManifestOutput := "/Users/lucmcdon/workplace/aws-cryptographic-material-providers-library/TestVectorsAwsCryptographicMaterialProviders/dafny/TestVectorsAwsCryptographicMaterialProviders/"
      )
    );
    if result.Failure? {
      print result.error;
    }
    expect result.Success?;
  }

  method {:test} TestDecryptManifest() {
    var result := TestManifests.StartDecrypt(
      Decrypt(
        manifestPath := "/Users/lucmcdon/workplace/aws-cryptographic-material-providers-library/TestVectorsAwsCryptographicMaterialProviders/dafny/TestVectorsAwsCryptographicMaterialProviders/"
      )
    );
    if result.Failure? {
      print result;
    }
    expect result.Success?;
  }

}
