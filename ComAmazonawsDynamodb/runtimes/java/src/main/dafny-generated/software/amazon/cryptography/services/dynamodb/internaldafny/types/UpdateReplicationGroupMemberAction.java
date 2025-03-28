// Class UpdateReplicationGroupMemberAction
// Dafny class UpdateReplicationGroupMemberAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateReplicationGroupMemberAction {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KMSMasterKeyId;
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> _ProvisionedThroughputOverride;
  public Wrappers_Compile.Option<OnDemandThroughputOverride> _OnDemandThroughputOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<TableClass> _TableClassOverride;
  public UpdateReplicationGroupMemberAction (dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<TableClass> TableClassOverride) {
    this._RegionName = RegionName;
    this._KMSMasterKeyId = KMSMasterKeyId;
    this._ProvisionedThroughputOverride = ProvisionedThroughputOverride;
    this._OnDemandThroughputOverride = OnDemandThroughputOverride;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._TableClassOverride = TableClassOverride;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateReplicationGroupMemberAction o = (UpdateReplicationGroupMemberAction)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._KMSMasterKeyId, o._KMSMasterKeyId) && java.util.Objects.equals(this._ProvisionedThroughputOverride, o._ProvisionedThroughputOverride) && java.util.Objects.equals(this._OnDemandThroughputOverride, o._OnDemandThroughputOverride) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._TableClassOverride, o._TableClassOverride);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KMSMasterKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableClassOverride);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateReplicationGroupMemberAction.UpdateReplicationGroupMemberAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KMSMasterKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableClassOverride));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateReplicationGroupMemberAction> _TYPE = dafny.TypeDescriptor.<UpdateReplicationGroupMemberAction>referenceWithInitializer(UpdateReplicationGroupMemberAction.class, () -> UpdateReplicationGroupMemberAction.Default());
  public static dafny.TypeDescriptor<UpdateReplicationGroupMemberAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateReplicationGroupMemberAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateReplicationGroupMemberAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateReplicationGroupMemberAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ProvisionedThroughputOverride>Default(ProvisionedThroughputOverride._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughputOverride>Default(OnDemandThroughputOverride._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>>Default(ReplicaGlobalSecondaryIndexList._typeDescriptor()), Wrappers_Compile.Option.<TableClass>Default(TableClass._typeDescriptor()));
  public static UpdateReplicationGroupMemberAction Default() {
    return theDefault;
  }
  public static UpdateReplicationGroupMemberAction create(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<TableClass> TableClassOverride) {
    return new UpdateReplicationGroupMemberAction(RegionName, KMSMasterKeyId, ProvisionedThroughputOverride, OnDemandThroughputOverride, GlobalSecondaryIndexes, TableClassOverride);
  }
  public static UpdateReplicationGroupMemberAction create_UpdateReplicationGroupMemberAction(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<TableClass> TableClassOverride) {
    return create(RegionName, KMSMasterKeyId, ProvisionedThroughputOverride, OnDemandThroughputOverride, GlobalSecondaryIndexes, TableClassOverride);
  }
  public boolean is_UpdateReplicationGroupMemberAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KMSMasterKeyId() {
    return this._KMSMasterKeyId;
  }
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> dtor_ProvisionedThroughputOverride() {
    return this._ProvisionedThroughputOverride;
  }
  public Wrappers_Compile.Option<OnDemandThroughputOverride> dtor_OnDemandThroughputOverride() {
    return this._OnDemandThroughputOverride;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndex>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<TableClass> dtor_TableClassOverride() {
    return this._TableClassOverride;
  }
}
