// Class HKDF
// Dafny class HKDF compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class HKDF {
  public software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _hmac;
  public int _saltLength;
  public int _inputKeyLength;
  public int _outputKeyLength;
  public HKDF (software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm hmac, int saltLength, int inputKeyLength, int outputKeyLength) {
    this._hmac = hmac;
    this._saltLength = saltLength;
    this._inputKeyLength = inputKeyLength;
    this._outputKeyLength = outputKeyLength;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HKDF o = (HKDF)other;
    return true && java.util.Objects.equals(this._hmac, o._hmac) && this._saltLength == o._saltLength && this._inputKeyLength == o._inputKeyLength && this._outputKeyLength == o._outputKeyLength;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._hmac);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._saltLength);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._inputKeyLength);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._outputKeyLength);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.HKDF.HKDF");
    s.append("(");
    s.append(dafny.Helpers.toString(this._hmac));
    s.append(", ");
    s.append(this._saltLength);
    s.append(", ");
    s.append(this._inputKeyLength);
    s.append(", ");
    s.append(this._outputKeyLength);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HKDF> _TYPE = dafny.TypeDescriptor.<HKDF>referenceWithInitializer(HKDF.class, () -> HKDF.Default());
  public static dafny.TypeDescriptor<HKDF> _typeDescriptor() {
    return (dafny.TypeDescriptor<HKDF>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HKDF theDefault = HKDF.create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.Default(), 0, 0, 0);
  public static HKDF Default() {
    return theDefault;
  }
  public static HKDF create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm hmac, int saltLength, int inputKeyLength, int outputKeyLength) {
    return new HKDF(hmac, saltLength, inputKeyLength, outputKeyLength);
  }
  public static HKDF create_HKDF(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm hmac, int saltLength, int inputKeyLength, int outputKeyLength) {
    return create(hmac, saltLength, inputKeyLength, outputKeyLength);
  }
  public boolean is_HKDF() { return true; }
  public software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm dtor_hmac() {
    return this._hmac;
  }
  public int dtor_saltLength() {
    return this._saltLength;
  }
  public int dtor_inputKeyLength() {
    return this._inputKeyLength;
  }
  public int dtor_outputKeyLength() {
    return this._outputKeyLength;
  }
}
