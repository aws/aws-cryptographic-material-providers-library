import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
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
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
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
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying
import TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring
import TestAwsKmsEncryptedDataKeyFilter

assert "TestLocalCMC" == __name__
TestLocalCMC = sys.modules[__name__]

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
        return software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(data, TestLocalCMC.default__.MakeMat(data), 123456789, expiryTime, Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def LocalCMCBasics():
        d_2126_st_: LocalCMC.LocalCMC
        nw83_ = LocalCMC.LocalCMC()
        nw83_.ctor__(100, 1)
        d_2126_st_ = nw83_
        d_2127_abc_: _dafny.Seq
        d_2127_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_2128_cde_: _dafny.Seq
        d_2128_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_2129_res_: Wrappers.Result
        out580_: Wrappers.Result
        out580_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2127_abc_), 10000)
        d_2129_res_ = out580_
        if not((d_2129_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2129_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2130_res2_: tuple
        d_2131_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out581_: Wrappers.Result
        out581_ = (d_2126_st_).PutCacheEntry_k(TestLocalCMC.default__.MakePut(d_2127_abc_, 10000))
        d_2131_valueOrError0_ = out581_
        if not(not((d_2131_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(59,13): " + _dafny.string_of(d_2131_valueOrError0_))
        d_2130_res2_ = (d_2131_valueOrError0_).Extract()
        d_2132_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out582_: Wrappers.Result
        out582_ = (d_2126_st_).PutCacheEntry_k(TestLocalCMC.default__.MakePut(d_2128_cde_, 10000))
        d_2132_valueOrError1_ = out582_
        if not(not((d_2132_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(60,9): " + _dafny.string_of(d_2132_valueOrError1_))
        d_2130_res2_ = (d_2132_valueOrError1_).Extract()
        d_2133_res3_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput
        d_2134_valueOrError2_: Wrappers.Result = None
        out583_: Wrappers.Result
        out583_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2127_abc_), 9999)
        d_2134_valueOrError2_ = out583_
        if not(not((d_2134_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(62,13): " + _dafny.string_of(d_2134_valueOrError2_))
        d_2133_res3_ = (d_2134_valueOrError2_).Extract()
        d_2135_valueOrError3_: Wrappers.Result = None
        out584_: Wrappers.Result
        out584_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2127_abc_), 10000)
        d_2135_valueOrError3_ = out584_
        if not(not((d_2135_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(63,9): " + _dafny.string_of(d_2135_valueOrError3_))
        d_2133_res3_ = (d_2135_valueOrError3_).Extract()
        out585_: Wrappers.Result
        out585_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2127_abc_), 10001)
        d_2129_res_ = out585_
        if not((d_2129_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2129_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2136_valueOrError4_: Wrappers.Result = None
        out586_: Wrappers.Result
        out586_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2128_cde_), 9999)
        d_2136_valueOrError4_ = out586_
        if not(not((d_2136_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,9): " + _dafny.string_of(d_2136_valueOrError4_))
        d_2133_res3_ = (d_2136_valueOrError4_).Extract()
        d_2137_res5_: tuple
        d_2138_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out587_: Wrappers.Result
        out587_ = (d_2126_st_).DeleteCacheEntry_k(TestLocalCMC.default__.MakeDel(d_2128_cde_))
        d_2138_valueOrError5_ = out587_
        if not(not((d_2138_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(69,13): " + _dafny.string_of(d_2138_valueOrError5_))
        d_2137_res5_ = (d_2138_valueOrError5_).Extract()
        out588_: Wrappers.Result
        out588_ = (d_2126_st_).GetCacheEntryWithTime(TestLocalCMC.default__.MakeGet(d_2127_abc_), 9999)
        d_2129_res_ = out588_
        if not((d_2129_res_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2129_res_).error).is_EntryDoesNotExist):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2139_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out589_: Wrappers.Result
        out589_ = (d_2126_st_).DeleteCacheEntry_k(TestLocalCMC.default__.MakeDel(d_2128_cde_))
        d_2139_valueOrError6_ = out589_
        if not(not((d_2139_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,9): " + _dafny.string_of(d_2139_valueOrError6_))
        d_2137_res5_ = (d_2139_valueOrError6_).Extract()

