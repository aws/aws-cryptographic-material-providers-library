// Class DerivationAlgorithm
// Dafny class DerivationAlgorithm compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DerivationAlgorithm {
  public DerivationAlgorithm() {
  }
  private static final dafny.TypeDescriptor<DerivationAlgorithm> _TYPE = dafny.TypeDescriptor.<DerivationAlgorithm>referenceWithInitializer(DerivationAlgorithm.class, () -> DerivationAlgorithm.Default());
  public static dafny.TypeDescriptor<DerivationAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<DerivationAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DerivationAlgorithm theDefault = DerivationAlgorithm.create_HKDF(HKDF.Default());
  public static DerivationAlgorithm Default() {
    return theDefault;
  }
  public static DerivationAlgorithm create_HKDF(HKDF HKDF) {
    return new DerivationAlgorithm_HKDF(HKDF);
  }
  public static DerivationAlgorithm create_IDENTITY(IDENTITY IDENTITY) {
    return new DerivationAlgorithm_IDENTITY(IDENTITY);
  }
  public static DerivationAlgorithm create_None(None None) {
    return new DerivationAlgorithm_None(None);
  }
  public boolean is_HKDF() { return this instanceof DerivationAlgorithm_HKDF; }
  public boolean is_IDENTITY() { return this instanceof DerivationAlgorithm_IDENTITY; }
  public boolean is_None() { return this instanceof DerivationAlgorithm_None; }
  public HKDF dtor_HKDF() {
    DerivationAlgorithm d = this;
    return ((DerivationAlgorithm_HKDF)d)._HKDF;
  }
  public IDENTITY dtor_IDENTITY() {
    DerivationAlgorithm d = this;
    return ((DerivationAlgorithm_IDENTITY)d)._IDENTITY;
  }
  public None dtor_None() {
    DerivationAlgorithm d = this;
    return ((DerivationAlgorithm_None)d)._None;
  }
}
