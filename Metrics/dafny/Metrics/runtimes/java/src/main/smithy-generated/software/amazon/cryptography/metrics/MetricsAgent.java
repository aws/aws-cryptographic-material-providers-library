// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.util.Objects;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.model.PutCountInput;
import software.amazon.cryptography.metrics.model.PutDateInput;
import software.amazon.cryptography.metrics.model.PutOutput;
import software.amazon.cryptography.metrics.model.PutPropertyInput;
import software.amazon.cryptography.metrics.model.PutTimeInput;

public final class MetricsAgent implements IMetricsAgent {

  private final software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent _impl;

  private MetricsAgent(
    software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent iMetricsAgent
  ) {
    Objects.requireNonNull(
      iMetricsAgent,
      "Missing value for required argument `iMetricsAgent`"
    );
    this._impl = iMetricsAgent;
  }

  public static MetricsAgent wrap(
    software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent iMetricsAgent
  ) {
    return new MetricsAgent(iMetricsAgent);
  }

  public static <I extends IMetricsAgent> MetricsAgent wrap(I iMetricsAgent) {
    Objects.requireNonNull(
      iMetricsAgent,
      "Missing value for required argument `iMetricsAgent`"
    );
    if (
      iMetricsAgent instanceof software.amazon.cryptography.metrics.MetricsAgent
    ) {
      return ((MetricsAgent) iMetricsAgent);
    }
    return MetricsAgent.wrap(new NativeWrapper(iMetricsAgent));
  }

  public software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent impl() {
    return this._impl;
  }

  public PutOutput PutCount(PutCountInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PutCountInput dafnyValue =
      ToDafny.PutCountInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > result = this._impl.PutCount(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PutOutput(result.dtor_value());
  }

  public PutOutput PutDate(PutDateInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PutDateInput dafnyValue =
      ToDafny.PutDateInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > result = this._impl.PutDate(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PutOutput(result.dtor_value());
  }

  public PutOutput PutProperty(PutPropertyInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput dafnyValue =
      ToDafny.PutPropertyInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > result = this._impl.PutProperty(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PutOutput(result.dtor_value());
  }

  public PutOutput PutTime(PutTimeInput input) {
    software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput dafnyValue =
      ToDafny.PutTimeInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > result = this._impl.PutTime(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.PutOutput(result.dtor_value());
  }

  protected static final class NativeWrapper
    implements
      software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent {

    protected final IMetricsAgent _impl;

    NativeWrapper(IMetricsAgent nativeImpl) {
      if (nativeImpl instanceof MetricsAgent) {
        throw new IllegalArgumentException(
          "Recursive wrapping is strictly forbidden."
        );
      }
      this._impl = nativeImpl;
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > PutCount(
      software.amazon.cryptography.metrics.internaldafny.types.PutCountInput dafnyInput
    ) {
      try {
        PutCountInput nativeInput = ToNative.PutCountInput(dafnyInput);
        PutOutput nativeOutput = this._impl.PutCount(nativeInput);
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
    > PutCount_k(
      software.amazon.cryptography.metrics.internaldafny.types.PutCountInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > PutDate(
      software.amazon.cryptography.metrics.internaldafny.types.PutDateInput dafnyInput
    ) {
      try {
        PutDateInput nativeInput = ToNative.PutDateInput(dafnyInput);
        PutOutput nativeOutput = this._impl.PutDate(nativeInput);
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
    > PutDate_k(
      software.amazon.cryptography.metrics.internaldafny.types.PutDateInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > PutProperty(
      software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput dafnyInput
    ) {
      try {
        PutPropertyInput nativeInput = ToNative.PutPropertyInput(dafnyInput);
        PutOutput nativeOutput = this._impl.PutProperty(nativeInput);
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
    > PutProperty_k(
      software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }

    public Result<
      software.amazon.cryptography.metrics.internaldafny.types.PutOutput,
      Error
    > PutTime(
      software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput dafnyInput
    ) {
      try {
        PutTimeInput nativeInput = ToNative.PutTimeInput(dafnyInput);
        PutOutput nativeOutput = this._impl.PutTime(nativeInput);
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
    > PutTime_k(
      software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput dafnyInput
    ) {
      throw new RuntimeException("Not supported at this time.");
    }
  }
}
