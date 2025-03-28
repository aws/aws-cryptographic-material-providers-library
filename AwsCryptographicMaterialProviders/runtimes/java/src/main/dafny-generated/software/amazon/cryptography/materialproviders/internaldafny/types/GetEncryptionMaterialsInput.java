// Class GetEncryptionMaterialsInput
// Dafny class GetEncryptionMaterialsInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetEncryptionMaterialsInput {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public CommitmentPolicy _commitmentPolicy;
  public Wrappers_Compile.Option<AlgorithmSuiteId> _algorithmSuiteId;
  public Wrappers_Compile.Option<java.lang.Long> _maxPlaintextLength;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _requiredEncryptionContextKeys;
  public GetEncryptionMaterialsInput (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, CommitmentPolicy commitmentPolicy, Wrappers_Compile.Option<AlgorithmSuiteId> algorithmSuiteId, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys) {
    this._encryptionContext = encryptionContext;
    this._commitmentPolicy = commitmentPolicy;
    this._algorithmSuiteId = algorithmSuiteId;
    this._maxPlaintextLength = maxPlaintextLength;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetEncryptionMaterialsInput o = (GetEncryptionMaterialsInput)other;
    return true && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy) && java.util.Objects.equals(this._algorithmSuiteId, o._algorithmSuiteId) && java.util.Objects.equals(this._maxPlaintextLength, o._maxPlaintextLength) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuiteId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._maxPlaintextLength);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput.GetEncryptionMaterialsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitmentPolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuiteId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._maxPlaintextLength));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetEncryptionMaterialsInput> _TYPE = dafny.TypeDescriptor.<GetEncryptionMaterialsInput>referenceWithInitializer(GetEncryptionMaterialsInput.class, () -> GetEncryptionMaterialsInput.Default());
  public static dafny.TypeDescriptor<GetEncryptionMaterialsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetEncryptionMaterialsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetEncryptionMaterialsInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.create(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), CommitmentPolicy.Default(), Wrappers_Compile.Option.<AlgorithmSuiteId>Default(AlgorithmSuiteId._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())));
  public static GetEncryptionMaterialsInput Default() {
    return theDefault;
  }
  public static GetEncryptionMaterialsInput create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, CommitmentPolicy commitmentPolicy, Wrappers_Compile.Option<AlgorithmSuiteId> algorithmSuiteId, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys) {
    return new GetEncryptionMaterialsInput(encryptionContext, commitmentPolicy, algorithmSuiteId, maxPlaintextLength, requiredEncryptionContextKeys);
  }
  public static GetEncryptionMaterialsInput create_GetEncryptionMaterialsInput(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, CommitmentPolicy commitmentPolicy, Wrappers_Compile.Option<AlgorithmSuiteId> algorithmSuiteId, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys) {
    return create(encryptionContext, commitmentPolicy, algorithmSuiteId, maxPlaintextLength, requiredEncryptionContextKeys);
  }
  public boolean is_GetEncryptionMaterialsInput() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public CommitmentPolicy dtor_commitmentPolicy() {
    return this._commitmentPolicy;
  }
  public Wrappers_Compile.Option<AlgorithmSuiteId> dtor_algorithmSuiteId() {
    return this._algorithmSuiteId;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_maxPlaintextLength() {
    return this._maxPlaintextLength;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
}
