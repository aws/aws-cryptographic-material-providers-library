// Class GrantListEntry
// Dafny class GrantListEntry compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GrantListEntry {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Name;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GranteePrincipal;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RetiringPrincipal;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IssuingAccount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantOperation>> _Operations;
  public Wrappers_Compile.Option<GrantConstraints> _Constraints;
  public GrantListEntry (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IssuingAccount, Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantOperation>> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints) {
    this._KeyId = KeyId;
    this._GrantId = GrantId;
    this._Name = Name;
    this._CreationDate = CreationDate;
    this._GranteePrincipal = GranteePrincipal;
    this._RetiringPrincipal = RetiringPrincipal;
    this._IssuingAccount = IssuingAccount;
    this._Operations = Operations;
    this._Constraints = Constraints;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantListEntry o = (GrantListEntry)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantId, o._GrantId) && java.util.Objects.equals(this._Name, o._Name) && java.util.Objects.equals(this._CreationDate, o._CreationDate) && java.util.Objects.equals(this._GranteePrincipal, o._GranteePrincipal) && java.util.Objects.equals(this._RetiringPrincipal, o._RetiringPrincipal) && java.util.Objects.equals(this._IssuingAccount, o._IssuingAccount) && java.util.Objects.equals(this._Operations, o._Operations) && java.util.Objects.equals(this._Constraints, o._Constraints);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GranteePrincipal);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RetiringPrincipal);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IssuingAccount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Operations);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Constraints);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantListEntry.GrantListEntry");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GranteePrincipal));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RetiringPrincipal));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IssuingAccount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Operations));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Constraints));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GrantListEntry> _TYPE = dafny.TypeDescriptor.<GrantListEntry>referenceWithInitializer(GrantListEntry.class, () -> GrantListEntry.Default());
  public static dafny.TypeDescriptor<GrantListEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<GrantListEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GrantListEntry theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GrantListEntry.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantNameType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PrincipalIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PrincipalIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PrincipalIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GrantOperation>>Default(dafny.DafnySequence.<GrantOperation>_typeDescriptor(GrantOperation._typeDescriptor())), Wrappers_Compile.Option.<GrantConstraints>Default(GrantConstraints._typeDescriptor()));
  public static GrantListEntry Default() {
    return theDefault;
  }
  public static GrantListEntry create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IssuingAccount, Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantOperation>> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints) {
    return new GrantListEntry(KeyId, GrantId, Name, CreationDate, GranteePrincipal, RetiringPrincipal, IssuingAccount, Operations, Constraints);
  }
  public static GrantListEntry create_GrantListEntry(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RetiringPrincipal, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IssuingAccount, Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantOperation>> Operations, Wrappers_Compile.Option<GrantConstraints> Constraints) {
    return create(KeyId, GrantId, Name, CreationDate, GranteePrincipal, RetiringPrincipal, IssuingAccount, Operations, Constraints);
  }
  public boolean is_GrantListEntry() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantId() {
    return this._GrantId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Name() {
    return this._Name;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDate() {
    return this._CreationDate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GranteePrincipal() {
    return this._GranteePrincipal;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RetiringPrincipal() {
    return this._RetiringPrincipal;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IssuingAccount() {
    return this._IssuingAccount;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantOperation>> dtor_Operations() {
    return this._Operations;
  }
  public Wrappers_Compile.Option<GrantConstraints> dtor_Constraints() {
    return this._Constraints;
  }
}
