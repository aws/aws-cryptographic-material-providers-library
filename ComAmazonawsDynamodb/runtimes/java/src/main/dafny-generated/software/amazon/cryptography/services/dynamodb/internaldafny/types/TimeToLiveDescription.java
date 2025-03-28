// Class TimeToLiveDescription
// Dafny class TimeToLiveDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TimeToLiveDescription {
  public Wrappers_Compile.Option<TimeToLiveStatus> _TimeToLiveStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AttributeName;
  public TimeToLiveDescription (Wrappers_Compile.Option<TimeToLiveStatus> TimeToLiveStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AttributeName) {
    this._TimeToLiveStatus = TimeToLiveStatus;
    this._AttributeName = AttributeName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeToLiveDescription o = (TimeToLiveDescription)other;
    return true && java.util.Objects.equals(this._TimeToLiveStatus, o._TimeToLiveStatus) && java.util.Objects.equals(this._AttributeName, o._AttributeName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeToLiveStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TimeToLiveDescription.TimeToLiveDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TimeToLiveStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributeName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TimeToLiveDescription> _TYPE = dafny.TypeDescriptor.<TimeToLiveDescription>referenceWithInitializer(TimeToLiveDescription.class, () -> TimeToLiveDescription.Default());
  public static dafny.TypeDescriptor<TimeToLiveDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<TimeToLiveDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TimeToLiveDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveDescription.create(Wrappers_Compile.Option.<TimeToLiveStatus>Default(TimeToLiveStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TimeToLiveAttributeName._typeDescriptor()));
  public static TimeToLiveDescription Default() {
    return theDefault;
  }
  public static TimeToLiveDescription create(Wrappers_Compile.Option<TimeToLiveStatus> TimeToLiveStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AttributeName) {
    return new TimeToLiveDescription(TimeToLiveStatus, AttributeName);
  }
  public static TimeToLiveDescription create_TimeToLiveDescription(Wrappers_Compile.Option<TimeToLiveStatus> TimeToLiveStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AttributeName) {
    return create(TimeToLiveStatus, AttributeName);
  }
  public boolean is_TimeToLiveDescription() { return true; }
  public Wrappers_Compile.Option<TimeToLiveStatus> dtor_TimeToLiveStatus() {
    return this._TimeToLiveStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AttributeName() {
    return this._AttributeName;
  }
}
