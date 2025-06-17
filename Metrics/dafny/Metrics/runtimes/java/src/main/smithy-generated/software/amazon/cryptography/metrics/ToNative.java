// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import dafny.DafnySequence;
import java.lang.RuntimeException;
import java.util.List;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.internaldafny.types.Error_CollectionOfErrors;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsPublishError;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsPutError;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsServiceError;
import software.amazon.cryptography.metrics.internaldafny.types.Error_Opaque;
import software.amazon.cryptography.metrics.internaldafny.types.Error_OpaqueWithText;
import software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient;
import software.amazon.cryptography.metrics.model.CollectionOfErrors;
import software.amazon.cryptography.metrics.model.CreateLoggerOutput;
import software.amazon.cryptography.metrics.model.CreateMetricsAgentInput;
import software.amazon.cryptography.metrics.model.CreateMetricsAgentOutput;
import software.amazon.cryptography.metrics.model.CreateTextLoggerInput;
import software.amazon.cryptography.metrics.model.CreateTextMetricsAgentInput;
import software.amazon.cryptography.metrics.model.MetricsConfig;
import software.amazon.cryptography.metrics.model.MetricsPublishError;
import software.amazon.cryptography.metrics.model.MetricsPutError;
import software.amazon.cryptography.metrics.model.MetricsServiceError;
import software.amazon.cryptography.metrics.model.OpaqueError;
import software.amazon.cryptography.metrics.model.OpaqueWithTextError;
import software.amazon.cryptography.metrics.model.PublishInput;
import software.amazon.cryptography.metrics.model.PublishOutput;
import software.amazon.cryptography.metrics.model.PutCountInput;
import software.amazon.cryptography.metrics.model.PutDateInput;
import software.amazon.cryptography.metrics.model.PutInput;
import software.amazon.cryptography.metrics.model.PutOutput;
import software.amazon.cryptography.metrics.model.PutPropertyInput;
import software.amazon.cryptography.metrics.model.PutTimeInput;

public class ToNative {

  public static OpaqueError Error(Error_Opaque dafnyValue) {
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    return nativeBuilder.build();
  }

