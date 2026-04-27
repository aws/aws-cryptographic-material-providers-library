// Class RotationsListEntry
// Dafny class RotationsListEntry compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RotationsListEntry {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RotationDate;
  public Wrappers_Compile.Option<RotationType> _RotationType;
  public RotationsListEntry (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RotationDate, Wrappers_Compile.Option<RotationType> RotationType) {
    this._KeyId = KeyId;
    this._RotationDate = RotationDate;
    this._RotationType = RotationType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RotationsListEntry o = (RotationsListEntry)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._RotationDate, o._RotationDate) && java.util.Objects.equals(this._RotationType, o._RotationType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RotationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RotationType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.RotationsListEntry.RotationsListEntry");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RotationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RotationType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RotationsListEntry> _TYPE = dafny.TypeDescriptor.<RotationsListEntry>referenceWithInitializer(RotationsListEntry.class, () -> RotationsListEntry.Default());
  public static dafny.TypeDescriptor<RotationsListEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<RotationsListEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RotationsListEntry theDefault = RotationsListEntry.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<RotationType>Default(RotationType._typeDescriptor()));
  public static RotationsListEntry Default() {
    return theDefault;
  }
  public static RotationsListEntry create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RotationDate, Wrappers_Compile.Option<RotationType> RotationType) {
    return new RotationsListEntry(KeyId, RotationDate, RotationType);
  }
  public static RotationsListEntry create_RotationsListEntry(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RotationDate, Wrappers_Compile.Option<RotationType> RotationType) {
    return create(KeyId, RotationDate, RotationType);
  }
  public boolean is_RotationsListEntry() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RotationDate() {
    return this._RotationDate;
  }
  public Wrappers_Compile.Option<RotationType> dtor_RotationType() {
    return this._RotationType;
  }
}
