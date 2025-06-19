// Class DescribeBackupOutput
// Dafny class DescribeBackupOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeBackupOutput {
  public Wrappers_Compile.Option<BackupDescription> _BackupDescription;
  public DescribeBackupOutput (Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    this._BackupDescription = BackupDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeBackupOutput o = (DescribeBackupOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeBackupOutput.DescribeBackupOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeBackupOutput> _TYPE = dafny.TypeDescriptor.<DescribeBackupOutput>referenceWithInitializer(DescribeBackupOutput.class, () -> DescribeBackupOutput.Default());
  public static dafny.TypeDescriptor<DescribeBackupOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeBackupOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeBackupOutput theDefault = DescribeBackupOutput.create(Wrappers_Compile.Option.<BackupDescription>Default(BackupDescription._typeDescriptor()));
  public static DescribeBackupOutput Default() {
    return theDefault;
  }
  public static DescribeBackupOutput create(Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    return new DescribeBackupOutput(BackupDescription);
  }
  public static DescribeBackupOutput create_DescribeBackupOutput(Wrappers_Compile.Option<BackupDescription> BackupDescription) {
    return create(BackupDescription);
  }
  public boolean is_DescribeBackupOutput() { return true; }
  public Wrappers_Compile.Option<BackupDescription> dtor_BackupDescription() {
    return this._BackupDescription;
  }
}
