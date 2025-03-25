// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.KeyStoreClient;
import software.amazon.cryptography.keystore.internaldafny.__default;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
import software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient;
import software.amazon.cryptography.keystore.model.CreateKeyInput;
import software.amazon.cryptography.keystore.model.CreateKeyOutput;
import software.amazon.cryptography.keystore.model.CreateKeyStoreInput;
import software.amazon.cryptography.keystore.model.CreateKeyStoreOutput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.GetKeyStoreInfoOutput;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.VersionKeyInput;
import software.amazon.cryptography.keystore.model.VersionKeyOutput;

public class KeyStore {

  private final IKeyStoreClient _impl;

  protected KeyStore(BuilderImpl builder) {
    KeyStoreConfig input = builder.KeyStoreConfig();
    software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig dafnyValue =
      ToDafny.KeyStoreConfig(input);
    Result<KeyStoreClient, Error> result = __default.KeyStore(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    this._impl = result.dtor_value();
  }

  KeyStore(IKeyStoreClient impl) {
    this._impl = impl;
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  /**
   * Create a new Branch Key in the Branch Key Store.
   * This method ONLY creates hierarchy-version-1 branch keys.
   * This creates 3 items: the ACTIVE branch key item, the DECRYPT_ONLY for the ACTIVE branch key item, and the beacon key.
   * In DynamoDB, the sort-key for the ACTIVE branch key is 'branch:ACTIVE`;
   * the sort-key for the decrypt_only is 'branch:version:<uuid>';
   * the sort-key for the beacon key is `beacon:ACTIVE'.
   * The active branch key and the decrypt_only items have the same plain-text data key.
   * The beacon key plain-text data key is unqiue.
   * KMS is called 3 times; GenerateDataKeyWithoutPlaintext is called twice, ReEncrypt is called once.
   * All three items are written to DDB by a TransactionWriteItems, conditioned on the absence of a conflicting Branch Key ID.
   * See Branch Key Store Developer Guide's 'Create Branch Keys': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-branch-keys.html
   * @return Outputs for Branch Key creation.
   */
  public CreateKeyOutput CreateKey(CreateKeyInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput dafnyValue =
      ToDafny.CreateKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput,
      Error
    > result = this._impl.CreateKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.CreateKeyOutput(result.dtor_value());
  }

  /**
   * Create the DynamoDB table that backs this Key Store based on the Key Store configuration. If a table already exists, validate it is configured as expected.
   * @return Outputs for Key Store DynamoDB table creation.
   */
  public CreateKeyStoreOutput CreateKeyStore(CreateKeyStoreInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput dafnyValue =
      ToDafny.CreateKeyStoreInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput,
      Error
    > result = this._impl.CreateKeyStore(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.CreateKeyStoreOutput(result.dtor_value());
  }

  /**
   * Get the ACTIVE version for a particular Branch Key from the Key Store.
   *
   * @param input Inputs for getting a Branch Key's ACTIVE version.
   * @return Outputs for getting a Branch Key's ACTIVE version.
   */
  public GetActiveBranchKeyOutput GetActiveBranchKey(
    GetActiveBranchKeyInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput dafnyValue =
      ToDafny.GetActiveBranchKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput,
      Error
    > result = this._impl.GetActiveBranchKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetActiveBranchKeyOutput(result.dtor_value());
  }

  /**
   * Get a Beacon Key from the Key Store.
   *
   * @param input Inputs for getting a Beacon Key
   * @return Outputs for getting a Beacon Key
   */
  public GetBeaconKeyOutput GetBeaconKey(GetBeaconKeyInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput dafnyValue =
      ToDafny.GetBeaconKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput,
      Error
    > result = this._impl.GetBeaconKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetBeaconKeyOutput(result.dtor_value());
  }

  /**
   * Get a particular version of a Branch Key from the Key Store.
   *
   * @param input Inputs for getting a version of a Branch Key.
   * @return Outputs for getting a version of a Branch Key.
   */
  public GetBranchKeyVersionOutput GetBranchKeyVersion(
    GetBranchKeyVersionInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput dafnyValue =
      ToDafny.GetBranchKeyVersionInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput,
      Error
    > result = this._impl.GetBranchKeyVersion(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetBranchKeyVersionOutput(result.dtor_value());
  }

  /**
   * Returns the configuration information for a Key Store.
   * @return The configuration information for a Key Store.
   */
  public GetKeyStoreInfoOutput GetKeyStoreInfo() {
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput,
      Error
    > result = this._impl.GetKeyStoreInfo();
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetKeyStoreInfoOutput(result.dtor_value());
  }

  /**
   * Rotates an exsisting Branch Key;
   * this generates a fresh AES-256 key which all future encrypts will use
   * for the Key Derivation Function,
   * until VersionKey is executed again.
   * This method ONLY works with hierarchy-version-1 Branch Keys;
   * if a hierarchy-version-2 Branch Key is encountered, the operation fails before calling KMS.
   * Rotation is accomplished by first authenticating the ACTIVE branch key item via 'kms:ReEncrypt'.
   * 'kms:GenerateDataKeyWithoutPlaintext', followed by 'kms:ReEncrypt' is used to create a new ACTIVE and matching DECRYPT_ONLY.
   * These two items are then writen to the Branch Key Store via a TransactionWriteItems;
   * this only overwrites the ACTIVE item, the DECRYPT_ONLY is a new item.
   * This leaves all the previous DECRYPT_ONLY items avabile to service decryption of previous rotations.
   * See Branch Key Store Developer Guide's 'Rotate your active branch key': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html
   *
   * @param input Inputs for versioning a Branch Key.
   * @return Outputs for versioning a Branch Key.
   */
  public VersionKeyOutput VersionKey(VersionKeyInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput dafnyValue =
      ToDafny.VersionKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput,
      Error
    > result = this._impl.VersionKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.VersionKeyOutput(result.dtor_value());
  }

  protected IKeyStoreClient impl() {
    return this._impl;
  }

  public interface Builder {
    Builder KeyStoreConfig(KeyStoreConfig KeyStoreConfig);

    KeyStoreConfig KeyStoreConfig();

    KeyStore build();
  }

  static class BuilderImpl implements Builder {

    protected KeyStoreConfig KeyStoreConfig;

    protected BuilderImpl() {}

    public Builder KeyStoreConfig(KeyStoreConfig KeyStoreConfig) {
      this.KeyStoreConfig = KeyStoreConfig;
      return this;
    }

    public KeyStoreConfig KeyStoreConfig() {
      return this.KeyStoreConfig;
    }

    public KeyStore build() {
      if (Objects.isNull(this.KeyStoreConfig())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KeyStoreConfig`"
        );
      }
      return new KeyStore(this);
    }
  }
}
