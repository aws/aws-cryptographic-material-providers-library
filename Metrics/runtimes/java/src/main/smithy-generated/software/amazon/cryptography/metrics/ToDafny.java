// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import Wrappers_Compile.Option;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Character;
import java.lang.Long;
import java.lang.RuntimeException;
import java.util.List;
import java.util.Objects;
import software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput;
import software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsPublishError;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsPutError;
import software.amazon.cryptography.metrics.internaldafny.types.Error_MetricsServiceError;
import software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient;
import software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig;
import software.amazon.cryptography.metrics.internaldafny.types.PutCountInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutDateInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutOutput;
import software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput;
import software.amazon.cryptography.metrics.model.CollectionOfErrors;
import software.amazon.cryptography.metrics.model.MetricsPublishError;
import software.amazon.cryptography.metrics.model.MetricsPutError;
import software.amazon.cryptography.metrics.model.MetricsServiceError;
import software.amazon.cryptography.metrics.model.OpaqueError;
import software.amazon.cryptography.metrics.model.OpaqueWithTextError;

public class ToDafny {

  public static Error Error(RuntimeException nativeValue) {
    if (nativeValue instanceof MetricsPublishError) {
      return ToDafny.Error((MetricsPublishError) nativeValue);
    }
    if (nativeValue instanceof MetricsPutError) {
      return ToDafny.Error((MetricsPutError) nativeValue);
    }
    if (nativeValue instanceof MetricsServiceError) {
      return ToDafny.Error((MetricsServiceError) nativeValue);
    }
    if (nativeValue instanceof OpaqueError) {
      return ToDafny.Error((OpaqueError) nativeValue);
    }
    if (nativeValue instanceof OpaqueWithTextError) {
      return ToDafny.Error((OpaqueWithTextError) nativeValue);
    }
    if (nativeValue instanceof CollectionOfErrors) {
      return ToDafny.Error((CollectionOfErrors) nativeValue);
    }
    return Error.create_Opaque(nativeValue);
  }

  public static Error Error(OpaqueError nativeValue) {
    return Error.create_Opaque(nativeValue.obj());
  }

  public static Error Error(OpaqueWithTextError nativeValue) {
    return Error.create_OpaqueWithText(
      nativeValue.obj(),
      dafny.DafnySequence.asString(nativeValue.objMessage())
    );
  }

  public static Error Error(CollectionOfErrors nativeValue) {
    DafnySequence<? extends Error> list =
      software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
        nativeValue.list(),
        ToDafny::Error,
        Error._typeDescriptor()
      );
    DafnySequence<? extends Character> message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.getMessage()
      );
    return Error.create_CollectionOfErrors(list, message);
  }

  public static CreateMetricsAgentInput CreateMetricsAgentInput(
    software.amazon.cryptography.metrics.model.CreateMetricsAgentInput nativeValue
  ) {
    DafnySequence<
      ? extends software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent
    > metricsAgents;
    metricsAgents = ToDafny.MetricsAgentList(nativeValue.metricsAgents());
    return new CreateMetricsAgentInput(metricsAgents);
  }

  public static CreateMetricsAgentOutput CreateMetricsAgentOutput(
    software.amazon.cryptography.metrics.model.CreateMetricsAgentOutput nativeValue
  ) {
    software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent metricsAgent;
    metricsAgent = ToDafny.MetricsAgent(nativeValue.metricsAgent());
    return new CreateMetricsAgentOutput(metricsAgent);
  }

  public static MetricsConfig MetricsConfig(
    software.amazon.cryptography.metrics.model.MetricsConfig nativeValue
  ) {
    return new MetricsConfig();
  }

  public static PutCountInput PutCountInput(
    software.amazon.cryptography.metrics.model.PutCountInput nativeValue
  ) {
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    Long count;
    count = (nativeValue.count());
    Option<DafnySequence<? extends Character>> transactionId;
    transactionId =
      Objects.nonNull(nativeValue.transactionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.transactionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PutCountInput(description, count, transactionId);
  }

  public static PutDateInput PutDateInput(
    software.amazon.cryptography.metrics.model.PutDateInput nativeValue
  ) {
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    DafnySequence<? extends Character> date;
    date =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.date()
      );
    Option<DafnySequence<? extends Character>> transactionId;
    transactionId =
      Objects.nonNull(nativeValue.transactionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.transactionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PutDateInput(description, date, transactionId);
  }

  public static PutOutput PutOutput(
    software.amazon.cryptography.metrics.model.PutOutput nativeValue
  ) {
    return new PutOutput();
  }

  public static PutPropertyInput PutPropertyInput(
    software.amazon.cryptography.metrics.model.PutPropertyInput nativeValue
  ) {
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    DafnySequence<? extends Character> value;
    value =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.value()
      );
    Option<DafnySequence<? extends Character>> transactionId;
    transactionId =
      Objects.nonNull(nativeValue.transactionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.transactionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PutPropertyInput(description, value, transactionId);
  }

  public static PutTimeInput PutTimeInput(
    software.amazon.cryptography.metrics.model.PutTimeInput nativeValue
  ) {
    DafnySequence<? extends Character> description;
    description =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.description()
      );
    Long duration;
    duration = (nativeValue.duration());
    Option<DafnySequence<? extends Character>> transactionId;
    transactionId =
      Objects.nonNull(nativeValue.transactionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.transactionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PutTimeInput(description, duration, transactionId);
  }

  public static Error Error(MetricsPublishError nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MetricsPublishError(message);
  }

  public static Error Error(MetricsPutError nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MetricsPutError(message);
  }

  public static Error Error(MetricsServiceError nativeValue) {
    DafnySequence<? extends Character> message;
    message =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.message()
      );
    return new Error_MetricsServiceError(message);
  }

  public static DafnySequence<
    ? extends software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent
  > MetricsAgentList(List<IMetricsAgent> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.metrics.ToDafny::MetricsAgent,
      TypeDescriptor.reference(
        software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent.class
      )
    );
  }

  public static software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent MetricsAgent(
    IMetricsAgent nativeValue
  ) {
    return MetricsAgent.wrap(nativeValue).impl();
  }

  public static IAwsCryptographicMetricsClient AwsCryptographicMetrics(
    Metrics nativeValue
  ) {
    return nativeValue.impl();
  }
}
