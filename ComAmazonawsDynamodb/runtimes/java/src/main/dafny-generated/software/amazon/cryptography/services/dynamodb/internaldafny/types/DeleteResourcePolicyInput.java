// Class DeleteResourcePolicyInput
// Dafny class DeleteResourcePolicyInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteResourcePolicyInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExpectedRevisionId;
  public DeleteResourcePolicyInput (dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId) {
    this._ResourceArn = ResourceArn;
    this._ExpectedRevisionId = ExpectedRevisionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteResourcePolicyInput o = (DeleteResourcePolicyInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn) && java.util.Objects.equals(this._ExpectedRevisionId, o._ExpectedRevisionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpectedRevisionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteResourcePolicyInput.DeleteResourcePolicyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpectedRevisionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteResourcePolicyInput> _TYPE = dafny.TypeDescriptor.<DeleteResourcePolicyInput>referenceWithInitializer(DeleteResourcePolicyInput.class, () -> DeleteResourcePolicyInput.Default());
  public static dafny.TypeDescriptor<DeleteResourcePolicyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteResourcePolicyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteResourcePolicyInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteResourcePolicyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyRevisionId._typeDescriptor()));
  public static DeleteResourcePolicyInput Default() {
    return theDefault;
  }
  public static DeleteResourcePolicyInput create(dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId) {
    return new DeleteResourcePolicyInput(ResourceArn, ExpectedRevisionId);
  }
  public static DeleteResourcePolicyInput create_DeleteResourcePolicyInput(dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId) {
    return create(ResourceArn, ExpectedRevisionId);
  }
  public boolean is_DeleteResourcePolicyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExpectedRevisionId() {
    return this._ExpectedRevisionId;
  }
}
