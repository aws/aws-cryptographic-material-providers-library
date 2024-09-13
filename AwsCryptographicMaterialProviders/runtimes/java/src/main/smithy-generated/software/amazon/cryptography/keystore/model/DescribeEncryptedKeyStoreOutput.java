// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class DescribeEncryptedKeyStoreOutput {

  private final String Name;

  protected DescribeEncryptedKeyStoreOutput(BuilderImpl builder) {
    this.Name = builder.Name();
  }

  public String Name() {
    return this.Name;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Name(String Name);

    String Name();

    DescribeEncryptedKeyStoreOutput build();
  }

  static class BuilderImpl implements Builder {

    protected String Name;

    protected BuilderImpl() {}

    protected BuilderImpl(DescribeEncryptedKeyStoreOutput model) {
      this.Name = model.Name();
    }

    public Builder Name(String Name) {
      this.Name = Name;
      return this;
    }

    public String Name() {
      return this.Name;
    }

    public DescribeEncryptedKeyStoreOutput build() {
      if (Objects.isNull(this.Name())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Name`"
        );
      }
      return new DescribeEncryptedKeyStoreOutput(this);
    }
  }
}
