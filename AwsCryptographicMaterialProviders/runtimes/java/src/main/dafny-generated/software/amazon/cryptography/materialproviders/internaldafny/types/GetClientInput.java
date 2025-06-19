// Class GetClientInput
// Dafny class GetClientInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetClientInput {
  public dafny.DafnySequence<? extends Character> _region;
  public GetClientInput (dafny.DafnySequence<? extends Character> region) {
    this._region = region;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetClientInput o = (GetClientInput)other;
    return true && java.util.Objects.equals(this._region, o._region);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._region);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetClientInput.GetClientInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._region));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetClientInput> _TYPE = dafny.TypeDescriptor.<GetClientInput>referenceWithInitializer(GetClientInput.class, () -> GetClientInput.Default());
  public static dafny.TypeDescriptor<GetClientInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetClientInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetClientInput theDefault = GetClientInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetClientInput Default() {
    return theDefault;
  }
  public static GetClientInput create(dafny.DafnySequence<? extends Character> region) {
    return new GetClientInput(region);
  }
  public static GetClientInput create_GetClientInput(dafny.DafnySequence<? extends Character> region) {
    return create(region);
  }
  public boolean is_GetClientInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_region() {
    return this._region;
  }
}
