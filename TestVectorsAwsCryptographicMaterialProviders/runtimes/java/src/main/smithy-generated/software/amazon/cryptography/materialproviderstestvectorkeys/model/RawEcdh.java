// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviderstestvectorkeys.model;

import java.util.Objects;

public class RawEcdh {

  private final String senderKeyId;

  private final String recipientKeyId;

  private final String senderPublicKey;

  private final String recipientPublicKey;

  private final String providerId;

  private final String curveSpec;

  private final String keyAgreementScheme;

  protected RawEcdh(BuilderImpl builder) {
    this.senderKeyId = builder.senderKeyId();
    this.recipientKeyId = builder.recipientKeyId();
    this.senderPublicKey = builder.senderPublicKey();
    this.recipientPublicKey = builder.recipientPublicKey();
    this.providerId = builder.providerId();
    this.curveSpec = builder.curveSpec();
    this.keyAgreementScheme = builder.keyAgreementScheme();
  }

  public String senderKeyId() {
    return this.senderKeyId;
  }

  public String recipientKeyId() {
    return this.recipientKeyId;
  }

  public String senderPublicKey() {
    return this.senderPublicKey;
  }

  public String recipientPublicKey() {
    return this.recipientPublicKey;
  }

  public String providerId() {
    return this.providerId;
  }

  public String curveSpec() {
    return this.curveSpec;
  }

  public String keyAgreementScheme() {
    return this.keyAgreementScheme;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder senderKeyId(String senderKeyId);

    String senderKeyId();

    Builder recipientKeyId(String recipientKeyId);

    String recipientKeyId();

    Builder senderPublicKey(String senderPublicKey);

    String senderPublicKey();

    Builder recipientPublicKey(String recipientPublicKey);

    String recipientPublicKey();

    Builder providerId(String providerId);

    String providerId();

    Builder curveSpec(String curveSpec);

    String curveSpec();

    Builder keyAgreementScheme(String keyAgreementScheme);

    String keyAgreementScheme();

    RawEcdh build();
  }

  static class BuilderImpl implements Builder {

    protected String senderKeyId;

    protected String recipientKeyId;

    protected String senderPublicKey;

    protected String recipientPublicKey;

    protected String providerId;

    protected String curveSpec;

    protected String keyAgreementScheme;

    protected BuilderImpl() {}

    protected BuilderImpl(RawEcdh model) {
      this.senderKeyId = model.senderKeyId();
      this.recipientKeyId = model.recipientKeyId();
      this.senderPublicKey = model.senderPublicKey();
      this.recipientPublicKey = model.recipientPublicKey();
      this.providerId = model.providerId();
      this.curveSpec = model.curveSpec();
      this.keyAgreementScheme = model.keyAgreementScheme();
    }

    public Builder senderKeyId(String senderKeyId) {
      this.senderKeyId = senderKeyId;
      return this;
    }

    public String senderKeyId() {
      return this.senderKeyId;
    }

    public Builder recipientKeyId(String recipientKeyId) {
      this.recipientKeyId = recipientKeyId;
      return this;
    }

    public String recipientKeyId() {
      return this.recipientKeyId;
    }

    public Builder senderPublicKey(String senderPublicKey) {
      this.senderPublicKey = senderPublicKey;
      return this;
    }

    public String senderPublicKey() {
      return this.senderPublicKey;
    }

    public Builder recipientPublicKey(String recipientPublicKey) {
      this.recipientPublicKey = recipientPublicKey;
      return this;
    }

    public String recipientPublicKey() {
      return this.recipientPublicKey;
    }

    public Builder providerId(String providerId) {
      this.providerId = providerId;
      return this;
    }

    public String providerId() {
      return this.providerId;
    }

    public Builder curveSpec(String curveSpec) {
      this.curveSpec = curveSpec;
      return this;
    }

    public String curveSpec() {
      return this.curveSpec;
    }

    public Builder keyAgreementScheme(String keyAgreementScheme) {
      this.keyAgreementScheme = keyAgreementScheme;
      return this;
    }

    public String keyAgreementScheme() {
      return this.keyAgreementScheme;
    }

    public RawEcdh build() {
      if (Objects.isNull(this.senderKeyId())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderKeyId`"
        );
      }
      if (Objects.isNull(this.recipientKeyId())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientKeyId`"
        );
      }
      if (Objects.isNull(this.senderPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderPublicKey`"
        );
      }
      if (Objects.isNull(this.recipientPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientPublicKey`"
        );
      }
      if (Objects.isNull(this.providerId())) {
        throw new IllegalArgumentException(
          "Missing value for required field `providerId`"
        );
      }
      if (Objects.isNull(this.curveSpec())) {
        throw new IllegalArgumentException(
          "Missing value for required field `curveSpec`"
        );
      }
      if (Objects.isNull(this.keyAgreementScheme())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyAgreementScheme`"
        );
      }
      return new RawEcdh(this);
    }
  }
}
