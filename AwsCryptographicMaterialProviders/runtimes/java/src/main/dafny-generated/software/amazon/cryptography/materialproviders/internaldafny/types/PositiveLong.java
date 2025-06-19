// Class PositiveLong
// Dafny class PositiveLong compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PositiveLong {
  public PositiveLong() {
  }
  public static boolean _Is(long __source) {
    long _1_x = (__source);
    if (true) {
      return __default.IsValid__PositiveLong(_1_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Long> _TYPE = dafny.TypeDescriptor.longWithDefault(0L);
  public static dafny.TypeDescriptor<java.lang.Long> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Long>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
