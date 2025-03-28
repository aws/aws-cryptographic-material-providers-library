// Class GetResourcePolicyOutput
// Dafny class GetResourcePolicyOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetResourcePolicyOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Policy;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RevisionId;
  public GetResourcePolicyOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    this._Policy = Policy;
    this._RevisionId = RevisionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetResourcePolicyOutput o = (GetResourcePolicyOutput)other;
    return true && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._RevisionId, o._RevisionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RevisionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GetResourcePolicyOutput.GetResourcePolicyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RevisionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetResourcePolicyOutput> _TYPE = dafny.TypeDescriptor.<GetResourcePolicyOutput>referenceWithInitializer(GetResourcePolicyOutput.class, () -> GetResourcePolicyOutput.Default());
  public static dafny.TypeDescriptor<GetResourcePolicyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetResourcePolicyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetResourcePolicyOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GetResourcePolicyOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyRevisionId._typeDescriptor()));
  public static GetResourcePolicyOutput Default() {
    return theDefault;
  }
  public static GetResourcePolicyOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return new GetResourcePolicyOutput(Policy, RevisionId);
  }
  public static GetResourcePolicyOutput create_GetResourcePolicyOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RevisionId) {
    return create(Policy, RevisionId);
  }
  public boolean is_GetResourcePolicyOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RevisionId() {
    return this._RevisionId;
  }
}
