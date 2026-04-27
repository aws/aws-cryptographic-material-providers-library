// Class ListExportsMaxLimit
// Dafny class ListExportsMaxLimit compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListExportsMaxLimit {
  public ListExportsMaxLimit() {
  }
  public static boolean _Is(int __source) {
    int _15_x = (__source);
    if (true) {
      return __default.IsValid__ListExportsMaxLimit(_15_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
