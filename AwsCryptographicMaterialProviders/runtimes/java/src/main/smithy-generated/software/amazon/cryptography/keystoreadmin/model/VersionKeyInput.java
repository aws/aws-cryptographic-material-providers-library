// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.awssdk.services.kms.KmsClient;

/**
 * Inputs for versioning a Branch Key.
 */
public class VersionKeyInput {

  /**
   * The identifier for the Branch Key to be versioned.
   */
  private final String branchKeyIdentifier;

  /**
   * Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  private final String kmsArn;

  /**
   * The KMS client this Key Store uses to call AWS KMS.
   */
  private final KmsClient kmsClient;

  protected VersionKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.kmsArn = builder.kmsArn();
    this.kmsClient = builder.kmsClient();
  }

  /**
   * @return The identifier for the Branch Key to be versioned.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  public String kmsArn() {
    return this.kmsArn;
  }

  /**
   * @return The KMS client this Key Store uses to call AWS KMS.
   */
  public KmsClient kmsClient() {
    return this.kmsClient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the Branch Key to be versioned.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the Branch Key to be versioned.
     */
    String branchKeyIdentifier();

    /**
     * @param kmsArn Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    Builder kmsArn(String kmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    String kmsArn();

    /**
     * @param kmsClient The KMS client this Key Store uses to call AWS KMS.
     */
    Builder kmsClient(KmsClient kmsClient);

    /**
     * @return The KMS client this Key Store uses to call AWS KMS.
     */
    KmsClient kmsClient();

    VersionKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected String kmsArn;

    protected KmsClient kmsClient;

    protected BuilderImpl() {}

    protected BuilderImpl(VersionKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.kmsArn = model.kmsArn();
      this.kmsClient = model.kmsClient();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder kmsArn(String kmsArn) {
      this.kmsArn = kmsArn;
      return this;
    }

    public String kmsArn() {
      return this.kmsArn;
    }

    public Builder kmsClient(KmsClient kmsClient) {
      this.kmsClient = kmsClient;
      return this;
    }

    public KmsClient kmsClient() {
      return this.kmsClient;
    }

    public VersionKeyInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      if (Objects.isNull(this.kmsClient())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsClient`"
        );
      }
      return new VersionKeyInput(this);
    }
  }
}
