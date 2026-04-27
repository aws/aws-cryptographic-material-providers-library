// Class GetPublicKeyResponse
// Dafny class GetPublicKeyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetPublicKeyResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PublicKey;
  public Wrappers_Compile.Option<CustomerMasterKeySpec> _CustomerMasterKeySpec;
  public Wrappers_Compile.Option<KeySpec> _KeySpec;
  public Wrappers_Compile.Option<KeyUsageType> _KeyUsage;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> _EncryptionAlgorithms;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> _SigningAlgorithms;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> _KeyAgreementAlgorithms;
  public GetPublicKeyResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms) {
    this._KeyId = KeyId;
    this._PublicKey = PublicKey;
    this._CustomerMasterKeySpec = CustomerMasterKeySpec;
    this._KeySpec = KeySpec;
    this._KeyUsage = KeyUsage;
    this._EncryptionAlgorithms = EncryptionAlgorithms;
    this._SigningAlgorithms = SigningAlgorithms;
    this._KeyAgreementAlgorithms = KeyAgreementAlgorithms;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetPublicKeyResponse o = (GetPublicKeyResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._PublicKey, o._PublicKey) && java.util.Objects.equals(this._CustomerMasterKeySpec, o._CustomerMasterKeySpec) && java.util.Objects.equals(this._KeySpec, o._KeySpec) && java.util.Objects.equals(this._KeyUsage, o._KeyUsage) && java.util.Objects.equals(this._EncryptionAlgorithms, o._EncryptionAlgorithms) && java.util.Objects.equals(this._SigningAlgorithms, o._SigningAlgorithms) && java.util.Objects.equals(this._KeyAgreementAlgorithms, o._KeyAgreementAlgorithms);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomerMasterKeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyUsage);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementAlgorithms);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetPublicKeyResponse.GetPublicKeyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomerMasterKeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyUsage));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyAgreementAlgorithms));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetPublicKeyResponse> _TYPE = dafny.TypeDescriptor.<GetPublicKeyResponse>referenceWithInitializer(GetPublicKeyResponse.class, () -> GetPublicKeyResponse.Default());
  public static dafny.TypeDescriptor<GetPublicKeyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetPublicKeyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetPublicKeyResponse theDefault = GetPublicKeyResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PublicKeyType._typeDescriptor()), Wrappers_Compile.Option.<CustomerMasterKeySpec>Default(CustomerMasterKeySpec._typeDescriptor()), Wrappers_Compile.Option.<KeySpec>Default(KeySpec._typeDescriptor()), Wrappers_Compile.Option.<KeyUsageType>Default(KeyUsageType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>>Default(dafny.DafnySequence.<EncryptionAlgorithmSpec>_typeDescriptor(EncryptionAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends SigningAlgorithmSpec>>Default(dafny.DafnySequence.<SigningAlgorithmSpec>_typeDescriptor(SigningAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>>Default(dafny.DafnySequence.<KeyAgreementAlgorithmSpec>_typeDescriptor(KeyAgreementAlgorithmSpec._typeDescriptor())));
  public static GetPublicKeyResponse Default() {
    return theDefault;
  }
  public static GetPublicKeyResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms) {
    return new GetPublicKeyResponse(KeyId, PublicKey, CustomerMasterKeySpec, KeySpec, KeyUsage, EncryptionAlgorithms, SigningAlgorithms, KeyAgreementAlgorithms);
  }
  public static GetPublicKeyResponse create_GetPublicKeyResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms) {
    return create(KeyId, PublicKey, CustomerMasterKeySpec, KeySpec, KeyUsage, EncryptionAlgorithms, SigningAlgorithms, KeyAgreementAlgorithms);
  }
  public boolean is_GetPublicKeyResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PublicKey() {
    return this._PublicKey;
  }
  public Wrappers_Compile.Option<CustomerMasterKeySpec> dtor_CustomerMasterKeySpec() {
    return this._CustomerMasterKeySpec;
  }
  public Wrappers_Compile.Option<KeySpec> dtor_KeySpec() {
    return this._KeySpec;
  }
  public Wrappers_Compile.Option<KeyUsageType> dtor_KeyUsage() {
    return this._KeyUsage;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> dtor_EncryptionAlgorithms() {
    return this._EncryptionAlgorithms;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> dtor_SigningAlgorithms() {
    return this._SigningAlgorithms;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> dtor_KeyAgreementAlgorithms() {
    return this._KeyAgreementAlgorithms;
  }
}
