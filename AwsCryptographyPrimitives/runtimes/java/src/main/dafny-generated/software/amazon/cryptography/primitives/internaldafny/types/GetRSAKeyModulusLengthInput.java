// Class GetRSAKeyModulusLengthInput
// Dafny class GetRSAKeyModulusLengthInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetRSAKeyModulusLengthInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public GetRSAKeyModulusLengthInput (dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetRSAKeyModulusLengthInput o = (GetRSAKeyModulusLengthInput)other;
    return true && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthInput.GetRSAKeyModulusLengthInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetRSAKeyModulusLengthInput> _TYPE = dafny.TypeDescriptor.<GetRSAKeyModulusLengthInput>referenceWithInitializer(GetRSAKeyModulusLengthInput.class, () -> GetRSAKeyModulusLengthInput.Default());
  public static dafny.TypeDescriptor<GetRSAKeyModulusLengthInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetRSAKeyModulusLengthInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetRSAKeyModulusLengthInput theDefault = GetRSAKeyModulusLengthInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static GetRSAKeyModulusLengthInput Default() {
    return theDefault;
  }
  public static GetRSAKeyModulusLengthInput create(dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new GetRSAKeyModulusLengthInput(publicKey);
  }
  public static GetRSAKeyModulusLengthInput create_GetRSAKeyModulusLengthInput(dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return create(publicKey);
  }
  public boolean is_GetRSAKeyModulusLengthInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
}
