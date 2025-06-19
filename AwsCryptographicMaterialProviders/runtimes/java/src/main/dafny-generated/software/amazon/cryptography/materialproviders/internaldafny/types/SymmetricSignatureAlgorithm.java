// Class SymmetricSignatureAlgorithm
// Dafny class SymmetricSignatureAlgorithm compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SymmetricSignatureAlgorithm {
  public SymmetricSignatureAlgorithm() {
  }
  private static final dafny.TypeDescriptor<SymmetricSignatureAlgorithm> _TYPE = dafny.TypeDescriptor.<SymmetricSignatureAlgorithm>referenceWithInitializer(SymmetricSignatureAlgorithm.class, () -> SymmetricSignatureAlgorithm.Default());
  public static dafny.TypeDescriptor<SymmetricSignatureAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<SymmetricSignatureAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SymmetricSignatureAlgorithm theDefault = SymmetricSignatureAlgorithm.create_HMAC(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.Default());
  public static SymmetricSignatureAlgorithm Default() {
    return theDefault;
  }
  public static SymmetricSignatureAlgorithm create_HMAC(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm HMAC) {
    return new SymmetricSignatureAlgorithm_HMAC(HMAC);
  }
  public static SymmetricSignatureAlgorithm create_None(None None) {
    return new SymmetricSignatureAlgorithm_None(None);
  }
  public boolean is_HMAC() { return this instanceof SymmetricSignatureAlgorithm_HMAC; }
  public boolean is_None() { return this instanceof SymmetricSignatureAlgorithm_None; }
  public software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm dtor_HMAC() {
    SymmetricSignatureAlgorithm d = this;
    return ((SymmetricSignatureAlgorithm_HMAC)d)._HMAC;
  }
  public None dtor_None() {
    SymmetricSignatureAlgorithm d = this;
    return ((SymmetricSignatureAlgorithm_None)d)._None;
  }
}
