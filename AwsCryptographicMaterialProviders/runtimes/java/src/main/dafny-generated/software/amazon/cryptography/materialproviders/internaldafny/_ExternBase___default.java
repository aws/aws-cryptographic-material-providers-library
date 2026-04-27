// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig DefaultMaterialProvidersConfig() {
    return software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig.create();
  }
  public static Wrappers_Compile.Result<MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig config)
  {
    Wrappers_Compile.Result<MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeCrypto;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _0_maybeCrypto = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _1_valueOrError0 = (_0_maybeCrypto).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialProvidersClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(MaterialProvidersClient.class)));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient _3_cryptoPrimitivesX;
    _3_cryptoPrimitivesX = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _4_cryptoPrimitives;
    _4_cryptoPrimitives = ((software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient)(java.lang.Object)(_3_cryptoPrimitivesX));
    MaterialProvidersClient _5_client;
    MaterialProvidersClient _nw0 = new MaterialProvidersClient();
    _nw0.__ctor(AwsCryptographyMaterialProvidersOperations_Compile.Config.create(_4_cryptoPrimitives));
    _5_client = _nw0;
    res = Wrappers_Compile.Result.<MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _5_client);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.materialproviders.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "MaterialProviders._default";
  }
}
