// Class CodePoint
// Dafny class CodePoint compiled into Java
package Unicode_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CodePoint {
  public CodePoint() {
  }
  public static boolean _Is(int __source) {
    int _0_i = (__source);
    return (((_0_i) == 0 ? 0 : 1) != -1) && (java.lang.Integer.compareUnsigned(_0_i, 1114111) <= 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
