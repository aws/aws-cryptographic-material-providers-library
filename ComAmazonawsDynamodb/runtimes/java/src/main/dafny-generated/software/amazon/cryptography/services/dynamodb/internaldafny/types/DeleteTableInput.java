// Class DeleteTableInput
// Dafny class DeleteTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteTableInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DeleteTableInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteTableInput o = (DeleteTableInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteTableInput.DeleteTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteTableInput> _TYPE = dafny.TypeDescriptor.<DeleteTableInput>referenceWithInitializer(DeleteTableInput.class, () -> DeleteTableInput.Default());
  public static dafny.TypeDescriptor<DeleteTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteTableInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteTableInput Default() {
    return theDefault;
  }
  public static DeleteTableInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DeleteTableInput(TableName);
  }
  public static DeleteTableInput create_DeleteTableInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DeleteTableInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
