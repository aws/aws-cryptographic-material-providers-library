// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class InitializeMutationFlag {

  /**
   * This is a new mutation.
   */
  private final String Created;

  /**
   * A matching mutation already existed.
   */
  private final String Resumed;

  /**
   * A matching mutation already existed, but no Page Index was found.
   */
  private final String ResumedWithoutIndex;

  protected InitializeMutationFlag(BuilderImpl builder) {
    this.Created = builder.Created();
    this.Resumed = builder.Resumed();
    this.ResumedWithoutIndex = builder.ResumedWithoutIndex();
  }

  /**
   * @return This is a new mutation.
   */
  public String Created() {
    return this.Created;
  }

  /**
   * @return A matching mutation already existed.
   */
  public String Resumed() {
    return this.Resumed;
  }

  /**
   * @return A matching mutation already existed, but no Page Index was found.
   */
  public String ResumedWithoutIndex() {
    return this.ResumedWithoutIndex;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Created This is a new mutation.
     */
    Builder Created(String Created);

    /**
     * @return This is a new mutation.
     */
    String Created();

    /**
     * @param Resumed A matching mutation already existed.
     */
    Builder Resumed(String Resumed);

    /**
     * @return A matching mutation already existed.
     */
    String Resumed();

    /**
     * @param ResumedWithoutIndex A matching mutation already existed, but no Page Index was found.
     */
    Builder ResumedWithoutIndex(String ResumedWithoutIndex);

    /**
     * @return A matching mutation already existed, but no Page Index was found.
     */
    String ResumedWithoutIndex();

    InitializeMutationFlag build();
  }

  static class BuilderImpl implements Builder {

    protected String Created;

    protected String Resumed;

    protected String ResumedWithoutIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationFlag model) {
      this.Created = model.Created();
      this.Resumed = model.Resumed();
      this.ResumedWithoutIndex = model.ResumedWithoutIndex();
    }

    public Builder Created(String Created) {
      this.Created = Created;
      return this;
    }

    public String Created() {
      return this.Created;
    }

    public Builder Resumed(String Resumed) {
      this.Resumed = Resumed;
      return this;
    }

    public String Resumed() {
      return this.Resumed;
    }

    public Builder ResumedWithoutIndex(String ResumedWithoutIndex) {
      this.ResumedWithoutIndex = ResumedWithoutIndex;
      return this;
    }

    public String ResumedWithoutIndex() {
      return this.ResumedWithoutIndex;
    }

    public InitializeMutationFlag build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`InitializeMutationFlag` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new InitializeMutationFlag(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.Created,
        this.Resumed,
        this.ResumedWithoutIndex,
      };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
