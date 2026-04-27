// Class RotationPeriodInDaysType
// Dafny class RotationPeriodInDaysType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RotationPeriodInDaysType {
  public RotationPeriodInDaysType() {
  }
  public static boolean _Is(int __source) {
    int _24_x = (__source);
    if (true) {
      return __default.IsValid__RotationPeriodInDaysType(_24_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
