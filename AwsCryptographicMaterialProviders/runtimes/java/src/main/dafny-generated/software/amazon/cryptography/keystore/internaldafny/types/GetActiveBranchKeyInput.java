// Class GetActiveBranchKeyInput
// Dafny class GetActiveBranchKeyInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetActiveBranchKeyInput {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public GetActiveBranchKeyInput (dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    this._branchKeyIdentifier = branchKeyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetActiveBranchKeyInput o = (GetActiveBranchKeyInput)other;
    return true && java.util.Objects.equals(this._branchKeyIdentifier, o._branchKeyIdentifier);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyIdentifier);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput.GetActiveBranchKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetActiveBranchKeyInput> _TYPE = dafny.TypeDescriptor.<GetActiveBranchKeyInput>referenceWithInitializer(GetActiveBranchKeyInput.class, () -> GetActiveBranchKeyInput.Default());
  public static dafny.TypeDescriptor<GetActiveBranchKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetActiveBranchKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetActiveBranchKeyInput theDefault = GetActiveBranchKeyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetActiveBranchKeyInput Default() {
    return theDefault;
  }
  public static GetActiveBranchKeyInput create(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return new GetActiveBranchKeyInput(branchKeyIdentifier);
  }
  public static GetActiveBranchKeyInput create_GetActiveBranchKeyInput(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return create(branchKeyIdentifier);
  }
  public boolean is_GetActiveBranchKeyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
}
