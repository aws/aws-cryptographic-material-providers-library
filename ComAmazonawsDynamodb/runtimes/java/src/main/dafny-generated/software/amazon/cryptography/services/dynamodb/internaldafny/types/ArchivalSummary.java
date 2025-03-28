// Class ArchivalSummary
// Dafny class ArchivalSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ArchivalSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ArchivalDateTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ArchivalReason;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ArchivalBackupArn;
  public ArchivalSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalReason, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalBackupArn) {
    this._ArchivalDateTime = ArchivalDateTime;
    this._ArchivalReason = ArchivalReason;
    this._ArchivalBackupArn = ArchivalBackupArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ArchivalSummary o = (ArchivalSummary)other;
    return true && java.util.Objects.equals(this._ArchivalDateTime, o._ArchivalDateTime) && java.util.Objects.equals(this._ArchivalReason, o._ArchivalReason) && java.util.Objects.equals(this._ArchivalBackupArn, o._ArchivalBackupArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ArchivalDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ArchivalReason);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ArchivalBackupArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ArchivalSummary.ArchivalSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ArchivalDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ArchivalReason));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ArchivalBackupArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ArchivalSummary> _TYPE = dafny.TypeDescriptor.<ArchivalSummary>referenceWithInitializer(ArchivalSummary.class, () -> ArchivalSummary.Default());
  public static dafny.TypeDescriptor<ArchivalSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<ArchivalSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ArchivalSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ArchivalSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(BackupArn._typeDescriptor()));
  public static ArchivalSummary Default() {
    return theDefault;
  }
  public static ArchivalSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalReason, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalBackupArn) {
    return new ArchivalSummary(ArchivalDateTime, ArchivalReason, ArchivalBackupArn);
  }
  public static ArchivalSummary create_ArchivalSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalReason, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ArchivalBackupArn) {
    return create(ArchivalDateTime, ArchivalReason, ArchivalBackupArn);
  }
  public boolean is_ArchivalSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ArchivalDateTime() {
    return this._ArchivalDateTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ArchivalReason() {
    return this._ArchivalReason;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ArchivalBackupArn() {
    return this._ArchivalBackupArn;
  }
}
