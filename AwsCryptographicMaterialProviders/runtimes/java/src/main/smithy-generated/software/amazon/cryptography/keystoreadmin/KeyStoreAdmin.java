// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.util.Objects;
import software.amazon.cryptography.keystoreadmin.internaldafny.KeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.internaldafny.__default;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.Error;
import software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;

public class KeyStoreAdmin {

  private final IKeyStoreAdminClient _impl;

  protected KeyStoreAdmin(BuilderImpl builder) {
    KeyStoreAdminConfig input = builder.KeyStoreAdminConfig();
    software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig dafnyValue =
      ToDafny.KeyStoreAdminConfig(input);
    Result<KeyStoreAdminClient, Error> result = __default.KeyStoreAdmin(
      dafnyValue
    );
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    this._impl = result.dtor_value();
  }

  KeyStoreAdmin(IKeyStoreAdminClient impl) {
    this._impl = impl;
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  /**
   * Create a new Branch Key in the Key Store. Additionally create a Beacon Key that is tied to this Branch Key.
   * @return Outputs for Branch Key creation.
   */
  public CreateKeyOutput CreateKey(CreateKeyInput input) {
    software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput dafnyValue =
      ToDafny.CreateKeyInput(input);
    Result<
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput,
      Error
    > result = this._impl.CreateKey(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.CreateKeyOutput(result.dtor_value());
  }

  protected IKeyStoreAdminClient impl() {
    return this._impl;
  }

  public interface Builder {
    Builder KeyStoreAdminConfig(KeyStoreAdminConfig KeyStoreAdminConfig);

    KeyStoreAdminConfig KeyStoreAdminConfig();

    KeyStoreAdmin build();
  }

  static class BuilderImpl implements Builder {

    protected KeyStoreAdminConfig KeyStoreAdminConfig;

    protected BuilderImpl() {}

    public Builder KeyStoreAdminConfig(
      KeyStoreAdminConfig KeyStoreAdminConfig
    ) {
      this.KeyStoreAdminConfig = KeyStoreAdminConfig;
      return this;
    }

    public KeyStoreAdminConfig KeyStoreAdminConfig() {
      return this.KeyStoreAdminConfig;
    }

    public KeyStoreAdmin build() {
      if (Objects.isNull(this.KeyStoreAdminConfig())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KeyStoreAdminConfig`"
        );
      }
      return new KeyStoreAdmin(this);
    }
  }
}
