// Class ErrorCount
// Dafny class ErrorCount compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ErrorCount {
  public ErrorCount() {
  }
  public static boolean _Is(long __source) {
    long _0_x = (__source);
    if (true) {
      return __default.IsValid__ErrorCount(_0_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Long> _TYPE = dafny.TypeDescriptor.longWithDefault(0L);
  public static dafny.TypeDescriptor<java.lang.Long> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Long>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
