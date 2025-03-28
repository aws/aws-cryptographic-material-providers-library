// Class AES__CTR
// Dafny class AES__CTR compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AES__CTR {
  public int _keyLength;
  public int _nonceLength;
  public AES__CTR (int keyLength, int nonceLength) {
    this._keyLength = keyLength;
    this._nonceLength = nonceLength;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AES__CTR o = (AES__CTR)other;
    return true && this._keyLength == o._keyLength && this._nonceLength == o._nonceLength;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._keyLength);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._nonceLength);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AES_CTR.AES_CTR");
    s.append("(");
    s.append(this._keyLength);
    s.append(", ");
    s.append(this._nonceLength);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AES__CTR> _TYPE = dafny.TypeDescriptor.<AES__CTR>referenceWithInitializer(AES__CTR.class, () -> AES__CTR.Default());
  public static dafny.TypeDescriptor<AES__CTR> _typeDescriptor() {
    return (dafny.TypeDescriptor<AES__CTR>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AES__CTR theDefault = software.amazon.cryptography.primitives.internaldafny.types.AES__CTR.create(0, 0);
  public static AES__CTR Default() {
    return theDefault;
  }
  public static AES__CTR create(int keyLength, int nonceLength) {
    return new AES__CTR(keyLength, nonceLength);
  }
  public static AES__CTR create_AES__CTR(int keyLength, int nonceLength) {
    return create(keyLength, nonceLength);
  }
  public boolean is_AES__CTR() { return true; }
  public int dtor_keyLength() {
    return this._keyLength;
  }
  public int dtor_nonceLength() {
    return this._nonceLength;
  }
}
