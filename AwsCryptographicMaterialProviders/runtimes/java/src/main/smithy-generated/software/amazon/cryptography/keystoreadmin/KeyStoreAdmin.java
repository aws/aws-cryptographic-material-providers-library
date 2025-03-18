// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.util.Objects;
import software.amazon.cryptography.keystoreadmin.internaldafny.KeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.internaldafny.__default;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyInput;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyOutput;

public class KeyStoreAdmin {

  private final IKeyStoreAdminClient _impl;

  protected KeyStoreAdmin(BuilderImpl builder) {
    KeyStoreAdminConfig input = builder.KeyStoreAdminConfig();
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig dafnyValue =
      ToDafny.KeyStoreAdminConfig(input);
    Result<KeyStoreAdminClient, Error> result = __default.KeyStoreAdmin(
      dafnyValue
    );
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    this._impl = result.dtor_value();
  }

  KeyStoreAdmin(IKeyStoreAdminClient impl) {
    this._impl = impl;
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  /**
   * Applies the Mutation to a page of Branch Key Items.
   * If all Items have been mutated, removes the Mutation Commitment and Index.
   * This operation can race other Apply Mutation requests for the same Branch Key.
   * Should that occur, all but one of the requests will fail with a 'Key Storage Exception'.
   * Note that the Mutation Token only contains serializable members;
   * the 'System Key' and 'Strategy' settings are separate parameters.
   * In particular, the 'System Key' setting MUST be consistent across
   * the Initialize Mutation and all the Apply Mutation calls of a Mutation.
   *
   */
  public ApplyMutationOutput ApplyMutation(ApplyMutationInput input) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput dafnyValue =
      ToDafny.ApplyMutationInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput,
      Error
    > result = this._impl.ApplyMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.ApplyMutationOutput(result.dtor_value());
  }

