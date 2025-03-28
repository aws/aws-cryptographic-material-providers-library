// Class BilledSizeBytes
// Dafny class BilledSizeBytes compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BilledSizeBytes {
  public BilledSizeBytes() {
  }
  public static boolean _Is(long __source) {
    long _10_x = (__source);
    if (true) {
      return __default.IsValid__BilledSizeBytes(_10_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Long> _TYPE = dafny.TypeDescriptor.longWithDefault(0L);
  public static dafny.TypeDescriptor<java.lang.Long> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Long>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
