// Class GetKeyDescriptionOutput
// Dafny class GetKeyDescriptionOutput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyDescriptionOutput {
  public KeyDescription _keyDescription;
  public GetKeyDescriptionOutput (KeyDescription keyDescription) {
    this._keyDescription = keyDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyDescriptionOutput o = (GetKeyDescriptionOutput)other;
    return true && java.util.Objects.equals(this._keyDescription, o._keyDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput.GetKeyDescriptionOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyDescriptionOutput> _TYPE = dafny.TypeDescriptor.<GetKeyDescriptionOutput>referenceWithInitializer(GetKeyDescriptionOutput.class, () -> GetKeyDescriptionOutput.Default());
  public static dafny.TypeDescriptor<GetKeyDescriptionOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyDescriptionOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyDescriptionOutput theDefault = GetKeyDescriptionOutput.create(KeyDescription.Default());
  public static GetKeyDescriptionOutput Default() {
    return theDefault;
  }
  public static GetKeyDescriptionOutput create(KeyDescription keyDescription) {
    return new GetKeyDescriptionOutput(keyDescription);
  }
  public static GetKeyDescriptionOutput create_GetKeyDescriptionOutput(KeyDescription keyDescription) {
    return create(keyDescription);
  }
  public boolean is_GetKeyDescriptionOutput() { return true; }
  public KeyDescription dtor_keyDescription() {
    return this._keyDescription;
  }
}
