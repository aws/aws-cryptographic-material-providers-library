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
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoInput;
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoOutput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyInput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyOutput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionOutput;

public interface IKeyStorageInterface {
  /**
   * Get the ACTIVE branch key for encryption for an existing branch key.
   *
   * @param input Get the ACTIVE version for a particular Branch Key.
   * @return Outputs for getting a Branch Key's ACTIVE version.
   */
  GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(
    GetEncryptedActiveBranchKeyInput input
  );

  /**
   * Get the beacon key associated with an existing branch key.
   *
   * @param input Inputs for getting a Beacon Key
   * @return Outputs for getting a Beacon Key
   */
  GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(
    GetEncryptedBeaconKeyInput input
  );

  /**
   * Get a specific branch key version for an existing branch key.
   *
   * @param input Inputs for getting a version of a Branch Key.
   * @return Outputs for getting a version of a Branch Key.
   */
  GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(
    GetEncryptedBranchKeyVersionInput input
  );

  /**
   * Gets information about the underlying storage system.
   *
   * @param input Input for getting information about the underlying storage.
   * @return Output containing information about the underlying storage.
   */
  GetKeyStorageInfoOutput GetKeyStorageInfo(GetKeyStorageInfoInput input);

  /**
   * WriteNewEncryptedBranchKey persists the active item, decrypt only (version) item, and Beacon Key Item of a newly created Branch Key.
   *
   * @param input
   * The information required to atomically write an a new branch key into a key store.
   * The identifiers for all keys passed should be the same.
   *
   * @return The output of writing a new branch key. There is currently no additional information returned.
   */
  WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKey(
    WriteNewEncryptedBranchKeyInput input
  );

  /**
   * WriteNewEncryptedBranchKeyVersion persists the new active item, decrypt only (version) item of a newly generated Branch Key version.
   *
   * @param input
   * The information required to atomically write a new version for an existing branch key into a key store.
   * The identifiers for all keys passed should be the same.
   *
   * @return The output of writing a new version for an existing branch key. There is currently no additional information returned.
   */
  WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersion(
    WriteNewEncryptedBranchKeyVersionInput input
  );
}
