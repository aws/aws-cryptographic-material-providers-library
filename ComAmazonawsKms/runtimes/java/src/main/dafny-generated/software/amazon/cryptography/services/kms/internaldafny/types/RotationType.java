// Class RotationType
// Dafny class RotationType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class RotationType {
  public RotationType() {
  }
  private static final dafny.TypeDescriptor<RotationType> _TYPE = dafny.TypeDescriptor.<RotationType>referenceWithInitializer(RotationType.class, () -> RotationType.Default());
  public static dafny.TypeDescriptor<RotationType> _typeDescriptor() {
    return (dafny.TypeDescriptor<RotationType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RotationType theDefault = RotationType.create_AUTOMATIC();
  public static RotationType Default() {
    return theDefault;
  }
  public static RotationType create_AUTOMATIC() {
    return new RotationType_AUTOMATIC();
  }
  public static RotationType create_ON__DEMAND() {
    return new RotationType_ON__DEMAND();
  }
  public boolean is_AUTOMATIC() { return this instanceof RotationType_AUTOMATIC; }
  public boolean is_ON__DEMAND() { return this instanceof RotationType_ON__DEMAND; }
  public static java.util.ArrayList<RotationType> AllSingletonConstructors() {
    java.util.ArrayList<RotationType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RotationType_AUTOMATIC());
    singleton_iterator.add(new RotationType_ON__DEMAND());
    return singleton_iterator;
  }
}
