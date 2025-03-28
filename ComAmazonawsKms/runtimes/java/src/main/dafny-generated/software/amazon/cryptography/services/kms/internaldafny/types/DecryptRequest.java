// Class DecryptRequest
// Dafny class DecryptRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptRequest {
  public dafny.DafnySequence<? extends java.lang.Byte> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _EncryptionAlgorithm;
  public Wrappers_Compile.Option<RecipientInfo> _Recipient;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public DecryptRequest (dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<RecipientInfo> Recipient, Wrappers_Compile.Option<Boolean> DryRun) {
    this._CiphertextBlob = CiphertextBlob;
    this._EncryptionContext = EncryptionContext;
    this._GrantTokens = GrantTokens;
    this._KeyId = KeyId;
    this._EncryptionAlgorithm = EncryptionAlgorithm;
    this._Recipient = Recipient;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptRequest o = (DecryptRequest)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._EncryptionContext, o._EncryptionContext) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._EncryptionAlgorithm, o._EncryptionAlgorithm) && java.util.Objects.equals(this._Recipient, o._Recipient) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Recipient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DecryptRequest.DecryptRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Recipient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptRequest> _TYPE = dafny.TypeDescriptor.<DecryptRequest>referenceWithInitializer(DecryptRequest.class, () -> DecryptRequest.Default());
  public static dafny.TypeDescriptor<DecryptRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<RecipientInfo>Default(RecipientInfo._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static DecryptRequest Default() {
    return theDefault;
  }
  public static DecryptRequest create(dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<RecipientInfo> Recipient, Wrappers_Compile.Option<Boolean> DryRun) {
    return new DecryptRequest(CiphertextBlob, EncryptionContext, GrantTokens, KeyId, EncryptionAlgorithm, Recipient, DryRun);
  }
  public static DecryptRequest create_DecryptRequest(dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<RecipientInfo> Recipient, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(CiphertextBlob, EncryptionContext, GrantTokens, KeyId, EncryptionAlgorithm, Recipient, DryRun);
  }
  public boolean is_DecryptRequest() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContext() {
    return this._EncryptionContext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_EncryptionAlgorithm() {
    return this._EncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<RecipientInfo> dtor_Recipient() {
    return this._Recipient;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
