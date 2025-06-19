// Class AESEncryptOutput
// Dafny class AESEncryptOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AESEncryptOutput {
  public dafny.DafnySequence<? extends java.lang.Byte> _cipherText;
  public dafny.DafnySequence<? extends java.lang.Byte> _authTag;
  public AESEncryptOutput (dafny.DafnySequence<? extends java.lang.Byte> cipherText, dafny.DafnySequence<? extends java.lang.Byte> authTag) {
    this._cipherText = cipherText;
    this._authTag = authTag;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AESEncryptOutput o = (AESEncryptOutput)other;
    return true && java.util.Objects.equals(this._cipherText, o._cipherText) && java.util.Objects.equals(this._authTag, o._authTag);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cipherText);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._authTag);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AESEncryptOutput.AESEncryptOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._cipherText));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._authTag));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AESEncryptOutput> _TYPE = dafny.TypeDescriptor.<AESEncryptOutput>referenceWithInitializer(AESEncryptOutput.class, () -> AESEncryptOutput.Default());
  public static dafny.TypeDescriptor<AESEncryptOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<AESEncryptOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AESEncryptOutput theDefault = AESEncryptOutput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AESEncryptOutput Default() {
    return theDefault;
  }
  public static AESEncryptOutput create(dafny.DafnySequence<? extends java.lang.Byte> cipherText, dafny.DafnySequence<? extends java.lang.Byte> authTag) {
    return new AESEncryptOutput(cipherText, authTag);
  }
  public static AESEncryptOutput create_AESEncryptOutput(dafny.DafnySequence<? extends java.lang.Byte> cipherText, dafny.DafnySequence<? extends java.lang.Byte> authTag) {
    return create(cipherText, authTag);
  }
  public boolean is_AESEncryptOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_cipherText() {
    return this._cipherText;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_authTag() {
    return this._authTag;
  }
}
