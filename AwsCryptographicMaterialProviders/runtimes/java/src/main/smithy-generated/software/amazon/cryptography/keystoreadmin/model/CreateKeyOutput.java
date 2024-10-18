// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class CreateKeyOutput {

  /**
   * A identifier for the created Branch Key.
   */
  private final String Identifier;

  protected CreateKeyOutput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return A identifier for the created Branch Key.
   */
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
    /**
     * @param Identifier A identifier for the created Branch Key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return A identifier for the created Branch Key.
     */
    String Identifier();

    CreateKeyOutput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateKeyOutput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public CreateKeyOutput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new CreateKeyOutput(this);
    }
  }
}
