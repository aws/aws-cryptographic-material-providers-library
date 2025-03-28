// Class SignatureAlgorithm
// Dafny class SignatureAlgorithm compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SignatureAlgorithm {
  public SignatureAlgorithm() {
  }
  private static final dafny.TypeDescriptor<SignatureAlgorithm> _TYPE = dafny.TypeDescriptor.<SignatureAlgorithm>referenceWithInitializer(SignatureAlgorithm.class, () -> SignatureAlgorithm.Default());
  public static dafny.TypeDescriptor<SignatureAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<SignatureAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SignatureAlgorithm theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(ECDSA.Default());
  public static SignatureAlgorithm Default() {
    return theDefault;
  }
  public static SignatureAlgorithm create_ECDSA(ECDSA ECDSA) {
    return new SignatureAlgorithm_ECDSA(ECDSA);
  }
  public static SignatureAlgorithm create_None(None None) {
    return new SignatureAlgorithm_None(None);
  }
  public boolean is_ECDSA() { return this instanceof SignatureAlgorithm_ECDSA; }
  public boolean is_None() { return this instanceof SignatureAlgorithm_None; }
  public ECDSA dtor_ECDSA() {
    SignatureAlgorithm d = this;
    return ((SignatureAlgorithm_ECDSA)d)._ECDSA;
  }
  public None dtor_None() {
    SignatureAlgorithm d = this;
    return ((SignatureAlgorithm_None)d)._None;
  }
}
