// Class CreateKeyStoreOutput
// Dafny class CreateKeyStoreOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyStoreOutput {
  public dafny.DafnySequence<? extends Character> _tableArn;
  public CreateKeyStoreOutput (dafny.DafnySequence<? extends Character> tableArn) {
    this._tableArn = tableArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyStoreOutput o = (CreateKeyStoreOutput)other;
    return true && java.util.Objects.equals(this._tableArn, o._tableArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._tableArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput.CreateKeyStoreOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._tableArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyStoreOutput> _TYPE = dafny.TypeDescriptor.<CreateKeyStoreOutput>referenceWithInitializer(CreateKeyStoreOutput.class, () -> CreateKeyStoreOutput.Default());
  public static dafny.TypeDescriptor<CreateKeyStoreOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyStoreOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyStoreOutput theDefault = CreateKeyStoreOutput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateKeyStoreOutput Default() {
    return theDefault;
  }
  public static CreateKeyStoreOutput create(dafny.DafnySequence<? extends Character> tableArn) {
    return new CreateKeyStoreOutput(tableArn);
  }
  public static CreateKeyStoreOutput create_CreateKeyStoreOutput(dafny.DafnySequence<? extends Character> tableArn) {
    return create(tableArn);
  }
  public boolean is_CreateKeyStoreOutput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_tableArn() {
    return this._tableArn;
  }
}
