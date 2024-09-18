// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class DescribeMutationOutput {

  /**
   * If a Mutation is In Flight for this Branch Key.
   */
  private final MutationInFlight MutationInFlight;

  protected DescribeMutationOutput(BuilderImpl builder) {
    this.MutationInFlight = builder.MutationInFlight();
  }

  /**
   * @return If a Mutation is In Flight for this Branch Key.
   */
  public MutationInFlight MutationInFlight() {
    return this.MutationInFlight;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param MutationInFlight If a Mutation is In Flight for this Branch Key.
     */
    Builder MutationInFlight(MutationInFlight MutationInFlight);

    /**
     * @return If a Mutation is In Flight for this Branch Key.
     */
    MutationInFlight MutationInFlight();

    DescribeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationInFlight MutationInFlight;

    protected BuilderImpl() {}

    protected BuilderImpl(DescribeMutationOutput model) {
      this.MutationInFlight = model.MutationInFlight();
    }

    public Builder MutationInFlight(MutationInFlight MutationInFlight) {
      this.MutationInFlight = MutationInFlight;
      return this;
    }

    public MutationInFlight MutationInFlight() {
      return this.MutationInFlight;
    }

    public DescribeMutationOutput build() {
      if (Objects.isNull(this.MutationInFlight())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationInFlight`"
        );
      }
      return new DescribeMutationOutput(this);
    }
  }
}
