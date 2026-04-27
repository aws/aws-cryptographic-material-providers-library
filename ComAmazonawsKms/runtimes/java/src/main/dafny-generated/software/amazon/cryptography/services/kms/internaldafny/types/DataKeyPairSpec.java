// Class DataKeyPairSpec
// Dafny class DataKeyPairSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DataKeyPairSpec {
  public DataKeyPairSpec() {
  }
  private static final dafny.TypeDescriptor<DataKeyPairSpec> _TYPE = dafny.TypeDescriptor.<DataKeyPairSpec>referenceWithInitializer(DataKeyPairSpec.class, () -> DataKeyPairSpec.Default());
  public static dafny.TypeDescriptor<DataKeyPairSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<DataKeyPairSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DataKeyPairSpec theDefault = DataKeyPairSpec.create_RSA__2048();
  public static DataKeyPairSpec Default() {
    return theDefault;
  }
  public static DataKeyPairSpec create_RSA__2048() {
    return new DataKeyPairSpec_RSA__2048();
  }
  public static DataKeyPairSpec create_RSA__3072() {
    return new DataKeyPairSpec_RSA__3072();
  }
  public static DataKeyPairSpec create_RSA__4096() {
    return new DataKeyPairSpec_RSA__4096();
  }
  public static DataKeyPairSpec create_ECC__NIST__P256() {
    return new DataKeyPairSpec_ECC__NIST__P256();
  }
  public static DataKeyPairSpec create_ECC__NIST__P384() {
    return new DataKeyPairSpec_ECC__NIST__P384();
  }
  public static DataKeyPairSpec create_ECC__NIST__P521() {
    return new DataKeyPairSpec_ECC__NIST__P521();
  }
  public static DataKeyPairSpec create_ECC__SECG__P256K1() {
    return new DataKeyPairSpec_ECC__SECG__P256K1();
  }
  public static DataKeyPairSpec create_SM2() {
    return new DataKeyPairSpec_SM2();
  }
  public boolean is_RSA__2048() { return this instanceof DataKeyPairSpec_RSA__2048; }
  public boolean is_RSA__3072() { return this instanceof DataKeyPairSpec_RSA__3072; }
  public boolean is_RSA__4096() { return this instanceof DataKeyPairSpec_RSA__4096; }
  public boolean is_ECC__NIST__P256() { return this instanceof DataKeyPairSpec_ECC__NIST__P256; }
  public boolean is_ECC__NIST__P384() { return this instanceof DataKeyPairSpec_ECC__NIST__P384; }
  public boolean is_ECC__NIST__P521() { return this instanceof DataKeyPairSpec_ECC__NIST__P521; }
  public boolean is_ECC__SECG__P256K1() { return this instanceof DataKeyPairSpec_ECC__SECG__P256K1; }
  public boolean is_SM2() { return this instanceof DataKeyPairSpec_SM2; }
  public static java.util.ArrayList<DataKeyPairSpec> AllSingletonConstructors() {
    java.util.ArrayList<DataKeyPairSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DataKeyPairSpec_RSA__2048());
    singleton_iterator.add(new DataKeyPairSpec_RSA__3072());
    singleton_iterator.add(new DataKeyPairSpec_RSA__4096());
    singleton_iterator.add(new DataKeyPairSpec_ECC__NIST__P256());
    singleton_iterator.add(new DataKeyPairSpec_ECC__NIST__P384());
    singleton_iterator.add(new DataKeyPairSpec_ECC__NIST__P521());
    singleton_iterator.add(new DataKeyPairSpec_ECC__SECG__P256K1());
    singleton_iterator.add(new DataKeyPairSpec_SM2());
    return singleton_iterator;
  }
}
