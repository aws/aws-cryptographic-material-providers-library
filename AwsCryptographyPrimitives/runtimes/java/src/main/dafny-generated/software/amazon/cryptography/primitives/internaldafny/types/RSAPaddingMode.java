// Class RSAPaddingMode
// Dafny class RSAPaddingMode compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class RSAPaddingMode {
  public RSAPaddingMode() {
  }
  private static final dafny.TypeDescriptor<RSAPaddingMode> _TYPE = dafny.TypeDescriptor.<RSAPaddingMode>referenceWithInitializer(RSAPaddingMode.class, () -> RSAPaddingMode.Default());
  public static dafny.TypeDescriptor<RSAPaddingMode> _typeDescriptor() {
    return (dafny.TypeDescriptor<RSAPaddingMode>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RSAPaddingMode theDefault = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_PKCS1();
  public static RSAPaddingMode Default() {
    return theDefault;
  }
  public static RSAPaddingMode create_PKCS1() {
    return new RSAPaddingMode_PKCS1();
  }
  public static RSAPaddingMode create_OAEP__SHA1() {
    return new RSAPaddingMode_OAEP__SHA1();
  }
  public static RSAPaddingMode create_OAEP__SHA256() {
    return new RSAPaddingMode_OAEP__SHA256();
  }
  public static RSAPaddingMode create_OAEP__SHA384() {
    return new RSAPaddingMode_OAEP__SHA384();
  }
  public static RSAPaddingMode create_OAEP__SHA512() {
    return new RSAPaddingMode_OAEP__SHA512();
  }
  public boolean is_PKCS1() { return this instanceof RSAPaddingMode_PKCS1; }
  public boolean is_OAEP__SHA1() { return this instanceof RSAPaddingMode_OAEP__SHA1; }
  public boolean is_OAEP__SHA256() { return this instanceof RSAPaddingMode_OAEP__SHA256; }
  public boolean is_OAEP__SHA384() { return this instanceof RSAPaddingMode_OAEP__SHA384; }
  public boolean is_OAEP__SHA512() { return this instanceof RSAPaddingMode_OAEP__SHA512; }
  public static java.util.ArrayList<RSAPaddingMode> AllSingletonConstructors() {
    java.util.ArrayList<RSAPaddingMode> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RSAPaddingMode_PKCS1());
    singleton_iterator.add(new RSAPaddingMode_OAEP__SHA1());
    singleton_iterator.add(new RSAPaddingMode_OAEP__SHA256());
    singleton_iterator.add(new RSAPaddingMode_OAEP__SHA384());
    singleton_iterator.add(new RSAPaddingMode_OAEP__SHA512());
    return singleton_iterator;
  }
}
