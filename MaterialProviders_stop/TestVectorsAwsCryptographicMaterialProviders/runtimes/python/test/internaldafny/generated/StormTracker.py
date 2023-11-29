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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
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
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
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
        nw31_ = LocalCMC.LocalCMC()
        nw31_.ctor__((cache).entryCapacity, ((cache).entryPruningTailSize).UnwrapOr(1))
        (self).wrapped = nw31_
        nw32_ = DafnyLibraries.MutableMap()
        (self).inFlight = nw32_
        (self).gracePeriod = (cache).gracePeriod
        (self).graceInterval = (cache).graceInterval
        (self).fanOut = (cache).fanOut
        (self).inFlightTTL = (cache).inFlightTTL
        (self).sleepMilli = (cache).sleepMilli
        (self).lastPrune = 0

    def InFlightSize(self):
        d_695_x_ = (self.inFlight).Size()
        if (d_695_x_) <= ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT):
            return d_695_x_
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
        d_696_fanOutReached_: bool
        out136_: bool
        out136_ = (self).FanOutReached(now)
        d_696_fanOutReached_ = out136_
        if d_696_fanOutReached_:
            output = StormTracker.CacheState_Full(result)
            return output
        elif ((result).expiryTime) <= (now):
            out137_: StormTracker.CacheState
            out137_ = (self).CheckNewEntry(identifier, now)
            output = out137_
        elif (now) < (((result).expiryTime) - (self.gracePeriod)):
            output = StormTracker.CacheState_Full(result)
            return output
        elif True:
            if (self.inFlight).HasKey(identifier):
                d_697_entry_: BoundedInts.int64
                d_697_entry_ = (self.inFlight).Select(identifier)
                if ((self).AddLong(d_697_entry_, self.graceInterval)) > (now):
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
        d_698_keySet_: _dafny.Set
        d_698_keySet_ = (self.inFlight).Keys()
        d_699_keys_: _dafny.Seq
        d_699_keys_ = SortedSets.default__.SetToSequence(d_698_keySet_)
        hi8_: int = len(d_699_keys_)
        for d_700_i_ in range(0, hi8_):
            d_701_v_: BoundedInts.int64
            d_701_v_ = (self.inFlight).Select((d_699_keys_)[d_700_i_])
            if (now) >= ((self).AddLong(d_701_v_, self.inFlightTTL)):
                (self.inFlight).Remove((d_699_keys_)[d_700_i_])

    def CheckNewEntry(self, identifier, now):
        output: StormTracker.CacheState = StormTracker.CacheState_EmptyWait.default()()
        d_702_fanOutReached_: bool
        out138_: bool
        out138_ = (self).FanOutReached(now)
        d_702_fanOutReached_ = out138_
        if d_702_fanOutReached_:
            output = StormTracker.CacheState_EmptyWait()
            return output
        elif (self.inFlight).HasKey(identifier):
            d_703_entry_: BoundedInts.int64
            d_703_entry_ = (self.inFlight).Select(identifier)
            if ((self).AddLong(d_703_entry_, self.graceInterval)) > (now):
                output = StormTracker.CacheState_EmptyWait()
                return output
        (self.inFlight).Put(identifier, now)
        output = StormTracker.CacheState_EmptyFetch()
        return output
        return output

    def GetFromCacheWithTime(self, input, now):
        output: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        d_704_result_: Wrappers.Result
        out139_: Wrappers.Result
        out139_ = (self.wrapped).GetCacheEntryWithTime(input, now)
        d_704_result_ = out139_
        if (d_704_result_).is_Success:
            d_705_newResult_: StormTracker.CacheState
            out140_: StormTracker.CacheState
            out140_ = (self).CheckInFlight((input).identifier, (d_704_result_).value, now)
            d_705_newResult_ = out140_
            output = Wrappers.Result_Success(d_705_newResult_)
            return output
        elif ((d_704_result_).error).is_EntryDoesNotExist:
            d_706_newResult_: StormTracker.CacheState
            out141_: StormTracker.CacheState
            out141_ = (self).CheckNewEntry((input).identifier, now)
            d_706_newResult_ = out141_
            output = Wrappers.Result_Success(d_706_newResult_)
            return output
        elif True:
            output = Wrappers.Result_Failure((d_704_result_).error)
            return output
        return output

    def GetFromCache(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(StormTracker.CacheState.default())()
        d_707_now_: BoundedInts.int64
        out142_: BoundedInts.int64
        out142_ = Time.default__.CurrentRelativeTime()
        d_707_now_ = out142_
        out143_: Wrappers.Result
        out143_ = (self).GetFromCacheWithTime(input, d_707_now_)
        output = out143_
        return output

    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        d_708_result_: Wrappers.Result
        out144_: Wrappers.Result
        out144_ = (self).GetFromCache(input)
        d_708_result_ = out144_
        if (d_708_result_).is_Failure:
            output = Wrappers.Result_Failure((d_708_result_).error)
            return output
        elif ((d_708_result_).value).is_Full:
            output = Wrappers.Result_Success(((d_708_result_).value).data)
            return output
        elif True:
            output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
            return output
        return output

    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out145_: Wrappers.Result
        out145_ = (self.wrapped).PutCacheEntry_k(input)
        output = out145_
        return output

    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out146_: Wrappers.Result
        out146_ = (self.wrapped).DeleteCacheEntry_k(input)
        output = out146_
        return output

    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out147_: Wrappers.Result
        out147_ = (self.wrapped).UpdateUsageMetadata_k(input)
        output = out147_
        return output

