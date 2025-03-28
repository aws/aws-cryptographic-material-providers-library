// Class DeleteReplicationGroupMemberAction
// Dafny class DeleteReplicationGroupMemberAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteReplicationGroupMemberAction {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public DeleteReplicationGroupMemberAction (dafny.DafnySequence<? extends Character> RegionName) {
    this._RegionName = RegionName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteReplicationGroupMemberAction o = (DeleteReplicationGroupMemberAction)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteReplicationGroupMemberAction.DeleteReplicationGroupMemberAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteReplicationGroupMemberAction> _TYPE = dafny.TypeDescriptor.<DeleteReplicationGroupMemberAction>referenceWithInitializer(DeleteReplicationGroupMemberAction.class, () -> DeleteReplicationGroupMemberAction.Default());
  public static dafny.TypeDescriptor<DeleteReplicationGroupMemberAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteReplicationGroupMemberAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteReplicationGroupMemberAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteReplicationGroupMemberAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteReplicationGroupMemberAction Default() {
    return theDefault;
  }
  public static DeleteReplicationGroupMemberAction create(dafny.DafnySequence<? extends Character> RegionName) {
    return new DeleteReplicationGroupMemberAction(RegionName);
  }
  public static DeleteReplicationGroupMemberAction create_DeleteReplicationGroupMemberAction(dafny.DafnySequence<? extends Character> RegionName) {
    return create(RegionName);
  }
  public boolean is_DeleteReplicationGroupMemberAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
}
