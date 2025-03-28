// Class ScanSegment
// Dafny class ScanSegment compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ScanSegment {
  public ScanSegment() {
  }
  public static boolean _Is(int __source) {
    int _39_x = (__source);
    if (true) {
      return __default.IsValid__ScanSegment(_39_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
