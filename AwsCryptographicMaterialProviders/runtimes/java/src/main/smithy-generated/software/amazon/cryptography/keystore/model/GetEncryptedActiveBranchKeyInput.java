// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetEncryptedActiveBranchKeyInput {

  private final String Identifier;

  protected GetEncryptedActiveBranchKeyInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  public String Identifier() {
    return this.Identifier;
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

    GetEncryptedActiveBranchKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedActiveBranchKeyInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetEncryptedActiveBranchKeyInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetEncryptedActiveBranchKeyInput(this);
    }
  }
}
