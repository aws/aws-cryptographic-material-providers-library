// Class ReplicationGroupUpdate
// Dafny class ReplicationGroupUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicationGroupUpdate {
  public Wrappers_Compile.Option<CreateReplicationGroupMemberAction> _Create;
  public Wrappers_Compile.Option<UpdateReplicationGroupMemberAction> _Update;
  public Wrappers_Compile.Option<DeleteReplicationGroupMemberAction> _Delete;
  public ReplicationGroupUpdate (Wrappers_Compile.Option<CreateReplicationGroupMemberAction> Create, Wrappers_Compile.Option<UpdateReplicationGroupMemberAction> Update, Wrappers_Compile.Option<DeleteReplicationGroupMemberAction> Delete) {
    this._Create = Create;
    this._Update = Update;
    this._Delete = Delete;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicationGroupUpdate o = (ReplicationGroupUpdate)other;
    return true && java.util.Objects.equals(this._Create, o._Create) && java.util.Objects.equals(this._Update, o._Update) && java.util.Objects.equals(this._Delete, o._Delete);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Create);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Update);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Delete);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicationGroupUpdate.ReplicationGroupUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Create));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Update));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Delete));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicationGroupUpdate> _TYPE = dafny.TypeDescriptor.<ReplicationGroupUpdate>referenceWithInitializer(ReplicationGroupUpdate.class, () -> ReplicationGroupUpdate.Default());
  public static dafny.TypeDescriptor<ReplicationGroupUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicationGroupUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicationGroupUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicationGroupUpdate.create(Wrappers_Compile.Option.<CreateReplicationGroupMemberAction>Default(CreateReplicationGroupMemberAction._typeDescriptor()), Wrappers_Compile.Option.<UpdateReplicationGroupMemberAction>Default(UpdateReplicationGroupMemberAction._typeDescriptor()), Wrappers_Compile.Option.<DeleteReplicationGroupMemberAction>Default(DeleteReplicationGroupMemberAction._typeDescriptor()));
  public static ReplicationGroupUpdate Default() {
    return theDefault;
  }
  public static ReplicationGroupUpdate create(Wrappers_Compile.Option<CreateReplicationGroupMemberAction> Create, Wrappers_Compile.Option<UpdateReplicationGroupMemberAction> Update, Wrappers_Compile.Option<DeleteReplicationGroupMemberAction> Delete) {
    return new ReplicationGroupUpdate(Create, Update, Delete);
  }
  public static ReplicationGroupUpdate create_ReplicationGroupUpdate(Wrappers_Compile.Option<CreateReplicationGroupMemberAction> Create, Wrappers_Compile.Option<UpdateReplicationGroupMemberAction> Update, Wrappers_Compile.Option<DeleteReplicationGroupMemberAction> Delete) {
    return create(Create, Update, Delete);
  }
  public boolean is_ReplicationGroupUpdate() { return true; }
  public Wrappers_Compile.Option<CreateReplicationGroupMemberAction> dtor_Create() {
    return this._Create;
  }
  public Wrappers_Compile.Option<UpdateReplicationGroupMemberAction> dtor_Update() {
    return this._Update;
  }
  public Wrappers_Compile.Option<DeleteReplicationGroupMemberAction> dtor_Delete() {
    return this._Delete;
  }
}
