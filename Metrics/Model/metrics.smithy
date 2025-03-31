namespace aws.cryptography.metrics

use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable

@aws.polymorph#localService(
  sdkId: "MetricsLogger",
  config: MetricsLoggerConfig
)
service MetricsPublisher {
  version: "2025-12-01",
  resources: [MetricsLogger],
  errors: [
    MetricsPutError,
    MetricsChainError
  ]
}

structure MetricsLoggerConfig {}

@extendable
resource MetricsLogger {
  operations: [Put]
}

@reference(resource: MetricsLogger)
structure MetricsLoggerReference {}

list MetricsLoggerList {
  member: MetricsLoggerReference 
}

structure Metrics {
  @required
  logger: MetricsLoggerList,
  @required
  transactionId: String
}

operation Put {
  input: PutInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

operation Chain {
  input: ChainInput,
  output: ChainOutput,
  errors: [MetricsChainError]
}

structure PutInput {
  @required
  logger: Metrics,

  @required
  message: String
}

structure PutOutput {
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