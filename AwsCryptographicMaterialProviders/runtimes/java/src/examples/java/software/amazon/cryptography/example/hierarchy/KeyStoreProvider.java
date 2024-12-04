package software.amazon.cryptography.example.hierarchy;

import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.MRDiscovery;

public class KeyStoreProvider {

  public static KeyStore keyStore() {
    return KeyStore
      .builder()
      .KeyStoreConfig(
        KeyStoreConfig
          .builder()
          .ddbClient(Fixtures.ddbClientWest2)
          .ddbTableName(Fixtures.TEST_KEYSTORE_NAME)
          .logicalKeyStoreName(Fixtures.TEST_LOGICAL_KEYSTORE_NAME)
          .kmsClient(Fixtures.kmsClientWest2)
          .kmsConfiguration(
            KMSConfiguration
              .builder()
              .mrDiscovery(MRDiscovery.builder().region("us-west-2").build())
              .build()
          )
          .build()
      )
      .build();
  }
}
