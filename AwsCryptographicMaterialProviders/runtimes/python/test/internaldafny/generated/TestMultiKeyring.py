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
import TestRawAESKeyring as TestRawAESKeyring

# Module: TestMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getInputEncryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_585_mpl_: MaterialProviders.MaterialProvidersClient
        d_586_valueOrError0_: Wrappers.Result = None
        out202_: Wrappers.Result
        out202_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_586_valueOrError0_ = out202_
        if not(not((d_586_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,15): " + _dafny.string_of(d_586_valueOrError0_))
        d_585_mpl_ = (d_586_valueOrError0_).Extract()
        d_587_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_587_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_588_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_589_valueOrError1_: Wrappers.Result = None
        d_589_valueOrError1_ = (d_585_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_587_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_589_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,33): " + _dafny.string_of(d_589_valueOrError1_))
        d_588_encryptionMaterialsIn_ = (d_589_valueOrError1_).Extract()
        res = d_588_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        d_590_mpl_: MaterialProviders.MaterialProvidersClient
        d_591_valueOrError0_: Wrappers.Result = None
        out203_: Wrappers.Result
        out203_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_591_valueOrError0_ = out203_
        if not(not((d_591_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,15): " + _dafny.string_of(d_591_valueOrError0_))
        d_590_mpl_ = (d_591_valueOrError0_).Extract()
        d_592_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_592_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_593_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_594_valueOrError1_: Wrappers.Result = None
        d_594_valueOrError1_ = (d_590_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_592_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_594_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,33): " + _dafny.string_of(d_594_valueOrError1_))
        d_593_decryptionMaterialsIn_ = (d_594_valueOrError1_).Extract()
        res = d_593_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_595_mpl_: MaterialProviders.MaterialProvidersClient
        d_596_valueOrError0_: Wrappers.Result = None
        out204_: Wrappers.Result
        out204_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_596_valueOrError0_ = out204_
        if not(not((d_596_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,15): " + _dafny.string_of(d_596_valueOrError0_))
        d_595_mpl_ = (d_596_valueOrError0_).Extract()
        d_597_encryptionContext_: _dafny.Map
        out205_: _dafny.Map
        out205_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_597_encryptionContext_ = out205_
        d_598_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out206_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out206_ = default__.getInputEncryptionMaterials(d_597_encryptionContext_)
        d_598_encryptionMaterials_ = out206_
        d_599_decryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out207_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out207_ = default__.getInputDecryptionMaterials(d_597_encryptionContext_)
        d_599_decryptionMaterials_ = out207_
        d_600_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out208_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out208_ = default__.setupRawAesKeyring(d_597_encryptionContext_)
        d_600_rawAESKeyring_ = out208_
        d_601_expectedEncryptionMaterials_: Wrappers.Result
        out209_: Wrappers.Result
        out209_ = (d_600_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_598_encryptionMaterials_))
        d_601_expectedEncryptionMaterials_ = out209_
        if not((d_601_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_602_expectedPlaintextDataKey_: Wrappers.Option
        d_602_expectedPlaintextDataKey_ = (((d_601_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_602_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_603_staticKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out210_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out210_ = default__.SetupStaticKeyring(Wrappers.Option_Some(((d_601_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_603_staticKeyring_ = out210_
        d_604_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_605_valueOrError1_: Wrappers.Result = None
        out211_: Wrappers.Result
        out211_ = (d_595_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_603_staticKeyring_), _dafny.Seq([d_600_rawAESKeyring_])))
        d_605_valueOrError1_ = out211_
        if not(not((d_605_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,24): " + _dafny.string_of(d_605_valueOrError1_))
        d_604_multiKeyring_ = (d_605_valueOrError1_).Extract()
        d_606_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_607_valueOrError2_: Wrappers.Result = None
        out212_: Wrappers.Result
        out212_ = (d_604_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_598_encryptionMaterials_))
        d_607_valueOrError2_ = out212_
        if not(not((d_607_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,34): " + _dafny.string_of(d_607_valueOrError2_))
        d_606_encryptionMaterialsOut_ = (d_607_valueOrError2_).Extract()
        d_608___v0_: tuple
        d_609_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_609_valueOrError3_ = (d_595_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_606_encryptionMaterialsOut_).materials)
        if not(not((d_609_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,13): " + _dafny.string_of(d_609_valueOrError3_))
        d_608___v0_ = (d_609_valueOrError3_).Extract()
        if not(((((d_606_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_602_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_606_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_610_mpl_: MaterialProviders.MaterialProvidersClient
        d_611_valueOrError0_: Wrappers.Result = None
        out213_: Wrappers.Result
        out213_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_611_valueOrError0_ = out213_
        if not(not((d_611_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,15): " + _dafny.string_of(d_611_valueOrError0_))
        d_610_mpl_ = (d_611_valueOrError0_).Extract()
        d_612_encryptionContext_: _dafny.Map
        out214_: _dafny.Map
        out214_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_612_encryptionContext_ = out214_
        d_613_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out215_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out215_ = default__.setupRawAesKeyring(d_612_encryptionContext_)
        d_613_rawAESKeyring_ = out215_
        d_614_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out216_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out216_ = default__.SetupFailingKeyring()
        d_614_failingKeyring_ = out216_
        d_615_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_616_valueOrError1_: Wrappers.Result = None
        out217_: Wrappers.Result
        out217_ = (d_610_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_613_rawAESKeyring_), _dafny.Seq([d_614_failingKeyring_])))
        d_616_valueOrError1_ = out217_
        if not(not((d_616_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,24): " + _dafny.string_of(d_616_valueOrError1_))
        d_615_multiKeyring_ = (d_616_valueOrError1_).Extract()
        d_617_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out218_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out218_ = default__.getInputEncryptionMaterials(d_612_encryptionContext_)
        d_617_encryptionMaterials_ = out218_
        d_618_result_: Wrappers.Result
        out219_: Wrappers.Result
        out219_ = (d_615_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_617_encryptionMaterials_))
        d_618_result_ = out219_
        if not((d_618_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_619_mpl_: MaterialProviders.MaterialProvidersClient
        d_620_valueOrError0_: Wrappers.Result = None
        out220_: Wrappers.Result
        out220_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_620_valueOrError0_ = out220_
        if not(not((d_620_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,15): " + _dafny.string_of(d_620_valueOrError0_))
        d_619_mpl_ = (d_620_valueOrError0_).Extract()
        d_621_encryptionContext_: _dafny.Map
        out221_: _dafny.Map
        out221_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_621_encryptionContext_ = out221_
        d_622_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out222_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out222_ = default__.SetupFailingKeyring()
        d_622_failingKeyring_ = out222_
        d_623_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out223_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out223_ = default__.setupRawAesKeyring(d_621_encryptionContext_)
        d_623_rawAESKeyring_ = out223_
        d_624_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_625_valueOrError1_: Wrappers.Result = None
        out224_: Wrappers.Result
        out224_ = (d_619_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_622_failingKeyring_), _dafny.Seq([d_623_rawAESKeyring_])))
        d_625_valueOrError1_ = out224_
        if not(not((d_625_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,24): " + _dafny.string_of(d_625_valueOrError1_))
        d_624_multiKeyring_ = (d_625_valueOrError1_).Extract()
        d_626_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out225_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out225_ = default__.getInputEncryptionMaterials(d_621_encryptionContext_)
        d_626_encryptionMaterials_ = out225_
        d_627_result_: Wrappers.Result
        out226_: Wrappers.Result
        out226_ = (d_624_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_626_encryptionMaterials_))
        d_627_result_ = out226_
        if not((d_627_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_628_mpl_: MaterialProviders.MaterialProvidersClient
        d_629_valueOrError0_: Wrappers.Result = None
        out227_: Wrappers.Result
        out227_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_629_valueOrError0_ = out227_
        if not(not((d_629_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,15): " + _dafny.string_of(d_629_valueOrError0_))
        d_628_mpl_ = (d_629_valueOrError0_).Extract()
        d_630_encryptionContext_: _dafny.Map
        out228_: _dafny.Map
        out228_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_630_encryptionContext_ = out228_
        d_631_encryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out229_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out229_ = default__.getInputEncryptionMaterials(d_630_encryptionContext_)
        d_631_encryptionMaterials_ = out229_
        d_632_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out230_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out230_ = default__.SetupStaticKeyring(Wrappers.Option_Some(d_631_encryptionMaterials_), Wrappers.Option_None())
        d_632_failingKeyring_ = out230_
        d_633_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_634_valueOrError1_: Wrappers.Result = None
        out231_: Wrappers.Result
        out231_ = (d_628_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_632_failingKeyring_), _dafny.Seq([])))
        d_634_valueOrError1_ = out231_
        if not(not((d_634_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,24): " + _dafny.string_of(d_634_valueOrError1_))
        d_633_multiKeyring_ = (d_634_valueOrError1_).Extract()
        d_635_result_: Wrappers.Result
        out232_: Wrappers.Result
        out232_ = (d_633_multiKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_631_encryptionMaterials_))
        d_635_result_ = out232_
        if not((d_635_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_636_mpl_: MaterialProviders.MaterialProvidersClient
        d_637_valueOrError0_: Wrappers.Result = None
        out233_: Wrappers.Result
        out233_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_637_valueOrError0_ = out233_
        if not(not((d_637_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,15): " + _dafny.string_of(d_637_valueOrError0_))
        d_636_mpl_ = (d_637_valueOrError0_).Extract()
        d_638_encryptionContext_: _dafny.Map
        out234_: _dafny.Map
        out234_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_638_encryptionContext_ = out234_
        d_639_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out235_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out235_ = default__.setupRawAesKeyring(d_638_encryptionContext_)
        d_639_rawAESKeyring_ = out235_
        d_640_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out236_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out236_ = default__.getInputEncryptionMaterials(d_638_encryptionContext_)
        d_640_inputEncryptionMaterials_ = out236_
        d_641_encryptionMaterials_: Wrappers.Result
        out237_: Wrappers.Result
        out237_ = (d_639_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_640_inputEncryptionMaterials_))
        d_641_encryptionMaterials_ = out237_
        if not((d_641_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_642_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out238_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out238_ = default__.getInputDecryptionMaterials(d_638_encryptionContext_)
        d_642_inputDecryptionMaterials_ = out238_
        d_643_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out239_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out239_ = default__.SetupFailingKeyring()
        d_643_failingKeyring_ = out239_
        d_644_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_645_valueOrError1_: Wrappers.Result = None
        out240_: Wrappers.Result
        out240_ = (d_636_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_639_rawAESKeyring_), _dafny.Seq([d_643_failingKeyring_])))
        d_645_valueOrError1_ = out240_
        if not(not((d_645_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,24): " + _dafny.string_of(d_645_valueOrError1_))
        d_644_multiKeyring_ = (d_645_valueOrError1_).Extract()
        d_646_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_646_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_642_inputDecryptionMaterials_, (((d_641_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_647_decryptionMaterials_: Wrappers.Result
        out241_: Wrappers.Result
        out241_ = (d_644_multiKeyring_).OnDecrypt(d_646_onDecryptInput_)
        d_647_decryptionMaterials_ = out241_
        if not((d_647_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_647_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_641_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_648_mpl_: MaterialProviders.MaterialProvidersClient
        d_649_valueOrError0_: Wrappers.Result = None
        out242_: Wrappers.Result
        out242_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_649_valueOrError0_ = out242_
        if not(not((d_649_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,15): " + _dafny.string_of(d_649_valueOrError0_))
        d_648_mpl_ = (d_649_valueOrError0_).Extract()
        d_650_encryptionContext_: _dafny.Map
        out243_: _dafny.Map
        out243_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_650_encryptionContext_ = out243_
        d_651_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out244_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out244_ = default__.setupRawAesKeyring(d_650_encryptionContext_)
        d_651_rawAESKeyring_ = out244_
        d_652_inputEncryptionMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out245_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out245_ = default__.getInputEncryptionMaterials(d_650_encryptionContext_)
        d_652_inputEncryptionMaterials_ = out245_
        d_653_encryptionMaterials_: Wrappers.Result
        out246_: Wrappers.Result
        out246_ = (d_651_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_652_inputEncryptionMaterials_))
        d_653_encryptionMaterials_ = out246_
        if not((d_653_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_654_inputDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out247_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        out247_ = default__.getInputDecryptionMaterials(d_650_encryptionContext_)
        d_654_inputDecryptionMaterials_ = out247_
        d_655_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out248_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out248_ = default__.SetupFailingKeyring()
        d_655_failingKeyring_ = out248_
        d_656_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_657_valueOrError1_: Wrappers.Result = None
        out249_: Wrappers.Result
        out249_ = (d_648_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_655_failingKeyring_), _dafny.Seq([d_655_failingKeyring_, d_651_rawAESKeyring_, d_655_failingKeyring_])))
        d_657_valueOrError1_ = out249_
        if not(not((d_657_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,24): " + _dafny.string_of(d_657_valueOrError1_))
        d_656_multiKeyring_ = (d_657_valueOrError1_).Extract()
        d_658_onDecryptInput_: AwsCryptographyMaterialProvidersTypes.OnDecryptInput
        d_658_onDecryptInput_ = AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_654_inputDecryptionMaterials_, (((d_653_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_659_decryptionMaterials_: Wrappers.Result
        out250_: Wrappers.Result
        out250_ = (d_656_multiKeyring_).OnDecrypt(d_658_onDecryptInput_)
        d_659_decryptionMaterials_ = out250_
        if not((d_659_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_659_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_653_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_660_mpl_: MaterialProviders.MaterialProvidersClient
        d_661_valueOrError0_: Wrappers.Result = None
        out251_: Wrappers.Result
        out251_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_661_valueOrError0_ = out251_
        if not(not((d_661_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,15): " + _dafny.string_of(d_661_valueOrError0_))
        d_660_mpl_ = (d_661_valueOrError0_).Extract()
        d_662_encryptionContext_: _dafny.Map
        out252_: _dafny.Map
        out252_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_662_encryptionContext_ = out252_
        d_663_failingKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out253_: AwsCryptographyMaterialProvidersTypes.IKeyring
        out253_ = default__.SetupFailingKeyring()
        d_663_failingKeyring_ = out253_
        d_664_multiKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_665_valueOrError1_: Wrappers.Result = None
        out254_: Wrappers.Result
        out254_ = (d_660_mpl_).CreateMultiKeyring(AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_663_failingKeyring_, d_663_failingKeyring_])))
        d_665_valueOrError1_ = out254_
        if not(not((d_665_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,24): " + _dafny.string_of(d_665_valueOrError1_))
        d_664_multiKeyring_ = (d_665_valueOrError1_).Extract()
        d_666_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_667_valueOrError2_: Wrappers.Result = None
        d_667_valueOrError2_ = (d_660_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_662_encryptionContext_, _dafny.Seq([])))
        if not(not((d_667_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,21): " + _dafny.string_of(d_667_valueOrError2_))
        d_666_materials_ = (d_667_valueOrError2_).Extract()
        d_668_result_: Wrappers.Result
        out255_: Wrappers.Result
        out255_ = (d_664_multiKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_666_materials_, _dafny.Seq([])))
        d_668_result_ = out255_
        if not((d_668_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        d_669_mpl_: MaterialProviders.MaterialProvidersClient
        d_670_valueOrError0_: Wrappers.Result = None
        out256_: Wrappers.Result
        out256_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_670_valueOrError0_ = out256_
        if not(not((d_670_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,15): " + _dafny.string_of(d_670_valueOrError0_))
        d_669_mpl_ = (d_670_valueOrError0_).Extract()
        d_671_namespace_: _dafny.Seq
        d_672_name_: _dafny.Seq
        out257_: _dafny.Seq
        out258_: _dafny.Seq
        out257_, out258_ = TestUtils.default__.NamespaceAndName(0)
        d_671_namespace_ = out257_
        d_672_name_ = out258_
        d_673_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_674_valueOrError1_: Wrappers.Result = None
        out259_: Wrappers.Result
        out259_ = (d_669_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_671_namespace_, d_672_name_, _dafny.Seq([0 for d_675_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_674_valueOrError1_ = out259_
        if not(not((d_674_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,25): " + _dafny.string_of(d_674_valueOrError1_))
        d_673_rawAESKeyring_ = (d_674_valueOrError1_).Extract()
        res = d_673_rawAESKeyring_
        return res
        return res

    @staticmethod
    def SetupStaticKeyring(encryptionMaterials, decryptionMaterials):
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        nw4_ = StaticKeyring()
        nw4_.ctor__(encryptionMaterials, decryptionMaterials)
        res = nw4_
        return res
        return res

    @staticmethod
    def SetupFailingKeyring():
        res: AwsCryptographyMaterialProvidersTypes.IKeyring = None
        nw5_ = FailingKeyring()
        nw5_.ctor__()
        res = nw5_
        return res
        return res


class StaticKeyring(AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._encryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        self._decryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.StaticKeyring"
    def OnDecrypt(self, input):
        out260_: Wrappers.Result
        out260_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out260_

    def OnEncrypt(self, input):
        out261_: Wrappers.Result
        out261_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out261_

    def ctor__(self, encryptionMaterials, decryptionMaterials):
        (self)._encryptionMaterials = encryptionMaterials
        (self)._decryptionMaterials = decryptionMaterials

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).encryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(((self).encryptionMaterials).value))
            return res
        elif True:
            d_676_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_676_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_676_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_677_exception_: AwsCryptographyMaterialProvidersTypes.Error
            d_677_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_677_exception_)
            return res
        return res

    @property
    def encryptionMaterials(self):
        return self._encryptionMaterials
    @property
    def decryptionMaterials(self):
        return self._decryptionMaterials

class FailingKeyring(AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.FailingKeyring"
    def OnDecrypt(self, input):
        out262_: Wrappers.Result
        out262_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out262_

    def OnEncrypt(self, input):
        out263_: Wrappers.Result
        out263_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out263_

    def ctor__(self):
        pass
        pass

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_678_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_678_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_678_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_679_exception_: AwsCryptographyMaterialProvidersTypes.Error
        d_679_exception_ = AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_679_exception_)
        return res
        return res

