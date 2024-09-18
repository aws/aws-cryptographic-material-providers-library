// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import software.amazon.awssdk.services.kms.KmsClient;

public class AwsKms {

  /**
   * The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  private final List<String> grantTokens;

  /**
   * The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  private final KmsClient kmsClient;

  protected AwsKms(BuilderImpl builder) {
    this.grantTokens = builder.grantTokens();
    this.kmsClient = builder.kmsClient();
  }

  /**
   * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
  }

  /**
   * @return The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
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
     * @param grantTokens The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    List<String> grantTokens();

    /**
     * @param kmsClient The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    Builder kmsClient(KmsClient kmsClient);

    /**
     * @return The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    KmsClient kmsClient();

    AwsKms build();
  }

  static class BuilderImpl implements Builder {

    protected List<String> grantTokens;

    protected KmsClient kmsClient;

    protected BuilderImpl() {}

    protected BuilderImpl(AwsKms model) {
      this.grantTokens = model.grantTokens();
      this.kmsClient = model.kmsClient();
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public Builder kmsClient(KmsClient kmsClient) {
      this.kmsClient = kmsClient;
      return this;
    }

    public KmsClient kmsClient() {
      return this.kmsClient;
    }

    public AwsKms build() {
      return new AwsKms(this);
    }
  }
}
