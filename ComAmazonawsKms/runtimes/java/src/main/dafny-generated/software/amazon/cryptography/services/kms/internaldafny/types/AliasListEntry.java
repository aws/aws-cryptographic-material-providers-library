// Class AliasListEntry
// Dafny class AliasListEntry compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AliasListEntry {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AliasName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AliasArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TargetKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastUpdatedDate;
  public AliasListEntry (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TargetKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdatedDate) {
    this._AliasName = AliasName;
    this._AliasArn = AliasArn;
    this._TargetKeyId = TargetKeyId;
    this._CreationDate = CreationDate;
    this._LastUpdatedDate = LastUpdatedDate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AliasListEntry o = (AliasListEntry)other;
    return true && java.util.Objects.equals(this._AliasName, o._AliasName) && java.util.Objects.equals(this._AliasArn, o._AliasArn) && java.util.Objects.equals(this._TargetKeyId, o._TargetKeyId) && java.util.Objects.equals(this._CreationDate, o._CreationDate) && java.util.Objects.equals(this._LastUpdatedDate, o._LastUpdatedDate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AliasName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AliasArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastUpdatedDate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.AliasListEntry.AliasListEntry");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AliasName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AliasArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastUpdatedDate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AliasListEntry> _TYPE = dafny.TypeDescriptor.<AliasListEntry>referenceWithInitializer(AliasListEntry.class, () -> AliasListEntry.Default());
  public static dafny.TypeDescriptor<AliasListEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<AliasListEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AliasListEntry theDefault = software.amazon.cryptography.services.kms.internaldafny.types.AliasListEntry.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(AliasNameType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ArnType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static AliasListEntry Default() {
    return theDefault;
  }
  public static AliasListEntry create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TargetKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdatedDate) {
    return new AliasListEntry(AliasName, AliasArn, TargetKeyId, CreationDate, LastUpdatedDate);
  }
  public static AliasListEntry create_AliasListEntry(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AliasArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TargetKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastUpdatedDate) {
    return create(AliasName, AliasArn, TargetKeyId, CreationDate, LastUpdatedDate);
  }
  public boolean is_AliasListEntry() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AliasName() {
    return this._AliasName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AliasArn() {
    return this._AliasArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TargetKeyId() {
    return this._TargetKeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDate() {
    return this._CreationDate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastUpdatedDate() {
    return this._LastUpdatedDate;
  }
}
