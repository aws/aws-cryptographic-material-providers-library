// Class WrappingKeySpec
// Dafny class WrappingKeySpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class WrappingKeySpec {
  public WrappingKeySpec() {
  }
  private static final dafny.TypeDescriptor<WrappingKeySpec> _TYPE = dafny.TypeDescriptor.<WrappingKeySpec>referenceWithInitializer(WrappingKeySpec.class, () -> WrappingKeySpec.Default());
  public static dafny.TypeDescriptor<WrappingKeySpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<WrappingKeySpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final WrappingKeySpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.WrappingKeySpec.create_RSA__2048();
  public static WrappingKeySpec Default() {
    return theDefault;
  }
  public static WrappingKeySpec create_RSA__2048() {
    return new WrappingKeySpec_RSA__2048();
  }
  public static WrappingKeySpec create_RSA__3072() {
    return new WrappingKeySpec_RSA__3072();
  }
  public static WrappingKeySpec create_RSA__4096() {
    return new WrappingKeySpec_RSA__4096();
  }
  public static WrappingKeySpec create_SM2() {
    return new WrappingKeySpec_SM2();
  }
  public boolean is_RSA__2048() { return this instanceof WrappingKeySpec_RSA__2048; }
  public boolean is_RSA__3072() { return this instanceof WrappingKeySpec_RSA__3072; }
  public boolean is_RSA__4096() { return this instanceof WrappingKeySpec_RSA__4096; }
  public boolean is_SM2() { return this instanceof WrappingKeySpec_SM2; }
  public static java.util.ArrayList<WrappingKeySpec> AllSingletonConstructors() {
    java.util.ArrayList<WrappingKeySpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new WrappingKeySpec_RSA__2048());
    singleton_iterator.add(new WrappingKeySpec_RSA__3072());
    singleton_iterator.add(new WrappingKeySpec_RSA__4096());
    singleton_iterator.add(new WrappingKeySpec_SM2());
    return singleton_iterator;
  }
}
