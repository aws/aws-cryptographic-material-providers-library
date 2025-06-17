// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import software.amazon.cryptography.metrics.model.PublishInput;
import software.amazon.cryptography.metrics.model.PublishOutput;
import software.amazon.cryptography.metrics.model.PutInput;
import software.amazon.cryptography.metrics.model.PutOutput;

public interface ILogger {
  PublishOutput Publish(PublishInput input);

  PutOutput Put(PutInput input);
}
