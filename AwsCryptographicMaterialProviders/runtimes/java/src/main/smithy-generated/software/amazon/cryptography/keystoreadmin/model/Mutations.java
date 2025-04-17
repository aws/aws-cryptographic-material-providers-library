// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

/**
 * Define the Mutation in terms of the terminal, or end state,
 * value for a particular Branch Key property.
 * The original value will be REPLACED with this value.
 * As of v<HV-2>, a Mutation can either:
 * - replace the KmsArn protecting the Branch Key
 * - replace the encryption context
 * - change the 'hierarchy-version'
 * - any combination of the above
 */
public class Mutations {

  /**
   * Optional. If not set, there will be no change to the KMS ARN.
   *   If set, ReEncrypt all Items of the Branch Key
   *   to be authorized by this
   *   AWS Key Management Service Key.
   *   A Multi-Region or Single Region AWS KMS Key are permitted,
   *   but not aliases!
   */
  private final String TerminalKmsArn;

  /**
   * Optional. If not set, there will be no change to the Encryption Context.
   *   ReEncrypt all Items of the Branch Key
   *   to be authorized with this encryption context.
   *   An empty Encryption Context is not allowed.
   */
  private final Map<String, String> TerminalEncryptionContext;

  /**
   * Optional. If set, changes the hierarchy-version of the Branch Key.
   *   At this time, only '2' is allowed; there is no operation that faciliates HV-2 -> HV-1.
   */
  private final HierarchyVersion TerminalHierarchyVersion;

  protected Mutations(BuilderImpl builder) {
    this.TerminalKmsArn = builder.TerminalKmsArn();
    this.TerminalEncryptionContext = builder.TerminalEncryptionContext();
    this.TerminalHierarchyVersion = builder.TerminalHierarchyVersion();
  }

  /**
   * @return Optional. If not set, there will be no change to the KMS ARN.
   *   If set, ReEncrypt all Items of the Branch Key
   *   to be authorized by this
   *   AWS Key Management Service Key.
   *   A Multi-Region or Single Region AWS KMS Key are permitted,
   *   but not aliases!
   */
  public String TerminalKmsArn() {
    return this.TerminalKmsArn;
  }

  /**
   * @return Optional. If not set, there will be no change to the Encryption Context.
   *   ReEncrypt all Items of the Branch Key
   *   to be authorized with this encryption context.
   *   An empty Encryption Context is not allowed.
   */
  public Map<String, String> TerminalEncryptionContext() {
    return this.TerminalEncryptionContext;
  }

  /**
   * @return Optional. If set, changes the hierarchy-version of the Branch Key.
   *   At this time, only '2' is allowed; there is no operation that faciliates HV-2 -> HV-1.
   */
  public HierarchyVersion TerminalHierarchyVersion() {
    return this.TerminalHierarchyVersion;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param TerminalKmsArn Optional. If not set, there will be no change to the KMS ARN.
     *   If set, ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    Builder TerminalKmsArn(String TerminalKmsArn);

    /**
     * @return Optional. If not set, there will be no change to the KMS ARN.
     *   If set, ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    String TerminalKmsArn();

    /**
     * @param TerminalEncryptionContext Optional. If not set, there will be no change to the Encryption Context.
     *   ReEncrypt all Items of the Branch Key
     *   to be authorized with this encryption context.
     *   An empty Encryption Context is not allowed.
     */
    Builder TerminalEncryptionContext(
      Map<String, String> TerminalEncryptionContext
    );

    /**
     * @return Optional. If not set, there will be no change to the Encryption Context.
     *   ReEncrypt all Items of the Branch Key
     *   to be authorized with this encryption context.
     *   An empty Encryption Context is not allowed.
     */
    Map<String, String> TerminalEncryptionContext();

    /**
     * @param TerminalHierarchyVersion Optional. If set, changes the hierarchy-version of the Branch Key.
     *   At this time, only '2' is allowed; there is no operation that faciliates HV-2 -> HV-1.
     */
    Builder TerminalHierarchyVersion(HierarchyVersion TerminalHierarchyVersion);

    /**
     * @return Optional. If set, changes the hierarchy-version of the Branch Key.
     *   At this time, only '2' is allowed; there is no operation that faciliates HV-2 -> HV-1.
     */
    HierarchyVersion TerminalHierarchyVersion();

    Mutations build();
  }

  static class BuilderImpl implements Builder {

    protected String TerminalKmsArn;

    protected Map<String, String> TerminalEncryptionContext;

    protected HierarchyVersion TerminalHierarchyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(Mutations model) {
      this.TerminalKmsArn = model.TerminalKmsArn();
      this.TerminalEncryptionContext = model.TerminalEncryptionContext();
      this.TerminalHierarchyVersion = model.TerminalHierarchyVersion();
    }

    public Builder TerminalKmsArn(String TerminalKmsArn) {
      this.TerminalKmsArn = TerminalKmsArn;
      return this;
    }

    public String TerminalKmsArn() {
      return this.TerminalKmsArn;
    }

    public Builder TerminalEncryptionContext(
      Map<String, String> TerminalEncryptionContext
    ) {
      this.TerminalEncryptionContext = TerminalEncryptionContext;
      return this;
    }

    public Map<String, String> TerminalEncryptionContext() {
      return this.TerminalEncryptionContext;
    }

    public Builder TerminalHierarchyVersion(
      HierarchyVersion TerminalHierarchyVersion
    ) {
      this.TerminalHierarchyVersion = TerminalHierarchyVersion;
      return this;
    }

    public HierarchyVersion TerminalHierarchyVersion() {
      return this.TerminalHierarchyVersion;
    }

    public Mutations build() {
      return new Mutations(this);
    }
  }
}
