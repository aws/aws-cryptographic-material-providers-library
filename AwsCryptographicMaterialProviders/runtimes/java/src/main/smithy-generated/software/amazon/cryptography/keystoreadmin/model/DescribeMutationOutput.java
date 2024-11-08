// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

public class DescribeMutationOutput {

  /**
   * The original properities of the Branch Key.
   */
  private final MutableBranchKeyProperities Original;

  /**
   * The terminal properities of the Branch Key.
   */
  private final MutableBranchKeyProperities Terminal;

  protected DescribeMutationOutput(BuilderImpl builder) {
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
  }

  /**
   * @return The original properities of the Branch Key.
   */
  public MutableBranchKeyProperities Original() {
    return this.Original;
  }

  /**
   * @return The terminal properities of the Branch Key.
   */
  public MutableBranchKeyProperities Terminal() {
    return this.Terminal;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Original The original properities of the Branch Key.
     */
    Builder Original(MutableBranchKeyProperities Original);

    /**
     * @return The original properities of the Branch Key.
     */
    MutableBranchKeyProperities Original();

    /**
     * @param Terminal The terminal properities of the Branch Key.
     */
    Builder Terminal(MutableBranchKeyProperities Terminal);

    /**
     * @return The terminal properities of the Branch Key.
     */
    MutableBranchKeyProperities Terminal();

    DescribeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutableBranchKeyProperities Original;

    protected MutableBranchKeyProperities Terminal;

    protected BuilderImpl() {}

    protected BuilderImpl(DescribeMutationOutput model) {
      this.Original = model.Original();
      this.Terminal = model.Terminal();
    }

    public Builder Original(MutableBranchKeyProperities Original) {
      this.Original = Original;
      return this;
    }

    public MutableBranchKeyProperities Original() {
      return this.Original;
    }

    public Builder Terminal(MutableBranchKeyProperities Terminal) {
      this.Terminal = Terminal;
      return this;
    }

    public MutableBranchKeyProperities Terminal() {
      return this.Terminal;
    }

    public DescribeMutationOutput build() {
      return new DescribeMutationOutput(this);
    }
  }
}
