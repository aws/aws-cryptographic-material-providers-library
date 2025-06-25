// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

rootProject.name = "AwsCryptographyMetrics"

includeBuild(File("../../../StandardLibrary/runtimes/java/")) {
  name = "StandardLibrary"
  dependencySubstitution {
    substitute(module("software.amazon.cryptography:StandardLibrary")).using(project(":"))
  }
}
