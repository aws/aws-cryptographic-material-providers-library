import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC

# Module: StormTracker

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultStorm():
        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache(1000, Wrappers.Option_Some(1), (10) * (1000), (1) * (1000), 20, (10) * (1000), 20, Wrappers.Option_Some(AwsCryptographyMaterialProvidersTypes.TimeUnits_Milliseconds()))

    @staticmethod
    def ConsistentSettings(cache):
        return ((((cache).graceInterval) <= ((cache).gracePeriod)) and (((cache).inFlightTTL) <= ((cache).gracePeriod))) and (((cache).graceInterval) <= ((cache).inFlightTTL))

    @staticmethod
    def N(n):
        return StandardLibrary_String.default__.Base10Int2String(n)

    @staticmethod
    def BadCacheMsg(cache):
        d_0_msg_ = _dafny.Seq("For a StormCache : ")
        d_1_msg_ = (d_0_msg_) + ((((((_dafny.Seq("graceInterval must not exceed gracePeriod, yet configuration has graceInterval=")) + (default__.N((cache).graceInterval))) + (_dafny.Seq(" and gracePeriod="))) + (default__.N((cache).gracePeriod))) + (_dafny.Seq(". ")) if not(((cache).graceInterval) <= ((cache).gracePeriod)) else _dafny.Seq("")))
        d_2_msg_ = (d_1_msg_) + ((((((_dafny.Seq("inFlightTTL must not exceed gracePeriod, yet configuration has inFlightTTL=")) + (default__.N((cache).inFlightTTL))) + (_dafny.Seq(" and gracePeriod="))) + (default__.N((cache).gracePeriod))) + (_dafny.Seq(". ")) if not(((cache).inFlightTTL) <= ((cache).gracePeriod)) else _dafny.Seq("")))
        return d_2_msg_

    @staticmethod
    def CheckSettings(cache):
        if default__.ConsistentSettings(cache):
            return Wrappers.Outcome_Pass()
        elif True:
            return Wrappers.Outcome_Fail(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(default__.BadCacheMsg(cache)))


class CacheState:
    @classmethod
    def default(cls, ):
        return lambda: CacheState_EmptyWait()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EmptyWait(self) -> bool:
        return isinstance(self, CacheState_EmptyWait)
    @property
    def is_EmptyFetch(self) -> bool:
        return isinstance(self, CacheState_EmptyFetch)
    @property
    def is_Full(self) -> bool:
        return isinstance(self, CacheState_Full)

