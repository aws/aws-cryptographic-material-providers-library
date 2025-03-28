// Class GenerateMacResponse
// Dafny class GenerateMacResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateMacResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _Mac;
  public Wrappers_Compile.Option<MacAlgorithmSpec> _MacAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public GenerateMacResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Mac, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    this._Mac = Mac;
    this._MacAlgorithm = MacAlgorithm;
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateMacResponse o = (GenerateMacResponse)other;
    return true && java.util.Objects.equals(this._Mac, o._Mac) && java.util.Objects.equals(this._MacAlgorithm, o._MacAlgorithm) && java.util.Objects.equals(this._KeyId, o._KeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Mac);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateMacResponse.GenerateMacResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Mac));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateMacResponse> _TYPE = dafny.TypeDescriptor.<GenerateMacResponse>referenceWithInitializer(GenerateMacResponse.class, () -> GenerateMacResponse.Default());
  public static dafny.TypeDescriptor<GenerateMacResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateMacResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateMacResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateMacResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<MacAlgorithmSpec>Default(MacAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()));
  public static GenerateMacResponse Default() {
    return theDefault;
  }
  public static GenerateMacResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Mac, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return new GenerateMacResponse(Mac, MacAlgorithm, KeyId);
  }
  public static GenerateMacResponse create_GenerateMacResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Mac, Wrappers_Compile.Option<MacAlgorithmSpec> MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return create(Mac, MacAlgorithm, KeyId);
  }
  public boolean is_GenerateMacResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_Mac() {
    return this._Mac;
  }
  public Wrappers_Compile.Option<MacAlgorithmSpec> dtor_MacAlgorithm() {
    return this._MacAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
}
