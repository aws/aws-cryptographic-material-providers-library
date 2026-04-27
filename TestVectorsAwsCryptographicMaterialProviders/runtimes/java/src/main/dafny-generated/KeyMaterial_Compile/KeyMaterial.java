// Class KeyMaterial
// Dafny class KeyMaterial compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyMaterial {
  public KeyMaterial() {
  }
  private static final dafny.TypeDescriptor<KeyMaterial> _TYPE = dafny.TypeDescriptor.<KeyMaterial>referenceWithInitializer(KeyMaterial.class, () -> KeyMaterial.Default());
  public static dafny.TypeDescriptor<KeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyMaterial theDefault = KeyMaterial.create_Symetric(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), false, false, dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), java.math.BigInteger.ZERO, dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KeyMaterial Default() {
    return theDefault;
  }
  public static KeyMaterial create_Symetric(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> algorithm, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends java.lang.Byte> wrappingKey, dafny.DafnySequence<? extends Character> keyIdentifier) {
    return new KeyMaterial_Symetric(name, encrypt, decrypt, algorithm, bits, encoding, wrappingKey, keyIdentifier);
  }
  public static KeyMaterial create_PrivateRSA(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> algorithm, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends Character> material, dafny.DafnySequence<? extends Character> keyIdentifier) {
    return new KeyMaterial_PrivateRSA(name, encrypt, decrypt, algorithm, bits, encoding, material, keyIdentifier);
  }
  public static KeyMaterial create_PublicRSA(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> algorithm, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends Character> material, dafny.DafnySequence<? extends Character> keyIdentifier) {
    return new KeyMaterial_PublicRSA(name, encrypt, decrypt, bits, algorithm, encoding, material, keyIdentifier);
  }
  public static KeyMaterial create_PrivateECDH(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> algorithm, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends Character> senderMaterial, dafny.DafnySequence<? extends Character> recipientMaterial, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> keyIdentifier) {
    return new KeyMaterial_PrivateECDH(name, encrypt, decrypt, algorithm, bits, encoding, senderMaterial, recipientMaterial, senderPublicKey, recipientPublicKey, keyIdentifier);
  }
  public static KeyMaterial create_KMS(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier) {
    return new KeyMaterial_KMS(name, encrypt, decrypt, keyIdentifier);
  }
  public static KeyMaterial create_KMSAsymetric(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> algorithm, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new KeyMaterial_KMSAsymetric(name, encrypt, decrypt, keyIdentifier, bits, algorithm, encoding, publicKey);
  }
  public static KeyMaterial create_KMSEcdh(dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier, dafny.DafnySequence<? extends Character> algorithm, dafny.DafnySequence<? extends Character> senderMaterial, dafny.DafnySequence<? extends Character> recipientMaterial, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey) {
    return new KeyMaterial_KMSEcdh(name, encrypt, decrypt, keyIdentifier, algorithm, senderMaterial, recipientMaterial, senderPublicKey, recipientPublicKey);
  }
  public static KeyMaterial create_StaticMaterial(dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> symmetricSigningKeys) {
    return new KeyMaterial_StaticMaterial(name, algorithmSuite, encryptionContext, encryptedDataKeys, requiredEncryptionContextKeys, plaintextDataKey, signingKey, verificationKey, symmetricSigningKeys);
  }
  public static KeyMaterial create_StaticKeyStoreInformation(dafny.DafnySequence<? extends Character> keyIdentifier, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnySequence<? extends java.lang.Byte> branchKey, dafny.DafnySequence<? extends java.lang.Byte> beaconKey) {
    return new KeyMaterial_StaticKeyStoreInformation(keyIdentifier, branchKeyVersion, branchKey, beaconKey);
  }
  public boolean is_Symetric() { return this instanceof KeyMaterial_Symetric; }
  public boolean is_PrivateRSA() { return this instanceof KeyMaterial_PrivateRSA; }
  public boolean is_PublicRSA() { return this instanceof KeyMaterial_PublicRSA; }
  public boolean is_PrivateECDH() { return this instanceof KeyMaterial_PrivateECDH; }
  public boolean is_KMS() { return this instanceof KeyMaterial_KMS; }
  public boolean is_KMSAsymetric() { return this instanceof KeyMaterial_KMSAsymetric; }
  public boolean is_KMSEcdh() { return this instanceof KeyMaterial_KMSEcdh; }
  public boolean is_StaticMaterial() { return this instanceof KeyMaterial_StaticMaterial; }
  public boolean is_StaticKeyStoreInformation() { return this instanceof KeyMaterial_StaticKeyStoreInformation; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._name; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._name; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._name; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._name; }
    if (d instanceof KeyMaterial_KMS) { return ((KeyMaterial_KMS)d)._name; }
    if (d instanceof KeyMaterial_KMSAsymetric) { return ((KeyMaterial_KMSAsymetric)d)._name; }
    if (d instanceof KeyMaterial_KMSEcdh) { return ((KeyMaterial_KMSEcdh)d)._name; }
    return ((KeyMaterial_StaticMaterial)d)._name;
  }
  public boolean dtor_encrypt() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._encrypt; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._encrypt; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._encrypt; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._encrypt; }
    if (d instanceof KeyMaterial_KMS) { return ((KeyMaterial_KMS)d)._encrypt; }
    if (d instanceof KeyMaterial_KMSAsymetric) { return ((KeyMaterial_KMSAsymetric)d)._encrypt; }
    return ((KeyMaterial_KMSEcdh)d)._encrypt;
  }
  public boolean dtor_decrypt() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._decrypt; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._decrypt; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._decrypt; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._decrypt; }
    if (d instanceof KeyMaterial_KMS) { return ((KeyMaterial_KMS)d)._decrypt; }
    if (d instanceof KeyMaterial_KMSAsymetric) { return ((KeyMaterial_KMSAsymetric)d)._decrypt; }
    return ((KeyMaterial_KMSEcdh)d)._decrypt;
  }
  public dafny.DafnySequence<? extends Character> dtor_algorithm() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._algorithm; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._algorithm; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._algorithm; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._algorithm; }
    if (d instanceof KeyMaterial_KMSAsymetric) { return ((KeyMaterial_KMSAsymetric)d)._algorithm; }
    return ((KeyMaterial_KMSEcdh)d)._algorithm;
  }
  public java.math.BigInteger dtor_bits() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._bits; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._bits; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._bits; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._bits; }
    return ((KeyMaterial_KMSAsymetric)d)._bits;
  }
  public dafny.DafnySequence<? extends Character> dtor_encoding() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._encoding; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._encoding; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._encoding; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._encoding; }
    return ((KeyMaterial_KMSAsymetric)d)._encoding;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappingKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_Symetric)d)._wrappingKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyIdentifier() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_Symetric) { return ((KeyMaterial_Symetric)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_PublicRSA) { return ((KeyMaterial_PublicRSA)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_KMS) { return ((KeyMaterial_KMS)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_KMSAsymetric) { return ((KeyMaterial_KMSAsymetric)d)._keyIdentifier; }
    if (d instanceof KeyMaterial_KMSEcdh) { return ((KeyMaterial_KMSEcdh)d)._keyIdentifier; }
    return ((KeyMaterial_StaticKeyStoreInformation)d)._keyIdentifier;
  }
  public dafny.DafnySequence<? extends Character> dtor_material() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_PrivateRSA) { return ((KeyMaterial_PrivateRSA)d)._material; }
    return ((KeyMaterial_PublicRSA)d)._material;
  }
  public dafny.DafnySequence<? extends Character> dtor_senderMaterial() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._senderMaterial; }
    return ((KeyMaterial_KMSEcdh)d)._senderMaterial;
  }
  public dafny.DafnySequence<? extends Character> dtor_recipientMaterial() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._recipientMaterial; }
    return ((KeyMaterial_KMSEcdh)d)._recipientMaterial;
  }
  public dafny.DafnySequence<? extends Character> dtor_senderPublicKey() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._senderPublicKey; }
    return ((KeyMaterial_KMSEcdh)d)._senderPublicKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_recipientPublicKey() {
    KeyMaterial d = this;
    if (d instanceof KeyMaterial_PrivateECDH) { return ((KeyMaterial_PrivateECDH)d)._recipientPublicKey; }
    return ((KeyMaterial_KMSEcdh)d)._recipientPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_KMSAsymetric)d)._publicKey;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo dtor_algorithmSuite() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._algorithmSuite;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._encryptionContext;
  }
  public dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> dtor_encryptedDataKeys() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._encryptedDataKeys;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._requiredEncryptionContextKeys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_plaintextDataKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._plaintextDataKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_signingKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._signingKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_verificationKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._verificationKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_symmetricSigningKeys() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticMaterial)d)._symmetricSigningKeys;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_branchKeyVersion() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticKeyStoreInformation)d)._branchKeyVersion;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_branchKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticKeyStoreInformation)d)._branchKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_beaconKey() {
    KeyMaterial d = this;
    return ((KeyMaterial_StaticKeyStoreInformation)d)._beaconKey;
  }
}
