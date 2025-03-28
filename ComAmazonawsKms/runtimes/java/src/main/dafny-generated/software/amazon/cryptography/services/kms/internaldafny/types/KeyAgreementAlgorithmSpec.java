// Class KeyAgreementAlgorithmSpec
// Dafny class KeyAgreementAlgorithmSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyAgreementAlgorithmSpec {
  public KeyAgreementAlgorithmSpec () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyAgreementAlgorithmSpec o = (KeyAgreementAlgorithmSpec)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec.ECDH");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyAgreementAlgorithmSpec> _TYPE = dafny.TypeDescriptor.<KeyAgreementAlgorithmSpec>referenceWithInitializer(KeyAgreementAlgorithmSpec.class, () -> KeyAgreementAlgorithmSpec.Default());
  public static dafny.TypeDescriptor<KeyAgreementAlgorithmSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyAgreementAlgorithmSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyAgreementAlgorithmSpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec.create();
  public static KeyAgreementAlgorithmSpec Default() {
    return theDefault;
  }
  public static KeyAgreementAlgorithmSpec create() {
    return new KeyAgreementAlgorithmSpec();
  }
  public static KeyAgreementAlgorithmSpec create_ECDH() {
    return create();
  }
  public boolean is_ECDH() { return true; }
  public static java.util.ArrayList<KeyAgreementAlgorithmSpec> AllSingletonConstructors() {
    java.util.ArrayList<KeyAgreementAlgorithmSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyAgreementAlgorithmSpec());
    return singleton_iterator;
  }
}
