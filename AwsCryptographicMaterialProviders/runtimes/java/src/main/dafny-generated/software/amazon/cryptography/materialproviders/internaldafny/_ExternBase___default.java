// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;
import EcdhEdkWrapping_Compile.*;
import RawECDHKeyring_Compile.*;
import AwsKmsEcdhKeyring_Compile.*;
import RawAESKeyring_Compile.*;
import RawRSAKeyring_Compile.*;
import CMM_Compile.*;
import Defaults_Compile.*;
import Commitment_Compile.*;
import DefaultCMM_Compile.*;
import DefaultClientSupplier_Compile.*;
import Utils_Compile.*;
import RequiredEncryptionContextCMM_Compile.*;
import AwsCryptographyMaterialProvidersOperations_Compile.*;

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
