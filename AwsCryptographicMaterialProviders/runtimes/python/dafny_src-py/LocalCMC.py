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
import software_amazon_cryptography_keystore_internaldafny
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

assert "LocalCMC" == __name__
LocalCMC = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RemoveValue(k0, m):
        d_861_m_k_: _dafny.Map
        d_861_m_k_ = (m) - (_dafny.Set({k0}))

    @_dafny.classproperty
    def NULL(instance):
        return LocalCMC.Ref_Null()
    @_dafny.classproperty
    def INT32__MAX__VALUE(instance):
        return 2040109465
    @_dafny.classproperty
    def INT64__MAX__VALUE(instance):
        return 8762203435012037017

class Ref:
    @classmethod
    def default(cls, ):
        return lambda: Ref_Null()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Ptr(self) -> bool:
        return isinstance(self, LocalCMC.Ref_Ptr)
    @property
    def is_Null(self) -> bool:
        return isinstance(self, LocalCMC.Ref_Null)

class Ref_Ptr(Ref, NamedTuple('Ptr', [('deref', Any)])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Ptr({_dafny.string_of(self.deref)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LocalCMC.Ref_Ptr) and self.deref == __o.deref
    def __hash__(self) -> int:
        return super().__hash__()

class Ref_Null(Ref, NamedTuple('Null', [])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Null'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LocalCMC.Ref_Null)
    def __hash__(self) -> int:
        return super().__hash__()


class CacheEntry:
    def  __init__(self):
        self.prev: LocalCMC.Ref = LocalCMC.Ref_Null.default()()
        self.next: LocalCMC.Ref = LocalCMC.Ref_Null.default()()
        self.messagesUsed: BoundedInts.int32 = None
        self.bytesUsed: BoundedInts.int32 = None
        self._identifier: _dafny.Seq = _dafny.Seq({})
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.Materials = None
        self._creationTime: BoundedInts.int64 = None
        self._expiryTime: BoundedInts.int64 = None
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.CacheEntry"
    def ctor__(self, materials_k, identifier_k, creationTime_k, expiryTime_k, messagesUsed_k, bytesUsed_k):
        (self)._materials = materials_k
        (self)._identifier = identifier_k
        (self)._creationTime = creationTime_k
        (self)._expiryTime = expiryTime_k
        (self).messagesUsed = messagesUsed_k
        (self).bytesUsed = bytesUsed_k
        (self).prev = (LocalCMC.default__).NULL
        (self).next = (LocalCMC.default__).NULL

    @property
    def identifier(self):
        return self._identifier
    @property
    def materials(self):
        return self._materials
    @property
    def creationTime(self):
        return self._creationTime
    @property
    def expiryTime(self):
        return self._expiryTime

class DoublyLinkedCacheEntryList:
    def  __init__(self):
        self.head: LocalCMC.Ref = LocalCMC.Ref_Null.default()()
        self.tail: LocalCMC.Ref = LocalCMC.Ref_Null.default()()
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.DoublyLinkedCacheEntryList"
    def ctor__(self):
        (self).head = LocalCMC.Ref_Null()
        (self).tail = LocalCMC.Ref_Null()

    def pushCell(self, toPush):
        d_862_cRef_: LocalCMC.Ref
        d_862_cRef_ = LocalCMC.Ref_Ptr(toPush)
        if (self.head).is_Ptr:
            obj0_ = (self.head).deref
            obj0_.prev = d_862_cRef_
            (toPush).next = self.head
            (self).head = d_862_cRef_
        elif True:
            (self).head = d_862_cRef_
            (self).tail = self.head

    def moveToFront(self, c):
        if ((self.head).deref) != (c):
            d_863_toPush_: LocalCMC.Ref
            d_863_toPush_ = LocalCMC.Ref_Ptr(c)
            (self).remove(c)
            if (self.head).is_Ptr:
                obj1_ = (self.head).deref
                obj1_.prev = d_863_toPush_
                obj2_ = (d_863_toPush_).deref
                obj2_.next = self.head
                (self).head = d_863_toPush_
            elif True:
                (self).head = d_863_toPush_
                (self).tail = self.head

    def remove(self, toRemove):
        if (toRemove.prev).is_Null:
            (self).head = toRemove.next
        elif True:
            obj3_ = (toRemove.prev).deref
            obj3_.next = toRemove.next
        if (toRemove.next).is_Null:
            (self).tail = toRemove.prev
        elif True:
            obj4_ = (toRemove.next).deref
            obj4_.prev = toRemove.prev
        with _dafny.label("0"):
            pass
        (toRemove).next = (LocalCMC.default__).NULL
        (toRemove).prev = (LocalCMC.default__).NULL


class LocalCMC(software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache):
    def  __init__(self):
        self.queue: LocalCMC.DoublyLinkedCacheEntryList = None
        self.cache: DafnyLibraries.MutableMap = None
        self._entryCapacity: int = int(0)
        self._entryPruningTailSize: int = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.LocalCMC"
    def PutCacheEntry(self, input):
        out164_: Wrappers.Result
        out164_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.PutCacheEntry(self, input)
        return out164_

    def UpdateUsageMetadata(self, input):
        out165_: Wrappers.Result
        out165_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.UpdateUsageMetadata(self, input)
        return out165_

    def GetCacheEntry(self, input):
        out166_: Wrappers.Result
        out166_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.GetCacheEntry(self, input)
        return out166_

    def DeleteCacheEntry(self, input):
        out167_: Wrappers.Result
        out167_ = software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache.DeleteCacheEntry(self, input)
        return out167_

    def ctor__(self, entryCapacity_k, entryPruningTailSize_k):
        (self)._entryCapacity = entryCapacity_k
        (self)._entryPruningTailSize = entryPruningTailSize_k
        nw29_ = DafnyLibraries.MutableMap()
        (self).cache = nw29_
        nw30_ = LocalCMC.DoublyLinkedCacheEntryList()
        nw30_.ctor__()
        (self).queue = nw30_

    def GetCacheEntry_k(self, input):
        output: Wrappers.Result = None
        d_864_now_: BoundedInts.int64
        out168_: BoundedInts.int64
        out168_ = Time.default__.CurrentRelativeTime()
        d_864_now_ = out168_
        out169_: Wrappers.Result
        out169_ = (self).GetCacheEntryWithTime(input, d_864_now_)
        output = out169_
        return output

    def GetCacheEntryWithTime(self, input, now):
        output: Wrappers.Result = None
        if (self.cache).HasKey((input).identifier):
            d_865_entry_: LocalCMC.CacheEntry
            d_865_entry_ = (self.cache).Select((input).identifier)
            if (now) <= ((d_865_entry_).expiryTime):
                (self.queue).moveToFront(d_865_entry_)
                output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput_GetCacheEntryOutput((d_865_entry_).materials, (d_865_entry_).creationTime, (d_865_entry_).expiryTime, d_865_entry_.messagesUsed, d_865_entry_.bytesUsed))
                d_866___v0_: tuple
                d_867_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
                out170_: Wrappers.Result
                out170_ = (self).pruning(now)
                d_867_valueOrError0_ = out170_
                if (d_867_valueOrError0_).IsFailure():
                    output = (d_867_valueOrError0_).PropagateFailure()
                    return output
                d_866___v0_ = (d_867_valueOrError0_).Extract()
            elif True:
                d_868___v1_: tuple
                d_869_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
                out171_: Wrappers.Result
                out171_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_869_valueOrError1_ = out171_
                if (d_869_valueOrError1_).IsFailure():
                    output = (d_869_valueOrError1_).PropagateFailure()
                    return output
                d_868___v1_ = (d_869_valueOrError1_).Extract()
                output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry past TTL")))
        elif True:
            output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
        return output

    def PutCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        if ((self).entryCapacity) == (0):
            output = Wrappers.Result_Success(())
            return output
        if (self.cache).HasKey((input).identifier):
            d_870___v2_: tuple
            d_871_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out172_: Wrappers.Result
            out172_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
            d_871_valueOrError0_ = out172_
            if (d_871_valueOrError0_).IsFailure():
                output = (d_871_valueOrError0_).PropagateFailure()
                return output
            d_870___v2_ = (d_871_valueOrError0_).Extract()
        if ((self).entryCapacity) == ((self.cache).Size()):
            d_872___v3_: tuple
            d_873_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out173_: Wrappers.Result
            out173_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
            d_873_valueOrError1_ = out173_
            if (d_873_valueOrError1_).IsFailure():
                output = (d_873_valueOrError1_).PropagateFailure()
                return output
            d_872___v3_ = (d_873_valueOrError1_).Extract()
        d_874_cell_: LocalCMC.CacheEntry
        nw31_ = LocalCMC.CacheEntry()
        nw31_.ctor__((input).materials, (input).identifier, (input).creationTime, (input).expiryTime, ((input).messagesUsed).UnwrapOr(0), ((input).bytesUsed).UnwrapOr(0))
        d_874_cell_ = nw31_
        (self.queue).pushCell(d_874_cell_)
        (self.cache).Put((input).identifier, d_874_cell_)
        output = Wrappers.Result_Success(())
        return output

    def DeleteCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_875_cell_: LocalCMC.CacheEntry
            d_875_cell_ = (self.cache).Select((input).identifier)
            with _dafny.label("1"):
                (self.cache).Remove((input).identifier)
                pass
            (self.queue).remove(d_875_cell_)
        output = Wrappers.Result_Success(())
        return output

    def UpdateUsageMetadata_k(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_876_cell_: LocalCMC.CacheEntry
            d_876_cell_ = (self.cache).Select((input).identifier)
            if ((d_876_cell_.messagesUsed) <= (((LocalCMC.default__).INT32__MAX__VALUE) - (1))) and ((d_876_cell_.bytesUsed) <= (((LocalCMC.default__).INT32__MAX__VALUE) - ((input).bytesUsed))):
                rhs0_: BoundedInts.int32 = (d_876_cell_.messagesUsed) + (1)
                rhs1_: BoundedInts.int32 = (d_876_cell_.bytesUsed) + ((input).bytesUsed)
                lhs0_: LocalCMC.CacheEntry = d_876_cell_
                lhs1_: LocalCMC.CacheEntry = d_876_cell_
                lhs0_.messagesUsed = rhs0_
                lhs1_.bytesUsed = rhs1_
            elif True:
                d_877___v4_: tuple
                d_878_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
                out174_: Wrappers.Result
                out174_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_878_valueOrError0_ = out174_
                if (d_878_valueOrError0_).IsFailure():
                    output = (d_878_valueOrError0_).PropagateFailure()
                    return output
                d_877___v4_ = (d_878_valueOrError0_).Extract()
        output = Wrappers.Result_Success(())
        return output
        return output

    def pruning(self, now):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        hi7_: int = (self).entryPruningTailSize
        for d_879_i_ in range(0, hi7_):
            if (self.queue.tail).is_Ptr:
                if (((self.queue.tail).deref).expiryTime) < (now):
                    d_880___v5_: tuple
                    d_881_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
                    out175_: Wrappers.Result
                    out175_ = (self).DeleteCacheEntry_k(software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
                    d_881_valueOrError0_ = out175_
                    if (d_881_valueOrError0_).IsFailure():
                        output = (d_881_valueOrError0_).PropagateFailure()
                        return output
                    d_880___v5_ = (d_881_valueOrError0_).Extract()
                elif True:
                    output = Wrappers.Result_Success(())
                    return output
            elif True:
                output = Wrappers.Result_Success(())
                return output
        output = Wrappers.Result_Success(())
        return output
        return output

    @property
    def entryCapacity(self):
        return self._entryCapacity
    @property
    def entryPruningTailSize(self):
        return self._entryPruningTailSize
