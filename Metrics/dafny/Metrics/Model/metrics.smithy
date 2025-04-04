namespace aws.cryptography.metrics

use aws.polymorph#localService
use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable

@range(min: 1)
integer CountingNumber

@aws.polymorph#localService(
  sdkId: "MetricsLogger",
  config: MetricsLoggerConfig
)
service AwsCryptographicMetrics {
  version: "2023-04-01",
  resources: [Logger],
  operations: [
    CreateTextLogger,
    // CreateAwsCloudWatchLogger
  ],
  errors: [
    MetricsPutError,
    MetricsPublishError,
    MetricsChainError
  ]
}

union PublishingCriteria {
  TimeLimit: SecondLimitInput,
  MessageLimit: MessageLimitInput,
  OperationLimit: OperationLimitInput,
}

structure MetricsLoggerConfig {
  Logger: MetricsLoggerReference,
  PublishingCriteria: PublishingCriteria 
}

structure SecondLimitInput {
  @required
  interval: CountingNumber,
  @required
  timeUnits: TimeUnits
}

structure MessageLimitInput {
  @required
  @range(min: 1, max: 100)
  numberOfMessages: Integer
}

structure OperationLimitInput {
  @required
  endOfOperation: Boolean
}

structure Metrics {
  @required
  logger: MetricsLoggerReference,
  @required
  transactionId: String
}

operation Chain {
  input: ChainInput,
  output: ChainOutput,
  errors: [MetricsChainError]
}

structure ChainInput {
  @required
  chainedLogger: Metrics,

  @required
  newLogger: Metrics,
}

structure ChainOutput {
  @required
  newChainedLogger: Metrics
}

@error("client")
structure MetricsPutError {
  @required
  message: String,
} 

@error("client")
structure MetricsChainError {
  @required
  message: String,
}

@error("client")
structure MetricsPublishError {
  @required
  message: String
}

@enum([
  {
    name: "Seconds",
    value: "Seconds",
  },
  {
    name: "Milliseconds",
    value: "Milliseconds",
  },
])
string TimeUnits