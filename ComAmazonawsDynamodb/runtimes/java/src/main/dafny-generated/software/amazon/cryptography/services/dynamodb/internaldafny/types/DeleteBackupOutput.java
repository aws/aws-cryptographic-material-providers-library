// Class DeleteBackupOutput
// Dafny class DeleteBackupOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteBackupOutput {
  public Wrappers_Compile.Option<BackupDescription> _BackupDescription;
  public DeleteBackupOutput (Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    this._BackupDescription = BackupDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteBackupOutput o = (DeleteBackupOutput)other;
    return true && java.util.Objects.equals(this._BackupDescription, o._BackupDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteBackupOutput.DeleteBackupOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteBackupOutput> _TYPE = dafny.TypeDescriptor.<DeleteBackupOutput>referenceWithInitializer(DeleteBackupOutput.class, () -> DeleteBackupOutput.Default());
  public static dafny.TypeDescriptor<DeleteBackupOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteBackupOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteBackupOutput theDefault = DeleteBackupOutput.create(Wrappers_Compile.Option.<BackupDescription>Default(BackupDescription._typeDescriptor()));
  public static DeleteBackupOutput Default() {
    return theDefault;
  }
  public static DeleteBackupOutput create(Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    return new DeleteBackupOutput(BackupDescription);
  }
  public static DeleteBackupOutput create_DeleteBackupOutput(Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    return create(BackupDescription);
  }
  public boolean is_DeleteBackupOutput() { return true; }
  public Wrappers_Compile.Option<BackupDescription> dtor_BackupDescription() {
    return this._BackupDescription;
  }
}
