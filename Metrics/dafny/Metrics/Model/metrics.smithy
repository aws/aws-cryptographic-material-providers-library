namespace aws.cryptography.metrics

use aws.polymorph#localService
use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable

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
    MetricsChainError,
    MetricsServiceError
  ]
}

structure MetricsLoggerConfig {}

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

@error("client")
structure MetricsServiceError {
  @required
  message: String
}