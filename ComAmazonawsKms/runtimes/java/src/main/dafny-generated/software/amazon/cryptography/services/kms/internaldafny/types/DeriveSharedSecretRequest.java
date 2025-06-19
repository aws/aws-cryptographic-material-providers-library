// Class DeriveSharedSecretRequest
// Dafny class DeriveSharedSecretRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeriveSharedSecretRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public KeyAgreementAlgorithmSpec _KeyAgreementAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _PublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public Wrappers_Compile.Option<RecipientInfo> _Recipient;
  public DeriveSharedSecretRequest (dafny.DafnySequence<? extends Character> KeyId, KeyAgreementAlgorithmSpec KeyAgreementAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    this._KeyId = KeyId;
    this._KeyAgreementAlgorithm = KeyAgreementAlgorithm;
    this._PublicKey = PublicKey;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
    this._Recipient = Recipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeriveSharedSecretRequest o = (DeriveSharedSecretRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._KeyAgreementAlgorithm, o._KeyAgreementAlgorithm) && java.util.Objects.equals(this._PublicKey, o._PublicKey) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun) && java.util.Objects.equals(this._Recipient, o._Recipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Recipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DeriveSharedSecretRequest.DeriveSharedSecretRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyAgreementAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Recipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeriveSharedSecretRequest> _TYPE = dafny.TypeDescriptor.<DeriveSharedSecretRequest>referenceWithInitializer(DeriveSharedSecretRequest.class, () -> DeriveSharedSecretRequest.Default());
  public static dafny.TypeDescriptor<DeriveSharedSecretRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeriveSharedSecretRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeriveSharedSecretRequest theDefault = DeriveSharedSecretRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), KeyAgreementAlgorithmSpec.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<RecipientInfo>Default(RecipientInfo._typeDescriptor()));
  public static DeriveSharedSecretRequest Default() {
    return theDefault;
  }
  public static DeriveSharedSecretRequest create(dafny.DafnySequence<? extends Character> KeyId, KeyAgreementAlgorithmSpec KeyAgreementAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    return new DeriveSharedSecretRequest(KeyId, KeyAgreementAlgorithm, PublicKey, GrantTokens, DryRun, Recipient);
  }
  public static DeriveSharedSecretRequest create_DeriveSharedSecretRequest(dafny.DafnySequence<? extends Character> KeyId, KeyAgreementAlgorithmSpec KeyAgreementAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    return create(KeyId, KeyAgreementAlgorithm, PublicKey, GrantTokens, DryRun, Recipient);
  }
  public boolean is_DeriveSharedSecretRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public KeyAgreementAlgorithmSpec dtor_KeyAgreementAlgorithm() {
    return this._KeyAgreementAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_PublicKey() {
    return this._PublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
  public Wrappers_Compile.Option<RecipientInfo> dtor_Recipient() {
    return this._Recipient;
  }
}
