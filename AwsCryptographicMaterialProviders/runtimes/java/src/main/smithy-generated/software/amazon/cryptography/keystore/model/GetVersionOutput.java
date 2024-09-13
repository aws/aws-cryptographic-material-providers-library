// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetVersionOutput {

  private final EncryptedHierarchicalKey Item;

  protected GetVersionOutput(BuilderImpl builder) {
    this.Item = builder.Item();
  }

  public EncryptedHierarchicalKey Item() {
    return this.Item;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Item(EncryptedHierarchicalKey Item);

    EncryptedHierarchicalKey Item();

    GetVersionOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Item;

    protected BuilderImpl() {}

    protected BuilderImpl(GetVersionOutput model) {
      this.Item = model.Item();
    }

    public Builder Item(EncryptedHierarchicalKey Item) {
      this.Item = Item;
      return this;
    }

    public EncryptedHierarchicalKey Item() {
      return this.Item;
    }

    public GetVersionOutput build() {
      if (Objects.isNull(this.Item())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Item`"
        );
      }
      return new GetVersionOutput(this);
    }
  }
}
