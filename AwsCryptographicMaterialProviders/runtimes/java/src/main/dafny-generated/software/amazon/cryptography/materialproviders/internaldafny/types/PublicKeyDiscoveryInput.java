// Class PublicKeyDiscoveryInput
// Dafny class PublicKeyDiscoveryInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PublicKeyDiscoveryInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientStaticPrivateKey;
  public PublicKeyDiscoveryInput (dafny.DafnySequence<? extends java.lang.Byte> recipientStaticPrivateKey) {
    this._recipientStaticPrivateKey = recipientStaticPrivateKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PublicKeyDiscoveryInput o = (PublicKeyDiscoveryInput)other;
    return true && java.util.Objects.equals(this._recipientStaticPrivateKey, o._recipientStaticPrivateKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientStaticPrivateKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput.PublicKeyDiscoveryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._recipientStaticPrivateKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PublicKeyDiscoveryInput> _TYPE = dafny.TypeDescriptor.<PublicKeyDiscoveryInput>referenceWithInitializer(PublicKeyDiscoveryInput.class, () -> PublicKeyDiscoveryInput.Default());
  public static dafny.TypeDescriptor<PublicKeyDiscoveryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PublicKeyDiscoveryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PublicKeyDiscoveryInput theDefault = PublicKeyDiscoveryInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static PublicKeyDiscoveryInput Default() {
    return theDefault;
  }
  public static PublicKeyDiscoveryInput create(dafny.DafnySequence<? extends java.lang.Byte> recipientStaticPrivateKey) {
    return new PublicKeyDiscoveryInput(recipientStaticPrivateKey);
  }
  public static PublicKeyDiscoveryInput create_PublicKeyDiscoveryInput(dafny.DafnySequence<? extends java.lang.Byte> recipientStaticPrivateKey) {
    return create(recipientStaticPrivateKey);
  }
  public boolean is_PublicKeyDiscoveryInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_recipientStaticPrivateKey() {
    return this._recipientStaticPrivateKey;
  }
}
