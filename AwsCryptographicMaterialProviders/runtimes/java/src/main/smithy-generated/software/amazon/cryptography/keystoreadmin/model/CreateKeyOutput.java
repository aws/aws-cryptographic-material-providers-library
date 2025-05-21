// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class CreateKeyOutput {

  /**
   * A identifier for the created Branch Key.
   */
  private final String Identifier;

  /**
   * The hierarchy-version of a Branch Key;
   *   all items of the same Branch Key SHOULD
   *   have the same hierarchy-version.
   *   The hierarchy-version determines how the Branch Key Store
   *   protects and validates the branch key context (BKC).
   */
  private final HierarchyVersion HierarchyVersion;

  protected CreateKeyOutput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.HierarchyVersion = builder.HierarchyVersion();
  }

  /**
   * @return A identifier for the created Branch Key.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The hierarchy-version of a Branch Key;
   *   all items of the same Branch Key SHOULD
   *   have the same hierarchy-version.
   *   The hierarchy-version determines how the Branch Key Store
   *   protects and validates the branch key context (BKC).
   */
  public HierarchyVersion HierarchyVersion() {
    return this.HierarchyVersion;
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

    /**
     * @param HierarchyVersion The hierarchy-version of a Branch Key;
     *   all items of the same Branch Key SHOULD
     *   have the same hierarchy-version.
     *   The hierarchy-version determines how the Branch Key Store
     *   protects and validates the branch key context (BKC).
     */
    Builder HierarchyVersion(HierarchyVersion HierarchyVersion);

    /**
     * @return The hierarchy-version of a Branch Key;
     *   all items of the same Branch Key SHOULD
     *   have the same hierarchy-version.
     *   The hierarchy-version determines how the Branch Key Store
     *   protects and validates the branch key context (BKC).
     */
    HierarchyVersion HierarchyVersion();

    CreateKeyOutput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected HierarchyVersion HierarchyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateKeyOutput model) {
      this.Identifier = model.Identifier();
      this.HierarchyVersion = model.HierarchyVersion();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder HierarchyVersion(HierarchyVersion HierarchyVersion) {
      this.HierarchyVersion = HierarchyVersion;
      return this;
    }

    public HierarchyVersion HierarchyVersion() {
      return this.HierarchyVersion;
    }

    public CreateKeyOutput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.HierarchyVersion())) {
        throw new IllegalArgumentException(
          "Missing value for required field `HierarchyVersion`"
        );
      }
      return new CreateKeyOutput(this);
    }
  }
}
