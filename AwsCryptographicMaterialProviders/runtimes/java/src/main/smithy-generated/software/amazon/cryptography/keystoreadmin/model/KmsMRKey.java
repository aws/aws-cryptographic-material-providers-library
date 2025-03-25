// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

/**
 * If an MRK ARN is provided,
 * then the ARNs region will be replaced
 * with the provided region.
 */
public class KmsMRKey {

  /**
   * This MUST be a KMS MRK ARN; aliases and Single Region keys are rejected.
   */
  private final String KeyArn;

  /**
   * MRK ARN will have its region replaced with this.
   */
  private final String Region;

  protected KmsMRKey(BuilderImpl builder) {
    this.KeyArn = builder.KeyArn();
    this.Region = builder.Region();
  }

  /**
   * @return This MUST be a KMS MRK ARN; aliases and Single Region keys are rejected.
   */
  public String KeyArn() {
    return this.KeyArn;
  }

  /**
   * @return MRK ARN will have its region replaced with this.
   */
  public String Region() {
    return this.Region;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KeyArn This MUST be a KMS MRK ARN; aliases and Single Region keys are rejected.
     */
    Builder KeyArn(String KeyArn);

    /**
     * @return This MUST be a KMS MRK ARN; aliases and Single Region keys are rejected.
     */
    String KeyArn();

    /**
     * @param Region MRK ARN will have its region replaced with this.
     */
    Builder Region(String Region);

    /**
     * @return MRK ARN will have its region replaced with this.
     */
    String Region();

    KmsMRKey build();
  }

  static class BuilderImpl implements Builder {

    protected String KeyArn;

    protected String Region;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsMRKey model) {
      this.KeyArn = model.KeyArn();
      this.Region = model.Region();
    }

    public Builder KeyArn(String KeyArn) {
      this.KeyArn = KeyArn;
      return this;
    }

    public String KeyArn() {
      return this.KeyArn;
    }

    public Builder Region(String Region) {
      this.Region = Region;
      return this;
    }

    public String Region() {
      return this.Region;
    }

    public KmsMRKey build() {
      if (Objects.isNull(this.KeyArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KeyArn`"
        );
      }
      if (Objects.nonNull(this.KeyArn()) && this.KeyArn().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `KeyArn` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.KeyArn()) && this.KeyArn().length() > 2048) {
        throw new IllegalArgumentException(
          "The size of `KeyArn` must be less than or equal to 2048"
        );
      }
      if (Objects.isNull(this.Region())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Region`"
        );
      }
      if (Objects.nonNull(this.Region()) && this.Region().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `Region` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.Region()) && this.Region().length() > 32) {
        throw new IllegalArgumentException(
          "The size of `Region` must be less than or equal to 32"
        );
      }
      return new KmsMRKey(this);
    }
  }
}
