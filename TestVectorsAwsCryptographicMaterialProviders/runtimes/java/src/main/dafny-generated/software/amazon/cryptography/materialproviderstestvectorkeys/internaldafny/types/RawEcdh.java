// Class RawEcdh
// Dafny class RawEcdh compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawEcdh {
  public dafny.DafnySequence<? extends Character> _senderKeyId;
  public dafny.DafnySequence<? extends Character> _recipientKeyId;
  public dafny.DafnySequence<? extends Character> _senderPublicKey;
  public dafny.DafnySequence<? extends Character> _recipientPublicKey;
  public dafny.DafnySequence<? extends Character> _providerId;
  public dafny.DafnySequence<? extends Character> _curveSpec;
  public dafny.DafnySequence<? extends Character> _keyAgreementScheme;
  public RawEcdh (dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> providerId, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    this._senderKeyId = senderKeyId;
    this._recipientKeyId = recipientKeyId;
    this._senderPublicKey = senderPublicKey;
    this._recipientPublicKey = recipientPublicKey;
    this._providerId = providerId;
    this._curveSpec = curveSpec;
    this._keyAgreementScheme = keyAgreementScheme;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawEcdh o = (RawEcdh)other;
    return true && java.util.Objects.equals(this._senderKeyId, o._senderKeyId) && java.util.Objects.equals(this._recipientKeyId, o._recipientKeyId) && java.util.Objects.equals(this._senderPublicKey, o._senderPublicKey) && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey) && java.util.Objects.equals(this._providerId, o._providerId) && java.util.Objects.equals(this._curveSpec, o._curveSpec) && java.util.Objects.equals(this._keyAgreementScheme, o._keyAgreementScheme);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._providerId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._curveSpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyAgreementScheme);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh.RawEcdh");
    s.append("(");
    s.append(dafny.Helpers.toString(this._senderKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._senderPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._providerId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._curveSpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyAgreementScheme));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RawEcdh> _TYPE = dafny.TypeDescriptor.<RawEcdh>referenceWithInitializer(RawEcdh.class, () -> RawEcdh.Default());
  public static dafny.TypeDescriptor<RawEcdh> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawEcdh>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RawEcdh theDefault = RawEcdh.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static RawEcdh Default() {
    return theDefault;
  }
  public static RawEcdh create(dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> providerId, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    return new RawEcdh(senderKeyId, recipientKeyId, senderPublicKey, recipientPublicKey, providerId, curveSpec, keyAgreementScheme);
  }
  public static RawEcdh create_RawEcdh(dafny.DafnySequence<? extends Character> senderKeyId, dafny.DafnySequence<? extends Character> recipientKeyId, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey, dafny.DafnySequence<? extends Character> providerId, dafny.DafnySequence<? extends Character> curveSpec, dafny.DafnySequence<? extends Character> keyAgreementScheme) {
    return create(senderKeyId, recipientKeyId, senderPublicKey, recipientPublicKey, providerId, curveSpec, keyAgreementScheme);
  }
  public boolean is_RawEcdh() { return true; }
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
  public dafny.DafnySequence<? extends Character> dtor_providerId() {
    return this._providerId;
  }
  public dafny.DafnySequence<? extends Character> dtor_curveSpec() {
    return this._curveSpec;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyAgreementScheme() {
    return this._keyAgreementScheme;
  }
}
