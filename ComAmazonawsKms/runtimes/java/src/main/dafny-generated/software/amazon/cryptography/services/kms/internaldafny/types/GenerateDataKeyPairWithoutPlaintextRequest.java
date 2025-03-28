// Class GenerateDataKeyPairWithoutPlaintextRequest
// Dafny class GenerateDataKeyPairWithoutPlaintextRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyPairWithoutPlaintextRequest {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContext;
  public dafny.DafnySequence<? extends Character> _KeyId;
  public DataKeyPairSpec _KeyPairSpec;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public GenerateDataKeyPairWithoutPlaintextRequest (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, dafny.DafnySequence<? extends Character> KeyId, DataKeyPairSpec KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._EncryptionContext = EncryptionContext;
    this._KeyId = KeyId;
    this._KeyPairSpec = KeyPairSpec;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyPairWithoutPlaintextRequest o = (GenerateDataKeyPairWithoutPlaintextRequest)other;
    return true && java.util.Objects.equals(this._EncryptionContext, o._EncryptionContext) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._KeyPairSpec, o._KeyPairSpec) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyPairSpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyPairWithoutPlaintextRequest.GenerateDataKeyPairWithoutPlaintextRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._EncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyPairSpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextRequest> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyPairWithoutPlaintextRequest>referenceWithInitializer(GenerateDataKeyPairWithoutPlaintextRequest.class, () -> GenerateDataKeyPairWithoutPlaintextRequest.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyPairWithoutPlaintextRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairWithoutPlaintextRequest.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), DataKeyPairSpec.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static GenerateDataKeyPairWithoutPlaintextRequest Default() {
    return theDefault;
  }
  public static GenerateDataKeyPairWithoutPlaintextRequest create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, dafny.DafnySequence<? extends Character> KeyId, DataKeyPairSpec KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new GenerateDataKeyPairWithoutPlaintextRequest(EncryptionContext, KeyId, KeyPairSpec, GrantTokens, DryRun);
  }
  public static GenerateDataKeyPairWithoutPlaintextRequest create_GenerateDataKeyPairWithoutPlaintextRequest(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, dafny.DafnySequence<? extends Character> KeyId, DataKeyPairSpec KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(EncryptionContext, KeyId, KeyPairSpec, GrantTokens, DryRun);
  }
  public boolean is_GenerateDataKeyPairWithoutPlaintextRequest() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContext() {
    return this._EncryptionContext;
  }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public DataKeyPairSpec dtor_KeyPairSpec() {
    return this._KeyPairSpec;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
