// Class PointInTimeRecoverySpecification
// Dafny class PointInTimeRecoverySpecification compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PointInTimeRecoverySpecification {
  public boolean _PointInTimeRecoveryEnabled;
  public PointInTimeRecoverySpecification (boolean PointInTimeRecoveryEnabled) {
    this._PointInTimeRecoveryEnabled = PointInTimeRecoveryEnabled;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PointInTimeRecoverySpecification o = (PointInTimeRecoverySpecification)other;
    return true && this._PointInTimeRecoveryEnabled == o._PointInTimeRecoveryEnabled;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._PointInTimeRecoveryEnabled);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.PointInTimeRecoverySpecification.PointInTimeRecoverySpecification");
    s.append("(");
    s.append(this._PointInTimeRecoveryEnabled);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PointInTimeRecoverySpecification> _TYPE = dafny.TypeDescriptor.<PointInTimeRecoverySpecification>referenceWithInitializer(PointInTimeRecoverySpecification.class, () -> PointInTimeRecoverySpecification.Default());
  public static dafny.TypeDescriptor<PointInTimeRecoverySpecification> _typeDescriptor() {
    return (dafny.TypeDescriptor<PointInTimeRecoverySpecification>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PointInTimeRecoverySpecification theDefault = PointInTimeRecoverySpecification.create(false);
  public static PointInTimeRecoverySpecification Default() {
    return theDefault;
  }
  public static PointInTimeRecoverySpecification create(boolean PointInTimeRecoveryEnabled) {
    return new PointInTimeRecoverySpecification(PointInTimeRecoveryEnabled);
  }
  public static PointInTimeRecoverySpecification create_PointInTimeRecoverySpecification(boolean PointInTimeRecoveryEnabled) {
    return create(PointInTimeRecoveryEnabled);
  }
  public boolean is_PointInTimeRecoverySpecification() { return true; }
  public boolean dtor_PointInTimeRecoveryEnabled() {
    return this._PointInTimeRecoveryEnabled;
  }
}
