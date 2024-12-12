// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

/**
 * If a Mutation is In Flight for this Branch Key.
 */
public class MutationInFlight {

  private final MutationDescription Yes;

  private final String No;

  protected MutationInFlight(BuilderImpl builder) {
    this.Yes = builder.Yes();
    this.No = builder.No();
  }

  public MutationDescription Yes() {
    return this.Yes;
  }

  public String No() {
    return this.No;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Yes(MutationDescription Yes);

    MutationDescription Yes();

    Builder No(String No);

    String No();

    MutationInFlight build();
  }

  static class BuilderImpl implements Builder {

    protected MutationDescription Yes;

    protected String No;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationInFlight model) {
      this.Yes = model.Yes();
      this.No = model.No();
    }

    public Builder Yes(MutationDescription Yes) {
      this.Yes = Yes;
      return this;
    }

    public MutationDescription Yes() {
      return this.Yes;
    }

    public Builder No(String No) {
      this.No = No;
      return this;
    }

    public String No() {
      return this.No;
    }

    public MutationInFlight build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`MutationInFlight` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new MutationInFlight(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.Yes, this.No };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
