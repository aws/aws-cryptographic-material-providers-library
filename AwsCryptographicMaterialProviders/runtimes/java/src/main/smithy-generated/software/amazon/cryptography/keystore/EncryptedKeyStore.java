// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
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

public final class EncryptedKeyStore implements IEncryptedKeyStore {

  private final software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore _impl;

  private EncryptedKeyStore(
    software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore iEncryptedKeyStore
  ) {
    Objects.requireNonNull(
      iEncryptedKeyStore,
      "Missing value for required argument `iEncryptedKeyStore`"
    );
    this._impl = iEncryptedKeyStore;
  }

  public static EncryptedKeyStore wrap(
    software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore iEncryptedKeyStore
  ) {
    return new EncryptedKeyStore(iEncryptedKeyStore);
  }

  public static <I extends IEncryptedKeyStore> EncryptedKeyStore wrap(
    I iEncryptedKeyStore
  ) {
    Objects.requireNonNull(
      iEncryptedKeyStore,
      "Missing value for required argument `iEncryptedKeyStore`"
    );
    if (
      iEncryptedKeyStore instanceof
      software.amazon.cryptography.keystore.EncryptedKeyStore
    ) {
      return ((EncryptedKeyStore) iEncryptedKeyStore);
    }
    return EncryptedKeyStore.wrap(new NativeWrapper(iEncryptedKeyStore));
  }

  public software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore impl() {
    return this._impl;
  }

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

  public GetTableNameOutput GetTableName(GetTableNameInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetTableNameInput dafnyValue =
      ToDafny.GetTableNameInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetTableNameOutput,
      Error
    > result = this._impl.GetTableName(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetTableNameOutput(result.dtor_value());
  }

  public WriteNewBranchKeyVersionToKeystoreOutput WriteNewBranchKeyVersionToKeystore(
    WriteNewBranchKeyVersionToKeystoreInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreInput dafnyValue =
      ToDafny.WriteNewBranchKeyVersionToKeystoreInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreOutput,
      Error
    > result = this._impl.WriteNewBranchKeyVersionToKeystore(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewBranchKeyVersionToKeystoreOutput(
      result.dtor_value()
    );
  }

  public WriteNewKeyToStoreOutput WriteNewKeyToStore(
    WriteNewKeyToStoreInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreInput dafnyValue =
      ToDafny.WriteNewKeyToStoreInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreOutput,
      Error
    > result = this._impl.WriteNewKeyToStore(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewKeyToStoreOutput(result.dtor_value());
  }

  protected static final class NativeWrapper
    implements
      software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore {

    protected final IEncryptedKeyStore _impl;

    NativeWrapper(IEncryptedKeyStore nativeImpl) {
      if (nativeImpl instanceof EncryptedKeyStore) {
        throw new IllegalArgumentException(
          "Recursive wrapping is strictly forbidden."
        );
      }
      this._impl = nativeImpl;
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
      software.amazon.cryptography.keystore.internaldafny.types.GetTableNameOutput,
      Error
    > GetTableName(
      software.amazon.cryptography.keystore.internaldafny.types.GetTableNameInput dafnyInput
    ) {
      try {
        GetTableNameInput nativeInput = ToNative.GetTableNameInput(dafnyInput);
        GetTableNameOutput nativeOutput = this._impl.GetTableName(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetTableNameOutput dafnyOutput =
          ToDafny.GetTableNameOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetTableNameOutput,
      Error
    > GetTableName_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetTableNameInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreOutput,
      Error
    > WriteNewBranchKeyVersionToKeystore(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreInput dafnyInput
    ) {
      try {
        WriteNewBranchKeyVersionToKeystoreInput nativeInput =
          ToNative.WriteNewBranchKeyVersionToKeystoreInput(dafnyInput);
        WriteNewBranchKeyVersionToKeystoreOutput nativeOutput =
          this._impl.WriteNewBranchKeyVersionToKeystore(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreOutput dafnyOutput =
          ToDafny.WriteNewBranchKeyVersionToKeystoreOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreOutput,
      Error
    > WriteNewBranchKeyVersionToKeystore_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewBranchKeyVersionToKeystoreInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreOutput,
      Error
    > WriteNewKeyToStore(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreInput dafnyInput
    ) {
      try {
        WriteNewKeyToStoreInput nativeInput = ToNative.WriteNewKeyToStoreInput(
          dafnyInput
        );
        WriteNewKeyToStoreOutput nativeOutput =
          this._impl.WriteNewKeyToStore(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreOutput dafnyOutput =
          ToDafny.WriteNewKeyToStoreOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreOutput,
      Error
    > WriteNewKeyToStore_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyToStoreInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
