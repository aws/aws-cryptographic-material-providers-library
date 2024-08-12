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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
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
import TestLyingBranchKey as TestLyingBranchKey
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
import TestRawECDHKeyring as TestRawECDHKeyring
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
import TestAwsKmsEcdhKeyring as TestAwsKmsEcdhKeyring
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
        d_1463_st_: StormTracker.StormTracker
        nw11_ = StormTracker.StormTracker()
        nw11_.ctor__(StormTracker.default__.DefaultStorm())
        d_1463_st_ = nw11_
        d_1464_abc_: _dafny.Seq
        d_1464_abc_ = UTF8.default__.EncodeAscii(_dafny.Seq("abc"))
        d_1465_cde_: _dafny.Seq
        d_1465_cde_ = UTF8.default__.EncodeAscii(_dafny.Seq("cde"))
        d_1466_res_: StormTracker.CacheState
        d_1467_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out558_: Wrappers.Result
        out558_ = (d_1463_st_).GetFromCacheWithTime(default__.MakeGet(d_1464_abc_), 10000)
        d_1467_valueOrError0_ = out558_
        if not(not((d_1467_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(55,15): " + _dafny.string_of(d_1467_valueOrError0_))
        d_1466_res_ = (d_1467_valueOrError0_).Extract()
        if not((d_1466_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1468_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out559_: Wrappers.Result
        out559_ = (d_1463_st_).GetFromCacheWithTime(default__.MakeGet(d_1464_abc_), 10000)
        d_1468_valueOrError1_ = out559_
        if not(not((d_1468_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(57,11): " + _dafny.string_of(d_1468_valueOrError1_))
        d_1466_res_ = (d_1468_valueOrError1_).Extract()
        if not((d_1466_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(58,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1469_res2_: tuple
        d_1470_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out560_: Wrappers.Result
        out560_ = (d_1463_st_).PutCacheEntry(default__.MakePut(d_1464_abc_, 10000))
        d_1470_valueOrError2_ = out560_
        if not(not((d_1470_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(59,16): " + _dafny.string_of(d_1470_valueOrError2_))
        d_1469_res2_ = (d_1470_valueOrError2_).Extract()
        d_1471_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out561_: Wrappers.Result
        out561_ = (d_1463_st_).PutCacheEntry(default__.MakePut(d_1465_cde_, 10000))
        d_1471_valueOrError3_ = out561_
        if not(not((d_1471_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(60,12): " + _dafny.string_of(d_1471_valueOrError3_))
        d_1469_res2_ = (d_1471_valueOrError3_).Extract()
        d_1472_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out562_: Wrappers.Result
        out562_ = (d_1463_st_).GetFromCacheWithTime(default__.MakeGet(d_1464_abc_), 10001)
        d_1472_valueOrError4_ = out562_
        if not(not((d_1472_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(61,11): " + _dafny.string_of(d_1472_valueOrError4_))
        d_1466_res_ = (d_1472_valueOrError4_).Extract()
        if not((d_1466_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1473_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out563_: Wrappers.Result
        out563_ = (d_1463_st_).GetFromCacheWithTime(default__.MakeGet(d_1464_abc_), 10001)
        d_1473_valueOrError5_ = out563_
        if not(not((d_1473_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(63,11): " + _dafny.string_of(d_1473_valueOrError5_))
        d_1466_res_ = (d_1473_valueOrError5_).Extract()
        if not((d_1466_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1474_res3_: Wrappers.Result
        out564_: Wrappers.Result
        out564_ = (d_1463_st_).GetCacheEntry(default__.MakeGet(d_1464_abc_))
        d_1474_res3_ = out564_
        out565_: Wrappers.Result
        out565_ = (d_1463_st_).GetCacheEntry(default__.MakeGet(d_1464_abc_))
        d_1474_res3_ = out565_
        d_1475_res4_: Wrappers.Result
        out566_: Wrappers.Result
        out566_ = (d_1463_st_).GetFromCache(default__.MakeGet(d_1464_abc_))
        d_1475_res4_ = out566_
        out567_: Wrappers.Result
        out567_ = (d_1463_st_).GetFromCache(default__.MakeGet(d_1464_abc_))
        d_1475_res4_ = out567_
        d_1476_res5_: Wrappers.Result
        out568_: Wrappers.Result
        out568_ = (d_1463_st_).DeleteCacheEntry(default__.MakeDel(d_1464_abc_))
        d_1476_res5_ = out568_
        out569_: Wrappers.Result
        out569_ = (d_1463_st_).DeleteCacheEntry(default__.MakeDel(d_1464_abc_))
        d_1476_res5_ = out569_

    @staticmethod
    def StormTrackerFanOut():
        d_1477_st_: StormTracker.StormTracker
        nw12_ = StormTracker.StormTracker()
        def iife52_(_pat_let24_0):
            def iife53_(d_1478_dt__update__tmp_h0_):
                def iife54_(_pat_let25_0):
                    def iife55_(d_1479_dt__update_hfanOut_h0_):
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_1478_dt__update__tmp_h0_).entryCapacity, (d_1478_dt__update__tmp_h0_).entryPruningTailSize, (d_1478_dt__update__tmp_h0_).gracePeriod, (d_1478_dt__update__tmp_h0_).graceInterval, d_1479_dt__update_hfanOut_h0_, (d_1478_dt__update__tmp_h0_).inFlightTTL, (d_1478_dt__update__tmp_h0_).sleepMilli)
                    return iife55_(_pat_let25_0)
                return iife54_(3)
            return iife53_(_pat_let24_0)
        nw12_.ctor__(iife52_(StormTracker.default__.DefaultStorm()))
        d_1477_st_ = nw12_
        d_1480_one_: _dafny.Seq
        d_1480_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_1481_two_: _dafny.Seq
        d_1481_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_1482_three_: _dafny.Seq
        d_1482_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_1483_four_: _dafny.Seq
        d_1483_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_1484_res_: StormTracker.CacheState
        d_1485_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out570_: Wrappers.Result
        out570_ = (d_1477_st_).GetFromCacheWithTime(default__.MakeGet(d_1480_one_), 10000)
        d_1485_valueOrError0_ = out570_
        if not(not((d_1485_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(84,15): " + _dafny.string_of(d_1485_valueOrError0_))
        d_1484_res_ = (d_1485_valueOrError0_).Extract()
        if not((d_1484_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1486_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out571_: Wrappers.Result
        out571_ = (d_1477_st_).GetFromCacheWithTime(default__.MakeGet(d_1481_two_), 10000)
        d_1486_valueOrError1_ = out571_
        if not(not((d_1486_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(86,11): " + _dafny.string_of(d_1486_valueOrError1_))
        d_1484_res_ = (d_1486_valueOrError1_).Extract()
        if not((d_1484_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1487_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out572_: Wrappers.Result
        out572_ = (d_1477_st_).GetFromCacheWithTime(default__.MakeGet(d_1482_three_), 10000)
        d_1487_valueOrError2_ = out572_
        if not(not((d_1487_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(88,11): " + _dafny.string_of(d_1487_valueOrError2_))
        d_1484_res_ = (d_1487_valueOrError2_).Extract()
        if not((d_1484_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1488_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out573_: Wrappers.Result
        out573_ = (d_1477_st_).GetFromCacheWithTime(default__.MakeGet(d_1483_four_), 10000)
        d_1488_valueOrError3_ = out573_
        if not(not((d_1488_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(90,11): " + _dafny.string_of(d_1488_valueOrError3_))
        d_1484_res_ = (d_1488_valueOrError3_).Extract()
        if not((d_1484_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerTTL():
        d_1489_st_: StormTracker.StormTracker
        nw13_ = StormTracker.StormTracker()
        def iife56_(_pat_let26_0):
            def iife57_(d_1490_dt__update__tmp_h0_):
                def iife58_(_pat_let27_0):
                    def iife59_(d_1491_dt__update_hinFlightTTL_h0_):
                        def iife60_(_pat_let28_0):
                            def iife61_(d_1492_dt__update_hfanOut_h0_):
                                return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_1490_dt__update__tmp_h0_).entryCapacity, (d_1490_dt__update__tmp_h0_).entryPruningTailSize, (d_1490_dt__update__tmp_h0_).gracePeriod, (d_1490_dt__update__tmp_h0_).graceInterval, d_1492_dt__update_hfanOut_h0_, d_1491_dt__update_hinFlightTTL_h0_, (d_1490_dt__update__tmp_h0_).sleepMilli)
                            return iife61_(_pat_let28_0)
                        return iife60_(3)
                    return iife59_(_pat_let27_0)
                return iife58_(5)
            return iife57_(_pat_let26_0)
        nw13_.ctor__(iife56_(StormTracker.default__.DefaultStorm()))
        d_1489_st_ = nw13_
        d_1493_one_: _dafny.Seq
        d_1493_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_1494_two_: _dafny.Seq
        d_1494_two_ = UTF8.default__.EncodeAscii(_dafny.Seq("two"))
        d_1495_three_: _dafny.Seq
        d_1495_three_ = UTF8.default__.EncodeAscii(_dafny.Seq("three"))
        d_1496_four_: _dafny.Seq
        d_1496_four_ = UTF8.default__.EncodeAscii(_dafny.Seq("four"))
        d_1497_res_: StormTracker.CacheState
        d_1498_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out574_: Wrappers.Result
        out574_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1493_one_), 10000)
        d_1498_valueOrError0_ = out574_
        if not(not((d_1498_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,15): " + _dafny.string_of(d_1498_valueOrError0_))
        d_1497_res_ = (d_1498_valueOrError0_).Extract()
        if not((d_1497_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1499_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out575_: Wrappers.Result
        out575_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1494_two_), 10000)
        d_1499_valueOrError1_ = out575_
        if not(not((d_1499_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,11): " + _dafny.string_of(d_1499_valueOrError1_))
        d_1497_res_ = (d_1499_valueOrError1_).Extract()
        if not((d_1497_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1500_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out576_: Wrappers.Result
        out576_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1495_three_), 10000)
        d_1500_valueOrError2_ = out576_
        if not(not((d_1500_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + _dafny.string_of(d_1500_valueOrError2_))
        d_1497_res_ = (d_1500_valueOrError2_).Extract()
        if not((d_1497_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1501_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out577_: Wrappers.Result
        out577_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1496_four_), 10000)
        d_1501_valueOrError3_ = out577_
        if not(not((d_1501_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,11): " + _dafny.string_of(d_1501_valueOrError3_))
        d_1497_res_ = (d_1501_valueOrError3_).Extract()
        if not((d_1497_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1502_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out578_: Wrappers.Result
        out578_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1496_four_), 10001)
        d_1502_valueOrError4_ = out578_
        if not(not((d_1502_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(111,11): " + _dafny.string_of(d_1502_valueOrError4_))
        d_1497_res_ = (d_1502_valueOrError4_).Extract()
        if not((d_1497_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1503_valueOrError5_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out579_: Wrappers.Result
        out579_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1496_four_), 10003)
        d_1503_valueOrError5_ = out579_
        if not(not((d_1503_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(113,11): " + _dafny.string_of(d_1503_valueOrError5_))
        d_1497_res_ = (d_1503_valueOrError5_).Extract()
        if not((d_1497_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1504_valueOrError6_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out580_: Wrappers.Result
        out580_ = (d_1489_st_).GetFromCacheWithTime(default__.MakeGet(d_1496_four_), 10005)
        d_1504_valueOrError6_ = out580_
        if not(not((d_1504_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(115,11): " + _dafny.string_of(d_1504_valueOrError6_))
        d_1497_res_ = (d_1504_valueOrError6_).Extract()
        if not((d_1497_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(116,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGraceInterval():
        d_1505_st_: StormTracker.StormTracker
        nw14_ = StormTracker.StormTracker()
        def iife62_(_pat_let29_0):
            def iife63_(d_1506_dt__update__tmp_h0_):
                def iife64_(_pat_let30_0):
                    def iife65_(d_1507_dt__update_hgraceInterval_h0_):
                        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache((d_1506_dt__update__tmp_h0_).entryCapacity, (d_1506_dt__update__tmp_h0_).entryPruningTailSize, (d_1506_dt__update__tmp_h0_).gracePeriod, d_1507_dt__update_hgraceInterval_h0_, (d_1506_dt__update__tmp_h0_).fanOut, (d_1506_dt__update__tmp_h0_).inFlightTTL, (d_1506_dt__update__tmp_h0_).sleepMilli)
                    return iife65_(_pat_let30_0)
                return iife64_(3)
            return iife63_(_pat_let29_0)
        nw14_.ctor__(iife62_(StormTracker.default__.DefaultStorm()))
        d_1505_st_ = nw14_
        d_1508_one_: _dafny.Seq
        d_1508_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_1509_res_: StormTracker.CacheState
        d_1510_valueOrError0_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out581_: Wrappers.Result
        out581_ = (d_1505_st_).GetFromCacheWithTime(default__.MakeGet(d_1508_one_), 10000)
        d_1510_valueOrError0_ = out581_
        if not(not((d_1510_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,15): " + _dafny.string_of(d_1510_valueOrError0_))
        d_1509_res_ = (d_1510_valueOrError0_).Extract()
        if not((d_1509_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1511_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out582_: Wrappers.Result
        out582_ = (d_1505_st_).GetFromCacheWithTime(default__.MakeGet(d_1508_one_), 10000)
        d_1511_valueOrError1_ = out582_
        if not(not((d_1511_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,11): " + _dafny.string_of(d_1511_valueOrError1_))
        d_1509_res_ = (d_1511_valueOrError1_).Extract()
        if not((d_1509_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1512_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out583_: Wrappers.Result
        out583_ = (d_1505_st_).GetFromCacheWithTime(default__.MakeGet(d_1508_one_), 10001)
        d_1512_valueOrError2_ = out583_
        if not(not((d_1512_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,11): " + _dafny.string_of(d_1512_valueOrError2_))
        d_1509_res_ = (d_1512_valueOrError2_).Extract()
        if not((d_1509_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1513_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out584_: Wrappers.Result
        out584_ = (d_1505_st_).GetFromCacheWithTime(default__.MakeGet(d_1508_one_), 10002)
        d_1513_valueOrError3_ = out584_
        if not(not((d_1513_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,11): " + _dafny.string_of(d_1513_valueOrError3_))
        d_1509_res_ = (d_1513_valueOrError3_).Extract()
        if not((d_1509_res_).is_EmptyWait):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(132,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1514_valueOrError4_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out585_: Wrappers.Result
        out585_ = (d_1505_st_).GetFromCacheWithTime(default__.MakeGet(d_1508_one_), 10003)
        d_1514_valueOrError4_ = out585_
        if not(not((d_1514_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(133,11): " + _dafny.string_of(d_1514_valueOrError4_))
        d_1509_res_ = (d_1514_valueOrError4_).Extract()
        if not((d_1509_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def StormTrackerGracePeriod():
        d_1515_st_: StormTracker.StormTracker
        nw15_ = StormTracker.StormTracker()
        nw15_.ctor__(StormTracker.default__.DefaultStorm())
        d_1515_st_ = nw15_
        d_1516_one_: _dafny.Seq
        d_1516_one_ = UTF8.default__.EncodeAscii(_dafny.Seq("one"))
        d_1517_res2_: tuple
        d_1518_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out586_: Wrappers.Result
        out586_ = (d_1515_st_).PutCacheEntry(default__.MakePut(d_1516_one_, 10010))
        d_1518_valueOrError0_ = out586_
        if not(not((d_1518_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,16): " + _dafny.string_of(d_1518_valueOrError0_))
        d_1517_res2_ = (d_1518_valueOrError0_).Extract()
        d_1519_res_: StormTracker.CacheState
        d_1520_valueOrError1_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out587_: Wrappers.Result
        out587_ = (d_1515_st_).GetFromCacheWithTime(default__.MakeGet(d_1516_one_), 9999)
        d_1520_valueOrError1_ = out587_
        if not(not((d_1520_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,15): " + _dafny.string_of(d_1520_valueOrError1_))
        d_1519_res_ = (d_1520_valueOrError1_).Extract()
        if not((d_1519_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1521_valueOrError2_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out588_: Wrappers.Result
        out588_ = (d_1515_st_).GetFromCacheWithTime(default__.MakeGet(d_1516_one_), 10000)
        d_1521_valueOrError2_ = out588_
        if not(not((d_1521_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + _dafny.string_of(d_1521_valueOrError2_))
        d_1519_res_ = (d_1521_valueOrError2_).Extract()
        if not((d_1519_res_).is_EmptyFetch):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1522_valueOrError3_: Wrappers.Result = Wrappers.Result.default(StormTracker.CacheState.default())()
        out589_: Wrappers.Result
        out589_ = (d_1515_st_).GetFromCacheWithTime(default__.MakeGet(d_1516_one_), 10000)
        d_1522_valueOrError3_ = out589_
        if not(not((d_1522_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,11): " + _dafny.string_of(d_1522_valueOrError3_))
        d_1519_res_ = (d_1522_valueOrError3_).Extract()
        if not((d_1519_res_).is_Full):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

