// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

public enum EccCurveSpec {
  ECC_NIST_P256("secp256r1"),

  ECC_NIST_P384("secp384r1"),

  ECC_NIST_P521("secp521r1"),

  SM2("SM2PKE");

  private final String value;

  private EccCurveSpec(String value) {
    this.value = value;
  }

  public String toString() {
    return String.valueOf(value);
  }
}
