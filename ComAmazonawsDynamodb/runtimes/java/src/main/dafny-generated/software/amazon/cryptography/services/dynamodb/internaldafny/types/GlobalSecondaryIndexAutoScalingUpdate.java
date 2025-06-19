// Class GlobalSecondaryIndexAutoScalingUpdate
// Dafny class GlobalSecondaryIndexAutoScalingUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndexAutoScalingUpdate {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ProvisionedWriteCapacityAutoScalingUpdate;
  public GlobalSecondaryIndexAutoScalingUpdate (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate) {
    this._IndexName = IndexName;
    this._ProvisionedWriteCapacityAutoScalingUpdate = ProvisionedWriteCapacityAutoScalingUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalSecondaryIndexAutoScalingUpdate o = (GlobalSecondaryIndexAutoScalingUpdate)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedWriteCapacityAutoScalingUpdate, o._ProvisionedWriteCapacityAutoScalingUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityAutoScalingUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalSecondaryIndexAutoScalingUpdate.GlobalSecondaryIndexAutoScalingUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityAutoScalingUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalSecondaryIndexAutoScalingUpdate> _TYPE = dafny.TypeDescriptor.<GlobalSecondaryIndexAutoScalingUpdate>referenceWithInitializer(GlobalSecondaryIndexAutoScalingUpdate.class, () -> GlobalSecondaryIndexAutoScalingUpdate.Default());
  public static dafny.TypeDescriptor<GlobalSecondaryIndexAutoScalingUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalSecondaryIndexAutoScalingUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalSecondaryIndexAutoScalingUpdate theDefault = GlobalSecondaryIndexAutoScalingUpdate.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()));
  public static GlobalSecondaryIndexAutoScalingUpdate Default() {
    return theDefault;
  }
  public static GlobalSecondaryIndexAutoScalingUpdate create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate) {
    return new GlobalSecondaryIndexAutoScalingUpdate(IndexName, ProvisionedWriteCapacityAutoScalingUpdate);
  }
  public static GlobalSecondaryIndexAutoScalingUpdate create_GlobalSecondaryIndexAutoScalingUpdate(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate) {
    return create(IndexName, ProvisionedWriteCapacityAutoScalingUpdate);
  }
  public boolean is_GlobalSecondaryIndexAutoScalingUpdate() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ProvisionedWriteCapacityAutoScalingUpdate() {
    return this._ProvisionedWriteCapacityAutoScalingUpdate;
  }
}
