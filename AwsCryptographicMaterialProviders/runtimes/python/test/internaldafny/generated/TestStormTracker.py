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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
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
import TestLocalCMC

# Module: TestStormTracker

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
    def StormTrackerBasics():
        d_721_st_: StormTracker.StormTracker
        nw10_ = StormTracker.StormTracker()
        nw10_.ctor__(StormTracker.default__.DefaultStorm())
        d_721_st_ = nw10_
        d_722_abc_: _dafny.Seq
        d_722_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_723_cde_: _dafny.Seq
        d_723_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_724_res_: StormTracker.CacheState
        d_725_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out290_: Wrappers.Result
        out290_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10000)
        d_725_valueOrError0_ = out290_
        if not(not((d_725_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,12): " + _dafny.string_of(d_725_valueOrError0_))
        d_724_res_ = (d_725_valueOrError0_).Extract()
        if not((d_724_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_726_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out291_: Wrappers.Result
        out291_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10000)
        d_726_valueOrError1_ = out291_
        if not(not((d_726_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,8): " + _dafny.string_of(d_726_valueOrError1_))
        d_724_res_ = (d_726_valueOrError1_).Extract()
        if not((d_724_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_727_res2_: tuple
        d_728_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out292_: Wrappers.Result
        out292_ = (d_721_st_).PutCacheEntry(default__.MakePut(d_722_abc_, 10000))
        d_728_valueOrError2_ = out292_
        if not(not((d_728_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,13): " + _dafny.string_of(d_728_valueOrError2_))
        d_727_res2_ = (d_728_valueOrError2_).Extract()
        d_729_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out293_: Wrappers.Result
        out293_ = (d_721_st_).PutCacheEntry(default__.MakePut(d_723_cde_, 10000))
        d_729_valueOrError3_ = out293_
        if not(not((d_729_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,9): " + _dafny.string_of(d_729_valueOrError3_))
        d_727_res2_ = (d_729_valueOrError3_).Extract()
        d_730_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out294_: Wrappers.Result
        out294_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10001)
        d_730_valueOrError4_ = out294_
        if not(not((d_730_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,8): " + _dafny.string_of(d_730_valueOrError4_))
        d_724_res_ = (d_730_valueOrError4_).Extract()
        if not((d_724_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_731_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out295_: Wrappers.Result
        out295_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10001)
        d_731_valueOrError5_ = out295_
        if not(not((d_731_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,8): " + _dafny.string_of(d_731_valueOrError5_))
        d_724_res_ = (d_731_valueOrError5_).Extract()
        if not((d_724_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_732_res3_: Wrappers.Result
        out296_: Wrappers.Result
        out296_ = (d_721_st_).GetCacheEntry(default__.MakeGet(d_722_abc_))
        d_732_res3_ = out296_
        out297_: Wrappers.Result
        out297_ = (d_721_st_).GetCacheEntry(default__.MakeGet(d_722_abc_))
        d_732_res3_ = out297_
        d_733_res4_: Wrappers.Result
        out298_: Wrappers.Result
        out298_ = (d_721_st_).GetFromCache(default__.MakeGet(d_722_abc_))
        d_733_res4_ = out298_
        out299_: Wrappers.Result
        out299_ = (d_721_st_).GetFromCache(default__.MakeGet(d_722_abc_))
        d_733_res4_ = out299_
        d_734_res5_: Wrappers.Result
        out300_: Wrappers.Result
        out300_ = (d_721_st_).DeleteCacheEntry(default__.MakeDel(d_722_abc_))
        d_734_res5_ = out300_
        out301_: Wrappers.Result
        out301_ = (d_721_st_).DeleteCacheEntry(default__.MakeDel(d_722_abc_))
        d_734_res5_ = out301_

    @staticmethod
    def StormTrackerFanOut():
        d_735_st_: StormTracker.StormTracker
        nw11_ = StormTracker.StormTracker()
        def iife24_(_pat_let11_0):
            def iife25_(d_736_dt__update__tmp_h0_):
                def iife26_(_pat_let12_0):
                    def iife27_(d_737_dt__update_hfanOut_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_736_dt__update__tmp_h0_).entryCapacity, (d_736_dt__update__tmp_h0_).entryPruningTailSize, (d_736_dt__update__tmp_h0_).gracePeriod, (d_736_dt__update__tmp_h0_).graceInterval, d_737_dt__update_hfanOut_h0_, (d_736_dt__update__tmp_h0_).inFlightTTL, (d_736_dt__update__tmp_h0_).sleepMilli)
                    return iife27_(_pat_let12_0)
                return iife26_(3)
            return iife25_(_pat_let11_0)
        nw11_.ctor__(iife24_(StormTracker.default__.DefaultStorm()))
        d_735_st_ = nw11_
        d_738_one_: _dafny.Seq
        d_738_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_739_two_: _dafny.Seq
        d_739_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_740_three_: _dafny.Seq
        d_740_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_741_four_: _dafny.Seq
        d_741_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_742_res_: StormTracker.CacheState
        d_743_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out302_: Wrappers.Result
        out302_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_738_one_), 10000)
        d_743_valueOrError0_ = out302_
        if not(not((d_743_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,12): " + _dafny.string_of(d_743_valueOrError0_))
        d_742_res_ = (d_743_valueOrError0_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_744_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out303_: Wrappers.Result
        out303_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_739_two_), 10000)
        d_744_valueOrError1_ = out303_
        if not(not((d_744_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,8): " + _dafny.string_of(d_744_valueOrError1_))
        d_742_res_ = (d_744_valueOrError1_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_745_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out304_: Wrappers.Result
        out304_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_740_three_), 10000)
        d_745_valueOrError2_ = out304_
        if not(not((d_745_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,8): " + _dafny.string_of(d_745_valueOrError2_))
        d_742_res_ = (d_745_valueOrError2_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_746_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out305_: Wrappers.Result
        out305_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_741_four_), 10000)
        d_746_valueOrError3_ = out305_
        if not(not((d_746_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,8): " + _dafny.string_of(d_746_valueOrError3_))
        d_742_res_ = (d_746_valueOrError3_).Extract()
        if not((d_742_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerTTL():
        d_747_st_: StormTracker.StormTracker
        nw12_ = StormTracker.StormTracker()
        def iife28_(_pat_let13_0):
            def iife29_(d_748_dt__update__tmp_h0_):
                def iife30_(_pat_let14_0):
                    def iife31_(d_749_dt__update_hinFlightTTL_h0_):
                        def iife32_(_pat_let15_0):
                            def iife33_(d_750_dt__update_hfanOut_h0_):
                                return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_748_dt__update__tmp_h0_).entryCapacity, (d_748_dt__update__tmp_h0_).entryPruningTailSize, (d_748_dt__update__tmp_h0_).gracePeriod, (d_748_dt__update__tmp_h0_).graceInterval, d_750_dt__update_hfanOut_h0_, d_749_dt__update_hinFlightTTL_h0_, (d_748_dt__update__tmp_h0_).sleepMilli)
                            return iife33_(_pat_let15_0)
                        return iife32_(3)
                    return iife31_(_pat_let14_0)
                return iife30_(5)
            return iife29_(_pat_let13_0)
        nw12_.ctor__(iife28_(StormTracker.default__.DefaultStorm()))
        d_747_st_ = nw12_
        d_751_one_: _dafny.Seq
        d_751_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_752_two_: _dafny.Seq
        d_752_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_753_three_: _dafny.Seq
        d_753_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_754_four_: _dafny.Seq
        d_754_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_755_res_: StormTracker.CacheState
        d_756_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out306_: Wrappers.Result
        out306_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_751_one_), 10000)
        d_756_valueOrError0_ = out306_
        if not(not((d_756_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,12): " + _dafny.string_of(d_756_valueOrError0_))
        d_755_res_ = (d_756_valueOrError0_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_757_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out307_: Wrappers.Result
        out307_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_752_two_), 10000)
        d_757_valueOrError1_ = out307_
        if not(not((d_757_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,8): " + _dafny.string_of(d_757_valueOrError1_))
        d_755_res_ = (d_757_valueOrError1_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_758_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out308_: Wrappers.Result
        out308_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_753_three_), 10000)
        d_758_valueOrError2_ = out308_
        if not(not((d_758_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,8): " + _dafny.string_of(d_758_valueOrError2_))
        d_755_res_ = (d_758_valueOrError2_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_759_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out309_: Wrappers.Result
        out309_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10000)
        d_759_valueOrError3_ = out309_
        if not(not((d_759_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,8): " + _dafny.string_of(d_759_valueOrError3_))
        d_755_res_ = (d_759_valueOrError3_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_760_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out310_: Wrappers.Result
        out310_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10001)
        d_760_valueOrError4_ = out310_
        if not(not((d_760_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,8): " + _dafny.string_of(d_760_valueOrError4_))
        d_755_res_ = (d_760_valueOrError4_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_761_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out311_: Wrappers.Result
        out311_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10003)
        d_761_valueOrError5_ = out311_
        if not(not((d_761_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,8): " + _dafny.string_of(d_761_valueOrError5_))
        d_755_res_ = (d_761_valueOrError5_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_762_valueOrError6_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out312_: Wrappers.Result
        out312_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10005)
        d_762_valueOrError6_ = out312_
        if not(not((d_762_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,8): " + _dafny.string_of(d_762_valueOrError6_))
        d_755_res_ = (d_762_valueOrError6_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(116,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGraceInterval():
        d_763_st_: StormTracker.StormTracker
        nw13_ = StormTracker.StormTracker()
        def iife34_(_pat_let16_0):
            def iife35_(d_764_dt__update__tmp_h0_):
                def iife36_(_pat_let17_0):
                    def iife37_(d_765_dt__update_hgraceInterval_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache((d_764_dt__update__tmp_h0_).entryCapacity, (d_764_dt__update__tmp_h0_).entryPruningTailSize, (d_764_dt__update__tmp_h0_).gracePeriod, d_765_dt__update_hgraceInterval_h0_, (d_764_dt__update__tmp_h0_).fanOut, (d_764_dt__update__tmp_h0_).inFlightTTL, (d_764_dt__update__tmp_h0_).sleepMilli)
                    return iife37_(_pat_let17_0)
                return iife36_(3)
            return iife35_(_pat_let16_0)
        nw13_.ctor__(iife34_(StormTracker.default__.DefaultStorm()))
        d_763_st_ = nw13_
        d_766_one_: _dafny.Seq
        d_766_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_767_res_: StormTracker.CacheState
        d_768_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out313_: Wrappers.Result
        out313_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10000)
        d_768_valueOrError0_ = out313_
        if not(not((d_768_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,12): " + _dafny.string_of(d_768_valueOrError0_))
        d_767_res_ = (d_768_valueOrError0_).Extract()
        if not((d_767_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_769_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out314_: Wrappers.Result
        out314_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10000)
        d_769_valueOrError1_ = out314_
        if not(not((d_769_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,8): " + _dafny.string_of(d_769_valueOrError1_))
        d_767_res_ = (d_769_valueOrError1_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_770_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out315_: Wrappers.Result
        out315_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10001)
        d_770_valueOrError2_ = out315_
        if not(not((d_770_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,8): " + _dafny.string_of(d_770_valueOrError2_))
        d_767_res_ = (d_770_valueOrError2_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_771_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out316_: Wrappers.Result
        out316_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10002)
        d_771_valueOrError3_ = out316_
        if not(not((d_771_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,8): " + _dafny.string_of(d_771_valueOrError3_))
        d_767_res_ = (d_771_valueOrError3_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_772_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out317_: Wrappers.Result
        out317_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10003)
        d_772_valueOrError4_ = out317_
        if not(not((d_772_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,8): " + _dafny.string_of(d_772_valueOrError4_))
        d_767_res_ = (d_772_valueOrError4_).Extract()
        if not((d_767_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGracePeriod():
        d_773_st_: StormTracker.StormTracker
        nw14_ = StormTracker.StormTracker()
        nw14_.ctor__(StormTracker.default__.DefaultStorm())
        d_773_st_ = nw14_
        d_774_one_: _dafny.Seq
        d_774_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_775_res2_: tuple
        d_776_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out318_: Wrappers.Result
        out318_ = (d_773_st_).PutCacheEntry(default__.MakePut(d_774_one_, 10010))
        d_776_valueOrError0_ = out318_
        if not(not((d_776_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,13): " + _dafny.string_of(d_776_valueOrError0_))
        d_775_res2_ = (d_776_valueOrError0_).Extract()
        d_777_res_: StormTracker.CacheState
        d_778_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out319_: Wrappers.Result
        out319_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 9999)
        d_778_valueOrError1_ = out319_
        if not(not((d_778_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,12): " + _dafny.string_of(d_778_valueOrError1_))
        d_777_res_ = (d_778_valueOrError1_).Extract()
        if not((d_777_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_779_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out320_: Wrappers.Result
        out320_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 10000)
        d_779_valueOrError2_ = out320_
        if not(not((d_779_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,8): " + _dafny.string_of(d_779_valueOrError2_))
        d_777_res_ = (d_779_valueOrError2_).Extract()
        if not((d_777_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_780_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out321_: Wrappers.Result
        out321_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 10000)
        d_780_valueOrError3_ = out321_
        if not(not((d_780_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,8): " + _dafny.string_of(d_780_valueOrError3_))
        d_777_res_ = (d_780_valueOrError3_).Extract()
        if not((d_777_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

