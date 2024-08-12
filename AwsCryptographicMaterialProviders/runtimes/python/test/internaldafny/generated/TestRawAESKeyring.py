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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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

# Module: TestRawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_690_mpl_: MaterialProviders.MaterialProvidersClient
        d_691_valueOrError0_: Wrappers.Result = None
        out252_: Wrappers.Result
        out252_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_691_valueOrError0_ = out252_
        if not(not((d_691_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(20,15): " + _dafny.string_of(d_691_valueOrError0_))
        d_690_mpl_ = (d_691_valueOrError0_).Extract()
        d_692_namespace_: _dafny.Seq
        d_693_name_: _dafny.Seq
        out253_: _dafny.Seq
        out254_: _dafny.Seq
        out253_, out254_ = TestUtils.default__.NamespaceAndName(0)
        d_692_namespace_ = out253_
        d_693_name_ = out254_
        d_694_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_695_valueOrError1_: Wrappers.Result = None
        out255_: Wrappers.Result
        out255_ = (d_690_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_692_namespace_, d_693_name_, _dafny.Seq([0 for d_696_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_695_valueOrError1_ = out255_
        if not(not((d_695_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(23,25): " + _dafny.string_of(d_695_valueOrError1_))
        d_694_rawAESKeyring_ = (d_695_valueOrError1_).Extract()
        d_697_encryptionContext_: _dafny.Map
        out256_: _dafny.Map
        out256_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_697_encryptionContext_ = out256_
        d_698_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_698_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_699_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_700_valueOrError2_: Wrappers.Result = None
        d_700_valueOrError2_ = (d_690_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_698_algorithmSuiteId_, d_697_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_700_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(32,33): " + _dafny.string_of(d_700_valueOrError2_))
        d_699_encryptionMaterialsIn_ = (d_700_valueOrError2_).Extract()
        d_701_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_702_valueOrError3_: Wrappers.Result = None
        out257_: Wrappers.Result
        out257_ = (d_694_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_699_encryptionMaterialsIn_))
        d_702_valueOrError3_ = out257_
        if not(not((d_702_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(42,34): " + _dafny.string_of(d_702_valueOrError3_))
        d_701_encryptionMaterialsOut_ = (d_702_valueOrError3_).Extract()
        d_703___v0_: tuple
        d_704_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_704_valueOrError4_ = (d_690_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_701_encryptionMaterialsOut_).materials)
        if not(not((d_704_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(57,13): " + _dafny.string_of(d_704_valueOrError4_))
        d_703___v0_ = (d_704_valueOrError4_).Extract()
        if not((len(((d_701_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_705_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_705_edk_ = (((d_701_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_706_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_707_valueOrError5_: Wrappers.Result = None
        d_707_valueOrError5_ = (d_690_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_698_algorithmSuiteId_, d_697_encryptionContext_, _dafny.Seq([])))
        if not(not((d_707_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(68,33): " + _dafny.string_of(d_707_valueOrError5_))
        d_706_decryptionMaterialsIn_ = (d_707_valueOrError5_).Extract()
        d_708_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_709_valueOrError6_: Wrappers.Result = None
        out258_: Wrappers.Result
        out258_ = (d_694_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_706_decryptionMaterialsIn_, _dafny.Seq([d_705_edk_])))
        d_709_valueOrError6_ = out258_
        if not(not((d_709_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(75,34): " + _dafny.string_of(d_709_valueOrError6_))
        d_708_decryptionMaterialsOut_ = (d_709_valueOrError6_).Extract()
        if not((((d_701_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_701_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_710_mpl_: MaterialProviders.MaterialProvidersClient
        d_711_valueOrError0_: Wrappers.Result = None
        out259_: Wrappers.Result
        out259_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_711_valueOrError0_ = out259_
        if not(not((d_711_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(93,15): " + _dafny.string_of(d_711_valueOrError0_))
        d_710_mpl_ = (d_711_valueOrError0_).Extract()
        d_712_namespace_: _dafny.Seq
        d_713_name_: _dafny.Seq
        out260_: _dafny.Seq
        out261_: _dafny.Seq
        out260_, out261_ = TestUtils.default__.NamespaceAndName(0)
        d_712_namespace_ = out260_
        d_713_name_ = out261_
        d_714_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_715_valueOrError1_: Wrappers.Result = None
        out262_: Wrappers.Result
        out262_ = (d_710_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_712_namespace_, d_713_name_, _dafny.Seq([0 for d_716_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_715_valueOrError1_ = out262_
        if not(not((d_715_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(96,25): " + _dafny.string_of(d_715_valueOrError1_))
        d_714_rawAESKeyring_ = (d_715_valueOrError1_).Extract()
        d_717_encryptionContext_: _dafny.Map
        out263_: _dafny.Map
        out263_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_717_encryptionContext_ = out263_
        d_718_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_718_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_719_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_720_valueOrError2_: Wrappers.Result = None
        d_720_valueOrError2_ = (d_710_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_718_algorithmSuiteId_, d_717_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_720_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(105,33): " + _dafny.string_of(d_720_valueOrError2_))
        d_719_encryptionMaterialsIn_ = (d_720_valueOrError2_).Extract()
        d_721_pdk_: _dafny.Seq
        d_721_pdk_ = _dafny.Seq([0 for d_722_i_ in range(32)])
        d_723_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_724_valueOrError3_: Wrappers.Result = None
        pat_let_tv1_ = d_721_pdk_
        out264_: Wrappers.Result
        def iife24_(_pat_let10_0):
            def iife25_(d_725_dt__update__tmp_h0_):
                def iife26_(_pat_let11_0):
                    def iife27_(d_726_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_725_dt__update__tmp_h0_).algorithmSuite, (d_725_dt__update__tmp_h0_).encryptionContext, (d_725_dt__update__tmp_h0_).encryptedDataKeys, (d_725_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_726_dt__update_hplaintextDataKey_h0_, (d_725_dt__update__tmp_h0_).signingKey, (d_725_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife27_(_pat_let11_0)
                return iife26_(Wrappers.Option_Some(pat_let_tv1_))
            return iife25_(_pat_let10_0)
        out264_ = (d_714_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(iife24_(d_719_encryptionMaterialsIn_)))
        d_724_valueOrError3_ = out264_
        if not(not((d_724_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(120,34): " + _dafny.string_of(d_724_valueOrError3_))
        d_723_encryptionMaterialsOut_ = (d_724_valueOrError3_).Extract()
        d_727___v1_: tuple
        d_728_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_728_valueOrError4_ = (d_710_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_723_encryptionMaterialsOut_).materials)
        if not(not((d_728_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(124,13): " + _dafny.string_of(d_728_valueOrError4_))
        d_727___v1_ = (d_728_valueOrError4_).Extract()
        d_729_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_729_edk_ = (((d_723_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_730_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_731_valueOrError5_: Wrappers.Result = None
        d_731_valueOrError5_ = (d_710_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_718_algorithmSuiteId_, d_717_encryptionContext_, _dafny.Seq([])))
        if not(not((d_731_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(128,33): " + _dafny.string_of(d_731_valueOrError5_))
        d_730_decryptionMaterialsIn_ = (d_731_valueOrError5_).Extract()
        d_732_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_733_valueOrError6_: Wrappers.Result = None
        out265_: Wrappers.Result
        out265_ = (d_714_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_730_decryptionMaterialsIn_, _dafny.Seq([d_729_edk_])))
        d_733_valueOrError6_ = out265_
        if not(not((d_733_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(136,34): " + _dafny.string_of(d_733_valueOrError6_))
        d_732_decryptionMaterialsOut_ = (d_733_valueOrError6_).Extract()
        if not((((d_732_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_721_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_734_mpl_: MaterialProviders.MaterialProvidersClient
        d_735_valueOrError0_: Wrappers.Result = None
        out266_: Wrappers.Result
        out266_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_735_valueOrError0_ = out266_
        if not(not((d_735_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(154,15): " + _dafny.string_of(d_735_valueOrError0_))
        d_734_mpl_ = (d_735_valueOrError0_).Extract()
        d_736_namespace_: _dafny.Seq
        d_737_name_: _dafny.Seq
        out267_: _dafny.Seq
        out268_: _dafny.Seq
        out267_, out268_ = TestUtils.default__.NamespaceAndName(0)
        d_736_namespace_ = out267_
        d_737_name_ = out268_
        d_738_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_739_valueOrError1_: Wrappers.Result = None
        out269_: Wrappers.Result
        out269_ = (d_734_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_736_namespace_, d_737_name_, _dafny.Seq([0 for d_740_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_739_valueOrError1_ = out269_
        if not(not((d_739_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(157,25): " + _dafny.string_of(d_739_valueOrError1_))
        d_738_rawAESKeyring_ = (d_739_valueOrError1_).Extract()
        d_741_mismatchedAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_742_valueOrError2_: Wrappers.Result = None
        out270_: Wrappers.Result
        out270_ = (d_734_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_736_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_743_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_742_valueOrError2_ = out270_
        if not(not((d_742_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(164,32): " + _dafny.string_of(d_742_valueOrError2_))
        d_741_mismatchedAESKeyring_ = (d_742_valueOrError2_).Extract()
        d_744_encryptionContext_: _dafny.Map
        out271_: _dafny.Map
        out271_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_744_encryptionContext_ = out271_
        d_745_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_745_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_746_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_747_valueOrError3_: Wrappers.Result = None
        d_747_valueOrError3_ = (d_734_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_745_algorithmSuiteId_, d_744_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_747_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(174,33): " + _dafny.string_of(d_747_valueOrError3_))
        d_746_encryptionMaterialsIn_ = (d_747_valueOrError3_).Extract()
        d_748_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_749_valueOrError4_: Wrappers.Result = None
        out272_: Wrappers.Result
        out272_ = (d_738_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_746_encryptionMaterialsIn_))
        d_749_valueOrError4_ = out272_
        if not(not((d_749_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(184,34): " + _dafny.string_of(d_749_valueOrError4_))
        d_748_encryptionMaterialsOut_ = (d_749_valueOrError4_).Extract()
        d_750___v2_: tuple
        d_751_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_751_valueOrError5_ = (d_734_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_748_encryptionMaterialsOut_).materials)
        if not(not((d_751_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(188,13): " + _dafny.string_of(d_751_valueOrError5_))
        d_750___v2_ = (d_751_valueOrError5_).Extract()
        d_752_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_752_edk_ = (((d_748_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_753_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_754_valueOrError6_: Wrappers.Result = None
        d_754_valueOrError6_ = (d_734_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_745_algorithmSuiteId_, d_744_encryptionContext_, _dafny.Seq([])))
        if not(not((d_754_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(192,33): " + _dafny.string_of(d_754_valueOrError6_))
        d_753_decryptionMaterialsIn_ = (d_754_valueOrError6_).Extract()
        d_755_decryptionMaterialsOut_: Wrappers.Result
        out273_: Wrappers.Result
        out273_ = (d_741_mismatchedAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_753_decryptionMaterialsIn_, _dafny.Seq([d_752_edk_])))
        d_755_decryptionMaterialsOut_ = out273_
        if not((d_755_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(205,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_755_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_755_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_755_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(208,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_755_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("AESKeyring"), d_736_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(209,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_756_mpl_: MaterialProviders.MaterialProvidersClient
        d_757_valueOrError0_: Wrappers.Result = None
        out274_: Wrappers.Result
        out274_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_757_valueOrError0_ = out274_
        if not(not((d_757_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,15): " + _dafny.string_of(d_757_valueOrError0_))
        d_756_mpl_ = (d_757_valueOrError0_).Extract()
        d_758_namespace_: _dafny.Seq
        d_759_name_: _dafny.Seq
        out275_: _dafny.Seq
        out276_: _dafny.Seq
        out275_, out276_ = TestUtils.default__.NamespaceAndName(0)
        d_758_namespace_ = out275_
        d_759_name_ = out276_
        d_760_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_761_valueOrError1_: Wrappers.Result = None
        out277_: Wrappers.Result
        out277_ = (d_756_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_758_namespace_, d_759_name_, _dafny.Seq([0 for d_762_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_761_valueOrError1_ = out277_
        if not(not((d_761_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(218,25): " + _dafny.string_of(d_761_valueOrError1_))
        d_760_rawAESKeyring_ = (d_761_valueOrError1_).Extract()
        d_763_encryptionContext_: _dafny.Map
        out278_: _dafny.Map
        out278_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_763_encryptionContext_ = out278_
        d_764_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_764_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_765_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_766_valueOrError2_: Wrappers.Result = None
        d_766_valueOrError2_ = (d_756_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_764_algorithmSuiteId_, d_763_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_766_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(227,33): " + _dafny.string_of(d_766_valueOrError2_))
        d_765_encryptionMaterialsIn_ = (d_766_valueOrError2_).Extract()
        d_767_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_768_valueOrError3_: Wrappers.Result = None
        out279_: Wrappers.Result
        out279_ = (d_760_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_765_encryptionMaterialsIn_))
        d_768_valueOrError3_ = out279_
        if not(not((d_768_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(237,34): " + _dafny.string_of(d_768_valueOrError3_))
        d_767_encryptionMaterialsOut_ = (d_768_valueOrError3_).Extract()
        d_769___v3_: tuple
        d_770_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_770_valueOrError4_ = (d_756_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_767_encryptionMaterialsOut_).materials)
        if not(not((d_770_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(241,13): " + _dafny.string_of(d_770_valueOrError4_))
        d_769___v3_ = (d_770_valueOrError4_).Extract()
        d_771_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_771_edk_ = (((d_767_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_772_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_773_valueOrError5_: Wrappers.Result = None
        d_773_valueOrError5_ = (d_756_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_764_algorithmSuiteId_, d_763_encryptionContext_, _dafny.Seq([])))
        if not(not((d_773_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(245,33): " + _dafny.string_of(d_773_valueOrError5_))
        d_772_decryptionMaterialsIn_ = (d_773_valueOrError5_).Extract()
        d_774_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_774_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_771_edk_).keyProviderId, (d_771_edk_).keyProviderInfo, _dafny.Seq([0 for d_775_i_ in range(len((d_771_edk_).ciphertext))]))
        d_776_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_777_valueOrError6_: Wrappers.Result = None
        out280_: Wrappers.Result
        out280_ = (d_760_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_772_decryptionMaterialsIn_, _dafny.Seq([d_774_fakeEdk_, d_771_edk_])))
        d_777_valueOrError6_ = out280_
        if not(not((d_777_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(258,34): " + _dafny.string_of(d_777_valueOrError6_))
        d_776_decryptionMaterialsOut_ = (d_777_valueOrError6_).Extract()
        if not((((d_776_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_767_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_778_mpl_: MaterialProviders.MaterialProvidersClient
        d_779_valueOrError0_: Wrappers.Result = None
        out281_: Wrappers.Result
        out281_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_779_valueOrError0_ = out281_
        if not(not((d_779_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,15): " + _dafny.string_of(d_779_valueOrError0_))
        d_778_mpl_ = (d_779_valueOrError0_).Extract()
        d_780_namespace_: _dafny.Seq
        d_781_name_: _dafny.Seq
        out282_: _dafny.Seq
        out283_: _dafny.Seq
        out282_, out283_ = TestUtils.default__.NamespaceAndName(0)
        d_780_namespace_ = out282_
        d_781_name_ = out283_
        d_782_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_783_valueOrError1_: Wrappers.Result = None
        out284_: Wrappers.Result
        out284_ = (d_778_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_780_namespace_, d_781_name_, _dafny.Seq([0 for d_784_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_783_valueOrError1_ = out284_
        if not(not((d_783_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(274,25): " + _dafny.string_of(d_783_valueOrError1_))
        d_782_rawAESKeyring_ = (d_783_valueOrError1_).Extract()
        d_785_encryptionContext_: _dafny.Map
        out285_: _dafny.Map
        out285_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_785_encryptionContext_ = out285_
        d_786_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_786_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_787_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_788_valueOrError2_: Wrappers.Result = None
        d_788_valueOrError2_ = (d_778_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_786_algorithmSuiteId_, d_785_encryptionContext_, _dafny.Seq([])))
        if not(not((d_788_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(283,33): " + _dafny.string_of(d_788_valueOrError2_))
        d_787_decryptionMaterialsIn_ = (d_788_valueOrError2_).Extract()
        d_789_decryptionMaterialsOut_: Wrappers.Result
        out286_: Wrappers.Result
        out286_ = (d_782_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_787_decryptionMaterialsIn_, _dafny.Seq([])))
        d_789_decryptionMaterialsOut_ = out286_
        if not((d_789_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(296,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_790_mpl_: MaterialProviders.MaterialProvidersClient
        d_791_valueOrError0_: Wrappers.Result = None
        out287_: Wrappers.Result
        out287_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_791_valueOrError0_ = out287_
        if not(not((d_791_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,15): " + _dafny.string_of(d_791_valueOrError0_))
        d_790_mpl_ = (d_791_valueOrError0_).Extract()
        d_792_namespace_: _dafny.Seq
        d_793_name_: _dafny.Seq
        out288_: _dafny.Seq
        out289_: _dafny.Seq
        out288_, out289_ = TestUtils.default__.NamespaceAndName(0)
        d_792_namespace_ = out288_
        d_793_name_ = out289_
        d_794_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_795_valueOrError1_: Wrappers.Result = None
        out290_: Wrappers.Result
        out290_ = (d_790_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_792_namespace_, d_793_name_, _dafny.Seq([0 for d_796_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_795_valueOrError1_ = out290_
        if not(not((d_795_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(308,25): " + _dafny.string_of(d_795_valueOrError1_))
        d_794_rawAESKeyring_ = (d_795_valueOrError1_).Extract()
        d_797_unserializableEncryptionContext_: _dafny.Map
        out291_: _dafny.Map
        out291_ = default__.generateUnserializableEncryptionContext()
        d_797_unserializableEncryptionContext_ = out291_
        d_798_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_798_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_799_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_800_valueOrError2_: Wrappers.Result = None
        d_800_valueOrError2_ = (d_790_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_798_algorithmSuiteId_, d_797_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_800_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(317,33): " + _dafny.string_of(d_800_valueOrError2_))
        d_799_encryptionMaterialsIn_ = (d_800_valueOrError2_).Extract()
        d_801_encryptionMaterialsOut_: Wrappers.Result
        out292_: Wrappers.Result
        out292_ = (d_794_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_799_encryptionMaterialsIn_))
        d_801_encryptionMaterialsOut_ = out292_
        if not((d_801_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(329,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_802_mpl_: MaterialProviders.MaterialProvidersClient
        d_803_valueOrError0_: Wrappers.Result = None
        out293_: Wrappers.Result
        out293_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_803_valueOrError0_ = out293_
        if not(not((d_803_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,15): " + _dafny.string_of(d_803_valueOrError0_))
        d_802_mpl_ = (d_803_valueOrError0_).Extract()
        d_804_namespace_: _dafny.Seq
        d_805_name_: _dafny.Seq
        out294_: _dafny.Seq
        out295_: _dafny.Seq
        out294_, out295_ = TestUtils.default__.NamespaceAndName(0)
        d_804_namespace_ = out294_
        d_805_name_ = out295_
        d_806_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_807_valueOrError1_: Wrappers.Result = None
        out296_: Wrappers.Result
        out296_ = (d_802_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_804_namespace_, d_805_name_, _dafny.Seq([0 for d_808_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_807_valueOrError1_ = out296_
        if not(not((d_807_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(342,25): " + _dafny.string_of(d_807_valueOrError1_))
        d_806_rawAESKeyring_ = (d_807_valueOrError1_).Extract()
        d_809_encryptionContext_: _dafny.Map
        out297_: _dafny.Map
        out297_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_809_encryptionContext_ = out297_
        d_810_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_810_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_811_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_812_valueOrError2_: Wrappers.Result = None
        d_812_valueOrError2_ = (d_802_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_810_algorithmSuiteId_, d_809_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_812_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(351,33): " + _dafny.string_of(d_812_valueOrError2_))
        d_811_encryptionMaterialsIn_ = (d_812_valueOrError2_).Extract()
        d_813_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_814_valueOrError3_: Wrappers.Result = None
        out298_: Wrappers.Result
        out298_ = (d_806_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_811_encryptionMaterialsIn_))
        d_814_valueOrError3_ = out298_
        if not(not((d_814_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,34): " + _dafny.string_of(d_814_valueOrError3_))
        d_813_encryptionMaterialsOut_ = (d_814_valueOrError3_).Extract()
        d_815___v4_: tuple
        d_816_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_816_valueOrError4_ = (d_802_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_813_encryptionMaterialsOut_).materials)
        if not(not((d_816_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(364,13): " + _dafny.string_of(d_816_valueOrError4_))
        d_815___v4_ = (d_816_valueOrError4_).Extract()
        d_817_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_817_edk_ = (((d_813_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_818_unserializableEncryptionContext_: _dafny.Map
        out299_: _dafny.Map
        out299_ = default__.generateUnserializableEncryptionContext()
        d_818_unserializableEncryptionContext_ = out299_
        d_819_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_820_valueOrError5_: Wrappers.Result = None
        d_820_valueOrError5_ = (d_802_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_810_algorithmSuiteId_, d_818_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_820_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(369,33): " + _dafny.string_of(d_820_valueOrError5_))
        d_819_decryptionMaterialsIn_ = (d_820_valueOrError5_).Extract()
        d_821_decryptionMaterialsOut_: Wrappers.Result
        out300_: Wrappers.Result
        out300_ = (d_806_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_819_decryptionMaterialsIn_, _dafny.Seq([d_817_edk_])))
        d_821_decryptionMaterialsOut_ = out300_
        if not((d_821_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(382,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_822_keyA_: _dafny.Seq
        d_823_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_823_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_823_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(387,16): " + _dafny.string_of(d_823_valueOrError0_))
        d_822_keyA_ = (d_823_valueOrError0_).Extract()
        d_824_invalidVal_: _dafny.Seq
        d_824_invalidVal_ = _dafny.Seq([0 for d_825___v5_ in range(65536)])
        encCtx = _dafny.Map({d_822_keyA_: d_824_invalidVal_})
        return encCtx
        return encCtx

