// Class KeyDescriptionVersion
// Dafny class KeyDescriptionVersion compiled into Java
package KeyDescription_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescriptionVersion {
  public KeyDescriptionVersion() {
  }
  public static java.math.BigInteger Witness = java.math.BigInteger.ONE;
  public static java.math.BigInteger defaultValue() {
    return Witness;
  }
  public static boolean _Is(java.math.BigInteger __source) {
    java.math.BigInteger _0_v = __source;
    return __default.KeyDescriptionVersion_q(_0_v);
  }
  private static final dafny.TypeDescriptor<java.math.BigInteger> _TYPE = dafny.TypeDescriptor.<java.math.BigInteger>referenceWithInitializer(java.math.BigInteger.class, () -> KeyDescriptionVersion.defaultValue());
  public static dafny.TypeDescriptor<java.math.BigInteger> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.math.BigInteger>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
