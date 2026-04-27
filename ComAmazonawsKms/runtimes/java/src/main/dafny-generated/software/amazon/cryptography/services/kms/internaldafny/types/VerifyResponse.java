// Class VerifyResponse
// Dafny class VerifyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class VerifyResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<Boolean> _SignatureValid;
  public Wrappers_Compile.Option<SigningAlgorithmSpec> _SigningAlgorithm;
  public VerifyResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> SignatureValid, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    this._KeyId = KeyId;
    this._SignatureValid = SignatureValid;
    this._SigningAlgorithm = SigningAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VerifyResponse o = (VerifyResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._SignatureValid, o._SignatureValid) && java.util.Objects.equals(this._SigningAlgorithm, o._SigningAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SignatureValid);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.VerifyResponse.VerifyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SignatureValid));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VerifyResponse> _TYPE = dafny.TypeDescriptor.<VerifyResponse>referenceWithInitializer(VerifyResponse.class, () -> VerifyResponse.Default());
  public static dafny.TypeDescriptor<VerifyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<VerifyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VerifyResponse theDefault = VerifyResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<SigningAlgorithmSpec>Default(SigningAlgorithmSpec._typeDescriptor()));
  public static VerifyResponse Default() {
    return theDefault;
  }
  public static VerifyResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> SignatureValid, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    return new VerifyResponse(KeyId, SignatureValid, SigningAlgorithm);
  }
  public static VerifyResponse create_VerifyResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> SignatureValid, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    return create(KeyId, SignatureValid, SigningAlgorithm);
  }
  public boolean is_VerifyResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_SignatureValid() {
    return this._SignatureValid;
  }
  public Wrappers_Compile.Option<SigningAlgorithmSpec> dtor_SigningAlgorithm() {
    return this._SigningAlgorithm;
  }
}
