// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.materialproviders.internaldafny.wrapped;

import Wrappers_Compile.Result;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.ToNative;
import software.amazon.cryptography.materialproviders.internaldafny.types.Error;
import software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient;
import software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.wrapped.TestMaterialProviders;

public class __default extends _ExternBase___default {

  public static Result<
    IAwsCryptographicMaterialProvidersClient,
    Error
  > WrappedMaterialProviders(MaterialProvidersConfig config) {
    software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig wrappedConfig =
      ToNative.MaterialProvidersConfig(config);
    software.amazon.cryptography.materialproviders.MaterialProviders impl =
      MaterialProviders
        .builder()
        .MaterialProvidersConfig(wrappedConfig)
        .build();
    TestMaterialProviders wrappedClient = TestMaterialProviders
      .builder()
      .impl(impl)
      .build();
    return software.amazon.cryptography.materialproviders.internaldafny._ExternBase___default.CreateSuccessOfClient(
      wrappedClient
    );
  }
}
