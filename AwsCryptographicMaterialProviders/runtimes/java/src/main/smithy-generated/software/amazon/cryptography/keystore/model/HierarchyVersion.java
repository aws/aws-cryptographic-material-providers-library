// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

/**
 * Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.
 */
public enum HierarchyVersion {
  v1("1"),

  v2("2");

  private final String value;

  private HierarchyVersion(String value) {
    this.value = value;
  }

  public String toString() {
    return String.valueOf(value);
  }
}
