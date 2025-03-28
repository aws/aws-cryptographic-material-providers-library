// Class UpdateGlobalSecondaryIndexAction
// Dafny class UpdateGlobalSecondaryIndexAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateGlobalSecondaryIndexAction {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public UpdateGlobalSecondaryIndexAction (dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._IndexName = IndexName;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateGlobalSecondaryIndexAction o = (UpdateGlobalSecondaryIndexAction)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateGlobalSecondaryIndexAction.UpdateGlobalSecondaryIndexAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateGlobalSecondaryIndexAction> _TYPE = dafny.TypeDescriptor.<UpdateGlobalSecondaryIndexAction>referenceWithInitializer(UpdateGlobalSecondaryIndexAction.class, () -> UpdateGlobalSecondaryIndexAction.Default());
  public static dafny.TypeDescriptor<UpdateGlobalSecondaryIndexAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateGlobalSecondaryIndexAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateGlobalSecondaryIndexAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalSecondaryIndexAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static UpdateGlobalSecondaryIndexAction Default() {
    return theDefault;
  }
  public static UpdateGlobalSecondaryIndexAction create(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new UpdateGlobalSecondaryIndexAction(IndexName, ProvisionedThroughput, OnDemandThroughput);
  }
  public static UpdateGlobalSecondaryIndexAction create_UpdateGlobalSecondaryIndexAction(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(IndexName, ProvisionedThroughput, OnDemandThroughput);
  }
  public boolean is_UpdateGlobalSecondaryIndexAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
