// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class KMSIdentifier {

  private final String kmsKeyArn;

  private final String kmsMRKeyArn;

  protected KMSIdentifier(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.kmsMRKeyArn = builder.kmsMRKeyArn();
  }

  /**
   * @return
   */
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return
   */
  public String kmsMRKeyArn() {
    return this.kmsMRKeyArn;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn
     */
    Builder kmsKeyArn(String kmsKeyArn);

    /**
     * @return
     */
    String kmsKeyArn();

    /**
     * @param kmsMRKeyArn
     */
    Builder kmsMRKeyArn(String kmsMRKeyArn);

    /**
     * @return
     */
    String kmsMRKeyArn();

    KMSIdentifier build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected String kmsMRKeyArn;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSIdentifier model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.kmsMRKeyArn = model.kmsMRKeyArn();
    }

    public Builder kmsKeyArn(String kmsKeyArn) {
      this.kmsKeyArn = kmsKeyArn;
      return this;
    }

    public String kmsKeyArn() {
      return this.kmsKeyArn;
    }

    public Builder kmsMRKeyArn(String kmsMRKeyArn) {
      this.kmsMRKeyArn = kmsMRKeyArn;
      return this;
    }

    public String kmsMRKeyArn() {
      return this.kmsMRKeyArn;
    }

    public KMSIdentifier build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KMSIdentifier` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KMSIdentifier(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsKeyArn, this.kmsMRKeyArn };
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
