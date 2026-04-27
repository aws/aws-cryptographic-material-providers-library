// Class KmsMrkAware
// Dafny class KmsMrkAware compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsMrkAware {
  public dafny.DafnySequence<? extends Character> _keyId;
  public KmsMrkAware (dafny.DafnySequence<? extends Character> keyId) {
    this._keyId = keyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsMrkAware o = (KmsMrkAware)other;
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
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware.KmsMrkAware");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsMrkAware> _TYPE = dafny.TypeDescriptor.<KmsMrkAware>referenceWithInitializer(KmsMrkAware.class, () -> KmsMrkAware.Default());
  public static dafny.TypeDescriptor<KmsMrkAware> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsMrkAware>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsMrkAware theDefault = KmsMrkAware.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KmsMrkAware Default() {
    return theDefault;
  }
  public static KmsMrkAware create(dafny.DafnySequence<? extends Character> keyId) {
    return new KmsMrkAware(keyId);
  }
  public static KmsMrkAware create_KmsMrkAware(dafny.DafnySequence<? extends Character> keyId) {
    return create(keyId);
  }
  public boolean is_KmsMrkAware() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
}
