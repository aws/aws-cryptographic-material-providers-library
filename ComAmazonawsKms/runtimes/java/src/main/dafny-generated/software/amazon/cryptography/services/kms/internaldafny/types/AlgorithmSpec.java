// Class AlgorithmSpec
// Dafny class AlgorithmSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AlgorithmSpec {
  public AlgorithmSpec() {
  }
  private static final dafny.TypeDescriptor<AlgorithmSpec> _TYPE = dafny.TypeDescriptor.<AlgorithmSpec>referenceWithInitializer(AlgorithmSpec.class, () -> AlgorithmSpec.Default());
  public static dafny.TypeDescriptor<AlgorithmSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<AlgorithmSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AlgorithmSpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.AlgorithmSpec.create_RSAES__PKCS1__V1__5();
  public static AlgorithmSpec Default() {
    return theDefault;
  }
  public static AlgorithmSpec create_RSAES__PKCS1__V1__5() {
    return new AlgorithmSpec_RSAES__PKCS1__V1__5();
  }
  public static AlgorithmSpec create_RSAES__OAEP__SHA__1() {
    return new AlgorithmSpec_RSAES__OAEP__SHA__1();
  }
  public static AlgorithmSpec create_RSAES__OAEP__SHA__256() {
    return new AlgorithmSpec_RSAES__OAEP__SHA__256();
  }
  public static AlgorithmSpec create_RSA__AES__KEY__WRAP__SHA__1() {
    return new AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1();
  }
  public static AlgorithmSpec create_RSA__AES__KEY__WRAP__SHA__256() {
    return new AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256();
  }
  public static AlgorithmSpec create_SM2PKE() {
    return new AlgorithmSpec_SM2PKE();
  }
  public boolean is_RSAES__PKCS1__V1__5() { return this instanceof AlgorithmSpec_RSAES__PKCS1__V1__5; }
  public boolean is_RSAES__OAEP__SHA__1() { return this instanceof AlgorithmSpec_RSAES__OAEP__SHA__1; }
  public boolean is_RSAES__OAEP__SHA__256() { return this instanceof AlgorithmSpec_RSAES__OAEP__SHA__256; }
  public boolean is_RSA__AES__KEY__WRAP__SHA__1() { return this instanceof AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1; }
  public boolean is_RSA__AES__KEY__WRAP__SHA__256() { return this instanceof AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256; }
  public boolean is_SM2PKE() { return this instanceof AlgorithmSpec_SM2PKE; }
  public static java.util.ArrayList<AlgorithmSpec> AllSingletonConstructors() {
    java.util.ArrayList<AlgorithmSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new AlgorithmSpec_RSAES__PKCS1__V1__5());
    singleton_iterator.add(new AlgorithmSpec_RSAES__OAEP__SHA__1());
    singleton_iterator.add(new AlgorithmSpec_RSAES__OAEP__SHA__256());
    singleton_iterator.add(new AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1());
    singleton_iterator.add(new AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256());
    singleton_iterator.add(new AlgorithmSpec_SM2PKE());
    return singleton_iterator;
  }
}
