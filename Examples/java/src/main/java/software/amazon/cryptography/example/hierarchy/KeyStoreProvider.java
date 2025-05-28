// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.MRDiscovery;

public class KeyStoreProvider {

  /**
   * Branch Key Store for the default test table with the default KMS Client
   * @param kmsArn If non-null, creates a strict MRK Branch Key Store;
   *               otherwise, creates a Discovery Key Store.
   */
  public static KeyStore keyStore(@Nullable String kmsArn) {
    return keyStore(kmsArn, Fixtures.kmsClientWest2);
  }

  /**
   * @param kmsArn If non-null, creates a strict MRK Branch Key Store;
   *               otherwise, creates a Discovery Key Store.
   * @param kmsClient KMS Client used by the Key Store
   */
  public static KeyStore keyStore(
    @Nullable String kmsArn,
    @Nonnull KmsClient kmsClient
  ) {
    KMSConfiguration kmsConfiguration;
    if (kmsArn != null) {
      kmsConfiguration = KMSConfiguration.builder().kmsMRKeyArn(kmsArn).build();
    } else {
      kmsConfiguration =
        KMSConfiguration
          .builder()
          .mrDiscovery(MRDiscovery.builder().region("us-west-2").build())
          .build();
    }
    return KeyStore
      .builder()
      .KeyStoreConfig(
        KeyStoreConfig
          .builder()
          .ddbClient(Fixtures.ddbClientWest2)
          .ddbTableName(Fixtures.TEST_KEYSTORE_NAME)
          .logicalKeyStoreName(Fixtures.TEST_LOGICAL_KEYSTORE_NAME)
          .kmsClient(kmsClient)
          .kmsConfiguration(kmsConfiguration)
          .build()
      )
      .build();
  }
}
