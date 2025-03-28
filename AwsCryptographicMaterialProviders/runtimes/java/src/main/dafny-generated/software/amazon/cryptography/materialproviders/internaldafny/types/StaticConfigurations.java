// Class StaticConfigurations
// Dafny class StaticConfigurations compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class StaticConfigurations {
  public StaticConfigurations() {
  }
  private static final dafny.TypeDescriptor<StaticConfigurations> _TYPE = dafny.TypeDescriptor.<StaticConfigurations>referenceWithInitializer(StaticConfigurations.class, () -> StaticConfigurations.Default());
  public static dafny.TypeDescriptor<StaticConfigurations> _typeDescriptor() {
    return (dafny.TypeDescriptor<StaticConfigurations>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StaticConfigurations theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.StaticConfigurations.create_AWS__KMS__ECDH(KmsEcdhStaticConfigurations.Default());
  public static StaticConfigurations Default() {
    return theDefault;
  }
  public static StaticConfigurations create_AWS__KMS__ECDH(KmsEcdhStaticConfigurations AWS__KMS__ECDH) {
    return new StaticConfigurations_AWS__KMS__ECDH(AWS__KMS__ECDH);
  }
  public static StaticConfigurations create_RAW__ECDH(RawEcdhStaticConfigurations RAW__ECDH) {
    return new StaticConfigurations_RAW__ECDH(RAW__ECDH);
  }
  public boolean is_AWS__KMS__ECDH() { return this instanceof StaticConfigurations_AWS__KMS__ECDH; }
  public boolean is_RAW__ECDH() { return this instanceof StaticConfigurations_RAW__ECDH; }
  public KmsEcdhStaticConfigurations dtor_AWS__KMS__ECDH() {
    StaticConfigurations d = this;
    return ((StaticConfigurations_AWS__KMS__ECDH)d)._AWS__KMS__ECDH;
  }
  public RawEcdhStaticConfigurations dtor_RAW__ECDH() {
    StaticConfigurations d = this;
    return ((StaticConfigurations_RAW__ECDH)d)._RAW__ECDH;
  }
}
