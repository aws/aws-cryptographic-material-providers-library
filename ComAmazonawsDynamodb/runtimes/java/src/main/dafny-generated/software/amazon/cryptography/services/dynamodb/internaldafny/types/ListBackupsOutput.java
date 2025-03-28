// Class ListBackupsOutput
// Dafny class ListBackupsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListBackupsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends BackupSummary>> _BackupSummaries;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastEvaluatedBackupArn;
  public ListBackupsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends BackupSummary>> BackupSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedBackupArn) {
    this._BackupSummaries = BackupSummaries;
    this._LastEvaluatedBackupArn = LastEvaluatedBackupArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListBackupsOutput o = (ListBackupsOutput)other;
    return true && java.util.Objects.equals(this._BackupSummaries, o._BackupSummaries) && java.util.Objects.equals(this._LastEvaluatedBackupArn, o._LastEvaluatedBackupArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupSummaries);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastEvaluatedBackupArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListBackupsOutput.ListBackupsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._BackupSummaries));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastEvaluatedBackupArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListBackupsOutput> _TYPE = dafny.TypeDescriptor.<ListBackupsOutput>referenceWithInitializer(ListBackupsOutput.class, () -> ListBackupsOutput.Default());
  public static dafny.TypeDescriptor<ListBackupsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListBackupsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListBackupsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListBackupsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends BackupSummary>>Default(dafny.DafnySequence.<BackupSummary>_typeDescriptor(BackupSummary._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupArn._typeDescriptor()));
  public static ListBackupsOutput Default() {
    return theDefault;
  }
  public static ListBackupsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends BackupSummary>> BackupSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedBackupArn) {
    return new ListBackupsOutput(BackupSummaries, LastEvaluatedBackupArn);
  }
  public static ListBackupsOutput create_ListBackupsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends BackupSummary>> BackupSummaries, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedBackupArn) {
    return create(BackupSummaries, LastEvaluatedBackupArn);
  }
  public boolean is_ListBackupsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends BackupSummary>> dtor_BackupSummaries() {
    return this._BackupSummaries;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastEvaluatedBackupArn() {
    return this._LastEvaluatedBackupArn;
  }
}
