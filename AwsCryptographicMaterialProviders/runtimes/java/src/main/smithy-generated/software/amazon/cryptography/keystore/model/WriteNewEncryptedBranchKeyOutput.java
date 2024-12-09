// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

/**
 * The output of writing a new branch key. There is currently no additional information returned.
 */
public class WriteNewEncryptedBranchKeyOutput {

  protected WriteNewEncryptedBranchKeyOutput(BuilderImpl builder) {}

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    WriteNewEncryptedBranchKeyOutput build();
  }

  static class BuilderImpl implements Builder {

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewEncryptedBranchKeyOutput model) {}

    public WriteNewEncryptedBranchKeyOutput build() {
      return new WriteNewEncryptedBranchKeyOutput(this);
    }
  }
}
