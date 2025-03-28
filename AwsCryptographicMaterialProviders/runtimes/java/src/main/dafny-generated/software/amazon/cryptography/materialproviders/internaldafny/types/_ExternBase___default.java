// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static boolean IsValid__CountingNumber(int x) {
    return (1) <= (x);
  }
  public static boolean IsValid__PositiveInteger(int x) {
    return java.lang.Integer.signum((x)) != -1;
  }
  public static boolean IsValid__PositiveLong(long x) {
    return java.lang.Long.signum((x)) != -1;
  }
  public static boolean IsDummySubsetType(java.math.BigInteger x) {
    return (x).signum() == 1;
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyMaterialProvidersTypes._default";
  }
}
