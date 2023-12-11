package software.amazon.cryptography.materialproviders.internaldafny.wrapped;

import Wrappers_Compile.Result;
import java.util.logging.Logger;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.ToNative;
import software.amazon.cryptography.materialproviders.internaldafny.types.Error;
import software.amazon.cryptography.materialproviders.internaldafny.types.Error;
import software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient;
import software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient;
import software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.wrapped.TestMaterialProviders;
import software.amazon.cryptography.primitives.model.GetHKDFProviderInput;
import software.amazon.cryptography.primitives.model.HKDFProvider;

public class __default extends _ExternBase___default {

  private static final Logger LOGGER = Logger.getLogger(
    __default.class.getName()
  );

  static {
    try {
      com.amazon.corretto.crypto.provider.AmazonCorrettoCryptoProvider.install();
    } catch (java.lang.NoClassDefFoundError ignore) {}
    software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig wrappedConfig =
      ToNative.MaterialProvidersConfig(MaterialProvidersConfig.Default());
    software.amazon.cryptography.materialproviders.MaterialProviders impl =
      MaterialProviders
        .builder()
        .MaterialProvidersConfig(wrappedConfig)
        .build();
    HKDFProvider hkdfProvider = impl
      .GetHKDFProvider(GetHKDFProviderInput.builder().build())
      .provider();
    LOGGER.warning(String.format("HKDF Provider is %s", hkdfProvider));
  }

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
    HKDFProvider hkdfProvider = impl
      .GetHKDFProvider(GetHKDFProviderInput.builder().build())
      .provider();
    TestMaterialProviders wrappedClient = TestMaterialProviders
      .builder()
      .impl(impl)
      .build();
    return Result.create_Success(wrappedClient);
  }
}
