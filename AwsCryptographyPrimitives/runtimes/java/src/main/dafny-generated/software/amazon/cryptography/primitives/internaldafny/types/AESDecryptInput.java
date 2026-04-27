// Class AESDecryptInput
// Dafny class AESDecryptInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AESDecryptInput {
  public AES__GCM _encAlg;
  public dafny.DafnySequence<? extends java.lang.Byte> _key;
  public dafny.DafnySequence<? extends java.lang.Byte> _cipherTxt;
  public dafny.DafnySequence<? extends java.lang.Byte> _authTag;
  public dafny.DafnySequence<? extends java.lang.Byte> _iv;
  public dafny.DafnySequence<? extends java.lang.Byte> _aad;
  public AESDecryptInput (AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> cipherTxt, dafny.DafnySequence<? extends java.lang.Byte> authTag, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    this._encAlg = encAlg;
    this._key = key;
    this._cipherTxt = cipherTxt;
    this._authTag = authTag;
    this._iv = iv;
    this._aad = aad;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AESDecryptInput o = (AESDecryptInput)other;
    return true && java.util.Objects.equals(this._encAlg, o._encAlg) && java.util.Objects.equals(this._key, o._key) && java.util.Objects.equals(this._cipherTxt, o._cipherTxt) && java.util.Objects.equals(this._authTag, o._authTag) && java.util.Objects.equals(this._iv, o._iv) && java.util.Objects.equals(this._aad, o._aad);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encAlg);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cipherTxt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._authTag);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._iv);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._aad);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AESDecryptInput.AESDecryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encAlg));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cipherTxt));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._authTag));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._iv));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._aad));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AESDecryptInput> _TYPE = dafny.TypeDescriptor.<AESDecryptInput>referenceWithInitializer(AESDecryptInput.class, () -> AESDecryptInput.Default());
  public static dafny.TypeDescriptor<AESDecryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<AESDecryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AESDecryptInput theDefault = AESDecryptInput.create(AES__GCM.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AESDecryptInput Default() {
    return theDefault;
  }
  public static AESDecryptInput create(AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> cipherTxt, dafny.DafnySequence<? extends java.lang.Byte> authTag, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    return new AESDecryptInput(encAlg, key, cipherTxt, authTag, iv, aad);
  }
  public static AESDecryptInput create_AESDecryptInput(AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> cipherTxt, dafny.DafnySequence<? extends java.lang.Byte> authTag, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    return create(encAlg, key, cipherTxt, authTag, iv, aad);
  }
  public boolean is_AESDecryptInput() { return true; }
  public AES__GCM dtor_encAlg() {
    return this._encAlg;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_key() {
    return this._key;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_cipherTxt() {
    return this._cipherTxt;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_authTag() {
    return this._authTag;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_iv() {
    return this._iv;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_aad() {
    return this._aad;
  }
}
