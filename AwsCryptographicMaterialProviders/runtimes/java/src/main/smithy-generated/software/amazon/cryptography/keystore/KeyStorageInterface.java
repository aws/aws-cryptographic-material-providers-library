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
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoInput;
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoOutput;
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
