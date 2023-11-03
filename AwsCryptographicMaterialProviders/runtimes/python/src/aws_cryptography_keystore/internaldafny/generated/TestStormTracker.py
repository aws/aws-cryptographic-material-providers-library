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
import TestLocalCMC

assert "TestStormTracker" == __name__
TestStormTracker = sys.modules[__name__]

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
        return software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(data, TestStormTracker.default__.MakeMat(data), 123456789, expiryTime, Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def StormTrackerBasics():
        d_2140_st_: StormTracker.StormTracker
        nw84_ = StormTracker.StormTracker()
        nw84_.ctor__(StormTracker.default__.DefaultStorm())
        d_2140_st_ = nw84_
        d_2141_abc_: _dafny.Seq
        d_2141_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_2142_cde_: _dafny.Seq
        d_2142_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_2143_res_: StormTracker.CacheState
        d_2144_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out590_: Wrappers.Result
        out590_ = (d_2140_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2141_abc_), 10000)
        d_2144_valueOrError0_ = out590_
        if not(not((d_2144_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,12): " + _dafny.string_of(d_2144_valueOrError0_))
        d_2143_res_ = (d_2144_valueOrError0_).Extract()
        if not((d_2143_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2145_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out591_: Wrappers.Result
        out591_ = (d_2140_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2141_abc_), 10000)
        d_2145_valueOrError1_ = out591_
        if not(not((d_2145_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,8): " + _dafny.string_of(d_2145_valueOrError1_))
        d_2143_res_ = (d_2145_valueOrError1_).Extract()
        if not((d_2143_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2146_res2_: tuple
        d_2147_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out592_: Wrappers.Result
        out592_ = (d_2140_st_).PutCacheEntry(TestStormTracker.default__.MakePut(d_2141_abc_, 10000))
        d_2147_valueOrError2_ = out592_
        if not(not((d_2147_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,13): " + _dafny.string_of(d_2147_valueOrError2_))
        d_2146_res2_ = (d_2147_valueOrError2_).Extract()
        d_2148_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out593_: Wrappers.Result
        out593_ = (d_2140_st_).PutCacheEntry(TestStormTracker.default__.MakePut(d_2142_cde_, 10000))
        d_2148_valueOrError3_ = out593_
        if not(not((d_2148_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,9): " + _dafny.string_of(d_2148_valueOrError3_))
        d_2146_res2_ = (d_2148_valueOrError3_).Extract()
        d_2149_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out594_: Wrappers.Result
        out594_ = (d_2140_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2141_abc_), 10001)
        d_2149_valueOrError4_ = out594_
        if not(not((d_2149_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,8): " + _dafny.string_of(d_2149_valueOrError4_))
        d_2143_res_ = (d_2149_valueOrError4_).Extract()
        if not((d_2143_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2150_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out595_: Wrappers.Result
        out595_ = (d_2140_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2141_abc_), 10001)
        d_2150_valueOrError5_ = out595_
        if not(not((d_2150_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,8): " + _dafny.string_of(d_2150_valueOrError5_))
        d_2143_res_ = (d_2150_valueOrError5_).Extract()
        if not((d_2143_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2151_res3_: Wrappers.Result
        out596_: Wrappers.Result
        out596_ = (d_2140_st_).GetCacheEntry(TestStormTracker.default__.MakeGet(d_2141_abc_))
        d_2151_res3_ = out596_
        out597_: Wrappers.Result
        out597_ = (d_2140_st_).GetCacheEntry(TestStormTracker.default__.MakeGet(d_2141_abc_))
        d_2151_res3_ = out597_
        d_2152_res4_: Wrappers.Result
        out598_: Wrappers.Result
        out598_ = (d_2140_st_).GetFromCache(TestStormTracker.default__.MakeGet(d_2141_abc_))
        d_2152_res4_ = out598_
        out599_: Wrappers.Result
        out599_ = (d_2140_st_).GetFromCache(TestStormTracker.default__.MakeGet(d_2141_abc_))
        d_2152_res4_ = out599_
        d_2153_res5_: Wrappers.Result
        out600_: Wrappers.Result
        out600_ = (d_2140_st_).DeleteCacheEntry(TestStormTracker.default__.MakeDel(d_2141_abc_))
        d_2153_res5_ = out600_
        out601_: Wrappers.Result
        out601_ = (d_2140_st_).DeleteCacheEntry(TestStormTracker.default__.MakeDel(d_2141_abc_))
        d_2153_res5_ = out601_

    @staticmethod
    def StormTrackerFanOut():
        d_2154_st_: StormTracker.StormTracker
        nw85_ = StormTracker.StormTracker()
        def iife85_(_pat_let36_0):
            def iife86_(d_2155_dt__update__tmp_h0_):
                def iife87_(_pat_let37_0):
                    def iife88_(d_2156_dt__update_hfanOut_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_2155_dt__update__tmp_h0_).entryCapacity, (d_2155_dt__update__tmp_h0_).entryPruningTailSize, (d_2155_dt__update__tmp_h0_).gracePeriod, (d_2155_dt__update__tmp_h0_).graceInterval, d_2156_dt__update_hfanOut_h0_, (d_2155_dt__update__tmp_h0_).inFlightTTL, (d_2155_dt__update__tmp_h0_).sleepMilli)
                    return iife88_(_pat_let37_0)
                return iife87_(3)
            return iife86_(_pat_let36_0)
        nw85_.ctor__(iife85_(StormTracker.default__.DefaultStorm()))
        d_2154_st_ = nw85_
        d_2157_one_: _dafny.Seq
        d_2157_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_2158_two_: _dafny.Seq
        d_2158_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_2159_three_: _dafny.Seq
        d_2159_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_2160_four_: _dafny.Seq
        d_2160_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_2161_res_: StormTracker.CacheState
        d_2162_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out602_: Wrappers.Result
        out602_ = (d_2154_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2157_one_), 10000)
        d_2162_valueOrError0_ = out602_
        if not(not((d_2162_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,12): " + _dafny.string_of(d_2162_valueOrError0_))
        d_2161_res_ = (d_2162_valueOrError0_).Extract()
        if not((d_2161_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2163_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out603_: Wrappers.Result
        out603_ = (d_2154_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2158_two_), 10000)
        d_2163_valueOrError1_ = out603_
        if not(not((d_2163_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,8): " + _dafny.string_of(d_2163_valueOrError1_))
        d_2161_res_ = (d_2163_valueOrError1_).Extract()
        if not((d_2161_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2164_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out604_: Wrappers.Result
        out604_ = (d_2154_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2159_three_), 10000)
        d_2164_valueOrError2_ = out604_
        if not(not((d_2164_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,8): " + _dafny.string_of(d_2164_valueOrError2_))
        d_2161_res_ = (d_2164_valueOrError2_).Extract()
        if not((d_2161_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2165_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out605_: Wrappers.Result
        out605_ = (d_2154_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2160_four_), 10000)
        d_2165_valueOrError3_ = out605_
        if not(not((d_2165_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,8): " + _dafny.string_of(d_2165_valueOrError3_))
        d_2161_res_ = (d_2165_valueOrError3_).Extract()
        if not((d_2161_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerTTL():
        d_2166_st_: StormTracker.StormTracker
        nw86_ = StormTracker.StormTracker()
        def iife89_(_pat_let38_0):
            def iife90_(d_2167_dt__update__tmp_h0_):
                def iife91_(_pat_let39_0):
                    def iife92_(d_2168_dt__update_hinFlightTTL_h0_):
                        def iife93_(_pat_let40_0):
                            def iife94_(d_2169_dt__update_hfanOut_h0_):
                                return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_2167_dt__update__tmp_h0_).entryCapacity, (d_2167_dt__update__tmp_h0_).entryPruningTailSize, (d_2167_dt__update__tmp_h0_).gracePeriod, (d_2167_dt__update__tmp_h0_).graceInterval, d_2169_dt__update_hfanOut_h0_, d_2168_dt__update_hinFlightTTL_h0_, (d_2167_dt__update__tmp_h0_).sleepMilli)
                            return iife94_(_pat_let40_0)
                        return iife93_(3)
                    return iife92_(_pat_let39_0)
                return iife91_(5)
            return iife90_(_pat_let38_0)
        nw86_.ctor__(iife89_(StormTracker.default__.DefaultStorm()))
        d_2166_st_ = nw86_
        d_2170_one_: _dafny.Seq
        d_2170_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_2171_two_: _dafny.Seq
        d_2171_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_2172_three_: _dafny.Seq
        d_2172_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_2173_four_: _dafny.Seq
        d_2173_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_2174_res_: StormTracker.CacheState
        d_2175_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out606_: Wrappers.Result
        out606_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2170_one_), 10000)
        d_2175_valueOrError0_ = out606_
        if not(not((d_2175_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,12): " + _dafny.string_of(d_2175_valueOrError0_))
        d_2174_res_ = (d_2175_valueOrError0_).Extract()
        if not((d_2174_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2176_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out607_: Wrappers.Result
        out607_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2171_two_), 10000)
        d_2176_valueOrError1_ = out607_
        if not(not((d_2176_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,8): " + _dafny.string_of(d_2176_valueOrError1_))
        d_2174_res_ = (d_2176_valueOrError1_).Extract()
        if not((d_2174_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2177_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out608_: Wrappers.Result
        out608_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2172_three_), 10000)
        d_2177_valueOrError2_ = out608_
        if not(not((d_2177_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,8): " + _dafny.string_of(d_2177_valueOrError2_))
        d_2174_res_ = (d_2177_valueOrError2_).Extract()
        if not((d_2174_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2178_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out609_: Wrappers.Result
        out609_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2173_four_), 10000)
        d_2178_valueOrError3_ = out609_
        if not(not((d_2178_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,8): " + _dafny.string_of(d_2178_valueOrError3_))
        d_2174_res_ = (d_2178_valueOrError3_).Extract()
        if not((d_2174_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2179_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out610_: Wrappers.Result
        out610_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2173_four_), 10001)
        d_2179_valueOrError4_ = out610_
        if not(not((d_2179_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,8): " + _dafny.string_of(d_2179_valueOrError4_))
        d_2174_res_ = (d_2179_valueOrError4_).Extract()
        if not((d_2174_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2180_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out611_: Wrappers.Result
        out611_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2173_four_), 10003)
        d_2180_valueOrError5_ = out611_
        if not(not((d_2180_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,8): " + _dafny.string_of(d_2180_valueOrError5_))
        d_2174_res_ = (d_2180_valueOrError5_).Extract()
        if not((d_2174_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2181_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out612_: Wrappers.Result
        out612_ = (d_2166_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2173_four_), 10005)
        d_2181_valueOrError6_ = out612_
        if not(not((d_2181_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,8): " + _dafny.string_of(d_2181_valueOrError6_))
        d_2174_res_ = (d_2181_valueOrError6_).Extract()
        if not((d_2174_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(116,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGraceInterval():
        d_2182_st_: StormTracker.StormTracker
        nw87_ = StormTracker.StormTracker()
        def iife95_(_pat_let41_0):
            def iife96_(d_2183_dt__update__tmp_h0_):
                def iife97_(_pat_let42_0):
                    def iife98_(d_2184_dt__update_hgraceInterval_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_2183_dt__update__tmp_h0_).entryCapacity, (d_2183_dt__update__tmp_h0_).entryPruningTailSize, (d_2183_dt__update__tmp_h0_).gracePeriod, d_2184_dt__update_hgraceInterval_h0_, (d_2183_dt__update__tmp_h0_).fanOut, (d_2183_dt__update__tmp_h0_).inFlightTTL, (d_2183_dt__update__tmp_h0_).sleepMilli)
                    return iife98_(_pat_let42_0)
                return iife97_(3)
            return iife96_(_pat_let41_0)
        nw87_.ctor__(iife95_(StormTracker.default__.DefaultStorm()))
        d_2182_st_ = nw87_
        d_2185_one_: _dafny.Seq
        d_2185_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_2186_res_: StormTracker.CacheState
        d_2187_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out613_: Wrappers.Result
        out613_ = (d_2182_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2185_one_), 10000)
        d_2187_valueOrError0_ = out613_
        if not(not((d_2187_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,12): " + _dafny.string_of(d_2187_valueOrError0_))
        d_2186_res_ = (d_2187_valueOrError0_).Extract()
        if not((d_2186_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2188_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out614_: Wrappers.Result
        out614_ = (d_2182_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2185_one_), 10000)
        d_2188_valueOrError1_ = out614_
        if not(not((d_2188_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,8): " + _dafny.string_of(d_2188_valueOrError1_))
        d_2186_res_ = (d_2188_valueOrError1_).Extract()
        if not((d_2186_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2189_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out615_: Wrappers.Result
        out615_ = (d_2182_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2185_one_), 10001)
        d_2189_valueOrError2_ = out615_
        if not(not((d_2189_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,8): " + _dafny.string_of(d_2189_valueOrError2_))
        d_2186_res_ = (d_2189_valueOrError2_).Extract()
        if not((d_2186_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2190_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out616_: Wrappers.Result
        out616_ = (d_2182_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2185_one_), 10002)
        d_2190_valueOrError3_ = out616_
        if not(not((d_2190_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,8): " + _dafny.string_of(d_2190_valueOrError3_))
        d_2186_res_ = (d_2190_valueOrError3_).Extract()
        if not((d_2186_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2191_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out617_: Wrappers.Result
        out617_ = (d_2182_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2185_one_), 10003)
        d_2191_valueOrError4_ = out617_
        if not(not((d_2191_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,8): " + _dafny.string_of(d_2191_valueOrError4_))
        d_2186_res_ = (d_2191_valueOrError4_).Extract()
        if not((d_2186_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGracePeriod():
        d_2192_st_: StormTracker.StormTracker
        nw88_ = StormTracker.StormTracker()
        nw88_.ctor__(StormTracker.default__.DefaultStorm())
        d_2192_st_ = nw88_
        d_2193_one_: _dafny.Seq
        d_2193_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_2194_res2_: tuple
        d_2195_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out618_: Wrappers.Result
        out618_ = (d_2192_st_).PutCacheEntry(TestStormTracker.default__.MakePut(d_2193_one_, 10010))
        d_2195_valueOrError0_ = out618_
        if not(not((d_2195_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,13): " + _dafny.string_of(d_2195_valueOrError0_))
        d_2194_res2_ = (d_2195_valueOrError0_).Extract()
        d_2196_res_: StormTracker.CacheState
        d_2197_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out619_: Wrappers.Result
        out619_ = (d_2192_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2193_one_), 9999)
        d_2197_valueOrError1_ = out619_
        if not(not((d_2197_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,12): " + _dafny.string_of(d_2197_valueOrError1_))
        d_2196_res_ = (d_2197_valueOrError1_).Extract()
        if not((d_2196_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2198_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out620_: Wrappers.Result
        out620_ = (d_2192_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2193_one_), 10000)
        d_2198_valueOrError2_ = out620_
        if not(not((d_2198_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,8): " + _dafny.string_of(d_2198_valueOrError2_))
        d_2196_res_ = (d_2198_valueOrError2_).Extract()
        if not((d_2196_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2199_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        out621_: Wrappers.Result
        out621_ = (d_2192_st_).GetFromCacheWithTime(TestStormTracker.default__.MakeGet(d_2193_one_), 10000)
        d_2199_valueOrError3_ = out621_
        if not(not((d_2199_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,8): " + _dafny.string_of(d_2199_valueOrError3_))
        d_2196_res_ = (d_2199_valueOrError3_).Extract()
        if not((d_2196_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

