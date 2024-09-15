// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

/**
 * Information for a symmetric beacon key. At this time there is no additional information.
 */
public class ActiveHierarchicalSymmetricBeacon {

  protected ActiveHierarchicalSymmetricBeacon(BuilderImpl builder) {}

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    ActiveHierarchicalSymmetricBeacon build();
  }

  static class BuilderImpl implements Builder {

    protected BuilderImpl() {}

    protected BuilderImpl(ActiveHierarchicalSymmetricBeacon model) {}

    public ActiveHierarchicalSymmetricBeacon build() {
      return new ActiveHierarchicalSymmetricBeacon(this);
    }
  }
}
