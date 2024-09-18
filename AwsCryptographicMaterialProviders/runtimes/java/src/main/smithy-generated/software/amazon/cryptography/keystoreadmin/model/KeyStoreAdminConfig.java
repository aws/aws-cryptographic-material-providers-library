// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.Storage;

public class KeyStoreAdminConfig {

  /**
   * The logical name for this Key Store,
   *   which is cryptographically bound to the keys it holds.
   *   This appears in the Encryption Context of KMS requests as `tablename`.
   *
   *   There SHOULD be a one to one mapping between the Storage's physical name,
   *   i.e: DynamoDB Table Names,
   *   and the Logical KeyStore Name.
   *   This value can be set to the DynamoDB table name itself
   *   (Storage's physical name),
   *   but does not need to.
   *
   *   Controlling this value independently enables restoring from DDB table backups
   *   even when the table name after restoration is not exactly the same.
   */
  private final String logicalKeyStoreName;

  /**
   * The storage configuration for this Key Store.
   */
  private final Storage storage;

  protected KeyStoreAdminConfig(BuilderImpl builder) {
    this.logicalKeyStoreName = builder.logicalKeyStoreName();
    this.storage = builder.storage();
  }

  /**
   * @return The logical name for this Key Store,
   *   which is cryptographically bound to the keys it holds.
   *   This appears in the Encryption Context of KMS requests as `tablename`.
   *
   *   There SHOULD be a one to one mapping between the Storage's physical name,
   *   i.e: DynamoDB Table Names,
   *   and the Logical KeyStore Name.
   *   This value can be set to the DynamoDB table name itself
   *   (Storage's physical name),
   *   but does not need to.
   *
   *   Controlling this value independently enables restoring from DDB table backups
   *   even when the table name after restoration is not exactly the same.
   */
  public String logicalKeyStoreName() {
    return this.logicalKeyStoreName;
  }

  /**
   * @return The storage configuration for this Key Store.
   */
  public Storage storage() {
    return this.storage;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param logicalKeyStoreName The logical name for this Key Store,
     *   which is cryptographically bound to the keys it holds.
     *   This appears in the Encryption Context of KMS requests as `tablename`.
     *
     *   There SHOULD be a one to one mapping between the Storage's physical name,
     *   i.e: DynamoDB Table Names,
     *   and the Logical KeyStore Name.
     *   This value can be set to the DynamoDB table name itself
     *   (Storage's physical name),
     *   but does not need to.
     *
     *   Controlling this value independently enables restoring from DDB table backups
     *   even when the table name after restoration is not exactly the same.
     */
    Builder logicalKeyStoreName(String logicalKeyStoreName);

    /**
     * @return The logical name for this Key Store,
     *   which is cryptographically bound to the keys it holds.
     *   This appears in the Encryption Context of KMS requests as `tablename`.
     *
     *   There SHOULD be a one to one mapping between the Storage's physical name,
     *   i.e: DynamoDB Table Names,
     *   and the Logical KeyStore Name.
     *   This value can be set to the DynamoDB table name itself
     *   (Storage's physical name),
     *   but does not need to.
     *
     *   Controlling this value independently enables restoring from DDB table backups
     *   even when the table name after restoration is not exactly the same.
     */
    String logicalKeyStoreName();

    /**
     * @param storage The storage configuration for this Key Store.
     */
    Builder storage(Storage storage);

    /**
     * @return The storage configuration for this Key Store.
     */
    Storage storage();

    KeyStoreAdminConfig build();
  }

  static class BuilderImpl implements Builder {

    protected String logicalKeyStoreName;

    protected Storage storage;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyStoreAdminConfig model) {
      this.logicalKeyStoreName = model.logicalKeyStoreName();
      this.storage = model.storage();
    }

    public Builder logicalKeyStoreName(String logicalKeyStoreName) {
      this.logicalKeyStoreName = logicalKeyStoreName;
      return this;
    }

    public String logicalKeyStoreName() {
      return this.logicalKeyStoreName;
    }

    public Builder storage(Storage storage) {
      this.storage = storage;
      return this;
    }

    public Storage storage() {
      return this.storage;
    }

    public KeyStoreAdminConfig build() {
      if (Objects.isNull(this.logicalKeyStoreName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `logicalKeyStoreName`"
        );
      }
      if (Objects.isNull(this.storage())) {
        throw new IllegalArgumentException(
          "Missing value for required field `storage`"
        );
      }
      return new KeyStoreAdminConfig(this);
    }
  }
}
