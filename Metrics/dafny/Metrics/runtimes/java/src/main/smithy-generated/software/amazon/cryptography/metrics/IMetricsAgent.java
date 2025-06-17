// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import software.amazon.cryptography.metrics.model.PutCountInput;
import software.amazon.cryptography.metrics.model.PutDateInput;
import software.amazon.cryptography.metrics.model.PutOutput;
import software.amazon.cryptography.metrics.model.PutPropertyInput;
import software.amazon.cryptography.metrics.model.PutTimeInput;

public interface IMetricsAgent {
  PutOutput PutCount(PutCountInput input);

  PutOutput PutDate(PutDateInput input);

  PutOutput PutProperty(PutPropertyInput input);

  PutOutput PutTime(PutTimeInput input);
}
