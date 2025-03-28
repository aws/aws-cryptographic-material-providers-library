// Class ReplicaUpdate
// Dafny class ReplicaUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaUpdate {
  public Wrappers_Compile.Option<CreateReplicaAction> _Create;
  public Wrappers_Compile.Option<DeleteReplicaAction> _Delete;
  public ReplicaUpdate (Wrappers_Compile.Option<CreateReplicaAction> Create, Wrappers_Compile.Option<DeleteReplicaAction> Delete) {
    this._Create = Create;
    this._Delete = Delete;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaUpdate o = (ReplicaUpdate)other;
    return true && java.util.Objects.equals(this._Create, o._Create) && java.util.Objects.equals(this._Delete, o._Delete);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Create);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Delete);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaUpdate.ReplicaUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Create));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Delete));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaUpdate> _TYPE = dafny.TypeDescriptor.<ReplicaUpdate>referenceWithInitializer(ReplicaUpdate.class, () -> ReplicaUpdate.Default());
  public static dafny.TypeDescriptor<ReplicaUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaUpdate.create(Wrappers_Compile.Option.<CreateReplicaAction>Default(CreateReplicaAction._typeDescriptor()), Wrappers_Compile.Option.<DeleteReplicaAction>Default(DeleteReplicaAction._typeDescriptor()));
  public static ReplicaUpdate Default() {
    return theDefault;
  }
  public static ReplicaUpdate create(Wrappers_Compile.Option<CreateReplicaAction> Create, Wrappers_Compile.Option<DeleteReplicaAction> Delete) {
    return new ReplicaUpdate(Create, Delete);
  }
  public static ReplicaUpdate create_ReplicaUpdate(Wrappers_Compile.Option<CreateReplicaAction> Create, Wrappers_Compile.Option<DeleteReplicaAction> Delete) {
    return create(Create, Delete);
  }
  public boolean is_ReplicaUpdate() { return true; }
  public Wrappers_Compile.Option<CreateReplicaAction> dtor_Create() {
    return this._Create;
  }
  public Wrappers_Compile.Option<DeleteReplicaAction> dtor_Delete() {
    return this._Delete;
  }
}
