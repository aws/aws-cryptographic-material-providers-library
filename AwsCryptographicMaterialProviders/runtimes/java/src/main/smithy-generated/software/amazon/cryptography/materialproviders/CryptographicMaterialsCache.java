// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders;

import Wrappers_Compile.Result;
import dafny.Tuple0;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.materialproviders.internaldafny.types.Error;
import software.amazon.cryptography.materialproviders.model.DeleteCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryOutput;
import software.amazon.cryptography.materialproviders.model.PutCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.UpdateUsageMetadataInput;

public final class CryptographicMaterialsCache
  implements ICryptographicMaterialsCache {

  private final software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _impl;

  private CryptographicMaterialsCache(
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache iCryptographicMaterialsCache
  ) {
    Objects.requireNonNull(
      iCryptographicMaterialsCache,
      "Missing value for required argument `iCryptographicMaterialsCache`"
    );
    this._impl = iCryptographicMaterialsCache;
  }

  public static CryptographicMaterialsCache wrap(
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache iCryptographicMaterialsCache
  ) {
    return new CryptographicMaterialsCache(iCryptographicMaterialsCache);
  }

  public static <
    I extends ICryptographicMaterialsCache
  > CryptographicMaterialsCache wrap(I iCryptographicMaterialsCache) {
    Objects.requireNonNull(
      iCryptographicMaterialsCache,
      "Missing value for required argument `iCryptographicMaterialsCache`"
    );
    if (
      iCryptographicMaterialsCache instanceof
      software.amazon.cryptography.materialproviders.CryptographicMaterialsCache
    ) {
      return ((CryptographicMaterialsCache) iCryptographicMaterialsCache);
    }
    return CryptographicMaterialsCache.wrap(
      new NativeWrapper(iCryptographicMaterialsCache)
    );
  }

  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache impl() {
    return this._impl;
  }

  public void DeleteCacheEntry(DeleteCacheEntryInput input) {
    software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput dafnyValue =
      ToDafny.DeleteCacheEntryInput(input);
    Result<Tuple0, Error> result = this._impl.DeleteCacheEntry(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
  }

  public GetCacheEntryOutput GetCacheEntry(GetCacheEntryInput input) {
    software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput dafnyValue =
      ToDafny.GetCacheEntryInput(input);
    Result<
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput,
      Error
    > result = this._impl.GetCacheEntry(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.GetCacheEntryOutput(result.dtor_value());
  }

  public void PutCacheEntry(PutCacheEntryInput input) {
    software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput dafnyValue =
      ToDafny.PutCacheEntryInput(input);
    Result<Tuple0, Error> result = this._impl.PutCacheEntry(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
  }

  public void UpdateUsageMetadata(UpdateUsageMetadataInput input) {
    software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput dafnyValue =
      ToDafny.UpdateUsageMetadataInput(input);
    Result<Tuple0, Error> result = this._impl.UpdateUsageMetadata(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
  }

  protected static final class NativeWrapper
    implements
      software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache {

    protected final ICryptographicMaterialsCache _impl;

    NativeWrapper(ICryptographicMaterialsCache nativeImpl) {
      if (nativeImpl instanceof CryptographicMaterialsCache) {
        throw new IllegalArgumentException(
          "Recursive wrapping is strictly forbidden."
        );
      }
      this._impl = nativeImpl;
    }

    public Result<Tuple0, Error> DeleteCacheEntry(
      software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput dafnyInput
    ) {
      try {
        DeleteCacheEntryInput nativeInput = ToNative.DeleteCacheEntryInput(
          dafnyInput
        );
        this._impl.DeleteCacheEntry(nativeInput);
        return Result.create_Success(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          Tuple0.create()
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<Tuple0, Error> DeleteCacheEntry_k(
      software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput,
      Error
    > GetCacheEntry(
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput dafnyInput
    ) {
      try {
        GetCacheEntryInput nativeInput = ToNative.GetCacheEntryInput(
          dafnyInput
        );
        GetCacheEntryOutput nativeOutput =
          this._impl.GetCacheEntry(nativeInput);
        software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput dafnyOutput =
          ToDafny.GetCacheEntryOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput,
      Error
    > GetCacheEntry_k(
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<Tuple0, Error> PutCacheEntry(
      software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput dafnyInput
    ) {
      try {
        PutCacheEntryInput nativeInput = ToNative.PutCacheEntryInput(
          dafnyInput
        );
        this._impl.PutCacheEntry(nativeInput);
        return Result.create_Success(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          Tuple0.create()
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<Tuple0, Error> PutCacheEntry_k(
      software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<Tuple0, Error> UpdateUsageMetadata(
      software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput dafnyInput
    ) {
      try {
        UpdateUsageMetadataInput nativeInput =
          ToNative.UpdateUsageMetadataInput(dafnyInput);
        this._impl.UpdateUsageMetadata(nativeInput);
        return Result.create_Success(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          Tuple0.create()
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          dafny.Tuple0._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<Tuple0, Error> UpdateUsageMetadata_k(
      software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
