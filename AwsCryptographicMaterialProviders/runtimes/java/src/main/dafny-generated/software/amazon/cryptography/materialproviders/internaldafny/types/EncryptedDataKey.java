// Class EncryptedDataKey
// Dafny class EncryptedDataKey compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptedDataKey {
  public dafny.DafnySequence<? extends java.lang.Byte> _keyProviderId;
  public dafny.DafnySequence<? extends java.lang.Byte> _keyProviderInfo;
  public dafny.DafnySequence<? extends java.lang.Byte> _ciphertext;
  public EncryptedDataKey (dafny.DafnySequence<? extends java.lang.Byte> keyProviderId, dafny.DafnySequence<? extends java.lang.Byte> keyProviderInfo, dafny.DafnySequence<? extends java.lang.Byte> ciphertext) {
    this._keyProviderId = keyProviderId;
    this._keyProviderInfo = keyProviderInfo;
    this._ciphertext = ciphertext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptedDataKey o = (EncryptedDataKey)other;
    return true && java.util.Objects.equals(this._keyProviderId, o._keyProviderId) && java.util.Objects.equals(this._keyProviderInfo, o._keyProviderInfo) && java.util.Objects.equals(this._ciphertext, o._ciphertext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyProviderId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyProviderInfo);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ciphertext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.EncryptedDataKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyProviderId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyProviderInfo));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ciphertext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EncryptedDataKey> _TYPE = dafny.TypeDescriptor.<EncryptedDataKey>referenceWithInitializer(EncryptedDataKey.class, () -> EncryptedDataKey.Default());
  public static dafny.TypeDescriptor<EncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptedDataKey theDefault = EncryptedDataKey.create(UTF8.ValidUTF8Bytes.defaultValue(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static EncryptedDataKey Default() {
    return theDefault;
  }
  public static EncryptedDataKey create(dafny.DafnySequence<? extends java.lang.Byte> keyProviderId, dafny.DafnySequence<? extends java.lang.Byte> keyProviderInfo, dafny.DafnySequence<? extends java.lang.Byte> ciphertext) {
    return new EncryptedDataKey(keyProviderId, keyProviderInfo, ciphertext);
  }
  public static EncryptedDataKey create_EncryptedDataKey(dafny.DafnySequence<? extends java.lang.Byte> keyProviderId, dafny.DafnySequence<? extends java.lang.Byte> keyProviderInfo, dafny.DafnySequence<? extends java.lang.Byte> ciphertext) {
    return create(keyProviderId, keyProviderInfo, ciphertext);
  }
  public boolean is_EncryptedDataKey() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_keyProviderId() {
    return this._keyProviderId;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_keyProviderInfo() {
    return this._keyProviderInfo;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ciphertext() {
    return this._ciphertext;
  }
}
