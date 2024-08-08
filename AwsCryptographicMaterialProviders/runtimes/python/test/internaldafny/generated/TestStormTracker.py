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
        d_952_st_: StormTracker.StormTracker
        nw11_ = StormTracker.StormTracker()
        nw11_.ctor__(StormTracker.default__.DefaultStorm())
        d_952_st_ = nw11_
        d_953_abc_: _dafny.Seq
        d_953_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_954_cde_: _dafny.Seq
        d_954_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_955_res_: StormTracker.CacheState
        d_956_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out367_: Wrappers.Result
        out367_ = (d_952_st_).GetFromCacheWithTime(default__.MakeGet(d_953_abc_), 10000)
        d_956_valueOrError0_ = out367_
        if not(not((d_956_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,15): " + _dafny.string_of(d_956_valueOrError0_))
        d_955_res_ = (d_956_valueOrError0_).Extract()
        if not((d_955_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_957_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out368_: Wrappers.Result
        out368_ = (d_952_st_).GetFromCacheWithTime(default__.MakeGet(d_953_abc_), 10000)
        d_957_valueOrError1_ = out368_
        if not(not((d_957_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,11): " + _dafny.string_of(d_957_valueOrError1_))
        d_955_res_ = (d_957_valueOrError1_).Extract()
        if not((d_955_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_958_res2_: tuple
        d_959_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out369_: Wrappers.Result
        out369_ = (d_952_st_).PutCacheEntry(default__.MakePut(d_953_abc_, 10000))
        d_959_valueOrError2_ = out369_
        if not(not((d_959_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,16): " + _dafny.string_of(d_959_valueOrError2_))
        d_958_res2_ = (d_959_valueOrError2_).Extract()
        d_960_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out370_: Wrappers.Result
        out370_ = (d_952_st_).PutCacheEntry(default__.MakePut(d_954_cde_, 10000))
        d_960_valueOrError3_ = out370_
        if not(not((d_960_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,12): " + _dafny.string_of(d_960_valueOrError3_))
        d_958_res2_ = (d_960_valueOrError3_).Extract()
        d_961_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out371_: Wrappers.Result
        out371_ = (d_952_st_).GetFromCacheWithTime(default__.MakeGet(d_953_abc_), 10001)
        d_961_valueOrError4_ = out371_
        if not(not((d_961_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,11): " + _dafny.string_of(d_961_valueOrError4_))
        d_955_res_ = (d_961_valueOrError4_).Extract()
        if not((d_955_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_962_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out372_: Wrappers.Result
        out372_ = (d_952_st_).GetFromCacheWithTime(default__.MakeGet(d_953_abc_), 10001)
        d_962_valueOrError5_ = out372_
        if not(not((d_962_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,11): " + _dafny.string_of(d_962_valueOrError5_))
        d_955_res_ = (d_962_valueOrError5_).Extract()
        if not((d_955_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_963_res3_: Wrappers.Result
        out373_: Wrappers.Result
        out373_ = (d_952_st_).GetCacheEntry(default__.MakeGet(d_953_abc_))
        d_963_res3_ = out373_
        out374_: Wrappers.Result
        out374_ = (d_952_st_).GetCacheEntry(default__.MakeGet(d_953_abc_))
        d_963_res3_ = out374_
        d_964_res4_: Wrappers.Result
        out375_: Wrappers.Result
        out375_ = (d_952_st_).GetFromCache(default__.MakeGet(d_953_abc_))
        d_964_res4_ = out375_
        out376_: Wrappers.Result
        out376_ = (d_952_st_).GetFromCache(default__.MakeGet(d_953_abc_))
        d_964_res4_ = out376_
        d_965_res5_: Wrappers.Result
        out377_: Wrappers.Result
        out377_ = (d_952_st_).DeleteCacheEntry(default__.MakeDel(d_953_abc_))
        d_965_res5_ = out377_
        out378_: Wrappers.Result
        out378_ = (d_952_st_).DeleteCacheEntry(default__.MakeDel(d_953_abc_))
        d_965_res5_ = out378_

    @staticmethod
    def StormTrackerFanOut():
        d_966_st_: StormTracker.StormTracker
        nw12_ = StormTracker.StormTracker()
        def iife40_(_pat_let18_0):
            def iife41_(d_967_dt__update__tmp_h0_):
                def iife42_(_pat_let19_0):
                    def iife43_(d_968_dt__update_hfanOut_h0_):
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_967_dt__update__tmp_h0_).entryCapacity, (d_967_dt__update__tmp_h0_).entryPruningTailSize, (d_967_dt__update__tmp_h0_).gracePeriod, (d_967_dt__update__tmp_h0_).graceInterval, d_968_dt__update_hfanOut_h0_, (d_967_dt__update__tmp_h0_).inFlightTTL, (d_967_dt__update__tmp_h0_).sleepMilli)
                    return iife43_(_pat_let19_0)
                return iife42_(3)
            return iife41_(_pat_let18_0)
        nw12_.ctor__(iife40_(StormTracker.default__.DefaultStorm()))
        d_966_st_ = nw12_
        d_969_one_: _dafny.Seq
        d_969_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_970_two_: _dafny.Seq
        d_970_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_971_three_: _dafny.Seq
        d_971_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_972_four_: _dafny.Seq
        d_972_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_973_res_: StormTracker.CacheState
        d_974_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out379_: Wrappers.Result
        out379_ = (d_966_st_).GetFromCacheWithTime(default__.MakeGet(d_969_one_), 10000)
        d_974_valueOrError0_ = out379_
        if not(not((d_974_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,15): " + _dafny.string_of(d_974_valueOrError0_))
        d_973_res_ = (d_974_valueOrError0_).Extract()
        if not((d_973_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_975_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out380_: Wrappers.Result
        out380_ = (d_966_st_).GetFromCacheWithTime(default__.MakeGet(d_970_two_), 10000)
        d_975_valueOrError1_ = out380_
        if not(not((d_975_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,11): " + _dafny.string_of(d_975_valueOrError1_))
        d_973_res_ = (d_975_valueOrError1_).Extract()
        if not((d_973_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_976_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out381_: Wrappers.Result
        out381_ = (d_966_st_).GetFromCacheWithTime(default__.MakeGet(d_971_three_), 10000)
        d_976_valueOrError2_ = out381_
        if not(not((d_976_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,11): " + _dafny.string_of(d_976_valueOrError2_))
        d_973_res_ = (d_976_valueOrError2_).Extract()
        if not((d_973_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_977_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out382_: Wrappers.Result
        out382_ = (d_966_st_).GetFromCacheWithTime(default__.MakeGet(d_972_four_), 10000)
        d_977_valueOrError3_ = out382_
        if not(not((d_977_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,11): " + _dafny.string_of(d_977_valueOrError3_))
        d_973_res_ = (d_977_valueOrError3_).Extract()
        if not((d_973_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerTTL():
        d_978_st_: StormTracker.StormTracker
        nw13_ = StormTracker.StormTracker()
        def iife44_(_pat_let20_0):
            def iife45_(d_979_dt__update__tmp_h0_):
                def iife46_(_pat_let21_0):
                    def iife47_(d_980_dt__update_hinFlightTTL_h0_):
                        def iife48_(_pat_let22_0):
                            def iife49_(d_981_dt__update_hfanOut_h0_):
                                return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_979_dt__update__tmp_h0_).entryCapacity, (d_979_dt__update__tmp_h0_).entryPruningTailSize, (d_979_dt__update__tmp_h0_).gracePeriod, (d_979_dt__update__tmp_h0_).graceInterval, d_981_dt__update_hfanOut_h0_, d_980_dt__update_hinFlightTTL_h0_, (d_979_dt__update__tmp_h0_).sleepMilli)
                            return iife49_(_pat_let22_0)
                        return iife48_(3)
                    return iife47_(_pat_let21_0)
                return iife46_(5)
            return iife45_(_pat_let20_0)
        nw13_.ctor__(iife44_(StormTracker.default__.DefaultStorm()))
        d_978_st_ = nw13_
        d_982_one_: _dafny.Seq
        d_982_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_983_two_: _dafny.Seq
        d_983_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_984_three_: _dafny.Seq
        d_984_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_985_four_: _dafny.Seq
        d_985_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_986_res_: StormTracker.CacheState
        d_987_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out383_: Wrappers.Result
        out383_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_982_one_), 10000)
        d_987_valueOrError0_ = out383_
        if not(not((d_987_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,15): " + _dafny.string_of(d_987_valueOrError0_))
        d_986_res_ = (d_987_valueOrError0_).Extract()
        if not((d_986_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_988_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out384_: Wrappers.Result
        out384_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_983_two_), 10000)
        d_988_valueOrError1_ = out384_
        if not(not((d_988_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,11): " + _dafny.string_of(d_988_valueOrError1_))
        d_986_res_ = (d_988_valueOrError1_).Extract()
        if not((d_986_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_989_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out385_: Wrappers.Result
        out385_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_984_three_), 10000)
        d_989_valueOrError2_ = out385_
        if not(not((d_989_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + _dafny.string_of(d_989_valueOrError2_))
        d_986_res_ = (d_989_valueOrError2_).Extract()
        if not((d_986_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_990_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out386_: Wrappers.Result
        out386_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_985_four_), 10000)
        d_990_valueOrError3_ = out386_
        if not(not((d_990_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,11): " + _dafny.string_of(d_990_valueOrError3_))
        d_986_res_ = (d_990_valueOrError3_).Extract()
        if not((d_986_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_991_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out387_: Wrappers.Result
        out387_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_985_four_), 10001)
        d_991_valueOrError4_ = out387_
        if not(not((d_991_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,11): " + _dafny.string_of(d_991_valueOrError4_))
        d_986_res_ = (d_991_valueOrError4_).Extract()
        if not((d_986_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_992_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out388_: Wrappers.Result
        out388_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_985_four_), 10003)
        d_992_valueOrError5_ = out388_
        if not(not((d_992_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,11): " + _dafny.string_of(d_992_valueOrError5_))
        d_986_res_ = (d_992_valueOrError5_).Extract()
        if not((d_986_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_993_valueOrError6_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out389_: Wrappers.Result
        out389_ = (d_978_st_).GetFromCacheWithTime(default__.MakeGet(d_985_four_), 10005)
        d_993_valueOrError6_ = out389_
        if not(not((d_993_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,11): " + _dafny.string_of(d_993_valueOrError6_))
        d_986_res_ = (d_993_valueOrError6_).Extract()
        if not((d_986_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(116,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGraceInterval():
        d_994_st_: StormTracker.StormTracker
        nw14_ = StormTracker.StormTracker()
        def iife50_(_pat_let23_0):
            def iife51_(d_995_dt__update__tmp_h0_):
                def iife52_(_pat_let24_0):
                    def iife53_(d_996_dt__update_hgraceInterval_h0_):
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_995_dt__update__tmp_h0_).entryCapacity, (d_995_dt__update__tmp_h0_).entryPruningTailSize, (d_995_dt__update__tmp_h0_).gracePeriod, d_996_dt__update_hgraceInterval_h0_, (d_995_dt__update__tmp_h0_).fanOut, (d_995_dt__update__tmp_h0_).inFlightTTL, (d_995_dt__update__tmp_h0_).sleepMilli)
                    return iife53_(_pat_let24_0)
                return iife52_(3)
            return iife51_(_pat_let23_0)
        nw14_.ctor__(iife50_(StormTracker.default__.DefaultStorm()))
        d_994_st_ = nw14_
        d_997_one_: _dafny.Seq
        d_997_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_998_res_: StormTracker.CacheState
        d_999_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out390_: Wrappers.Result
        out390_ = (d_994_st_).GetFromCacheWithTime(default__.MakeGet(d_997_one_), 10000)
        d_999_valueOrError0_ = out390_
        if not(not((d_999_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,15): " + _dafny.string_of(d_999_valueOrError0_))
        d_998_res_ = (d_999_valueOrError0_).Extract()
        if not((d_998_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1000_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out391_: Wrappers.Result
        out391_ = (d_994_st_).GetFromCacheWithTime(default__.MakeGet(d_997_one_), 10000)
        d_1000_valueOrError1_ = out391_
        if not(not((d_1000_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,11): " + _dafny.string_of(d_1000_valueOrError1_))
        d_998_res_ = (d_1000_valueOrError1_).Extract()
        if not((d_998_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1001_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out392_: Wrappers.Result
        out392_ = (d_994_st_).GetFromCacheWithTime(default__.MakeGet(d_997_one_), 10001)
        d_1001_valueOrError2_ = out392_
        if not(not((d_1001_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,11): " + _dafny.string_of(d_1001_valueOrError2_))
        d_998_res_ = (d_1001_valueOrError2_).Extract()
        if not((d_998_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1002_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out393_: Wrappers.Result
        out393_ = (d_994_st_).GetFromCacheWithTime(default__.MakeGet(d_997_one_), 10002)
        d_1002_valueOrError3_ = out393_
        if not(not((d_1002_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,11): " + _dafny.string_of(d_1002_valueOrError3_))
        d_998_res_ = (d_1002_valueOrError3_).Extract()
        if not((d_998_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1003_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out394_: Wrappers.Result
        out394_ = (d_994_st_).GetFromCacheWithTime(default__.MakeGet(d_997_one_), 10003)
        d_1003_valueOrError4_ = out394_
        if not(not((d_1003_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,11): " + _dafny.string_of(d_1003_valueOrError4_))
        d_998_res_ = (d_1003_valueOrError4_).Extract()
        if not((d_998_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGracePeriod():
        d_1004_st_: StormTracker.StormTracker
        nw15_ = StormTracker.StormTracker()
        nw15_.ctor__(StormTracker.default__.DefaultStorm())
        d_1004_st_ = nw15_
        d_1005_one_: _dafny.Seq
        d_1005_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_1006_res2_: tuple
        d_1007_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out395_: Wrappers.Result
        out395_ = (d_1004_st_).PutCacheEntry(default__.MakePut(d_1005_one_, 10010))
        d_1007_valueOrError0_ = out395_
        if not(not((d_1007_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,16): " + _dafny.string_of(d_1007_valueOrError0_))
        d_1006_res2_ = (d_1007_valueOrError0_).Extract()
        d_1008_res_: StormTracker.CacheState
        d_1009_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out396_: Wrappers.Result
        out396_ = (d_1004_st_).GetFromCacheWithTime(default__.MakeGet(d_1005_one_), 9999)
        d_1009_valueOrError1_ = out396_
        if not(not((d_1009_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,15): " + _dafny.string_of(d_1009_valueOrError1_))
        d_1008_res_ = (d_1009_valueOrError1_).Extract()
        if not((d_1008_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1010_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out397_: Wrappers.Result
        out397_ = (d_1004_st_).GetFromCacheWithTime(default__.MakeGet(d_1005_one_), 10000)
        d_1010_valueOrError2_ = out397_
        if not(not((d_1010_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + _dafny.string_of(d_1010_valueOrError2_))
        d_1008_res_ = (d_1010_valueOrError2_).Extract()
        if not((d_1008_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1011_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out398_: Wrappers.Result
        out398_ = (d_1004_st_).GetFromCacheWithTime(default__.MakeGet(d_1005_one_), 10000)
        d_1011_valueOrError3_ = out398_
        if not(not((d_1011_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,11): " + _dafny.string_of(d_1011_valueOrError3_))
        d_1008_res_ = (d_1011_valueOrError3_).Extract()
        if not((d_1008_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

