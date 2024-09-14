// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import software.amazon.cryptography.keystore.model.DescribeEncryptedKeyStoreInput;
import software.amazon.cryptography.keystore.model.DescribeEncryptedKeyStoreOutput;
import software.amazon.cryptography.keystore.model.GetActiveInput;
import software.amazon.cryptography.keystore.model.GetActiveOutput;
import software.amazon.cryptography.keystore.model.GetBeaconInput;
import software.amazon.cryptography.keystore.model.GetBeaconOutput;
import software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.model.GetVersionInput;
import software.amazon.cryptography.keystore.model.GetVersionOutput;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;
import software.amazon.cryptography.keystore.model.WriteCompleteMutationInput;
import software.amazon.cryptography.keystore.model.WriteCompleteMutationOutput;
import software.amazon.cryptography.keystore.model.WriteItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.model.WriteItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.model.WriteMutatedVersionsInput;
import software.amazon.cryptography.keystore.model.WriteMutatedVersionsOutput;
import software.amazon.cryptography.keystore.model.WriteNewKeyInput;
import software.amazon.cryptography.keystore.model.WriteNewKeyOutput;
import software.amazon.cryptography.keystore.model.WriteNewVersionInput;
import software.amazon.cryptography.keystore.model.WriteNewVersionOutput;

public interface IEncryptedKeyStore {
  DescribeEncryptedKeyStoreOutput DescribeEncryptedKeyStore(
    DescribeEncryptedKeyStoreInput input
  );

  GetActiveOutput GetActive(GetActiveInput input);

  GetBeaconOutput GetBeacon(GetBeaconInput input);

  GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(
    GetItemsForInitializeMutationInput input
  );

  GetVersionOutput GetVersion(GetVersionInput input);

  QueryForVersionsOutput QueryForVersions(QueryForVersionsInput input);

  WriteCompleteMutationOutput WriteCompleteMutation(
    WriteCompleteMutationInput input
  );

  WriteItemsForInitializeMutationOutput WriteItemsForInitializeMutation(
    WriteItemsForInitializeMutationInput input
  );

  WriteMutatedVersionsOutput WriteMutatedVersions(
    WriteMutatedVersionsInput input
  );

  WriteNewKeyOutput WriteNewKey(WriteNewKeyInput input);

  WriteNewVersionOutput WriteNewVersion(WriteNewVersionInput input);
}
