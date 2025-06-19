// Class SigningAlgorithmSpec
// Dafny class SigningAlgorithmSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SigningAlgorithmSpec {
  public SigningAlgorithmSpec() {
  }
  private static final dafny.TypeDescriptor<SigningAlgorithmSpec> _TYPE = dafny.TypeDescriptor.<SigningAlgorithmSpec>referenceWithInitializer(SigningAlgorithmSpec.class, () -> SigningAlgorithmSpec.Default());
  public static dafny.TypeDescriptor<SigningAlgorithmSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<SigningAlgorithmSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SigningAlgorithmSpec theDefault = SigningAlgorithmSpec.create_RSASSA__PSS__SHA__256();
  public static SigningAlgorithmSpec Default() {
    return theDefault;
  }
  public static SigningAlgorithmSpec create_RSASSA__PSS__SHA__256() {
    return new SigningAlgorithmSpec_RSASSA__PSS__SHA__256();
  }
  public static SigningAlgorithmSpec create_RSASSA__PSS__SHA__384() {
    return new SigningAlgorithmSpec_RSASSA__PSS__SHA__384();
  }
  public static SigningAlgorithmSpec create_RSASSA__PSS__SHA__512() {
    return new SigningAlgorithmSpec_RSASSA__PSS__SHA__512();
  }
  public static SigningAlgorithmSpec create_RSASSA__PKCS1__V1__5__SHA__256() {
    return new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256();
  }
  public static SigningAlgorithmSpec create_RSASSA__PKCS1__V1__5__SHA__384() {
    return new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384();
  }
  public static SigningAlgorithmSpec create_RSASSA__PKCS1__V1__5__SHA__512() {
    return new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512();
  }
  public static SigningAlgorithmSpec create_ECDSA__SHA__256() {
    return new SigningAlgorithmSpec_ECDSA__SHA__256();
  }
  public static SigningAlgorithmSpec create_ECDSA__SHA__384() {
    return new SigningAlgorithmSpec_ECDSA__SHA__384();
  }
  public static SigningAlgorithmSpec create_ECDSA__SHA__512() {
    return new SigningAlgorithmSpec_ECDSA__SHA__512();
  }
  public static SigningAlgorithmSpec create_SM2DSA() {
    return new SigningAlgorithmSpec_SM2DSA();
  }
  public boolean is_RSASSA__PSS__SHA__256() { return this instanceof SigningAlgorithmSpec_RSASSA__PSS__SHA__256; }
  public boolean is_RSASSA__PSS__SHA__384() { return this instanceof SigningAlgorithmSpec_RSASSA__PSS__SHA__384; }
  public boolean is_RSASSA__PSS__SHA__512() { return this instanceof SigningAlgorithmSpec_RSASSA__PSS__SHA__512; }
  public boolean is_RSASSA__PKCS1__V1__5__SHA__256() { return this instanceof SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256; }
  public boolean is_RSASSA__PKCS1__V1__5__SHA__384() { return this instanceof SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384; }
  public boolean is_RSASSA__PKCS1__V1__5__SHA__512() { return this instanceof SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512; }
  public boolean is_ECDSA__SHA__256() { return this instanceof SigningAlgorithmSpec_ECDSA__SHA__256; }
  public boolean is_ECDSA__SHA__384() { return this instanceof SigningAlgorithmSpec_ECDSA__SHA__384; }
  public boolean is_ECDSA__SHA__512() { return this instanceof SigningAlgorithmSpec_ECDSA__SHA__512; }
  public boolean is_SM2DSA() { return this instanceof SigningAlgorithmSpec_SM2DSA; }
  public static java.util.ArrayList<SigningAlgorithmSpec> AllSingletonConstructors() {
    java.util.ArrayList<SigningAlgorithmSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PSS__SHA__256());
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PSS__SHA__384());
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PSS__SHA__512());
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256());
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384());
    singleton_iterator.add(new SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512());
    singleton_iterator.add(new SigningAlgorithmSpec_ECDSA__SHA__256());
    singleton_iterator.add(new SigningAlgorithmSpec_ECDSA__SHA__384());
    singleton_iterator.add(new SigningAlgorithmSpec_ECDSA__SHA__512());
    singleton_iterator.add(new SigningAlgorithmSpec_SM2DSA());
    return singleton_iterator;
  }
}
