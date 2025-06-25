// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.model.PublishInput;
import software.amazon.cryptography.metrics.model.PublishOutput;
import software.amazon.cryptography.metrics.model.PutInput;
import software.amazon.cryptography.metrics.model.PutOutput;

public final class Logger implements ILogger {

  private final software.amazon.cryptography.metrics.internaldafny.types.ILogger _impl;

  private Logger(
    software.amazon.cryptography.metrics.internaldafny.types.ILogger iLogger
  ) {
    Objects.requireNonNull(
      iLogger,
      "Missing value for required argument `iLogger`"
    );
    this._impl = iLogger;
  }

  public static Logger wrap(
    software.amazon.cryptography.metrics.internaldafny.types.ILogger iLogger
  ) {
    return new Logger(iLogger);
  }

  public static <I extends ILogger> Logger wrap(I iLogger) {
    Objects.requireNonNull(
      iLogger,
      "Missing value for required argument `iLogger`"
    );
    if (iLogger instanceof software.amazon.cryptography.metrics.Logger) {
      return ((Logger) iLogger);
    }
    return Logger.wrap(new NativeWrapper(iLogger));
  }

  public software.amazon.cryptography.metrics.internaldafny.types.ILogger impl() {
    return this._impl;
  }

  public PublishOutput Publish(PublishInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PublishInput dafnyValue =
      ToDafny.PublishInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PublishOutput,
      Error
    > result = this._impl.Publish(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PublishOutput(result.dtor_value());
  }

  public PutOutput Put(PutInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PutInput dafnyValue =
      ToDafny.PutInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > result = this._impl.Put(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PutOutput(result.dtor_value());
  }

  protected static final class NativeWrapper
    implements
      software.amazon.cryptography.metrics.internaldafny.types.ILogger {

    protected final ILogger _impl;

    NativeWrapper(ILogger nativeImpl) {
      if (nativeImpl instanceof Logger) {
        throw new IllegalArgumentException(
          "Recursive wrapping is strictly forbidden."
        );
      }
      this._impl = nativeImpl;
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PublishOutput,
      Error
    > Publish(
      software.amazon.cryptography.metrics.internaldafny.types.PublishInput dafnyInput
    ) {
      try {
        PublishInput nativeInput = ToNative.PublishInput(dafnyInput);
        PublishOutput nativeOutput = this._impl.Publish(nativeInput);
        software.amazon.cryptography.metrics.internaldafny.types.PublishOutput dafnyOutput =
          ToDafny.PublishOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.metrics.internaldafny.types.PublishOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.metrics.internaldafny.types.PublishOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PublishOutput,
      Error
    > Publish_k(
      software.amazon.cryptography.metrics.internaldafny.types.PublishInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > Put(
      software.amazon.cryptography.metrics.internaldafny.types.PutInput dafnyInput
    ) {
      try {
        PutInput nativeInput = ToNative.PutInput(dafnyInput);
        PutOutput nativeOutput = this._impl.Put(nativeInput);
        software.amazon.cryptography.metrics.internaldafny.types.PutOutput dafnyOutput =
          ToDafny.PutOutput(nativeOutput);
        return Result.create_Success(
          software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(),
          Error._typeDescriptor(),
          dafnyOutput
        );
      } catch (RuntimeException ex) {
        return Result.create_Failure(
          software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(),
          Error._typeDescriptor(),
          ToDafny.Error(ex)
        );
      }
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > Put_k(
      software.amazon.cryptography.metrics.internaldafny.types.PutInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
