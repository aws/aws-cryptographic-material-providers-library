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
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
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

# Module: TestRawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_449_mpl_: MaterialProviders.MaterialProvidersClient
        d_450_valueOrError0_: Wrappers.Result = None
        out153_: Wrappers.Result
        out153_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_450_valueOrError0_ = out153_
        if not(not((d_450_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(20,15): " + _dafny.string_of(d_450_valueOrError0_))
        d_449_mpl_ = (d_450_valueOrError0_).Extract()
        d_451_namespace_: _dafny.Seq
        d_452_name_: _dafny.Seq
        out154_: _dafny.Seq
        out155_: _dafny.Seq
        out154_, out155_ = TestUtils.default__.NamespaceAndName(0)
        d_451_namespace_ = out154_
        d_452_name_ = out155_
        d_453_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_454_valueOrError1_: Wrappers.Result = None
        out156_: Wrappers.Result
        out156_ = (d_449_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_451_namespace_, d_452_name_, _dafny.Seq([0 for d_455_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_454_valueOrError1_ = out156_
        if not(not((d_454_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(23,25): " + _dafny.string_of(d_454_valueOrError1_))
        d_453_rawAESKeyring_ = (d_454_valueOrError1_).Extract()
        d_456_encryptionContext_: _dafny.Map
        out157_: _dafny.Map
        out157_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_456_encryptionContext_ = out157_
        d_457_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_457_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_458_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_459_valueOrError2_: Wrappers.Result = None
        d_459_valueOrError2_ = (d_449_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_457_algorithmSuiteId_, d_456_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_459_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(32,33): " + _dafny.string_of(d_459_valueOrError2_))
        d_458_encryptionMaterialsIn_ = (d_459_valueOrError2_).Extract()
        d_460_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_461_valueOrError3_: Wrappers.Result = None
        out158_: Wrappers.Result
        out158_ = (d_453_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_458_encryptionMaterialsIn_))
        d_461_valueOrError3_ = out158_
        if not(not((d_461_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(42,34): " + _dafny.string_of(d_461_valueOrError3_))
        d_460_encryptionMaterialsOut_ = (d_461_valueOrError3_).Extract()
        d_462___v0_: tuple
        d_463_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_463_valueOrError4_ = (d_449_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_460_encryptionMaterialsOut_).materials)
        if not(not((d_463_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(57,13): " + _dafny.string_of(d_463_valueOrError4_))
        d_462___v0_ = (d_463_valueOrError4_).Extract()
        if not((len(((d_460_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_464_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_464_edk_ = (((d_460_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_465_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_466_valueOrError5_: Wrappers.Result = None
        d_466_valueOrError5_ = (d_449_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_457_algorithmSuiteId_, d_456_encryptionContext_, _dafny.Seq([])))
        if not(not((d_466_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(68,33): " + _dafny.string_of(d_466_valueOrError5_))
        d_465_decryptionMaterialsIn_ = (d_466_valueOrError5_).Extract()
        d_467_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_468_valueOrError6_: Wrappers.Result = None
        out159_: Wrappers.Result
        out159_ = (d_453_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_465_decryptionMaterialsIn_, _dafny.Seq([d_464_edk_])))
        d_468_valueOrError6_ = out159_
        if not(not((d_468_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(75,34): " + _dafny.string_of(d_468_valueOrError6_))
        d_467_decryptionMaterialsOut_ = (d_468_valueOrError6_).Extract()
        if not((((d_460_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_460_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_469_mpl_: MaterialProviders.MaterialProvidersClient
        d_470_valueOrError0_: Wrappers.Result = None
        out160_: Wrappers.Result
        out160_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_470_valueOrError0_ = out160_
        if not(not((d_470_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(93,15): " + _dafny.string_of(d_470_valueOrError0_))
        d_469_mpl_ = (d_470_valueOrError0_).Extract()
        d_471_namespace_: _dafny.Seq
        d_472_name_: _dafny.Seq
        out161_: _dafny.Seq
        out162_: _dafny.Seq
        out161_, out162_ = TestUtils.default__.NamespaceAndName(0)
        d_471_namespace_ = out161_
        d_472_name_ = out162_
        d_473_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_474_valueOrError1_: Wrappers.Result = None
        out163_: Wrappers.Result
        out163_ = (d_469_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_471_namespace_, d_472_name_, _dafny.Seq([0 for d_475_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_474_valueOrError1_ = out163_
        if not(not((d_474_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(96,25): " + _dafny.string_of(d_474_valueOrError1_))
        d_473_rawAESKeyring_ = (d_474_valueOrError1_).Extract()
        d_476_encryptionContext_: _dafny.Map
        out164_: _dafny.Map
        out164_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_476_encryptionContext_ = out164_
        d_477_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_477_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_478_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_479_valueOrError2_: Wrappers.Result = None
        d_479_valueOrError2_ = (d_469_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_477_algorithmSuiteId_, d_476_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_479_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(105,33): " + _dafny.string_of(d_479_valueOrError2_))
        d_478_encryptionMaterialsIn_ = (d_479_valueOrError2_).Extract()
        d_480_pdk_: _dafny.Seq
        d_480_pdk_ = _dafny.Seq([0 for d_481_i_ in range(32)])
        d_482_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_483_valueOrError3_: Wrappers.Result = None
        pat_let_tv1_ = d_480_pdk_
        out165_: Wrappers.Result
        def iife12_(_pat_let4_0):
            def iife13_(d_484_dt__update__tmp_h0_):
                def iife14_(_pat_let5_0):
                    def iife15_(d_485_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_484_dt__update__tmp_h0_).algorithmSuite, (d_484_dt__update__tmp_h0_).encryptionContext, (d_484_dt__update__tmp_h0_).encryptedDataKeys, (d_484_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_485_dt__update_hplaintextDataKey_h0_, (d_484_dt__update__tmp_h0_).signingKey, (d_484_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife15_(_pat_let5_0)
                return iife14_(Wrappers.Option_Some(pat_let_tv1_))
            return iife13_(_pat_let4_0)
        out165_ = (d_473_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(iife12_(d_478_encryptionMaterialsIn_)))
        d_483_valueOrError3_ = out165_
        if not(not((d_483_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(120,34): " + _dafny.string_of(d_483_valueOrError3_))
        d_482_encryptionMaterialsOut_ = (d_483_valueOrError3_).Extract()
        d_486___v1_: tuple
        d_487_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_487_valueOrError4_ = (d_469_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_482_encryptionMaterialsOut_).materials)
        if not(not((d_487_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(124,13): " + _dafny.string_of(d_487_valueOrError4_))
        d_486___v1_ = (d_487_valueOrError4_).Extract()
        d_488_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_488_edk_ = (((d_482_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_489_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_490_valueOrError5_: Wrappers.Result = None
        d_490_valueOrError5_ = (d_469_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_477_algorithmSuiteId_, d_476_encryptionContext_, _dafny.Seq([])))
        if not(not((d_490_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(128,33): " + _dafny.string_of(d_490_valueOrError5_))
        d_489_decryptionMaterialsIn_ = (d_490_valueOrError5_).Extract()
        d_491_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_492_valueOrError6_: Wrappers.Result = None
        out166_: Wrappers.Result
        out166_ = (d_473_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_489_decryptionMaterialsIn_, _dafny.Seq([d_488_edk_])))
        d_492_valueOrError6_ = out166_
        if not(not((d_492_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(136,34): " + _dafny.string_of(d_492_valueOrError6_))
        d_491_decryptionMaterialsOut_ = (d_492_valueOrError6_).Extract()
        if not((((d_491_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_480_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_493_mpl_: MaterialProviders.MaterialProvidersClient
        d_494_valueOrError0_: Wrappers.Result = None
        out167_: Wrappers.Result
        out167_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_494_valueOrError0_ = out167_
        if not(not((d_494_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(154,15): " + _dafny.string_of(d_494_valueOrError0_))
        d_493_mpl_ = (d_494_valueOrError0_).Extract()
        d_495_namespace_: _dafny.Seq
        d_496_name_: _dafny.Seq
        out168_: _dafny.Seq
        out169_: _dafny.Seq
        out168_, out169_ = TestUtils.default__.NamespaceAndName(0)
        d_495_namespace_ = out168_
        d_496_name_ = out169_
        d_497_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_498_valueOrError1_: Wrappers.Result = None
        out170_: Wrappers.Result
        out170_ = (d_493_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_495_namespace_, d_496_name_, _dafny.Seq([0 for d_499_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_498_valueOrError1_ = out170_
        if not(not((d_498_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(157,25): " + _dafny.string_of(d_498_valueOrError1_))
        d_497_rawAESKeyring_ = (d_498_valueOrError1_).Extract()
        d_500_mismatchedAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_501_valueOrError2_: Wrappers.Result = None
        out171_: Wrappers.Result
        out171_ = (d_493_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_495_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_502_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_501_valueOrError2_ = out171_
        if not(not((d_501_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(164,32): " + _dafny.string_of(d_501_valueOrError2_))
        d_500_mismatchedAESKeyring_ = (d_501_valueOrError2_).Extract()
        d_503_encryptionContext_: _dafny.Map
        out172_: _dafny.Map
        out172_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_503_encryptionContext_ = out172_
        d_504_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_504_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_505_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_506_valueOrError3_: Wrappers.Result = None
        d_506_valueOrError3_ = (d_493_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_504_algorithmSuiteId_, d_503_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_506_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(174,33): " + _dafny.string_of(d_506_valueOrError3_))
        d_505_encryptionMaterialsIn_ = (d_506_valueOrError3_).Extract()
        d_507_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_508_valueOrError4_: Wrappers.Result = None
        out173_: Wrappers.Result
        out173_ = (d_497_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_505_encryptionMaterialsIn_))
        d_508_valueOrError4_ = out173_
        if not(not((d_508_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(184,34): " + _dafny.string_of(d_508_valueOrError4_))
        d_507_encryptionMaterialsOut_ = (d_508_valueOrError4_).Extract()
        d_509___v2_: tuple
        d_510_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_510_valueOrError5_ = (d_493_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_507_encryptionMaterialsOut_).materials)
        if not(not((d_510_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(188,13): " + _dafny.string_of(d_510_valueOrError5_))
        d_509___v2_ = (d_510_valueOrError5_).Extract()
        d_511_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_511_edk_ = (((d_507_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_512_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_513_valueOrError6_: Wrappers.Result = None
        d_513_valueOrError6_ = (d_493_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_504_algorithmSuiteId_, d_503_encryptionContext_, _dafny.Seq([])))
        if not(not((d_513_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(192,33): " + _dafny.string_of(d_513_valueOrError6_))
        d_512_decryptionMaterialsIn_ = (d_513_valueOrError6_).Extract()
        d_514_decryptionMaterialsOut_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = (d_500_mismatchedAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_512_decryptionMaterialsIn_, _dafny.Seq([d_511_edk_])))
        d_514_decryptionMaterialsOut_ = out174_
        if not((d_514_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(205,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_514_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_514_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_514_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(208,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_514_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("AESKeyring"), d_495_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(209,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_515_mpl_: MaterialProviders.MaterialProvidersClient
        d_516_valueOrError0_: Wrappers.Result = None
        out175_: Wrappers.Result
        out175_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_516_valueOrError0_ = out175_
        if not(not((d_516_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,15): " + _dafny.string_of(d_516_valueOrError0_))
        d_515_mpl_ = (d_516_valueOrError0_).Extract()
        d_517_namespace_: _dafny.Seq
        d_518_name_: _dafny.Seq
        out176_: _dafny.Seq
        out177_: _dafny.Seq
        out176_, out177_ = TestUtils.default__.NamespaceAndName(0)
        d_517_namespace_ = out176_
        d_518_name_ = out177_
        d_519_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_520_valueOrError1_: Wrappers.Result = None
        out178_: Wrappers.Result
        out178_ = (d_515_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_517_namespace_, d_518_name_, _dafny.Seq([0 for d_521_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_520_valueOrError1_ = out178_
        if not(not((d_520_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(218,25): " + _dafny.string_of(d_520_valueOrError1_))
        d_519_rawAESKeyring_ = (d_520_valueOrError1_).Extract()
        d_522_encryptionContext_: _dafny.Map
        out179_: _dafny.Map
        out179_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_522_encryptionContext_ = out179_
        d_523_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_523_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_524_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_525_valueOrError2_: Wrappers.Result = None
        d_525_valueOrError2_ = (d_515_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_523_algorithmSuiteId_, d_522_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_525_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(227,33): " + _dafny.string_of(d_525_valueOrError2_))
        d_524_encryptionMaterialsIn_ = (d_525_valueOrError2_).Extract()
        d_526_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_527_valueOrError3_: Wrappers.Result = None
        out180_: Wrappers.Result
        out180_ = (d_519_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_524_encryptionMaterialsIn_))
        d_527_valueOrError3_ = out180_
        if not(not((d_527_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(237,34): " + _dafny.string_of(d_527_valueOrError3_))
        d_526_encryptionMaterialsOut_ = (d_527_valueOrError3_).Extract()
        d_528___v3_: tuple
        d_529_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_529_valueOrError4_ = (d_515_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_526_encryptionMaterialsOut_).materials)
        if not(not((d_529_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(241,13): " + _dafny.string_of(d_529_valueOrError4_))
        d_528___v3_ = (d_529_valueOrError4_).Extract()
        d_530_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_530_edk_ = (((d_526_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_531_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_532_valueOrError5_: Wrappers.Result = None
        d_532_valueOrError5_ = (d_515_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_523_algorithmSuiteId_, d_522_encryptionContext_, _dafny.Seq([])))
        if not(not((d_532_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(245,33): " + _dafny.string_of(d_532_valueOrError5_))
        d_531_decryptionMaterialsIn_ = (d_532_valueOrError5_).Extract()
        d_533_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_533_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_530_edk_).keyProviderId, (d_530_edk_).keyProviderInfo, _dafny.Seq([0 for d_534_i_ in range(len((d_530_edk_).ciphertext))]))
        d_535_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_536_valueOrError6_: Wrappers.Result = None
        out181_: Wrappers.Result
        out181_ = (d_519_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_531_decryptionMaterialsIn_, _dafny.Seq([d_533_fakeEdk_, d_530_edk_])))
        d_536_valueOrError6_ = out181_
        if not(not((d_536_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(258,34): " + _dafny.string_of(d_536_valueOrError6_))
        d_535_decryptionMaterialsOut_ = (d_536_valueOrError6_).Extract()
        if not((((d_535_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_526_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_537_mpl_: MaterialProviders.MaterialProvidersClient
        d_538_valueOrError0_: Wrappers.Result = None
        out182_: Wrappers.Result
        out182_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_538_valueOrError0_ = out182_
        if not(not((d_538_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,15): " + _dafny.string_of(d_538_valueOrError0_))
        d_537_mpl_ = (d_538_valueOrError0_).Extract()
        d_539_namespace_: _dafny.Seq
        d_540_name_: _dafny.Seq
        out183_: _dafny.Seq
        out184_: _dafny.Seq
        out183_, out184_ = TestUtils.default__.NamespaceAndName(0)
        d_539_namespace_ = out183_
        d_540_name_ = out184_
        d_541_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_542_valueOrError1_: Wrappers.Result = None
        out185_: Wrappers.Result
        out185_ = (d_537_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_539_namespace_, d_540_name_, _dafny.Seq([0 for d_543_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_542_valueOrError1_ = out185_
        if not(not((d_542_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(274,25): " + _dafny.string_of(d_542_valueOrError1_))
        d_541_rawAESKeyring_ = (d_542_valueOrError1_).Extract()
        d_544_encryptionContext_: _dafny.Map
        out186_: _dafny.Map
        out186_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_544_encryptionContext_ = out186_
        d_545_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_545_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_546_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_547_valueOrError2_: Wrappers.Result = None
        d_547_valueOrError2_ = (d_537_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_545_algorithmSuiteId_, d_544_encryptionContext_, _dafny.Seq([])))
        if not(not((d_547_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(283,33): " + _dafny.string_of(d_547_valueOrError2_))
        d_546_decryptionMaterialsIn_ = (d_547_valueOrError2_).Extract()
        d_548_decryptionMaterialsOut_: Wrappers.Result
        out187_: Wrappers.Result
        out187_ = (d_541_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_546_decryptionMaterialsIn_, _dafny.Seq([])))
        d_548_decryptionMaterialsOut_ = out187_
        if not((d_548_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(296,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_549_mpl_: MaterialProviders.MaterialProvidersClient
        d_550_valueOrError0_: Wrappers.Result = None
        out188_: Wrappers.Result
        out188_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_550_valueOrError0_ = out188_
        if not(not((d_550_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,15): " + _dafny.string_of(d_550_valueOrError0_))
        d_549_mpl_ = (d_550_valueOrError0_).Extract()
        d_551_namespace_: _dafny.Seq
        d_552_name_: _dafny.Seq
        out189_: _dafny.Seq
        out190_: _dafny.Seq
        out189_, out190_ = TestUtils.default__.NamespaceAndName(0)
        d_551_namespace_ = out189_
        d_552_name_ = out190_
        d_553_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_554_valueOrError1_: Wrappers.Result = None
        out191_: Wrappers.Result
        out191_ = (d_549_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_551_namespace_, d_552_name_, _dafny.Seq([0 for d_555_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_554_valueOrError1_ = out191_
        if not(not((d_554_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(308,25): " + _dafny.string_of(d_554_valueOrError1_))
        d_553_rawAESKeyring_ = (d_554_valueOrError1_).Extract()
        d_556_unserializableEncryptionContext_: _dafny.Map
        out192_: _dafny.Map
        out192_ = default__.generateUnserializableEncryptionContext()
        d_556_unserializableEncryptionContext_ = out192_
        d_557_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_557_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_558_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_559_valueOrError2_: Wrappers.Result = None
        d_559_valueOrError2_ = (d_549_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_557_algorithmSuiteId_, d_556_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_559_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(317,33): " + _dafny.string_of(d_559_valueOrError2_))
        d_558_encryptionMaterialsIn_ = (d_559_valueOrError2_).Extract()
        d_560_encryptionMaterialsOut_: Wrappers.Result
        out193_: Wrappers.Result
        out193_ = (d_553_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_558_encryptionMaterialsIn_))
        d_560_encryptionMaterialsOut_ = out193_
        if not((d_560_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(329,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_561_mpl_: MaterialProviders.MaterialProvidersClient
        d_562_valueOrError0_: Wrappers.Result = None
        out194_: Wrappers.Result
        out194_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_562_valueOrError0_ = out194_
        if not(not((d_562_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,15): " + _dafny.string_of(d_562_valueOrError0_))
        d_561_mpl_ = (d_562_valueOrError0_).Extract()
        d_563_namespace_: _dafny.Seq
        d_564_name_: _dafny.Seq
        out195_: _dafny.Seq
        out196_: _dafny.Seq
        out195_, out196_ = TestUtils.default__.NamespaceAndName(0)
        d_563_namespace_ = out195_
        d_564_name_ = out196_
        d_565_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_566_valueOrError1_: Wrappers.Result = None
        out197_: Wrappers.Result
        out197_ = (d_561_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_563_namespace_, d_564_name_, _dafny.Seq([0 for d_567_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_566_valueOrError1_ = out197_
        if not(not((d_566_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(342,25): " + _dafny.string_of(d_566_valueOrError1_))
        d_565_rawAESKeyring_ = (d_566_valueOrError1_).Extract()
        d_568_encryptionContext_: _dafny.Map
        out198_: _dafny.Map
        out198_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_568_encryptionContext_ = out198_
        d_569_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_569_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_570_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_571_valueOrError2_: Wrappers.Result = None
        d_571_valueOrError2_ = (d_561_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_569_algorithmSuiteId_, d_568_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_571_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(351,33): " + _dafny.string_of(d_571_valueOrError2_))
        d_570_encryptionMaterialsIn_ = (d_571_valueOrError2_).Extract()
        d_572_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_573_valueOrError3_: Wrappers.Result = None
        out199_: Wrappers.Result
        out199_ = (d_565_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_570_encryptionMaterialsIn_))
        d_573_valueOrError3_ = out199_
        if not(not((d_573_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,34): " + _dafny.string_of(d_573_valueOrError3_))
        d_572_encryptionMaterialsOut_ = (d_573_valueOrError3_).Extract()
        d_574___v4_: tuple
        d_575_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_575_valueOrError4_ = (d_561_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_572_encryptionMaterialsOut_).materials)
        if not(not((d_575_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(364,13): " + _dafny.string_of(d_575_valueOrError4_))
        d_574___v4_ = (d_575_valueOrError4_).Extract()
        d_576_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_576_edk_ = (((d_572_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_577_unserializableEncryptionContext_: _dafny.Map
        out200_: _dafny.Map
        out200_ = default__.generateUnserializableEncryptionContext()
        d_577_unserializableEncryptionContext_ = out200_
        d_578_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_579_valueOrError5_: Wrappers.Result = None
        d_579_valueOrError5_ = (d_561_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_569_algorithmSuiteId_, d_577_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_579_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(369,33): " + _dafny.string_of(d_579_valueOrError5_))
        d_578_decryptionMaterialsIn_ = (d_579_valueOrError5_).Extract()
        d_580_decryptionMaterialsOut_: Wrappers.Result
        out201_: Wrappers.Result
        out201_ = (d_565_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_578_decryptionMaterialsIn_, _dafny.Seq([d_576_edk_])))
        d_580_decryptionMaterialsOut_ = out201_
        if not((d_580_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(382,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_581_keyA_: _dafny.Seq
        d_582_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_582_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_582_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(387,16): " + _dafny.string_of(d_582_valueOrError0_))
        d_581_keyA_ = (d_582_valueOrError0_).Extract()
        d_583_invalidVal_: _dafny.Seq
        d_583_invalidVal_ = _dafny.Seq([0 for d_584___v5_ in range(65536)])
        encCtx = _dafny.Map({d_581_keyA_: d_583_invalidVal_})
        return encCtx
        return encCtx

