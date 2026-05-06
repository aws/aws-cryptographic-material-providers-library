// Class HierarchyKeyring
// Dafny class HierarchyKeyring compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class HierarchyKeyring {
  public dafny.DafnySequence<? extends Character> _keyId;
  public HierarchyKeyring (dafny.DafnySequence<? extends Character> keyId) {
    this._keyId = keyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HierarchyKeyring o = (HierarchyKeyring)other;
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
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring.HierarchyKeyring");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HierarchyKeyring> _TYPE = dafny.TypeDescriptor.<HierarchyKeyring>referenceWithInitializer(HierarchyKeyring.class, () -> HierarchyKeyring.Default());
  public static dafny.TypeDescriptor<HierarchyKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<HierarchyKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HierarchyKeyring theDefault = HierarchyKeyring.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static HierarchyKeyring Default() {
    return theDefault;
  }
  public static HierarchyKeyring create(dafny.DafnySequence<? extends Character> keyId) {
    return new HierarchyKeyring(keyId);
  }
  public static HierarchyKeyring create_HierarchyKeyring(dafny.DafnySequence<? extends Character> keyId) {
    return create(keyId);
  }
  public boolean is_HierarchyKeyring() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
}
