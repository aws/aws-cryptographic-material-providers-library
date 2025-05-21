// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
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

public final class KeyStorageInterface implements IKeyStorageInterface {

  private final software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface _impl;

  private KeyStorageInterface(
    software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface iKeyStorageInterface
  ) {
    Objects.requireNonNull(
      iKeyStorageInterface,
      "Missing value for required argument `iKeyStorageInterface`"
    );
    this._impl = iKeyStorageInterface;
  }

  public static KeyStorageInterface wrap(
    software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface iKeyStorageInterface
  ) {
    return new KeyStorageInterface(iKeyStorageInterface);
  }

  public static <I extends IKeyStorageInterface> KeyStorageInterface wrap(
    I iKeyStorageInterface
  ) {
    Objects.requireNonNull(
      iKeyStorageInterface,
      "Missing value for required argument `iKeyStorageInterface`"
    );
    if (
      iKeyStorageInterface instanceof
      software.amazon.cryptography.keystore.KeyStorageInterface
    ) {
      return ((KeyStorageInterface) iKeyStorageInterface);
    }
    return KeyStorageInterface.wrap(new NativeWrapper(iKeyStorageInterface));
  }

  public software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface impl() {
    return this._impl;
  }

  /**
   * Delete an existing Mutation Commitment & Index.
   *
   */
  public DeleteMutationOutput DeleteMutation(DeleteMutationInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput dafnyValue =
      ToDafny.DeleteMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput,
      Error
    > result = this._impl.DeleteMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.DeleteMutationOutput(result.dtor_value());
  }

  /**
   * Get the ACTIVE branch key for encryption for an existing branch key.
   *
   * @param input Get the ACTIVE version for a particular Branch Key.
   * @return Outputs for getting a Branch Key's ACTIVE version.
   */
  public GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(
    GetEncryptedActiveBranchKeyInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput dafnyValue =
      ToDafny.GetEncryptedActiveBranchKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput,
      Error
    > result = this._impl.GetEncryptedActiveBranchKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetEncryptedActiveBranchKeyOutput(result.dtor_value());
  }

  /**
   * Get the beacon key associated with an existing branch key.
   *
   * @param input Inputs for getting a Beacon Key
   * @return Outputs for getting a Beacon Key
   */
  public GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(
    GetEncryptedBeaconKeyInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput dafnyValue =
      ToDafny.GetEncryptedBeaconKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput,
      Error
    > result = this._impl.GetEncryptedBeaconKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetEncryptedBeaconKeyOutput(result.dtor_value());
  }

