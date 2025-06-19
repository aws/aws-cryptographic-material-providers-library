// Class ECDSASignInput
// Dafny class ECDSASignInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECDSASignInput {
  public ECDSASignatureAlgorithm _signatureAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _signingKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _message;
  public ECDSASignInput (ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> signingKey, dafny.DafnySequence<? extends java.lang.Byte> message) {
    this._signatureAlgorithm = signatureAlgorithm;
    this._signingKey = signingKey;
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDSASignInput o = (ECDSASignInput)other;
    return true && java.util.Objects.equals(this._signatureAlgorithm, o._signatureAlgorithm) && java.util.Objects.equals(this._signingKey, o._signingKey) && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signatureAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDSASignInput.ECDSASignInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._signatureAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ECDSASignInput> _TYPE = dafny.TypeDescriptor.<ECDSASignInput>referenceWithInitializer(ECDSASignInput.class, () -> ECDSASignInput.Default());
  public static dafny.TypeDescriptor<ECDSASignInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECDSASignInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECDSASignInput theDefault = ECDSASignInput.create(ECDSASignatureAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ECDSASignInput Default() {
    return theDefault;
  }
  public static ECDSASignInput create(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> signingKey, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return new ECDSASignInput(signatureAlgorithm, signingKey, message);
  }
  public static ECDSASignInput create_ECDSASignInput(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> signingKey, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return create(signatureAlgorithm, signingKey, message);
  }
  public boolean is_ECDSASignInput() { return true; }
  public ECDSASignatureAlgorithm dtor_signatureAlgorithm() {
    return this._signatureAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_signingKey() {
    return this._signingKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_message() {
    return this._message;
  }
}
