// Class HighSurrogateCodePoint
// Dafny class HighSurrogateCodePoint compiled into Java
package Unicode_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class HighSurrogateCodePoint {
  public HighSurrogateCodePoint() {
  }
  public static int Witness = __default.HIGH__SURROGATE__MIN();
  public static int defaultValue() {
    return Witness;
  }
  public static boolean _Is(int __source) {
    int _1_p = (__source);
    if (CodePoint._Is(_1_p)) {
      return (java.lang.Integer.compareUnsigned(__default.HIGH__SURROGATE__MIN(), _1_p) <= 0) && (java.lang.Integer.compareUnsigned(_1_p, __default.HIGH__SURROGATE__MAX()) <= 0);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(Witness);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
