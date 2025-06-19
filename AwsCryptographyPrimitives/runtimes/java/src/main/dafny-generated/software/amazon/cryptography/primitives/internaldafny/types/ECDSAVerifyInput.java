// Class ECDSAVerifyInput
// Dafny class ECDSAVerifyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECDSAVerifyInput {
  public ECDSASignatureAlgorithm _signatureAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _verificationKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _message;
  public dafny.DafnySequence<? extends java.lang.Byte> _signature;
  public ECDSAVerifyInput (ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> message, dafny.DafnySequence<? extends java.lang.Byte> signature) {
    this._signatureAlgorithm = signatureAlgorithm;
    this._verificationKey = verificationKey;
    this._message = message;
    this._signature = signature;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDSAVerifyInput o = (ECDSAVerifyInput)other;
    return true && java.util.Objects.equals(this._signatureAlgorithm, o._signatureAlgorithm) && java.util.Objects.equals(this._verificationKey, o._verificationKey) && java.util.Objects.equals(this._message, o._message) && java.util.Objects.equals(this._signature, o._signature);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signatureAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signature);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDSAVerifyInput.ECDSAVerifyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._signatureAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signature));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ECDSAVerifyInput> _TYPE = dafny.TypeDescriptor.<ECDSAVerifyInput>referenceWithInitializer(ECDSAVerifyInput.class, () -> ECDSAVerifyInput.Default());
  public static dafny.TypeDescriptor<ECDSAVerifyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECDSAVerifyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECDSAVerifyInput theDefault = ECDSAVerifyInput.create(ECDSASignatureAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ECDSAVerifyInput Default() {
    return theDefault;
  }
  public static ECDSAVerifyInput create(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> message, dafny.DafnySequence<? extends java.lang.Byte> signature) {
    return new ECDSAVerifyInput(signatureAlgorithm, verificationKey, message, signature);
  }
  public static ECDSAVerifyInput create_ECDSAVerifyInput(ECDSASignatureAlgorithm signatureAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> message, dafny.DafnySequence<? extends java.lang.Byte> signature) {
    return create(signatureAlgorithm, verificationKey, message, signature);
  }
  public boolean is_ECDSAVerifyInput() { return true; }
  public ECDSASignatureAlgorithm dtor_signatureAlgorithm() {
    return this._signatureAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_verificationKey() {
    return this._verificationKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_message() {
    return this._message;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_signature() {
    return this._signature;
  }
}
