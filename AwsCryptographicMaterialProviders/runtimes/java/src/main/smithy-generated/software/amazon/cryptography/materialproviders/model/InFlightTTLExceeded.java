// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Thrown if a request is waiting for longer than `inflightTTL`.
 * The Storm Tracking Cache protects against unbounded parallelism.
 * The Storm Tracking Cache will only work `fanOut` number of concurrent requests.
 * As requests are completed,
 * queued requests are worked.
 * If a request is not worked in less than `inflightTTL`,
 * this exception is thrown.
 *
 * Note that this exception does NOT imply that the material requested
 * is invalid or unreachable;
 * it only implies that the cache had more requests to handle than it could
 * with the given `fanOut` and `inflightTTL` constraints.
 */
public class InFlightTTLExceeded extends RuntimeException {

  protected InFlightTTLExceeded(BuilderImpl builder) {
    super(messageFromBuilder(builder), builder.cause());
  }

  private static String messageFromBuilder(Builder builder) {
    if (builder.message() != null) {
      return builder.message();
    }
    if (builder.cause() != null) {
      return builder.cause().getMessage();
    }
    return null;
  }

  /**
   * See {@link Throwable#getMessage()}.
   */
  public String message() {
    return this.getMessage();
  }

  /**
   * See {@link Throwable#getCause()}.
   */
  public Throwable cause() {
    return this.getCause();
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param message The detailed message. The detail message is saved for later retrieval by the {@link #getMessage()} method.
     */
    Builder message(String message);

    /**
     * @return The detailed message. The detail message is saved for later retrieval by the {@link #getMessage()} method.
     */
    String message();

    /**
     * @param cause The cause (which is saved for later retrieval by the {@link #getCause()} method). (A {@code null} value is permitted, and indicates that the cause is nonexistent or unknown.)
     */
    Builder cause(Throwable cause);

    /**
     * @return The cause (which is saved for later retrieval by the {@link #getCause()} method). (A {@code null} value is permitted, and indicates that the cause is nonexistent or unknown.)
     */
    Throwable cause();

    InFlightTTLExceeded build();
  }

  static class BuilderImpl implements Builder {

    protected String message;

    protected Throwable cause;

    protected BuilderImpl() {}

    protected BuilderImpl(InFlightTTLExceeded model) {
      this.message = model.message();
      this.cause = model.cause();
    }

    public Builder message(String message) {
      this.message = message;
      return this;
    }

    public String message() {
      return this.message;
    }

    public Builder cause(Throwable cause) {
      this.cause = cause;
      return this;
    }

    public Throwable cause() {
      return this.cause;
    }

    public InFlightTTLExceeded build() {
      if (Objects.isNull(this.message())) {
        throw new IllegalArgumentException(
          "Missing value for required field `message`"
        );
      }
      return new InFlightTTLExceeded(this);
    }
  }
}
