// Class GenerateDataKeyWithoutPlaintextRequest
// Dafny class GenerateDataKeyWithoutPlaintextRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyWithoutPlaintextRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _EncryptionContext;
  public Wrappers_Compile.Option<DataKeySpec> _KeySpec;
  public Wrappers_Compile.Option<java.lang.Integer> _NumberOfBytes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public GenerateDataKeyWithoutPlaintextRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<DataKeySpec> KeySpec, Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._EncryptionContext = EncryptionContext;
    this._KeySpec = KeySpec;
    this._NumberOfBytes = NumberOfBytes;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyWithoutPlaintextRequest o = (GenerateDataKeyWithoutPlaintextRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._EncryptionContext, o._EncryptionContext) && java.util.Objects.equals(this._KeySpec, o._KeySpec) && java.util.Objects.equals(this._NumberOfBytes, o._NumberOfBytes) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NumberOfBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest.GenerateDataKeyWithoutPlaintextRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NumberOfBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextRequest> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyWithoutPlaintextRequest>referenceWithInitializer(GenerateDataKeyWithoutPlaintextRequest.class, () -> GenerateDataKeyWithoutPlaintextRequest.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyWithoutPlaintextRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<DataKeySpec>Default(DataKeySpec._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(NumberOfBytesType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static GenerateDataKeyWithoutPlaintextRequest Default() {
    return theDefault;
  }
  public static GenerateDataKeyWithoutPlaintextRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<DataKeySpec> KeySpec, Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new GenerateDataKeyWithoutPlaintextRequest(KeyId, EncryptionContext, KeySpec, NumberOfBytes, GrantTokens, DryRun);
  }
  public static GenerateDataKeyWithoutPlaintextRequest create_GenerateDataKeyWithoutPlaintextRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> EncryptionContext, Wrappers_Compile.Option<DataKeySpec> KeySpec, Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, EncryptionContext, KeySpec, NumberOfBytes, GrantTokens, DryRun);
  }
  public boolean is_GenerateDataKeyWithoutPlaintextRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_EncryptionContext() {
    return this._EncryptionContext;
  }
  public Wrappers_Compile.Option<DataKeySpec> dtor_KeySpec() {
    return this._KeySpec;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_NumberOfBytes() {
    return this._NumberOfBytes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
