// Class GetBranchKeyIdOutput
// Dafny class GetBranchKeyIdOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetBranchKeyIdOutput {
  public dafny.DafnySequence<? extends Character> _branchKeyId;
  public GetBranchKeyIdOutput (dafny.DafnySequence<? extends Character> branchKeyId) {
    this._branchKeyId = branchKeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBranchKeyIdOutput o = (GetBranchKeyIdOutput)other;
    return true && java.util.Objects.equals(this._branchKeyId, o._branchKeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.GetBranchKeyIdOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBranchKeyIdOutput> _TYPE = dafny.TypeDescriptor.<GetBranchKeyIdOutput>referenceWithInitializer(GetBranchKeyIdOutput.class, () -> GetBranchKeyIdOutput.Default());
  public static dafny.TypeDescriptor<GetBranchKeyIdOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBranchKeyIdOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBranchKeyIdOutput theDefault = GetBranchKeyIdOutput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetBranchKeyIdOutput Default() {
    return theDefault;
  }
  public static GetBranchKeyIdOutput create(dafny.DafnySequence<? extends Character> branchKeyId) {
    return new GetBranchKeyIdOutput(branchKeyId);
  }
  public static GetBranchKeyIdOutput create_GetBranchKeyIdOutput(dafny.DafnySequence<? extends Character> branchKeyId) {
    return create(branchKeyId);
  }
  public boolean is_GetBranchKeyIdOutput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyId() {
    return this._branchKeyId;
  }
}
