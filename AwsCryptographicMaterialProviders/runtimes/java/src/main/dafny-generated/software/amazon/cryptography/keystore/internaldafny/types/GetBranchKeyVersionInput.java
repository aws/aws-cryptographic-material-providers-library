// Class GetBranchKeyVersionInput
// Dafny class GetBranchKeyVersionInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetBranchKeyVersionInput {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public dafny.DafnySequence<? extends Character> _branchKeyVersion;
  public GetBranchKeyVersionInput (dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends Character> branchKeyVersion) {
    this._branchKeyIdentifier = branchKeyIdentifier;
    this._branchKeyVersion = branchKeyVersion;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBranchKeyVersionInput o = (GetBranchKeyVersionInput)other;
    return true && java.util.Objects.equals(this._branchKeyIdentifier, o._branchKeyIdentifier) && java.util.Objects.equals(this._branchKeyVersion, o._branchKeyVersion);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyVersion);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput.GetBranchKeyVersionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKeyVersion));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBranchKeyVersionInput> _TYPE = dafny.TypeDescriptor.<GetBranchKeyVersionInput>referenceWithInitializer(GetBranchKeyVersionInput.class, () -> GetBranchKeyVersionInput.Default());
  public static dafny.TypeDescriptor<GetBranchKeyVersionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBranchKeyVersionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBranchKeyVersionInput theDefault = software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetBranchKeyVersionInput Default() {
    return theDefault;
  }
  public static GetBranchKeyVersionInput create(dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends Character> branchKeyVersion) {
    return new GetBranchKeyVersionInput(branchKeyIdentifier, branchKeyVersion);
  }
  public static GetBranchKeyVersionInput create_GetBranchKeyVersionInput(dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends Character> branchKeyVersion) {
    return create(branchKeyIdentifier, branchKeyVersion);
  }
  public boolean is_GetBranchKeyVersionInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyVersion() {
    return this._branchKeyVersion;
  }
}
