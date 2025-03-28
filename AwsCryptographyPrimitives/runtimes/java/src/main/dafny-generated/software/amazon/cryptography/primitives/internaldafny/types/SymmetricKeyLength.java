// Class SymmetricKeyLength
// Dafny class SymmetricKeyLength compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SymmetricKeyLength {
  public SymmetricKeyLength() {
  }
  public static boolean _Is(int __source) {
    int _3_x = (__source);
    if (true) {
      return __default.IsValid__SymmetricKeyLength(_3_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
