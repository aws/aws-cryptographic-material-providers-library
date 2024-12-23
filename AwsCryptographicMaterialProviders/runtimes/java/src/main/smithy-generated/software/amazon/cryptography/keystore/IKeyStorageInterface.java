// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import software.amazon.cryptography.keystore.model.DeleteMutationInput;
import software.amazon.cryptography.keystore.model.DeleteMutationOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetEncryptedBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationInput;
import software.amazon.cryptography.keystore.model.GetItemsForInitializeMutationOutput;
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoInput;
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoOutput;
import software.amazon.cryptography.keystore.model.GetMutationInput;
import software.amazon.cryptography.keystore.model.GetMutationOutput;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;
import software.amazon.cryptography.keystore.model.WriteAtomicMutationInput;
import software.amazon.cryptography.keystore.model.WriteAtomicMutationOutput;
import software.amazon.cryptography.keystore.model.WriteInitializeMutationInput;
import software.amazon.cryptography.keystore.model.WriteInitializeMutationOutput;
import software.amazon.cryptography.keystore.model.WriteMutatedVersionsInput;
import software.amazon.cryptography.keystore.model.WriteMutatedVersionsOutput;
import software.amazon.cryptography.keystore.model.WriteMutationIndexInput;
import software.amazon.cryptography.keystore.model.WriteMutationIndexOutput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyInput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyOutput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.WriteNewEncryptedBranchKeyVersionOutput;

public interface IKeyStorageInterface {
  /**
   * Delete an existing Mutation Commitment & Index.
   *
   */
  DeleteMutationOutput DeleteMutation(DeleteMutationInput input);

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
   * Retrieves the items necessary to initialize a Mutation,
   * while checking for any in-flight Mutations.
   * These items are the ACTIVE branch key and the beacon key.
   * If a Mutation is already in-flight for this Branch Key,
   * the in-flight Mutation's Commitment and Index are also returned.
   *
   */
  GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(
    GetItemsForInitializeMutationInput input
  );

  /**
   * Gets information about the underlying storage system.
   *
   * @param input Input for getting information about the underlying storage.
   * @return Output containing information about the underlying storage.
   */
  GetKeyStorageInfoOutput GetKeyStorageInfo(GetKeyStorageInfoInput input);

  /**
   * Check for Mutation Commitment on a Branch Key ID.
   * If one exists, returns the Mutation Lock.
   * Otherwise, returns nothing.
   *
   */
  GetMutationOutput GetMutation(GetMutationInput input);

  /**
   * Query Storage for a page of version (decrypt only) items
   * of a Branch Key.
   *
   */
  QueryForVersionsOutput QueryForVersions(QueryForVersionsInput input);

  /**
   * Atomically writes,
   * in the terminal state of a Mutation:
   * - new ACTIVE item, if provided
   * - version (decrypt only) for new ACTIVE, if provided
   * - beacon key
   * - a page of version (decrypt only) items
   *
   */
  WriteAtomicMutationOutput WriteAtomicMutation(WriteAtomicMutationInput input);

  /**
   * Atomically writes,
   * in the terminal state of a Mutation:
   * - new ACTIVE item, if provided
   * - version (decrypt only) for new ACTIVE, if provided
   * - beacon key
   * Also writes the Mutation Commitment & Index.
   *
   */
  WriteInitializeMutationOutput WriteInitializeMutation(
    WriteInitializeMutationInput input
  );

  /**
   * Atomically writes,
   * in the terminal state of a Mutation,
   * a page of version (decrypt only) items,
   * conditioned on:
   * - every version already existing
   * - every version's cipher-text had not changed
   * - the Mutation Commitment has not changed
   *
   * If the Mutation is complete,
   * the Mutation Index and Mutation Commitment are deleted.
   * Otherwise,
   * the Mutation Index is updated,
   * conditioned on it not having been changed since
   * it was last read.
   *
   *
   */
  WriteMutatedVersionsOutput WriteMutatedVersions(
    WriteMutatedVersionsInput input
  );

  /**
   * Creates a Mutation Index, conditioned on the Mutation Commitment.
   * Used in the edge case where the Commitment exists and Index does not.
   * The Index may have been deleted to restart the mutation from the very beginning.
   *
   *
   */
  WriteMutationIndexOutput WriteMutationIndex(WriteMutationIndexInput input);

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
