// Class KMSInfo
// Dafny class KMSInfo compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KMSInfo {
  public dafny.DafnySequence<? extends Character> _keyId;
  public KMSInfo (dafny.DafnySequence<? extends Character> keyId) {
    this._keyId = keyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSInfo o = (KMSInfo)other;
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
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo.KMSInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KMSInfo> _TYPE = dafny.TypeDescriptor.<KMSInfo>referenceWithInitializer(KMSInfo.class, () -> KMSInfo.Default());
  public static dafny.TypeDescriptor<KMSInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KMSInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KMSInfo theDefault = KMSInfo.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KMSInfo Default() {
    return theDefault;
  }
  public static KMSInfo create(dafny.DafnySequence<? extends Character> keyId) {
    return new KMSInfo(keyId);
  }
  public static KMSInfo create_KMSInfo(dafny.DafnySequence<? extends Character> keyId) {
    return create(keyId);
  }
  public boolean is_KMSInfo() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
}
