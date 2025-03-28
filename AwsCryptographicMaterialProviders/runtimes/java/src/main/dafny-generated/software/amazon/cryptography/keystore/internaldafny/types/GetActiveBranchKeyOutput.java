// Class GetActiveBranchKeyOutput
// Dafny class GetActiveBranchKeyOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetActiveBranchKeyOutput {
  public BranchKeyMaterials _branchKeyMaterials;
  public GetActiveBranchKeyOutput (BranchKeyMaterials branchKeyMaterials) {
    this._branchKeyMaterials = branchKeyMaterials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetActiveBranchKeyOutput o = (GetActiveBranchKeyOutput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.GetActiveBranchKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyMaterials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetActiveBranchKeyOutput> _TYPE = dafny.TypeDescriptor.<GetActiveBranchKeyOutput>referenceWithInitializer(GetActiveBranchKeyOutput.class, () -> GetActiveBranchKeyOutput.Default());
  public static dafny.TypeDescriptor<GetActiveBranchKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetActiveBranchKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetActiveBranchKeyOutput theDefault = software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.create(BranchKeyMaterials.Default());
  public static GetActiveBranchKeyOutput Default() {
    return theDefault;
  }
  public static GetActiveBranchKeyOutput create(BranchKeyMaterials branchKeyMaterials) {
    return new GetActiveBranchKeyOutput(branchKeyMaterials);
  }
  public static GetActiveBranchKeyOutput create_GetActiveBranchKeyOutput(BranchKeyMaterials branchKeyMaterials) {
    return create(branchKeyMaterials);
  }
  public boolean is_GetActiveBranchKeyOutput() { return true; }
  public BranchKeyMaterials dtor_branchKeyMaterials() {
    return this._branchKeyMaterials;
  }
}
