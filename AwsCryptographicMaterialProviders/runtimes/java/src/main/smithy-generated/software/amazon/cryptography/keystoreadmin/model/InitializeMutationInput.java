// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class InitializeMutationInput {

  /**
   * The identifier for the Branch Key to be mutated.
   */
  private final String Identifier;

  /**
   * Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  private final Mutations Mutations;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   *   However, if the Branch Key's 'hierarchy-version' is HV-2,
   *   or the Branch Key is being mutated to HV-2,
   *   the Strategy MUST be AwsKmsDecryptEncrypt or AwsKmsSimple.
   */
  private final KeyManagementStrategy Strategy;

  /**
   * Key Store Admin protects any non-cryptographic
   * items stored with this Key.
   * Using 'KMS Symmetric Encryption' is a best practice,
   * as it prevents actors with only write access to the Key Store's storage
   * from tampering with Mutations.
   * For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.
   */
  private final SystemKey SystemKey;

  /**
   * Optional. Defaults to False, which Versions (or Rotates) the Branch Key,
   *   creating a new Version that has only ever been in the terminal state.
   *   Setting this value to True disables the rotation.
   *   This is a Security vs Performance trade off.
   *   Mutating a Branch Key can change the security domain of the Branch Key.
   *   Some application's Threat Models benefit from ensuring a new Version
   *   is created whenever a Mutation occurs,
   *   allowing the application to track under which security domain data
   *   was protected.
   *   However, not all Threat Models call for this.
   *   Particularly if Mutations are triggered in response to external actors,
   *   creating a new Version for every Mutation request can needlessly grow
   *   the item count of a Branch Key.
   */
  private final Boolean DoNotVersion;

  protected InitializeMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Mutations = builder.Mutations();
    this.Strategy = builder.Strategy();
    this.SystemKey = builder.SystemKey();
    this.DoNotVersion = builder.DoNotVersion();
  }

  /**
   * @return The identifier for the Branch Key to be mutated.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return Describes the Mutation that will be applied to all Items of the Branch Key.
   */
  public Mutations Mutations() {
    return this.Mutations;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   *   However, if the Branch Key's 'hierarchy-version' is HV-2,
   *   or the Branch Key is being mutated to HV-2,
   *   the Strategy MUST be AwsKmsDecryptEncrypt or AwsKmsSimple.
   */
  public KeyManagementStrategy Strategy() {
    return this.Strategy;
  }

  /**
   * @return Key Store Admin protects any non-cryptographic
   * items stored with this Key.
   * Using 'KMS Symmetric Encryption' is a best practice,
   * as it prevents actors with only write access to the Key Store's storage
   * from tampering with Mutations.
   * For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.
   */
  public SystemKey SystemKey() {
    return this.SystemKey;
  }

  /**
   * @return Optional. Defaults to False, which Versions (or Rotates) the Branch Key,
   *   creating a new Version that has only ever been in the terminal state.
   *   Setting this value to True disables the rotation.
   *   This is a Security vs Performance trade off.
   *   Mutating a Branch Key can change the security domain of the Branch Key.
   *   Some application's Threat Models benefit from ensuring a new Version
   *   is created whenever a Mutation occurs,
   *   allowing the application to track under which security domain data
   *   was protected.
   *   However, not all Threat Models call for this.
   *   Particularly if Mutations are triggered in response to external actors,
   *   creating a new Version for every Mutation request can needlessly grow
   *   the item count of a Branch Key.
   */
  public Boolean DoNotVersion() {
    return this.DoNotVersion;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key to be mutated.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to be mutated.
     */
    String Identifier();

    /**
     * @param Mutations Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Builder Mutations(Mutations Mutations);

    /**
     * @return Describes the Mutation that will be applied to all Items of the Branch Key.
     */
    Mutations Mutations();

    /**
     * @param Strategy Optional. Defaults to reEncrypt with a default KMS Client.
     *   However, if the Branch Key's 'hierarchy-version' is HV-2,
     *   or the Branch Key is being mutated to HV-2,
     *   the Strategy MUST be AwsKmsDecryptEncrypt or AwsKmsSimple.
     */
    Builder Strategy(KeyManagementStrategy Strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     *   However, if the Branch Key's 'hierarchy-version' is HV-2,
     *   or the Branch Key is being mutated to HV-2,
     *   the Strategy MUST be AwsKmsDecryptEncrypt or AwsKmsSimple.
     */
    KeyManagementStrategy Strategy();

    /**
     * @param SystemKey Key Store Admin protects any non-cryptographic
     * items stored with this Key.
     * Using 'KMS Symmetric Encryption' is a best practice,
     * as it prevents actors with only write access to the Key Store's storage
     * from tampering with Mutations.
     * For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.
     */
    Builder SystemKey(SystemKey SystemKey);

    /**
     * @return Key Store Admin protects any non-cryptographic
     * items stored with this Key.
     * Using 'KMS Symmetric Encryption' is a best practice,
     * as it prevents actors with only write access to the Key Store's storage
     * from tampering with Mutations.
     * For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.
     */
    SystemKey SystemKey();

    /**
     * @param DoNotVersion Optional. Defaults to False, which Versions (or Rotates) the Branch Key,
     *   creating a new Version that has only ever been in the terminal state.
     *   Setting this value to True disables the rotation.
     *   This is a Security vs Performance trade off.
     *   Mutating a Branch Key can change the security domain of the Branch Key.
     *   Some application's Threat Models benefit from ensuring a new Version
     *   is created whenever a Mutation occurs,
     *   allowing the application to track under which security domain data
     *   was protected.
     *   However, not all Threat Models call for this.
     *   Particularly if Mutations are triggered in response to external actors,
     *   creating a new Version for every Mutation request can needlessly grow
     *   the item count of a Branch Key.
     */
    Builder DoNotVersion(Boolean DoNotVersion);

    /**
     * @return Optional. Defaults to False, which Versions (or Rotates) the Branch Key,
     *   creating a new Version that has only ever been in the terminal state.
     *   Setting this value to True disables the rotation.
     *   This is a Security vs Performance trade off.
     *   Mutating a Branch Key can change the security domain of the Branch Key.
     *   Some application's Threat Models benefit from ensuring a new Version
     *   is created whenever a Mutation occurs,
     *   allowing the application to track under which security domain data
     *   was protected.
     *   However, not all Threat Models call for this.
     *   Particularly if Mutations are triggered in response to external actors,
     *   creating a new Version for every Mutation request can needlessly grow
     *   the item count of a Branch Key.
     */
    Boolean DoNotVersion();

    InitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected Mutations Mutations;

    protected KeyManagementStrategy Strategy;

    protected SystemKey SystemKey;

    protected Boolean DoNotVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationInput model) {
      this.Identifier = model.Identifier();
      this.Mutations = model.Mutations();
      this.Strategy = model.Strategy();
      this.SystemKey = model.SystemKey();
      this.DoNotVersion = model.DoNotVersion();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Mutations(Mutations Mutations) {
      this.Mutations = Mutations;
      return this;
    }

    public Mutations Mutations() {
      return this.Mutations;
    }

    public Builder Strategy(KeyManagementStrategy Strategy) {
      this.Strategy = Strategy;
      return this;
    }

    public KeyManagementStrategy Strategy() {
      return this.Strategy;
    }

    public Builder SystemKey(SystemKey SystemKey) {
      this.SystemKey = SystemKey;
      return this;
    }

    public SystemKey SystemKey() {
      return this.SystemKey;
    }

    public Builder DoNotVersion(Boolean DoNotVersion) {
      this.DoNotVersion = DoNotVersion;
      return this;
    }

    public Boolean DoNotVersion() {
      return this.DoNotVersion;
    }

    public InitializeMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Mutations())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Mutations`"
        );
      }
      if (Objects.isNull(this.SystemKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `SystemKey`"
        );
      }
      return new InitializeMutationInput(this);
    }
  }
}
