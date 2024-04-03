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

# Module: TestMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getInputEncryptionMaterials(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_389_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_390_valueOrError0_: Wrappers.Result = None
        out134_: Wrappers.Result
        out134_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_390_valueOrError0_ = out134_
        if not(not((d_390_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(18,15): " + _dafny.string_of(d_390_valueOrError0_))
        d_389_mpl_ = (d_390_valueOrError0_).Extract()
        d_391_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_391_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_392_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_393_valueOrError1_: Wrappers.Result = None
        d_393_valueOrError1_ = (d_389_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_391_algorithmSuiteId_, encryptionContext, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_393_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(21,33): " + _dafny.string_of(d_393_valueOrError1_))
        d_392_encryptionMaterialsIn_ = (d_393_valueOrError1_).Extract()
        res = d_392_encryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def getInputDecryptionMaterials(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        d_394_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_395_valueOrError0_: Wrappers.Result = None
        out135_: Wrappers.Result
        out135_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_395_valueOrError0_ = out135_
        if not(not((d_395_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(35,15): " + _dafny.string_of(d_395_valueOrError0_))
        d_394_mpl_ = (d_395_valueOrError0_).Extract()
        d_396_algorithmSuiteId_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId
        d_396_algorithmSuiteId_ = software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_397_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_398_valueOrError1_: Wrappers.Result = None
        d_398_valueOrError1_ = (d_394_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_396_algorithmSuiteId_, encryptionContext, _dafny.Seq([])))
        if not(not((d_398_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(38,33): " + _dafny.string_of(d_398_valueOrError1_))
        d_397_decryptionMaterialsIn_ = (d_398_valueOrError1_).Extract()
        res = d_397_decryptionMaterialsIn_
        return res
        return res

    @staticmethod
    def TestHappyCase():
        d_399_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_400_valueOrError0_: Wrappers.Result = None
        out136_: Wrappers.Result
        out136_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_400_valueOrError0_ = out136_
        if not(not((d_400_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(51,15): " + _dafny.string_of(d_400_valueOrError0_))
        d_399_mpl_ = (d_400_valueOrError0_).Extract()
        d_401_encryptionContext_: _dafny.Map
        out137_: _dafny.Map
        out137_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_401_encryptionContext_ = out137_
        d_402_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out138_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out138_ = default__.getInputEncryptionMaterials(d_401_encryptionContext_)
        d_402_encryptionMaterials_ = out138_
        d_403_decryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out139_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out139_ = default__.getInputDecryptionMaterials(d_401_encryptionContext_)
        d_403_decryptionMaterials_ = out139_
        d_404_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out140_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out140_ = default__.setupRawAesKeyring(d_401_encryptionContext_)
        d_404_rawAESKeyring_ = out140_
        d_405_expectedEncryptionMaterials_: Wrappers.Result
        out141_: Wrappers.Result
        out141_ = (d_404_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_402_encryptionMaterials_))
        d_405_expectedEncryptionMaterials_ = out141_
        if not((d_405_expectedEncryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_406_expectedPlaintextDataKey_: Wrappers.Option
        d_406_expectedPlaintextDataKey_ = (((d_405_expectedEncryptionMaterials_).value).materials).plaintextDataKey
        if not((d_406_expectedPlaintextDataKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_407_staticKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out142_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out142_ = default__.SetupStaticKeyring(Wrappers.Option_Some(((d_405_expectedEncryptionMaterials_).value).materials), Wrappers.Option_None())
        d_407_staticKeyring_ = out142_
        d_408_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_409_valueOrError1_: Wrappers.Result = None
        out143_: Wrappers.Result
        out143_ = (d_399_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_407_staticKeyring_), _dafny.Seq([d_404_rawAESKeyring_])))
        d_409_valueOrError1_ = out143_
        if not(not((d_409_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(69,24): " + _dafny.string_of(d_409_valueOrError1_))
        d_408_multiKeyring_ = (d_409_valueOrError1_).Extract()
        d_410_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_411_valueOrError2_: Wrappers.Result = None
        out144_: Wrappers.Result
        out144_ = (d_408_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_402_encryptionMaterials_))
        d_411_valueOrError2_ = out144_
        if not(not((d_411_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(74,34): " + _dafny.string_of(d_411_valueOrError2_))
        d_410_encryptionMaterialsOut_ = (d_411_valueOrError2_).Extract()
        d_412___v0_: tuple
        d_413_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_413_valueOrError3_ = (d_399_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_410_encryptionMaterialsOut_).materials)
        if not(not((d_413_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(76,13): " + _dafny.string_of(d_413_valueOrError3_))
        d_412___v0_ = (d_413_valueOrError3_).Extract()
        if not(((((d_410_encryptionMaterialsOut_).materials).plaintextDataKey).value) == ((d_406_expectedPlaintextDataKey_).value)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_410_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (2)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestChildKeyringFailureEncrypt():
        d_414_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_415_valueOrError0_: Wrappers.Result = None
        out145_: Wrappers.Result
        out145_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_415_valueOrError0_ = out145_
        if not(not((d_415_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(106,15): " + _dafny.string_of(d_415_valueOrError0_))
        d_414_mpl_ = (d_415_valueOrError0_).Extract()
        d_416_encryptionContext_: _dafny.Map
        out146_: _dafny.Map
        out146_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_416_encryptionContext_ = out146_
        d_417_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out147_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out147_ = default__.setupRawAesKeyring(d_416_encryptionContext_)
        d_417_rawAESKeyring_ = out147_
        d_418_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out148_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out148_ = default__.SetupFailingKeyring()
        d_418_failingKeyring_ = out148_
        d_419_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_420_valueOrError1_: Wrappers.Result = None
        out149_: Wrappers.Result
        out149_ = (d_414_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_417_rawAESKeyring_), _dafny.Seq([d_418_failingKeyring_])))
        d_420_valueOrError1_ = out149_
        if not(not((d_420_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(116,24): " + _dafny.string_of(d_420_valueOrError1_))
        d_419_multiKeyring_ = (d_420_valueOrError1_).Extract()
        d_421_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out150_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out150_ = default__.getInputEncryptionMaterials(d_416_encryptionContext_)
        d_421_encryptionMaterials_ = out150_
        d_422_result_: Wrappers.Result
        out151_: Wrappers.Result
        out151_ = (d_419_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_421_encryptionMaterials_))
        d_422_result_ = out151_
        if not((d_422_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(124,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringFails():
        d_423_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_424_valueOrError0_: Wrappers.Result = None
        out152_: Wrappers.Result
        out152_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_424_valueOrError0_ = out152_
        if not(not((d_424_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(129,15): " + _dafny.string_of(d_424_valueOrError0_))
        d_423_mpl_ = (d_424_valueOrError0_).Extract()
        d_425_encryptionContext_: _dafny.Map
        out153_: _dafny.Map
        out153_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_425_encryptionContext_ = out153_
        d_426_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out154_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out154_ = default__.SetupFailingKeyring()
        d_426_failingKeyring_ = out154_
        d_427_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out155_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out155_ = default__.setupRawAesKeyring(d_425_encryptionContext_)
        d_427_rawAESKeyring_ = out155_
        d_428_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_429_valueOrError1_: Wrappers.Result = None
        out156_: Wrappers.Result
        out156_ = (d_423_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_426_failingKeyring_), _dafny.Seq([d_427_rawAESKeyring_])))
        d_429_valueOrError1_ = out156_
        if not(not((d_429_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(142,24): " + _dafny.string_of(d_429_valueOrError1_))
        d_428_multiKeyring_ = (d_429_valueOrError1_).Extract()
        d_430_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out157_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out157_ = default__.getInputEncryptionMaterials(d_425_encryptionContext_)
        d_430_encryptionMaterials_ = out157_
        d_431_result_: Wrappers.Result
        out158_: Wrappers.Result
        out158_ = (d_428_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_430_encryptionMaterials_))
        d_431_result_ = out158_
        if not((d_431_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorKeyringDoesNotReturnPlaintextDataKey():
        d_432_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_433_valueOrError0_: Wrappers.Result = None
        out159_: Wrappers.Result
        out159_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_433_valueOrError0_ = out159_
        if not(not((d_433_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(155,15): " + _dafny.string_of(d_433_valueOrError0_))
        d_432_mpl_ = (d_433_valueOrError0_).Extract()
        d_434_encryptionContext_: _dafny.Map
        out160_: _dafny.Map
        out160_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_434_encryptionContext_ = out160_
        d_435_encryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out161_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out161_ = default__.getInputEncryptionMaterials(d_434_encryptionContext_)
        d_435_encryptionMaterials_ = out161_
        d_436_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out162_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out162_ = default__.SetupStaticKeyring(Wrappers.Option_Some(d_435_encryptionMaterials_), Wrappers.Option_None())
        d_436_failingKeyring_ = out162_
        d_437_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_438_valueOrError1_: Wrappers.Result = None
        out163_: Wrappers.Result
        out163_ = (d_432_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_436_failingKeyring_), _dafny.Seq([])))
        d_438_valueOrError1_ = out163_
        if not(not((d_438_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(165,24): " + _dafny.string_of(d_438_valueOrError1_))
        d_437_multiKeyring_ = (d_438_valueOrError1_).Extract()
        d_439_result_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = (d_437_multiKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_435_encryptionMaterials_))
        d_439_result_ = out164_
        if not((d_439_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorAbleToDecrypt():
        d_440_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_441_valueOrError0_: Wrappers.Result = None
        out165_: Wrappers.Result
        out165_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_441_valueOrError0_ = out165_
        if not(not((d_441_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(176,15): " + _dafny.string_of(d_441_valueOrError0_))
        d_440_mpl_ = (d_441_valueOrError0_).Extract()
        d_442_encryptionContext_: _dafny.Map
        out166_: _dafny.Map
        out166_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_442_encryptionContext_ = out166_
        d_443_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out167_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out167_ = default__.setupRawAesKeyring(d_442_encryptionContext_)
        d_443_rawAESKeyring_ = out167_
        d_444_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out168_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out168_ = default__.getInputEncryptionMaterials(d_442_encryptionContext_)
        d_444_inputEncryptionMaterials_ = out168_
        d_445_encryptionMaterials_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = (d_443_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_444_inputEncryptionMaterials_))
        d_445_encryptionMaterials_ = out169_
        if not((d_445_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(190,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_446_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out170_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out170_ = default__.getInputDecryptionMaterials(d_442_encryptionContext_)
        d_446_inputDecryptionMaterials_ = out170_
        d_447_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out171_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out171_ = default__.SetupFailingKeyring()
        d_447_failingKeyring_ = out171_
        d_448_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_449_valueOrError1_: Wrappers.Result = None
        out172_: Wrappers.Result
        out172_ = (d_440_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_443_rawAESKeyring_), _dafny.Seq([d_447_failingKeyring_])))
        d_449_valueOrError1_ = out172_
        if not(not((d_449_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(196,24): " + _dafny.string_of(d_449_valueOrError1_))
        d_448_multiKeyring_ = (d_449_valueOrError1_).Extract()
        d_450_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_450_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_446_inputDecryptionMaterials_, (((d_445_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_451_decryptionMaterials_: Wrappers.Result
        out173_: Wrappers.Result
        out173_ = (d_448_multiKeyring_).OnDecrypt(d_450_onDecryptInput_)
        d_451_decryptionMaterials_ = out173_
        if not((d_451_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_451_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_445_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGeneratorUnableToDecrypt():
        d_452_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_453_valueOrError0_: Wrappers.Result = None
        out174_: Wrappers.Result
        out174_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_453_valueOrError0_ = out174_
        if not(not((d_453_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(212,15): " + _dafny.string_of(d_453_valueOrError0_))
        d_452_mpl_ = (d_453_valueOrError0_).Extract()
        d_454_encryptionContext_: _dafny.Map
        out175_: _dafny.Map
        out175_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_454_encryptionContext_ = out175_
        d_455_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out176_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out176_ = default__.setupRawAesKeyring(d_454_encryptionContext_)
        d_455_rawAESKeyring_ = out176_
        d_456_inputEncryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out177_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out177_ = default__.getInputEncryptionMaterials(d_454_encryptionContext_)
        d_456_inputEncryptionMaterials_ = out177_
        d_457_encryptionMaterials_: Wrappers.Result
        out178_: Wrappers.Result
        out178_ = (d_455_rawAESKeyring_).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(d_456_inputEncryptionMaterials_))
        d_457_encryptionMaterials_ = out178_
        if not((d_457_encryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(237,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_458_inputDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out179_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        out179_ = default__.getInputDecryptionMaterials(d_454_encryptionContext_)
        d_458_inputDecryptionMaterials_ = out179_
        d_459_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out180_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out180_ = default__.SetupFailingKeyring()
        d_459_failingKeyring_ = out180_
        d_460_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_461_valueOrError1_: Wrappers.Result = None
        out181_: Wrappers.Result
        out181_ = (d_452_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_Some(d_459_failingKeyring_), _dafny.Seq([d_459_failingKeyring_, d_455_rawAESKeyring_, d_459_failingKeyring_])))
        d_461_valueOrError1_ = out181_
        if not(not((d_461_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(245,24): " + _dafny.string_of(d_461_valueOrError1_))
        d_460_multiKeyring_ = (d_461_valueOrError1_).Extract()
        d_462_onDecryptInput_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput
        d_462_onDecryptInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_458_inputDecryptionMaterials_, (((d_457_encryptionMaterials_).value).materials).encryptedDataKeys)
        d_463_decryptionMaterials_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = (d_460_multiKeyring_).OnDecrypt(d_462_onDecryptInput_)
        d_463_decryptionMaterials_ = out182_
        if not((d_463_decryptionMaterials_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_463_decryptionMaterials_).value).materials).plaintextDataKey) == ((((d_457_encryptionMaterials_).value).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(266,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCollectFailuresDecrypt():
        d_464_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_465_valueOrError0_: Wrappers.Result = None
        out183_: Wrappers.Result
        out183_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_465_valueOrError0_ = out183_
        if not(not((d_465_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(272,15): " + _dafny.string_of(d_465_valueOrError0_))
        d_464_mpl_ = (d_465_valueOrError0_).Extract()
        d_466_encryptionContext_: _dafny.Map
        out184_: _dafny.Map
        out184_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_466_encryptionContext_ = out184_
        d_467_failingKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out185_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        out185_ = default__.SetupFailingKeyring()
        d_467_failingKeyring_ = out185_
        d_468_multiKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_469_valueOrError1_: Wrappers.Result = None
        out186_: Wrappers.Result
        out186_ = (d_464_mpl_).CreateMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None(), _dafny.Seq([d_467_failingKeyring_, d_467_failingKeyring_])))
        d_469_valueOrError1_ = out186_
        if not(not((d_469_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(291,24): " + _dafny.string_of(d_469_valueOrError1_))
        d_468_multiKeyring_ = (d_469_valueOrError1_).Extract()
        d_470_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_471_valueOrError2_: Wrappers.Result = None
        d_471_valueOrError2_ = (d_464_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), d_466_encryptionContext_, _dafny.Seq([])))
        if not(not((d_471_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(296,21): " + _dafny.string_of(d_471_valueOrError2_))
        d_470_materials_ = (d_471_valueOrError2_).Extract()
        d_472_result_: Wrappers.Result
        out187_: Wrappers.Result
        out187_ = (d_468_multiKeyring_).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_470_materials_, _dafny.Seq([])))
        d_472_result_ = out187_
        if not((d_472_result_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def setupRawAesKeyring(encryptionContext):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        d_473_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_474_valueOrError0_: Wrappers.Result = None
        out188_: Wrappers.Result
        out188_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_474_valueOrError0_ = out188_
        if not(not((d_474_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(313,15): " + _dafny.string_of(d_474_valueOrError0_))
        d_473_mpl_ = (d_474_valueOrError0_).Extract()
        d_475_namespace_: _dafny.Seq
        d_476_name_: _dafny.Seq
        out189_: _dafny.Seq
        out190_: _dafny.Seq
        out189_, out190_ = TestUtils.default__.NamespaceAndName(0)
        d_475_namespace_ = out189_
        d_476_name_ = out190_
        d_477_rawAESKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_478_valueOrError1_: Wrappers.Result = None
        out191_: Wrappers.Result
        out191_ = (d_473_mpl_).CreateRawAesKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_475_namespace_, d_476_name_, _dafny.Seq([0 for d_479_i_ in range(32)]), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_478_valueOrError1_ = out191_
        if not(not((d_478_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestMultiKeyring.dfy(316,25): " + _dafny.string_of(d_478_valueOrError1_))
        d_477_rawAESKeyring_ = (d_478_valueOrError1_).Extract()
        res = d_477_rawAESKeyring_
        return res
        return res

    @staticmethod
    def SetupStaticKeyring(encryptionMaterials, decryptionMaterials):
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        nw4_ = StaticKeyring()
        nw4_.ctor__(encryptionMaterials, decryptionMaterials)
        res = nw4_
        return res
        return res

    @staticmethod
    def SetupFailingKeyring():
        res: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        nw5_ = FailingKeyring()
        nw5_.ctor__()
        res = nw5_
        return res
        return res


class StaticKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._encryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        self._decryptionMaterials: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.StaticKeyring"
    def OnEncrypt(self, input):
        out192_: Wrappers.Result
        out192_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out192_

    def OnDecrypt(self, input):
        out193_: Wrappers.Result
        out193_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out193_

    def ctor__(self, encryptionMaterials, decryptionMaterials):
        (self)._encryptionMaterials = encryptionMaterials
        (self)._decryptionMaterials = decryptionMaterials

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).encryptionMaterials).is_Some:
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(((self).encryptionMaterials).value))
            return res
        elif True:
            d_480_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_480_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_480_exception_)
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).decryptionMaterials).is_Some:
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(((self).decryptionMaterials).value))
            return res
        elif True:
            d_481_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
            d_481_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
            res = Wrappers.Result_Failure(d_481_exception_)
            return res
        return res

    @property
    def encryptionMaterials(self):
        return self._encryptionMaterials
    @property
    def decryptionMaterials(self):
        return self._decryptionMaterials

class FailingKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestMultiKeyring.FailingKeyring"
    def OnEncrypt(self, input):
        out194_: Wrappers.Result
        out194_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out194_

    def OnDecrypt(self, input):
        out195_: Wrappers.Result
        out195_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out195_

    def ctor__(self):
        pass
        pass

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_482_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_482_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_482_exception_)
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_483_exception_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_483_exception_ = software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Failure"))
        res = Wrappers.Result_Failure(d_483_exception_)
        return res
        return res

