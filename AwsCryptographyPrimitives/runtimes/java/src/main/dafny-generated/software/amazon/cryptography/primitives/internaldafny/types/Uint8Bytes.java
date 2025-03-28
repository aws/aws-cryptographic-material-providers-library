// Class Uint8Bytes
// Dafny class Uint8Bytes compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Uint8Bytes {
  public Uint8Bytes() {
  }
  public static boolean _Is(int __source) {
    int _5_x = (__source);
    if (true) {
      return __default.IsValid__Uint8Bytes(_5_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
