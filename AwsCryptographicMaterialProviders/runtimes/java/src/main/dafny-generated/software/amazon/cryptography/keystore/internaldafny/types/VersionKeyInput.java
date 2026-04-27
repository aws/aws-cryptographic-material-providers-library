// Class VersionKeyInput
// Dafny class VersionKeyInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class VersionKeyInput {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public VersionKeyInput (dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    this._branchKeyIdentifier = branchKeyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VersionKeyInput o = (VersionKeyInput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.VersionKeyInput.VersionKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VersionKeyInput> _TYPE = dafny.TypeDescriptor.<VersionKeyInput>referenceWithInitializer(VersionKeyInput.class, () -> VersionKeyInput.Default());
  public static dafny.TypeDescriptor<VersionKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<VersionKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VersionKeyInput theDefault = VersionKeyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static VersionKeyInput Default() {
    return theDefault;
  }
  public static VersionKeyInput create(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return new VersionKeyInput(branchKeyIdentifier);
  }
  public static VersionKeyInput create_VersionKeyInput(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return create(branchKeyIdentifier);
  }
  public boolean is_VersionKeyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
}
