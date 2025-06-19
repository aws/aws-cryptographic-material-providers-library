// Class TimeToLiveSpecification
// Dafny class TimeToLiveSpecification compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TimeToLiveSpecification {
  public boolean _Enabled;
  public dafny.DafnySequence<? extends Character> _AttributeName;
  public TimeToLiveSpecification (boolean Enabled, dafny.DafnySequence<? extends Character> AttributeName) {
    this._Enabled = Enabled;
    this._AttributeName = AttributeName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeToLiveSpecification o = (TimeToLiveSpecification)other;
    return true && this._Enabled == o._Enabled && java.util.Objects.equals(this._AttributeName, o._AttributeName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._Enabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TimeToLiveSpecification.TimeToLiveSpecification");
    s.append("(");
    s.append(this._Enabled);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributeName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TimeToLiveSpecification> _TYPE = dafny.TypeDescriptor.<TimeToLiveSpecification>referenceWithInitializer(TimeToLiveSpecification.class, () -> TimeToLiveSpecification.Default());
  public static dafny.TypeDescriptor<TimeToLiveSpecification> _typeDescriptor() {
    return (dafny.TypeDescriptor<TimeToLiveSpecification>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TimeToLiveSpecification theDefault = TimeToLiveSpecification.create(false, dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static TimeToLiveSpecification Default() {
    return theDefault;
  }
  public static TimeToLiveSpecification create(boolean Enabled, dafny.DafnySequence<? extends Character> AttributeName) {
    return new TimeToLiveSpecification(Enabled, AttributeName);
  }
  public static TimeToLiveSpecification create_TimeToLiveSpecification(boolean Enabled, dafny.DafnySequence<? extends Character> AttributeName) {
    return create(Enabled, AttributeName);
  }
  public boolean is_TimeToLiveSpecification() { return true; }
  public boolean dtor_Enabled() {
    return this._Enabled;
  }
  public dafny.DafnySequence<? extends Character> dtor_AttributeName() {
    return this._AttributeName;
  }
}
