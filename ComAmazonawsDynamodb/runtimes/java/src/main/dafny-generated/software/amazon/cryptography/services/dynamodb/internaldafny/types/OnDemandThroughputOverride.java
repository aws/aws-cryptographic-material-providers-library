// Class OnDemandThroughputOverride
// Dafny class OnDemandThroughputOverride compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class OnDemandThroughputOverride {
  public Wrappers_Compile.Option<java.lang.Long> _MaxReadRequestUnits;
  public OnDemandThroughputOverride (Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits) {
    this._MaxReadRequestUnits = MaxReadRequestUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnDemandThroughputOverride o = (OnDemandThroughputOverride)other;
    return true && java.util.Objects.equals(this._MaxReadRequestUnits, o._MaxReadRequestUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaxReadRequestUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.OnDemandThroughputOverride.OnDemandThroughputOverride");
    s.append("(");
    s.append(dafny.Helpers.toString(this._MaxReadRequestUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnDemandThroughputOverride> _TYPE = dafny.TypeDescriptor.<OnDemandThroughputOverride>referenceWithInitializer(OnDemandThroughputOverride.class, () -> OnDemandThroughputOverride.Default());
  public static dafny.TypeDescriptor<OnDemandThroughputOverride> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDemandThroughputOverride>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnDemandThroughputOverride theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.OnDemandThroughputOverride.create(Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()));
  public static OnDemandThroughputOverride Default() {
    return theDefault;
  }
  public static OnDemandThroughputOverride create(Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits) {
    return new OnDemandThroughputOverride(MaxReadRequestUnits);
  }
  public static OnDemandThroughputOverride create_OnDemandThroughputOverride(Wrappers_Compile.Option<java.lang.Long> MaxReadRequestUnits) {
    return create(MaxReadRequestUnits);
  }
  public boolean is_OnDemandThroughputOverride() { return true; }
  public Wrappers_Compile.Option<java.lang.Long> dtor_MaxReadRequestUnits() {
    return this._MaxReadRequestUnits;
  }
}
