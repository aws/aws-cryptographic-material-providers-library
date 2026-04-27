// Class DescribeBackupInput
// Dafny class DescribeBackupInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeBackupInput {
  public dafny.DafnySequence<? extends Character> _BackupArn;
  public DescribeBackupInput (dafny.DafnySequence<? extends Character> BackupArn) {
    this._BackupArn = BackupArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeBackupInput o = (DescribeBackupInput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeBackupInput.DescribeBackupInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeBackupInput> _TYPE = dafny.TypeDescriptor.<DescribeBackupInput>referenceWithInitializer(DescribeBackupInput.class, () -> DescribeBackupInput.Default());
  public static dafny.TypeDescriptor<DescribeBackupInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeBackupInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeBackupInput theDefault = DescribeBackupInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeBackupInput Default() {
    return theDefault;
  }
  public static DescribeBackupInput create(dafny.DafnySequence<? extends Character> BackupArn) {
    return new DescribeBackupInput(BackupArn);
  }
  public static DescribeBackupInput create_DescribeBackupInput(dafny.DafnySequence<? extends Character> BackupArn) {
    return create(BackupArn);
  }
  public boolean is_DescribeBackupInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_BackupArn() {
    return this._BackupArn;
  }
}
