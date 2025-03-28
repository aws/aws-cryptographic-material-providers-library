// Class ReplicaGlobalSecondaryIndexDescription
// Dafny class ReplicaGlobalSecondaryIndexDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> _ProvisionedThroughputOverride;
  public Wrappers_Compile.Option<OnDemandThroughputOverride> _OnDemandThroughputOverride;
  public ReplicaGlobalSecondaryIndexDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride) {
    this._IndexName = IndexName;
    this._ProvisionedThroughputOverride = ProvisionedThroughputOverride;
    this._OnDemandThroughputOverride = OnDemandThroughputOverride;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaGlobalSecondaryIndexDescription o = (ReplicaGlobalSecondaryIndexDescription)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedThroughputOverride, o._ProvisionedThroughputOverride) && java.util.Objects.equals(this._OnDemandThroughputOverride, o._OnDemandThroughputOverride);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughputOverride);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexDescription.ReplicaGlobalSecondaryIndexDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughputOverride));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexDescription> _TYPE = dafny.TypeDescriptor.<ReplicaGlobalSecondaryIndexDescription>referenceWithInitializer(ReplicaGlobalSecondaryIndexDescription.class, () -> ReplicaGlobalSecondaryIndexDescription.Default());
  public static dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaGlobalSecondaryIndexDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<ProvisionedThroughputOverride>Default(ProvisionedThroughputOverride._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughputOverride>Default(OnDemandThroughputOverride._typeDescriptor()));
  public static ReplicaGlobalSecondaryIndexDescription Default() {
    return theDefault;
  }
  public static ReplicaGlobalSecondaryIndexDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride) {
    return new ReplicaGlobalSecondaryIndexDescription(IndexName, ProvisionedThroughputOverride, OnDemandThroughputOverride);
  }
  public static ReplicaGlobalSecondaryIndexDescription create_ReplicaGlobalSecondaryIndexDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride) {
    return create(IndexName, ProvisionedThroughputOverride, OnDemandThroughputOverride);
  }
  public boolean is_ReplicaGlobalSecondaryIndexDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> dtor_ProvisionedThroughputOverride() {
    return this._ProvisionedThroughputOverride;
  }
  public Wrappers_Compile.Option<OnDemandThroughputOverride> dtor_OnDemandThroughputOverride() {
    return this._OnDemandThroughputOverride;
  }
}
