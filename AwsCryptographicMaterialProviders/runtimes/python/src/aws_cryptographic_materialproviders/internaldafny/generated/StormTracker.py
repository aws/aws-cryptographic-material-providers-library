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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC

# Module: StormTracker

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultStorm():
        return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache_StormTrackingCache(1000, Wrappers.Option_Some(1), 10, 1, 20, 20, 20)


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
        d_778_x_ = (self.inFlight).Size()
        if (d_778_x_) <= (StandardLibrary_UInt.default__.INT64__MAX__LIMIT):
            return d_778_x_
        elif True:
            return StandardLibrary_UInt.default__.INT64__MAX__LIMIT

    def FanOutReached(self, now):
        res: bool = False
        (self).PruneInFlight(now)
        res = (self.fanOut) <= ((self).InFlightSize())
        return res
        return res

    def AddLong(self, x, y):
        if (x) < ((StandardLibrary_UInt.default__.INT64__MAX__LIMIT) - (y)):
            return (x) + (y)
        elif True:
            return StandardLibrary_UInt.default__.INT64__MAX__LIMIT

    def CheckInFlight(self, identifier, result, now):
        output: CacheState = CacheState.default()()
        d_779_fanOutReached_: bool
        out129_: bool
        out129_ = (self).FanOutReached(now)
        d_779_fanOutReached_ = out129_
        if d_779_fanOutReached_:
            output = CacheState_Full(result)
            return output
        elif ((result).expiryTime) <= (now):
            out130_: CacheState
            out130_ = (self).CheckNewEntry(identifier, now)
            output = out130_
        elif (now) < (((result).expiryTime) - (self.gracePeriod)):
            output = CacheState_Full(result)
            return output
        elif True:
            if (self.inFlight).HasKey(identifier):
                d_780_entry_: int
                d_780_entry_ = (self.inFlight).Select(identifier)
                if ((self).AddLong(d_780_entry_, self.graceInterval)) > (now):
                    output = CacheState_Full(result)
                    return output
            (self.inFlight).Put(identifier, now)
            output = CacheState_EmptyFetch()
            return output
        return output

    def PruneInFlight(self, now):
        if (self.fanOut) > ((self).InFlightSize()):
            return
        if (self.lastPrune) == (now):
            return
        (self).lastPrune = now
        d_781_keySet_: _dafny.Set
        d_781_keySet_ = (self.inFlight).Keys()
        d_782_keys_: _dafny.Seq
        d_782_keys_ = SortedSets.default__.SetToSequence(d_781_keySet_)
        hi7_ = len(d_782_keys_)
        for d_783_i_ in range(0, hi7_):
            d_784_v_: int
            d_784_v_ = (self.inFlight).Select((d_782_keys_)[d_783_i_])
            if (now) >= ((self).AddLong(d_784_v_, self.inFlightTTL)):
                (self.inFlight).Remove((d_782_keys_)[d_783_i_])

    def CheckNewEntry(self, identifier, now):
        output: CacheState = CacheState.default()()
        d_785_fanOutReached_: bool
        out131_: bool
        out131_ = (self).FanOutReached(now)
        d_785_fanOutReached_ = out131_
        if d_785_fanOutReached_:
            output = CacheState_EmptyWait()
            return output
        elif (self.inFlight).HasKey(identifier):
            d_786_entry_: int
            d_786_entry_ = (self.inFlight).Select(identifier)
            if ((self).AddLong(d_786_entry_, self.graceInterval)) > (now):
                output = CacheState_EmptyWait()
                return output
        (self.inFlight).Put(identifier, now)
        output = CacheState_EmptyFetch()
        return output
        return output

    def GetFromCacheWithTime(self, input, now):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_787_result_: Wrappers.Result
        out132_: Wrappers.Result
        out132_ = (self.wrapped).GetCacheEntryWithTime(input, now)
        d_787_result_ = out132_
        if (d_787_result_).is_Success:
            d_788_newResult_: CacheState
            out133_: CacheState
            out133_ = (self).CheckInFlight((input).identifier, (d_787_result_).value, now)
            d_788_newResult_ = out133_
            output = Wrappers.Result_Success(d_788_newResult_)
            return output
        elif ((d_787_result_).error).is_EntryDoesNotExist:
            d_789_newResult_: CacheState
            out134_: CacheState
            out134_ = (self).CheckNewEntry((input).identifier, now)
            d_789_newResult_ = out134_
            output = Wrappers.Result_Success(d_789_newResult_)
            return output
        elif True:
            output = Wrappers.Result_Failure((d_787_result_).error)
            return output
        return output

    def GetFromCache(self, input):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_790_now_: int
        out135_: int
        out135_ = Time.default__.CurrentRelativeTime()
        d_790_now_ = out135_
        out136_: Wrappers.Result
        out136_ = (self).GetFromCacheWithTime(input, d_790_now_)
        output = out136_
        return output

    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        d_791_result_: Wrappers.Result
        out137_: Wrappers.Result
        out137_ = (self).GetFromCache(input)
        d_791_result_ = out137_
        if (d_791_result_).is_Failure:
            output = Wrappers.Result_Failure((d_791_result_).error)
            return output
        elif ((d_791_result_).value).is_Full:
            output = Wrappers.Result_Success(((d_791_result_).value).data)
            return output
        elif True:
            output = Wrappers.Result_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
            return output
        return output

    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out138_: Wrappers.Result
        out138_ = (self.wrapped).PutCacheEntry_k(input)
        output = out138_
        return output

    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out139_: Wrappers.Result
        out139_ = (self.wrapped).DeleteCacheEntry_k(input)
        output = out139_
        return output

    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out140_: Wrappers.Result
        out140_ = (self.wrapped).UpdateUsageMetadata_k(input)
        output = out140_
        return output

