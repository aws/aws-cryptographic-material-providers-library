namespace aws.cryptography.metrics

use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable

@aws.polymorph#localService(
  sdkId: "Metrics",
  config: MetricsConfig
)
service AwsCryptographicMetrics {
  version: "2023-04-01",
  resources: [MetricsAgent],
  operations: [
    CreateMultiMetricsAgent
  ],
  errors: [
    MetricsPutError,
    MetricsPublishError,
    MetricsServiceError
  ]
}

structure MetricsConfig {}