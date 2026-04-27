// Class ECDHCurveSpec
// Dafny class ECDHCurveSpec compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ECDHCurveSpec {
  public ECDHCurveSpec() {
  }
  private static final dafny.TypeDescriptor<ECDHCurveSpec> _TYPE = dafny.TypeDescriptor.<ECDHCurveSpec>referenceWithInitializer(ECDHCurveSpec.class, () -> ECDHCurveSpec.Default());
  public static dafny.TypeDescriptor<ECDHCurveSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECDHCurveSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECDHCurveSpec theDefault = ECDHCurveSpec.create_ECC__NIST__P256();
  public static ECDHCurveSpec Default() {
    return theDefault;
  }
  public static ECDHCurveSpec create_ECC__NIST__P256() {
    return new ECDHCurveSpec_ECC__NIST__P256();
  }
  public static ECDHCurveSpec create_ECC__NIST__P384() {
    return new ECDHCurveSpec_ECC__NIST__P384();
  }
  public static ECDHCurveSpec create_ECC__NIST__P521() {
    return new ECDHCurveSpec_ECC__NIST__P521();
  }
  public static ECDHCurveSpec create_SM2() {
    return new ECDHCurveSpec_SM2();
  }
  public boolean is_ECC__NIST__P256() { return this instanceof ECDHCurveSpec_ECC__NIST__P256; }
  public boolean is_ECC__NIST__P384() { return this instanceof ECDHCurveSpec_ECC__NIST__P384; }
  public boolean is_ECC__NIST__P521() { return this instanceof ECDHCurveSpec_ECC__NIST__P521; }
  public boolean is_SM2() { return this instanceof ECDHCurveSpec_SM2; }
  public static java.util.ArrayList<ECDHCurveSpec> AllSingletonConstructors() {
    java.util.ArrayList<ECDHCurveSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ECDHCurveSpec_ECC__NIST__P256());
    singleton_iterator.add(new ECDHCurveSpec_ECC__NIST__P384());
    singleton_iterator.add(new ECDHCurveSpec_ECC__NIST__P521());
    singleton_iterator.add(new ECDHCurveSpec_SM2());
    return singleton_iterator;
  }
}
