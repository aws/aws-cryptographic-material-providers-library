// Class StaticKeyring
// Dafny class StaticKeyring compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticKeyring {
  public dafny.DafnySequence<? extends Character> _keyId;
  public StaticKeyring (dafny.DafnySequence<? extends Character> keyId) {
    this._keyId = keyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StaticKeyring o = (StaticKeyring)other;
    return true && java.util.Objects.equals(this._keyId, o._keyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring.StaticKeyring");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<StaticKeyring> _TYPE = dafny.TypeDescriptor.<StaticKeyring>referenceWithInitializer(StaticKeyring.class, () -> StaticKeyring.Default());
  public static dafny.TypeDescriptor<StaticKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<StaticKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StaticKeyring theDefault = StaticKeyring.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static StaticKeyring Default() {
    return theDefault;
  }
  public static StaticKeyring create(dafny.DafnySequence<? extends Character> keyId) {
    return new StaticKeyring(keyId);
  }
  public static StaticKeyring create_StaticKeyring(dafny.DafnySequence<? extends Character> keyId) {
    return create(keyId);
  }
  public boolean is_StaticKeyring() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
}
