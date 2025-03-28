// Class ListTablesInputLimit
// Dafny class ListTablesInputLimit compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListTablesInputLimit {
  public ListTablesInputLimit() {
  }
  public static boolean _Is(int __source) {
    int _17_x = (__source);
    if (true) {
      return __default.IsValid__ListTablesInputLimit(_17_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
