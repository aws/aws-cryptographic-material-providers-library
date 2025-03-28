// Class CustomerMasterKeySpec
// Dafny class CustomerMasterKeySpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CustomerMasterKeySpec {
  public CustomerMasterKeySpec() {
  }
  private static final dafny.TypeDescriptor<CustomerMasterKeySpec> _TYPE = dafny.TypeDescriptor.<CustomerMasterKeySpec>referenceWithInitializer(CustomerMasterKeySpec.class, () -> CustomerMasterKeySpec.Default());
  public static dafny.TypeDescriptor<CustomerMasterKeySpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<CustomerMasterKeySpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CustomerMasterKeySpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec.create_RSA__2048();
  public static CustomerMasterKeySpec Default() {
    return theDefault;
  }
  public static CustomerMasterKeySpec create_RSA__2048() {
    return new CustomerMasterKeySpec_RSA__2048();
  }
  public static CustomerMasterKeySpec create_RSA__3072() {
    return new CustomerMasterKeySpec_RSA__3072();
  }
  public static CustomerMasterKeySpec create_RSA__4096() {
    return new CustomerMasterKeySpec_RSA__4096();
  }
  public static CustomerMasterKeySpec create_ECC__NIST__P256() {
    return new CustomerMasterKeySpec_ECC__NIST__P256();
  }
  public static CustomerMasterKeySpec create_ECC__NIST__P384() {
    return new CustomerMasterKeySpec_ECC__NIST__P384();
  }
  public static CustomerMasterKeySpec create_ECC__NIST__P521() {
    return new CustomerMasterKeySpec_ECC__NIST__P521();
  }
  public static CustomerMasterKeySpec create_ECC__SECG__P256K1() {
    return new CustomerMasterKeySpec_ECC__SECG__P256K1();
  }
  public static CustomerMasterKeySpec create_SYMMETRIC__DEFAULT() {
    return new CustomerMasterKeySpec_SYMMETRIC__DEFAULT();
  }
  public static CustomerMasterKeySpec create_HMAC__224() {
    return new CustomerMasterKeySpec_HMAC__224();
  }
  public static CustomerMasterKeySpec create_HMAC__256() {
    return new CustomerMasterKeySpec_HMAC__256();
  }
  public static CustomerMasterKeySpec create_HMAC__384() {
    return new CustomerMasterKeySpec_HMAC__384();
  }
  public static CustomerMasterKeySpec create_HMAC__512() {
    return new CustomerMasterKeySpec_HMAC__512();
  }
  public static CustomerMasterKeySpec create_SM2() {
    return new CustomerMasterKeySpec_SM2();
  }
  public boolean is_RSA__2048() { return this instanceof CustomerMasterKeySpec_RSA__2048; }
  public boolean is_RSA__3072() { return this instanceof CustomerMasterKeySpec_RSA__3072; }
  public boolean is_RSA__4096() { return this instanceof CustomerMasterKeySpec_RSA__4096; }
  public boolean is_ECC__NIST__P256() { return this instanceof CustomerMasterKeySpec_ECC__NIST__P256; }
  public boolean is_ECC__NIST__P384() { return this instanceof CustomerMasterKeySpec_ECC__NIST__P384; }
  public boolean is_ECC__NIST__P521() { return this instanceof CustomerMasterKeySpec_ECC__NIST__P521; }
  public boolean is_ECC__SECG__P256K1() { return this instanceof CustomerMasterKeySpec_ECC__SECG__P256K1; }
  public boolean is_SYMMETRIC__DEFAULT() { return this instanceof CustomerMasterKeySpec_SYMMETRIC__DEFAULT; }
  public boolean is_HMAC__224() { return this instanceof CustomerMasterKeySpec_HMAC__224; }
  public boolean is_HMAC__256() { return this instanceof CustomerMasterKeySpec_HMAC__256; }
  public boolean is_HMAC__384() { return this instanceof CustomerMasterKeySpec_HMAC__384; }
  public boolean is_HMAC__512() { return this instanceof CustomerMasterKeySpec_HMAC__512; }
  public boolean is_SM2() { return this instanceof CustomerMasterKeySpec_SM2; }
  public static java.util.ArrayList<CustomerMasterKeySpec> AllSingletonConstructors() {
    java.util.ArrayList<CustomerMasterKeySpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CustomerMasterKeySpec_RSA__2048());
    singleton_iterator.add(new CustomerMasterKeySpec_RSA__3072());
    singleton_iterator.add(new CustomerMasterKeySpec_RSA__4096());
    singleton_iterator.add(new CustomerMasterKeySpec_ECC__NIST__P256());
    singleton_iterator.add(new CustomerMasterKeySpec_ECC__NIST__P384());
    singleton_iterator.add(new CustomerMasterKeySpec_ECC__NIST__P521());
    singleton_iterator.add(new CustomerMasterKeySpec_ECC__SECG__P256K1());
    singleton_iterator.add(new CustomerMasterKeySpec_SYMMETRIC__DEFAULT());
    singleton_iterator.add(new CustomerMasterKeySpec_HMAC__224());
    singleton_iterator.add(new CustomerMasterKeySpec_HMAC__256());
    singleton_iterator.add(new CustomerMasterKeySpec_HMAC__384());
    singleton_iterator.add(new CustomerMasterKeySpec_HMAC__512());
    singleton_iterator.add(new CustomerMasterKeySpec_SM2());
    return singleton_iterator;
  }
}
