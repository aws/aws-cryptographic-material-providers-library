// Class DeleteGlobalSecondaryIndexAction
// Dafny class DeleteGlobalSecondaryIndexAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteGlobalSecondaryIndexAction {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public DeleteGlobalSecondaryIndexAction (dafny.DafnySequence<? extends Character> IndexName) {
    this._IndexName = IndexName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteGlobalSecondaryIndexAction o = (DeleteGlobalSecondaryIndexAction)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteGlobalSecondaryIndexAction.DeleteGlobalSecondaryIndexAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteGlobalSecondaryIndexAction> _TYPE = dafny.TypeDescriptor.<DeleteGlobalSecondaryIndexAction>referenceWithInitializer(DeleteGlobalSecondaryIndexAction.class, () -> DeleteGlobalSecondaryIndexAction.Default());
  public static dafny.TypeDescriptor<DeleteGlobalSecondaryIndexAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteGlobalSecondaryIndexAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteGlobalSecondaryIndexAction theDefault = DeleteGlobalSecondaryIndexAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteGlobalSecondaryIndexAction Default() {
    return theDefault;
  }
  public static DeleteGlobalSecondaryIndexAction create(dafny.DafnySequence<? extends Character> IndexName) {
    return new DeleteGlobalSecondaryIndexAction(IndexName);
  }
  public static DeleteGlobalSecondaryIndexAction create_DeleteGlobalSecondaryIndexAction(dafny.DafnySequence<? extends Character> IndexName) {
    return create(IndexName);
  }
  public boolean is_DeleteGlobalSecondaryIndexAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
}
