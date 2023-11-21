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

assert "StormTracker" == __name__
StormTracker = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultStorm():
        return software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache(1000, Wrappers.Option_Some(1), 10, 1, 20, 20, 20)


class CacheState:
    @classmethod
    def default(cls, ):
        return lambda: CacheState_EmptyWait()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EmptyWait(self) -> bool:
        return isinstance(self, StormTracker.CacheState_EmptyWait)
    @property
    def is_EmptyFetch(self) -> bool:
        return isinstance(self, StormTracker.CacheState_EmptyFetch)
    @property
    def is_Full(self) -> bool:
        return isinstance(self, StormTracker.CacheState_Full)

class CacheState_EmptyWait(CacheState, NamedTuple('EmptyWait', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyWait'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StormTracker.CacheState_EmptyWait)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_EmptyFetch(CacheState, NamedTuple('EmptyFetch', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyFetch'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StormTracker.CacheState_EmptyFetch)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_Full(CacheState, NamedTuple('Full', [('data', Any)])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.Full({_dafny.string_of(self.data)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StormTracker.CacheState_Full) and self.data == __o.data
    def __hash__(self) -> int:
        return super().__hash__()


class StormTracker:
    def  __init__(self):
        self.wrapped: LocalCMC.LocalCMC = None
        self.inFlight: DafnyLibraries.MutableMap = None
        self.gracePeriod: BoundedInts.int64 = None
        self.graceInterval: BoundedInts.int64 = None
        self.fanOut: BoundedInts.int64 = None
        self.inFlightTTL: BoundedInts.int64 = None
        self.lastPrune: BoundedInts.int64 = None
        self.sleepMilli: BoundedInts.int64 = None
        pass

    def __dafnystr__(self) -> str:
        return "StormTracker.StormTracker"
    def ctor__(self, cache):
        nw32_ = LocalCMC.LocalCMC()
        nw32_.ctor__((cache).entryCapacity, ((cache).entryPruningTailSize).UnwrapOr(1))
        (self).wrapped = nw32_
        nw33_ = DafnyLibraries.MutableMap()
        (self).inFlight = nw33_
        (self).gracePeriod = (cache).gracePeriod
        (self).graceInterval = (cache).graceInterval
        (self).fanOut = (cache).fanOut
        (self).inFlightTTL = (cache).inFlightTTL
        (self).sleepMilli = (cache).sleepMilli
        (self).lastPrune = 0

    def InFlightSize(self):
        d_1081_x_ = (self.inFlight).Size()
        if (d_1081_x_) <= ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT):
            return d_1081_x_
        elif True:
            return (StandardLibrary_mUInt.default__).INT64__MAX__LIMIT

    def FanOutReached(self, now):
        res: bool = False
        (self).PruneInFlight(now)
        res = (self.fanOut) <= ((self).InFlightSize())
        return res
        return res

    def AddLong(self, x, y):
        if (x) < (((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT) - (y)):
            return (x) + (y)
        elif True:
            return (StandardLibrary_mUInt.default__).INT64__MAX__LIMIT

    def CheckInFlight(self, identifier, result, now):
        output: StormTracker.CacheState = StormTracker.CacheState_EmptyWait.default()()
        d_1082_fanOutReached_: bool
        out257_: bool
        out257_ = (self).FanOutReached(now)
        d_1082_fanOutReached_ = out257_
        if d_1082_fanOutReached_:
            output = StormTracker.CacheState_Full(result)
            return output
        elif ((result).expiryTime) <= (now):
            out258_: StormTracker.CacheState
            out258_ = (self).CheckNewEntry(identifier, now)
            output = out258_
        elif (now) < (((result).expiryTime) - (self.gracePeriod)):
            output = StormTracker.CacheState_Full(result)
            return output
        elif True:
            if (self.inFlight).HasKey(identifier):
                d_1083_entry_: BoundedInts.int64
                d_1083_entry_ = (self.inFlight).Select(identifier)
                if ((self).AddLong(d_1083_entry_, self.graceInterval)) > (now):
                    output = StormTracker.CacheState_Full(result)
                    return output
            (self.inFlight).Put(identifier, now)
            output = StormTracker.CacheState_EmptyFetch()
            return output
        return output

    def PruneInFlight(self, now):
        if (self.fanOut) > ((self).InFlightSize()):
            return
        if (self.lastPrune) == (now):
            return
        (self).lastPrune = now
        d_1084_keySet_: _dafny.Set
        d_1084_keySet_ = (self.inFlight).Keys()
        d_1085_keys_: _dafny.Seq
        d_1085_keys_ = SortedSets.default__.SetToSequence(d_1084_keySet_)
        hi8_: int = len(d_1085_keys_)
        for d_1086_i_ in range(0, hi8_):
            d_1087_v_: BoundedInts.int64
            d_1087_v_ = (self.inFlight).Select((d_1085_keys_)[d_1086_i_])
            if (now) >= ((self).AddLong(d_1087_v_, self.inFlightTTL)):
                (self.inFlight).Remove((d_1085_keys_)[d_1086_i_])

    def CheckNewEntry(self, identifier, now):
        output: StormTracker.CacheState = StormTracker.CacheState_EmptyWait.default()()
        d_1088_fanOutReached_: bool
        out259_: bool
        out259_ = (self).FanOutReached(now)
        d_1088_fanOutReached_ = out259_
        if d_1088_fanOutReached_:
            output = StormTracker.CacheState_EmptyWait()
            return output
        elif (self.inFlight).HasKey(identifier):
            d_1089_entry_: BoundedInts.int64
            d_1089_entry_ = (self.inFlight).Select(identifier)
            if ((self).AddLong(d_1089_entry_, self.graceInterval)) > (now):
                output = StormTracker.CacheState_EmptyWait()
                return output
        (self.inFlight).Put(identifier, now)
        output = StormTracker.CacheState_EmptyFetch()
        return output
        return output

    def GetFromCacheWithTime(self, input, now):
        output: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        d_1090_result_: Wrappers.Result
        out260_: Wrappers.Result
        out260_ = (self.wrapped).GetCacheEntryWithTime(input, now)
        d_1090_result_ = out260_
        if (d_1090_result_).is_Success:
            d_1091_newResult_: StormTracker.CacheState
            out261_: StormTracker.CacheState
            out261_ = (self).CheckInFlight((input).identifier, (d_1090_result_).value, now)
            d_1091_newResult_ = out261_
            output = Wrappers.Result_Success(d_1091_newResult_)
            return output
        elif ((d_1090_result_).error).is_EntryDoesNotExist:
            d_1092_newResult_: StormTracker.CacheState
            out262_: StormTracker.CacheState
            out262_ = (self).CheckNewEntry((input).identifier, now)
            d_1092_newResult_ = out262_
            output = Wrappers.Result_Success(d_1092_newResult_)
            return output
        elif True:
            output = Wrappers.Result_Failure((d_1090_result_).error)
            return output
        return output

    def GetFromCache(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        d_1093_now_: BoundedInts.int64
        out263_: BoundedInts.int64
        out263_ = Time.default__.CurrentRelativeTime()
        d_1093_now_ = out263_
        out264_: Wrappers.Result
        out264_ = (self).GetFromCacheWithTime(input, d_1093_now_)
        output = out264_
        return output

    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        d_1094_result_: Wrappers.Result
        out265_: Wrappers.Result
        out265_ = (self).GetFromCache(input)
        d_1094_result_ = out265_
        if (d_1094_result_).is_Failure:
            output = Wrappers.Result_Failure((d_1094_result_).error)
            return output
        elif ((d_1094_result_).value).is_Full:
            output = Wrappers.Result_Success(((d_1094_result_).value).data)
            return output
        elif True:
            output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
            return output
        return output

    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out266_: Wrappers.Result
        out266_ = (self.wrapped).PutCacheEntry_k(input)
        output = out266_
        return output

    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out267_: Wrappers.Result
        out267_ = (self.wrapped).DeleteCacheEntry_k(input)
        output = out267_
        return output

    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out268_: Wrappers.Result
        out268_ = (self.wrapped).UpdateUsageMetadata_k(input)
        output = out268_
        return output

