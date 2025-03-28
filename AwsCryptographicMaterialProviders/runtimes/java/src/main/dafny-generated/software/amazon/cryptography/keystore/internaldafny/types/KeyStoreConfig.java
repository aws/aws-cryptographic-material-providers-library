// Class KeyStoreConfig
// Dafny class KeyStoreConfig compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyStoreConfig {
  public dafny.DafnySequence<? extends Character> _ddbTableName;
  public KMSConfiguration _kmsConfiguration;
  public dafny.DafnySequence<? extends Character> _logicalKeyStoreName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _id;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> _ddbClient;
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> _kmsClient;
  public KeyStoreConfig (dafny.DafnySequence<? extends Character> ddbTableName, KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends Character> logicalKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> id, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ddbClient, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient) {
    this._ddbTableName = ddbTableName;
    this._kmsConfiguration = kmsConfiguration;
    this._logicalKeyStoreName = logicalKeyStoreName;
    this._id = id;
    this._grantTokens = grantTokens;
    this._ddbClient = ddbClient;
    this._kmsClient = kmsClient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyStoreConfig o = (KeyStoreConfig)other;
    return true && java.util.Objects.equals(this._ddbTableName, o._ddbTableName) && java.util.Objects.equals(this._kmsConfiguration, o._kmsConfiguration) && java.util.Objects.equals(this._logicalKeyStoreName, o._logicalKeyStoreName) && java.util.Objects.equals(this._id, o._id) && java.util.Objects.equals(this._grantTokens, o._grantTokens) && java.util.Objects.equals(this._ddbClient, o._ddbClient) && java.util.Objects.equals(this._kmsClient, o._kmsClient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ddbTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsConfiguration);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._logicalKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._id);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ddbClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.KeyStoreConfig.KeyStoreConfig");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ddbTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsConfiguration));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._logicalKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._id));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ddbClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyStoreConfig> _TYPE = dafny.TypeDescriptor.<KeyStoreConfig>referenceWithInitializer(KeyStoreConfig.class, () -> KeyStoreConfig.Default());
  public static dafny.TypeDescriptor<KeyStoreConfig> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyStoreConfig>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyStoreConfig theDefault = software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), KMSConfiguration.Default(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>Default(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class))), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>Default(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))));
  public static KeyStoreConfig Default() {
    return theDefault;
  }
  public static KeyStoreConfig create(dafny.DafnySequence<? extends Character> ddbTableName, KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends Character> logicalKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> id, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ddbClient, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient) {
    return new KeyStoreConfig(ddbTableName, kmsConfiguration, logicalKeyStoreName, id, grantTokens, ddbClient, kmsClient);
  }
  public static KeyStoreConfig create_KeyStoreConfig(dafny.DafnySequence<? extends Character> ddbTableName, KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends Character> logicalKeyStoreName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> id, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ddbClient, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient) {
    return create(ddbTableName, kmsConfiguration, logicalKeyStoreName, id, grantTokens, ddbClient, kmsClient);
  }
  public boolean is_KeyStoreConfig() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ddbTableName() {
    return this._ddbTableName;
  }
  public KMSConfiguration dtor_kmsConfiguration() {
    return this._kmsConfiguration;
  }
  public dafny.DafnySequence<? extends Character> dtor_logicalKeyStoreName() {
    return this._logicalKeyStoreName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_id() {
    return this._id;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> dtor_ddbClient() {
    return this._ddbClient;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> dtor_kmsClient() {
    return this._kmsClient;
  }
}
