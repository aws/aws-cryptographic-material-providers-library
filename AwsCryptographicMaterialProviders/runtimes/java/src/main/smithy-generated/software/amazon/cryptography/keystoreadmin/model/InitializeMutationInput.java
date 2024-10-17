// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class InitializeMutationInput {

  /**
   * The identifier for the Branch Key to be mutated.
   */
  private final String Identifier;

  /**
   * Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  private final Mutations Mutations;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   */
  private final KeyManagementStrategy Strategy;

  protected InitializeMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Mutations = builder.Mutations();
    this.Strategy = builder.Strategy();
  }

  /**
   * @return The identifier for the Branch Key to be mutated.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  public Mutations Mutations() {
    return this.Mutations;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   */
  public KeyManagementStrategy Strategy() {
    return this.Strategy;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key to be mutated.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to be mutated.
     */
    String Identifier();

    /**
     * @param Mutations Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Builder Mutations(Mutations Mutations);

    /**
     * @return Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Mutations Mutations();

    /**
     * @param Strategy Optional. Defaults to reEncrypt with a default KMS Client.
     */
    Builder Strategy(KeyManagementStrategy Strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     */
    KeyManagementStrategy Strategy();

    InitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected Mutations Mutations;

    protected KeyManagementStrategy Strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationInput model) {
      this.Identifier = model.Identifier();
      this.Mutations = model.Mutations();
      this.Strategy = model.Strategy();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Mutations(Mutations Mutations) {
      this.Mutations = Mutations;
      return this;
    }

    public Mutations Mutations() {
      return this.Mutations;
    }

    public Builder Strategy(KeyManagementStrategy Strategy) {
      this.Strategy = Strategy;
      return this;
    }

    public KeyManagementStrategy Strategy() {
      return this.Strategy;
    }

    public InitializeMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Mutations())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Mutations`"
        );
      }
      return new InitializeMutationInput(this);
    }
  }
}
