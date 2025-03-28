// Class DecryptMaterialsInput
// Dafny class DecryptMaterialsInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptMaterialsInput {
  public AlgorithmSuiteId _algorithmSuiteId;
  public CommitmentPolicy _commitmentPolicy;
  public dafny.DafnySequence<? extends EncryptedDataKey> _encryptedDataKeys;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _reproducedEncryptionContext;
  public DecryptMaterialsInput (AlgorithmSuiteId algorithmSuiteId, CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    this._algorithmSuiteId = algorithmSuiteId;
    this._commitmentPolicy = commitmentPolicy;
    this._encryptedDataKeys = encryptedDataKeys;
    this._encryptionContext = encryptionContext;
    this._reproducedEncryptionContext = reproducedEncryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptMaterialsInput o = (DecryptMaterialsInput)other;
    return true && java.util.Objects.equals(this._algorithmSuiteId, o._algorithmSuiteId) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._reproducedEncryptionContext, o._reproducedEncryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuiteId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._reproducedEncryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput.DecryptMaterialsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithmSuiteId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitmentPolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptedDataKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._reproducedEncryptionContext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptMaterialsInput> _TYPE = dafny.TypeDescriptor.<DecryptMaterialsInput>referenceWithInitializer(DecryptMaterialsInput.class, () -> DecryptMaterialsInput.Default());
  public static dafny.TypeDescriptor<DecryptMaterialsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptMaterialsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptMaterialsInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput.create(AlgorithmSuiteId.Default(), CommitmentPolicy.Default(), dafny.DafnySequence.<EncryptedDataKey> empty(EncryptedDataKey._typeDescriptor()), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor())));
  public static DecryptMaterialsInput Default() {
    return theDefault;
  }
  public static DecryptMaterialsInput create(AlgorithmSuiteId algorithmSuiteId, CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    return new DecryptMaterialsInput(algorithmSuiteId, commitmentPolicy, encryptedDataKeys, encryptionContext, reproducedEncryptionContext);
  }
  public static DecryptMaterialsInput create_DecryptMaterialsInput(AlgorithmSuiteId algorithmSuiteId, CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    return create(algorithmSuiteId, commitmentPolicy, encryptedDataKeys, encryptionContext, reproducedEncryptionContext);
  }
  public boolean is_DecryptMaterialsInput() { return true; }
  public AlgorithmSuiteId dtor_algorithmSuiteId() {
    return this._algorithmSuiteId;
  }
  public CommitmentPolicy dtor_commitmentPolicy() {
    return this._commitmentPolicy;
  }
  public dafny.DafnySequence<? extends EncryptedDataKey> dtor_encryptedDataKeys() {
    return this._encryptedDataKeys;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_reproducedEncryptionContext() {
    return this._reproducedEncryptionContext;
  }
}
