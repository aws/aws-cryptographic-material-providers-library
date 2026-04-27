// Class EncryptionAlgorithmSpec
// Dafny class EncryptionAlgorithmSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class EncryptionAlgorithmSpec {
  public EncryptionAlgorithmSpec() {
  }
  private static final dafny.TypeDescriptor<EncryptionAlgorithmSpec> _TYPE = dafny.TypeDescriptor.<EncryptionAlgorithmSpec>referenceWithInitializer(EncryptionAlgorithmSpec.class, () -> EncryptionAlgorithmSpec.Default());
  public static dafny.TypeDescriptor<EncryptionAlgorithmSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptionAlgorithmSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptionAlgorithmSpec theDefault = EncryptionAlgorithmSpec.create_SYMMETRIC__DEFAULT();
  public static EncryptionAlgorithmSpec Default() {
    return theDefault;
  }
  public static EncryptionAlgorithmSpec create_SYMMETRIC__DEFAULT() {
    return new EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT();
  }
  public static EncryptionAlgorithmSpec create_RSAES__OAEP__SHA__1() {
    return new EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1();
  }
  public static EncryptionAlgorithmSpec create_RSAES__OAEP__SHA__256() {
    return new EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256();
  }
  public boolean is_SYMMETRIC__DEFAULT() { return this instanceof EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT; }
  public boolean is_RSAES__OAEP__SHA__1() { return this instanceof EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1; }
  public boolean is_RSAES__OAEP__SHA__256() { return this instanceof EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256; }
  public static java.util.ArrayList<EncryptionAlgorithmSpec> AllSingletonConstructors() {
    java.util.ArrayList<EncryptionAlgorithmSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT());
    singleton_iterator.add(new EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1());
    singleton_iterator.add(new EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256());
    return singleton_iterator;
  }
}
