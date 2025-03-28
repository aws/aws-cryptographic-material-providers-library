// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static boolean IsValid__PositiveInteger(int x) {
    return java.lang.Integer.signum((x)) != -1;
  }
  public static boolean IsValid__RSAModulusLengthBits(int x) {
    return (81) <= (x);
  }
  public static boolean IsValid__RSAModulusLengthBitsToGenerate(int x) {
    return ((81) <= (x)) && ((x) <= (4096));
  }
  public static boolean IsValid__SymmetricKeyLength(int x) {
    return ((1) <= (x)) && ((x) <= (32));
  }
  public static boolean IsValid__Uint8Bits(int x) {
    return (java.lang.Integer.signum((x)) != -1) && ((x) <= (255));
  }
  public static boolean IsValid__Uint8Bytes(int x) {
    return (java.lang.Integer.signum((x)) != -1) && ((x) <= (32));
  }
  public static boolean IsDummySubsetType(java.math.BigInteger x) {
    return (x).signum() == 1;
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyPrimitivesTypes._default";
  }
}
