// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetEncryptedBranchKeyVersionInput {

  private final String Identifier;

  private final String Version;

  protected GetEncryptedBranchKeyVersionInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Version = builder.Version();
  }

  public String Identifier() {
    return this.Identifier;
  }

  public String Version() {
    return this.Version;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Identifier(String Identifier);

    String Identifier();

    Builder Version(String Version);

    String Version();

    GetEncryptedBranchKeyVersionInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected String Version;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedBranchKeyVersionInput model) {
      this.Identifier = model.Identifier();
      this.Version = model.Version();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Version(String Version) {
      this.Version = Version;
      return this;
    }

    public String Version() {
      return this.Version;
    }

    public GetEncryptedBranchKeyVersionInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Version`"
        );
      }
      return new GetEncryptedBranchKeyVersionInput(this);
    }
  }
}
