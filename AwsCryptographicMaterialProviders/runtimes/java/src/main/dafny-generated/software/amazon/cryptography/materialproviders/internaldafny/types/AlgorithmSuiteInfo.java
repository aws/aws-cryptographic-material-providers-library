// Class AlgorithmSuiteInfo
// Dafny class AlgorithmSuiteInfo compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSuiteInfo {
  public AlgorithmSuiteId _id;
  public dafny.DafnySequence<? extends java.lang.Byte> _binaryId;
  public int _messageVersion;
  public Encrypt _encrypt;
  public DerivationAlgorithm _kdf;
  public DerivationAlgorithm _commitment;
  public SignatureAlgorithm _signature;
  public SymmetricSignatureAlgorithm _symmetricSignature;
  public EdkWrappingAlgorithm _edkWrapping;
  public AlgorithmSuiteInfo (AlgorithmSuiteId id, dafny.DafnySequence<? extends java.lang.Byte> binaryId, int messageVersion, Encrypt encrypt, DerivationAlgorithm kdf, DerivationAlgorithm commitment, SignatureAlgorithm signature, SymmetricSignatureAlgorithm symmetricSignature, EdkWrappingAlgorithm edkWrapping) {
    this._id = id;
    this._binaryId = binaryId;
    this._messageVersion = messageVersion;
    this._encrypt = encrypt;
    this._kdf = kdf;
    this._commitment = commitment;
    this._signature = signature;
    this._symmetricSignature = symmetricSignature;
    this._edkWrapping = edkWrapping;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AlgorithmSuiteInfo o = (AlgorithmSuiteInfo)other;
    return true && java.util.Objects.equals(this._id, o._id) && java.util.Objects.equals(this._binaryId, o._binaryId) && this._messageVersion == o._messageVersion && java.util.Objects.equals(this._encrypt, o._encrypt) && java.util.Objects.equals(this._kdf, o._kdf) && java.util.Objects.equals(this._commitment, o._commitment) && java.util.Objects.equals(this._signature, o._signature) && java.util.Objects.equals(this._symmetricSignature, o._symmetricSignature) && java.util.Objects.equals(this._edkWrapping, o._edkWrapping);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._id);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._binaryId);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._messageVersion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encrypt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kdf);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitment);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signature);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSignature);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._edkWrapping);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.AlgorithmSuiteInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._id));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._binaryId));
    s.append(", ");
    s.append(this._messageVersion);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encrypt));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kdf));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitment));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signature));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSignature));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._edkWrapping));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AlgorithmSuiteInfo> _TYPE = dafny.TypeDescriptor.<AlgorithmSuiteInfo>referenceWithInitializer(AlgorithmSuiteInfo.class, () -> AlgorithmSuiteInfo.Default());
  public static dafny.TypeDescriptor<AlgorithmSuiteInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<AlgorithmSuiteInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AlgorithmSuiteInfo theDefault = AlgorithmSuiteInfo.create(AlgorithmSuiteId.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, Encrypt.Default(), DerivationAlgorithm.Default(), DerivationAlgorithm.Default(), SignatureAlgorithm.Default(), SymmetricSignatureAlgorithm.Default(), EdkWrappingAlgorithm.Default());
  public static AlgorithmSuiteInfo Default() {
    return theDefault;
  }
  public static AlgorithmSuiteInfo create(AlgorithmSuiteId id, dafny.DafnySequence<? extends java.lang.Byte> binaryId, int messageVersion, Encrypt encrypt, DerivationAlgorithm kdf, DerivationAlgorithm commitment, SignatureAlgorithm signature, SymmetricSignatureAlgorithm symmetricSignature, EdkWrappingAlgorithm edkWrapping) {
    return new AlgorithmSuiteInfo(id, binaryId, messageVersion, encrypt, kdf, commitment, signature, symmetricSignature, edkWrapping);
  }
  public static AlgorithmSuiteInfo create_AlgorithmSuiteInfo(AlgorithmSuiteId id, dafny.DafnySequence<? extends java.lang.Byte> binaryId, int messageVersion, Encrypt encrypt, DerivationAlgorithm kdf, DerivationAlgorithm commitment, SignatureAlgorithm signature, SymmetricSignatureAlgorithm symmetricSignature, EdkWrappingAlgorithm edkWrapping) {
    return create(id, binaryId, messageVersion, encrypt, kdf, commitment, signature, symmetricSignature, edkWrapping);
  }
  public boolean is_AlgorithmSuiteInfo() { return true; }
  public AlgorithmSuiteId dtor_id() {
    return this._id;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_binaryId() {
    return this._binaryId;
  }
  public int dtor_messageVersion() {
    return this._messageVersion;
  }
  public Encrypt dtor_encrypt() {
    return this._encrypt;
  }
  public DerivationAlgorithm dtor_kdf() {
    return this._kdf;
  }
  public DerivationAlgorithm dtor_commitment() {
    return this._commitment;
  }
  public SignatureAlgorithm dtor_signature() {
    return this._signature;
  }
  public SymmetricSignatureAlgorithm dtor_symmetricSignature() {
    return this._symmetricSignature;
  }
  public EdkWrappingAlgorithm dtor_edkWrapping() {
    return this._edkWrapping;
  }
}
