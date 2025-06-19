// Class ECCPublicKey
// Dafny class ECCPublicKey compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECCPublicKey {
  public dafny.DafnySequence<? extends java.lang.Byte> _der;
  public ECCPublicKey (dafny.DafnySequence<? extends java.lang.Byte> der) {
    this._der = der;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECCPublicKey o = (ECCPublicKey)other;
    return true && java.util.Objects.equals(this._der, o._der);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._der);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECCPublicKey.ECCPublicKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._der));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ECCPublicKey> _TYPE = dafny.TypeDescriptor.<ECCPublicKey>referenceWithInitializer(ECCPublicKey.class, () -> ECCPublicKey.Default());
  public static dafny.TypeDescriptor<ECCPublicKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECCPublicKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECCPublicKey theDefault = ECCPublicKey.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ECCPublicKey Default() {
    return theDefault;
  }
  public static ECCPublicKey create(dafny.DafnySequence<? extends java.lang.Byte> der) {
    return new ECCPublicKey(der);
  }
  public static ECCPublicKey create_ECCPublicKey(dafny.DafnySequence<? extends java.lang.Byte> der) {
    return create(der);
  }
  public boolean is_ECCPublicKey() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_der() {
    return this._der;
  }
}
