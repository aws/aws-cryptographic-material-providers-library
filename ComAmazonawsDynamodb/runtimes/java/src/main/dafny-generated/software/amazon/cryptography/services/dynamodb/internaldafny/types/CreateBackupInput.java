// Class CreateBackupInput
// Dafny class CreateBackupInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateBackupInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends Character> _BackupName;
  public CreateBackupInput (dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> BackupName) {
    this._TableName = TableName;
    this._BackupName = BackupName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateBackupInput o = (CreateBackupInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._BackupName, o._BackupName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateBackupInput.CreateBackupInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateBackupInput> _TYPE = dafny.TypeDescriptor.<CreateBackupInput>referenceWithInitializer(CreateBackupInput.class, () -> CreateBackupInput.Default());
  public static dafny.TypeDescriptor<CreateBackupInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateBackupInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateBackupInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateBackupInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateBackupInput Default() {
    return theDefault;
  }
  public static CreateBackupInput create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> BackupName) {
    return new CreateBackupInput(TableName, BackupName);
  }
  public static CreateBackupInput create_CreateBackupInput(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> BackupName) {
    return create(TableName, BackupName);
  }
  public boolean is_CreateBackupInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_BackupName() {
    return this._BackupName;
  }
}
