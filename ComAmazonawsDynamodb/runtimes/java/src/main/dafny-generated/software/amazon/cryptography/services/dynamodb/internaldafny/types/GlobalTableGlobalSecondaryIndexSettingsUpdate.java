// Class GlobalTableGlobalSecondaryIndexSettingsUpdate
// Dafny class GlobalTableGlobalSecondaryIndexSettingsUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTableGlobalSecondaryIndexSettingsUpdate {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public Wrappers_Compile.Option<java.lang.Long> _ProvisionedWriteCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ProvisionedWriteCapacityAutoScalingSettingsUpdate;
  public GlobalTableGlobalSecondaryIndexSettingsUpdate (dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingSettingsUpdate) {
    this._IndexName = IndexName;
    this._ProvisionedWriteCapacityUnits = ProvisionedWriteCapacityUnits;
    this._ProvisionedWriteCapacityAutoScalingSettingsUpdate = ProvisionedWriteCapacityAutoScalingSettingsUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalTableGlobalSecondaryIndexSettingsUpdate o = (GlobalTableGlobalSecondaryIndexSettingsUpdate)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedWriteCapacityUnits, o._ProvisionedWriteCapacityUnits) && java.util.Objects.equals(this._ProvisionedWriteCapacityAutoScalingSettingsUpdate, o._ProvisionedWriteCapacityAutoScalingSettingsUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityAutoScalingSettingsUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalTableGlobalSecondaryIndexSettingsUpdate.GlobalTableGlobalSecondaryIndexSettingsUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityAutoScalingSettingsUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalTableGlobalSecondaryIndexSettingsUpdate> _TYPE = dafny.TypeDescriptor.<GlobalTableGlobalSecondaryIndexSettingsUpdate>referenceWithInitializer(GlobalTableGlobalSecondaryIndexSettingsUpdate.class, () -> GlobalTableGlobalSecondaryIndexSettingsUpdate.Default());
  public static dafny.TypeDescriptor<GlobalTableGlobalSecondaryIndexSettingsUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalTableGlobalSecondaryIndexSettingsUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalTableGlobalSecondaryIndexSettingsUpdate theDefault = GlobalTableGlobalSecondaryIndexSettingsUpdate.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()));
  public static GlobalTableGlobalSecondaryIndexSettingsUpdate Default() {
    return theDefault;
  }
  public static GlobalTableGlobalSecondaryIndexSettingsUpdate create(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingSettingsUpdate) {
    return new GlobalTableGlobalSecondaryIndexSettingsUpdate(IndexName, ProvisionedWriteCapacityUnits, ProvisionedWriteCapacityAutoScalingSettingsUpdate);
  }
  public static GlobalTableGlobalSecondaryIndexSettingsUpdate create_GlobalTableGlobalSecondaryIndexSettingsUpdate(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingSettingsUpdate) {
    return create(IndexName, ProvisionedWriteCapacityUnits, ProvisionedWriteCapacityAutoScalingSettingsUpdate);
  }
  public boolean is_GlobalTableGlobalSecondaryIndexSettingsUpdate() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProvisionedWriteCapacityUnits() {
    return this._ProvisionedWriteCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ProvisionedWriteCapacityAutoScalingSettingsUpdate() {
    return this._ProvisionedWriteCapacityAutoScalingSettingsUpdate;
  }
}
