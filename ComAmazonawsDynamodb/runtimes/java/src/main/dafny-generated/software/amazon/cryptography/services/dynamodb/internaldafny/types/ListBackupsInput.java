// Class ListBackupsInput
// Dafny class ListBackupsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListBackupsInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TimeRangeLowerBound;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TimeRangeUpperBound;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExclusiveStartBackupArn;
  public Wrappers_Compile.Option<BackupTypeFilter> _BackupType;
  public ListBackupsInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeLowerBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeUpperBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartBackupArn, Wrappers_Compile.Option<BackupTypeFilter> BackupType) {
    this._TableName = TableName;
    this._Limit = Limit;
    this._TimeRangeLowerBound = TimeRangeLowerBound;
    this._TimeRangeUpperBound = TimeRangeUpperBound;
    this._ExclusiveStartBackupArn = ExclusiveStartBackupArn;
    this._BackupType = BackupType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListBackupsInput o = (ListBackupsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._TimeRangeLowerBound, o._TimeRangeLowerBound) && java.util.Objects.equals(this._TimeRangeUpperBound, o._TimeRangeUpperBound) && java.util.Objects.equals(this._ExclusiveStartBackupArn, o._ExclusiveStartBackupArn) && java.util.Objects.equals(this._BackupType, o._BackupType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeRangeLowerBound);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeRangeUpperBound);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExclusiveStartBackupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListBackupsInput.ListBackupsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TimeRangeLowerBound));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TimeRangeUpperBound));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExclusiveStartBackupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListBackupsInput> _TYPE = dafny.TypeDescriptor.<ListBackupsInput>referenceWithInitializer(ListBackupsInput.class, () -> ListBackupsInput.Default());
  public static dafny.TypeDescriptor<ListBackupsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListBackupsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListBackupsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListBackupsInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(BackupsInputLimit._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupArn._typeDescriptor()), Wrappers_Compile.Option.<BackupTypeFilter>Default(BackupTypeFilter._typeDescriptor()));
  public static ListBackupsInput Default() {
    return theDefault;
  }
  public static ListBackupsInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeLowerBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeUpperBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartBackupArn, Wrappers_Compile.Option<BackupTypeFilter> BackupType) {
    return new ListBackupsInput(TableName, Limit, TimeRangeLowerBound, TimeRangeUpperBound, ExclusiveStartBackupArn, BackupType);
  }
  public static ListBackupsInput create_ListBackupsInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeLowerBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TimeRangeUpperBound, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartBackupArn, Wrappers_Compile.Option<BackupTypeFilter> BackupType) {
    return create(TableName, Limit, TimeRangeLowerBound, TimeRangeUpperBound, ExclusiveStartBackupArn, BackupType);
  }
  public boolean is_ListBackupsInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TimeRangeLowerBound() {
    return this._TimeRangeLowerBound;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TimeRangeUpperBound() {
    return this._TimeRangeUpperBound;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExclusiveStartBackupArn() {
    return this._ExclusiveStartBackupArn;
  }
  public Wrappers_Compile.Option<BackupTypeFilter> dtor_BackupType() {
    return this._BackupType;
  }
}
