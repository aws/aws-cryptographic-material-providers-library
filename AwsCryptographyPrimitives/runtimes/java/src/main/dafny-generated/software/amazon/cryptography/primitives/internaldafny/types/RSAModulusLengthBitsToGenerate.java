// Class RSAModulusLengthBitsToGenerate
// Dafny class RSAModulusLengthBitsToGenerate compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAModulusLengthBitsToGenerate {
  public RSAModulusLengthBitsToGenerate() {
  }
  public static boolean _Is(int __source) {
    int _2_x = (__source);
    if (true) {
      return __default.IsValid__RSAModulusLengthBitsToGenerate(_2_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
