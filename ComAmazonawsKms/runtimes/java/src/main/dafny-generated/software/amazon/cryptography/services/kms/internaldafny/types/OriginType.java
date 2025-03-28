// Class OriginType
// Dafny class OriginType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class OriginType {
  public OriginType() {
  }
  private static final dafny.TypeDescriptor<OriginType> _TYPE = dafny.TypeDescriptor.<OriginType>referenceWithInitializer(OriginType.class, () -> OriginType.Default());
  public static dafny.TypeDescriptor<OriginType> _typeDescriptor() {
    return (dafny.TypeDescriptor<OriginType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OriginType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.OriginType.create_AWS__KMS();
  public static OriginType Default() {
    return theDefault;
  }
  public static OriginType create_AWS__KMS() {
    return new OriginType_AWS__KMS();
  }
  public static OriginType create_EXTERNAL() {
    return new OriginType_EXTERNAL();
  }
  public static OriginType create_AWS__CLOUDHSM() {
    return new OriginType_AWS__CLOUDHSM();
  }
  public static OriginType create_EXTERNAL__KEY__STORE() {
    return new OriginType_EXTERNAL__KEY__STORE();
  }
  public boolean is_AWS__KMS() { return this instanceof OriginType_AWS__KMS; }
  public boolean is_EXTERNAL() { return this instanceof OriginType_EXTERNAL; }
  public boolean is_AWS__CLOUDHSM() { return this instanceof OriginType_AWS__CLOUDHSM; }
  public boolean is_EXTERNAL__KEY__STORE() { return this instanceof OriginType_EXTERNAL__KEY__STORE; }
  public static java.util.ArrayList<OriginType> AllSingletonConstructors() {
    java.util.ArrayList<OriginType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new OriginType_AWS__KMS());
    singleton_iterator.add(new OriginType_EXTERNAL());
    singleton_iterator.add(new OriginType_AWS__CLOUDHSM());
    singleton_iterator.add(new OriginType_EXTERNAL__KEY__STORE());
    return singleton_iterator;
  }
}
