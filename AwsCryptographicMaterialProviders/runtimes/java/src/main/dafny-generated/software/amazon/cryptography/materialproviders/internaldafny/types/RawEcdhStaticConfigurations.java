// Class RawEcdhStaticConfigurations
// Dafny class RawEcdhStaticConfigurations compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class RawEcdhStaticConfigurations {
  public RawEcdhStaticConfigurations() {
  }
  private static final dafny.TypeDescriptor<RawEcdhStaticConfigurations> _TYPE = dafny.TypeDescriptor.<RawEcdhStaticConfigurations>referenceWithInitializer(RawEcdhStaticConfigurations.class, () -> RawEcdhStaticConfigurations.Default());
  public static dafny.TypeDescriptor<RawEcdhStaticConfigurations> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawEcdhStaticConfigurations>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RawEcdhStaticConfigurations theDefault = RawEcdhStaticConfigurations.create_PublicKeyDiscovery(PublicKeyDiscoveryInput.Default());
  public static RawEcdhStaticConfigurations Default() {
    return theDefault;
  }
  public static RawEcdhStaticConfigurations create_PublicKeyDiscovery(PublicKeyDiscoveryInput PublicKeyDiscovery) {
    return new RawEcdhStaticConfigurations_PublicKeyDiscovery(PublicKeyDiscovery);
  }
  public static RawEcdhStaticConfigurations create_RawPrivateKeyToStaticPublicKey(RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey) {
    return new RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(RawPrivateKeyToStaticPublicKey);
  }
  public static RawEcdhStaticConfigurations create_EphemeralPrivateKeyToStaticPublicKey(EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey) {
    return new RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(EphemeralPrivateKeyToStaticPublicKey);
  }
  public boolean is_PublicKeyDiscovery() { return this instanceof RawEcdhStaticConfigurations_PublicKeyDiscovery; }
  public boolean is_RawPrivateKeyToStaticPublicKey() { return this instanceof RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey; }
  public boolean is_EphemeralPrivateKeyToStaticPublicKey() { return this instanceof RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey; }
  public PublicKeyDiscoveryInput dtor_PublicKeyDiscovery() {
    RawEcdhStaticConfigurations d = this;
    return ((RawEcdhStaticConfigurations_PublicKeyDiscovery)d)._PublicKeyDiscovery;
  }
  public RawPrivateKeyToStaticPublicKeyInput dtor_RawPrivateKeyToStaticPublicKey() {
    RawEcdhStaticConfigurations d = this;
    return ((RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey)d)._RawPrivateKeyToStaticPublicKey;
  }
  public EphemeralPrivateKeyToStaticPublicKeyInput dtor_EphemeralPrivateKeyToStaticPublicKey() {
    RawEcdhStaticConfigurations d = this;
    return ((RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey)d)._EphemeralPrivateKeyToStaticPublicKey;
  }
}
