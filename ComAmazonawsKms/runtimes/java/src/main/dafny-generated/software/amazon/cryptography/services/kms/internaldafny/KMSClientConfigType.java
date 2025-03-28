// Class KMSClientConfigType
// Dafny class KMSClientConfigType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny;

import software.amazon.cryptography.services.kms.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class KMSClientConfigType {
  public KMSClientConfigType () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSClientConfigType o = (KMSClientConfigType)other;
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
    s.append("Kms.KMSClientConfigType.KMSClientConfigType");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KMSClientConfigType> _TYPE = dafny.TypeDescriptor.<KMSClientConfigType>referenceWithInitializer(KMSClientConfigType.class, () -> KMSClientConfigType.Default());
  public static dafny.TypeDescriptor<KMSClientConfigType> _typeDescriptor() {
    return (dafny.TypeDescriptor<KMSClientConfigType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KMSClientConfigType theDefault = software.amazon.cryptography.services.kms.internaldafny.KMSClientConfigType.create();
  public static KMSClientConfigType Default() {
    return theDefault;
  }
  public static KMSClientConfigType create() {
    return new KMSClientConfigType();
  }
  public static KMSClientConfigType create_KMSClientConfigType() {
    return create();
  }
  public boolean is_KMSClientConfigType() { return true; }
  public static java.util.ArrayList<KMSClientConfigType> AllSingletonConstructors() {
    java.util.ArrayList<KMSClientConfigType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KMSClientConfigType());
    return singleton_iterator;
  }
}
