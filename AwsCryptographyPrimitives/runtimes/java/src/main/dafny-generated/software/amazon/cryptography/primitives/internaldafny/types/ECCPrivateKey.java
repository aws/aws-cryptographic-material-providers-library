// Class ECCPrivateKey
// Dafny class ECCPrivateKey compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECCPrivateKey {
  public dafny.DafnySequence<? extends java.lang.Byte> _pem;
  public ECCPrivateKey (dafny.DafnySequence<? extends java.lang.Byte> pem) {
    this._pem = pem;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECCPrivateKey o = (ECCPrivateKey)other;
    return true && java.util.Objects.equals(this._pem, o._pem);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._pem);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECCPrivateKey.ECCPrivateKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._pem));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ECCPrivateKey> _TYPE = dafny.TypeDescriptor.<ECCPrivateKey>referenceWithInitializer(ECCPrivateKey.class, () -> ECCPrivateKey.Default());
  public static dafny.TypeDescriptor<ECCPrivateKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECCPrivateKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECCPrivateKey theDefault = ECCPrivateKey.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ECCPrivateKey Default() {
    return theDefault;
  }
  public static ECCPrivateKey create(dafny.DafnySequence<? extends java.lang.Byte> pem) {
    return new ECCPrivateKey(pem);
  }
  public static ECCPrivateKey create_ECCPrivateKey(dafny.DafnySequence<? extends java.lang.Byte> pem) {
    return create(pem);
  }
  public boolean is_ECCPrivateKey() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_pem() {
    return this._pem;
  }
}
