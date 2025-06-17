// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

public class CreateTextLoggerInput {

  private final String fileName;

  protected CreateTextLoggerInput(BuilderImpl builder) {
    this.fileName = builder.fileName();
  }

  public String fileName() {
    return this.fileName;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder fileName(String fileName);

    String fileName();

    CreateTextLoggerInput build();
  }

  static class BuilderImpl implements Builder {

    protected String fileName;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateTextLoggerInput model) {
      this.fileName = model.fileName();
    }

    public Builder fileName(String fileName) {
      this.fileName = fileName;
      return this;
    }

    public String fileName() {
      return this.fileName;
    }

    public CreateTextLoggerInput build() {
      return new CreateTextLoggerInput(this);
    }
  }
}
