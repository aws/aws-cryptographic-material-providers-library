package software.amazon.cryptography.example.hierarchy;

import java.util.List;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.ClientProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.Discovery;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;

public class KeyStoreProvider {
  public static KeyStore DiscoveryKeyStore(
    @Nonnull final String physicalName,
    @Nonnull final String logicalName,
    @Nullable final List<String> grantTokens,
    @Nullable KmsClient kmsClient,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    KMSConfiguration kmsConfig = KMSConfiguration.builder()
      .discovery(Discovery.builder().build())
      .build();
    KeyStoreConfig.Builder builder = KeyStoreConfig(
      physicalName, logicalName, grantTokens, kmsClient, dynamoDbClient);
    return buildIt(builder, kmsConfig);
  }

  public static KeyStore StrictKeyStore(
    @Nonnull final String kmsArn,
    @Nonnull final String physicalName,
    @Nonnull final String logicalName,
    @Nullable final List<String> grantTokens,
    @Nullable KmsClient kmsClient,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    KMSConfiguration kmsConfig = KMSConfiguration.builder()
      .kmsMRKeyArn(kmsArn)
      .build();
    KeyStoreConfig.Builder builder = KeyStoreConfig(
      physicalName, logicalName, grantTokens, kmsClient, dynamoDbClient);
    return buildIt(builder, kmsConfig);
  }

  private static KeyStoreConfig.Builder KeyStoreConfig(
    @Nonnull final String physicalName,
    @Nonnull final String logicalName,
    @Nullable final List<String> grantTokens,
    @Nullable KmsClient kmsClient,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    kmsClient = ClientProvider.kms(kmsClient);
    dynamoDbClient = ClientProvider.dynamoDB(dynamoDbClient);
    KeyStoreConfig.Builder builder = KeyStoreConfig.builder()
      .ddbTableName(physicalName)
      .logicalKeyStoreName(logicalName)
      .ddbClient(dynamoDbClient)
      .kmsClient(kmsClient);
    if (grantTokens != null && !grantTokens.isEmpty()) {
      builder.grantTokens(grantTokens);
    }
    return builder;
  }

  private static KeyStore buildIt(
    KeyStoreConfig.Builder builder,
    KMSConfiguration kmsConfig
    ) {
    return KeyStore.builder()
      .KeyStoreConfig(
        builder.kmsConfiguration(kmsConfig).build())
      .build();
  }
}
