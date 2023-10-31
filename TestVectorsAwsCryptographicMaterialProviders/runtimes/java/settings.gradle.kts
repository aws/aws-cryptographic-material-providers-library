// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

rootProject.name = "TestVectorsAwsCryptographicMaterialProviders"

includeBuild(File("../../../AwsCryptographicMaterialProviders/runtimes/java/")) {
  name = "AwsCryptographicMaterialProviders"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:aws-cryptographic-material-providers")).using(project(":"))
  }
}
