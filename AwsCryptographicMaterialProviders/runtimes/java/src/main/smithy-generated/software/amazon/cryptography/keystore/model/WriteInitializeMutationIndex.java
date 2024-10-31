// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Write Initialize Mutation allows Mutations to either create or update the Index.
 */
public class WriteInitializeMutationIndex {

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex create;

  /**
   * To avoid information loss, overwrites to any itme in the Key Store
   * are done conditioned on the old value.
   */
  private final OverWriteMutationIndex update;

  protected WriteInitializeMutationIndex(BuilderImpl builder) {
    this.create = builder.create();
    this.update = builder.update();
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex create() {
    return this.create;
  }

  /**
   * @return To avoid information loss, overwrites to any itme in the Key Store
   * are done conditioned on the old value.
   */
  public OverWriteMutationIndex update() {
    return this.update;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param create Information on an in-flight Mutation of a Branch Key.
     */
    Builder create(MutationIndex create);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex create();

    /**
     * @param update To avoid information loss, overwrites to any itme in the Key Store
     * are done conditioned on the old value.
     */
    Builder update(OverWriteMutationIndex update);

    /**
     * @return To avoid information loss, overwrites to any itme in the Key Store
     * are done conditioned on the old value.
     */
    OverWriteMutationIndex update();

    WriteInitializeMutationIndex build();
  }

  static class BuilderImpl implements Builder {

    protected MutationIndex create;

    protected OverWriteMutationIndex update;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationIndex model) {
      this.create = model.create();
      this.update = model.update();
    }

    public Builder create(MutationIndex create) {
      this.create = create;
      return this;
    }

    public MutationIndex create() {
      return this.create;
    }

    public Builder update(OverWriteMutationIndex update) {
      this.update = update;
      return this;
    }

    public OverWriteMutationIndex update() {
      return this.update;
    }

    public WriteInitializeMutationIndex build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`WriteInitializeMutationIndex` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new WriteInitializeMutationIndex(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.create, this.update };
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
