// Class GetKeyDescriptionInput
// Dafny class GetKeyDescriptionInput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyDescriptionInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _json;
  public GetKeyDescriptionInput (dafny.DafnySequence<? extends java.lang.Byte> json) {
    this._json = json;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyDescriptionInput o = (GetKeyDescriptionInput)other;
    return true && java.util.Objects.equals(this._json, o._json);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._json);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput.GetKeyDescriptionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._json));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyDescriptionInput> _TYPE = dafny.TypeDescriptor.<GetKeyDescriptionInput>referenceWithInitializer(GetKeyDescriptionInput.class, () -> GetKeyDescriptionInput.Default());
  public static dafny.TypeDescriptor<GetKeyDescriptionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyDescriptionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyDescriptionInput theDefault = GetKeyDescriptionInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static GetKeyDescriptionInput Default() {
    return theDefault;
  }
  public static GetKeyDescriptionInput create(dafny.DafnySequence<? extends java.lang.Byte> json) {
    return new GetKeyDescriptionInput(json);
  }
  public static GetKeyDescriptionInput create_GetKeyDescriptionInput(dafny.DafnySequence<? extends java.lang.Byte> json) {
    return create(json);
  }
  public boolean is_GetKeyDescriptionInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_json() {
    return this._json;
  }
}
