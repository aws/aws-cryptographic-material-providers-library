// Class GrantConstraints
// Dafny class GrantConstraints compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GrantConstraints {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContextSubset;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContextEquals;
  public GrantConstraints (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextSubset, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextEquals) {
    this._EncryptionContextSubset = EncryptionContextSubset;
    this._EncryptionContextEquals = EncryptionContextEquals;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GrantConstraints o = (GrantConstraints)other;
    return true && java.util.Objects.equals(this._EncryptionContextSubset, o._EncryptionContextSubset) && java.util.Objects.equals(this._EncryptionContextEquals, o._EncryptionContextEquals);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContextSubset);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContextEquals);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GrantConstraints.GrantConstraints");
    s.append("(");
    s.append(dafny.Helpers.toString(this._EncryptionContextSubset));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionContextEquals));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GrantConstraints> _TYPE = dafny.TypeDescriptor.<GrantConstraints>referenceWithInitializer(GrantConstraints.class, () -> GrantConstraints.Default());
  public static dafny.TypeDescriptor<GrantConstraints> _typeDescriptor() {
    return (dafny.TypeDescriptor<GrantConstraints>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GrantConstraints theDefault = GrantConstraints.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static GrantConstraints Default() {
    return theDefault;
  }
  public static GrantConstraints create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextSubset, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextEquals) {
    return new GrantConstraints(EncryptionContextSubset, EncryptionContextEquals);
  }
  public static GrantConstraints create_GrantConstraints(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextSubset, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContextEquals) {
    return create(EncryptionContextSubset, EncryptionContextEquals);
  }
  public boolean is_GrantConstraints() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContextSubset() {
    return this._EncryptionContextSubset;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContextEquals() {
    return this._EncryptionContextEquals;
  }
}
