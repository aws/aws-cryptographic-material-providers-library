// Class InitializeDecryptionMaterialsInput
// Dafny class InitializeDecryptionMaterialsInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class InitializeDecryptionMaterialsInput {
  public AlgorithmSuiteId _algorithmSuiteId;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public InitializeDecryptionMaterialsInput (AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    this._algorithmSuiteId = algorithmSuiteId;
    this._encryptionContext = encryptionContext;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InitializeDecryptionMaterialsInput o = (InitializeDecryptionMaterialsInput)other;
    return true && java.util.Objects.equals(this._algorithmSuiteId, o._algorithmSuiteId) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuiteId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput.InitializeDecryptionMaterialsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithmSuiteId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<InitializeDecryptionMaterialsInput> _TYPE = dafny.TypeDescriptor.<InitializeDecryptionMaterialsInput>referenceWithInitializer(InitializeDecryptionMaterialsInput.class, () -> InitializeDecryptionMaterialsInput.Default());
  public static dafny.TypeDescriptor<InitializeDecryptionMaterialsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<InitializeDecryptionMaterialsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final InitializeDecryptionMaterialsInput theDefault = InitializeDecryptionMaterialsInput.create(AlgorithmSuiteId.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()));
  public static InitializeDecryptionMaterialsInput Default() {
    return theDefault;
  }
  public static InitializeDecryptionMaterialsInput create(AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return new InitializeDecryptionMaterialsInput(algorithmSuiteId, encryptionContext, requiredEncryptionContextKeys);
  }
  public static InitializeDecryptionMaterialsInput create_InitializeDecryptionMaterialsInput(AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return create(algorithmSuiteId, encryptionContext, requiredEncryptionContextKeys);
  }
  public boolean is_InitializeDecryptionMaterialsInput() { return true; }
  public AlgorithmSuiteId dtor_algorithmSuiteId() {
    return this._algorithmSuiteId;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
}
