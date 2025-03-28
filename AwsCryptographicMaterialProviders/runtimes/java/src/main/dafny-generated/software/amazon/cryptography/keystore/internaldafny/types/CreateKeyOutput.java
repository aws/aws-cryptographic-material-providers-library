// Class CreateKeyOutput
// Dafny class CreateKeyOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyOutput {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public CreateKeyOutput (dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    this._branchKeyIdentifier = branchKeyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyOutput o = (CreateKeyOutput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.CreateKeyOutput.CreateKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyOutput> _TYPE = dafny.TypeDescriptor.<CreateKeyOutput>referenceWithInitializer(CreateKeyOutput.class, () -> CreateKeyOutput.Default());
  public static dafny.TypeDescriptor<CreateKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyOutput theDefault = software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateKeyOutput Default() {
    return theDefault;
  }
  public static CreateKeyOutput create(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return new CreateKeyOutput(branchKeyIdentifier);
  }
  public static CreateKeyOutput create_CreateKeyOutput(dafny.DafnySequence<? extends Character> branchKeyIdentifier) {
    return create(branchKeyIdentifier);
  }
  public boolean is_CreateKeyOutput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
}
