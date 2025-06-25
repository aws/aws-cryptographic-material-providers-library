namespace aws.cryptography.metrics

use aws.polymorph#reference
use aws.polymorph#extendable

@extendable
resource MetricsAgent {
  operations: [
    PutDate,
    PutTime,
    PutCount,
    PutProperty
  ]
}

// Operations for different metric types
operation PutDate {
  input: PutDateInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

operation PutTime {
  input: PutTimeInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

operation PutCount {
  input: PutCountInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

operation PutProperty {
  input: PutPropertyInput,
  output: PutOutput,
  errors: [MetricsPutError]
}

// Input structures for each operation with flattened values
structure PutDateInput {
  @required
  description: String,
  @required
  date: Timestamp,
  transactionId: String
}

structure PutTimeInput {
  @required
  description: String,
  @required
  duration: Long,  // Duration in milliseconds
  transactionId: String
}

structure PutCountInput {
  @required
  description: String,
  @required
  count: Long,
  transactionId: String
}

structure PutPropertyInput {
  @required
  description: String,
  @required
  value: String,
  transactionId: String
}

// Common output structure
structure PutOutput {}

@error("client")
structure MetricsPutError {
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

@reference(resource: MetricsAgent)
structure MetricsAgentReference {}

list MetricsAgentList {
  member: MetricsAgentReference
}

// MultiMetricsAgent Constructor
operation CreateMultiMetricsAgent {
    input: CreateMetricsAgentInput,
    output: CreateMetricsAgentOutput
}

structure CreateMetricsAgentInput {
    @required 
    metricsAgents: MetricsAgentList
}

structure CreateMetricsAgentOutput {
    @required
    metricsAgent: MetricsAgentReference
}