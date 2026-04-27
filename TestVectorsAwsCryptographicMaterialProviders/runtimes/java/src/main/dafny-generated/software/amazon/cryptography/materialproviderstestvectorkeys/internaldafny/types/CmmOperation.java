// Class CmmOperation
// Dafny class CmmOperation compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CmmOperation {
  public CmmOperation() {
  }
  private static final dafny.TypeDescriptor<CmmOperation> _TYPE = dafny.TypeDescriptor.<CmmOperation>referenceWithInitializer(CmmOperation.class, () -> CmmOperation.Default());
  public static dafny.TypeDescriptor<CmmOperation> _typeDescriptor() {
    return (dafny.TypeDescriptor<CmmOperation>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CmmOperation theDefault = CmmOperation.create_ENCRYPT();
  public static CmmOperation Default() {
    return theDefault;
  }
  public static CmmOperation create_ENCRYPT() {
    return new CmmOperation_ENCRYPT();
  }
  public static CmmOperation create_DECRYPT() {
    return new CmmOperation_DECRYPT();
  }
  public boolean is_ENCRYPT() { return this instanceof CmmOperation_ENCRYPT; }
  public boolean is_DECRYPT() { return this instanceof CmmOperation_DECRYPT; }
  public static java.util.ArrayList<CmmOperation> AllSingletonConstructors() {
    java.util.ArrayList<CmmOperation> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CmmOperation_ENCRYPT());
    singleton_iterator.add(new CmmOperation_DECRYPT());
    return singleton_iterator;
  }
}
