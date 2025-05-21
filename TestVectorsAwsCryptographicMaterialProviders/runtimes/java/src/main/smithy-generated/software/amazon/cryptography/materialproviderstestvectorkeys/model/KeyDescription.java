// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviderstestvectorkeys.model;

import java.util.Objects;

public class KeyDescription {

  private final KMSInfo Kms;

  private final KmsMrkAware KmsMrk;

  private final KmsMrkAwareDiscovery KmsMrkDiscovery;

  private final RawRSA RSA;

  private final RawAES AES;

  private final RawEcdh ECDH;

  private final StaticKeyring Static;

  private final KmsRsaKeyring KmsRsa;

  private final KmsEcdhKeyring KmsECDH;

  private final HierarchyKeyring Hierarchy;

  private final MultiKeyring Multi;

  private final RequiredEncryptionContextCMM RequiredEncryptionContext;

  protected KeyDescription(BuilderImpl builder) {
    this.Kms = builder.Kms();
    this.KmsMrk = builder.KmsMrk();
    this.KmsMrkDiscovery = builder.KmsMrkDiscovery();
    this.RSA = builder.RSA();
    this.AES = builder.AES();
    this.ECDH = builder.ECDH();
    this.Static = builder.Static();
    this.KmsRsa = builder.KmsRsa();
    this.KmsECDH = builder.KmsECDH();
    this.Hierarchy = builder.Hierarchy();
    this.Multi = builder.Multi();
    this.RequiredEncryptionContext = builder.RequiredEncryptionContext();
  }

  public KMSInfo Kms() {
    return this.Kms;
  }

  public KmsMrkAware KmsMrk() {
    return this.KmsMrk;
  }

  public KmsMrkAwareDiscovery KmsMrkDiscovery() {
    return this.KmsMrkDiscovery;
  }

  public RawRSA RSA() {
    return this.RSA;
  }

  public RawAES AES() {
    return this.AES;
  }

  public RawEcdh ECDH() {
    return this.ECDH;
  }

  public StaticKeyring Static() {
    return this.Static;
  }

  public KmsRsaKeyring KmsRsa() {
    return this.KmsRsa;
  }

  public KmsEcdhKeyring KmsECDH() {
    return this.KmsECDH;
  }

  public HierarchyKeyring Hierarchy() {
    return this.Hierarchy;
  }

  public MultiKeyring Multi() {
    return this.Multi;
  }

  public RequiredEncryptionContextCMM RequiredEncryptionContext() {
    return this.RequiredEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Kms(KMSInfo Kms);

    KMSInfo Kms();

    Builder KmsMrk(KmsMrkAware KmsMrk);

    KmsMrkAware KmsMrk();

    Builder KmsMrkDiscovery(KmsMrkAwareDiscovery KmsMrkDiscovery);

    KmsMrkAwareDiscovery KmsMrkDiscovery();

    Builder RSA(RawRSA RSA);

    RawRSA RSA();

    Builder AES(RawAES AES);

    RawAES AES();

    Builder ECDH(RawEcdh ECDH);

    RawEcdh ECDH();

    Builder Static(StaticKeyring Static);

    StaticKeyring Static();

    Builder KmsRsa(KmsRsaKeyring KmsRsa);

    KmsRsaKeyring KmsRsa();

    Builder KmsECDH(KmsEcdhKeyring KmsECDH);

    KmsEcdhKeyring KmsECDH();

    Builder Hierarchy(HierarchyKeyring Hierarchy);

    HierarchyKeyring Hierarchy();

    Builder Multi(MultiKeyring Multi);

    MultiKeyring Multi();

    Builder RequiredEncryptionContext(
      RequiredEncryptionContextCMM RequiredEncryptionContext
    );

    RequiredEncryptionContextCMM RequiredEncryptionContext();

    KeyDescription build();
  }

  static class BuilderImpl implements Builder {

    protected KMSInfo Kms;

    protected KmsMrkAware KmsMrk;

    protected KmsMrkAwareDiscovery KmsMrkDiscovery;

