// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

/**
 * The hierarchy-version of a Branch Key;
 *   all items of the same Branch Key SHOULD
 *   have the same hierarchy-version.
 *   The hierarchy-version determines how the Branch Key Store classes
 *   treat the Branch Keys.
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
