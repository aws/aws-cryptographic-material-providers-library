// Class RawAES
// Dafny class RawAES compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawAES {
  public dafny.DafnySequence<? extends Character> _keyId;
  public dafny.DafnySequence<? extends Character> _providerId;
  public RawAES (dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId) {
    this._keyId = keyId;
    this._providerId = providerId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawAES o = (RawAES)other;
    return true && java.util.Objects.equals(this._keyId, o._keyId) && java.util.Objects.equals(this._providerId, o._providerId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._providerId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES.RawAES");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._providerId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RawAES> _TYPE = dafny.TypeDescriptor.<RawAES>referenceWithInitializer(RawAES.class, () -> RawAES.Default());
  public static dafny.TypeDescriptor<RawAES> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawAES>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RawAES theDefault = RawAES.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static RawAES Default() {
    return theDefault;
  }
  public static RawAES create(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId) {
    return new RawAES(keyId, providerId);
  }
  public static RawAES create_RawAES(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId) {
    return create(keyId, providerId);
  }
  public boolean is_RawAES() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_providerId() {
    return this._providerId;
  }
}
