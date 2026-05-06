// Class KeyMaterial_StaticMaterial
// Dafny class KeyMaterial_StaticMaterial compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_StaticMaterial extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _name;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _encryptedDataKeys;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _plaintextDataKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _signingKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _verificationKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _symmetricSigningKeys;
  public KeyMaterial_StaticMaterial (dafny.DafnySequence<? extends Character> name, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> symmetricSigningKeys) {
    super();
    this._name = name;
    this._algorithmSuite = algorithmSuite;
    this._encryptionContext = encryptionContext;
    this._encryptedDataKeys = encryptedDataKeys;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
    this._plaintextDataKey = plaintextDataKey;
    this._signingKey = signingKey;
    this._verificationKey = verificationKey;
    this._symmetricSigningKeys = symmetricSigningKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_StaticMaterial o = (KeyMaterial_StaticMaterial)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys) && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._signingKey, o._signingKey) && java.util.Objects.equals(this._verificationKey, o._verificationKey) && java.util.Objects.equals(this._symmetricSigningKeys, o._symmetricSigningKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.StaticMaterial");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptedDataKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKeys));
    s.append(")");
    return s.toString();
  }
}
