// Class EncryptRequest
// Dafny class EncryptRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends java.lang.Byte> _Plaintext;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _EncryptionAlgorithm;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public EncryptRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Plaintext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._Plaintext = Plaintext;
    this._EncryptionContext = EncryptionContext;
    this._GrantTokens = GrantTokens;
    this._EncryptionAlgorithm = EncryptionAlgorithm;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptRequest o = (EncryptRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Plaintext, o._Plaintext) && java.util.Objects.equals(this._EncryptionContext, o._EncryptionContext) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._EncryptionAlgorithm, o._EncryptionAlgorithm) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Plaintext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.EncryptRequest.EncryptRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Plaintext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EncryptRequest> _TYPE = dafny.TypeDescriptor.<EncryptRequest>referenceWithInitializer(EncryptRequest.class, () -> EncryptRequest.Default());
  public static dafny.TypeDescriptor<EncryptRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static EncryptRequest Default() {
    return theDefault;
  }
  public static EncryptRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Plaintext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    return new EncryptRequest(KeyId, Plaintext, EncryptionContext, GrantTokens, EncryptionAlgorithm, DryRun);
  }
  public static EncryptRequest create_EncryptRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Plaintext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, Plaintext, EncryptionContext, GrantTokens, EncryptionAlgorithm, DryRun);
  }
  public boolean is_EncryptRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Plaintext() {
    return this._Plaintext;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContext() {
    return this._EncryptionContext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_EncryptionAlgorithm() {
    return this._EncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
