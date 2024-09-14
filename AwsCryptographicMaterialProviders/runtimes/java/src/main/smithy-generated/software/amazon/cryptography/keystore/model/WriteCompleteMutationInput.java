// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class WriteCompleteMutationInput {

  private final String Identifier;

  private final ByteBuffer Original;

  private final ByteBuffer Terminal;

  protected WriteCompleteMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
  }

  public String Identifier() {
    return this.Identifier;
  }

  public ByteBuffer Original() {
    return this.Original;
  }

  public ByteBuffer Terminal() {
    return this.Terminal;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Identifier(String Identifier);

    String Identifier();

    Builder Original(ByteBuffer Original);

    ByteBuffer Original();

    Builder Terminal(ByteBuffer Terminal);

    ByteBuffer Terminal();

    WriteCompleteMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected ByteBuffer Original;

    protected ByteBuffer Terminal;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteCompleteMutationInput model) {
      this.Identifier = model.Identifier();
      this.Original = model.Original();
      this.Terminal = model.Terminal();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Original(ByteBuffer Original) {
      this.Original = Original;
      return this;
    }

    public ByteBuffer Original() {
      return this.Original;
    }

    public Builder Terminal(ByteBuffer Terminal) {
      this.Terminal = Terminal;
      return this;
    }

    public ByteBuffer Terminal() {
      return this.Terminal;
    }

    public WriteCompleteMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Original())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Original`"
        );
      }
      if (Objects.isNull(this.Terminal())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Terminal`"
        );
      }
      return new WriteCompleteMutationInput(this);
    }
  }
}
