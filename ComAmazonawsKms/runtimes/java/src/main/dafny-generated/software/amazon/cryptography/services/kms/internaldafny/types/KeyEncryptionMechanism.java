// Class KeyEncryptionMechanism
// Dafny class KeyEncryptionMechanism compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyEncryptionMechanism {
  public KeyEncryptionMechanism () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyEncryptionMechanism o = (KeyEncryptionMechanism)other;
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
    s.append("ComAmazonawsKmsTypes.KeyEncryptionMechanism.RSAES_OAEP_SHA_256");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyEncryptionMechanism> _TYPE = dafny.TypeDescriptor.<KeyEncryptionMechanism>referenceWithInitializer(KeyEncryptionMechanism.class, () -> KeyEncryptionMechanism.Default());
  public static dafny.TypeDescriptor<KeyEncryptionMechanism> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyEncryptionMechanism>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyEncryptionMechanism theDefault = software.amazon.cryptography.services.kms.internaldafny.types.KeyEncryptionMechanism.create();
  public static KeyEncryptionMechanism Default() {
    return theDefault;
  }
  public static KeyEncryptionMechanism create() {
    return new KeyEncryptionMechanism();
  }
  public static KeyEncryptionMechanism create_RSAES__OAEP__SHA__256() {
    return create();
  }
  public boolean is_RSAES__OAEP__SHA__256() { return true; }
  public static java.util.ArrayList<KeyEncryptionMechanism> AllSingletonConstructors() {
    java.util.ArrayList<KeyEncryptionMechanism> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyEncryptionMechanism());
    return singleton_iterator;
  }
}
