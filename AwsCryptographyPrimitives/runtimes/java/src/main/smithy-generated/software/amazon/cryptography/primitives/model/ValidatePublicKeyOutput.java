// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class ValidatePublicKeyOutput {
  private final Boolean success;

  protected ValidatePublicKeyOutput(BuilderImpl builder) {
    this.success = builder.success();
  }

  public Boolean success() {
    return this.success;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder success(Boolean success);

    Boolean success();

    ValidatePublicKeyOutput build();
  }

  static class BuilderImpl implements Builder {
    protected Boolean success;

    protected BuilderImpl() {
    }

    protected BuilderImpl(ValidatePublicKeyOutput model) {
      this.success = model.success();
    }

    public Builder success(Boolean success) {
      this.success = success;
      return this;
    }

    public Boolean success() {
      return this.success;
    }

    public ValidatePublicKeyOutput build() {
      if (Objects.isNull(this.success()))  {
        throw new IllegalArgumentException("Missing value for required field `success`");
      }
      return new ValidatePublicKeyOutput(this);
    }
  }
}
