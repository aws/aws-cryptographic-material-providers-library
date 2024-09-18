// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class WriteInitializeMutationOutput {

  protected WriteInitializeMutationOutput(BuilderImpl builder) {}

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    WriteInitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationOutput model) {}

    public WriteInitializeMutationOutput build() {
      return new WriteInitializeMutationOutput(this);
    }
  }
}
