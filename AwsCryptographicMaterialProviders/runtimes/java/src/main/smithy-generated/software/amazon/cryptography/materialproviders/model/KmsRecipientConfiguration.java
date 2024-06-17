// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class KmsRecipientConfiguration {

  private final String RecipientKmsKeyId;

  private final ByteBuffer RecipientPublicKey;

  protected KmsRecipientConfiguration(BuilderImpl builder) {
    this.RecipientKmsKeyId = builder.RecipientKmsKeyId();
    this.RecipientPublicKey = builder.RecipientPublicKey();
  }

  public String RecipientKmsKeyId() {
    return this.RecipientKmsKeyId;
  }

  public ByteBuffer RecipientPublicKey() {
    return this.RecipientPublicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder RecipientKmsKeyId(String RecipientKmsKeyId);

    String RecipientKmsKeyId();

    Builder RecipientPublicKey(ByteBuffer RecipientPublicKey);

    ByteBuffer RecipientPublicKey();

    KmsRecipientConfiguration build();
  }

  static class BuilderImpl implements Builder {

    protected String RecipientKmsKeyId;

    protected ByteBuffer RecipientPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsRecipientConfiguration model) {
      this.RecipientKmsKeyId = model.RecipientKmsKeyId();
      this.RecipientPublicKey = model.RecipientPublicKey();
    }

    public Builder RecipientKmsKeyId(String RecipientKmsKeyId) {
      this.RecipientKmsKeyId = RecipientKmsKeyId;
      return this;
    }

    public String RecipientKmsKeyId() {
      return this.RecipientKmsKeyId;
    }

    public Builder RecipientPublicKey(ByteBuffer RecipientPublicKey) {
      this.RecipientPublicKey = RecipientPublicKey;
      return this;
    }

    public ByteBuffer RecipientPublicKey() {
      return this.RecipientPublicKey;
    }

    public KmsRecipientConfiguration build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KmsRecipientConfiguration` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KmsRecipientConfiguration(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.RecipientKmsKeyId, this.RecipientPublicKey };
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
