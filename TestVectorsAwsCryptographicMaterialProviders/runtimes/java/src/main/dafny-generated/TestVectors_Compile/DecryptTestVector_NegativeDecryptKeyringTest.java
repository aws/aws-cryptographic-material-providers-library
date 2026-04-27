// Class DecryptTestVector_NegativeDecryptKeyringTest
// Dafny class DecryptTestVector_NegativeDecryptKeyringTest compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptTestVector_NegativeDecryptKeyringTest extends DecryptTestVector {
  public dafny.DafnySequence<? extends Character> _name;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _commitmentPolicy;
  public dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _encryptedDataKeys;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends Character> _errorDescription;
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _keyDescription;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _reproducedEncryptionContext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _description;
  public DecryptTestVector_NegativeDecryptKeyringTest (dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends Character> errorDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description) {
    super();
    this._name = name;
    this._algorithmSuite = algorithmSuite;
    this._commitmentPolicy = commitmentPolicy;
    this._encryptedDataKeys = encryptedDataKeys;
    this._encryptionContext = encryptionContext;
    this._errorDescription = errorDescription;
    this._keyDescription = keyDescription;
    this._reproducedEncryptionContext = reproducedEncryptionContext;
    this._description = description;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptTestVector_NegativeDecryptKeyringTest o = (DecryptTestVector_NegativeDecryptKeyringTest)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._errorDescription, o._errorDescription) && java.util.Objects.equals(this._keyDescription, o._keyDescription) && java.util.Objects.equals(this._reproducedEncryptionContext, o._reproducedEncryptionContext) && java.util.Objects.equals(this._description, o._description);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._errorDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._reproducedEncryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestVectors.DecryptTestVector.NegativeDecryptKeyringTest");
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
    s.append(dafny.Helpers.toString(this._errorDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._reproducedEncryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._description));
    s.append(")");
    return s.toString();
  }
}
