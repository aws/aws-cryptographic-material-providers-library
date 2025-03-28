// Class AES__GCM
// Dafny class AES__GCM compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AES__GCM {
  public int _keyLength;
  public int _tagLength;
  public int _ivLength;
  public AES__GCM (int keyLength, int tagLength, int ivLength) {
    this._keyLength = keyLength;
    this._tagLength = tagLength;
    this._ivLength = ivLength;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AES__GCM o = (AES__GCM)other;
    return true && this._keyLength == o._keyLength && this._tagLength == o._tagLength && this._ivLength == o._ivLength;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._keyLength);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._tagLength);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._ivLength);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AES_GCM.AES_GCM");
    s.append("(");
    s.append(this._keyLength);
    s.append(", ");
    s.append(this._tagLength);
    s.append(", ");
    s.append(this._ivLength);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AES__GCM> _TYPE = dafny.TypeDescriptor.<AES__GCM>referenceWithInitializer(AES__GCM.class, () -> AES__GCM.Default());
  public static dafny.TypeDescriptor<AES__GCM> _typeDescriptor() {
    return (dafny.TypeDescriptor<AES__GCM>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AES__GCM theDefault = software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(0, 0, 0);
  public static AES__GCM Default() {
    return theDefault;
  }
  public static AES__GCM create(int keyLength, int tagLength, int ivLength) {
    return new AES__GCM(keyLength, tagLength, ivLength);
  }
  public static AES__GCM create_AES__GCM(int keyLength, int tagLength, int ivLength) {
    return create(keyLength, tagLength, ivLength);
  }
  public boolean is_AES__GCM() { return true; }
  public int dtor_keyLength() {
    return this._keyLength;
  }
  public int dtor_tagLength() {
    return this._tagLength;
  }
  public int dtor_ivLength() {
    return this._ivLength;
  }
}
