// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

rootProject.name = "TestVectorsAwsCryptographicMaterialProviders"

includeBuild(File("../../../AwsCryptographicMaterialProviders/runtimes/java/")) {
  name = "AwsCryptographicMaterialProviders"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:aws-cryptographic-material-providers")).using(project(":"))
  }
}

includeBuild(File("../../../StandardLibrary/runtimes/java/")) {
  name = "StandardLibrary"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:StandardLibrary")).using(project(":"))
  }
}

includeBuild(File("../../../AwsCryptographyPrimitives/runtimes/java/")) {
  name = "AwsCryptographyPrimitives"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:AwsCryptographyPrimitives")).using(project(":"))
  }
}

includeBuild(File("../../../ComAmazonawsDynamodb/runtimes/java/")) {
  name = "ComAmazonawsDynamodb"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:ComAmazonawsDynamodb")).using(project(":"))
  }
}

includeBuild(File("../../../ComAmazonawsKms/runtimes/java/")) {
  name = "ComAmazonawsKms"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:ComAmazonawsKms")).using(project(":"))
  }
}
