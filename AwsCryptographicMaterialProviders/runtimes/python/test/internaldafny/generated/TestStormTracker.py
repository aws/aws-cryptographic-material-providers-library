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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
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
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
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
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
import TestAwsKmsEncryptedDataKeyFilter as TestAwsKmsEncryptedDataKeyFilter
import TestLocalCMC as TestLocalCMC

# Module: TestStormTracker

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MakeMat(data):
        return AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(AwsCryptographyKeyStoreTypes.BranchKeyMaterials_BranchKeyMaterials(_dafny.Seq("spoo"), data, _dafny.Map({}), data))

    @staticmethod
    def MakeGet(data):
        return AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(data, Wrappers.Option_None())

    @staticmethod
    def MakeDel(data):
        return AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput(data)

    @staticmethod
    def MakePut(data, expiryTime):
        return AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(data, default__.MakeMat(data), 123456789, expiryTime, Wrappers.Option_None(), Wrappers.Option_None())

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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,15): " + _dafny.string_of(d_725_valueOrError0_))
        d_724_res_ = (d_725_valueOrError0_).Extract()
        if not((d_724_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_726_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out291_: Wrappers.Result
        out291_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10000)
        d_726_valueOrError1_ = out291_
        if not(not((d_726_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,11): " + _dafny.string_of(d_726_valueOrError1_))
        d_724_res_ = (d_726_valueOrError1_).Extract()
        if not((d_724_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_727_res2_: tuple
        d_728_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out292_: Wrappers.Result
        out292_ = (d_721_st_).PutCacheEntry(default__.MakePut(d_722_abc_, 10000))
        d_728_valueOrError2_ = out292_
        if not(not((d_728_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,16): " + _dafny.string_of(d_728_valueOrError2_))
        d_727_res2_ = (d_728_valueOrError2_).Extract()
        d_729_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out293_: Wrappers.Result
        out293_ = (d_721_st_).PutCacheEntry(default__.MakePut(d_723_cde_, 10000))
        d_729_valueOrError3_ = out293_
        if not(not((d_729_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,12): " + _dafny.string_of(d_729_valueOrError3_))
        d_727_res2_ = (d_729_valueOrError3_).Extract()
        d_730_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out294_: Wrappers.Result
        out294_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10001)
        d_730_valueOrError4_ = out294_
        if not(not((d_730_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,11): " + _dafny.string_of(d_730_valueOrError4_))
        d_724_res_ = (d_730_valueOrError4_).Extract()
        if not((d_724_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_731_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out295_: Wrappers.Result
        out295_ = (d_721_st_).GetFromCacheWithTime(default__.MakeGet(d_722_abc_), 10001)
        d_731_valueOrError5_ = out295_
        if not(not((d_731_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,11): " + _dafny.string_of(d_731_valueOrError5_))
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
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_736_dt__update__tmp_h0_).entryCapacity, (d_736_dt__update__tmp_h0_).entryPruningTailSize, (d_736_dt__update__tmp_h0_).gracePeriod, (d_736_dt__update__tmp_h0_).graceInterval, d_737_dt__update_hfanOut_h0_, (d_736_dt__update__tmp_h0_).inFlightTTL, (d_736_dt__update__tmp_h0_).sleepMilli)
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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,15): " + _dafny.string_of(d_743_valueOrError0_))
        d_742_res_ = (d_743_valueOrError0_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_744_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out303_: Wrappers.Result
        out303_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_739_two_), 10000)
        d_744_valueOrError1_ = out303_
        if not(not((d_744_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,11): " + _dafny.string_of(d_744_valueOrError1_))
        d_742_res_ = (d_744_valueOrError1_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_745_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out304_: Wrappers.Result
        out304_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_740_three_), 10000)
        d_745_valueOrError2_ = out304_
        if not(not((d_745_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,11): " + _dafny.string_of(d_745_valueOrError2_))
        d_742_res_ = (d_745_valueOrError2_).Extract()
        if not((d_742_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_746_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out305_: Wrappers.Result
        out305_ = (d_735_st_).GetFromCacheWithTime(default__.MakeGet(d_741_four_), 10000)
        d_746_valueOrError3_ = out305_
        if not(not((d_746_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,11): " + _dafny.string_of(d_746_valueOrError3_))
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
                                return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_748_dt__update__tmp_h0_).entryCapacity, (d_748_dt__update__tmp_h0_).entryPruningTailSize, (d_748_dt__update__tmp_h0_).gracePeriod, (d_748_dt__update__tmp_h0_).graceInterval, d_750_dt__update_hfanOut_h0_, d_749_dt__update_hinFlightTTL_h0_, (d_748_dt__update__tmp_h0_).sleepMilli)
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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,15): " + _dafny.string_of(d_756_valueOrError0_))
        d_755_res_ = (d_756_valueOrError0_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_757_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out307_: Wrappers.Result
        out307_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_752_two_), 10000)
        d_757_valueOrError1_ = out307_
        if not(not((d_757_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,11): " + _dafny.string_of(d_757_valueOrError1_))
        d_755_res_ = (d_757_valueOrError1_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_758_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out308_: Wrappers.Result
        out308_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_753_three_), 10000)
        d_758_valueOrError2_ = out308_
        if not(not((d_758_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + _dafny.string_of(d_758_valueOrError2_))
        d_755_res_ = (d_758_valueOrError2_).Extract()
        if not((d_755_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_759_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out309_: Wrappers.Result
        out309_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10000)
        d_759_valueOrError3_ = out309_
        if not(not((d_759_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,11): " + _dafny.string_of(d_759_valueOrError3_))
        d_755_res_ = (d_759_valueOrError3_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_760_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out310_: Wrappers.Result
        out310_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10001)
        d_760_valueOrError4_ = out310_
        if not(not((d_760_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,11): " + _dafny.string_of(d_760_valueOrError4_))
        d_755_res_ = (d_760_valueOrError4_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_761_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out311_: Wrappers.Result
        out311_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10003)
        d_761_valueOrError5_ = out311_
        if not(not((d_761_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,11): " + _dafny.string_of(d_761_valueOrError5_))
        d_755_res_ = (d_761_valueOrError5_).Extract()
        if not((d_755_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_762_valueOrError6_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out312_: Wrappers.Result
        out312_ = (d_747_st_).GetFromCacheWithTime(default__.MakeGet(d_754_four_), 10005)
        d_762_valueOrError6_ = out312_
        if not(not((d_762_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,11): " + _dafny.string_of(d_762_valueOrError6_))
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
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_764_dt__update__tmp_h0_).entryCapacity, (d_764_dt__update__tmp_h0_).entryPruningTailSize, (d_764_dt__update__tmp_h0_).gracePeriod, d_765_dt__update_hgraceInterval_h0_, (d_764_dt__update__tmp_h0_).fanOut, (d_764_dt__update__tmp_h0_).inFlightTTL, (d_764_dt__update__tmp_h0_).sleepMilli)
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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,15): " + _dafny.string_of(d_768_valueOrError0_))
        d_767_res_ = (d_768_valueOrError0_).Extract()
        if not((d_767_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_769_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out314_: Wrappers.Result
        out314_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10000)
        d_769_valueOrError1_ = out314_
        if not(not((d_769_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,11): " + _dafny.string_of(d_769_valueOrError1_))
        d_767_res_ = (d_769_valueOrError1_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_770_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out315_: Wrappers.Result
        out315_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10001)
        d_770_valueOrError2_ = out315_
        if not(not((d_770_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,11): " + _dafny.string_of(d_770_valueOrError2_))
        d_767_res_ = (d_770_valueOrError2_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_771_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out316_: Wrappers.Result
        out316_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10002)
        d_771_valueOrError3_ = out316_
        if not(not((d_771_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,11): " + _dafny.string_of(d_771_valueOrError3_))
        d_767_res_ = (d_771_valueOrError3_).Extract()
        if not((d_767_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_772_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out317_: Wrappers.Result
        out317_ = (d_763_st_).GetFromCacheWithTime(default__.MakeGet(d_766_one_), 10003)
        d_772_valueOrError4_ = out317_
        if not(not((d_772_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,11): " + _dafny.string_of(d_772_valueOrError4_))
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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,16): " + _dafny.string_of(d_776_valueOrError0_))
        d_775_res2_ = (d_776_valueOrError0_).Extract()
        d_777_res_: StormTracker.CacheState
        d_778_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out319_: Wrappers.Result
        out319_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 9999)
        d_778_valueOrError1_ = out319_
        if not(not((d_778_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,15): " + _dafny.string_of(d_778_valueOrError1_))
        d_777_res_ = (d_778_valueOrError1_).Extract()
        if not((d_777_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_779_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out320_: Wrappers.Result
        out320_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 10000)
        d_779_valueOrError2_ = out320_
        if not(not((d_779_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + _dafny.string_of(d_779_valueOrError2_))
        d_777_res_ = (d_779_valueOrError2_).Extract()
        if not((d_777_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_780_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out321_: Wrappers.Result
        out321_ = (d_773_st_).GetFromCacheWithTime(default__.MakeGet(d_774_one_), 10000)
        d_780_valueOrError3_ = out321_
        if not(not((d_780_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,11): " + _dafny.string_of(d_780_valueOrError3_))
        d_777_res_ = (d_780_valueOrError3_).Extract()
        if not((d_777_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

