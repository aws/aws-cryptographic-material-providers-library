// Class Config
// Dafny class Config compiled into Java
package AwsCryptographyKeyStoreOperations_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Config {
  public dafny.DafnySequence<? extends Character> _id;
  public dafny.DafnySequence<? extends Character> _ddbTableName;
  public dafny.DafnySequence<? extends Character> _logicalKeyStoreName;
  public software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration _kmsConfiguration;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _kmsClient;
  public software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _ddbClient;
  public Config (dafny.DafnySequence<? extends Character> id, dafny.DafnySequence<? extends Character> ddbTableName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient) {
    this._id = id;
    this._ddbTableName = ddbTableName;
    this._logicalKeyStoreName = logicalKeyStoreName;
    this._kmsConfiguration = kmsConfiguration;
    this._grantTokens = grantTokens;
    this._kmsClient = kmsClient;
    this._ddbClient = ddbClient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Config o = (Config)other;
    return true && java.util.Objects.equals(this._id, o._id) && java.util.Objects.equals(this._ddbTableName, o._ddbTableName) && java.util.Objects.equals(this._logicalKeyStoreName, o._logicalKeyStoreName) && java.util.Objects.equals(this._kmsConfiguration, o._kmsConfiguration) && java.util.Objects.equals(this._grantTokens, o._grantTokens) && this._kmsClient == o._kmsClient && this._ddbClient == o._ddbClient;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._id);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ddbTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._logicalKeyStoreName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsConfiguration);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ddbClient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreOperations.Config.Config");
    s.append("(");
    s.append(dafny.Helpers.toString(this._id));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ddbTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._logicalKeyStoreName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsConfiguration));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ddbClient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Config> _TYPE = dafny.TypeDescriptor.<Config>referenceWithInitializer(Config.class, () -> Config.Default());
  public static dafny.TypeDescriptor<Config> _typeDescriptor() {
    return (dafny.TypeDescriptor<Config>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Config theDefault = Config.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.Default(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor()), null, null);
  public static Config Default() {
    return theDefault;
  }
  public static Config create(dafny.DafnySequence<? extends Character> id, dafny.DafnySequence<? extends Character> ddbTableName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient) {
    return new Config(id, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient);
  }
  public static Config create_Config(dafny.DafnySequence<? extends Character> id, dafny.DafnySequence<? extends Character> ddbTableName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient) {
    return create(id, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient);
  }
  public boolean is_Config() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_id() {
    return this._id;
  }
  public dafny.DafnySequence<? extends Character> dtor_ddbTableName() {
    return this._ddbTableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_logicalKeyStoreName() {
    return this._logicalKeyStoreName;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration dtor_kmsConfiguration() {
    return this._kmsConfiguration;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_grantTokens() {
    return this._grantTokens;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient dtor_kmsClient() {
    return this._kmsClient;
  }
  public software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient dtor_ddbClient() {
    return this._ddbClient;
  }
}
