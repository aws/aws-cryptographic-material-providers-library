// Class RSAModulusLengthBits
// Dafny class RSAModulusLengthBits compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAModulusLengthBits {
  public RSAModulusLengthBits() {
  }
  public static boolean _Is(int __source) {
    int _1_x = (__source);
    if (true) {
      return __default.IsValid__RSAModulusLengthBits(_1_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
