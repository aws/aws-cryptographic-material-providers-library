// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.primitives.model.HKDFProvider;

public class GetHKDFProviderOutput {

  private final HKDFProvider provider;

  protected GetHKDFProviderOutput(BuilderImpl builder) {
    this.provider = builder.provider();
  }

  public HKDFProvider provider() {
    return this.provider;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder provider(HKDFProvider provider);

    HKDFProvider provider();

    GetHKDFProviderOutput build();
  }

  static class BuilderImpl implements Builder {

    protected HKDFProvider provider;

    protected BuilderImpl() {}

    protected BuilderImpl(GetHKDFProviderOutput model) {
      this.provider = model.provider();
    }

    public Builder provider(HKDFProvider provider) {
      this.provider = provider;
      return this;
    }

    public HKDFProvider provider() {
      return this.provider;
    }

    public GetHKDFProviderOutput build() {
      if (Objects.isNull(this.provider())) {
        throw new IllegalArgumentException(
          "Missing value for required field `provider`"
        );
      }
      return new GetHKDFProviderOutput(this);
    }
  }
}
