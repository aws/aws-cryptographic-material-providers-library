// Class KmsEcdhKeyring
// Dafny class KmsEcdhKeyring compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsEcdhKeyring {
  public dafny.DafnySequence<? extends Character> _senderKeyId;
  public dafny.DafnySequence<? extends Character> _recipientKeyId;
  public dafny.DafnySequence<? extends Character> _senderPublicKey;
  public dafny.DafnySequence<? extends Character> _recipientPublicKey;
  public dafny.DafnySequence<? extends Character> _curveSpec;
  public dafny.DafnySequence<? extends Character> _keyAgreementScheme;
  public KmsEcdhKeyring (dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    this._senderKeyId = senderKeyId;
    this._recipientKeyId = recipientKeyId;
    this._senderPublicKey = senderPublicKey;
    this._recipientPublicKey = recipientPublicKey;
    this._curveSpec = curveSpec;
    this._keyAgreementScheme = keyAgreementScheme;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsEcdhKeyring o = (KmsEcdhKeyring)other;
    return true && java.util.Objects.equals(this._senderKeyId, o._senderKeyId) && java.util.Objects.equals(this._recipientKeyId, o._recipientKeyId) && java.util.Objects.equals(this._senderPublicKey, o._senderPublicKey) && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey) && java.util.Objects.equals(this._curveSpec, o._curveSpec) && java.util.Objects.equals(this._keyAgreementScheme, o._keyAgreementScheme);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._curveSpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyAgreementScheme);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring.KmsEcdhKeyring");
    s.append("(");
    s.append(dafny.Helpers.toString(this._senderKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._senderPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._curveSpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyAgreementScheme));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsEcdhKeyring> _TYPE = dafny.TypeDescriptor.<KmsEcdhKeyring>referenceWithInitializer(KmsEcdhKeyring.class, () -> KmsEcdhKeyring.Default());
  public static dafny.TypeDescriptor<KmsEcdhKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsEcdhKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsEcdhKeyring theDefault = KmsEcdhKeyring.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KmsEcdhKeyring Default() {
    return theDefault;
  }
  public static KmsEcdhKeyring create(dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    return new KmsEcdhKeyring(senderKeyId, recipientKeyId, senderPublicKey, recipientPublicKey, curveSpec, keyAgreementScheme);
  }
  public static KmsEcdhKeyring create_KmsEcdhKeyring(dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    return create(senderKeyId, recipientKeyId, senderPublicKey, recipientPublicKey, curveSpec, keyAgreementScheme);
  }
  public boolean is_KmsEcdhKeyring() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_senderKeyId() {
    return this._senderKeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_recipientKeyId() {
    return this._recipientKeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_senderPublicKey() {
    return this._senderPublicKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_recipientPublicKey() {
    return this._recipientPublicKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_curveSpec() {
    return this._curveSpec;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyAgreementScheme() {
    return this._keyAgreementScheme;
  }
}
