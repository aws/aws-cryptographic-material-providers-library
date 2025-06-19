// Class ListImportsMaxLimit
// Dafny class ListImportsMaxLimit compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListImportsMaxLimit {
  public ListImportsMaxLimit() {
  }
  public static boolean _Is(int __source) {
    int _16_x = (__source);
    if (true) {
      return __default.IsValid__ListImportsMaxLimit(_16_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
