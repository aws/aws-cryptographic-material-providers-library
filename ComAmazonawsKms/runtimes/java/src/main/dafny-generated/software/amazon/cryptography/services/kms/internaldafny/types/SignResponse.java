// Class SignResponse
// Dafny class SignResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SignResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _Signature;
  public Wrappers_Compile.Option<SigningAlgorithmSpec> _SigningAlgorithm;
  public SignResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Signature, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    this._KeyId = KeyId;
    this._Signature = Signature;
    this._SigningAlgorithm = SigningAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SignResponse o = (SignResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Signature, o._Signature) && java.util.Objects.equals(this._SigningAlgorithm, o._SigningAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Signature);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.SignResponse.SignResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Signature));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SignResponse> _TYPE = dafny.TypeDescriptor.<SignResponse>referenceWithInitializer(SignResponse.class, () -> SignResponse.Default());
  public static dafny.TypeDescriptor<SignResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<SignResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SignResponse theDefault = SignResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<SigningAlgorithmSpec>Default(SigningAlgorithmSpec._typeDescriptor()));
  public static SignResponse Default() {
    return theDefault;
  }
  public static SignResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Signature, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    return new SignResponse(KeyId, Signature, SigningAlgorithm);
  }
  public static SignResponse create_SignResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Signature, Wrappers_Compile.Option<SigningAlgorithmSpec> SigningAlgorithm) {
    return create(KeyId, Signature, SigningAlgorithm);
  }
  public boolean is_SignResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_Signature() {
    return this._Signature;
  }
  public Wrappers_Compile.Option<SigningAlgorithmSpec> dtor_SigningAlgorithm() {
    return this._SigningAlgorithm;
  }
}
