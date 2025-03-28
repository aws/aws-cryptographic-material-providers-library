// Class CompressPublicKeyOutput
// Dafny class CompressPublicKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CompressPublicKeyOutput {
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedPublicKey;
  public CompressPublicKeyOutput (dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey) {
    this._compressedPublicKey = compressedPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CompressPublicKeyOutput o = (CompressPublicKeyOutput)other;
    return true && java.util.Objects.equals(this._compressedPublicKey, o._compressedPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._compressedPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.CompressPublicKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._compressedPublicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CompressPublicKeyOutput> _TYPE = dafny.TypeDescriptor.<CompressPublicKeyOutput>referenceWithInitializer(CompressPublicKeyOutput.class, () -> CompressPublicKeyOutput.Default());
  public static dafny.TypeDescriptor<CompressPublicKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CompressPublicKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CompressPublicKeyOutput theDefault = software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static CompressPublicKeyOutput Default() {
    return theDefault;
  }
  public static CompressPublicKeyOutput create(dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey) {
    return new CompressPublicKeyOutput(compressedPublicKey);
  }
  public static CompressPublicKeyOutput create_CompressPublicKeyOutput(dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey) {
    return create(compressedPublicKey);
  }
  public boolean is_CompressPublicKeyOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_compressedPublicKey() {
    return this._compressedPublicKey;
  }
}
