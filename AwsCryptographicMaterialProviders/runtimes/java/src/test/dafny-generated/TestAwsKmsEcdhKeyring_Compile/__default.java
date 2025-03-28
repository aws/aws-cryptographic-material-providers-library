// Class __default
// Dafny class __default compiled into Java
package TestAwsKmsEcdhKeyring_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;
import TestUtils_Compile.*;
import TestIntermediateKeyWrapping_Compile.*;
import TestErrorMessages_Compile.*;
import TestDefaultClientProvider_Compile.*;
import TestRawECDHKeyring_Compile.*;
import TestRawAESKeyring_Compile.*;
import TestMultiKeyring_Compile.*;
import TestRawRSAKeying_Compile.*;
import TestAwsKmsRsaKeyring_Compile.*;
import TestAwsKmsHierarchicalKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials GetTestMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId suiteId)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials out = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(44,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out1;
    _out1 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _2_encryptionContext = _out1;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _3_suite;
    _3_suite = AlgorithmSuites_Compile.__default.GetSuite(suiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _4_valueOrError1 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(suiteId, _2_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_4_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(49,33): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _5_encryptionMaterialsIn;
    _5_encryptionMaterialsIn = (_4_valueOrError1).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    out = _5_encryptionMaterialsIn;
    return out;
  }
  public static void TestKmsEcdhConfigurationFailure()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(63,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(65,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput.create(TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__R())), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _4_valueOrError2 = _out2;
    if (!(!((_4_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(67,48): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _5_kmsEcdhKeyringDiscoveryConfiguration;
    _5_kmsEcdhKeyringDiscoveryConfiguration = (_4_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _6_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out3;
    _out3 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _6_encryptionContext = _out3;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _7_algorithmSuiteId;
    _7_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _8_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_7_algorithmSuiteId, _6_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_8_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(83,33): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _9_encryptionMaterialsIn;
    _9_encryptionMaterialsIn = (_8_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_encryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_5_kmsEcdhKeyringDiscoveryConfiguration).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_9_encryptionMaterialsIn));
    _10_encryptionMaterialsOut = _out4;
    if (!((_10_encryptionMaterialsOut).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(97,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_10_encryptionMaterialsOut).dtor_error()).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(98,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    dafny.DafnySequence<? extends Character> _11_expectedErrorMessage;
    _11_expectedErrorMessage = ErrorMessages_Compile.__default.KMS__ECDH__DISCOVERY__ENCRYPT__ERROR();
    if (!((((_10_encryptionMaterialsOut).dtor_error()).dtor_message()).equals(_11_expectedErrorMessage))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(101,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(105,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(107,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _4_senderArns;
    _4_senderArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_recipientArns;
    _5_recipientArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__R());
    dafny.DafnySequence<? extends software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> _6_curveSpecs;
    _6_curveSpecs = dafny.DafnySequence.<software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> of(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_4_senderArns).length());
    for (java.math.BigInteger _7_i = java.math.BigInteger.ZERO; _7_i.compareTo(_hi0) < 0; _7_i = _7_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_publicKeyResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
      _out2 = (_3_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
      _8_publicKeyResponse = _out2;
      if (!((_8_publicKeyResponse).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(121,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_8_publicKeyResponse).dtor_value();
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _9___v0 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _10_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _11___v1 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _12___v2 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _13___v3 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _14___v4 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _15___v5 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _16___v6 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
      if (!((_10_PublicKey).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(123,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      System.out.print((dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\nTest with sender: "), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_4_senderArns).select(dafny.Helpers.toInt((_7_i)))))), dafny.DafnySequence.asString(" and recipient: ")), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i)))))), dafny.DafnySequence.asString("\n"))).verbatimString());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_4_senderArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_10_PublicKey).dtor_value())), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((_6_curveSpecs).select(dafny.Helpers.toInt((_7_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _17_valueOrError2 = _out3;
      if (!(!((_17_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(126,28): " + java.lang.String.valueOf(_17_valueOrError2));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _18_kmsEcdhKeyring;
      _18_kmsEcdhKeyring = (_17_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _19_encryptionContext;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
      _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
      _19_encryptionContext = _out4;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _20_algorithmSuiteId;
      _20_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _21_suite;
      _21_suite = AlgorithmSuites_Compile.__default.GetSuite(_20_algorithmSuiteId);
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _22_valueOrError3 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_20_algorithmSuiteId, _19_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
      if (!(!((_22_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(144,35): " + java.lang.String.valueOf(_22_valueOrError3));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _23_encryptionMaterialsIn;
      _23_encryptionMaterialsIn = (_22_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
      _out5 = (_18_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
      _24_valueOrError4 = _out5;
      if (!(!((_24_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(154,36): " + java.lang.String.valueOf(_24_valueOrError4));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _25_encryptionMaterialsOut;
      _25_encryptionMaterialsOut = (_24_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _26_valueOrError5 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_25_encryptionMaterialsOut).dtor_materials());
      if (!(!((_26_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(158,15): " + java.lang.String.valueOf(_26_valueOrError5));
      }
      dafny.Tuple0 _27___v7;
      _27___v7 = (_26_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_25_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(160,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _28_edk;
      _28_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_25_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _29_valueOrError6 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_20_algorithmSuiteId, _19_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
      if (!(!((_29_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(163,35): " + java.lang.String.valueOf(_29_valueOrError6));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _30_decryptionMaterialsIn;
      _30_decryptionMaterialsIn = (_29_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = (_18_kmsEcdhKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_30_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _28_edk)));
      _31_valueOrError7 = _out6;
      if (!(!((_31_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(170,36): " + java.lang.String.valueOf(_31_valueOrError7));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _32_decryptionMaterialsOut;
      _32_decryptionMaterialsOut = (_31_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(((_25_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_32_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(177,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(183,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(185,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _4_senderArns;
    _4_senderArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_recipientArns;
    _5_recipientArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__R());
    dafny.DafnySequence<? extends software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> _6_curveSpecs;
    _6_curveSpecs = dafny.DafnySequence.<software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> of(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_4_senderArns).length());
    for (java.math.BigInteger _7_i = java.math.BigInteger.ZERO; _7_i.compareTo(_hi0) < 0; _7_i = _7_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_publicKeyResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
      _out2 = (_3_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
      _8_publicKeyResponse = _out2;
      if (!((_8_publicKeyResponse).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(199,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_8_publicKeyResponse).dtor_value();
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _9___v8 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _10_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _11___v9 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _12___v10 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _13___v11 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _14___v12 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _15___v13 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _16___v14 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
      if (!((_10_PublicKey).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(201,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      System.out.print((dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\nTest with sender: "), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_4_senderArns).select(dafny.Helpers.toInt((_7_i)))))), dafny.DafnySequence.asString(" and recipient: ")), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i)))))), dafny.DafnySequence.asString("\n"))).verbatimString());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_4_senderArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_10_PublicKey).dtor_value())), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((_6_curveSpecs).select(dafny.Helpers.toInt((_7_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _17_valueOrError2 = _out3;
      if (!(!((_17_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(204,28): " + java.lang.String.valueOf(_17_valueOrError2));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _18_kmsEcdhKeyring;
      _18_kmsEcdhKeyring = (_17_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _19_encryptionContext;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
      _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
      _19_encryptionContext = _out4;
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _20_materials;
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _out5;
      _out5 = __default.GetTestMaterials(__default.TEST__DBE__ALG__SUITE__ID());
      _20_materials = _out5;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = (_18_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_20_materials));
      _21_valueOrError3 = _out6;
      if (!(!((_21_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(221,36): " + java.lang.String.valueOf(_21_valueOrError3));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _22_encryptionMaterialsOut;
      _22_encryptionMaterialsOut = (_21_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _23_valueOrError4 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_22_encryptionMaterialsOut).dtor_materials());
      if (!(!((_23_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(225,15): " + java.lang.String.valueOf(_23_valueOrError4));
      }
      dafny.Tuple0 _24___v15;
      _24___v15 = (_23_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_22_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(227,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _25_edk;
      _25_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_22_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _26_valueOrError5 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(__default.TEST__DBE__ALG__SUITE__ID(), _19_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
      if (!(!((_26_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(230,35): " + java.lang.String.valueOf(_26_valueOrError5));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _27_decryptionMaterialsIn;
      _27_decryptionMaterialsIn = (_26_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
      _out7 = (_18_kmsEcdhKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_27_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _25_edk)));
      _28_valueOrError6 = _out7;
      if (!(!((_28_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(237,36): " + java.lang.String.valueOf(_28_valueOrError6));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _29_decryptionMaterialsOut;
      _29_decryptionMaterialsOut = (_28_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(((_22_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_29_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(244,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestKmsEcdhKeyringDiscoverySuccess()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(251,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(253,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _4_senderArns;
    _4_senderArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S());
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_recipientArns;
    _5_recipientArns = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__R());
    dafny.DafnySequence<? extends software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> _6_curveSpecs;
    _6_curveSpecs = dafny.DafnySequence.<software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> of(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_4_senderArns).length());
    for (java.math.BigInteger _7_i = java.math.BigInteger.ZERO; _7_i.compareTo(_hi0) < 0; _7_i = _7_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_publicKeyResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
      _out2 = (_3_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
      _8_publicKeyResponse = _out2;
      if (!((_8_publicKeyResponse).is_Success())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(267,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_8_publicKeyResponse).dtor_value();
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _9___v16 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _10_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _11___v17 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _12___v18 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
      Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _13___v19 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _14___v20 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _15___v21 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _16___v22 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
      if (!((_10_PublicKey).is_Some())) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(269,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_4_senderArns).select(dafny.Helpers.toInt((_7_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_10_PublicKey).dtor_value())), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((_6_curveSpecs).select(dafny.Helpers.toInt((_7_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _17_valueOrError2 = _out3;
      if (!(!((_17_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(271,28): " + java.lang.String.valueOf(_17_valueOrError2));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _18_kmsEcdhKeyring;
      _18_kmsEcdhKeyring = (_17_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
      _out4 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i))))))), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((_6_curveSpecs).select(dafny.Helpers.toInt((_7_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _19_valueOrError3 = _out4;
      if (!(!((_19_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(285,37): " + java.lang.String.valueOf(_19_valueOrError3));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _20_kmsEcdhKeyringDiscovery;
      _20_kmsEcdhKeyringDiscovery = (_19_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _21_encryptionContext;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out5;
      _out5 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
      _21_encryptionContext = _out5;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _22_algorithmSuiteId;
      _22_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _23_suite;
      _23_suite = AlgorithmSuites_Compile.__default.GetSuite(_22_algorithmSuiteId);
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _24_valueOrError4 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_22_algorithmSuiteId, _21_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
      if (!(!((_24_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(302,35): " + java.lang.String.valueOf(_24_valueOrError4));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _25_encryptionMaterialsIn;
      _25_encryptionMaterialsIn = (_24_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = (_18_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_25_encryptionMaterialsIn));
      _26_valueOrError5 = _out6;
      if (!(!((_26_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(312,36): " + java.lang.String.valueOf(_26_valueOrError5));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _27_encryptionMaterialsOut;
      _27_encryptionMaterialsOut = (_26_valueOrError5).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError6 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _28_valueOrError6 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_27_encryptionMaterialsOut).dtor_materials());
      if (!(!((_28_valueOrError6).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(316,15): " + java.lang.String.valueOf(_28_valueOrError6));
      }
      dafny.Tuple0 _29___v23;
      _29___v23 = (_28_valueOrError6).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_27_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(318,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _30_edk;
      _30_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_27_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _31_valueOrError7 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_22_algorithmSuiteId, _21_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
      if (!(!((_31_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(321,35): " + java.lang.String.valueOf(_31_valueOrError7));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _32_decryptionMaterialsIn;
      _32_decryptionMaterialsIn = (_31_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      System.out.print((dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\nDiscovery Test for: "), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_recipientArns).select(dafny.Helpers.toInt((_7_i)))))), dafny.DafnySequence.asString("\n"))).verbatimString());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _33_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
      _out7 = (_20_kmsEcdhKeyringDiscovery).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_32_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _30_edk)));
      _33_valueOrError8 = _out7;
      if (!(!((_33_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(329,36): " + java.lang.String.valueOf(_33_valueOrError8));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _34_decryptionMaterialsOut;
      _34_decryptionMaterialsOut = (_33_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(((_27_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_34_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(336,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(343,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(344,22): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _3_primitives;
    _3_primitives = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = (_3_primitives).GenerateECCKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput.create(__default.P256()));
    _4_valueOrError2 = _out2;
    if (!(!((_4_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(346,28): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput _5_recipientKeypair;
    _5_recipientKeypair = (_4_valueOrError2).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _6_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _6_valueOrError3 = _out3;
    if (!(!((_6_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(352,21): " + java.lang.String.valueOf(_6_valueOrError3));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _7_kmsClient;
    _7_kmsClient = (_6_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _8_publicKeyResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out4;
    _out4 = (_7_kmsClient).GetPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor())));
    _8_publicKeyResponse = _out4;
    if (!((_8_publicKeyResponse).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(359,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _let_tmp_rhs0 = (_8_publicKeyResponse).dtor_value();
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _9___v24 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyId;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _10_PublicKey = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._PublicKey;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.CustomerMasterKeySpec> _11___v25 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._CustomerMasterKeySpec;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeySpec> _12___v26 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeySpec;
    Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType> _13___v27 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyUsage;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>> _14___v28 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._EncryptionAlgorithms;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.SigningAlgorithmSpec>> _15___v29 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._SigningAlgorithms;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends software.amazon.cryptography.services.kms.internaldafny.types.KeyAgreementAlgorithmSpec>> _16___v30 = ((software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse)_let_tmp_rhs0)._KeyAgreementAlgorithms;
    if (!((_10_PublicKey).is_Some())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(362,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), (_10_PublicKey).dtor_value()), ((_5_recipientKeypair).dtor_publicKey()).dtor_der())), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256(), _7_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _17_valueOrError4 = _out5;
    if (!(!((_17_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(364,26): " + java.lang.String.valueOf(_17_valueOrError4));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _18_kmsEcdhKeyring;
    _18_kmsEcdhKeyring = (_17_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_1_mpl).CreateRawEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_RawPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput.create(((_5_recipientKeypair).dtor_privateKey()).dtor_pem(), (_10_PublicKey).dtor_value())), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256()));
    _19_valueOrError5 = _out6;
    if (!(!((_19_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(379,28): " + java.lang.String.valueOf(_19_valueOrError5));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _20_recipientKeyring;
    _20_recipientKeyring = (_19_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _21_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out7;
    _out7 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _21_encryptionContext = _out7;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _22_algorithmSuiteId;
    _22_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _23_suite;
    _23_suite = AlgorithmSuites_Compile.__default.GetSuite(_22_algorithmSuiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _24_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_22_algorithmSuiteId, _21_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_24_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(395,33): " + java.lang.String.valueOf(_24_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _25_encryptionMaterialsIn;
    _25_encryptionMaterialsIn = (_24_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_18_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_25_encryptionMaterialsIn));
    _26_valueOrError7 = _out8;
    if (!(!((_26_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(405,34): " + java.lang.String.valueOf(_26_valueOrError7));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _27_encryptionMaterialsOut;
    _27_encryptionMaterialsOut = (_26_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError8 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _28_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_27_encryptionMaterialsOut).dtor_materials());
    if (!(!((_28_valueOrError8).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(409,13): " + java.lang.String.valueOf(_28_valueOrError8));
    }
    dafny.Tuple0 _29___v31;
    _29___v31 = (_28_valueOrError8).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_27_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(411,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _30_edk;
    _30_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_27_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _31_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_22_algorithmSuiteId, _21_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    if (!(!((_31_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(414,33): " + java.lang.String.valueOf(_31_valueOrError9));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _32_decryptionMaterialsIn;
    _32_decryptionMaterialsIn = (_31_valueOrError9).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _33_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_20_recipientKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_32_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _30_edk)));
    _33_valueOrError10 = _out9;
    if (!(!((_33_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(421,34): " + java.lang.String.valueOf(_33_valueOrError10));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _34_decryptionMaterialsOut;
    _34_decryptionMaterialsOut = (_33_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!(java.util.Objects.equals(((_27_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_34_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(428,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestKmsEcdhKeyringWithDerPublicKeys()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(434,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(436,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((__default.CURVES()).length());
    for (java.math.BigInteger _4_i = java.math.BigInteger.ZERO; _4_i.compareTo(_hi0) < 0; _4_i = _4_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _5_valueOrError2 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.derKmsSenderPublicKeyStrings()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_5_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(440,29): " + java.lang.String.valueOf(_5_valueOrError2));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _6_senderPublicKey;
      _6_senderPublicKey = (_5_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _7_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _7_valueOrError3 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.derKmsRecipientPublicKeyStrings()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_7_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(441,32): " + java.lang.String.valueOf(_7_valueOrError3));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _8_recipientPublicKey;
      _8_recipientPublicKey = (_7_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
      _out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderKmsKeys()).select(dafny.Helpers.toInt((_4_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey), _8_recipientPublicKey)), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.CURVES()).select(dafny.Helpers.toInt((_4_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _9_valueOrError4 = _out2;
      if (!(!((_9_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(443,34): " + java.lang.String.valueOf(_9_valueOrError4));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _10_senderKmsEcdhKeyring;
      _10_senderKmsEcdhKeyring = (_9_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.recipientKmsKeys()).select(dafny.Helpers.toInt((_4_i))))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _8_recipientPublicKey), _6_senderPublicKey)), ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.CURVES()).select(dafny.Helpers.toInt((_4_i))))), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _11_valueOrError5 = _out3;
      if (!(!((_11_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(458,37): " + java.lang.String.valueOf(_11_valueOrError5));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _12_recipientKmsEcdhKeyring;
      _12_recipientKmsEcdhKeyring = (_11_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _13_encryptionContext;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
      _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
      _13_encryptionContext = _out4;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _14_algorithmSuiteId;
      _14_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15_suite;
      _15_suite = AlgorithmSuites_Compile.__default.GetSuite(_14_algorithmSuiteId);
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _16_valueOrError6 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_14_algorithmSuiteId, _13_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
      if (!(!((_16_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(477,35): " + java.lang.String.valueOf(_16_valueOrError6));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _17_encryptionMaterialsIn;
      _17_encryptionMaterialsIn = (_16_valueOrError6).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
      _out5 = (_10_senderKmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_17_encryptionMaterialsIn));
      _18_valueOrError7 = _out5;
      if (!(!((_18_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(487,36): " + java.lang.String.valueOf(_18_valueOrError7));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _19_encryptionMaterialsOut;
      _19_encryptionMaterialsOut = (_18_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError8 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _20_valueOrError8 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_19_encryptionMaterialsOut).dtor_materials());
      if (!(!((_20_valueOrError8).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(491,15): " + java.lang.String.valueOf(_20_valueOrError8));
      }
      dafny.Tuple0 _21___v32;
      _21___v32 = (_20_valueOrError8).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_19_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(493,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _22_edk;
      _22_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_19_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _23_valueOrError9 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_14_algorithmSuiteId, _13_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
      if (!(!((_23_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(496,35): " + java.lang.String.valueOf(_23_valueOrError9));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _24_decryptionMaterialsIn;
      _24_decryptionMaterialsIn = (_23_valueOrError9).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = (_12_recipientKmsEcdhKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_24_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _22_edk)));
      _25_valueOrError10 = _out6;
      if (!(!((_25_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(503,36): " + java.lang.String.valueOf(_25_valueOrError10));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _26_decryptionMaterialsOut;
      _26_decryptionMaterialsOut = (_25_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(((_19_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_26_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(510,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestKmsEcdhRawEcdhKeyringWithDerPublicKeys()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(518,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(520,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((__default.CURVES()).length());
    for (java.math.BigInteger _4_i = java.math.BigInteger.ZERO; _4_i.compareTo(_hi0) < 0; _4_i = _4_i.add(java.math.BigInteger.ONE)) {
      dafny.DafnySequence<? extends Character> _5_senderKmsKey;
      _5_senderKmsKey = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.senderKmsKeys()).select(dafny.Helpers.toInt((_4_i)))));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _6_valueOrError2 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.derKmsSenderPublicKeyStrings()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_6_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(525,29): " + java.lang.String.valueOf(_6_valueOrError2));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _7_senderPublicKey;
      _7_senderPublicKey = (_6_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _8_valueOrError3 = UTF8.__default.Encode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.rawEccPrivateKeys()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_8_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(526,33): " + java.lang.String.valueOf(_8_valueOrError3));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _9_recipientPrivateKey;
      _9_recipientPrivateKey = (_8_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _10_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _10_valueOrError4 = Base64_Compile.__default.Decode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((__default.rawEccPublicKeysB64der()).select(dafny.Helpers.toInt((_4_i))))));
      if (!(!((_10_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(527,32): " + java.lang.String.valueOf(_10_valueOrError4));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _11_recipientPublicKey;
      _11_recipientPublicKey = (_10_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _12_curve;
      _12_curve = ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((__default.CURVES()).select(dafny.Helpers.toInt((_4_i)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
      _out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_5_senderKmsKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _7_senderPublicKey), _11_recipientPublicKey)), _12_curve, _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
      _13_valueOrError5 = _out2;
      if (!(!((_13_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(530,34): " + java.lang.String.valueOf(_13_valueOrError5));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _14_senderKmsEcdhKeyring;
      _14_senderKmsEcdhKeyring = (_13_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = (_1_mpl).CreateRawEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_RawPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput.create(_9_recipientPrivateKey, _7_senderPublicKey)), _12_curve));
      _15_valueOrError6 = _out3;
      if (!(!((_15_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(545,33): " + java.lang.String.valueOf(_15_valueOrError6));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _16_recipientRawKeyring;
      _16_recipientRawKeyring = (_15_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _17_encryptionContext;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out4;
      _out4 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
      _17_encryptionContext = _out4;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _18_algorithmSuiteId;
      _18_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _19_suite;
      _19_suite = AlgorithmSuites_Compile.__default.GetSuite(_18_algorithmSuiteId);
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _20_valueOrError7 = (_1_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_18_algorithmSuiteId, _17_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
      if (!(!((_20_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(561,35): " + java.lang.String.valueOf(_20_valueOrError7));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _21_encryptionMaterialsIn;
      _21_encryptionMaterialsIn = (_20_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
      _out5 = (_14_senderKmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_21_encryptionMaterialsIn));
      _22_valueOrError8 = _out5;
      if (!(!((_22_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(571,36): " + java.lang.String.valueOf(_22_valueOrError8));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _23_encryptionMaterialsOut;
      _23_encryptionMaterialsOut = (_22_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError9 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _24_valueOrError9 = (_1_mpl).EncryptionMaterialsHasPlaintextDataKey((_23_encryptionMaterialsOut).dtor_materials());
      if (!(!((_24_valueOrError9).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(575,15): " + java.lang.String.valueOf(_24_valueOrError9));
      }
      dafny.Tuple0 _25___v33;
      _25___v33 = (_24_valueOrError9).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(java.math.BigInteger.valueOf((((_23_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).length()), java.math.BigInteger.ONE))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(577,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _26_edk;
      _26_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((((_23_encryptionMaterialsOut).dtor_materials()).dtor_encryptedDataKeys()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _27_valueOrError10 = (_1_mpl).InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create(_18_algorithmSuiteId, _17_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
      if (!(!((_27_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(580,35): " + java.lang.String.valueOf(_27_valueOrError10));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _28_decryptionMaterialsIn;
      _28_decryptionMaterialsIn = (_27_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_valueOrError11 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = (_16_recipientRawKeyring).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_28_decryptionMaterialsIn, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _26_edk)));
      _29_valueOrError11 = _out6;
      if (!(!((_29_valueOrError11).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(587,36): " + java.lang.String.valueOf(_29_valueOrError11));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _30_decryptionMaterialsOut;
      _30_decryptionMaterialsOut = (_29_valueOrError11).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (!(java.util.Objects.equals(((_23_encryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey(), ((_30_decryptionMaterialsOut).dtor_materials()).dtor_plaintextDataKey()))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(594,6): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
    }
  }
  public static void TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(603,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(605,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError2 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__S());
    if (!(!((_4_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(607,27): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _5_senderPublicKey;
    _5_senderPublicKey = (_4_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _6_valueOrError3 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__R());
    if (!(!((_6_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(608,30): " + java.lang.String.valueOf(_6_valueOrError3));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_recipientPublicKey;
    _7_recipientPublicKey = (_6_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_senderKmsEcdhKeyring;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _5_senderPublicKey), _7_recipientPublicKey)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _8_senderKmsEcdhKeyring = _out2;
    if (!((_8_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(625,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(630,15): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _1_mpl;
    _1_mpl = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(632,21): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _3_kmsClient;
    _3_kmsClient = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _4_senderKmsKey256;
    _4_senderKmsKey256 = TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _5_valueOrError2 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__S());
    if (!(!((_5_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(635,33): " + java.lang.String.valueOf(_5_valueOrError2));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_senderPublicKey256;
    _6_senderPublicKey256 = (_5_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _7_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _7_valueOrError3 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P256__PUBLIC__R());
    if (!(!((_7_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(636,33): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_recipientPublicKey256;
    _8_recipientPublicKey256 = (_7_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _9_senderKmsKey384;
    _9_senderKmsKey384 = TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _10_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _10_valueOrError4 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__384__PUBLIC__KEY__S());
    if (!(!((_10_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(639,33): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_senderPublicKey384;
    _11_senderPublicKey384 = (_10_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _12_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _12_valueOrError5 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P384__PUBLIC__R());
    if (!(!((_12_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(640,33): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _13_recipientPublicKey384;
    _13_recipientPublicKey384 = (_12_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _14_senderKmsKey521;
    _14_senderKmsKey521 = TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _15_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _15_valueOrError6 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__521__PUBLIC__KEY__S());
    if (!(!((_15_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(643,33): " + java.lang.String.valueOf(_15_valueOrError6));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _16_senderPublicKey521;
    _16_senderPublicKey521 = (_15_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _17_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _17_valueOrError7 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P521__PUBLIC__R());
    if (!(!((_17_valueOrError7).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(644,33): " + java.lang.String.valueOf(_17_valueOrError7));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _18_recipientPublicKey521;
    _18_recipientPublicKey521 = (_17_valueOrError7).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_senderKmsEcdhKeyring;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _8_recipientPublicKey256)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out2;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(662,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _8_recipientPublicKey256)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _13_recipientPublicKey384)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out4;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(694,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _13_recipientPublicKey384)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out5;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _18_recipientPublicKey521)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out6;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(726,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _18_recipientPublicKey521)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out7;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _13_recipientPublicKey384)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out8;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(759,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _18_recipientPublicKey521)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out9;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(775,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _8_recipientPublicKey256)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out10;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(792,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _18_recipientPublicKey521)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out11;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(808,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out12;
    _out12 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _8_recipientPublicKey256)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out12;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(825,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out13;
    _out13 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _13_recipientPublicKey384)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out13;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(841,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out14;
    _out14 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _8_recipientPublicKey256)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out14;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(860,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out15;
    _out15 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _8_recipientPublicKey256)), __default.P256(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out15;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(876,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out16;
    _out16 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _13_recipientPublicKey384)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out16;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(893,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out17;
    _out17 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_14_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _16_senderPublicKey521), _13_recipientPublicKey384)), __default.P384(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out17;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(909,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out18;
    _out18 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_4_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _6_senderPublicKey256), _18_recipientPublicKey521)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out18;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(926,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out19;
    _out19 = (_1_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_9_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_senderPublicKey384), _18_recipientPublicKey521)), __default.P521(), _3_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _19_senderKmsEcdhKeyring = _out19;
    if (!((_19_senderKmsEcdhKeyring).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(942,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestLyingKmsKey()
  {
    dafny.DafnySequence<? extends Character> _0_senderKmsKey256;
    _0_senderKmsKey256 = TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _1_valueOrError0 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__S());
    if (!(!((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(948,33): " + java.lang.String.valueOf(_1_valueOrError0));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _2_senderPublicKey256;
    _2_senderPublicKey256 = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _3_valueOrError1 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P256__PUBLIC__R());
    if (!(!((_3_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(949,33): " + java.lang.String.valueOf(_3_valueOrError1));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _4_recipientPublicKey256;
    _4_recipientPublicKey256 = (_3_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _5_senderKmsKey384;
    _5_senderKmsKey384 = TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _6_valueOrError2 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__384__PUBLIC__KEY__S());
    if (!(!((_6_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(952,33): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_senderPublicKey384;
    _7_senderPublicKey384 = (_6_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _8_valueOrError3 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P384__PUBLIC__R());
    if (!(!((_8_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(953,33): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _9_recipientPublicKey384;
    _9_recipientPublicKey384 = (_8_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnySequence<? extends Character> _10_senderKmsKey521;
    _10_senderKmsKey521 = TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _11_valueOrError4 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.KMS__ECC__521__PUBLIC__KEY__S());
    if (!(!((_11_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(956,33): " + java.lang.String.valueOf(_11_valueOrError4));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _12_senderPublicKey521;
    _12_senderPublicKey521 = (_11_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _13_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _13_valueOrError5 = Base64_Compile.__default.Decode(TestUtils_Compile.__default.ECC__P521__PUBLIC__R());
    if (!(!((_13_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(957,33): " + java.lang.String.valueOf(_13_valueOrError5));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _14_recipientPublicKey521;
    _14_recipientPublicKey521 = (_13_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
    _15_valueOrError6 = _out0;
    if (!(!((_15_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(959,15): " + java.lang.String.valueOf(_15_valueOrError6));
    }
    software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _16_mpl;
    _16_mpl = (_15_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _17_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
    _17_valueOrError7 = _out1;
    if (!(!((_17_valueOrError7).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(961,21): " + java.lang.String.valueOf(_17_valueOrError7));
    }
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _18_kmsClient;
    _18_kmsClient = (_17_valueOrError7).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor());
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _19_encryptionContext;
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _out2;
    _out2 = TestUtils_Compile.__default.SmallEncryptionContext(TestUtils_Compile.SmallEncryptionContextVariation.create_A());
    _19_encryptionContext = _out2;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _20_algorithmSuiteId;
    _20_algorithmSuiteId = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _21_suite;
    _21_suite = AlgorithmSuites_Compile.__default.GetSuite(_20_algorithmSuiteId);
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _22_valueOrError8 = (_16_mpl).InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_20_algorithmSuiteId, _19_encryptionContext, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
    if (!(!((_22_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(967,33): " + java.lang.String.valueOf(_22_valueOrError8));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _23_encryptionMaterialsIn;
    _23_encryptionMaterialsIn = (_22_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_5_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _2_senderPublicKey256), _4_recipientPublicKey256)), __default.P256(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _24_valueOrError9 = _out3;
    if (!(!((_24_valueOrError9).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(985,26): " + java.lang.String.valueOf(_24_valueOrError9));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _25_kmsEcdhKeyring;
    _25_kmsEcdhKeyring = (_24_valueOrError9).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_encryptionMaterialsOut;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out4;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1002,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_10_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _2_senderPublicKey256), _4_recipientPublicKey256)), __default.P256(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _27_valueOrError10 = _out5;
    if (!(!((_27_valueOrError10).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1004,22): " + java.lang.String.valueOf(_27_valueOrError10));
    }
    _25_kmsEcdhKeyring = (_27_valueOrError10).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out6;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1021,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError11 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_0_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _7_senderPublicKey384), _9_recipientPublicKey384)), __default.P384(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _28_valueOrError11 = _out7;
    if (!(!((_28_valueOrError11).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1024,22): " + java.lang.String.valueOf(_28_valueOrError11));
    }
    _25_kmsEcdhKeyring = (_28_valueOrError11).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out8;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1041,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_valueOrError12 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_10_senderKmsKey521, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _7_senderPublicKey384), _9_recipientPublicKey384)), __default.P384(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _29_valueOrError12 = _out9;
    if (!(!((_29_valueOrError12).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1043,22): " + java.lang.String.valueOf(_29_valueOrError12));
    }
    _25_kmsEcdhKeyring = (_29_valueOrError12).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out10;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1060,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _30_valueOrError13 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_0_senderKmsKey256, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _12_senderPublicKey521), _14_recipientPublicKey521)), __default.P521(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _30_valueOrError13 = _out11;
    if (!(!((_30_valueOrError13).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1063,22): " + java.lang.String.valueOf(_30_valueOrError13));
    }
    _25_kmsEcdhKeyring = (_30_valueOrError13).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out12;
    _out12 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out12;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1080,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError14 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out13;
    _out13 = (_16_mpl).CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_5_senderKmsKey384, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _12_senderPublicKey521), _14_recipientPublicKey521)), __default.P521(), _18_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    _31_valueOrError14 = _out13;
    if (!(!((_31_valueOrError14).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1082,22): " + java.lang.String.valueOf(_31_valueOrError14));
    }
    _25_kmsEcdhKeyring = (_31_valueOrError14).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out14;
    _out14 = (_25_kmsEcdhKeyring).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_23_encryptionMaterialsIn));
    _26_encryptionMaterialsOut = _out14;
    if (!((_26_encryptionMaterialsOut).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1099,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec P256()
  {
    return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256();
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec P384()
  {
    return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384();
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec P521()
  {
    return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521();
  }
  public static dafny.DafnySequence<? extends software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> CURVES()
  {
    return dafny.DafnySequence.<software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec> of(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec._typeDescriptor(), __default.P256(), __default.P384(), __default.P521());
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId TEST__DBE__ALG__SUITE__ID()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> derKmsSenderPublicKeyStrings()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__S(), TestUtils_Compile.__default.KMS__ECC__384__PUBLIC__KEY__S(), TestUtils_Compile.__default.KMS__ECC__521__PUBLIC__KEY__S());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> derKmsRecipientPublicKeyStrings()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__PUBLIC__KEY__R(), TestUtils_Compile.__default.KMS__ECC__384__PUBLIC__KEY__R(), TestUtils_Compile.__default.KMS__ECC__521__PUBLIC__KEY__R());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> senderKmsKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__S(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__S());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> recipientKmsKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.KMS__ECC__256__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__384__KEY__ARN__R(), TestUtils_Compile.__default.KMS__ECC__521__KEY__ARN__R());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> rawEccPrivateKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.ECC__P256__PRIVATE(), TestUtils_Compile.__default.ECC__P384__PRIVATE(), TestUtils_Compile.__default.ECC__P521__PRIVATE());
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> rawEccPublicKeysB64der()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), TestUtils_Compile.__default.ECC__P256__PUBLIC(), TestUtils_Compile.__default.ECC__P384__PUBLIC(), TestUtils_Compile.__default.ECC__P521__PUBLIC());
  }
  @Override
  public java.lang.String toString() {
    return "TestAwsKmsEcdhKeyring._default";
  }
}
