// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class MutationDescription {

  /**
   * Detailed description of the Mutation for this Branch Key.
   */
  private final MutationDetails MutationDetails;

  /**
   * This token can be passed to Apply Mutation to continue the Mutation.
   */
  private final MutationToken MutationToken;

  /**
   * ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
   */
  private final String LastModifiedTime;

  protected MutationDescription(BuilderImpl builder) {
    this.MutationDetails = builder.MutationDetails();
    this.MutationToken = builder.MutationToken();
    this.LastModifiedTime = builder.LastModifiedTime();
  }

  /**
   * @return Detailed description of the Mutation for this Branch Key.
   */
  public MutationDetails MutationDetails() {
    return this.MutationDetails;
  }

  /**
   * @return This token can be passed to Apply Mutation to continue the Mutation.
   */
  public MutationToken MutationToken() {
    return this.MutationToken;
  }

  /**
   * @return ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
   */
  public String LastModifiedTime() {
    return this.LastModifiedTime;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param MutationDetails Detailed description of the Mutation for this Branch Key.
     */
    Builder MutationDetails(MutationDetails MutationDetails);

    /**
     * @return Detailed description of the Mutation for this Branch Key.
     */
    MutationDetails MutationDetails();

    /**
     * @param MutationToken This token can be passed to Apply Mutation to continue the Mutation.
     */
    Builder MutationToken(MutationToken MutationToken);

    /**
     * @return This token can be passed to Apply Mutation to continue the Mutation.
     */
    MutationToken MutationToken();

    /**
     * @param LastModifiedTime ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
     */
    Builder LastModifiedTime(String LastModifiedTime);

    /**
     * @return ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
     */
    String LastModifiedTime();

    MutationDescription build();
  }

  static class BuilderImpl implements Builder {

    protected MutationDetails MutationDetails;

    protected MutationToken MutationToken;

    protected String LastModifiedTime;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationDescription model) {
      this.MutationDetails = model.MutationDetails();
      this.MutationToken = model.MutationToken();
      this.LastModifiedTime = model.LastModifiedTime();
    }

    public Builder MutationDetails(MutationDetails MutationDetails) {
      this.MutationDetails = MutationDetails;
      return this;
    }

    public MutationDetails MutationDetails() {
      return this.MutationDetails;
    }

    public Builder MutationToken(MutationToken MutationToken) {
      this.MutationToken = MutationToken;
      return this;
    }

    public MutationToken MutationToken() {
      return this.MutationToken;
    }

    public Builder LastModifiedTime(String LastModifiedTime) {
      this.LastModifiedTime = LastModifiedTime;
      return this;
    }

    public String LastModifiedTime() {
      return this.LastModifiedTime;
    }

    public MutationDescription build() {
      if (Objects.isNull(this.MutationDetails())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationDetails`"
        );
      }
      if (Objects.isNull(this.MutationToken())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationToken`"
        );
      }
      return new MutationDescription(this);
    }
  }
}
