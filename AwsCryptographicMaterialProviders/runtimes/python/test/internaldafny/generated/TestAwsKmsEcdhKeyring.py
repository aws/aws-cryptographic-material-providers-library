import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestLyingBranchKey as TestLyingBranchKey
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawECDHKeyring as TestRawECDHKeyring
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring

# Module: TestAwsKmsEcdhKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetTestMaterials(suiteId):
        out: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_1167_mpl_: MaterialProviders.MaterialProvidersClient
        d_1168_valueOrError0_: Wrappers.Result = None
        out446_: Wrappers.Result
        out446_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1168_valueOrError0_ = out446_
        if not(not((d_1168_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(44,15): " + _dafny.string_of(d_1168_valueOrError0_))
        d_1167_mpl_ = (d_1168_valueOrError0_).Extract()
        d_1169_encryptionContext_: _dafny.Map
        out447_: _dafny.Map
        out447_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1169_encryptionContext_ = out447_
        d_1170_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1170_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_1171_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1172_valueOrError1_: Wrappers.Result = None
        d_1172_valueOrError1_ = (d_1167_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_1169_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1172_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(49,33): " + _dafny.string_of(d_1172_valueOrError1_))
        d_1171_encryptionMaterialsIn_ = (d_1172_valueOrError1_).Extract()
        out = d_1171_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestKmsEcdhConfigurationFailure():
        d_1173_mpl_: MaterialProviders.MaterialProvidersClient
        d_1174_valueOrError0_: Wrappers.Result = None
        out448_: Wrappers.Result
        out448_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1174_valueOrError0_ = out448_
        if not(not((d_1174_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(63,15): " + _dafny.string_of(d_1174_valueOrError0_))
        d_1173_mpl_ = (d_1174_valueOrError0_).Extract()
        d_1175_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1176_valueOrError1_: Wrappers.Result = None
        out449_: Wrappers.Result
        out449_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1176_valueOrError1_ = out449_
        if not(not((d_1176_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(65,21): " + _dafny.string_of(d_1176_valueOrError1_))
        d_1175_kmsClient_ = (d_1176_valueOrError1_).Extract()
        d_1177_kmsEcdhKeyringDiscoveryConfiguration_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1178_valueOrError2_: Wrappers.Result = None
        out450_: Wrappers.Result
        out450_ = (d_1173_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__R)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_1175_kmsClient_, Wrappers.Option_None()))
        d_1178_valueOrError2_ = out450_
        if not(not((d_1178_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(67,48): " + _dafny.string_of(d_1178_valueOrError2_))
        d_1177_kmsEcdhKeyringDiscoveryConfiguration_ = (d_1178_valueOrError2_).Extract()
        d_1179_encryptionContext_: _dafny.Map
        out451_: _dafny.Map
        out451_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1179_encryptionContext_ = out451_
        d_1180_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_1180_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1181_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1182_valueOrError3_: Wrappers.Result = None
        d_1182_valueOrError3_ = (d_1173_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1180_algorithmSuiteId_, d_1179_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1182_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(83,33): " + _dafny.string_of(d_1182_valueOrError3_))
        d_1181_encryptionMaterialsIn_ = (d_1182_valueOrError3_).Extract()
        d_1183_encryptionMaterialsOut_: Wrappers.Result
        out452_: Wrappers.Result
        out452_ = (d_1177_kmsEcdhKeyringDiscoveryConfiguration_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1181_encryptionMaterialsIn_))
        d_1183_encryptionMaterialsOut_ = out452_
        if not((d_1183_encryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_1183_encryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(98,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1184_expectedErrorMessage_: _dafny.Seq
        d_1184_expectedErrorMessage_ = ErrorMessages.default__.KMS__ECDH__DISCOVERY__ENCRYPT__ERROR
        if not((((d_1183_encryptionMaterialsOut_).error).message) == (d_1184_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess():
        d_1185_mpl_: MaterialProviders.MaterialProvidersClient
        d_1186_valueOrError0_: Wrappers.Result = None
        out453_: Wrappers.Result
        out453_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1186_valueOrError0_ = out453_
        if not(not((d_1186_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(105,15): " + _dafny.string_of(d_1186_valueOrError0_))
        d_1185_mpl_ = (d_1186_valueOrError0_).Extract()
        d_1187_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1188_valueOrError1_: Wrappers.Result = None
        out454_: Wrappers.Result
        out454_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1188_valueOrError1_ = out454_
        if not(not((d_1188_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(107,21): " + _dafny.string_of(d_1188_valueOrError1_))
        d_1187_kmsClient_ = (d_1188_valueOrError1_).Extract()
        d_1189_senderArns_: _dafny.Seq
        d_1189_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_1190_recipientArns_: _dafny.Seq
        d_1190_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_1191_curveSpecs_: _dafny.Seq
        d_1191_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi0_ = len(d_1189_senderArns_)
        for d_1192_i_ in range(0, hi0_):
            d_1193_publicKeyResponse_: Wrappers.Result
            out455_: Wrappers.Result
            out455_ = (d_1187_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_1190_recipientArns_)[d_1192_i_], Wrappers.Option_None()))
            d_1193_publicKeyResponse_ = out455_
            if not((d_1193_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(121,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs1_ = (d_1193_publicKeyResponse_).value
            d_1194___v0_ = let_tmp_rhs1_.KeyId
            d_1195_PublicKey_ = let_tmp_rhs1_.PublicKey
            d_1196___v1_ = let_tmp_rhs1_.CustomerMasterKeySpec
            d_1197___v2_ = let_tmp_rhs1_.KeySpec
            d_1198___v3_ = let_tmp_rhs1_.KeyUsage
            d_1199___v4_ = let_tmp_rhs1_.EncryptionAlgorithms
            d_1200___v5_ = let_tmp_rhs1_.SigningAlgorithms
            d_1201___v6_ = let_tmp_rhs1_.KeyAgreementAlgorithms
            if not((d_1195_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(123,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            _dafny.print(_dafny.string_of(((((_dafny.Seq("\nTest with sender: ")) + ((d_1189_senderArns_)[d_1192_i_])) + (_dafny.Seq(" and recipient: "))) + ((d_1190_recipientArns_)[d_1192_i_])) + (_dafny.Seq("\n"))))
            d_1202_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1203_valueOrError2_: Wrappers.Result = None
            out456_: Wrappers.Result
            out456_ = (d_1185_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_1189_senderArns_)[d_1192_i_], Wrappers.Option_None(), (d_1195_PublicKey_).value)), (d_1191_curveSpecs_)[d_1192_i_], d_1187_kmsClient_, Wrappers.Option_None()))
            d_1203_valueOrError2_ = out456_
            if not(not((d_1203_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(126,28): " + _dafny.string_of(d_1203_valueOrError2_))
            d_1202_kmsEcdhKeyring_ = (d_1203_valueOrError2_).Extract()
            d_1204_encryptionContext_: _dafny.Map
            out457_: _dafny.Map
            out457_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_1204_encryptionContext_ = out457_
            d_1205_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_1205_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_1206_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_1206_suite_ = AlgorithmSuites.default__.GetSuite(d_1205_algorithmSuiteId_)
            d_1207_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1208_valueOrError3_: Wrappers.Result = None
            d_1208_valueOrError3_ = (d_1185_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1205_algorithmSuiteId_, d_1204_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_1208_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(144,35): " + _dafny.string_of(d_1208_valueOrError3_))
            d_1207_encryptionMaterialsIn_ = (d_1208_valueOrError3_).Extract()
            d_1209_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_1210_valueOrError4_: Wrappers.Result = None
            out458_: Wrappers.Result
            out458_ = (d_1202_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1207_encryptionMaterialsIn_))
            d_1210_valueOrError4_ = out458_
            if not(not((d_1210_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(154,36): " + _dafny.string_of(d_1210_valueOrError4_))
            d_1209_encryptionMaterialsOut_ = (d_1210_valueOrError4_).Extract()
            d_1211___v7_: tuple
            d_1212_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1212_valueOrError5_ = (d_1185_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1209_encryptionMaterialsOut_).materials)
            if not(not((d_1212_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(158,15): " + _dafny.string_of(d_1212_valueOrError5_))
            d_1211___v7_ = (d_1212_valueOrError5_).Extract()
            if not((len(((d_1209_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(160,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1213_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_1213_edk_ = (((d_1209_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_1214_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_1215_valueOrError6_: Wrappers.Result = None
            d_1215_valueOrError6_ = (d_1185_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1205_algorithmSuiteId_, d_1204_encryptionContext_, _dafny.Seq([])))
            if not(not((d_1215_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(163,35): " + _dafny.string_of(d_1215_valueOrError6_))
            d_1214_decryptionMaterialsIn_ = (d_1215_valueOrError6_).Extract()
            d_1216_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_1217_valueOrError7_: Wrappers.Result = None
            out459_: Wrappers.Result
            out459_ = (d_1202_kmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1214_decryptionMaterialsIn_, _dafny.Seq([d_1213_edk_])))
            d_1217_valueOrError7_ = out459_
            if not(not((d_1217_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(170,36): " + _dafny.string_of(d_1217_valueOrError7_))
            d_1216_decryptionMaterialsOut_ = (d_1217_valueOrError7_).Extract()
            if not((((d_1209_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1216_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(177,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite():
        d_1218_mpl_: MaterialProviders.MaterialProvidersClient
        d_1219_valueOrError0_: Wrappers.Result = None
        out460_: Wrappers.Result
        out460_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1219_valueOrError0_ = out460_
        if not(not((d_1219_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(183,15): " + _dafny.string_of(d_1219_valueOrError0_))
        d_1218_mpl_ = (d_1219_valueOrError0_).Extract()
        d_1220_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1221_valueOrError1_: Wrappers.Result = None
        out461_: Wrappers.Result
        out461_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1221_valueOrError1_ = out461_
        if not(not((d_1221_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(185,21): " + _dafny.string_of(d_1221_valueOrError1_))
        d_1220_kmsClient_ = (d_1221_valueOrError1_).Extract()
        d_1222_senderArns_: _dafny.Seq
        d_1222_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_1223_recipientArns_: _dafny.Seq
        d_1223_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_1224_curveSpecs_: _dafny.Seq
        d_1224_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi1_ = len(d_1222_senderArns_)
        for d_1225_i_ in range(0, hi1_):
            d_1226_publicKeyResponse_: Wrappers.Result
            out462_: Wrappers.Result
            out462_ = (d_1220_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_1223_recipientArns_)[d_1225_i_], Wrappers.Option_None()))
            d_1226_publicKeyResponse_ = out462_
            if not((d_1226_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(199,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs2_ = (d_1226_publicKeyResponse_).value
            d_1227___v8_ = let_tmp_rhs2_.KeyId
            d_1228_PublicKey_ = let_tmp_rhs2_.PublicKey
            d_1229___v9_ = let_tmp_rhs2_.CustomerMasterKeySpec
            d_1230___v10_ = let_tmp_rhs2_.KeySpec
            d_1231___v11_ = let_tmp_rhs2_.KeyUsage
            d_1232___v12_ = let_tmp_rhs2_.EncryptionAlgorithms
            d_1233___v13_ = let_tmp_rhs2_.SigningAlgorithms
            d_1234___v14_ = let_tmp_rhs2_.KeyAgreementAlgorithms
            if not((d_1228_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(201,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            _dafny.print(_dafny.string_of(((((_dafny.Seq("\nTest with sender: ")) + ((d_1222_senderArns_)[d_1225_i_])) + (_dafny.Seq(" and recipient: "))) + ((d_1223_recipientArns_)[d_1225_i_])) + (_dafny.Seq("\n"))))
            d_1235_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1236_valueOrError2_: Wrappers.Result = None
            out463_: Wrappers.Result
            out463_ = (d_1218_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_1222_senderArns_)[d_1225_i_], Wrappers.Option_None(), (d_1228_PublicKey_).value)), (d_1224_curveSpecs_)[d_1225_i_], d_1220_kmsClient_, Wrappers.Option_None()))
            d_1236_valueOrError2_ = out463_
            if not(not((d_1236_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(204,28): " + _dafny.string_of(d_1236_valueOrError2_))
            d_1235_kmsEcdhKeyring_ = (d_1236_valueOrError2_).Extract()
            d_1237_encryptionContext_: _dafny.Map
            out464_: _dafny.Map
            out464_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_1237_encryptionContext_ = out464_
            d_1238_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            out465_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            out465_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
            d_1238_materials_ = out465_
            d_1239_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_1240_valueOrError3_: Wrappers.Result = None
            out466_: Wrappers.Result
            out466_ = (d_1235_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1238_materials_))
            d_1240_valueOrError3_ = out466_
            if not(not((d_1240_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(221,36): " + _dafny.string_of(d_1240_valueOrError3_))
            d_1239_encryptionMaterialsOut_ = (d_1240_valueOrError3_).Extract()
            d_1241___v15_: tuple
            d_1242_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1242_valueOrError4_ = (d_1218_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1239_encryptionMaterialsOut_).materials)
            if not(not((d_1242_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(225,15): " + _dafny.string_of(d_1242_valueOrError4_))
            d_1241___v15_ = (d_1242_valueOrError4_).Extract()
            if not((len(((d_1239_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(227,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1243_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_1243_edk_ = (((d_1239_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_1244_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_1245_valueOrError5_: Wrappers.Result = None
            d_1245_valueOrError5_ = (d_1218_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(default__.TEST__DBE__ALG__SUITE__ID, d_1237_encryptionContext_, _dafny.Seq([])))
            if not(not((d_1245_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(230,35): " + _dafny.string_of(d_1245_valueOrError5_))
            d_1244_decryptionMaterialsIn_ = (d_1245_valueOrError5_).Extract()
            d_1246_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_1247_valueOrError6_: Wrappers.Result = None
            out467_: Wrappers.Result
            out467_ = (d_1235_kmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1244_decryptionMaterialsIn_, _dafny.Seq([d_1243_edk_])))
            d_1247_valueOrError6_ = out467_
            if not(not((d_1247_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(237,36): " + _dafny.string_of(d_1247_valueOrError6_))
            d_1246_decryptionMaterialsOut_ = (d_1247_valueOrError6_).Extract()
            if not((((d_1239_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1246_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(244,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringDiscoverySuccess():
        d_1248_mpl_: MaterialProviders.MaterialProvidersClient
        d_1249_valueOrError0_: Wrappers.Result = None
        out468_: Wrappers.Result
        out468_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1249_valueOrError0_ = out468_
        if not(not((d_1249_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(251,15): " + _dafny.string_of(d_1249_valueOrError0_))
        d_1248_mpl_ = (d_1249_valueOrError0_).Extract()
        d_1250_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1251_valueOrError1_: Wrappers.Result = None
        out469_: Wrappers.Result
        out469_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1251_valueOrError1_ = out469_
        if not(not((d_1251_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(253,21): " + _dafny.string_of(d_1251_valueOrError1_))
        d_1250_kmsClient_ = (d_1251_valueOrError1_).Extract()
        d_1252_senderArns_: _dafny.Seq
        d_1252_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_1253_recipientArns_: _dafny.Seq
        d_1253_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_1254_curveSpecs_: _dafny.Seq
        d_1254_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi2_ = len(d_1252_senderArns_)
        for d_1255_i_ in range(0, hi2_):
            d_1256_publicKeyResponse_: Wrappers.Result
            out470_: Wrappers.Result
            out470_ = (d_1250_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_1253_recipientArns_)[d_1255_i_], Wrappers.Option_None()))
            d_1256_publicKeyResponse_ = out470_
            if not((d_1256_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(267,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs3_ = (d_1256_publicKeyResponse_).value
            d_1257___v16_ = let_tmp_rhs3_.KeyId
            d_1258_PublicKey_ = let_tmp_rhs3_.PublicKey
            d_1259___v17_ = let_tmp_rhs3_.CustomerMasterKeySpec
            d_1260___v18_ = let_tmp_rhs3_.KeySpec
            d_1261___v19_ = let_tmp_rhs3_.KeyUsage
            d_1262___v20_ = let_tmp_rhs3_.EncryptionAlgorithms
            d_1263___v21_ = let_tmp_rhs3_.SigningAlgorithms
            d_1264___v22_ = let_tmp_rhs3_.KeyAgreementAlgorithms
            if not((d_1258_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(269,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1265_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1266_valueOrError2_: Wrappers.Result = None
            out471_: Wrappers.Result
            out471_ = (d_1248_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_1252_senderArns_)[d_1255_i_], Wrappers.Option_None(), (d_1258_PublicKey_).value)), (d_1254_curveSpecs_)[d_1255_i_], d_1250_kmsClient_, Wrappers.Option_None()))
            d_1266_valueOrError2_ = out471_
            if not(not((d_1266_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(271,28): " + _dafny.string_of(d_1266_valueOrError2_))
            d_1265_kmsEcdhKeyring_ = (d_1266_valueOrError2_).Extract()
            d_1267_kmsEcdhKeyringDiscovery_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1268_valueOrError3_: Wrappers.Result = None
            out472_: Wrappers.Result
            out472_ = (d_1248_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput((d_1253_recipientArns_)[d_1255_i_])), (d_1254_curveSpecs_)[d_1255_i_], d_1250_kmsClient_, Wrappers.Option_None()))
            d_1268_valueOrError3_ = out472_
            if not(not((d_1268_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(285,37): " + _dafny.string_of(d_1268_valueOrError3_))
            d_1267_kmsEcdhKeyringDiscovery_ = (d_1268_valueOrError3_).Extract()
            d_1269_encryptionContext_: _dafny.Map
            out473_: _dafny.Map
            out473_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_1269_encryptionContext_ = out473_
            d_1270_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_1270_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_1271_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_1271_suite_ = AlgorithmSuites.default__.GetSuite(d_1270_algorithmSuiteId_)
            d_1272_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1273_valueOrError4_: Wrappers.Result = None
            d_1273_valueOrError4_ = (d_1248_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1270_algorithmSuiteId_, d_1269_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_1273_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(302,35): " + _dafny.string_of(d_1273_valueOrError4_))
            d_1272_encryptionMaterialsIn_ = (d_1273_valueOrError4_).Extract()
            d_1274_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_1275_valueOrError5_: Wrappers.Result = None
            out474_: Wrappers.Result
            out474_ = (d_1265_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1272_encryptionMaterialsIn_))
            d_1275_valueOrError5_ = out474_
            if not(not((d_1275_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(312,36): " + _dafny.string_of(d_1275_valueOrError5_))
            d_1274_encryptionMaterialsOut_ = (d_1275_valueOrError5_).Extract()
            d_1276___v23_: tuple
            d_1277_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1277_valueOrError6_ = (d_1248_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1274_encryptionMaterialsOut_).materials)
            if not(not((d_1277_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(316,15): " + _dafny.string_of(d_1277_valueOrError6_))
            d_1276___v23_ = (d_1277_valueOrError6_).Extract()
            if not((len(((d_1274_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(318,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1278_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_1278_edk_ = (((d_1274_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_1279_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_1280_valueOrError7_: Wrappers.Result = None
            d_1280_valueOrError7_ = (d_1248_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1270_algorithmSuiteId_, d_1269_encryptionContext_, _dafny.Seq([])))
            if not(not((d_1280_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(321,35): " + _dafny.string_of(d_1280_valueOrError7_))
            d_1279_decryptionMaterialsIn_ = (d_1280_valueOrError7_).Extract()
            _dafny.print(_dafny.string_of(((_dafny.Seq("\nDiscovery Test for: ")) + ((d_1253_recipientArns_)[d_1255_i_])) + (_dafny.Seq("\n"))))
            d_1281_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_1282_valueOrError8_: Wrappers.Result = None
            out475_: Wrappers.Result
            out475_ = (d_1267_kmsEcdhKeyringDiscovery_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1279_decryptionMaterialsIn_, _dafny.Seq([d_1278_edk_])))
            d_1282_valueOrError8_ = out475_
            if not(not((d_1282_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(329,36): " + _dafny.string_of(d_1282_valueOrError8_))
            d_1281_decryptionMaterialsOut_ = (d_1282_valueOrError8_).Extract()
            if not((((d_1274_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1281_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(336,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey():
        d_1283_mpl_: MaterialProviders.MaterialProvidersClient
        d_1284_valueOrError0_: Wrappers.Result = None
        out476_: Wrappers.Result
        out476_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1284_valueOrError0_ = out476_
        if not(not((d_1284_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(343,15): " + _dafny.string_of(d_1284_valueOrError0_))
        d_1283_mpl_ = (d_1284_valueOrError0_).Extract()
        d_1285_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_1286_valueOrError1_: Wrappers.Result = None
        out477_: Wrappers.Result
        out477_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_1286_valueOrError1_ = out477_
        if not(not((d_1286_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(344,22): " + _dafny.string_of(d_1286_valueOrError1_))
        d_1285_primitives_ = (d_1286_valueOrError1_).Extract()
        d_1287_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_1288_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out478_: Wrappers.Result
        out478_ = (d_1285_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_1288_valueOrError2_ = out478_
        if not(not((d_1288_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(346,28): " + _dafny.string_of(d_1288_valueOrError2_))
        d_1287_recipientKeypair_ = (d_1288_valueOrError2_).Extract()
        d_1289_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1290_valueOrError3_: Wrappers.Result = None
        out479_: Wrappers.Result
        out479_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1290_valueOrError3_ = out479_
        if not(not((d_1290_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(352,21): " + _dafny.string_of(d_1290_valueOrError3_))
        d_1289_kmsClient_ = (d_1290_valueOrError3_).Extract()
        d_1291_publicKeyResponse_: Wrappers.Result
        out480_: Wrappers.Result
        out480_ = (d_1289_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_None()))
        d_1291_publicKeyResponse_ = out480_
        if not((d_1291_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(359,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs4_ = (d_1291_publicKeyResponse_).value
        d_1292___v24_ = let_tmp_rhs4_.KeyId
        d_1293_PublicKey_ = let_tmp_rhs4_.PublicKey
        d_1294___v25_ = let_tmp_rhs4_.CustomerMasterKeySpec
        d_1295___v26_ = let_tmp_rhs4_.KeySpec
        d_1296___v27_ = let_tmp_rhs4_.KeyUsage
        d_1297___v28_ = let_tmp_rhs4_.EncryptionAlgorithms
        d_1298___v29_ = let_tmp_rhs4_.SigningAlgorithms
        d_1299___v30_ = let_tmp_rhs4_.KeyAgreementAlgorithms
        if not((d_1293_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(362,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1300_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1301_valueOrError4_: Wrappers.Result = None
        out481_: Wrappers.Result
        out481_ = (d_1283_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_Some((d_1293_PublicKey_).value), ((d_1287_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_1289_kmsClient_, Wrappers.Option_None()))
        d_1301_valueOrError4_ = out481_
        if not(not((d_1301_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(364,26): " + _dafny.string_of(d_1301_valueOrError4_))
        d_1300_kmsEcdhKeyring_ = (d_1301_valueOrError4_).Extract()
        d_1302_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1303_valueOrError5_: Wrappers.Result = None
        out482_: Wrappers.Result
        out482_ = (d_1283_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_1287_recipientKeypair_).privateKey).pem, (d_1293_PublicKey_).value)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_1303_valueOrError5_ = out482_
        if not(not((d_1303_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(379,28): " + _dafny.string_of(d_1303_valueOrError5_))
        d_1302_recipientKeyring_ = (d_1303_valueOrError5_).Extract()
        d_1304_encryptionContext_: _dafny.Map
        out483_: _dafny.Map
        out483_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1304_encryptionContext_ = out483_
        d_1305_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_1305_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1306_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1306_suite_ = AlgorithmSuites.default__.GetSuite(d_1305_algorithmSuiteId_)
        d_1307_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1308_valueOrError6_: Wrappers.Result = None
        d_1308_valueOrError6_ = (d_1283_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1305_algorithmSuiteId_, d_1304_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1308_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(395,33): " + _dafny.string_of(d_1308_valueOrError6_))
        d_1307_encryptionMaterialsIn_ = (d_1308_valueOrError6_).Extract()
        d_1309_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_1310_valueOrError7_: Wrappers.Result = None
        out484_: Wrappers.Result
        out484_ = (d_1300_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1307_encryptionMaterialsIn_))
        d_1310_valueOrError7_ = out484_
        if not(not((d_1310_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(405,34): " + _dafny.string_of(d_1310_valueOrError7_))
        d_1309_encryptionMaterialsOut_ = (d_1310_valueOrError7_).Extract()
        d_1311___v31_: tuple
        d_1312_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1312_valueOrError8_ = (d_1283_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1309_encryptionMaterialsOut_).materials)
        if not(not((d_1312_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(409,13): " + _dafny.string_of(d_1312_valueOrError8_))
        d_1311___v31_ = (d_1312_valueOrError8_).Extract()
        if not((len(((d_1309_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(411,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1313_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1313_edk_ = (((d_1309_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1314_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1315_valueOrError9_: Wrappers.Result = None
        d_1315_valueOrError9_ = (d_1283_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1305_algorithmSuiteId_, d_1304_encryptionContext_, _dafny.Seq([])))
        if not(not((d_1315_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(414,33): " + _dafny.string_of(d_1315_valueOrError9_))
        d_1314_decryptionMaterialsIn_ = (d_1315_valueOrError9_).Extract()
        d_1316_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_1317_valueOrError10_: Wrappers.Result = None
        out485_: Wrappers.Result
        out485_ = (d_1302_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1314_decryptionMaterialsIn_, _dafny.Seq([d_1313_edk_])))
        d_1317_valueOrError10_ = out485_
        if not(not((d_1317_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(421,34): " + _dafny.string_of(d_1317_valueOrError10_))
        d_1316_decryptionMaterialsOut_ = (d_1317_valueOrError10_).Extract()
        if not((((d_1309_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1316_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(428,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithDerPublicKeys():
        d_1318_mpl_: MaterialProviders.MaterialProvidersClient
        d_1319_valueOrError0_: Wrappers.Result = None
        out486_: Wrappers.Result
        out486_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1319_valueOrError0_ = out486_
        if not(not((d_1319_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(434,15): " + _dafny.string_of(d_1319_valueOrError0_))
        d_1318_mpl_ = (d_1319_valueOrError0_).Extract()
        d_1320_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1321_valueOrError1_: Wrappers.Result = None
        out487_: Wrappers.Result
        out487_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1321_valueOrError1_ = out487_
        if not(not((d_1321_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(436,21): " + _dafny.string_of(d_1321_valueOrError1_))
        d_1320_kmsClient_ = (d_1321_valueOrError1_).Extract()
        hi3_ = len(default__.CURVES)
        for d_1322_i_ in range(0, hi3_):
            d_1323_senderPublicKey_: _dafny.Seq
            d_1324_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1324_valueOrError2_ = Base64.default__.Decode((default__.derKmsSenderPublicKeyStrings)[d_1322_i_])
            if not(not((d_1324_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(440,29): " + _dafny.string_of(d_1324_valueOrError2_))
            d_1323_senderPublicKey_ = (d_1324_valueOrError2_).Extract()
            d_1325_recipientPublicKey_: _dafny.Seq
            d_1326_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1326_valueOrError3_ = Base64.default__.Decode((default__.derKmsRecipientPublicKeyStrings)[d_1322_i_])
            if not(not((d_1326_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(441,32): " + _dafny.string_of(d_1326_valueOrError3_))
            d_1325_recipientPublicKey_ = (d_1326_valueOrError3_).Extract()
            d_1327_senderKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1328_valueOrError4_: Wrappers.Result = None
            out488_: Wrappers.Result
            out488_ = (d_1318_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((default__.senderKmsKeys)[d_1322_i_], Wrappers.Option_Some(d_1323_senderPublicKey_), d_1325_recipientPublicKey_)), (default__.CURVES)[d_1322_i_], d_1320_kmsClient_, Wrappers.Option_None()))
            d_1328_valueOrError4_ = out488_
            if not(not((d_1328_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(443,34): " + _dafny.string_of(d_1328_valueOrError4_))
            d_1327_senderKmsEcdhKeyring_ = (d_1328_valueOrError4_).Extract()
            d_1329_recipientKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1330_valueOrError5_: Wrappers.Result = None
            out489_: Wrappers.Result
            out489_ = (d_1318_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((default__.recipientKmsKeys)[d_1322_i_], Wrappers.Option_Some(d_1325_recipientPublicKey_), d_1323_senderPublicKey_)), (default__.CURVES)[d_1322_i_], d_1320_kmsClient_, Wrappers.Option_None()))
            d_1330_valueOrError5_ = out489_
            if not(not((d_1330_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(458,37): " + _dafny.string_of(d_1330_valueOrError5_))
            d_1329_recipientKmsEcdhKeyring_ = (d_1330_valueOrError5_).Extract()
            d_1331_encryptionContext_: _dafny.Map
            out490_: _dafny.Map
            out490_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_1331_encryptionContext_ = out490_
            d_1332_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_1332_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_1333_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_1333_suite_ = AlgorithmSuites.default__.GetSuite(d_1332_algorithmSuiteId_)
            d_1334_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1335_valueOrError6_: Wrappers.Result = None
            d_1335_valueOrError6_ = (d_1318_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1332_algorithmSuiteId_, d_1331_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_1335_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(477,35): " + _dafny.string_of(d_1335_valueOrError6_))
            d_1334_encryptionMaterialsIn_ = (d_1335_valueOrError6_).Extract()
            d_1336_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_1337_valueOrError7_: Wrappers.Result = None
            out491_: Wrappers.Result
            out491_ = (d_1327_senderKmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1334_encryptionMaterialsIn_))
            d_1337_valueOrError7_ = out491_
            if not(not((d_1337_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(487,36): " + _dafny.string_of(d_1337_valueOrError7_))
            d_1336_encryptionMaterialsOut_ = (d_1337_valueOrError7_).Extract()
            d_1338___v32_: tuple
            d_1339_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1339_valueOrError8_ = (d_1318_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1336_encryptionMaterialsOut_).materials)
            if not(not((d_1339_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(491,15): " + _dafny.string_of(d_1339_valueOrError8_))
            d_1338___v32_ = (d_1339_valueOrError8_).Extract()
            if not((len(((d_1336_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(493,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1340_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_1340_edk_ = (((d_1336_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_1341_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_1342_valueOrError9_: Wrappers.Result = None
            d_1342_valueOrError9_ = (d_1318_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1332_algorithmSuiteId_, d_1331_encryptionContext_, _dafny.Seq([])))
            if not(not((d_1342_valueOrError9_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(496,35): " + _dafny.string_of(d_1342_valueOrError9_))
            d_1341_decryptionMaterialsIn_ = (d_1342_valueOrError9_).Extract()
            d_1343_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_1344_valueOrError10_: Wrappers.Result = None
            out492_: Wrappers.Result
            out492_ = (d_1329_recipientKmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1341_decryptionMaterialsIn_, _dafny.Seq([d_1340_edk_])))
            d_1344_valueOrError10_ = out492_
            if not(not((d_1344_valueOrError10_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(503,36): " + _dafny.string_of(d_1344_valueOrError10_))
            d_1343_decryptionMaterialsOut_ = (d_1344_valueOrError10_).Extract()
            if not((((d_1336_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1343_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(510,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhRawEcdhKeyringWithDerPublicKeys():
        d_1345_mpl_: MaterialProviders.MaterialProvidersClient
        d_1346_valueOrError0_: Wrappers.Result = None
        out493_: Wrappers.Result
        out493_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1346_valueOrError0_ = out493_
        if not(not((d_1346_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(518,15): " + _dafny.string_of(d_1346_valueOrError0_))
        d_1345_mpl_ = (d_1346_valueOrError0_).Extract()
        d_1347_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1348_valueOrError1_: Wrappers.Result = None
        out494_: Wrappers.Result
        out494_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1348_valueOrError1_ = out494_
        if not(not((d_1348_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(520,21): " + _dafny.string_of(d_1348_valueOrError1_))
        d_1347_kmsClient_ = (d_1348_valueOrError1_).Extract()
        hi4_ = len(default__.CURVES)
        for d_1349_i_ in range(0, hi4_):
            d_1350_senderKmsKey_: _dafny.Seq
            d_1350_senderKmsKey_ = (default__.senderKmsKeys)[d_1349_i_]
            d_1351_senderPublicKey_: _dafny.Seq
            d_1352_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1352_valueOrError2_ = Base64.default__.Decode((default__.derKmsSenderPublicKeyStrings)[d_1349_i_])
            if not(not((d_1352_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(525,29): " + _dafny.string_of(d_1352_valueOrError2_))
            d_1351_senderPublicKey_ = (d_1352_valueOrError2_).Extract()
            d_1353_recipientPrivateKey_: _dafny.Seq
            d_1354_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_1354_valueOrError3_ = UTF8.default__.Encode((default__.rawEccPrivateKeys)[d_1349_i_])
            if not(not((d_1354_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(526,33): " + _dafny.string_of(d_1354_valueOrError3_))
            d_1353_recipientPrivateKey_ = (d_1354_valueOrError3_).Extract()
            d_1355_recipientPublicKey_: _dafny.Seq
            d_1356_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1356_valueOrError4_ = Base64.default__.Decode((default__.rawEccPublicKeysB64der)[d_1349_i_])
            if not(not((d_1356_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(527,32): " + _dafny.string_of(d_1356_valueOrError4_))
            d_1355_recipientPublicKey_ = (d_1356_valueOrError4_).Extract()
            d_1357_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_1357_curve_ = (default__.CURVES)[d_1349_i_]
            d_1358_senderKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1359_valueOrError5_: Wrappers.Result = None
            out495_: Wrappers.Result
            out495_ = (d_1345_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1350_senderKmsKey_, Wrappers.Option_Some(d_1351_senderPublicKey_), d_1355_recipientPublicKey_)), d_1357_curve_, d_1347_kmsClient_, Wrappers.Option_None()))
            d_1359_valueOrError5_ = out495_
            if not(not((d_1359_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(530,34): " + _dafny.string_of(d_1359_valueOrError5_))
            d_1358_senderKmsEcdhKeyring_ = (d_1359_valueOrError5_).Extract()
            d_1360_recipientRawKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_1361_valueOrError6_: Wrappers.Result = None
            out496_: Wrappers.Result
            out496_ = (d_1345_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_1353_recipientPrivateKey_, d_1351_senderPublicKey_)), d_1357_curve_))
            d_1361_valueOrError6_ = out496_
            if not(not((d_1361_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(545,33): " + _dafny.string_of(d_1361_valueOrError6_))
            d_1360_recipientRawKeyring_ = (d_1361_valueOrError6_).Extract()
            d_1362_encryptionContext_: _dafny.Map
            out497_: _dafny.Map
            out497_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_1362_encryptionContext_ = out497_
            d_1363_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_1363_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_1364_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_1364_suite_ = AlgorithmSuites.default__.GetSuite(d_1363_algorithmSuiteId_)
            d_1365_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1366_valueOrError7_: Wrappers.Result = None
            d_1366_valueOrError7_ = (d_1345_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1363_algorithmSuiteId_, d_1362_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_1366_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(561,35): " + _dafny.string_of(d_1366_valueOrError7_))
            d_1365_encryptionMaterialsIn_ = (d_1366_valueOrError7_).Extract()
            d_1367_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_1368_valueOrError8_: Wrappers.Result = None
            out498_: Wrappers.Result
            out498_ = (d_1358_senderKmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1365_encryptionMaterialsIn_))
            d_1368_valueOrError8_ = out498_
            if not(not((d_1368_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(571,36): " + _dafny.string_of(d_1368_valueOrError8_))
            d_1367_encryptionMaterialsOut_ = (d_1368_valueOrError8_).Extract()
            d_1369___v33_: tuple
            d_1370_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1370_valueOrError9_ = (d_1345_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1367_encryptionMaterialsOut_).materials)
            if not(not((d_1370_valueOrError9_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(575,15): " + _dafny.string_of(d_1370_valueOrError9_))
            d_1369___v33_ = (d_1370_valueOrError9_).Extract()
            if not((len(((d_1367_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(577,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_1371_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_1371_edk_ = (((d_1367_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_1372_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_1373_valueOrError10_: Wrappers.Result = None
            d_1373_valueOrError10_ = (d_1345_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_1363_algorithmSuiteId_, d_1362_encryptionContext_, _dafny.Seq([])))
            if not(not((d_1373_valueOrError10_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(580,35): " + _dafny.string_of(d_1373_valueOrError10_))
            d_1372_decryptionMaterialsIn_ = (d_1373_valueOrError10_).Extract()
            d_1374_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_1375_valueOrError11_: Wrappers.Result = None
            out499_: Wrappers.Result
            out499_ = (d_1360_recipientRawKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1372_decryptionMaterialsIn_, _dafny.Seq([d_1371_edk_])))
            d_1375_valueOrError11_ = out499_
            if not(not((d_1375_valueOrError11_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(587,36): " + _dafny.string_of(d_1375_valueOrError11_))
            d_1374_decryptionMaterialsOut_ = (d_1375_valueOrError11_).Extract()
            if not((((d_1367_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1374_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(594,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure():
        d_1376_mpl_: MaterialProviders.MaterialProvidersClient
        d_1377_valueOrError0_: Wrappers.Result = None
        out500_: Wrappers.Result
        out500_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1377_valueOrError0_ = out500_
        if not(not((d_1377_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(603,15): " + _dafny.string_of(d_1377_valueOrError0_))
        d_1376_mpl_ = (d_1377_valueOrError0_).Extract()
        d_1378_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1379_valueOrError1_: Wrappers.Result = None
        out501_: Wrappers.Result
        out501_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1379_valueOrError1_ = out501_
        if not(not((d_1379_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(605,21): " + _dafny.string_of(d_1379_valueOrError1_))
        d_1378_kmsClient_ = (d_1379_valueOrError1_).Extract()
        d_1380_senderPublicKey_: _dafny.Seq
        d_1381_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1381_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_1381_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(607,27): " + _dafny.string_of(d_1381_valueOrError2_))
        d_1380_senderPublicKey_ = (d_1381_valueOrError2_).Extract()
        d_1382_recipientPublicKey_: _dafny.Seq
        d_1383_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1383_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__R)
        if not(not((d_1383_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(608,30): " + _dafny.string_of(d_1383_valueOrError3_))
        d_1382_recipientPublicKey_ = (d_1383_valueOrError3_).Extract()
        d_1384_senderKmsEcdhKeyring_: Wrappers.Result
        out502_: Wrappers.Result
        out502_ = (d_1376_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_Some(d_1380_senderPublicKey_), d_1382_recipientPublicKey_)), default__.P384, d_1378_kmsClient_, Wrappers.Option_None()))
        d_1384_senderKmsEcdhKeyring_ = out502_
        if not((d_1384_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(625,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure():
        d_1385_mpl_: MaterialProviders.MaterialProvidersClient
        d_1386_valueOrError0_: Wrappers.Result = None
        out503_: Wrappers.Result
        out503_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1386_valueOrError0_ = out503_
        if not(not((d_1386_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(630,15): " + _dafny.string_of(d_1386_valueOrError0_))
        d_1385_mpl_ = (d_1386_valueOrError0_).Extract()
        d_1387_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1388_valueOrError1_: Wrappers.Result = None
        out504_: Wrappers.Result
        out504_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1388_valueOrError1_ = out504_
        if not(not((d_1388_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(632,21): " + _dafny.string_of(d_1388_valueOrError1_))
        d_1387_kmsClient_ = (d_1388_valueOrError1_).Extract()
        d_1389_senderKmsKey256_: _dafny.Seq
        d_1389_senderKmsKey256_ = TestUtils.default__.KMS__ECC__256__KEY__ARN__S
        d_1390_senderPublicKey256_: _dafny.Seq
        d_1391_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1391_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_1391_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(635,33): " + _dafny.string_of(d_1391_valueOrError2_))
        d_1390_senderPublicKey256_ = (d_1391_valueOrError2_).Extract()
        d_1392_recipientPublicKey256_: _dafny.Seq
        d_1393_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1393_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_1393_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(636,33): " + _dafny.string_of(d_1393_valueOrError3_))
        d_1392_recipientPublicKey256_ = (d_1393_valueOrError3_).Extract()
        d_1394_senderKmsKey384_: _dafny.Seq
        d_1394_senderKmsKey384_ = TestUtils.default__.KMS__ECC__384__KEY__ARN__S
        d_1395_senderPublicKey384_: _dafny.Seq
        d_1396_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1396_valueOrError4_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S)
        if not(not((d_1396_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(639,33): " + _dafny.string_of(d_1396_valueOrError4_))
        d_1395_senderPublicKey384_ = (d_1396_valueOrError4_).Extract()
        d_1397_recipientPublicKey384_: _dafny.Seq
        d_1398_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1398_valueOrError5_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_1398_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(640,33): " + _dafny.string_of(d_1398_valueOrError5_))
        d_1397_recipientPublicKey384_ = (d_1398_valueOrError5_).Extract()
        d_1399_senderKmsKey521_: _dafny.Seq
        d_1399_senderKmsKey521_ = TestUtils.default__.KMS__ECC__521__KEY__ARN__S
        d_1400_senderPublicKey521_: _dafny.Seq
        d_1401_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1401_valueOrError6_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S)
        if not(not((d_1401_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(643,33): " + _dafny.string_of(d_1401_valueOrError6_))
        d_1400_senderPublicKey521_ = (d_1401_valueOrError6_).Extract()
        d_1402_recipientPublicKey521_: _dafny.Seq
        d_1403_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1403_valueOrError7_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_1403_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(644,33): " + _dafny.string_of(d_1403_valueOrError7_))
        d_1402_recipientPublicKey521_ = (d_1403_valueOrError7_).Extract()
        d_1404_senderKmsEcdhKeyring_: Wrappers.Result
        out505_: Wrappers.Result
        out505_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1392_recipientPublicKey256_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out505_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(662,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out506_: Wrappers.Result
        out506_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1392_recipientPublicKey256_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out506_
        out507_: Wrappers.Result
        out507_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1397_recipientPublicKey384_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out507_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(694,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out508_: Wrappers.Result
        out508_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1397_recipientPublicKey384_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out508_
        out509_: Wrappers.Result
        out509_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1402_recipientPublicKey521_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out509_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(726,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out510_: Wrappers.Result
        out510_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1402_recipientPublicKey521_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out510_
        out511_: Wrappers.Result
        out511_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1397_recipientPublicKey384_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out511_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(759,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out512_: Wrappers.Result
        out512_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1402_recipientPublicKey521_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out512_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(775,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out513_: Wrappers.Result
        out513_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1392_recipientPublicKey256_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out513_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(792,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out514_: Wrappers.Result
        out514_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1402_recipientPublicKey521_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out514_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(808,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out515_: Wrappers.Result
        out515_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1392_recipientPublicKey256_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out515_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(825,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out516_: Wrappers.Result
        out516_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1397_recipientPublicKey384_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out516_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(841,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out517_: Wrappers.Result
        out517_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1392_recipientPublicKey256_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out517_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(860,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out518_: Wrappers.Result
        out518_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1392_recipientPublicKey256_)), default__.P256, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out518_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(876,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out519_: Wrappers.Result
        out519_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1397_recipientPublicKey384_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out519_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(893,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out520_: Wrappers.Result
        out520_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1399_senderKmsKey521_, Wrappers.Option_Some(d_1400_senderPublicKey521_), d_1397_recipientPublicKey384_)), default__.P384, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out520_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(909,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out521_: Wrappers.Result
        out521_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1389_senderKmsKey256_, Wrappers.Option_Some(d_1390_senderPublicKey256_), d_1402_recipientPublicKey521_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out521_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(926,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out522_: Wrappers.Result
        out522_ = (d_1385_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1394_senderKmsKey384_, Wrappers.Option_Some(d_1395_senderPublicKey384_), d_1402_recipientPublicKey521_)), default__.P521, d_1387_kmsClient_, Wrappers.Option_None()))
        d_1404_senderKmsEcdhKeyring_ = out522_
        if not((d_1404_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(942,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestLyingKmsKey():
        d_1405_senderKmsKey256_: _dafny.Seq
        d_1405_senderKmsKey256_ = TestUtils.default__.KMS__ECC__256__KEY__ARN__S
        d_1406_senderPublicKey256_: _dafny.Seq
        d_1407_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1407_valueOrError0_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_1407_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(948,33): " + _dafny.string_of(d_1407_valueOrError0_))
        d_1406_senderPublicKey256_ = (d_1407_valueOrError0_).Extract()
        d_1408_recipientPublicKey256_: _dafny.Seq
        d_1409_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1409_valueOrError1_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_1409_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(949,33): " + _dafny.string_of(d_1409_valueOrError1_))
        d_1408_recipientPublicKey256_ = (d_1409_valueOrError1_).Extract()
        d_1410_senderKmsKey384_: _dafny.Seq
        d_1410_senderKmsKey384_ = TestUtils.default__.KMS__ECC__384__KEY__ARN__S
        d_1411_senderPublicKey384_: _dafny.Seq
        d_1412_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1412_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S)
        if not(not((d_1412_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(952,33): " + _dafny.string_of(d_1412_valueOrError2_))
        d_1411_senderPublicKey384_ = (d_1412_valueOrError2_).Extract()
        d_1413_recipientPublicKey384_: _dafny.Seq
        d_1414_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1414_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_1414_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(953,33): " + _dafny.string_of(d_1414_valueOrError3_))
        d_1413_recipientPublicKey384_ = (d_1414_valueOrError3_).Extract()
        d_1415_senderKmsKey521_: _dafny.Seq
        d_1415_senderKmsKey521_ = TestUtils.default__.KMS__ECC__521__KEY__ARN__S
        d_1416_senderPublicKey521_: _dafny.Seq
        d_1417_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1417_valueOrError4_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S)
        if not(not((d_1417_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(956,33): " + _dafny.string_of(d_1417_valueOrError4_))
        d_1416_senderPublicKey521_ = (d_1417_valueOrError4_).Extract()
        d_1418_recipientPublicKey521_: _dafny.Seq
        d_1419_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1419_valueOrError5_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_1419_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(957,33): " + _dafny.string_of(d_1419_valueOrError5_))
        d_1418_recipientPublicKey521_ = (d_1419_valueOrError5_).Extract()
        d_1420_mpl_: MaterialProviders.MaterialProvidersClient
        d_1421_valueOrError6_: Wrappers.Result = None
        out523_: Wrappers.Result
        out523_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1421_valueOrError6_ = out523_
        if not(not((d_1421_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(959,15): " + _dafny.string_of(d_1421_valueOrError6_))
        d_1420_mpl_ = (d_1421_valueOrError6_).Extract()
        d_1422_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1423_valueOrError7_: Wrappers.Result = None
        out524_: Wrappers.Result
        out524_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1423_valueOrError7_ = out524_
        if not(not((d_1423_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(961,21): " + _dafny.string_of(d_1423_valueOrError7_))
        d_1422_kmsClient_ = (d_1423_valueOrError7_).Extract()
        d_1424_encryptionContext_: _dafny.Map
        out525_: _dafny.Map
        out525_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1424_encryptionContext_ = out525_
        d_1425_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_1425_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_1426_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1426_suite_ = AlgorithmSuites.default__.GetSuite(d_1425_algorithmSuiteId_)
        d_1427_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1428_valueOrError8_: Wrappers.Result = None
        d_1428_valueOrError8_ = (d_1420_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_1425_algorithmSuiteId_, d_1424_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1428_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(967,33): " + _dafny.string_of(d_1428_valueOrError8_))
        d_1427_encryptionMaterialsIn_ = (d_1428_valueOrError8_).Extract()
        d_1429_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1430_valueOrError9_: Wrappers.Result = None
        out526_: Wrappers.Result
        out526_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1410_senderKmsKey384_, Wrappers.Option_Some(d_1406_senderPublicKey256_), d_1408_recipientPublicKey256_)), default__.P256, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1430_valueOrError9_ = out526_
        if not(not((d_1430_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(985,26): " + _dafny.string_of(d_1430_valueOrError9_))
        d_1429_kmsEcdhKeyring_ = (d_1430_valueOrError9_).Extract()
        d_1431_encryptionMaterialsOut_: Wrappers.Result
        out527_: Wrappers.Result
        out527_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out527_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1002,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1432_valueOrError10_: Wrappers.Result = None
        out528_: Wrappers.Result
        out528_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1415_senderKmsKey521_, Wrappers.Option_Some(d_1406_senderPublicKey256_), d_1408_recipientPublicKey256_)), default__.P256, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1432_valueOrError10_ = out528_
        if not(not((d_1432_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1004,22): " + _dafny.string_of(d_1432_valueOrError10_))
        d_1429_kmsEcdhKeyring_ = (d_1432_valueOrError10_).Extract()
        out529_: Wrappers.Result
        out529_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out529_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1021,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1433_valueOrError11_: Wrappers.Result = None
        out530_: Wrappers.Result
        out530_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1405_senderKmsKey256_, Wrappers.Option_Some(d_1411_senderPublicKey384_), d_1413_recipientPublicKey384_)), default__.P384, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1433_valueOrError11_ = out530_
        if not(not((d_1433_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1024,22): " + _dafny.string_of(d_1433_valueOrError11_))
        d_1429_kmsEcdhKeyring_ = (d_1433_valueOrError11_).Extract()
        out531_: Wrappers.Result
        out531_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out531_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1041,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1434_valueOrError12_: Wrappers.Result = None
        out532_: Wrappers.Result
        out532_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1415_senderKmsKey521_, Wrappers.Option_Some(d_1411_senderPublicKey384_), d_1413_recipientPublicKey384_)), default__.P384, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1434_valueOrError12_ = out532_
        if not(not((d_1434_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1043,22): " + _dafny.string_of(d_1434_valueOrError12_))
        d_1429_kmsEcdhKeyring_ = (d_1434_valueOrError12_).Extract()
        out533_: Wrappers.Result
        out533_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out533_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1060,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1435_valueOrError13_: Wrappers.Result = None
        out534_: Wrappers.Result
        out534_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1405_senderKmsKey256_, Wrappers.Option_Some(d_1416_senderPublicKey521_), d_1418_recipientPublicKey521_)), default__.P521, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1435_valueOrError13_ = out534_
        if not(not((d_1435_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1063,22): " + _dafny.string_of(d_1435_valueOrError13_))
        d_1429_kmsEcdhKeyring_ = (d_1435_valueOrError13_).Extract()
        out535_: Wrappers.Result
        out535_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out535_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1080,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1436_valueOrError14_: Wrappers.Result = None
        out536_: Wrappers.Result
        out536_ = (d_1420_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_1410_senderKmsKey384_, Wrappers.Option_Some(d_1416_senderPublicKey521_), d_1418_recipientPublicKey521_)), default__.P521, d_1422_kmsClient_, Wrappers.Option_None()))
        d_1436_valueOrError14_ = out536_
        if not(not((d_1436_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1082,22): " + _dafny.string_of(d_1436_valueOrError14_))
        d_1429_kmsEcdhKeyring_ = (d_1436_valueOrError14_).Extract()
        out537_: Wrappers.Result
        out537_ = (d_1429_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_1427_encryptionMaterialsIn_))
        d_1431_encryptionMaterialsOut_ = out537_
        if not((d_1431_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1099,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()
    @_dafny.classproperty
    def P384(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384()
    @_dafny.classproperty
    def P521(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()
    @_dafny.classproperty
    def CURVES(instance):
        return _dafny.Seq([default__.P256, default__.P384, default__.P521])
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
    @_dafny.classproperty
    def derKmsSenderPublicKeyStrings(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S])
    @_dafny.classproperty
    def derKmsRecipientPublicKeyStrings(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__R, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__R, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__R])
    @_dafny.classproperty
    def senderKmsKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
    @_dafny.classproperty
    def recipientKmsKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
    @_dafny.classproperty
    def rawEccPrivateKeys(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PRIVATE, TestUtils.default__.ECC__P384__PRIVATE, TestUtils.default__.ECC__P521__PRIVATE])
    @_dafny.classproperty
    def rawEccPublicKeysB64der(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PUBLIC, TestUtils.default__.ECC__P384__PUBLIC, TestUtils.default__.ECC__P521__PUBLIC])
