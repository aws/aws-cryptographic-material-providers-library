// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.List;
import java.util.Objects;

public class WriteMutatedVersionsInput {

  /**
   * List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  private final List<EncryptedHierarchicalKey> items;

  /**
   * The Identifier of the Branch Key.
   */
  private final String Identifier;

  /**
   * A commitment of the Original Mutable Properities of the Branch Key.
   */
  private final ByteBuffer Original;

  /**
   * A commitment of the Terminal Mutable Properities of the Branch Key.
   */
  private final ByteBuffer Terminal;

  /**
   * If set to True, the Mutation Lock will be deleted. Effectively defaults to false
   */
  private final Boolean CompleteMutation;

  protected WriteMutatedVersionsInput(BuilderImpl builder) {
    this.items = builder.items();
    this.Identifier = builder.Identifier();
    this.Original = builder.Original();
    this.Terminal = builder.Terminal();
    this.CompleteMutation = builder.CompleteMutation();
  }

  /**
   * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  public List<EncryptedHierarchicalKey> items() {
    return this.items;
  }

  /**
   * @return The Identifier of the Branch Key.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return A commitment of the Original Mutable Properities of the Branch Key.
   */
  public ByteBuffer Original() {
    return this.Original;
  }

  /**
   * @return A commitment of the Terminal Mutable Properities of the Branch Key.
   */
  public ByteBuffer Terminal() {
    return this.Terminal;
  }

  /**
   * @return If set to True, the Mutation Lock will be deleted. Effectively defaults to false
   */
  public Boolean CompleteMutation() {
    return this.CompleteMutation;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param items List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    Builder items(List<EncryptedHierarchicalKey> items);

    /**
     * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    List<EncryptedHierarchicalKey> items();

    /**
     * @param Identifier The Identifier of the Branch Key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Identifier of the Branch Key.
     */
    String Identifier();

    /**
     * @param Original A commitment of the Original Mutable Properities of the Branch Key.
     */
    Builder Original(ByteBuffer Original);

    /**
     * @return A commitment of the Original Mutable Properities of the Branch Key.
     */
    ByteBuffer Original();

    /**
     * @param Terminal A commitment of the Terminal Mutable Properities of the Branch Key.
     */
    Builder Terminal(ByteBuffer Terminal);

    /**
     * @return A commitment of the Terminal Mutable Properities of the Branch Key.
     */
    ByteBuffer Terminal();

    /**
     * @param CompleteMutation If set to True, the Mutation Lock will be deleted. Effectively defaults to false
     */
    Builder CompleteMutation(Boolean CompleteMutation);

    /**
     * @return If set to True, the Mutation Lock will be deleted. Effectively defaults to false
     */
    Boolean CompleteMutation();

    WriteMutatedVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected List<EncryptedHierarchicalKey> items;

    protected String Identifier;

    protected ByteBuffer Original;

    protected ByteBuffer Terminal;

    protected Boolean CompleteMutation;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteMutatedVersionsInput model) {
      this.items = model.items();
      this.Identifier = model.Identifier();
      this.Original = model.Original();
      this.Terminal = model.Terminal();
      this.CompleteMutation = model.CompleteMutation();
    }

    public Builder items(List<EncryptedHierarchicalKey> items) {
      this.items = items;
      return this;
    }

    public List<EncryptedHierarchicalKey> items() {
      return this.items;
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

    public Builder CompleteMutation(Boolean CompleteMutation) {
      this.CompleteMutation = CompleteMutation;
      return this;
    }

    public Boolean CompleteMutation() {
      return this.CompleteMutation;
    }

    public WriteMutatedVersionsInput build() {
      if (Objects.isNull(this.items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `items`"
        );
      }
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
      if (Objects.isNull(this.CompleteMutation())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CompleteMutation`"
        );
      }
      return new WriteMutatedVersionsInput(this);
    }
  }
}
