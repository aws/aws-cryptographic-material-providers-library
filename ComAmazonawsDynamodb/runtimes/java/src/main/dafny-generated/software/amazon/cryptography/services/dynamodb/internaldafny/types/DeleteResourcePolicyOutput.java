// Class DeleteResourcePolicyOutput
// Dafny class DeleteResourcePolicyOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteResourcePolicyOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RevisionId;
  public DeleteResourcePolicyOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    this._RevisionId = RevisionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteResourcePolicyOutput o = (DeleteResourcePolicyOutput)other;
    return true && java.util.Objects.equals(this._RevisionId, o._RevisionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RevisionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteResourcePolicyOutput.DeleteResourcePolicyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RevisionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteResourcePolicyOutput> _TYPE = dafny.TypeDescriptor.<DeleteResourcePolicyOutput>referenceWithInitializer(DeleteResourcePolicyOutput.class, () -> DeleteResourcePolicyOutput.Default());
  public static dafny.TypeDescriptor<DeleteResourcePolicyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteResourcePolicyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteResourcePolicyOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteResourcePolicyOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyRevisionId._typeDescriptor()));
  public static DeleteResourcePolicyOutput Default() {
    return theDefault;
  }
  public static DeleteResourcePolicyOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return new DeleteResourcePolicyOutput(RevisionId);
  }
  public static DeleteResourcePolicyOutput create_DeleteResourcePolicyOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return create(RevisionId);
  }
  public boolean is_DeleteResourcePolicyOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RevisionId() {
    return this._RevisionId;
  }
}