  /**
   * Get a specific branch key version for an existing branch key.
   *
   * @param input Inputs for getting a version of a Branch Key.
   * @return Outputs for getting a version of a Branch Key.
   */
  public GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(
    GetEncryptedBranchKeyVersionInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput dafnyValue =
      ToDafny.GetEncryptedBranchKeyVersionInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput,
      Error
    > result = this._impl.GetEncryptedBranchKeyVersion(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetEncryptedBranchKeyVersionOutput(result.dtor_value());
  }

  /**
   * Retrieves the items necessary to initialize a Mutation,
   * while checking for any in-flight Mutations.
   * These items are the ACTIVE branch key and the beacon key.
   * If a Mutation is already in-flight for this Branch Key,
   * the in-flight Mutation's Commitment and Index are also returned.
   *
   */
  public GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(
    GetItemsForInitializeMutationInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput dafnyValue =
      ToDafny.GetItemsForInitializeMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput,
      Error
    > result = this._impl.GetItemsForInitializeMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetItemsForInitializeMutationOutput(result.dtor_value());
  }

  /**
   * Gets information about the underlying storage system.
   *
   * @param input Input for getting information about the underlying storage.
   * @return Output containing information about the underlying storage.
   */
  public GetKeyStorageInfoOutput GetKeyStorageInfo(
    GetKeyStorageInfoInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput dafnyValue =
      ToDafny.GetKeyStorageInfoInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput,
      Error
    > result = this._impl.GetKeyStorageInfo(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetKeyStorageInfoOutput(result.dtor_value());
  }

  /**
   * Check for Mutation Commitment on a Branch Key ID.
   * If one exists, returns the Mutation Lock.
   * Otherwise, returns nothing.
   *
   */
  public GetMutationOutput GetMutation(GetMutationInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput dafnyValue =
      ToDafny.GetMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput,
      Error
    > result = this._impl.GetMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetMutationOutput(result.dtor_value());
  }

  /**
   * Query Storage for a page of version (decrypt only) items
   * of a Branch Key.
   *
   */
  public QueryForVersionsOutput QueryForVersions(QueryForVersionsInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput dafnyValue =
      ToDafny.QueryForVersionsInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput,
      Error
    > result = this._impl.QueryForVersions(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.QueryForVersionsOutput(result.dtor_value());
  }

  /**
   * Atomically writes,
   * in the terminal state of a Mutation:
   * - new ACTIVE item, if provided
   * - version (decrypt only) for new ACTIVE, if provided
   * - beacon key
   * - a page of version (decrypt only) items
   *
   */
  public WriteAtomicMutationOutput WriteAtomicMutation(
    WriteAtomicMutationInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput dafnyValue =
      ToDafny.WriteAtomicMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput,
      Error
    > result = this._impl.WriteAtomicMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteAtomicMutationOutput(result.dtor_value());
  }

  /**
   * Atomically writes,
   * in the terminal state of a Mutation:
   * - new ACTIVE item, if provided
   * - version (decrypt only) for new ACTIVE, if provided
   * - beacon key
   * Also writes the Mutation Commitment & Index.
   *
   */
  public WriteInitializeMutationOutput WriteInitializeMutation(
    WriteInitializeMutationInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput dafnyValue =
      ToDafny.WriteInitializeMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput,
      Error
    > result = this._impl.WriteInitializeMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteInitializeMutationOutput(result.dtor_value());
  }

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
  public WriteMutatedVersionsOutput WriteMutatedVersions(
    WriteMutatedVersionsInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput dafnyValue =
      ToDafny.WriteMutatedVersionsInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput,
      Error
    > result = this._impl.WriteMutatedVersions(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteMutatedVersionsOutput(result.dtor_value());
  }

  /**
   * Creates a Mutation Index, conditioned on the Mutation Commitment.
   * Used in the edge case where the Commitment exists and Index does not.
   * The Index may have been deleted to restart the mutation from the very beginning.
   *
   *
   */
  public WriteMutationIndexOutput WriteMutationIndex(
    WriteMutationIndexInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput dafnyValue =
      ToDafny.WriteMutationIndexInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput,
      Error
    > result = this._impl.WriteMutationIndex(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteMutationIndexOutput(result.dtor_value());
  }

  /**
   * WriteNewEncryptedBranchKey persists the active item, decrypt only (version) item, and Beacon Key Item of a newly created Branch Key.
   *
   * @param input
   * The information required to atomically write an a new branch key into a key store.
   * The identifiers for all keys passed should be the same.
   *
   * @return The output of writing a new branch key. There is currently no additional information returned.
   */
  public WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKey(
    WriteNewEncryptedBranchKeyInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput dafnyValue =
      ToDafny.WriteNewEncryptedBranchKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput,
      Error
    > result = this._impl.WriteNewEncryptedBranchKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewEncryptedBranchKeyOutput(result.dtor_value());
  }

  /**
   * WriteNewEncryptedBranchKeyVersion persists the new active item, decrypt only (version) item of a newly generated Branch Key version.
   *
   * @param input
   * The information required to atomically write a new version for an existing branch key into a key store.
   * The identifiers for all keys passed should be the same.
   *
   * @return The output of writing a new version for an existing branch key. There is currently no additional information returned.
   */
  public WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersion(
    WriteNewEncryptedBranchKeyVersionInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput dafnyValue =
      ToDafny.WriteNewEncryptedBranchKeyVersionInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput,
      Error
    > result = this._impl.WriteNewEncryptedBranchKeyVersion(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewEncryptedBranchKeyVersionOutput(
      result.dtor_value()
    );
  }

  protected static final class NativeWrapper
    implements
      software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface {

    protected final IKeyStorageInterface _impl;

    NativeWrapper(IKeyStorageInterface nativeImpl) {
      if (nativeImpl instanceof KeyStorageInterface) {
        throw new IllegalArgumentException(
          "Recursive wrapping is strictly forbidden."
        );
      }
      this._impl = nativeImpl;
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput,
      Error
    > DeleteMutation(
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput dafnyInput
    ) {
      try {
        DeleteMutationInput nativeInput = ToNative.DeleteMutationInput(
          dafnyInput
        );
        DeleteMutationOutput nativeOutput =
          this._impl.DeleteMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput dafnyOutput =
          ToDafny.DeleteMutationOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput,
      Error
    > DeleteMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput,
      Error
    > GetEncryptedActiveBranchKey(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput dafnyInput
    ) {
      try {
        GetEncryptedActiveBranchKeyInput nativeInput =
          ToNative.GetEncryptedActiveBranchKeyInput(dafnyInput);
        GetEncryptedActiveBranchKeyOutput nativeOutput =
          this._impl.GetEncryptedActiveBranchKey(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput dafnyOutput =
          ToDafny.GetEncryptedActiveBranchKeyOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput,
      Error
    > GetEncryptedActiveBranchKey_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput,
      Error
    > GetEncryptedBeaconKey(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput dafnyInput
    ) {
      try {
        GetEncryptedBeaconKeyInput nativeInput =
          ToNative.GetEncryptedBeaconKeyInput(dafnyInput);
        GetEncryptedBeaconKeyOutput nativeOutput =
          this._impl.GetEncryptedBeaconKey(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput dafnyOutput =
          ToDafny.GetEncryptedBeaconKeyOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput,
      Error
    > GetEncryptedBeaconKey_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput,
      Error
    > GetEncryptedBranchKeyVersion(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput dafnyInput
    ) {
      try {
        GetEncryptedBranchKeyVersionInput nativeInput =
          ToNative.GetEncryptedBranchKeyVersionInput(dafnyInput);
        GetEncryptedBranchKeyVersionOutput nativeOutput =
          this._impl.GetEncryptedBranchKeyVersion(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput dafnyOutput =
          ToDafny.GetEncryptedBranchKeyVersionOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput,
      Error
    > GetEncryptedBranchKeyVersion_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput,
      Error
    > GetItemsForInitializeMutation(
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput dafnyInput
    ) {
      try {
        GetItemsForInitializeMutationInput nativeInput =
          ToNative.GetItemsForInitializeMutationInput(dafnyInput);
        GetItemsForInitializeMutationOutput nativeOutput =
          this._impl.GetItemsForInitializeMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput dafnyOutput =
          ToDafny.GetItemsForInitializeMutationOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput,
      Error
    > GetItemsForInitializeMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput,
      Error
    > GetKeyStorageInfo(
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput dafnyInput
    ) {
      try {
        GetKeyStorageInfoInput nativeInput = ToNative.GetKeyStorageInfoInput(
          dafnyInput
        );
        GetKeyStorageInfoOutput nativeOutput =
          this._impl.GetKeyStorageInfo(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput dafnyOutput =
          ToDafny.GetKeyStorageInfoOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput,
      Error
    > GetKeyStorageInfo_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput,
      Error
    > GetMutation(
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput dafnyInput
    ) {
      try {
        GetMutationInput nativeInput = ToNative.GetMutationInput(dafnyInput);
        GetMutationOutput nativeOutput = this._impl.GetMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput dafnyOutput =
          ToDafny.GetMutationOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput,
      Error
    > GetMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput,
      Error
    > QueryForVersions(
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput dafnyInput
    ) {
      try {
        QueryForVersionsInput nativeInput = ToNative.QueryForVersionsInput(
          dafnyInput
        );
        QueryForVersionsOutput nativeOutput =
          this._impl.QueryForVersions(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput dafnyOutput =
          ToDafny.QueryForVersionsOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput,
      Error
    > QueryForVersions_k(
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput,
      Error
    > WriteAtomicMutation(
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput dafnyInput
    ) {
      try {
        WriteAtomicMutationInput nativeInput =
          ToNative.WriteAtomicMutationInput(dafnyInput);
        WriteAtomicMutationOutput nativeOutput =
          this._impl.WriteAtomicMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput dafnyOutput =
          ToDafny.WriteAtomicMutationOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput,
      Error
    > WriteAtomicMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput,
      Error
    > WriteInitializeMutation(
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput dafnyInput
    ) {
      try {
        WriteInitializeMutationInput nativeInput =
          ToNative.WriteInitializeMutationInput(dafnyInput);
        WriteInitializeMutationOutput nativeOutput =
          this._impl.WriteInitializeMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput dafnyOutput =
          ToDafny.WriteInitializeMutationOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput,
      Error
    > WriteInitializeMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput,
      Error
    > WriteMutatedVersions(
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput dafnyInput
    ) {
      try {
        WriteMutatedVersionsInput nativeInput =
          ToNative.WriteMutatedVersionsInput(dafnyInput);
        WriteMutatedVersionsOutput nativeOutput =
          this._impl.WriteMutatedVersions(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput dafnyOutput =
          ToDafny.WriteMutatedVersionsOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput,
      Error
    > WriteMutatedVersions_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput,
      Error
    > WriteMutationIndex(
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput dafnyInput
    ) {
      try {
        WriteMutationIndexInput nativeInput = ToNative.WriteMutationIndexInput(
          dafnyInput
        );
        WriteMutationIndexOutput nativeOutput =
          this._impl.WriteMutationIndex(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput dafnyOutput =
          ToDafny.WriteMutationIndexOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput,
      Error
    > WriteMutationIndex_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput,
      Error
    > WriteNewEncryptedBranchKey(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput dafnyInput
    ) {
      try {
        WriteNewEncryptedBranchKeyInput nativeInput =
          ToNative.WriteNewEncryptedBranchKeyInput(dafnyInput);
        WriteNewEncryptedBranchKeyOutput nativeOutput =
          this._impl.WriteNewEncryptedBranchKey(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput dafnyOutput =
          ToDafny.WriteNewEncryptedBranchKeyOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput,
      Error
    > WriteNewEncryptedBranchKey_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput,
      Error
    > WriteNewEncryptedBranchKeyVersion(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput dafnyInput
    ) {
      try {
        WriteNewEncryptedBranchKeyVersionInput nativeInput =
          ToNative.WriteNewEncryptedBranchKeyVersionInput(dafnyInput);
        WriteNewEncryptedBranchKeyVersionOutput nativeOutput =
          this._impl.WriteNewEncryptedBranchKeyVersion(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput dafnyOutput =
          ToDafny.WriteNewEncryptedBranchKeyVersionOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput,
      Error
    > WriteNewEncryptedBranchKeyVersion_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
