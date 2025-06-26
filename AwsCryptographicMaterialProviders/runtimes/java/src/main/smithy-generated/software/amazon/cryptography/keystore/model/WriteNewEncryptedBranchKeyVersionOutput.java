// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

/**
 * The output of writing a new version for an existing branch key. There is currently no additional information returned.
 */
public class WriteNewEncryptedBranchKeyVersionOutput {

  protected WriteNewEncryptedBranchKeyVersionOutput(BuilderImpl builder) {}

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    WriteNewEncryptedBranchKeyVersionOutput build();
  }

  static class BuilderImpl implements Builder {

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewEncryptedBranchKeyVersionOutput model) {}

    public WriteNewEncryptedBranchKeyVersionOutput build() {
      return new WriteNewEncryptedBranchKeyVersionOutput(this);
    }
  }
}