  /**
   * Create a new Branch Key in the Branch Key Store.
   * This creates 3 items: the ACTIVE branch key item, the DECRYPT_ONLY for the ACTIVE branch key item, and the beacon key.
   * In DynamoDB, the sort-key for the ACTIVE branch key is 'branch:ACTIVE`;
   * the sort-key for the decrypt_only is 'branch:version:<uuid>';
   * the sort-key for the beacon key is `beacon:ACTIVE'.
   * The active branch key and the decrypt_only items have the same plain-text data key.
   * The beacon key plain-text data key is unqiue.
   * KMS calls are determined by the 'hierarchy-version' and 'KeyManagementStrategy'.
   * All three items are written to DDB by a TransactionWriteItems, conditioned on the absence of a conflicting Branch Key ID.
   * See Branch Key Store Developer Guide's 'Create Branch Keys': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-branch-keys.html
   *
   */
  public CreateKeyOutput CreateKey(CreateKeyInput input) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput dafnyValue =
      ToDafny.CreateKeyInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput,
      Error
    > result = this._impl.CreateKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.CreateKeyOutput(result.dtor_value());
  }

  /**
   * Check for an in-flight Mutation on a Branch Key ID.
   * If one exists, return a description of the mutation.
   *
   */
  public DescribeMutationOutput DescribeMutation(DescribeMutationInput input) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput dafnyValue =
      ToDafny.DescribeMutationInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput,
      Error
    > result = this._impl.DescribeMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.DescribeMutationOutput(result.dtor_value());
  }

  /**
   * Starts a Mutation to all Items of a Branch Key ID.
   * Mutates the Beacon Key.
   * Either Mutates the Active & its version (decrypt only), or versions the Branch Key,
   * depending on the 'Do Not Version' argument.
   * Regardless, if operation is successful,
   * the Beacon, Active, & the Active's version are in the terminal state.
   * Establishes the Mutation Commitment; simultaneous conflicting Mutations are prevented by the Mutation Commitment.
   * A Mutation changes the Encryption Context and/or KMS Key associated with a Branch Key.
   * As such, a Mutation can cause actors to loose access to a Branch Key,
   * if the actor's access was predicated on particular Encryption Context value or KMS Key.
   * Mutations MUST be completed via subsequent invocations of the Apply Mutation Operation,
   * first invoked with the Mutation Token returned in 'Initialize Mutation Output'.
   * If access to a KMS Key is revoked while a Mutation is in-flight,
   * the Branch Key will be stuck in a mixed state.
   * This is not ideal, but once access to the KMS Key is restored,
   * the Mutation can be continued by calling 'Describe Mutation'
   * and then calling 'Apply Mutation' as normal.
   * With respect to the output's Mutation Token, this operation is idempotent;
   * if invoked with the same request as an in-flight Mutation,
   * the operation will return successful
   * with the same Mutation Token as earlier requests.
   * The 'Initialize Mutation Flag' of the output indicates
   * if the request was for a novel Mutation or one already in-flight.
   * 'MutationConflictException' is thrown if a different Mutation/change is already in-flight.
   * This operation can race against other Initialize Mutation requests or Version Key requests for the same Branch Key.
   * Should that occur, all but one of the requests will fail.
   * Race errors are either 'VersionRaceException' or 'KeyStorageException'.
   *
   */
  public InitializeMutationOutput InitializeMutation(
    InitializeMutationInput input
  ) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput dafnyValue =
      ToDafny.InitializeMutationInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput,
      Error
    > result = this._impl.InitializeMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.InitializeMutationOutput(result.dtor_value());
  }

  /**
   * Rotates the Branch Key by creating a new ACTIVE version of an existing Branch Key,
   * along with a complementing Version (DECRYPT_ONLY) in the Key Store.
   * This generates a fresh AES-256 key which all future encrypts will use
   * for the Key Derivation Function,
   * until VersionKey is executed again.
   * Rotation is accomplished by first authenticating the ACTIVE branch key item,
   * followed by generation of a new ACTIVE and matching DECRYPT_ONLY.
   * KMS calls are determined by the 'hierarchy-version' and 'KeyManagementStrategy'.
   * These two items are then writen to the Branch Key Store via a TransactionWriteItems;
   * this only overwrites the ACTIVE item, the DECRYPT_ONLY is a new item.
   * This leaves all the previous DECRYPT_ONLY items avabile to service decryption of previous rotations.
   * This operation can race against other Version Key requests or Initialize Mutation requests for the same Branch Key.
   * Should that occur, all but one of the requests will fail.
   * Race errors are either 'Version Race Exceptions' or 'Key Storage Exceptions'.
   * See Branch Key Store Developer Guide's 'Rotate your active branch key': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html
   *
   */
  public VersionKeyOutput VersionKey(VersionKeyInput input) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput dafnyValue =
      ToDafny.VersionKeyInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput,
      Error
    > result = this._impl.VersionKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.VersionKeyOutput(result.dtor_value());
  }

  protected IKeyStoreAdminClient impl() {
    return this._impl;
  }

  public interface Builder {
    Builder KeyStoreAdminConfig(KeyStoreAdminConfig KeyStoreAdminConfig);

    KeyStoreAdminConfig KeyStoreAdminConfig();

    KeyStoreAdmin build();
  }

  static class BuilderImpl implements Builder {

    protected KeyStoreAdminConfig KeyStoreAdminConfig;

    protected BuilderImpl() {}

    public Builder KeyStoreAdminConfig(
      KeyStoreAdminConfig KeyStoreAdminConfig
    ) {
      this.KeyStoreAdminConfig = KeyStoreAdminConfig;
      return this;
    }

    public KeyStoreAdminConfig KeyStoreAdminConfig() {
      return this.KeyStoreAdminConfig;
    }

    public KeyStoreAdmin build() {
      if (Objects.isNull(this.KeyStoreAdminConfig())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KeyStoreAdminConfig`"
        );
      }
      return new KeyStoreAdmin(this);
    }
  }
}
