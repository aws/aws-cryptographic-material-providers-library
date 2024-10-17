// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.List;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.cmc.GuavaCMC;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.CreateAwsKmsHierarchicalKeyringInput;
import software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig;

import static software.amazon.cryptography.example.hierarchy.KeyStoreProvider.DiscoveryKeyStore;

public class KeyringProvider {
  public static final long FIVE_MINUTES_IN_SECONDS = 5 * 60;

  public static IKeyring HierarchyWithGuavaCMC(
    final String branchKeyId,
    @Nonnull final String physicalName,
    @Nonnull final String logicalName,
    @Nullable final List<String> grantTokens,
    @Nullable KmsClient kmsClient,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable String partitionId
  ) {
    final MaterialProviders mpl = MaterialProviders.builder()
      .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
      .build();
    CreateAwsKmsHierarchicalKeyringInput.Builder input = CreateAwsKmsHierarchicalKeyringInput.builder()
      .cache(GuavaCMC.create(5, 100, 1000, false))
      .branchKeyId(branchKeyId)
      .keyStore(DiscoveryKeyStore(physicalName, logicalName, grantTokens, kmsClient, dynamoDbClient))
      .ttlSeconds(FIVE_MINUTES_IN_SECONDS);
    if (partitionId != null) {
      input.partitionId(partitionId);
    }
    return mpl.CreateAwsKmsHierarchicalKeyring(input.build());
  }
}
