// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

/**
 * The Storage is trusted enough for items of non-cryptographic material nature,
 * even if those items can affect the cryptographic materials.
 * Permissions to modify the data store are sufficient
 * to influence the contents of mutations in flight
 * without needing a KMS key permission,
 * which would otherwise be needed to do the same.
 */
public class TrustStorage {

  protected TrustStorage(BuilderImpl builder) {}

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    TrustStorage build();
  }

  static class BuilderImpl implements Builder {

    protected BuilderImpl() {}

    protected BuilderImpl(TrustStorage model) {}

    public TrustStorage build() {
      return new TrustStorage(this);
    }
  }
}
