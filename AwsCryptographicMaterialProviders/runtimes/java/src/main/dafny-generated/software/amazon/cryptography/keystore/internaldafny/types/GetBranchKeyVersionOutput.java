// Class GetBranchKeyVersionOutput
// Dafny class GetBranchKeyVersionOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetBranchKeyVersionOutput {
  public BranchKeyMaterials _branchKeyMaterials;
  public GetBranchKeyVersionOutput (BranchKeyMaterials branchKeyMaterials) {
    this._branchKeyMaterials = branchKeyMaterials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBranchKeyVersionOutput o = (GetBranchKeyVersionOutput)other;
    return true && java.util.Objects.equals(this._branchKeyMaterials, o._branchKeyMaterials);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyMaterials);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.GetBranchKeyVersionOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyMaterials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBranchKeyVersionOutput> _TYPE = dafny.TypeDescriptor.<GetBranchKeyVersionOutput>referenceWithInitializer(GetBranchKeyVersionOutput.class, () -> GetBranchKeyVersionOutput.Default());
  public static dafny.TypeDescriptor<GetBranchKeyVersionOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBranchKeyVersionOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBranchKeyVersionOutput theDefault = GetBranchKeyVersionOutput.create(BranchKeyMaterials.Default());
  public static GetBranchKeyVersionOutput Default() {
    return theDefault;
  }
  public static GetBranchKeyVersionOutput create(BranchKeyMaterials branchKeyMaterials) {
    return new GetBranchKeyVersionOutput(branchKeyMaterials);
  }
  public static GetBranchKeyVersionOutput create_GetBranchKeyVersionOutput(BranchKeyMaterials branchKeyMaterials) {
    return create(branchKeyMaterials);
  }
  public boolean is_GetBranchKeyVersionOutput() { return true; }
  public BranchKeyMaterials dtor_branchKeyMaterials() {
    return this._branchKeyMaterials;
  }
}
