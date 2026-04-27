// Class KeyDescription
// Dafny class KeyDescription compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyDescription {
  public KeyDescription() {
  }
  private static final dafny.TypeDescriptor<KeyDescription> _TYPE = dafny.TypeDescriptor.<KeyDescription>referenceWithInitializer(KeyDescription.class, () -> KeyDescription.Default());
  public static dafny.TypeDescriptor<KeyDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyDescription theDefault = KeyDescription.create_Kms(KMSInfo.Default());
  public static KeyDescription Default() {
    return theDefault;
  }
  public static KeyDescription create_Kms(KMSInfo Kms) {
    return new KeyDescription_Kms(Kms);
  }
  public static KeyDescription create_KmsMrk(KmsMrkAware KmsMrk) {
    return new KeyDescription_KmsMrk(KmsMrk);
  }
  public static KeyDescription create_KmsMrkDiscovery(KmsMrkAwareDiscovery KmsMrkDiscovery) {
    return new KeyDescription_KmsMrkDiscovery(KmsMrkDiscovery);
  }
  public static KeyDescription create_RSA(RawRSA RSA) {
    return new KeyDescription_RSA(RSA);
  }
  public static KeyDescription create_AES(RawAES AES) {
    return new KeyDescription_AES(AES);
  }
  public static KeyDescription create_ECDH(RawEcdh ECDH) {
    return new KeyDescription_ECDH(ECDH);
  }
  public static KeyDescription create_Static(StaticKeyring Static) {
    return new KeyDescription_Static(Static);
  }
  public static KeyDescription create_KmsRsa(KmsRsaKeyring KmsRsa) {
    return new KeyDescription_KmsRsa(KmsRsa);
  }
  public static KeyDescription create_KmsECDH(KmsEcdhKeyring KmsECDH) {
    return new KeyDescription_KmsECDH(KmsECDH);
  }
  public static KeyDescription create_Hierarchy(HierarchyKeyring Hierarchy) {
    return new KeyDescription_Hierarchy(Hierarchy);
  }
  public static KeyDescription create_Multi(MultiKeyring Multi) {
    return new KeyDescription_Multi(Multi);
  }
  public static KeyDescription create_RequiredEncryptionContext(RequiredEncryptionContextCMM RequiredEncryptionContext) {
    return new KeyDescription_RequiredEncryptionContext(RequiredEncryptionContext);
  }
  public boolean is_Kms() { return this instanceof KeyDescription_Kms; }
  public boolean is_KmsMrk() { return this instanceof KeyDescription_KmsMrk; }
  public boolean is_KmsMrkDiscovery() { return this instanceof KeyDescription_KmsMrkDiscovery; }
  public boolean is_RSA() { return this instanceof KeyDescription_RSA; }
  public boolean is_AES() { return this instanceof KeyDescription_AES; }
  public boolean is_ECDH() { return this instanceof KeyDescription_ECDH; }
  public boolean is_Static() { return this instanceof KeyDescription_Static; }
  public boolean is_KmsRsa() { return this instanceof KeyDescription_KmsRsa; }
  public boolean is_KmsECDH() { return this instanceof KeyDescription_KmsECDH; }
  public boolean is_Hierarchy() { return this instanceof KeyDescription_Hierarchy; }
  public boolean is_Multi() { return this instanceof KeyDescription_Multi; }
  public boolean is_RequiredEncryptionContext() { return this instanceof KeyDescription_RequiredEncryptionContext; }
  public KMSInfo dtor_Kms() {
    KeyDescription d = this;
    return ((KeyDescription_Kms)d)._Kms;
  }
  public KmsMrkAware dtor_KmsMrk() {
    KeyDescription d = this;
    return ((KeyDescription_KmsMrk)d)._KmsMrk;
  }
  public KmsMrkAwareDiscovery dtor_KmsMrkDiscovery() {
    KeyDescription d = this;
    return ((KeyDescription_KmsMrkDiscovery)d)._KmsMrkDiscovery;
  }
  public RawRSA dtor_RSA() {
    KeyDescription d = this;
    return ((KeyDescription_RSA)d)._RSA;
  }
  public RawAES dtor_AES() {
    KeyDescription d = this;
    return ((KeyDescription_AES)d)._AES;
  }
  public RawEcdh dtor_ECDH() {
    KeyDescription d = this;
    return ((KeyDescription_ECDH)d)._ECDH;
  }
  public StaticKeyring dtor_Static() {
    KeyDescription d = this;
    return ((KeyDescription_Static)d)._Static;
  }
  public KmsRsaKeyring dtor_KmsRsa() {
    KeyDescription d = this;
    return ((KeyDescription_KmsRsa)d)._KmsRsa;
  }
  public KmsEcdhKeyring dtor_KmsECDH() {
    KeyDescription d = this;
    return ((KeyDescription_KmsECDH)d)._KmsECDH;
  }
  public HierarchyKeyring dtor_Hierarchy() {
    KeyDescription d = this;
    return ((KeyDescription_Hierarchy)d)._Hierarchy;
  }
  public MultiKeyring dtor_Multi() {
    KeyDescription d = this;
    return ((KeyDescription_Multi)d)._Multi;
  }
  public RequiredEncryptionContextCMM dtor_RequiredEncryptionContext() {
    KeyDescription d = this;
    return ((KeyDescription_RequiredEncryptionContext)d)._RequiredEncryptionContext;
  }
}
