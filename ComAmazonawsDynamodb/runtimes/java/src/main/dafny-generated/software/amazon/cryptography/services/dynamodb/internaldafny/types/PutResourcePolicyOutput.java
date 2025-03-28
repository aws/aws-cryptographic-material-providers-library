// Class PutResourcePolicyOutput
// Dafny class PutResourcePolicyOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutResourcePolicyOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RevisionId;
  public PutResourcePolicyOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    this._RevisionId = RevisionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutResourcePolicyOutput o = (PutResourcePolicyOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.PutResourcePolicyOutput.PutResourcePolicyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RevisionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutResourcePolicyOutput> _TYPE = dafny.TypeDescriptor.<PutResourcePolicyOutput>referenceWithInitializer(PutResourcePolicyOutput.class, () -> PutResourcePolicyOutput.Default());
  public static dafny.TypeDescriptor<PutResourcePolicyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutResourcePolicyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutResourcePolicyOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.PutResourcePolicyOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyRevisionId._typeDescriptor()));
  public static PutResourcePolicyOutput Default() {
    return theDefault;
  }
  public static PutResourcePolicyOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return new PutResourcePolicyOutput(RevisionId);
  }
  public static PutResourcePolicyOutput create_PutResourcePolicyOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return create(RevisionId);
  }
  public boolean is_PutResourcePolicyOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RevisionId() {
    return this._RevisionId;
  }
}
