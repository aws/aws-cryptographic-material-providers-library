namespace aws.cryptography.metrics

use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable

@extendable
resource Logger {
  operations: [
    Put,
    Publish,
    // Chain?
  ]
}

@reference(resource: Logger)
structure MetricsLoggerReference {}

structure CreateLoggerOutput {
  @required
  logger: MetricsLoggerReference
}

operation Put {
  input: PutInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

structure PutInput {
  @required
  message: String
}

structure PutOutput {
}

operation Publish {
  input: PublishInput,
  output: PublishOutput,
  errors: [MetricsPublishError]
}

structure PublishInput {}

structure PublishOutput {}

operation CreateTextLogger {
  input: CreateTextLoggerInput,
  output: CreateLoggerOutput
}

structure CreateTextLoggerInput {
  fileName: String
} 