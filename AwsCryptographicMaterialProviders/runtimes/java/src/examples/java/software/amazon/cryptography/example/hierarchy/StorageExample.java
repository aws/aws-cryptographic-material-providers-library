package software.amazon.cryptography.example.hierarchy;

import java.util.stream.Collectors;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.cryptography.example.StorageCheater;
import software.amazon.cryptography.keystore.IKeyStorageInterface;
import software.amazon.cryptography.keystore.KeyStorageInterface;
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

public class StorageExample implements IKeyStorageInterface {

  private final KeyStorageInterface storageCheater;

  public static KeyStorageInterface create(
    DynamoDbClient ddbClient,
    String physicalName,
    String logicalName
  ) {
    IKeyStorageInterface _nw0 = new StorageExample(
      ddbClient,
      physicalName,
      logicalName
    );
    return KeyStorageInterface.wrap(_nw0);
  }

  StorageExample(
    DynamoDbClient ddbClient,
    String physicalName,
    String logicalName
  ) {
    this.storageCheater =
      StorageCheater.create(ddbClient, physicalName, logicalName);
  }

  /**
   * Delete an existing Mutation Commitment & Index.
   *
   * @param input
   */
  @Override
  public DeleteMutationOutput DeleteMutation(DeleteMutationInput input) {
    return storageCheater.DeleteMutation(input);
  }

  /**
   * Get the ACTIVE branch key for encryption for an existing branch key.
   *
   * @param input Get the ACTIVE version for a particular Branch Key.
   * @return Outputs for getting a Branch Key's ACTIVE version.
   */
  @Override
  public GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(
    GetEncryptedActiveBranchKeyInput input
  ) {
    return storageCheater.GetEncryptedActiveBranchKey(input);
  }

  /**
   * Get the beacon key associated with an existing branch key.
   *
   * @param input Inputs for getting a Beacon Key
   * @return Outputs for getting a Beacon Key
   */
  @Override
  public GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(
    GetEncryptedBeaconKeyInput input
  ) {
    return storageCheater.GetEncryptedBeaconKey(input);
  }

  /**
   * Get a specific branch key version for an existing branch key.
   *
   * @param input Inputs for getting a version of a Branch Key.
   * @return Outputs for getting a version of a Branch Key.
   */
  @Override
  public GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(
    GetEncryptedBranchKeyVersionInput input
  ) {
    return storageCheater.GetEncryptedBranchKeyVersion(input);
  }

  /**
   * Retrieves the items necessary to initialize a Mutation, while checking for any in-flight Mutations. These items are
   * the ACTIVE branch key and the beacon key. If a Mutation is already in-flight for this Branch Key, the in-flight
   * Mutation's Commitment and Index are also returned.
   *
   * @param input
   */
  @Override
  public GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(
    GetItemsForInitializeMutationInput input
  ) {
    return storageCheater.GetItemsForInitializeMutation(input);
  }

  /**
   * Gets information about the underlying storage system.
   *
   * @param input Input for getting information about the underlying storage.
   * @return Output containing information about the underlying storage.
   */
  @Override
  public GetKeyStorageInfoOutput GetKeyStorageInfo(
    GetKeyStorageInfoInput input
  ) {
    return storageCheater.GetKeyStorageInfo(input);
  }

  /**
   * Check for Mutation Commitment on a Branch Key ID. If one exists, returns the Mutation Lock. Otherwise, returns
   * nothing.
   *
   * @param input
   */
  @Override
  public GetMutationOutput GetMutation(GetMutationInput input) {
    return storageCheater.GetMutation(input);
  }

  /**
   * Query Storage for a page of version (decrypt only) items of a Branch Key.
   *
   * @param input
   */
  @Override
  public QueryForVersionsOutput QueryForVersions(QueryForVersionsInput input) {
    // System.out.println(
    //   "\nStorage Cheater: QueryForVersions: Last: " +
    //   input.ExclusiveStartKey() +
    //   "\n"
    // );
    QueryForVersionsOutput output = storageCheater.QueryForVersions(input);
    // System.out.println(
    //   "\nStorage Cheater: QueryForVersions: Found: " +
    //   output
    //     .Items()
    //     .stream()
    //     .map(item -> item.EncryptionContext().get("type") + " " + item.KmsArn())
    //     .collect(Collectors.joining("\n")) +
    //   "\n"
    // );
    return output;
  }

  /**
   * Atomically writes, in the terminal state of a Mutation: - new ACTIVE item, if provided - version (decrypt only) for
   * new ACTIVE, if provided - beacon key - a page of version (decrypt only) items
   *
   * @param input
   */
  @Override
  public WriteAtomicMutationOutput WriteAtomicMutation(
    WriteAtomicMutationInput input
  ) {
    return storageCheater.WriteAtomicMutation(input);
  }

  /**
   * Atomically writes, in the terminal state of a Mutation: - new ACTIVE item, if provided - version (decrypt only) for
   * new ACTIVE, if provided - beacon key Also writes the Mutation Commitment & Index.
   *
   * @param input
   */
  @Override
  public WriteInitializeMutationOutput WriteInitializeMutation(
    WriteInitializeMutationInput input
  ) {
    return storageCheater.WriteInitializeMutation(input);
  }

  /**
   * Atomically writes, in the terminal state of a Mutation, a page of version (decrypt only) items, conditioned on: -
   * every version already existing - every version's cipher-text had not changed - the Mutation Commitment has not
   * changed
   * <p>
   * If the Mutation is complete, the Mutation Index and Mutation Commitment are deleted. Otherwise, the Mutation Index
   * is updated, conditioned on it not having been changed since it was last read.
   *
   * @param input
   */
  @Override
  public WriteMutatedVersionsOutput WriteMutatedVersions(
    WriteMutatedVersionsInput input
  ) {
    // System.out.println(
    //   "\nStorage Cheater: Write Mutated Versions: Index: " +
    //   input.MutationIndex().Index().PageIndex() +
    //   "\n"
    // );
    return storageCheater.WriteMutatedVersions(input);
  }

  /**
   * Creates a Mutation Index, conditioned on the Mutation Commitment. Used in the edge case where the Commitment exists
   * and Index does not. The Index may have been deleted to restart the mutation from the very beginning.
   *
   * @param input
   */
  @Override
  public WriteMutationIndexOutput WriteMutationIndex(
    WriteMutationIndexInput input
  ) {
    return storageCheater.WriteMutationIndex(input);
  }

  /**
   * WriteNewEncryptedBranchKey persists the active item, decrypt only (version) item, and Beacon Key Item of a newly
   * created Branch Key.
   *
   * @param input The information required to atomically write an a new branch key into a key store. The identifiers for
   *              all keys passed should be the same.
   * @return The output of writing a new branch key. There is currently no additional information returned.
   */
  @Override
  public WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKey(
    WriteNewEncryptedBranchKeyInput input
  ) {
    return storageCheater.WriteNewEncryptedBranchKey(input);
  }

  /**
   * WriteNewEncryptedBranchKeyVersion persists the new active item, decrypt only (version) item of a newly generated
   * Branch Key version.
   *
   * @param input The information required to atomically write a new version for an existing branch key into a key
   *              store. The identifiers for all keys passed should be the same.
   * @return The output of writing a new version for an existing branch key. There is currently no additional
   * information returned.
   */
  @Override
  public WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersion(
    WriteNewEncryptedBranchKeyVersionInput input
  ) {
    return storageCheater.WriteNewEncryptedBranchKeyVersion(input);
  }
}
