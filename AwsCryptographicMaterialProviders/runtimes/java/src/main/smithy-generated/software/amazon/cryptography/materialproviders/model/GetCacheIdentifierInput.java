// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.Keyring;

/**
 * Inputs for computing a cache identifier.
 */
public class GetCacheIdentifierInput {

  /**
   * The Hierarchical Keyring whose internal state is used to compute the cache identifier.
   */
  private final IKeyring keyring;

  /**
   * The branch key identifier.
   */
  private final String branchKeyId;

  /**
   * The branch key version. If provided, computes the decrypt-path cache identifier. If omitted, computes the encrypt-path cache identifier.
   */
  private final String branchKeyVersion;

  protected GetCacheIdentifierInput(BuilderImpl builder) {
    this.keyring = builder.keyring();
    this.branchKeyId = builder.branchKeyId();
    this.branchKeyVersion = builder.branchKeyVersion();
  }

  /**
   * @return The Hierarchical Keyring whose internal state is used to compute the cache identifier.
   */
  public IKeyring keyring() {
    return this.keyring;
  }

  /**
   * @return The branch key identifier.
   */
  public String branchKeyId() {
    return this.branchKeyId;
  }

  /**
   * @return The branch key version. If provided, computes the decrypt-path cache identifier. If omitted, computes the encrypt-path cache identifier.
   */
  public String branchKeyVersion() {
    return this.branchKeyVersion;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param keyring The Hierarchical Keyring whose internal state is used to compute the cache identifier.
     */
    Builder keyring(IKeyring keyring);

    /**
     * @return The Hierarchical Keyring whose internal state is used to compute the cache identifier.
     */
    IKeyring keyring();

    /**
     * @param branchKeyId The branch key identifier.
     */
    Builder branchKeyId(String branchKeyId);

    /**
     * @return The branch key identifier.
     */
    String branchKeyId();

    /**
     * @param branchKeyVersion The branch key version. If provided, computes the decrypt-path cache identifier. If omitted, computes the encrypt-path cache identifier.
     */
    Builder branchKeyVersion(String branchKeyVersion);

    /**
     * @return The branch key version. If provided, computes the decrypt-path cache identifier. If omitted, computes the encrypt-path cache identifier.
     */
    String branchKeyVersion();

    GetCacheIdentifierInput build();
  }

  static class BuilderImpl implements Builder {

    protected IKeyring keyring;

    protected String branchKeyId;

    protected String branchKeyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(GetCacheIdentifierInput model) {
      this.keyring = model.keyring();
      this.branchKeyId = model.branchKeyId();
      this.branchKeyVersion = model.branchKeyVersion();
    }

    public Builder keyring(IKeyring keyring) {
      this.keyring = Keyring.wrap(keyring);
      return this;
    }

    public IKeyring keyring() {
      return this.keyring;
    }

    public Builder branchKeyId(String branchKeyId) {
      this.branchKeyId = branchKeyId;
      return this;
    }

    public String branchKeyId() {
      return this.branchKeyId;
    }

    public Builder branchKeyVersion(String branchKeyVersion) {
      this.branchKeyVersion = branchKeyVersion;
      return this;
    }

    public String branchKeyVersion() {
      return this.branchKeyVersion;
    }

    public GetCacheIdentifierInput build() {
      if (Objects.isNull(this.keyring())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyring`"
        );
      }
      if (Objects.isNull(this.branchKeyId())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyId`"
        );
      }
      return new GetCacheIdentifierInput(this);
    }
  }
}
