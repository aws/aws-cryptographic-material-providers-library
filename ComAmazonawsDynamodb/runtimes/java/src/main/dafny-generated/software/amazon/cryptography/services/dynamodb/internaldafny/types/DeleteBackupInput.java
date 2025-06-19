// Class DeleteBackupInput
// Dafny class DeleteBackupInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteBackupInput {
  public dafny.DafnySequence<? extends Character> _BackupArn;
  public DeleteBackupInput (dafny.DafnySequence<? extends Character> BackupArn) {
    this._BackupArn = BackupArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteBackupInput o = (DeleteBackupInput)other;
    return true && java.util.Objects.equals(this._BackupArn, o._BackupArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteBackupInput.DeleteBackupInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteBackupInput> _TYPE = dafny.TypeDescriptor.<DeleteBackupInput>referenceWithInitializer(DeleteBackupInput.class, () -> DeleteBackupInput.Default());
  public static dafny.TypeDescriptor<DeleteBackupInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteBackupInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteBackupInput theDefault = DeleteBackupInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteBackupInput Default() {
    return theDefault;
  }
  public static DeleteBackupInput create(dafny.DafnySequence<? extends Character> BackupArn) {
    return new DeleteBackupInput(BackupArn);
  }
  public static DeleteBackupInput create_DeleteBackupInput(dafny.DafnySequence<? extends Character> BackupArn) {
    return create(BackupArn);
  }
  public boolean is_DeleteBackupInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_BackupArn() {
    return this._BackupArn;
  }
}
