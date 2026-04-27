// Class ReEncryptRequest
// Dafny class ReEncryptRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReEncryptRequest {
  public dafny.DafnySequence<? extends java.lang.Byte> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _SourceEncryptionContext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceKeyId;
  public dafny.DafnySequence<? extends Character> _DestinationKeyId;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _DestinationEncryptionContext;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _SourceEncryptionAlgorithm;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _DestinationEncryptionAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public ReEncryptRequest (dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> SourceEncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, dafny.DafnySequence<? extends Character> DestinationKeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> DestinationEncryptionContext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._CiphertextBlob = CiphertextBlob;
    this._SourceEncryptionContext = SourceEncryptionContext;
    this._SourceKeyId = SourceKeyId;
    this._DestinationKeyId = DestinationKeyId;
    this._DestinationEncryptionContext = DestinationEncryptionContext;
    this._SourceEncryptionAlgorithm = SourceEncryptionAlgorithm;
    this._DestinationEncryptionAlgorithm = DestinationEncryptionAlgorithm;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReEncryptRequest o = (ReEncryptRequest)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._SourceEncryptionContext, o._SourceEncryptionContext) && java.util.Objects.equals(this._SourceKeyId, o._SourceKeyId) && java.util.Objects.equals(this._DestinationKeyId, o._DestinationKeyId) && java.util.Objects.equals(this._DestinationEncryptionContext, o._DestinationEncryptionContext) && java.util.Objects.equals(this._SourceEncryptionAlgorithm, o._SourceEncryptionAlgorithm) && java.util.Objects.equals(this._DestinationEncryptionAlgorithm, o._DestinationEncryptionAlgorithm) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceEncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationEncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceEncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationEncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ReEncryptRequest.ReEncryptRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceEncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationEncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceEncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationEncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReEncryptRequest> _TYPE = dafny.TypeDescriptor.<ReEncryptRequest>referenceWithInitializer(ReEncryptRequest.class, () -> ReEncryptRequest.Default());
  public static dafny.TypeDescriptor<ReEncryptRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReEncryptRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReEncryptRequest theDefault = ReEncryptRequest.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ReEncryptRequest Default() {
    return theDefault;
  }
  public static ReEncryptRequest create(dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> SourceEncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, dafny.DafnySequence<? extends Character> DestinationKeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> DestinationEncryptionContext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new ReEncryptRequest(CiphertextBlob, SourceEncryptionContext, SourceKeyId, DestinationKeyId, DestinationEncryptionContext, SourceEncryptionAlgorithm, DestinationEncryptionAlgorithm, GrantTokens, DryRun);
  }
  public static ReEncryptRequest create_ReEncryptRequest(dafny.DafnySequence<? extends java.lang.Byte> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> SourceEncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, dafny.DafnySequence<? extends Character> DestinationKeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> DestinationEncryptionContext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(CiphertextBlob, SourceEncryptionContext, SourceKeyId, DestinationKeyId, DestinationEncryptionContext, SourceEncryptionAlgorithm, DestinationEncryptionAlgorithm, GrantTokens, DryRun);
  }
  public boolean is_ReEncryptRequest() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_SourceEncryptionContext() {
    return this._SourceEncryptionContext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceKeyId() {
    return this._SourceKeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_DestinationKeyId() {
    return this._DestinationKeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_DestinationEncryptionContext() {
    return this._DestinationEncryptionContext;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_SourceEncryptionAlgorithm() {
    return this._SourceEncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_DestinationEncryptionAlgorithm() {
    return this._DestinationEncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
