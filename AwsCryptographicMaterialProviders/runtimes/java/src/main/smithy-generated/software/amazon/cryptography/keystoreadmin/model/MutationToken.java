// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class MutationToken {

  /**
   * The identifier for the Branch Key being mutated.
   */
  private final String Identifier;

  /**
   * Describes the original state of the Branch Key.
   */
  private final ByteBuffer Original;

  /**
   * Describes the terminal (or final) state of the Branch Key.
   */
  private final ByteBuffer Terminal;

  /**
   * Indirectly describes which items have already been mutated. Used to determine where to continue applying mutations.
   */
  private final ByteBuffer ExclusiveStartKey;

  /**
   * UUID of the Mutation Lock. If not provided, a Query will be issued to find the Mutation Lock.
   */
  private final String UUID;

  /**
   * ISO 8601 time when the mutation was initialized.
   */
  private final String CreateTime;

  protected MutationToken(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
    this.ExclusiveStartKey = builder.ExclusiveStartKey();
    this.UUID = builder.UUID();
    this.CreateTime = builder.CreateTime();
  }

  /**
   * @return The identifier for the Branch Key being mutated.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return Describes the original state of the Branch Key.
   */
  public ByteBuffer Original() {
    return this.Original;
  }

  /**
   * @return Describes the terminal (or final) state of the Branch Key.
   */
  public ByteBuffer Terminal() {
    return this.Terminal;
  }

  /**
   * @return Indirectly describes which items have already been mutated. Used to determine where to continue applying mutations.
   */
  public ByteBuffer ExclusiveStartKey() {
    return this.ExclusiveStartKey;
  }

  /**
   * @return UUID of the Mutation Lock. If not provided, a Query will be issued to find the Mutation Lock.
   */
  public String UUID() {
    return this.UUID;
  }

  /**
   * @return ISO 8601 time when the mutation was initialized.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key being mutated.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key being mutated.
     */
    String Identifier();

    /**
     * @param Original Describes the original state of the Branch Key.
     */
    Builder Original(ByteBuffer Original);

    /**
     * @return Describes the original state of the Branch Key.
     */
    ByteBuffer Original();

    /**
     * @param Terminal Describes the terminal (or final) state of the Branch Key.
     */
    Builder Terminal(ByteBuffer Terminal);

    /**
     * @return Describes the terminal (or final) state of the Branch Key.
     */
    ByteBuffer Terminal();

    /**
     * @param ExclusiveStartKey Indirectly describes which items have already been mutated. Used to determine where to continue applying mutations.
     */
    Builder ExclusiveStartKey(ByteBuffer ExclusiveStartKey);

    /**
     * @return Indirectly describes which items have already been mutated. Used to determine where to continue applying mutations.
     */
    ByteBuffer ExclusiveStartKey();

    /**
     * @param UUID UUID of the Mutation Lock. If not provided, a Query will be issued to find the Mutation Lock.
     */
    Builder UUID(String UUID);

    /**
     * @return UUID of the Mutation Lock. If not provided, a Query will be issued to find the Mutation Lock.
     */
    String UUID();

    /**
     * @param CreateTime ISO 8601 time when the mutation was initialized.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return ISO 8601 time when the mutation was initialized.
     */
    String CreateTime();

    MutationToken build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected ByteBuffer Original;

    protected ByteBuffer Terminal;

    protected ByteBuffer ExclusiveStartKey;

    protected String UUID;

    protected String CreateTime;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationToken model) {
      this.Identifier = model.Identifier();
      this.Original = model.Original();
      this.Terminal = model.Terminal();
      this.ExclusiveStartKey = model.ExclusiveStartKey();
      this.UUID = model.UUID();
      this.CreateTime = model.CreateTime();
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

    public Builder ExclusiveStartKey(ByteBuffer ExclusiveStartKey) {
      this.ExclusiveStartKey = ExclusiveStartKey;
      return this;
    }

    public ByteBuffer ExclusiveStartKey() {
      return this.ExclusiveStartKey;
    }

    public Builder UUID(String UUID) {
      this.UUID = UUID;
      return this;
    }

    public String UUID() {
      return this.UUID;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public MutationToken build() {
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
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      return new MutationToken(this);
    }
  }
}
