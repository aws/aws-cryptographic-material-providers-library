// Class EncryptTestVector
// Dafny class EncryptTestVector compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class EncryptTestVector {
  public EncryptTestVector() {
  }
  private static final dafny.TypeDescriptor<EncryptTestVector> _TYPE = dafny.TypeDescriptor.<EncryptTestVector>referenceWithInitializer(EncryptTestVector.class, () -> EncryptTestVector.Default());
  public static dafny.TypeDescriptor<EncryptTestVector> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptTestVector>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptTestVector theDefault = EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.Default(), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.Default(), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.Default(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.Default(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor())));
  public static EncryptTestVector Default() {
    return theDefault;
  }
  public static EncryptTestVector create_PositiveEncryptKeyringVector(dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription encryptDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription decryptDescription, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    return new EncryptTestVector_PositiveEncryptKeyringVector(name, description, encryptionContext, commitmentPolicy, algorithmSuite, maxPlaintextLength, requiredEncryptionContextKeys, encryptDescription, decryptDescription, reproducedEncryptionContext);
  }
  public static EncryptTestVector create_PositiveEncryptNegativeDecryptKeyringVector(dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys, dafny.DafnySequence<? extends Character> decryptErrorDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription encryptDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription decryptDescription, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    return new EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(name, description, encryptionContext, commitmentPolicy, algorithmSuite, maxPlaintextLength, requiredEncryptionContextKeys, decryptErrorDescription, encryptDescription, decryptDescription, reproducedEncryptionContext);
  }
  public static EncryptTestVector create_NegativeEncryptKeyringVector(dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys, dafny.DafnySequence<? extends Character> errorDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription) {
    return new EncryptTestVector_NegativeEncryptKeyringVector(name, description, encryptionContext, commitmentPolicy, algorithmSuite, maxPlaintextLength, requiredEncryptionContextKeys, errorDescription, keyDescription);
  }
  public boolean is_PositiveEncryptKeyringVector() { return this instanceof EncryptTestVector_PositiveEncryptKeyringVector; }
  public boolean is_PositiveEncryptNegativeDecryptKeyringVector() { return this instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector; }
  public boolean is_NegativeEncryptKeyringVector() { return this instanceof EncryptTestVector_NegativeEncryptKeyringVector; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._name; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._name; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._name;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_description() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._description; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._description; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._description;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._encryptionContext; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._encryptionContext; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._encryptionContext;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy dtor_commitmentPolicy() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._commitmentPolicy; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._commitmentPolicy; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._commitmentPolicy;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo dtor_algorithmSuite() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._algorithmSuite; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._algorithmSuite; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._algorithmSuite;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_maxPlaintextLength() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._maxPlaintextLength; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._maxPlaintextLength; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._maxPlaintextLength;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_requiredEncryptionContextKeys() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._requiredEncryptionContextKeys; }
    if (d instanceof EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._requiredEncryptionContextKeys; }
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._requiredEncryptionContextKeys;
  }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription dtor_encryptDescription() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._encryptDescription; }
    return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._encryptDescription;
  }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription dtor_decryptDescription() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._decryptDescription; }
    return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._decryptDescription;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_reproducedEncryptionContext() {
    EncryptTestVector d = this;
    if (d instanceof EncryptTestVector_PositiveEncryptKeyringVector) { return ((EncryptTestVector_PositiveEncryptKeyringVector)d)._reproducedEncryptionContext; }
    return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._reproducedEncryptionContext;
  }
  public dafny.DafnySequence<? extends Character> dtor_decryptErrorDescription() {
    EncryptTestVector d = this;
    return ((EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)d)._decryptErrorDescription;
  }
  public dafny.DafnySequence<? extends Character> dtor_errorDescription() {
    EncryptTestVector d = this;
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._errorDescription;
  }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription dtor_keyDescription() {
    EncryptTestVector d = this;
    return ((EncryptTestVector_NegativeEncryptKeyringVector)d)._keyDescription;
  }
}
