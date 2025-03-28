// Class KmsEcdhStaticConfigurations
// Dafny class KmsEcdhStaticConfigurations compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KmsEcdhStaticConfigurations {
  public KmsEcdhStaticConfigurations() {
  }
  private static final dafny.TypeDescriptor<KmsEcdhStaticConfigurations> _TYPE = dafny.TypeDescriptor.<KmsEcdhStaticConfigurations>referenceWithInitializer(KmsEcdhStaticConfigurations.class, () -> KmsEcdhStaticConfigurations.Default());
  public static dafny.TypeDescriptor<KmsEcdhStaticConfigurations> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsEcdhStaticConfigurations>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsEcdhStaticConfigurations theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPublicKeyDiscovery(KmsPublicKeyDiscoveryInput.Default());
  public static KmsEcdhStaticConfigurations Default() {
    return theDefault;
  }
  public static KmsEcdhStaticConfigurations create_KmsPublicKeyDiscovery(KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery) {
    return new KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(KmsPublicKeyDiscovery);
  }
  public static KmsEcdhStaticConfigurations create_KmsPrivateKeyToStaticPublicKey(KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey) {
    return new KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(KmsPrivateKeyToStaticPublicKey);
  }
  public boolean is_KmsPublicKeyDiscovery() { return this instanceof KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery; }
  public boolean is_KmsPrivateKeyToStaticPublicKey() { return this instanceof KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey; }
  public KmsPublicKeyDiscoveryInput dtor_KmsPublicKeyDiscovery() {
    KmsEcdhStaticConfigurations d = this;
    return ((KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery)d)._KmsPublicKeyDiscovery;
  }
  public KmsPrivateKeyToStaticPublicKeyInput dtor_KmsPrivateKeyToStaticPublicKey() {
    KmsEcdhStaticConfigurations d = this;
    return ((KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey)d)._KmsPrivateKeyToStaticPublicKey;
  }
}