class CacheState_EmptyWait(CacheState, NamedTuple('EmptyWait', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyWait'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_EmptyWait)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_EmptyFetch(CacheState, NamedTuple('EmptyFetch', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyFetch'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_EmptyFetch)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_Full(CacheState, NamedTuple('Full', [('data', Any)])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.Full({_dafny.string_of(self.data)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_Full) and self.data == __o.data
    def __hash__(self) -> int:
        return super().__hash__()


class StormTracker:
    def  __init__(self):
        self.wrapped: LocalCMC.LocalCMC = None
        self.inFlight: DafnyLibraries.MutableMap = None
        self.gracePeriod: int = None
        self.graceInterval: int = None
        self.fanOut: int = None
        self.inFlightTTL: int = None
        self.lastPrune: int = None
        self.sleepMilli: int = None
        pass

    def __dafnystr__(self) -> str:
        return "StormTracker.StormTracker"
    def ctor__(self, cache):
        d_0_gracePeriod_: int = int(0)
        d_1_graceInterval_: int = int(0)
        d_2_inFlightTTL_: int = int(0)
        if (((cache).timeUnits).UnwrapOr(AwsCryptographyMaterialProvidersTypes.TimeUnits_Seconds())).is_Seconds:
            d_0_gracePeriod_ = ((cache).gracePeriod) * (1000)
            d_1_graceInterval_ = ((cache).graceInterval) * (1000)
            d_2_inFlightTTL_ = ((cache).inFlightTTL) * (1000)
        elif True:
            d_0_gracePeriod_ = (cache).gracePeriod
            d_1_graceInterval_ = (cache).graceInterval
            d_2_inFlightTTL_ = (cache).inFlightTTL
        nw0_ = LocalCMC.LocalCMC()
        nw0_.ctor__((cache).entryCapacity, ((cache).entryPruningTailSize).UnwrapOr(1))
        (self).wrapped = nw0_
        nw1_ = DafnyLibraries.MutableMap()
        (self).inFlight = nw1_
        (self).gracePeriod = d_0_gracePeriod_
        (self).graceInterval = d_1_graceInterval_
        (self).fanOut = (cache).fanOut
        (self).inFlightTTL = d_2_inFlightTTL_
        (self).sleepMilli = (cache).sleepMilli
        (self).lastPrune = 0

    def FanOutReached(self, now):
        res: bool = False
        (self).PruneInFlight(now)
        res = (self.fanOut) <= ((self.inFlight).Size())
        return res
        return res

    def AddLong(self, x, y):
        if (x) < ((StandardLibrary_UInt.default__.INT64__MAX__LIMIT) - (y)):
            return (x) + (y)
        elif True:
            return StandardLibrary_UInt.default__.INT64__MAX__LIMIT

    def GracePeriod_q(self, result, now):
        return (((result).expiryTime) < (9223372036854775)) and (((((result).expiryTime) * (1000)) - (self.gracePeriod)) <= (now))

    def CheckInFlight(self, identifier, result, now):
        output: CacheState = CacheState.default()()
        d_0_fanOutReached_: bool
        out0_: bool
        out0_ = (self).FanOutReached(now)
        d_0_fanOutReached_ = out0_
        if d_0_fanOutReached_:
            output = CacheState_Full(result)
            return output
        elif not((self).GracePeriod_q(result, now)):
            output = CacheState_Full(result)
            return output
        elif True:
            if (self.inFlight).HasKey(identifier):
                d_1_entry_: int
                d_1_entry_ = (self.inFlight).Select(identifier)
                if ((self).AddLong(d_1_entry_, self.graceInterval)) > (now):
                    output = CacheState_Full(result)
                    return output
            (self.inFlight).Put(identifier, now)
            output = CacheState_EmptyFetch()
            return output
        return output

    def PruneInFlight(self, now):
        if ((self.inFlight).Size()) < (self.fanOut):
            return
        if ((now) - (1000)) < (self.lastPrune):
            return
        (self).lastPrune = now
        d_0_keySet_: _dafny.Set
        d_0_keySet_ = (self.inFlight).Keys()
        d_1_keys_: _dafny.Seq
        out0_: _dafny.Seq
        out0_ = SortedSets.default__.SetToSequence(d_0_keySet_)
        d_1_keys_ = out0_
        hi0_ = len(d_1_keys_)
        for d_2_i_ in range(0, hi0_):
            d_3_v_: int
            d_3_v_ = (self.inFlight).Select((d_1_keys_)[d_2_i_])
            if (now) >= ((self).AddLong(d_3_v_, self.inFlightTTL)):
                (self.inFlight).Remove((d_1_keys_)[d_2_i_])

    def CheckNewEntry(self, identifier, now):
        output: CacheState = CacheState.default()()
        d_0_fanOutReached_: bool
        out0_: bool
        out0_ = (self).FanOutReached(now)
        d_0_fanOutReached_ = out0_
        if d_0_fanOutReached_:
            output = CacheState_EmptyWait()
            return output
        elif (self.inFlight).HasKey(identifier):
            d_1_entry_: int
            d_1_entry_ = (self.inFlight).Select(identifier)
            if (now) < ((self).AddLong(d_1_entry_, self.graceInterval)):
                output = CacheState_EmptyWait()
                return output
        (self.inFlight).Put(identifier, now)
        output = CacheState_EmptyFetch()
        return output
        return output

    def GetFromCacheWithTime(self, input, now):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_0_result_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (self.wrapped).GetCacheEntryWithTime(input, _dafny.euclidian_division(now, 1000))
        d_0_result_ = out0_
        if (d_0_result_).is_Success:
            d_1_newResult_: CacheState
            out1_: CacheState
            out1_ = (self).CheckInFlight((input).identifier, (d_0_result_).value, now)
            d_1_newResult_ = out1_
            output = Wrappers.Result_Success(d_1_newResult_)
            return output
        elif ((d_0_result_).error).is_EntryDoesNotExist:
            d_2_newResult_: CacheState
            out2_: CacheState
            out2_ = (self).CheckNewEntry((input).identifier, now)
            d_2_newResult_ = out2_
            output = Wrappers.Result_Success(d_2_newResult_)
            return output
        elif True:
            output = Wrappers.Result_Failure((d_0_result_).error)
            return output
        return output

    def GetFromCache(self, input):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_0_now_: int
        out0_: int
        out0_ = Time.default__.CurrentRelativeTimeMilli()
        d_0_now_ = out0_
        out1_: Wrappers.Result
        out1_ = (self).GetFromCacheWithTime(input, d_0_now_)
        output = out1_
        return output

    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        d_0_result_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (self).GetFromCache(input)
        d_0_result_ = out0_
        if (d_0_result_).is_Failure:
            output = Wrappers.Result_Failure((d_0_result_).error)
            return output
        elif ((d_0_result_).value).is_Full:
            output = Wrappers.Result_Success(((d_0_result_).value).data)
            return output
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
            return output
        return output

    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out0_: Wrappers.Result
        out0_ = (self.wrapped).PutCacheEntry_k(input)
        output = out0_
        return output

    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out0_: Wrappers.Result
        out0_ = (self.wrapped).DeleteCacheEntry_k(input)
        output = out0_
        return output

    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out0_: Wrappers.Result
        out0_ = (self.wrapped).UpdateUsageMetadata_k(input)
        output = out0_
        return output

