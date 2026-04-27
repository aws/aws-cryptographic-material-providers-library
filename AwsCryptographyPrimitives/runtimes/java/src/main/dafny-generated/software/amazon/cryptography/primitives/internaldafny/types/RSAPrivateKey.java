// Class RSAPrivateKey
// Dafny class RSAPrivateKey compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAPrivateKey {
  public int _lengthBits;
  public dafny.DafnySequence<? extends java.lang.Byte> _pem;
  public RSAPrivateKey (int lengthBits, dafny.DafnySequence<? extends java.lang.Byte> pem) {
    this._lengthBits = lengthBits;
    this._pem = pem;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSAPrivateKey o = (RSAPrivateKey)other;
    return true && this._lengthBits == o._lengthBits && java.util.Objects.equals(this._pem, o._pem);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._lengthBits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._pem);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.RSAPrivateKey.RSAPrivateKey");
    s.append("(");
    s.append(this._lengthBits);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._pem));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RSAPrivateKey> _TYPE = dafny.TypeDescriptor.<RSAPrivateKey>referenceWithInitializer(RSAPrivateKey.class, () -> RSAPrivateKey.Default());
  public static dafny.TypeDescriptor<RSAPrivateKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<RSAPrivateKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RSAPrivateKey theDefault = RSAPrivateKey.create(0, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static RSAPrivateKey Default() {
    return theDefault;
  }
  public static RSAPrivateKey create(int lengthBits, dafny.DafnySequence<? extends java.lang.Byte> pem) {
    return new RSAPrivateKey(lengthBits, pem);
  }
  public static RSAPrivateKey create_RSAPrivateKey(int lengthBits, dafny.DafnySequence<? extends java.lang.Byte> pem) {
    return create(lengthBits, pem);
  }
  public boolean is_RSAPrivateKey() { return true; }
  public int dtor_lengthBits() {
    return this._lengthBits;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_pem() {
    return this._pem;
  }
}
