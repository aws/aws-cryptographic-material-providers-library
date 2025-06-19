// Class PointInTimeRecoveryDescription
// Dafny class PointInTimeRecoveryDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PointInTimeRecoveryDescription {
  public Wrappers_Compile.Option<PointInTimeRecoveryStatus> _PointInTimeRecoveryStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _EarliestRestorableDateTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LatestRestorableDateTime;
  public PointInTimeRecoveryDescription (Wrappers_Compile.Option<PointInTimeRecoveryStatus> PointInTimeRecoveryStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EarliestRestorableDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestRestorableDateTime) {
    this._PointInTimeRecoveryStatus = PointInTimeRecoveryStatus;
    this._EarliestRestorableDateTime = EarliestRestorableDateTime;
    this._LatestRestorableDateTime = LatestRestorableDateTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PointInTimeRecoveryDescription o = (PointInTimeRecoveryDescription)other;
    return true && java.util.Objects.equals(this._PointInTimeRecoveryStatus, o._PointInTimeRecoveryStatus) && java.util.Objects.equals(this._EarliestRestorableDateTime, o._EarliestRestorableDateTime) && java.util.Objects.equals(this._LatestRestorableDateTime, o._LatestRestorableDateTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PointInTimeRecoveryStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EarliestRestorableDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LatestRestorableDateTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.PointInTimeRecoveryDescription.PointInTimeRecoveryDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PointInTimeRecoveryStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EarliestRestorableDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LatestRestorableDateTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PointInTimeRecoveryDescription> _TYPE = dafny.TypeDescriptor.<PointInTimeRecoveryDescription>referenceWithInitializer(PointInTimeRecoveryDescription.class, () -> PointInTimeRecoveryDescription.Default());
  public static dafny.TypeDescriptor<PointInTimeRecoveryDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<PointInTimeRecoveryDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PointInTimeRecoveryDescription theDefault = PointInTimeRecoveryDescription.create(Wrappers_Compile.Option.<PointInTimeRecoveryStatus>Default(PointInTimeRecoveryStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static PointInTimeRecoveryDescription Default() {
    return theDefault;
  }
  public static PointInTimeRecoveryDescription create(Wrappers_Compile.Option<PointInTimeRecoveryStatus> PointInTimeRecoveryStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EarliestRestorableDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestRestorableDateTime) {
    return new PointInTimeRecoveryDescription(PointInTimeRecoveryStatus, EarliestRestorableDateTime, LatestRestorableDateTime);
  }
  public static PointInTimeRecoveryDescription create_PointInTimeRecoveryDescription(Wrappers_Compile.Option<PointInTimeRecoveryStatus> PointInTimeRecoveryStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EarliestRestorableDateTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestRestorableDateTime) {
    return create(PointInTimeRecoveryStatus, EarliestRestorableDateTime, LatestRestorableDateTime);
  }
  public boolean is_PointInTimeRecoveryDescription() { return true; }
  public Wrappers_Compile.Option<PointInTimeRecoveryStatus> dtor_PointInTimeRecoveryStatus() {
    return this._PointInTimeRecoveryStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_EarliestRestorableDateTime() {
    return this._EarliestRestorableDateTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LatestRestorableDateTime() {
    return this._LatestRestorableDateTime;
  }
}
