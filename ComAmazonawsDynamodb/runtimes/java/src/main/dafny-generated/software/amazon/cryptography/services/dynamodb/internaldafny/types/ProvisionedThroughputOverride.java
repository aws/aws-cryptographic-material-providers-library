// Class ProvisionedThroughputOverride
// Dafny class ProvisionedThroughputOverride compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ProvisionedThroughputOverride {
  public Wrappers_Compile.Option<java.lang.Long> _ReadCapacityUnits;
  public ProvisionedThroughputOverride (Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits) {
    this._ReadCapacityUnits = ReadCapacityUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ProvisionedThroughputOverride o = (ProvisionedThroughputOverride)other;
    return true && java.util.Objects.equals(this._ReadCapacityUnits, o._ReadCapacityUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReadCapacityUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ProvisionedThroughputOverride.ProvisionedThroughputOverride");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ReadCapacityUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ProvisionedThroughputOverride> _TYPE = dafny.TypeDescriptor.<ProvisionedThroughputOverride>referenceWithInitializer(ProvisionedThroughputOverride.class, () -> ProvisionedThroughputOverride.Default());
  public static dafny.TypeDescriptor<ProvisionedThroughputOverride> _typeDescriptor() {
    return (dafny.TypeDescriptor<ProvisionedThroughputOverride>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ProvisionedThroughputOverride theDefault = ProvisionedThroughputOverride.create(Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()));
  public static ProvisionedThroughputOverride Default() {
    return theDefault;
  }
  public static ProvisionedThroughputOverride create(Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits) {
    return new ProvisionedThroughputOverride(ReadCapacityUnits);
  }
  public static ProvisionedThroughputOverride create_ProvisionedThroughputOverride(Wrappers_Compile.Option<java.lang.Long> ReadCapacityUnits) {
    return create(ReadCapacityUnits);
  }
  public boolean is_ProvisionedThroughputOverride() { return true; }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ReadCapacityUnits() {
    return this._ReadCapacityUnits;
  }
}
