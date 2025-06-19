// Class PutResourcePolicyInput
// Dafny class PutResourcePolicyInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PutResourcePolicyInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public dafny.DafnySequence<? extends Character> _Policy;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExpectedRevisionId;
  public Wrappers_Compile.Option<Boolean> _ConfirmRemoveSelfResourceAccess;
  public PutResourcePolicyInput (dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId, Wrappers_Compile.Option<Boolean> ConfirmRemoveSelfResourceAccess) {
    this._ResourceArn = ResourceArn;
    this._Policy = Policy;
    this._ExpectedRevisionId = ExpectedRevisionId;
    this._ConfirmRemoveSelfResourceAccess = ConfirmRemoveSelfResourceAccess;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutResourcePolicyInput o = (PutResourcePolicyInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn) && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._ExpectedRevisionId, o._ExpectedRevisionId) && java.util.Objects.equals(this._ConfirmRemoveSelfResourceAccess, o._ConfirmRemoveSelfResourceAccess);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpectedRevisionId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConfirmRemoveSelfResourceAccess);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.PutResourcePolicyInput.PutResourcePolicyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpectedRevisionId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConfirmRemoveSelfResourceAccess));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutResourcePolicyInput> _TYPE = dafny.TypeDescriptor.<PutResourcePolicyInput>referenceWithInitializer(PutResourcePolicyInput.class, () -> PutResourcePolicyInput.Default());
  public static dafny.TypeDescriptor<PutResourcePolicyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutResourcePolicyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutResourcePolicyInput theDefault = PutResourcePolicyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyRevisionId._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static PutResourcePolicyInput Default() {
    return theDefault;
  }
  public static PutResourcePolicyInput create(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId, Wrappers_Compile.Option<Boolean> ConfirmRemoveSelfResourceAccess) {
    return new PutResourcePolicyInput(ResourceArn, Policy, ExpectedRevisionId, ConfirmRemoveSelfResourceAccess);
  }
  public static PutResourcePolicyInput create_PutResourcePolicyInput(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExpectedRevisionId, Wrappers_Compile.Option<Boolean> ConfirmRemoveSelfResourceAccess) {
    return create(ResourceArn, Policy, ExpectedRevisionId, ConfirmRemoveSelfResourceAccess);
  }
  public boolean is_PutResourcePolicyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
  public dafny.DafnySequence<? extends Character> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExpectedRevisionId() {
    return this._ExpectedRevisionId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConfirmRemoveSelfResourceAccess() {
    return this._ConfirmRemoveSelfResourceAccess;
  }
}
