// Class GetKeyStoreInfoOutput
// Dafny class GetKeyStoreInfoOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyStoreInfoOutput {
  public dafny.DafnySequence<? extends Character> _keyStoreId;
  public dafny.DafnySequence<? extends Character> _keyStoreName;
  public dafny.DafnySequence<? extends Character> _logicalKeyStoreName;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public KMSConfiguration _kmsConfiguration;
  public GetKeyStoreInfoOutput (dafny.DafnySequence<? extends Character> keyStoreId, dafny.DafnySequence<? extends Character> keyStoreName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, KMSConfiguration kmsConfiguration) {
    this._keyStoreId = keyStoreId;
    this._keyStoreName = keyStoreName;
    this._logicalKeyStoreName = logicalKeyStoreName;
    this._grantTokens = grantTokens;
    this._kmsConfiguration = kmsConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyStoreInfoOutput o = (GetKeyStoreInfoOutput)other;
    return true && java.util.Objects.equals(this._keyStoreId, o._keyStoreId) && java.util.Objects.equals(this._keyStoreName, o._keyStoreName) && java.util.Objects.equals(this._logicalKeyStoreName, o._logicalKeyStoreName) && java.util.Objects.equals(this._grantTokens, o._grantTokens) && java.util.Objects.equals(this._kmsConfiguration, o._kmsConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._logicalKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput.GetKeyStoreInfoOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._logicalKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyStoreInfoOutput> _TYPE = dafny.TypeDescriptor.<GetKeyStoreInfoOutput>referenceWithInitializer(GetKeyStoreInfoOutput.class, () -> GetKeyStoreInfoOutput.Default());
  public static dafny.TypeDescriptor<GetKeyStoreInfoOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyStoreInfoOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyStoreInfoOutput theDefault = GetKeyStoreInfoOutput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), KMSConfiguration.Default());
  public static GetKeyStoreInfoOutput Default() {
    return theDefault;
  }
  public static GetKeyStoreInfoOutput create(dafny.DafnySequence<? extends Character> keyStoreId, dafny.DafnySequence<? extends Character> keyStoreName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, KMSConfiguration kmsConfiguration) {
    return new GetKeyStoreInfoOutput(keyStoreId, keyStoreName, logicalKeyStoreName, grantTokens, kmsConfiguration);
  }
  public static GetKeyStoreInfoOutput create_GetKeyStoreInfoOutput(dafny.DafnySequence<? extends Character> keyStoreId, dafny.DafnySequence<? extends Character> keyStoreName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, KMSConfiguration kmsConfiguration) {
    return create(keyStoreId, keyStoreName, logicalKeyStoreName, grantTokens, kmsConfiguration);
  }
  public boolean is_GetKeyStoreInfoOutput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyStoreId() {
    return this._keyStoreId;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyStoreName() {
    return this._keyStoreName;
  }
  public dafny.DafnySequence<? extends Character> dtor_logicalKeyStoreName() {
    return this._logicalKeyStoreName;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_grantTokens() {
    return this._grantTokens;
  }
  public KMSConfiguration dtor_kmsConfiguration() {
    return this._kmsConfiguration;
  }
}
