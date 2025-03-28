// Class InitializeEncryptionMaterialsInput
// Dafny class InitializeEncryptionMaterialsInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class InitializeEncryptionMaterialsInput {
  public AlgorithmSuiteId _algorithmSuiteId;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _signingKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _verificationKey;
  public InitializeEncryptionMaterialsInput (AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey) {
    this._algorithmSuiteId = algorithmSuiteId;
    this._encryptionContext = encryptionContext;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
    this._signingKey = signingKey;
    this._verificationKey = verificationKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InitializeEncryptionMaterialsInput o = (InitializeEncryptionMaterialsInput)other;
    return true && java.util.Objects.equals(this._algorithmSuiteId, o._algorithmSuiteId) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys) && java.util.Objects.equals(this._signingKey, o._signingKey) && java.util.Objects.equals(this._verificationKey, o._verificationKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuiteId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput.InitializeEncryptionMaterialsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithmSuiteId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<InitializeEncryptionMaterialsInput> _TYPE = dafny.TypeDescriptor.<InitializeEncryptionMaterialsInput>referenceWithInitializer(InitializeEncryptionMaterialsInput.class, () -> InitializeEncryptionMaterialsInput.Default());
  public static dafny.TypeDescriptor<InitializeEncryptionMaterialsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<InitializeEncryptionMaterialsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final InitializeEncryptionMaterialsInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(AlgorithmSuiteId.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
  public static InitializeEncryptionMaterialsInput Default() {
    return theDefault;
  }
  public static InitializeEncryptionMaterialsInput create(AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey) {
    return new InitializeEncryptionMaterialsInput(algorithmSuiteId, encryptionContext, requiredEncryptionContextKeys, signingKey, verificationKey);
  }
  public static InitializeEncryptionMaterialsInput create_InitializeEncryptionMaterialsInput(AlgorithmSuiteId algorithmSuiteId, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey) {
    return create(algorithmSuiteId, encryptionContext, requiredEncryptionContextKeys, signingKey, verificationKey);
  }
  public boolean is_InitializeEncryptionMaterialsInput() { return true; }
  public AlgorithmSuiteId dtor_algorithmSuiteId() {
    return this._algorithmSuiteId;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_signingKey() {
    return this._signingKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_verificationKey() {
    return this._verificationKey;
  }
}
