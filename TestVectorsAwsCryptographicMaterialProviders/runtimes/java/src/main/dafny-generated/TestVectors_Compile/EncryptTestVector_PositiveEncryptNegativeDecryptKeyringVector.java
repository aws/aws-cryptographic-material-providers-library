// Class EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector
// Dafny class EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector extends EncryptTestVector {
  public dafny.DafnySequence<? extends Character> _name;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _description;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _commitmentPolicy;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public Wrappers_Compile.Option<java.lang.Long> _maxPlaintextLength;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _requiredEncryptionContextKeys;
  public dafny.DafnySequence<? extends Character> _decryptErrorDescription;
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _encryptDescription;
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _decryptDescription;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _reproducedEncryptionContext;
  public EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector (dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> description, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, Wrappers_Compile.Option<java.lang.Long> maxPlaintextLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys, dafny.DafnySequence<? extends Character> decryptErrorDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription encryptDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription decryptDescription, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> reproducedEncryptionContext) {
    super();
    this._name = name;
    this._description = description;
    this._encryptionContext = encryptionContext;
    this._commitmentPolicy = commitmentPolicy;
    this._algorithmSuite = algorithmSuite;
    this._maxPlaintextLength = maxPlaintextLength;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
    this._decryptErrorDescription = decryptErrorDescription;
    this._encryptDescription = encryptDescription;
    this._decryptDescription = decryptDescription;
    this._reproducedEncryptionContext = reproducedEncryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector o = (EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._description, o._description) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._maxPlaintextLength, o._maxPlaintextLength) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys) && java.util.Objects.equals(this._decryptErrorDescription, o._decryptErrorDescription) && java.util.Objects.equals(this._encryptDescription, o._encryptDescription) && java.util.Objects.equals(this._decryptDescription, o._decryptDescription) && java.util.Objects.equals(this._reproducedEncryptionContext, o._reproducedEncryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._maxPlaintextLength);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._decryptErrorDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._decryptDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._reproducedEncryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestVectors.EncryptTestVector.PositiveEncryptNegativeDecryptKeyringVector");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitmentPolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._maxPlaintextLength));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._decryptErrorDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._decryptDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._reproducedEncryptionContext));
    s.append(")");
    return s.toString();
  }
}
