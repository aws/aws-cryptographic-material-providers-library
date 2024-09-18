// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Information on an in-flight Mutation of a Branch Key.
 * This ensures:
 * - only one Mutation affects a Branch Key at a time
 * - all items of a Branch Key are mutated consistently
 */
public class MutationCommitment {

  /**
   * The Branch Key under Mutation.
   */
  private final String Identifier;

  /**
   * The create time as an ISO 8061 UTC string.
   */
  private final String CreateTime;

  /**
   * A unique identifier for the Mutation.
   */
  private final String UUID;

  /**
   * A commitment of the Original Mutable Properties of the Branch Key.
   */
  private final ByteBuffer Original;

  /**
   * A commitment of the Terminal Mutable Properties of the Branch Key.
   */
  private final ByteBuffer Terminal;

  /**
   * Description of the input to initialize a Mutation.
   */
  private final ByteBuffer Input;

  private final ByteBuffer CiphertextBlob;

  protected MutationCommitment(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.CreateTime = builder.CreateTime();
    this.UUID = builder.UUID();
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
    this.Input = builder.Input();
    this.CiphertextBlob = builder.CiphertextBlob();
  }

  /**
   * @return The Branch Key under Mutation.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The create time as an ISO 8061 UTC string.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  /**
   * @return A unique identifier for the Mutation.
   */
  public String UUID() {
    return this.UUID;
  }

  /**
   * @return A commitment of the Original Mutable Properties of the Branch Key.
   */
  public ByteBuffer Original() {
    return this.Original;
  }

  /**
   * @return A commitment of the Terminal Mutable Properties of the Branch Key.
   */
  public ByteBuffer Terminal() {
    return this.Terminal;
  }

  /**
   * @return Description of the input to initialize a Mutation.
   */
  public ByteBuffer Input() {
    return this.Input;
  }

  public ByteBuffer CiphertextBlob() {
    return this.CiphertextBlob;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The Branch Key under Mutation.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Branch Key under Mutation.
     */
    String Identifier();

    /**
     * @param CreateTime The create time as an ISO 8061 UTC string.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return The create time as an ISO 8061 UTC string.
     */
    String CreateTime();

    /**
     * @param UUID A unique identifier for the Mutation.
     */
    Builder UUID(String UUID);

    /**
     * @return A unique identifier for the Mutation.
     */
    String UUID();

    /**
     * @param Original A commitment of the Original Mutable Properties of the Branch Key.
     */
    Builder Original(ByteBuffer Original);

    /**
     * @return A commitment of the Original Mutable Properties of the Branch Key.
     */
    ByteBuffer Original();

    /**
     * @param Terminal A commitment of the Terminal Mutable Properties of the Branch Key.
     */
    Builder Terminal(ByteBuffer Terminal);

    /**
     * @return A commitment of the Terminal Mutable Properties of the Branch Key.
     */
    ByteBuffer Terminal();

    /**
     * @param Input Description of the input to initialize a Mutation.
     */
    Builder Input(ByteBuffer Input);

    /**
     * @return Description of the input to initialize a Mutation.
     */
    ByteBuffer Input();

    Builder CiphertextBlob(ByteBuffer CiphertextBlob);

    ByteBuffer CiphertextBlob();

    MutationCommitment build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected String CreateTime;

    protected String UUID;

    protected ByteBuffer Original;

    protected ByteBuffer Terminal;

    protected ByteBuffer Input;

    protected ByteBuffer CiphertextBlob;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationCommitment model) {
      this.Identifier = model.Identifier();
      this.CreateTime = model.CreateTime();
      this.UUID = model.UUID();
      this.Original = model.Original();
      this.Terminal = model.Terminal();
      this.Input = model.Input();
      this.CiphertextBlob = model.CiphertextBlob();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public Builder UUID(String UUID) {
      this.UUID = UUID;
      return this;
    }

    public String UUID() {
      return this.UUID;
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

    public Builder Input(ByteBuffer Input) {
      this.Input = Input;
      return this;
    }

    public ByteBuffer Input() {
      return this.Input;
    }

    public Builder CiphertextBlob(ByteBuffer CiphertextBlob) {
      this.CiphertextBlob = CiphertextBlob;
      return this;
    }

    public ByteBuffer CiphertextBlob() {
      return this.CiphertextBlob;
    }

    public MutationCommitment build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      if (Objects.isNull(this.UUID())) {
        throw new IllegalArgumentException(
          "Missing value for required field `UUID`"
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
      if (Objects.isNull(this.Input())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Input`"
        );
      }
      if (Objects.isNull(this.CiphertextBlob())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CiphertextBlob`"
        );
      }
      return new MutationCommitment(this);
    }
  }
}
