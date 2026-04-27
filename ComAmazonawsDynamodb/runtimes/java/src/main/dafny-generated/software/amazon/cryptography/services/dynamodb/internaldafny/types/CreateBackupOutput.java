// Class CreateBackupOutput
// Dafny class CreateBackupOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateBackupOutput {
  public Wrappers_Compile.Option<BackupDetails> _BackupDetails;
  public CreateBackupOutput (Wrappers_Compile.Option<BackupDetails> BackupDetails) {
    this._BackupDetails = BackupDetails;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateBackupOutput o = (CreateBackupOutput)other;
    return true && java.util.Objects.equals(this._BackupDetails, o._BackupDetails);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupDetails);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateBackupOutput.CreateBackupOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupDetails));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateBackupOutput> _TYPE = dafny.TypeDescriptor.<CreateBackupOutput>referenceWithInitializer(CreateBackupOutput.class, () -> CreateBackupOutput.Default());
  public static dafny.TypeDescriptor<CreateBackupOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateBackupOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateBackupOutput theDefault = CreateBackupOutput.create(Wrappers_Compile.Option.<BackupDetails>Default(BackupDetails._typeDescriptor()));
  public static CreateBackupOutput Default() {
    return theDefault;
  }
  public static CreateBackupOutput create(Wrappers_Compile.Option<BackupDetails> BackupDetails) {
    return new CreateBackupOutput(BackupDetails);
  }
  public static CreateBackupOutput create_CreateBackupOutput(Wrappers_Compile.Option<BackupDetails> BackupDetails) {
    return create(BackupDetails);
  }
  public boolean is_CreateBackupOutput() { return true; }
  public Wrappers_Compile.Option<BackupDetails> dtor_BackupDetails() {
    return this._BackupDetails;
  }
}
