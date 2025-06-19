// Class CreateGrantRequest
// Dafny class CreateGrantRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateGrantRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Character> _GranteePrincipal;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RetiringPrincipal;
  public dafny.DafnySequence<? extends GrantOperation> _Operations;
  public Wrappers_Compile.Option<GrantConstraints> _Constraints;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Name;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public CreateGrantRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, dafny.DafnySequence<? extends GrantOperation> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._GranteePrincipal = GranteePrincipal;
    this._RetiringPrincipal = RetiringPrincipal;
    this._Operations = Operations;
    this._Constraints = Constraints;
    this._GrantTokens = GrantTokens;
    this._Name = Name;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateGrantRequest o = (CreateGrantRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GranteePrincipal, o._GranteePrincipal) && java.util.Objects.equals(this._RetiringPrincipal, o._RetiringPrincipal) && java.util.Objects.equals(this._Operations, o._Operations) && java.util.Objects.equals(this._Constraints, o._Constraints) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._Name, o._Name) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GranteePrincipal);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RetiringPrincipal);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Operations);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Constraints);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CreateGrantRequest.CreateGrantRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GranteePrincipal));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RetiringPrincipal));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Operations));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Constraints));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateGrantRequest> _TYPE = dafny.TypeDescriptor.<CreateGrantRequest>referenceWithInitializer(CreateGrantRequest.class, () -> CreateGrantRequest.Default());
  public static dafny.TypeDescriptor<CreateGrantRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateGrantRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateGrantRequest theDefault = CreateGrantRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PrincipalIdType._typeDescriptor()), dafny.DafnySequence.<GrantOperation> empty(GrantOperation._typeDescriptor()), Wrappers_Compile.Option.<GrantConstraints>Default(GrantConstraints._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantNameType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static CreateGrantRequest Default() {
    return theDefault;
  }
  public static CreateGrantRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, dafny.DafnySequence<? extends GrantOperation> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<Boolean> DryRun) {
    return new CreateGrantRequest(KeyId, GranteePrincipal, RetiringPrincipal, Operations, Constraints, GrantTokens, Name, DryRun);
  }
  public static CreateGrantRequest create_CreateGrantRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, dafny.DafnySequence<? extends GrantOperation> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, GranteePrincipal, RetiringPrincipal, Operations, Constraints, GrantTokens, Name, DryRun);
  }
  public boolean is_CreateGrantRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_GranteePrincipal() {
    return this._GranteePrincipal;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RetiringPrincipal() {
    return this._RetiringPrincipal;
  }
  public dafny.DafnySequence<? extends GrantOperation> dtor_Operations() {
    return this._Operations;
  }
  public Wrappers_Compile.Option<GrantConstraints> dtor_Constraints() {
    return this._Constraints;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Name() {
    return this._Name;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
