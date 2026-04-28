// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

/**
 * Outputs for getting branch key versions.
 */
public class GetBranchKeyVersionsOutput {

  /**
   * The list of decrypted branch key materials.
   */
  private final List<BranchKeyMaterials> branchKeyMaterials;

  protected GetBranchKeyVersionsOutput(BuilderImpl builder) {
    this.branchKeyMaterials = builder.branchKeyMaterials();
  }

  /**
   * @return The list of decrypted branch key materials.
   */
  public List<BranchKeyMaterials> branchKeyMaterials() {
    return this.branchKeyMaterials;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyMaterials The list of decrypted branch key materials.
     */
    Builder branchKeyMaterials(List<BranchKeyMaterials> branchKeyMaterials);

    /**
     * @return The list of decrypted branch key materials.
     */
    List<BranchKeyMaterials> branchKeyMaterials();

    GetBranchKeyVersionsOutput build();
  }

  static class BuilderImpl implements Builder {

    protected List<BranchKeyMaterials> branchKeyMaterials;

    protected BuilderImpl() {}

    protected BuilderImpl(GetBranchKeyVersionsOutput model) {
      this.branchKeyMaterials = model.branchKeyMaterials();
    }

    public Builder branchKeyMaterials(
      List<BranchKeyMaterials> branchKeyMaterials
    ) {
      this.branchKeyMaterials = branchKeyMaterials;
      return this;
    }

    public List<BranchKeyMaterials> branchKeyMaterials() {
      return this.branchKeyMaterials;
    }

    public GetBranchKeyVersionsOutput build() {
      if (Objects.isNull(this.branchKeyMaterials())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyMaterials`"
        );
      }
      return new GetBranchKeyVersionsOutput(this);
    }
  }
}
