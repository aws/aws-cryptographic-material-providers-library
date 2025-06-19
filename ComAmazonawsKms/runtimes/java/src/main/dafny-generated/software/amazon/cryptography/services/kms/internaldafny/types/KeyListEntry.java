// Class KeyListEntry
// Dafny class KeyListEntry compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyListEntry {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyArn;
  public KeyListEntry (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyArn) {
    this._KeyId = KeyId;
    this._KeyArn = KeyArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyListEntry o = (KeyListEntry)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._KeyArn, o._KeyArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeyListEntry.KeyListEntry");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyListEntry> _TYPE = dafny.TypeDescriptor.<KeyListEntry>referenceWithInitializer(KeyListEntry.class, () -> KeyListEntry.Default());
  public static dafny.TypeDescriptor<KeyListEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyListEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyListEntry theDefault = KeyListEntry.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ArnType._typeDescriptor()));
  public static KeyListEntry Default() {
    return theDefault;
  }
  public static KeyListEntry create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyArn) {
    return new KeyListEntry(KeyId, KeyArn);
  }
  public static KeyListEntry create_KeyListEntry(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyArn) {
    return create(KeyId, KeyArn);
  }
  public boolean is_KeyListEntry() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyArn() {
    return this._KeyArn;
  }
}
