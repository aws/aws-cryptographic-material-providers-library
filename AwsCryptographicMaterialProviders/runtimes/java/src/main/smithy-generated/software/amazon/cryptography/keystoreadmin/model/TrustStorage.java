// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

/**
 * The Storage is trusted enough for items of non-cryptographic material nature,
 * even if those items can affect the cryptographic materials.
 * Thus, permissions to modify the Key Store's storage is sufficient
 * to influence the properties of mutations in flight
 * without needing a KMS key permission,
 * which would otherwise be needed to do the same.
 * As an extreme example,
 * an actor with only write access to the storage
 * could modify an in-flight Mutation's terminal KMS Key ARN.
 * Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
 * instead of 'Trust Storage' to ensure that Branch Keys are
 * only modified via actors with KMS key permissions.
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
