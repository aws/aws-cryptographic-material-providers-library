// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.keystore.internaldafny.types.Error;
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

  public DescribeEncryptedKeyStoreOutput DescribeEncryptedKeyStore(
    DescribeEncryptedKeyStoreInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreInput dafnyValue =
      ToDafny.DescribeEncryptedKeyStoreInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreOutput,
      Error
    > result = this._impl.DescribeEncryptedKeyStore(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.DescribeEncryptedKeyStoreOutput(result.dtor_value());
  }

  public GetActiveOutput GetActive(GetActiveInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetActiveInput dafnyValue =
      ToDafny.GetActiveInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveOutput,
      Error
    > result = this._impl.GetActive(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetActiveOutput(result.dtor_value());
  }

  public GetBeaconOutput GetBeacon(GetBeaconInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetBeaconInput dafnyValue =
      ToDafny.GetBeaconInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconOutput,
      Error
    > result = this._impl.GetBeacon(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetBeaconOutput(result.dtor_value());
  }

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

  public GetVersionOutput GetVersion(GetVersionInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.GetVersionInput dafnyValue =
      ToDafny.GetVersionInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetVersionOutput,
      Error
    > result = this._impl.GetVersion(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetVersionOutput(result.dtor_value());
  }

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

  public WriteCompleteMutationOutput WriteCompleteMutation(
    WriteCompleteMutationInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationInput dafnyValue =
      ToDafny.WriteCompleteMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationOutput,
      Error
    > result = this._impl.WriteCompleteMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteCompleteMutationOutput(result.dtor_value());
  }

  public WriteItemsForInitializeMutationOutput WriteItemsForInitializeMutation(
    WriteItemsForInitializeMutationInput input
  ) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationInput dafnyValue =
      ToDafny.WriteItemsForInitializeMutationInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationOutput,
      Error
    > result = this._impl.WriteItemsForInitializeMutation(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteItemsForInitializeMutationOutput(result.dtor_value());
  }

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

  public WriteNewKeyOutput WriteNewKey(WriteNewKeyInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyInput dafnyValue =
      ToDafny.WriteNewKeyInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyOutput,
      Error
    > result = this._impl.WriteNewKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewKeyOutput(result.dtor_value());
  }

  public WriteNewVersionOutput WriteNewVersion(WriteNewVersionInput input) {
    software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionInput dafnyValue =
      ToDafny.WriteNewVersionInput(input);
    Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionOutput,
      Error
    > result = this._impl.WriteNewVersion(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.WriteNewVersionOutput(result.dtor_value());
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
      software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreOutput,
      Error
    > DescribeEncryptedKeyStore(
      software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreInput dafnyInput
    ) {
      try {
        DescribeEncryptedKeyStoreInput nativeInput =
          ToNative.DescribeEncryptedKeyStoreInput(dafnyInput);
        DescribeEncryptedKeyStoreOutput nativeOutput =
          this._impl.DescribeEncryptedKeyStore(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreOutput dafnyOutput =
          ToDafny.DescribeEncryptedKeyStoreOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreOutput,
      Error
    > DescribeEncryptedKeyStore_k(
      software.amazon.cryptography.keystore.internaldafny.types.DescribeEncryptedKeyStoreInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveOutput,
      Error
    > GetActive(
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveInput dafnyInput
    ) {
      try {
        GetActiveInput nativeInput = ToNative.GetActiveInput(dafnyInput);
        GetActiveOutput nativeOutput = this._impl.GetActive(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetActiveOutput dafnyOutput =
          ToDafny.GetActiveOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveOutput,
      Error
    > GetActive_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconOutput,
      Error
    > GetBeacon(
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconInput dafnyInput
    ) {
      try {
        GetBeaconInput nativeInput = ToNative.GetBeaconInput(dafnyInput);
        GetBeaconOutput nativeOutput = this._impl.GetBeacon(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetBeaconOutput dafnyOutput =
          ToDafny.GetBeaconOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconOutput,
      Error
    > GetBeacon_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconInput dafnyInput
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
      software.amazon.cryptography.keystore.internaldafny.types.GetVersionOutput,
      Error
    > GetVersion(
      software.amazon.cryptography.keystore.internaldafny.types.GetVersionInput dafnyInput
    ) {
      try {
        GetVersionInput nativeInput = ToNative.GetVersionInput(dafnyInput);
        GetVersionOutput nativeOutput = this._impl.GetVersion(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.GetVersionOutput dafnyOutput =
          ToDafny.GetVersionOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.GetVersionOutput,
      Error
    > GetVersion_k(
      software.amazon.cryptography.keystore.internaldafny.types.GetVersionInput dafnyInput
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
      software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationOutput,
      Error
    > WriteCompleteMutation(
      software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationInput dafnyInput
    ) {
      try {
        WriteCompleteMutationInput nativeInput =
          ToNative.WriteCompleteMutationInput(dafnyInput);
        WriteCompleteMutationOutput nativeOutput =
          this._impl.WriteCompleteMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationOutput dafnyOutput =
          ToDafny.WriteCompleteMutationOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationOutput,
      Error
    > WriteCompleteMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteCompleteMutationInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationOutput,
      Error
    > WriteItemsForInitializeMutation(
      software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationInput dafnyInput
    ) {
      try {
        WriteItemsForInitializeMutationInput nativeInput =
          ToNative.WriteItemsForInitializeMutationInput(dafnyInput);
        WriteItemsForInitializeMutationOutput nativeOutput =
          this._impl.WriteItemsForInitializeMutation(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationOutput dafnyOutput =
          ToDafny.WriteItemsForInitializeMutationOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationOutput,
      Error
    > WriteItemsForInitializeMutation_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteItemsForInitializeMutationInput dafnyInput
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
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
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
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyOutput,
      Error
    > WriteNewKey(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyInput dafnyInput
    ) {
      try {
        WriteNewKeyInput nativeInput = ToNative.WriteNewKeyInput(dafnyInput);
        WriteNewKeyOutput nativeOutput = this._impl.WriteNewKey(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyOutput dafnyOutput =
          ToDafny.WriteNewKeyOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyOutput,
      Error
    > WriteNewKey_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewKeyInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionOutput,
      Error
    > WriteNewVersion(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionInput dafnyInput
    ) {
      try {
        WriteNewVersionInput nativeInput = ToNative.WriteNewVersionInput(
          dafnyInput
        );
        WriteNewVersionOutput nativeOutput =
          this._impl.WriteNewVersion(nativeInput);
        software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionOutput dafnyOutput =
          ToDafny.WriteNewVersionOutput(nativeOutput);
        return Result.create_Success(dafnyOutput);
      } catch (RuntimeException ex) {
        return Result.create_Failure(ToDafny.Error(ex));
      }
    }

    public Result<
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionOutput,
      Error
    > WriteNewVersion_k(
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewVersionInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