  public static OpaqueWithTextError Error(Error_OpaqueWithText dafnyValue) {
    OpaqueWithTextError.Builder nativeBuilder = OpaqueWithTextError.builder();
    nativeBuilder.obj(dafnyValue.dtor_obj());
    nativeBuilder.objMessage(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_objMessage()
      )
    );
    return nativeBuilder.build();
  }

  public static CollectionOfErrors Error(Error_CollectionOfErrors dafnyValue) {
    CollectionOfErrors.Builder nativeBuilder = CollectionOfErrors.builder();
    nativeBuilder.list(
      software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
        dafnyValue.dtor_list(),
        ToNative::Error
      )
    );
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MetricsPublishError Error(
    Error_MetricsPublishError dafnyValue
  ) {
    MetricsPublishError.Builder nativeBuilder = MetricsPublishError.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MetricsPutError Error(Error_MetricsPutError dafnyValue) {
    MetricsPutError.Builder nativeBuilder = MetricsPutError.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static MetricsServiceError Error(
    Error_MetricsServiceError dafnyValue
  ) {
    MetricsServiceError.Builder nativeBuilder = MetricsServiceError.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static RuntimeException Error(Error dafnyValue) {
    if (dafnyValue.is_MetricsPublishError()) {
      return ToNative.Error((Error_MetricsPublishError) dafnyValue);
    }
    if (dafnyValue.is_MetricsPutError()) {
      return ToNative.Error((Error_MetricsPutError) dafnyValue);
    }
    if (dafnyValue.is_MetricsServiceError()) {
      return ToNative.Error((Error_MetricsServiceError) dafnyValue);
    }
    if (dafnyValue.is_Opaque()) {
      return ToNative.Error((Error_Opaque) dafnyValue);
    }
    if (dafnyValue.is_OpaqueWithText()) {
      return ToNative.Error((Error_OpaqueWithText) dafnyValue);
    }
    if (dafnyValue.is_CollectionOfErrors()) {
      return ToNative.Error((Error_CollectionOfErrors) dafnyValue);
    }
    OpaqueError.Builder nativeBuilder = OpaqueError.builder();
    nativeBuilder.obj(dafnyValue);
    return nativeBuilder.build();
  }

  public static CreateLoggerOutput CreateLoggerOutput(
    software.amazon.cryptography.metrics.internaldafny.types.CreateLoggerOutput dafnyValue
  ) {
    CreateLoggerOutput.Builder nativeBuilder = CreateLoggerOutput.builder();
    nativeBuilder.logger(ToNative.Logger(dafnyValue.dtor_logger()));
    return nativeBuilder.build();
  }

  public static CreateMetricsAgentInput CreateMetricsAgentInput(
    software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput dafnyValue
  ) {
    CreateMetricsAgentInput.Builder nativeBuilder =
      CreateMetricsAgentInput.builder();
    nativeBuilder.metricsAgents(
      ToNative.MetricsAgentList(dafnyValue.dtor_metricsAgents())
    );
    return nativeBuilder.build();
  }

  public static CreateMetricsAgentOutput CreateMetricsAgentOutput(
    software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput dafnyValue
  ) {
    CreateMetricsAgentOutput.Builder nativeBuilder =
      CreateMetricsAgentOutput.builder();
    nativeBuilder.metricsAgent(
      ToNative.MetricsAgent(dafnyValue.dtor_metricsAgent())
    );
    return nativeBuilder.build();
  }

  public static CreateTextLoggerInput CreateTextLoggerInput(
    software.amazon.cryptography.metrics.internaldafny.types.CreateTextLoggerInput dafnyValue
  ) {
    CreateTextLoggerInput.Builder nativeBuilder =
      CreateTextLoggerInput.builder();
    if (dafnyValue.dtor_fileName().is_Some()) {
      nativeBuilder.fileName(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_fileName().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static CreateTextMetricsAgentInput CreateTextMetricsAgentInput(
    software.amazon.cryptography.metrics.internaldafny.types.CreateTextMetricsAgentInput dafnyValue
  ) {
    CreateTextMetricsAgentInput.Builder nativeBuilder =
      CreateTextMetricsAgentInput.builder();
    nativeBuilder.fileName(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_fileName()
      )
    );
    return nativeBuilder.build();
  }

  public static MetricsConfig MetricsConfig(
    software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig dafnyValue
  ) {
    MetricsConfig.Builder nativeBuilder = MetricsConfig.builder();
    return nativeBuilder.build();
  }

  public static PublishInput PublishInput(
    software.amazon.cryptography.metrics.internaldafny.types.PublishInput dafnyValue
  ) {
    PublishInput.Builder nativeBuilder = PublishInput.builder();
    return nativeBuilder.build();
  }

  public static PublishOutput PublishOutput(
    software.amazon.cryptography.metrics.internaldafny.types.PublishOutput dafnyValue
  ) {
    PublishOutput.Builder nativeBuilder = PublishOutput.builder();
    return nativeBuilder.build();
  }

  public static PutCountInput PutCountInput(
    software.amazon.cryptography.metrics.internaldafny.types.PutCountInput dafnyValue
  ) {
    PutCountInput.Builder nativeBuilder = PutCountInput.builder();
    nativeBuilder.description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_description()
      )
    );
    nativeBuilder.count((dafnyValue.dtor_count()));
    if (dafnyValue.dtor_transactionId().is_Some()) {
      nativeBuilder.transactionId(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_transactionId().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static PutDateInput PutDateInput(
    software.amazon.cryptography.metrics.internaldafny.types.PutDateInput dafnyValue
  ) {
    PutDateInput.Builder nativeBuilder = PutDateInput.builder();
    nativeBuilder.description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_description()
      )
    );
    nativeBuilder.date(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.Date(
        dafnyValue.dtor_date()
      )
    );
    if (dafnyValue.dtor_transactionId().is_Some()) {
      nativeBuilder.transactionId(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_transactionId().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static PutInput PutInput(
    software.amazon.cryptography.metrics.internaldafny.types.PutInput dafnyValue
  ) {
    PutInput.Builder nativeBuilder = PutInput.builder();
    nativeBuilder.message(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_message()
      )
    );
    return nativeBuilder.build();
  }

  public static PutOutput PutOutput(
    software.amazon.cryptography.metrics.internaldafny.types.PutOutput dafnyValue
  ) {
    PutOutput.Builder nativeBuilder = PutOutput.builder();
    return nativeBuilder.build();
  }

  public static PutPropertyInput PutPropertyInput(
    software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput dafnyValue
  ) {
    PutPropertyInput.Builder nativeBuilder = PutPropertyInput.builder();
    nativeBuilder.description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_description()
      )
    );
    nativeBuilder.value(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_value()
      )
    );
    if (dafnyValue.dtor_transactionId().is_Some()) {
      nativeBuilder.transactionId(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_transactionId().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static PutTimeInput PutTimeInput(
    software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput dafnyValue
  ) {
    PutTimeInput.Builder nativeBuilder = PutTimeInput.builder();
    nativeBuilder.description(
      software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
        dafnyValue.dtor_description()
      )
    );
    nativeBuilder.duration((dafnyValue.dtor_duration()));
    if (dafnyValue.dtor_transactionId().is_Some()) {
      nativeBuilder.transactionId(
        software.amazon.smithy.dafny.conversion.ToNative.Simple.String(
          dafnyValue.dtor_transactionId().dtor_value()
        )
      );
    }
    return nativeBuilder.build();
  }

  public static List<IMetricsAgent> MetricsAgentList(
    DafnySequence<
      ? extends software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent
    > dafnyValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToNative.Aggregate.GenericToList(
      dafnyValue,
      software.amazon.cryptography.metrics.ToNative::MetricsAgent
    );
  }

  public static ILogger Logger(
    software.amazon.cryptography.metrics.internaldafny.types.ILogger dafnyValue
  ) {
    if (dafnyValue instanceof Logger.NativeWrapper) {
      return ((Logger.NativeWrapper) dafnyValue)._impl;
    }
    return Logger.wrap(dafnyValue);
  }

  public static IMetricsAgent MetricsAgent(
    software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent dafnyValue
  ) {
    if (dafnyValue instanceof MetricsAgent.NativeWrapper) {
      return ((MetricsAgent.NativeWrapper) dafnyValue)._impl;
    }
    return MetricsAgent.wrap(dafnyValue);
  }

  public static Metrics AwsCryptographicMetrics(
    IAwsCryptographicMetricsClient dafnyValue
  ) {
    return new Metrics(dafnyValue);
  }
}
