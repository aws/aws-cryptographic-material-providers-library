import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import Relations
import Seq_MergeSort
import Math
import Seq
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import UUID
import Time
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import Base64
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import AesKdfCtr
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring

# Module: TestRawRSAKeying

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_484_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_485_valueOrError0_: Wrappers.Result = None
        out196_: Wrappers.Result
        out196_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_485_valueOrError0_ = out196_
        if not(not((d_485_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(18,15): " + _dafny.string_of(d_485_valueOrError0_))
        d_484_mpl_ = (d_485_valueOrError0_).Extract()
        d_486_namespace_: _dafny.Seq
        d_487_name_: _dafny.Seq
        out197_: _dafny.Seq
        out198_: _dafny.Seq
        out197_, out198_ = TestUtils.default__.NamespaceAndName(0)
        d_486_namespace_ = out197_
        d_487_name_ = out198_
        d_488_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out199_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out199_ = default__.GenerateKeyPair(2048)
        d_488_keys_ = out199_
        d_489_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_490_valueOrError1_: Wrappers.Result = None
        out200_: Wrappers.Result
        out200_ = (d_484_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_486_namespace_, d_487_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_488_keys_).publicKey).pem), Wrappers.Option_Some(((d_488_keys_).privateKey).pem)))
        d_490_valueOrError1_ = out200_
        if not(not((d_490_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(22,25): " + _dafny.string_of(d_490_valueOrError1_))
        d_489_rawRSAKeyring_ = (d_490_valueOrError1_).Extract()
        d_491_encryptionContext_: _dafny.Map
        out201_: _dafny.Map
        out201_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_491_encryptionContext_ = out201_
        d_492_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_492_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_493_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_494_valueOrError2_: Wrappers.Result = None
        d_494_valueOrError2_ = (d_484_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_492_algorithmSuiteId_, d_491_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_494_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(35,33): " + _dafny.string_of(d_494_valueOrError2_))
        d_493_encryptionMaterialsIn_ = (d_494_valueOrError2_).Extract()
        d_495_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_496_valueOrError3_: Wrappers.Result = None
        out202_: Wrappers.Result
        out202_ = (d_489_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_493_encryptionMaterialsIn_))
        d_496_valueOrError3_ = out202_
        if not(not((d_496_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(45,34): " + _dafny.string_of(d_496_valueOrError3_))
        d_495_encryptionMaterialsOut_ = (d_496_valueOrError3_).Extract()
        d_497___v0_: tuple
        d_498_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_498_valueOrError4_ = (d_484_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_495_encryptionMaterialsOut_).materials)
        if not(not((d_498_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(48,13): " + _dafny.string_of(d_498_valueOrError4_))
        d_497___v0_ = (d_498_valueOrError4_).Extract()
        d_499_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_499_edk_ = (((d_495_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_500_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_501_valueOrError5_: Wrappers.Result = None
        d_501_valueOrError5_ = (d_484_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_492_algorithmSuiteId_, d_491_encryptionContext_, _dafny.Seq([])))
        if not(not((d_501_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(52,33): " + _dafny.string_of(d_501_valueOrError5_))
        d_500_decryptionMaterialsIn_ = (d_501_valueOrError5_).Extract()
        d_502_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_503_valueOrError6_: Wrappers.Result = None
        out203_: Wrappers.Result
        out203_ = (d_489_rawRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_500_decryptionMaterialsIn_, _dafny.Seq([d_499_edk_])))
        d_503_valueOrError6_ = out203_
        if not(not((d_503_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(60,34): " + _dafny.string_of(d_503_valueOrError6_))
        d_502_decryptionMaterialsOut_ = (d_503_valueOrError6_).Extract()
        if not((((d_502_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_495_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_504_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_505_valueOrError0_: Wrappers.Result = None
        out204_: Wrappers.Result
        out204_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_505_valueOrError0_ = out204_
        if not(not((d_505_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(78,15): " + _dafny.string_of(d_505_valueOrError0_))
        d_504_mpl_ = (d_505_valueOrError0_).Extract()
        d_506_namespace_: _dafny.Seq
        d_507_name_: _dafny.Seq
        out205_: _dafny.Seq
        out206_: _dafny.Seq
        out205_, out206_ = TestUtils.default__.NamespaceAndName(0)
        d_506_namespace_ = out205_
        d_507_name_ = out206_
        d_508_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out207_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out207_ = default__.GenerateKeyPair(2048)
        d_508_keys_ = out207_
        d_509_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_510_valueOrError1_: Wrappers.Result = None
        out208_: Wrappers.Result
        out208_ = (d_504_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_506_namespace_, d_507_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_508_keys_).publicKey).pem), Wrappers.Option_Some(((d_508_keys_).privateKey).pem)))
        d_510_valueOrError1_ = out208_
        if not(not((d_510_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(82,25): " + _dafny.string_of(d_510_valueOrError1_))
        d_509_rawRSAKeyring_ = (d_510_valueOrError1_).Extract()
        d_511_mismatchedRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_512_valueOrError2_: Wrappers.Result = None
        out209_: Wrappers.Result
        out209_ = (d_504_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_506_namespace_, _dafny.Seq("mismatched"), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_508_keys_).publicKey).pem), Wrappers.Option_Some(((d_508_keys_).privateKey).pem)))
        d_512_valueOrError2_ = out209_
        if not(not((d_512_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(90,32): " + _dafny.string_of(d_512_valueOrError2_))
        d_511_mismatchedRSAKeyring_ = (d_512_valueOrError2_).Extract()
        d_513_encryptionContext_: _dafny.Map
        out210_: _dafny.Map
        out210_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_513_encryptionContext_ = out210_
        d_514_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_514_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_515_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_516_valueOrError3_: Wrappers.Result = None
        d_516_valueOrError3_ = (d_504_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_514_algorithmSuiteId_, d_513_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_516_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(103,33): " + _dafny.string_of(d_516_valueOrError3_))
        d_515_encryptionMaterialsIn_ = (d_516_valueOrError3_).Extract()
        d_517_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_518_valueOrError4_: Wrappers.Result = None
        out211_: Wrappers.Result
        out211_ = (d_509_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_515_encryptionMaterialsIn_))
        d_518_valueOrError4_ = out211_
        if not(not((d_518_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(112,34): " + _dafny.string_of(d_518_valueOrError4_))
        d_517_encryptionMaterialsOut_ = (d_518_valueOrError4_).Extract()
        d_519___v1_: tuple
        d_520_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_520_valueOrError5_ = (d_504_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_517_encryptionMaterialsOut_).materials)
        if not(not((d_520_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(115,13): " + _dafny.string_of(d_520_valueOrError5_))
        d_519___v1_ = (d_520_valueOrError5_).Extract()
        d_521_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_521_edk_ = (((d_517_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_522_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_523_valueOrError6_: Wrappers.Result = None
        d_523_valueOrError6_ = (d_504_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_514_algorithmSuiteId_, d_513_encryptionContext_, _dafny.Seq([])))
        if not(not((d_523_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(119,33): " + _dafny.string_of(d_523_valueOrError6_))
        d_522_decryptionMaterialsIn_ = (d_523_valueOrError6_).Extract()
        d_524_decryptionMaterialsOut_: Wrappers.Result
        out212_: Wrappers.Result
        out212_ = (d_511_mismatchedRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_522_decryptionMaterialsIn_, _dafny.Seq([d_521_edk_])))
        d_524_decryptionMaterialsOut_ = out212_
        if not((d_524_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(133,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptFailure():
        d_525_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_526_valueOrError0_: Wrappers.Result = None
        out213_: Wrappers.Result
        out213_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_526_valueOrError0_ = out213_
        if not(not((d_526_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,15): " + _dafny.string_of(d_526_valueOrError0_))
        d_525_mpl_ = (d_526_valueOrError0_).Extract()
        d_527_namespace_: _dafny.Seq
        d_528_name_: _dafny.Seq
        out214_: _dafny.Seq
        out215_: _dafny.Seq
        out214_, out215_ = TestUtils.default__.NamespaceAndName(0)
        d_527_namespace_ = out214_
        d_528_name_ = out215_
        d_529_encryptKeys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out216_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out216_ = default__.GenerateKeyPair(2048)
        d_529_encryptKeys_ = out216_
        d_530_decryptKeys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out217_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out217_ = default__.GenerateKeyPair(2048)
        d_530_decryptKeys_ = out217_
        d_531_encryptKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_532_valueOrError1_: Wrappers.Result = None
        out218_: Wrappers.Result
        out218_ = (d_525_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_527_namespace_, d_528_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_529_encryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_529_encryptKeys_).privateKey).pem)))
        d_532_valueOrError1_ = out218_
        if not(not((d_532_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(147,26): " + _dafny.string_of(d_532_valueOrError1_))
        d_531_encryptKeyring_ = (d_532_valueOrError1_).Extract()
        d_533_decryptKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_534_valueOrError2_: Wrappers.Result = None
        out219_: Wrappers.Result
        out219_ = (d_525_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_527_namespace_, d_528_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_530_decryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_530_decryptKeys_).privateKey).pem)))
        d_534_valueOrError2_ = out219_
        if not(not((d_534_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(155,26): " + _dafny.string_of(d_534_valueOrError2_))
        d_533_decryptKeyring_ = (d_534_valueOrError2_).Extract()
        d_535_encryptionContext_: _dafny.Map
        out220_: _dafny.Map
        out220_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_535_encryptionContext_ = out220_
        d_536_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_536_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_537_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_538_valueOrError3_: Wrappers.Result = None
        d_538_valueOrError3_ = (d_525_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_536_algorithmSuiteId_, d_535_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_538_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(166,33): " + _dafny.string_of(d_538_valueOrError3_))
        d_537_encryptionMaterialsIn_ = (d_538_valueOrError3_).Extract()
        d_539_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_540_valueOrError4_: Wrappers.Result = None
        out221_: Wrappers.Result
        out221_ = (d_531_encryptKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_537_encryptionMaterialsIn_))
        d_540_valueOrError4_ = out221_
        if not(not((d_540_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(175,34): " + _dafny.string_of(d_540_valueOrError4_))
        d_539_encryptionMaterialsOut_ = (d_540_valueOrError4_).Extract()
        d_541___v2_: tuple
        d_542_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_542_valueOrError5_ = (d_525_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_539_encryptionMaterialsOut_).materials)
        if not(not((d_542_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(178,13): " + _dafny.string_of(d_542_valueOrError5_))
        d_541___v2_ = (d_542_valueOrError5_).Extract()
        d_543_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_543_edk_ = (((d_539_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_544_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_545_valueOrError6_: Wrappers.Result = None
        d_545_valueOrError6_ = (d_525_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_536_algorithmSuiteId_, d_535_encryptionContext_, _dafny.Seq([])))
        if not(not((d_545_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(182,33): " + _dafny.string_of(d_545_valueOrError6_))
        d_544_decryptionMaterialsIn_ = (d_545_valueOrError6_).Extract()
        d_546_decryptionMaterialsOut_: Wrappers.Result
        out222_: Wrappers.Result
        out222_ = (d_533_decryptKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_544_decryptionMaterialsIn_, _dafny.Seq([d_543_edk_])))
        d_546_decryptionMaterialsOut_ = out222_
        if not((d_546_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_547_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_548_valueOrError0_: Wrappers.Result = None
        out223_: Wrappers.Result
        out223_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_548_valueOrError0_ = out223_
        if not(not((d_548_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(212,15): " + _dafny.string_of(d_548_valueOrError0_))
        d_547_mpl_ = (d_548_valueOrError0_).Extract()
        d_549_namespace_: _dafny.Seq
        d_550_name_: _dafny.Seq
        out224_: _dafny.Seq
        out225_: _dafny.Seq
        out224_, out225_ = TestUtils.default__.NamespaceAndName(0)
        d_549_namespace_ = out224_
        d_550_name_ = out225_
        d_551_keys_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out226_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput
        out226_ = default__.GenerateKeyPair(2048)
        d_551_keys_ = out226_
        d_552_rawRSAKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_553_valueOrError1_: Wrappers.Result = None
        out227_: Wrappers.Result
        out227_ = (d_547_mpl_).CreateRawRsaKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_549_namespace_, d_550_name_, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_551_keys_).publicKey).pem), Wrappers.Option_Some(((d_551_keys_).privateKey).pem)))
        d_553_valueOrError1_ = out227_
        if not(not((d_553_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(216,25): " + _dafny.string_of(d_553_valueOrError1_))
        d_552_rawRSAKeyring_ = (d_553_valueOrError1_).Extract()
        d_554_encryptionContext_: _dafny.Map
        out228_: _dafny.Map
        out228_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_554_encryptionContext_ = out228_
        d_555_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_555_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_556_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_557_valueOrError2_: Wrappers.Result = None
        d_557_valueOrError2_ = (d_547_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_555_algorithmSuiteId_, d_554_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_557_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(229,33): " + _dafny.string_of(d_557_valueOrError2_))
        d_556_encryptionMaterialsIn_ = (d_557_valueOrError2_).Extract()
        d_558_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_559_valueOrError3_: Wrappers.Result = None
        out229_: Wrappers.Result
        out229_ = (d_552_rawRSAKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_556_encryptionMaterialsIn_))
        d_559_valueOrError3_ = out229_
        if not(not((d_559_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(238,34): " + _dafny.string_of(d_559_valueOrError3_))
        d_558_encryptionMaterialsOut_ = (d_559_valueOrError3_).Extract()
        d_560___v3_: tuple
        d_561_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_561_valueOrError4_ = (d_547_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_558_encryptionMaterialsOut_).materials)
        if not(not((d_561_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(241,13): " + _dafny.string_of(d_561_valueOrError4_))
        d_560___v3_ = (d_561_valueOrError4_).Extract()
        d_562_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_562_edk_ = (((d_558_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_563_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_564_valueOrError5_: Wrappers.Result = None
        d_564_valueOrError5_ = (d_547_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_555_algorithmSuiteId_, d_554_encryptionContext_, _dafny.Seq([])))
        if not(not((d_564_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(245,33): " + _dafny.string_of(d_564_valueOrError5_))
        d_563_decryptionMaterialsIn_ = (d_564_valueOrError5_).Extract()
        d_565_fakeEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_565_fakeEdk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((d_562_edk_).keyProviderId, (d_562_edk_).keyProviderInfo, _dafny.Seq([0 for d_566_i_ in range(len((d_562_edk_).ciphertext))]))
        d_567_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_568_valueOrError6_: Wrappers.Result = None
        out230_: Wrappers.Result
        out230_ = (d_552_rawRSAKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_563_decryptionMaterialsIn_, _dafny.Seq([d_565_fakeEdk_, d_562_edk_])))
        d_568_valueOrError6_ = out230_
        if not(not((d_568_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(262,34): " + _dafny.string_of(d_568_valueOrError6_))
        d_567_decryptionMaterialsOut_ = (d_568_valueOrError6_).Extract()
        if not((((d_567_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_558_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(273,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GenerateKeyPair(keyModulusLength):
        keys: software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput = None
        d_569_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_570_valueOrError0_: Wrappers.Result = None
        out231_: Wrappers.Result
        out231_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_570_valueOrError0_ = out231_
        if not(not((d_570_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(280,18): " + _dafny.string_of(d_570_valueOrError0_))
        d_569_crypto_ = (d_570_valueOrError0_).Extract()
        d_571_valueOrError1_: Wrappers.Result = None
        out232_: Wrappers.Result
        out232_ = (d_569_crypto_).GenerateRSAKeyPair(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(keyModulusLength))
        d_571_valueOrError1_ = out232_
        if not(not((d_571_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(282,12): " + _dafny.string_of(d_571_valueOrError1_))
        keys = (d_571_valueOrError1_).Extract()
        return keys

