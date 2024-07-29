// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.GetTableNameInput;
import software.amazon.cryptography.keystore.model.GetTableNameOutput;
import software.amazon.cryptography.keystore.model.WriteNewBranchKeyVersionToKeystoreInput;
import software.amazon.cryptography.keystore.model.WriteNewBranchKeyVersionToKeystoreOutput;
import software.amazon.cryptography.keystore.model.WriteNewKeyToStoreInput;
import software.amazon.cryptography.keystore.model.WriteNewKeyToStoreOutput;

public interface IEncryptedKeyStore {
  GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(
    GetEncryptedActiveBranchKeyInput input
  );

  GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(
    GetEncryptedBeaconKeyInput input
  );

  GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(
    GetEncryptedBranchKeyVersionInput input
  );

  GetTableNameOutput GetTableName(GetTableNameInput input);

  WriteNewBranchKeyVersionToKeystoreOutput WriteNewBranchKeyVersionToKeystore(
    WriteNewBranchKeyVersionToKeystoreInput input
  );

  WriteNewKeyToStoreOutput WriteNewKeyToStore(WriteNewKeyToStoreInput input);
}
