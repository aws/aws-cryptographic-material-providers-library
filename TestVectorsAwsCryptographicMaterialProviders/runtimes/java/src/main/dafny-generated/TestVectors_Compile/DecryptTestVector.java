// Class DecryptTestVector
// Dafny class DecryptTestVector compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DecryptTestVector {
  public DecryptTestVector() {
  }
  private static final dafny.TypeDescriptor<DecryptTestVector> _TYPE = dafny.TypeDescriptor.<DecryptTestVector>referenceWithInitializer(DecryptTestVector.class, () -> DecryptTestVector.Default());
  public static dafny.TypeDescriptor<DecryptTestVector> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptTestVector>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptTestVector theDefault = DecryptTestVector.create_PositiveDecryptKeyringTest(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.Default(), software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.Default(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.Default(), DecryptResult.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor())));
  public static DecryptTestVector Default() {
    return theDefault;
  }
  public static DecryptTestVector create_PositiveDecryptKeyringTest(dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription, DecryptResult expectedResult, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    return new DecryptTestVector_PositiveDecryptKeyringTest(name, algorithmSuite, commitmentPolicy, encryptedDataKeys, encryptionContext, keyDescription, expectedResult, description, reproducedEncryptionContext);
  }
  public static DecryptTestVector create_NegativeDecryptKeyringTest(dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends Character> errorDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description) {
    return new DecryptTestVector_NegativeDecryptKeyringTest(name, algorithmSuite, commitmentPolicy, encryptedDataKeys, encryptionContext, errorDescription, keyDescription, reproducedEncryptionContext, description);
  }
  public boolean is_PositiveDecryptKeyringTest() { return this instanceof DecryptTestVector_PositiveDecryptKeyringTest; }
  public boolean is_NegativeDecryptKeyringTest() { return this instanceof DecryptTestVector_NegativeDecryptKeyringTest; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._name; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._name;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo dtor_algorithmSuite() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._algorithmSuite; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._algorithmSuite;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy dtor_commitmentPolicy() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._commitmentPolicy; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._commitmentPolicy;
  }
  public dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> dtor_encryptedDataKeys() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._encryptedDataKeys; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._encryptedDataKeys;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._encryptionContext; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._encryptionContext;
  }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription dtor_keyDescription() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._keyDescription; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._keyDescription;
  }
  public DecryptResult dtor_expectedResult() {
    DecryptTestVector d = this;
    return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._expectedResult;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_description() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._description; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._description;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_reproducedEncryptionContext() {
    DecryptTestVector d = this;
    if (d instanceof DecryptTestVector_PositiveDecryptKeyringTest) { return ((DecryptTestVector_PositiveDecryptKeyringTest)d)._reproducedEncryptionContext; }
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._reproducedEncryptionContext;
  }
  public dafny.DafnySequence<? extends Character> dtor_errorDescription() {
    DecryptTestVector d = this;
    return ((DecryptTestVector_NegativeDecryptKeyringTest)d)._errorDescription;
  }
}
