// Class DeleteReplicaAction
// Dafny class DeleteReplicaAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteReplicaAction {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public DeleteReplicaAction (dafny.DafnySequence<? extends Character> RegionName) {
    this._RegionName = RegionName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteReplicaAction o = (DeleteReplicaAction)other;
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
    s.append("ComAmazonawsDynamodbTypes.DeleteReplicaAction.DeleteReplicaAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteReplicaAction> _TYPE = dafny.TypeDescriptor.<DeleteReplicaAction>referenceWithInitializer(DeleteReplicaAction.class, () -> DeleteReplicaAction.Default());
  public static dafny.TypeDescriptor<DeleteReplicaAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteReplicaAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteReplicaAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteReplicaAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteReplicaAction Default() {
    return theDefault;
  }
  public static DeleteReplicaAction create(dafny.DafnySequence<? extends Character> RegionName) {
    return new DeleteReplicaAction(RegionName);
  }
  public static DeleteReplicaAction create_DeleteReplicaAction(dafny.DafnySequence<? extends Character> RegionName) {
    return create(RegionName);
  }
  public boolean is_DeleteReplicaAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
}
