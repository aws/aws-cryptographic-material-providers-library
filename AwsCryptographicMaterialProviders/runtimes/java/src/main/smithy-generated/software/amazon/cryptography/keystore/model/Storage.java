// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.IKeyStorageInterface;
import software.amazon.cryptography.keystore.KeyStorageInterface;

public class Storage {

  /**
   * The DynamoDB configuration that backs this Key Store.
   */
  private final DynamoDBTable ddb;

  /**
   * The custom storage configuration that backs this Key Store.
   */
  private final IKeyStorageInterface custom;

  protected Storage(BuilderImpl builder) {
    this.ddb = builder.ddb();
    this.custom = builder.custom();
  }

  /**
   * @return The DynamoDB configuration that backs this Key Store.
   */
  public DynamoDBTable ddb() {
    return this.ddb;
  }

  /**
   * @return The custom storage configuration that backs this Key Store.
   */
  public IKeyStorageInterface custom() {
    return this.custom;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ddb The DynamoDB configuration that backs this Key Store.
     */
    Builder ddb(DynamoDBTable ddb);

    /**
     * @return The DynamoDB configuration that backs this Key Store.
     */
    DynamoDBTable ddb();

    /**
     * @param custom The custom storage configuration that backs this Key Store.
     */
    Builder custom(IKeyStorageInterface custom);

    /**
     * @return The custom storage configuration that backs this Key Store.
     */
    IKeyStorageInterface custom();

    Storage build();
  }

  static class BuilderImpl implements Builder {

    protected DynamoDBTable ddb;

    protected IKeyStorageInterface custom;

    protected BuilderImpl() {}

    protected BuilderImpl(Storage model) {
      this.ddb = model.ddb();
      this.custom = model.custom();
    }

    public Builder ddb(DynamoDBTable ddb) {
      this.ddb = ddb;
      return this;
    }

    public DynamoDBTable ddb() {
      return this.ddb;
    }

    public Builder custom(IKeyStorageInterface custom) {
      this.custom = KeyStorageInterface.wrap(custom);
      return this;
    }

    public IKeyStorageInterface custom() {
      return this.custom;
    }

    public Storage build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`Storage` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new Storage(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.ddb, this.custom };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
