// Class DeriveSharedSecretOutput
// Dafny class DeriveSharedSecretOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeriveSharedSecretOutput {
  public dafny.DafnySequence<? extends java.lang.Byte> _sharedSecret;
  public DeriveSharedSecretOutput (dafny.DafnySequence<? extends java.lang.Byte> sharedSecret) {
    this._sharedSecret = sharedSecret;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeriveSharedSecretOutput o = (DeriveSharedSecretOutput)other;
    return true && java.util.Objects.equals(this._sharedSecret, o._sharedSecret);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._sharedSecret);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.DeriveSharedSecretOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._sharedSecret));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeriveSharedSecretOutput> _TYPE = dafny.TypeDescriptor.<DeriveSharedSecretOutput>referenceWithInitializer(DeriveSharedSecretOutput.class, () -> DeriveSharedSecretOutput.Default());
  public static dafny.TypeDescriptor<DeriveSharedSecretOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeriveSharedSecretOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeriveSharedSecretOutput theDefault = DeriveSharedSecretOutput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static DeriveSharedSecretOutput Default() {
    return theDefault;
  }
  public static DeriveSharedSecretOutput create(dafny.DafnySequence<? extends java.lang.Byte> sharedSecret) {
    return new DeriveSharedSecretOutput(sharedSecret);
  }
  public static DeriveSharedSecretOutput create_DeriveSharedSecretOutput(dafny.DafnySequence<? extends java.lang.Byte> sharedSecret) {
    return create(sharedSecret);
  }
  public boolean is_DeriveSharedSecretOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_sharedSecret() {
    return this._sharedSecret;
  }
}
