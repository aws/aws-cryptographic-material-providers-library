// Class GetBeaconKeyInput
// Dafny class GetBeaconKeyInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetBeaconKeyInput {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public GetBeaconKeyInput (dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    this._branchKeyIdentifier = branchKeyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBeaconKeyInput o = (GetBeaconKeyInput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.GetBeaconKeyInput.GetBeaconKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBeaconKeyInput> _TYPE = dafny.TypeDescriptor.<GetBeaconKeyInput>referenceWithInitializer(GetBeaconKeyInput.class, () -> GetBeaconKeyInput.Default());
  public static dafny.TypeDescriptor<GetBeaconKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBeaconKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBeaconKeyInput theDefault = software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetBeaconKeyInput Default() {
    return theDefault;
  }
  public static GetBeaconKeyInput create(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return new GetBeaconKeyInput(branchKeyIdentifier);
  }
  public static GetBeaconKeyInput create_GetBeaconKeyInput(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return create(branchKeyIdentifier);
  }
  public boolean is_GetBeaconKeyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
}