    protected RawRSA RSA;

    protected RawAES AES;

    protected RawEcdh ECDH;

    protected StaticKeyring Static;

    protected KmsRsaKeyring KmsRsa;

    protected KmsEcdhKeyring KmsECDH;

    protected HierarchyKeyring Hierarchy;

    protected MultiKeyring Multi;

    protected RequiredEncryptionContextCMM RequiredEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyDescription model) {
      this.Kms = model.Kms();
      this.KmsMrk = model.KmsMrk();
      this.KmsMrkDiscovery = model.KmsMrkDiscovery();
      this.RSA = model.RSA();
      this.AES = model.AES();
      this.ECDH = model.ECDH();
      this.Static = model.Static();
      this.KmsRsa = model.KmsRsa();
      this.KmsECDH = model.KmsECDH();
      this.Hierarchy = model.Hierarchy();
      this.Multi = model.Multi();
      this.RequiredEncryptionContext = model.RequiredEncryptionContext();
    }

    public Builder Kms(KMSInfo Kms) {
      this.Kms = Kms;
      return this;
    }

    public KMSInfo Kms() {
      return this.Kms;
    }

    public Builder KmsMrk(KmsMrkAware KmsMrk) {
      this.KmsMrk = KmsMrk;
      return this;
    }

    public KmsMrkAware KmsMrk() {
      return this.KmsMrk;
    }

    public Builder KmsMrkDiscovery(KmsMrkAwareDiscovery KmsMrkDiscovery) {
      this.KmsMrkDiscovery = KmsMrkDiscovery;
      return this;
    }

    public KmsMrkAwareDiscovery KmsMrkDiscovery() {
      return this.KmsMrkDiscovery;
    }

    public Builder RSA(RawRSA RSA) {
      this.RSA = RSA;
      return this;
    }

    public RawRSA RSA() {
      return this.RSA;
    }

    public Builder AES(RawAES AES) {
      this.AES = AES;
      return this;
    }

    public RawAES AES() {
      return this.AES;
    }

    public Builder ECDH(RawEcdh ECDH) {
      this.ECDH = ECDH;
      return this;
    }

    public RawEcdh ECDH() {
      return this.ECDH;
    }

    public Builder Static(StaticKeyring Static) {
      this.Static = Static;
      return this;
    }

    public StaticKeyring Static() {
      return this.Static;
    }

    public Builder KmsRsa(KmsRsaKeyring KmsRsa) {
      this.KmsRsa = KmsRsa;
      return this;
    }

    public KmsRsaKeyring KmsRsa() {
      return this.KmsRsa;
    }

    public Builder KmsECDH(KmsEcdhKeyring KmsECDH) {
      this.KmsECDH = KmsECDH;
      return this;
    }

    public KmsEcdhKeyring KmsECDH() {
      return this.KmsECDH;
    }

    public Builder Hierarchy(HierarchyKeyring Hierarchy) {
      this.Hierarchy = Hierarchy;
      return this;
    }

    public HierarchyKeyring Hierarchy() {
      return this.Hierarchy;
    }

    public Builder Multi(MultiKeyring Multi) {
      this.Multi = Multi;
      return this;
    }

    public MultiKeyring Multi() {
      return this.Multi;
    }

    public Builder RequiredEncryptionContext(
      RequiredEncryptionContextCMM RequiredEncryptionContext
    ) {
      this.RequiredEncryptionContext = RequiredEncryptionContext;
      return this;
    }

    public RequiredEncryptionContextCMM RequiredEncryptionContext() {
      return this.RequiredEncryptionContext;
    }

    public KeyDescription build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KeyDescription` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KeyDescription(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.Kms,
        this.KmsMrk,
        this.KmsMrkDiscovery,
        this.RSA,
        this.AES,
        this.ECDH,
        this.Static,
        this.KmsRsa,
        this.KmsECDH,
        this.Hierarchy,
        this.Multi,
        this.RequiredEncryptionContext,
      };
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
