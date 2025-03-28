// Class RestoreSummary
// Dafny class RestoreSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RestoreSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceBackupArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceTableArn;
  public dafny.DafnySequence<? extends Character> _RestoreDateTime;
  public boolean _RestoreInProgress;
  public RestoreSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceBackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, dafny.DafnySequence<? extends Character> RestoreDateTime, boolean RestoreInProgress) {
    this._SourceBackupArn = SourceBackupArn;
    this._SourceTableArn = SourceTableArn;
    this._RestoreDateTime = RestoreDateTime;
    this._RestoreInProgress = RestoreInProgress;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RestoreSummary o = (RestoreSummary)other;
    return true && java.util.Objects.equals(this._SourceBackupArn, o._SourceBackupArn) && java.util.Objects.equals(this._SourceTableArn, o._SourceTableArn) && java.util.Objects.equals(this._RestoreDateTime, o._RestoreDateTime) && this._RestoreInProgress == o._RestoreInProgress;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceBackupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceTableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RestoreDateTime);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._RestoreInProgress);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.RestoreSummary.RestoreSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._SourceBackupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceTableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RestoreDateTime));
    s.append(", ");
    s.append(this._RestoreInProgress);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RestoreSummary> _TYPE = dafny.TypeDescriptor.<RestoreSummary>referenceWithInitializer(RestoreSummary.class, () -> RestoreSummary.Default());
  public static dafny.TypeDescriptor<RestoreSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<RestoreSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RestoreSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), false);
  public static RestoreSummary Default() {
    return theDefault;
  }
  public static RestoreSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceBackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, dafny.DafnySequence<? extends Character> RestoreDateTime, boolean RestoreInProgress) {
    return new RestoreSummary(SourceBackupArn, SourceTableArn, RestoreDateTime, RestoreInProgress);
  }
  public static RestoreSummary create_RestoreSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceBackupArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, dafny.DafnySequence<? extends Character> RestoreDateTime, boolean RestoreInProgress) {
    return create(SourceBackupArn, SourceTableArn, RestoreDateTime, RestoreInProgress);
  }
  public boolean is_RestoreSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceBackupArn() {
    return this._SourceBackupArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceTableArn() {
    return this._SourceTableArn;
  }
  public dafny.DafnySequence<? extends Character> dtor_RestoreDateTime() {
    return this._RestoreDateTime;
  }
  public boolean dtor_RestoreInProgress() {
    return this._RestoreInProgress;
  }
}
