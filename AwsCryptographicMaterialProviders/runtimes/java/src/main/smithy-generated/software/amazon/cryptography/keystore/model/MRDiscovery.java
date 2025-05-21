// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class MRDiscovery {

  /**
   * Any MRK ARN discovered will have its region replaced with this.
   */
  private final String region;

  protected MRDiscovery(BuilderImpl builder) {
    this.region = builder.region();
  }

  /**
   * @return Any MRK ARN discovered will have its region replaced with this.
   */
  public String region() {
    return this.region;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param region Any MRK ARN discovered will have its region replaced with this.
     */
    Builder region(String region);

    /**
     * @return Any MRK ARN discovered will have its region replaced with this.
     */
    String region();

    MRDiscovery build();
  }

  static class BuilderImpl implements Builder {

    protected String region;

    protected BuilderImpl() {}

    protected BuilderImpl(MRDiscovery model) {
      this.region = model.region();
    }

    public Builder region(String region) {
      this.region = region;
      return this;
    }

    public String region() {
      return this.region;
    }

    public MRDiscovery build() {
      if (Objects.isNull(this.region())) {
        throw new IllegalArgumentException(
          "Missing value for required field `region`"
        );
      }
      if (Objects.nonNull(this.region()) && this.region().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `region` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.region()) && this.region().length() > 32) {
        throw new IllegalArgumentException(
          "The size of `region` must be less than or equal to 32"
        );
      }
      return new MRDiscovery(this);
    }
  }
}
