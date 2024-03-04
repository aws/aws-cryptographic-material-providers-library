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
import TestRawRSAKeying
import TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring
import TestAwsKmsEncryptedDataKeyFilter

# Module: TestLocalCMC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MakeMat(data):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials_BranchKeyMaterials(_dafny.Seq("spoo"), data, _dafny.Map({}), data))

    @staticmethod
    def MakeGet(data):
        return software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(data, Wrappers.Option_None())

    @staticmethod
    def MakeDel(data):
        return software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput(data)

    @staticmethod
    def MakePut(data, expiryTime):
        return software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(data, default__.MakeMat(data), 123456789, expiryTime, Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def LocalCMCBasics():
        d_707_st_: LocalCMC.LocalCMC
        nw9_ = LocalCMC.LocalCMC()
        nw9_.ctor__(100, 1)
        d_707_st_ = nw9_
        d_708_abc_: _dafny.Seq
        d_708_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_709_cde_: _dafny.Seq
        d_709_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_710_res_: Wrappers.Result
        out280_: Wrappers.Result
        out280_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_708_abc_), 10000)
        d_710_res_ = out280_
        if not((d_710_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_710_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_711_res2_: tuple
        d_712_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out281_: Wrappers.Result
        out281_ = (d_707_st_).PutCacheEntry_k(default__.MakePut(d_708_abc_, 10000))
        d_712_valueOrError0_ = out281_
        if not(not((d_712_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(59,13): " + _dafny.string_of(d_712_valueOrError0_))
        d_711_res2_ = (d_712_valueOrError0_).Extract()
        d_713_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out282_: Wrappers.Result
        out282_ = (d_707_st_).PutCacheEntry_k(default__.MakePut(d_709_cde_, 10000))
        d_713_valueOrError1_ = out282_
        if not(not((d_713_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(60,9): " + _dafny.string_of(d_713_valueOrError1_))
        d_711_res2_ = (d_713_valueOrError1_).Extract()
        d_714_res3_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput
        d_715_valueOrError2_: Wrappers.Result = None
        out283_: Wrappers.Result
        out283_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_708_abc_), 9999)
        d_715_valueOrError2_ = out283_
        if not(not((d_715_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(62,13): " + _dafny.string_of(d_715_valueOrError2_))
        d_714_res3_ = (d_715_valueOrError2_).Extract()
        d_716_valueOrError3_: Wrappers.Result = None
        out284_: Wrappers.Result
        out284_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_708_abc_), 10000)
        d_716_valueOrError3_ = out284_
        if not(not((d_716_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(63,9): " + _dafny.string_of(d_716_valueOrError3_))
        d_714_res3_ = (d_716_valueOrError3_).Extract()
        out285_: Wrappers.Result
        out285_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_708_abc_), 10001)
        d_710_res_ = out285_
        if not((d_710_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_710_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_717_valueOrError4_: Wrappers.Result = None
        out286_: Wrappers.Result
        out286_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_709_cde_), 9999)
        d_717_valueOrError4_ = out286_
        if not(not((d_717_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,9): " + _dafny.string_of(d_717_valueOrError4_))
        d_714_res3_ = (d_717_valueOrError4_).Extract()
        d_718_res5_: tuple
        d_719_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out287_: Wrappers.Result
        out287_ = (d_707_st_).DeleteCacheEntry_k(default__.MakeDel(d_709_cde_))
        d_719_valueOrError5_ = out287_
        if not(not((d_719_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(69,13): " + _dafny.string_of(d_719_valueOrError5_))
        d_718_res5_ = (d_719_valueOrError5_).Extract()
        out288_: Wrappers.Result
        out288_ = (d_707_st_).GetCacheEntryWithTime(default__.MakeGet(d_708_abc_), 9999)
        d_710_res_ = out288_
        if not((d_710_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_710_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_720_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out289_: Wrappers.Result
        out289_ = (d_707_st_).DeleteCacheEntry_k(default__.MakeDel(d_709_cde_))
        d_720_valueOrError6_ = out289_
        if not(not((d_720_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,9): " + _dafny.string_of(d_720_valueOrError6_))
        d_718_res5_ = (d_720_valueOrError6_).Extract()

