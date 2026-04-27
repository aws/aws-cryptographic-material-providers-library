// Class DecryptTestVector_PositiveDecryptKeyringTest
// Dafny class DecryptTestVector_PositiveDecryptKeyringTest compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptTestVector_PositiveDecryptKeyringTest extends DecryptTestVector {
  public dafny.DafnySequence<? extends Character> _name;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _commitmentPolicy;
  public dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _encryptedDataKeys;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _keyDescription;
  public DecryptResult _expectedResult;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _description;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _reproducedEncryptionContext;
  public DecryptTestVector_PositiveDecryptKeyringTest (dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription, DecryptResult expectedResult, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    super();
    this._name = name;
    this._algorithmSuite = algorithmSuite;
    this._commitmentPolicy = commitmentPolicy;
    this._encryptedDataKeys = encryptedDataKeys;
    this._encryptionContext = encryptionContext;
    this._keyDescription = keyDescription;
    this._expectedResult = expectedResult;
    this._description = description;
    this._reproducedEncryptionContext = reproducedEncryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptTestVector_PositiveDecryptKeyringTest o = (DecryptTestVector_PositiveDecryptKeyringTest)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._keyDescription, o._keyDescription) && java.util.Objects.equals(this._expectedResult, o._expectedResult) && java.util.Objects.equals(this._description, o._description) && java.util.Objects.equals(this._reproducedEncryptionContext, o._reproducedEncryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._expectedResult);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._reproducedEncryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestVectors.DecryptTestVector.PositiveDecryptKeyringTest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitmentPolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptedDataKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._expectedResult));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._reproducedEncryptionContext));
    s.append(")");
    return s.toString();
  }
}
