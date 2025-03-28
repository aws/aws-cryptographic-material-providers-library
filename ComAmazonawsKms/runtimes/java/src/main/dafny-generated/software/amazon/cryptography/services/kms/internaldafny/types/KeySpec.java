// Class KeySpec
// Dafny class KeySpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeySpec {
  public KeySpec() {
  }
  private static final dafny.TypeDescriptor<KeySpec> _TYPE = dafny.TypeDescriptor.<KeySpec>referenceWithInitializer(KeySpec.class, () -> KeySpec.Default());
  public static dafny.TypeDescriptor<KeySpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeySpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeySpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.KeySpec.create_RSA__2048();
  public static KeySpec Default() {
    return theDefault;
  }
  public static KeySpec create_RSA__2048() {
    return new KeySpec_RSA__2048();
  }
  public static KeySpec create_RSA__3072() {
    return new KeySpec_RSA__3072();
  }
  public static KeySpec create_RSA__4096() {
    return new KeySpec_RSA__4096();
  }
  public static KeySpec create_ECC__NIST__P256() {
    return new KeySpec_ECC__NIST__P256();
  }
  public static KeySpec create_ECC__NIST__P384() {
    return new KeySpec_ECC__NIST__P384();
  }
  public static KeySpec create_ECC__NIST__P521() {
    return new KeySpec_ECC__NIST__P521();
  }
  public static KeySpec create_ECC__SECG__P256K1() {
    return new KeySpec_ECC__SECG__P256K1();
  }
  public static KeySpec create_SYMMETRIC__DEFAULT() {
    return new KeySpec_SYMMETRIC__DEFAULT();
  }
  public static KeySpec create_HMAC__224() {
    return new KeySpec_HMAC__224();
  }
  public static KeySpec create_HMAC__256() {
    return new KeySpec_HMAC__256();
  }
  public static KeySpec create_HMAC__384() {
    return new KeySpec_HMAC__384();
  }
  public static KeySpec create_HMAC__512() {
    return new KeySpec_HMAC__512();
  }
  public static KeySpec create_SM2() {
    return new KeySpec_SM2();
  }
  public boolean is_RSA__2048() { return this instanceof KeySpec_RSA__2048; }
  public boolean is_RSA__3072() { return this instanceof KeySpec_RSA__3072; }
  public boolean is_RSA__4096() { return this instanceof KeySpec_RSA__4096; }
  public boolean is_ECC__NIST__P256() { return this instanceof KeySpec_ECC__NIST__P256; }
  public boolean is_ECC__NIST__P384() { return this instanceof KeySpec_ECC__NIST__P384; }
  public boolean is_ECC__NIST__P521() { return this instanceof KeySpec_ECC__NIST__P521; }
  public boolean is_ECC__SECG__P256K1() { return this instanceof KeySpec_ECC__SECG__P256K1; }
  public boolean is_SYMMETRIC__DEFAULT() { return this instanceof KeySpec_SYMMETRIC__DEFAULT; }
  public boolean is_HMAC__224() { return this instanceof KeySpec_HMAC__224; }
  public boolean is_HMAC__256() { return this instanceof KeySpec_HMAC__256; }
  public boolean is_HMAC__384() { return this instanceof KeySpec_HMAC__384; }
  public boolean is_HMAC__512() { return this instanceof KeySpec_HMAC__512; }
  public boolean is_SM2() { return this instanceof KeySpec_SM2; }
  public static java.util.ArrayList<KeySpec> AllSingletonConstructors() {
    java.util.ArrayList<KeySpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeySpec_RSA__2048());
    singleton_iterator.add(new KeySpec_RSA__3072());
    singleton_iterator.add(new KeySpec_RSA__4096());
    singleton_iterator.add(new KeySpec_ECC__NIST__P256());
    singleton_iterator.add(new KeySpec_ECC__NIST__P384());
    singleton_iterator.add(new KeySpec_ECC__NIST__P521());
    singleton_iterator.add(new KeySpec_ECC__SECG__P256K1());
    singleton_iterator.add(new KeySpec_SYMMETRIC__DEFAULT());
    singleton_iterator.add(new KeySpec_HMAC__224());
    singleton_iterator.add(new KeySpec_HMAC__256());
    singleton_iterator.add(new KeySpec_HMAC__384());
    singleton_iterator.add(new KeySpec_HMAC__512());
    singleton_iterator.add(new KeySpec_SM2());
    return singleton_iterator;
  }
}
