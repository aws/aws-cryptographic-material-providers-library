// Class VerifyMacResponse
// Dafny class VerifyMacResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class VerifyMacResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<Boolean> _MacValid;
  public Wrappers_Compile.Option<MacAlgorithmSpec> _MacAlgorithm;
  public VerifyMacResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> MacValid, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm) {
    this._KeyId = KeyId;
    this._MacValid = MacValid;
    this._MacAlgorithm = MacAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VerifyMacResponse o = (VerifyMacResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._MacValid, o._MacValid) && java.util.Objects.equals(this._MacAlgorithm, o._MacAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacValid);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.VerifyMacResponse.VerifyMacResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacValid));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VerifyMacResponse> _TYPE = dafny.TypeDescriptor.<VerifyMacResponse>referenceWithInitializer(VerifyMacResponse.class, () -> VerifyMacResponse.Default());
  public static dafny.TypeDescriptor<VerifyMacResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<VerifyMacResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VerifyMacResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.VerifyMacResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<MacAlgorithmSpec>Default(MacAlgorithmSpec._typeDescriptor()));
  public static VerifyMacResponse Default() {
    return theDefault;
  }
  public static VerifyMacResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> MacValid, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm) {
    return new VerifyMacResponse(KeyId, MacValid, MacAlgorithm);
  }
  public static VerifyMacResponse create_VerifyMacResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<Boolean> MacValid, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm) {
    return create(KeyId, MacValid, MacAlgorithm);
  }
  public boolean is_VerifyMacResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_MacValid() {
    return this._MacValid;
  }
  public Wrappers_Compile.Option<MacAlgorithmSpec> dtor_MacAlgorithm() {
    return this._MacAlgorithm;
  }
}
