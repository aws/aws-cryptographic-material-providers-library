// Class GenerateECDSASignatureKeyOutput
// Dafny class GenerateECDSASignatureKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateECDSASignatureKeyOutput {
  public ECDSASignatureAlgorithm _signatureAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _verificationKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _signingKey;
  public GenerateECDSASignatureKeyOutput (ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    this._signatureAlgorithm = signatureAlgorithm;
    this._verificationKey = verificationKey;
    this._signingKey = signingKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateECDSASignatureKeyOutput o = (GenerateECDSASignatureKeyOutput)other;
    return true && java.util.Objects.equals(this._signatureAlgorithm, o._signatureAlgorithm) && java.util.Objects.equals(this._verificationKey, o._verificationKey) && java.util.Objects.equals(this._signingKey, o._signingKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signatureAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.GenerateECDSASignatureKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._signatureAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateECDSASignatureKeyOutput> _TYPE = dafny.TypeDescriptor.<GenerateECDSASignatureKeyOutput>referenceWithInitializer(GenerateECDSASignatureKeyOutput.class, () -> GenerateECDSASignatureKeyOutput.Default());
  public static dafny.TypeDescriptor<GenerateECDSASignatureKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateECDSASignatureKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateECDSASignatureKeyOutput theDefault = software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.create(ECDSASignatureAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static GenerateECDSASignatureKeyOutput Default() {
    return theDefault;
  }
  public static GenerateECDSASignatureKeyOutput create(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    return new GenerateECDSASignatureKeyOutput(signatureAlgorithm, verificationKey, signingKey);
  }
  public static GenerateECDSASignatureKeyOutput create_GenerateECDSASignatureKeyOutput(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    return create(signatureAlgorithm, verificationKey, signingKey);
  }
  public boolean is_GenerateECDSASignatureKeyOutput() { return true; }
  public ECDSASignatureAlgorithm dtor_signatureAlgorithm() {
    return this._signatureAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_verificationKey() {
    return this._verificationKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_signingKey() {
    return this._signingKey;
  }
}
