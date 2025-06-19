// Class BackupSummary
// Dafny class BackupSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _BackupArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _BackupName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _BackupCreationDateTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _BackupExpiryDateTime;
  public Wrappers_Compile.Option<BackupStatus> _BackupStatus;
  public Wrappers_Compile.Option<BackupType> _BackupType;
  public Wrappers_Compile.Option<java.lang.Long> _BackupSizeBytes;
  public BackupSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime, Wrappers_Compile.Option<BackupStatus> BackupStatus, Wrappers_Compile.Option<BackupType> BackupType, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes) {
    this._TableName = TableName;
    this._TableId = TableId;
    this._TableArn = TableArn;
    this._BackupArn = BackupArn;
    this._BackupName = BackupName;
    this._BackupCreationDateTime = BackupCreationDateTime;
    this._BackupExpiryDateTime = BackupExpiryDateTime;
    this._BackupStatus = BackupStatus;
    this._BackupType = BackupType;
    this._BackupSizeBytes = BackupSizeBytes;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupSummary o = (BackupSummary)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._TableId, o._TableId) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._BackupArn, o._BackupArn) && java.util.Objects.equals(this._BackupName, o._BackupName) && java.util.Objects.equals(this._BackupCreationDateTime, o._BackupCreationDateTime) && java.util.Objects.equals(this._BackupExpiryDateTime, o._BackupExpiryDateTime) && java.util.Objects.equals(this._BackupStatus, o._BackupStatus) && java.util.Objects.equals(this._BackupType, o._BackupType) && java.util.Objects.equals(this._BackupSizeBytes, o._BackupSizeBytes);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupCreationDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupExpiryDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupSizeBytes);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BackupSummary.BackupSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupCreationDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupExpiryDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupSizeBytes));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BackupSummary> _TYPE = dafny.TypeDescriptor.<BackupSummary>referenceWithInitializer(BackupSummary.class, () -> BackupSummary.Default());
  public static dafny.TypeDescriptor<BackupSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupSummary theDefault = BackupSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<BackupStatus>Default(BackupStatus._typeDescriptor()), Wrappers_Compile.Option.<BackupType>Default(BackupType._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BackupSizeBytes._typeDescriptor()));
  public static BackupSummary Default() {
    return theDefault;
  }
  public static BackupSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime, Wrappers_Compile.Option<BackupStatus> BackupStatus, Wrappers_Compile.Option<BackupType> BackupType, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes) {
    return new BackupSummary(TableName, TableId, TableArn, BackupArn, BackupName, BackupCreationDateTime, BackupExpiryDateTime, BackupStatus, BackupType, BackupSizeBytes);
  }
  public static BackupSummary create_BackupSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupCreationDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> BackupExpiryDateTime, Wrappers_Compile.Option<BackupStatus> BackupStatus, Wrappers_Compile.Option<BackupType> BackupType, Wrappers_Compile.Option<java.lang.Long> BackupSizeBytes) {
    return create(TableName, TableId, TableArn, BackupArn, BackupName, BackupCreationDateTime, BackupExpiryDateTime, BackupStatus, BackupType, BackupSizeBytes);
  }
  public boolean is_BackupSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableId() {
    return this._TableId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_BackupArn() {
    return this._BackupArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_BackupName() {
    return this._BackupName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_BackupCreationDateTime() {
    return this._BackupCreationDateTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_BackupExpiryDateTime() {
    return this._BackupExpiryDateTime;
  }
  public Wrappers_Compile.Option<BackupStatus> dtor_BackupStatus() {
    return this._BackupStatus;
  }
  public Wrappers_Compile.Option<BackupType> dtor_BackupType() {
    return this._BackupType;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_BackupSizeBytes() {
    return this._BackupSizeBytes;
  }
}
