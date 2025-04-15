// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.downstream;

import static software.amazon.cryptography.example.Fixtures.HV2_BRANCH_KEY_ID;
import static software.amazon.cryptography.example.Fixtures.KEYSTORE_KMS_ARN;

import com.amazonaws.encryptionsdk.AwsCrypto;
import com.amazonaws.encryptionsdk.CryptoResult;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.CacheType;
import software.amazon.cryptography.materialproviders.model.CreateAwsKmsHierarchicalKeyringInput;
import software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.model.NoCache;

public class ESDKTest {

  private static final byte[] EXAMPLE_DATA =
    "Robbie is a sleepy dog.".getBytes(StandardCharsets.UTF_8);

  @Test
  public void encryptAndDecryptWithHierarchyVersion2Keyring() throws Exception {
    final AwsCrypto crypto = AwsCrypto.builder().build();
    final KeyStore branchKeyStore = KeyStoreProvider.keyStore(KEYSTORE_KMS_ARN);
    final MaterialProviders matProv = MaterialProviders
      .builder()
      .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
      .build();
    final CreateAwsKmsHierarchicalKeyringInput keyringInput =
      CreateAwsKmsHierarchicalKeyringInput
        .builder()
        .keyStore(branchKeyStore)
        .branchKeyId(HV2_BRANCH_KEY_ID)
        .ttlSeconds(0)
        .cache(
          CacheType
            .builder() // OPTIONAL
            .No(NoCache.builder().build())
            .build()
        )
        .build();
    final IKeyring hierarchicalKeyring =
      matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
    final CryptoResult<byte[], ?> encryptResult = crypto.encryptData(
      hierarchicalKeyring,
      EXAMPLE_DATA
    );
    CryptoResult<byte[], ?> cryptoResult = crypto.decryptData(
      hierarchicalKeyring,
      encryptResult.getResult()
    );
    assert Arrays.equals(cryptoResult.getResult(), EXAMPLE_DATA);
    Assert.assertEquals(
      cryptoResult.getResult(),
      EXAMPLE_DATA,
      "HV2 Decryption failed."
    );
  }
}
