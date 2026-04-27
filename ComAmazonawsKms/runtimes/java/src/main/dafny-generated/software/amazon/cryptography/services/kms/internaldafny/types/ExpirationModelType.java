// Class ExpirationModelType
// Dafny class ExpirationModelType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ExpirationModelType {
  public ExpirationModelType() {
  }
  private static final dafny.TypeDescriptor<ExpirationModelType> _TYPE = dafny.TypeDescriptor.<ExpirationModelType>referenceWithInitializer(ExpirationModelType.class, () -> ExpirationModelType.Default());
  public static dafny.TypeDescriptor<ExpirationModelType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExpirationModelType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExpirationModelType theDefault = ExpirationModelType.create_KEY__MATERIAL__EXPIRES();
  public static ExpirationModelType Default() {
    return theDefault;
  }
  public static ExpirationModelType create_KEY__MATERIAL__EXPIRES() {
    return new ExpirationModelType_KEY__MATERIAL__EXPIRES();
  }
  public static ExpirationModelType create_KEY__MATERIAL__DOES__NOT__EXPIRE() {
    return new ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE();
  }
  public boolean is_KEY__MATERIAL__EXPIRES() { return this instanceof ExpirationModelType_KEY__MATERIAL__EXPIRES; }
  public boolean is_KEY__MATERIAL__DOES__NOT__EXPIRE() { return this instanceof ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE; }
  public static java.util.ArrayList<ExpirationModelType> AllSingletonConstructors() {
    java.util.ArrayList<ExpirationModelType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ExpirationModelType_KEY__MATERIAL__EXPIRES());
    singleton_iterator.add(new ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE());
    return singleton_iterator;
  }
}
