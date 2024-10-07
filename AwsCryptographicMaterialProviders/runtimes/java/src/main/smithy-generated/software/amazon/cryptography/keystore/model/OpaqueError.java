// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class OpaqueError extends RuntimeException {

  /**
   * The unexpected object encountered. It MIGHT BE an Exception, but that is not guaranteed.
   */
  private final Object obj;

  /**
   * A best effort text representation of obj.
   */
  private final String alt_text;

  protected OpaqueError(BuilderImpl builder) {
    super(messageFromBuilder(builder), builder.cause());
    this.alt_text = builder.alt_text();
    this.obj = builder.obj();
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

  /**
   * @return The unexpected object encountered. It MIGHT BE an Exception, but that is not guaranteed.
   */
  public Object obj() {
    return this.obj;
  }

  /**
   * @return A best effort text representation of obj.
   */
  public String alt_text() {
    return this.alt_text;
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

    /**
     * @param obj The unexpected object encountered. It MIGHT BE an Exception, but that is not guaranteed.
     */
    Builder obj(Object obj);

    /**
     * @return The unexpected object encountered. It MIGHT BE an Exception, but that is not guaranteed.
     */
    Object obj();

    /**
     * @param alt_text A best effort text representation of obj.
     */
    Builder alt_text(String alt_text);

    /**
     * @return A best effort text representation of obj.
     */
    String alt_text();

    OpaqueError build();
  }

  static class BuilderImpl implements Builder {

    protected String message;

    protected Throwable cause;

    protected Object obj;

    protected String alt_text;

    protected BuilderImpl() {}

    protected BuilderImpl(OpaqueError model) {
      this.cause = model.getCause();
      this.message = model.getMessage();
      this.obj = model.obj();
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

    public Builder obj(Object obj) {
      this.obj = obj;
      return this;
    }

    public Object obj() {
      return this.obj;
    }

    public Builder alt_text(String alt_text) {
      this.alt_text = alt_text;
      return this;
    }

    public String alt_text() {
      return this.alt_text;
    }

    public OpaqueError build() {
      if (
        this.obj != null && this.cause == null && this.obj instanceof Throwable
      ) {
        this.cause = (Throwable) this.obj;
      } else if (this.obj == null && this.cause != null) {
        this.obj = this.cause;
      }
      return new OpaqueError(this);
    }
  }
}
