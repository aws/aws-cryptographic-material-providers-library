// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Inputs for getting a Beacon Key
 */
public class GetEncryptedBeaconKeyInput {

  /**
   * The identifier of the Branch Key the Beacon Key is associated with.
   */
  private final String Identifier;

  protected GetEncryptedBeaconKeyInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The identifier of the Branch Key the Beacon Key is associated with.
   */
  public String Identifier() {
    return this.Identifier;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier of the Branch Key the Beacon Key is associated with.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier of the Branch Key the Beacon Key is associated with.
     */
    String Identifier();

    GetEncryptedBeaconKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedBeaconKeyInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetEncryptedBeaconKeyInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetEncryptedBeaconKeyInput(this);
    }
  }
}
