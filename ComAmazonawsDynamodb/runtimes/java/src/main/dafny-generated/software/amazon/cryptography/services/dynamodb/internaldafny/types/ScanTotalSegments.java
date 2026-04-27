// Class ScanTotalSegments
// Dafny class ScanTotalSegments compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ScanTotalSegments {
  public ScanTotalSegments() {
  }
  public static boolean _Is(int __source) {
    int _40_x = (__source);
    if (true) {
      return __default.IsValid__ScanTotalSegments(_40_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
