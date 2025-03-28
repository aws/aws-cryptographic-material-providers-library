// Class AESEncryptInput
// Dafny class AESEncryptInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AESEncryptInput {
  public AES__GCM _encAlg;
  public dafny.DafnySequence<? extends java.lang.Byte> _iv;
  public dafny.DafnySequence<? extends java.lang.Byte> _key;
  public dafny.DafnySequence<? extends java.lang.Byte> _msg;
  public dafny.DafnySequence<? extends java.lang.Byte> _aad;
  public AESEncryptInput (AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> msg, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    this._encAlg = encAlg;
    this._iv = iv;
    this._key = key;
    this._msg = msg;
    this._aad = aad;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AESEncryptInput o = (AESEncryptInput)other;
    return true && java.util.Objects.equals(this._encAlg, o._encAlg) && java.util.Objects.equals(this._iv, o._iv) && java.util.Objects.equals(this._key, o._key) && java.util.Objects.equals(this._msg, o._msg) && java.util.Objects.equals(this._aad, o._aad);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encAlg);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._iv);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._msg);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._aad);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AESEncryptInput.AESEncryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encAlg));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._iv));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._msg));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._aad));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AESEncryptInput> _TYPE = dafny.TypeDescriptor.<AESEncryptInput>referenceWithInitializer(AESEncryptInput.class, () -> AESEncryptInput.Default());
  public static dafny.TypeDescriptor<AESEncryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<AESEncryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AESEncryptInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput.create(AES__GCM.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AESEncryptInput Default() {
    return theDefault;
  }
  public static AESEncryptInput create(AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> msg, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    return new AESEncryptInput(encAlg, iv, key, msg, aad);
  }
  public static AESEncryptInput create_AESEncryptInput(AES__GCM encAlg, dafny.DafnySequence<? extends java.lang.Byte> iv, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> msg, dafny.DafnySequence<? extends java.lang.Byte> aad) {
    return create(encAlg, iv, key, msg, aad);
  }
  public boolean is_AESEncryptInput() { return true; }
  public AES__GCM dtor_encAlg() {
    return this._encAlg;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_iv() {
    return this._iv;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_key() {
    return this._key;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_msg() {
    return this._msg;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_aad() {
    return this._aad;
  }
}
