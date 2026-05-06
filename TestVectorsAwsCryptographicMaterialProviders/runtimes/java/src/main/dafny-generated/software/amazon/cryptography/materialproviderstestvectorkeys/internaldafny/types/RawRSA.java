// Class RawRSA
// Dafny class RawRSA compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawRSA {
  public dafny.DafnySequence<? extends Character> _keyId;
  public dafny.DafnySequence<? extends Character> _providerId;
  public software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _padding;
  public RawRSA (dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme padding) {
    this._keyId = keyId;
    this._providerId = providerId;
    this._padding = padding;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawRSA o = (RawRSA)other;
    return true && java.util.Objects.equals(this._keyId, o._keyId) && java.util.Objects.equals(this._providerId, o._providerId) && java.util.Objects.equals(this._padding, o._padding);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._providerId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._padding);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA.RawRSA");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._providerId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._padding));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RawRSA> _TYPE = dafny.TypeDescriptor.<RawRSA>referenceWithInitializer(RawRSA.class, () -> RawRSA.Default());
  public static dafny.TypeDescriptor<RawRSA> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawRSA>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RawRSA theDefault = RawRSA.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.Default());
  public static RawRSA Default() {
    return theDefault;
  }
  public static RawRSA create(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme padding) {
    return new RawRSA(keyId, providerId, padding);
  }
  public static RawRSA create_RawRSA(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> providerId, software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme padding) {
    return create(keyId, providerId, padding);
  }
  public boolean is_RawRSA() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_providerId() {
    return this._providerId;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme dtor_padding() {
    return this._padding;
  }
}
