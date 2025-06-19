// Class MultiRegionKeyType
// Dafny class MultiRegionKeyType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class MultiRegionKeyType {
  public MultiRegionKeyType() {
  }
  private static final dafny.TypeDescriptor<MultiRegionKeyType> _TYPE = dafny.TypeDescriptor.<MultiRegionKeyType>referenceWithInitializer(MultiRegionKeyType.class, () -> MultiRegionKeyType.Default());
  public static dafny.TypeDescriptor<MultiRegionKeyType> _typeDescriptor() {
    return (dafny.TypeDescriptor<MultiRegionKeyType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MultiRegionKeyType theDefault = MultiRegionKeyType.create_PRIMARY();
  public static MultiRegionKeyType Default() {
    return theDefault;
  }
  public static MultiRegionKeyType create_PRIMARY() {
    return new MultiRegionKeyType_PRIMARY();
  }
  public static MultiRegionKeyType create_REPLICA() {
    return new MultiRegionKeyType_REPLICA();
  }
  public boolean is_PRIMARY() { return this instanceof MultiRegionKeyType_PRIMARY; }
  public boolean is_REPLICA() { return this instanceof MultiRegionKeyType_REPLICA; }
  public static java.util.ArrayList<MultiRegionKeyType> AllSingletonConstructors() {
    java.util.ArrayList<MultiRegionKeyType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new MultiRegionKeyType_PRIMARY());
    singleton_iterator.add(new MultiRegionKeyType_REPLICA());
    return singleton_iterator;
  }
}
