// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class InitializeMutationInput {

  /**
   * The identifier for the Branch Key to be mutated.
   */
  private final String branchKeyIdentifier;

  /**
   * Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  private final Mutations mutations;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   */
  private final KeyManagementStrategy strategy;

  protected InitializeMutationInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.mutations = builder.mutations();
    this.strategy = builder.strategy();
  }

  /**
   * @return The identifier for the Branch Key to be mutated.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  public Mutations mutations() {
    return this.mutations;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   */
  public KeyManagementStrategy strategy() {
    return this.strategy;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the Branch Key to be mutated.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the Branch Key to be mutated.
     */
    String branchKeyIdentifier();

    /**
     * @param mutations Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Builder mutations(Mutations mutations);

    /**
     * @return Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Mutations mutations();

    /**
     * @param strategy Optional. Defaults to reEncrypt with a default KMS Client.
     */
    Builder strategy(KeyManagementStrategy strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     */
    KeyManagementStrategy strategy();

    InitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected Mutations mutations;

    protected KeyManagementStrategy strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.mutations = model.mutations();
      this.strategy = model.strategy();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder mutations(Mutations mutations) {
      this.mutations = mutations;
      return this;
    }

    public Mutations mutations() {
      return this.mutations;
    }

    public Builder strategy(KeyManagementStrategy strategy) {
      this.strategy = strategy;
      return this;
    }

    public KeyManagementStrategy strategy() {
      return this.strategy;
    }

    public InitializeMutationInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.mutations())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutations`"
        );
      }
      return new InitializeMutationInput(this);
    }
  }
}
