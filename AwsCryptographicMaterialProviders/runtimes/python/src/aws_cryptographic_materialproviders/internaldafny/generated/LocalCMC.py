import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
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

# Module: LocalCMC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RemoveValue(k0, m):
        d_804_m_k_: _dafny.Map
        d_804_m_k_ = (m) - (_dafny.Set({k0}))

    @_dafny.classproperty
    def NULL(instance):
        return Ref_Null()
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
        return isinstance(self, Ref_Ptr)
    @property
    def is_Null(self) -> bool:
        return isinstance(self, Ref_Null)

class Ref_Ptr(Ref, NamedTuple('Ptr', [('deref', Any)])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Ptr({_dafny.string_of(self.deref)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Ref_Ptr) and self.deref == __o.deref
    def __hash__(self) -> int:
        return super().__hash__()

class Ref_Null(Ref, NamedTuple('Null', [])):
    def __dafnystr__(self) -> str:
        return f'LocalCMC.Ref.Null'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Ref_Null)
    def __hash__(self) -> int:
        return super().__hash__()


class CacheEntry:
    def  __init__(self):
        self.prev: Ref = Ref.default()()
        self.next: Ref = Ref.default()()
        self.messagesUsed: int = None
        self.bytesUsed: int = None
        self._i_identifier: _dafny.Seq = _dafny.Seq({})
        self._i_materials: AwsCryptographyMaterialProvidersTypes.Materials = None
        self._i_creationTime: int = None
        self._i_expiryTime: int = None
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.CacheEntry"
    def ctor__(self, materials_k, identifier_k, creationTime_k, expiryTime_k, messagesUsed_k, bytesUsed_k):
        (self)._i_materials = materials_k
        (self)._i_identifier = identifier_k
        (self)._i_creationTime = creationTime_k
        (self)._i_expiryTime = expiryTime_k
        (self).messagesUsed = messagesUsed_k
        (self).bytesUsed = bytesUsed_k
        (self).prev = default__.NULL
        (self).next = default__.NULL

    @property
    def identifier(self):
        return self._i_identifier
    @property
    def materials(self):
        return self._i_materials
    @property
    def creationTime(self):
        return self._i_creationTime
    @property
    def expiryTime(self):
        return self._i_expiryTime

class DoublyLinkedCacheEntryList:
    def  __init__(self):
        self.head: Ref = Ref.default()()
        self.tail: Ref = Ref.default()()
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.DoublyLinkedCacheEntryList"
    def ctor__(self):
        (self).head = Ref_Null()
        (self).tail = Ref_Null()

    def pushCell(self, toPush):
        d_805_cRef_: Ref
        d_805_cRef_ = Ref_Ptr(toPush)
        if (self.head).is_Ptr:
            obj0_ = (self.head).deref
            obj0_.prev = d_805_cRef_
            (toPush).next = self.head
            (self).head = d_805_cRef_
        elif True:
            (self).head = d_805_cRef_
            (self).tail = self.head

    def moveToFront(self, c):
        if ((self.head).deref) != (c):
            d_806_toPush_: Ref
            d_806_toPush_ = Ref_Ptr(c)
            (self).remove(c)
            if (self.head).is_Ptr:
                obj1_ = (self.head).deref
                obj1_.prev = d_806_toPush_
                obj2_ = (d_806_toPush_).deref
                obj2_.next = self.head
                (self).head = d_806_toPush_
            elif True:
                (self).head = d_806_toPush_
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
        (toRemove).next = default__.NULL
        (toRemove).prev = default__.NULL


class LocalCMC(AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache):
    def  __init__(self):
        self.queue: DoublyLinkedCacheEntryList = None
        self.cache: DafnyLibraries.MutableMap = None
        self._i_entryCapacity: int = int(0)
        self._i_entryPruningTailSize: int = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "LocalCMC.LocalCMC"
    def DeleteCacheEntry(self, input):
        out115_: Wrappers.Result
        out115_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache.DeleteCacheEntry(self, input)
        return out115_

    def GetCacheEntry(self, input):
        out116_: Wrappers.Result
        out116_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache.GetCacheEntry(self, input)
        return out116_

    def PutCacheEntry(self, input):
        out117_: Wrappers.Result
        out117_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache.PutCacheEntry(self, input)
        return out117_

    def UpdateUsageMetadata(self, input):
        out118_: Wrappers.Result
        out118_ = AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache.UpdateUsageMetadata(self, input)
        return out118_

    def ctor__(self, entryCapacity_k, entryPruningTailSize_k):
        (self)._i_entryCapacity = entryCapacity_k
        (self)._i_entryPruningTailSize = entryPruningTailSize_k
        nw28_ = DafnyLibraries.MutableMap()
        (self).cache = nw28_
        nw29_ = DoublyLinkedCacheEntryList()
        nw29_.ctor__()
        (self).queue = nw29_

    def GetCacheEntry_k(self, input):
        output: Wrappers.Result = None
        d_807_now_: int
        out119_: int
        out119_ = Time.default__.CurrentRelativeTime()
        d_807_now_ = out119_
        out120_: Wrappers.Result
        out120_ = (self).GetCacheEntryWithTime(input, d_807_now_)
        output = out120_
        return output

    def GetCacheEntryWithTime(self, input, now):
        output: Wrappers.Result = None
        if (self.cache).HasKey((input).identifier):
            d_808_entry_: CacheEntry
            d_808_entry_ = (self.cache).Select((input).identifier)
            if (now) <= ((d_808_entry_).expiryTime):
                (self.queue).moveToFront(d_808_entry_)
                output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput_GetCacheEntryOutput((d_808_entry_).materials, (d_808_entry_).creationTime, (d_808_entry_).expiryTime, d_808_entry_.messagesUsed, d_808_entry_.bytesUsed))
                d_809___v0_: tuple
                d_810_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out121_: Wrappers.Result
                out121_ = (self).pruning(now)
                d_810_valueOrError0_ = out121_
                if (d_810_valueOrError0_).IsFailure():
                    output = (d_810_valueOrError0_).PropagateFailure()
                    return output
                d_809___v0_ = (d_810_valueOrError0_).Extract()
            elif True:
                d_811___v1_: tuple
                d_812_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out122_: Wrappers.Result
                out122_ = (self).DeleteCacheEntry_k(AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_812_valueOrError1_ = out122_
                if (d_812_valueOrError1_).IsFailure():
                    output = (d_812_valueOrError1_).PropagateFailure()
                    return output
                d_811___v1_ = (d_812_valueOrError1_).Extract()
                output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(_dafny.Seq("Entry past TTL")))
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
        return output

    def PutCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if ((self).entryCapacity) == (0):
            output = Wrappers.Result_Success(())
            return output
        if (self.cache).HasKey((input).identifier):
            d_813___v2_: tuple
            d_814_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out123_: Wrappers.Result
            out123_ = (self).DeleteCacheEntry_k(AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
            d_814_valueOrError0_ = out123_
            if (d_814_valueOrError0_).IsFailure():
                output = (d_814_valueOrError0_).PropagateFailure()
                return output
            d_813___v2_ = (d_814_valueOrError0_).Extract()
        if ((self).entryCapacity) == ((self.cache).Size()):
            d_815___v3_: tuple
            d_816_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out124_: Wrappers.Result
            out124_ = (self).DeleteCacheEntry_k(AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
            d_816_valueOrError1_ = out124_
            if (d_816_valueOrError1_).IsFailure():
                output = (d_816_valueOrError1_).PropagateFailure()
                return output
            d_815___v3_ = (d_816_valueOrError1_).Extract()
        d_817_cell_: CacheEntry
        nw30_ = CacheEntry()
        nw30_.ctor__((input).materials, (input).identifier, (input).creationTime, (input).expiryTime, ((input).messagesUsed).UnwrapOr(0), ((input).bytesUsed).UnwrapOr(0))
        d_817_cell_ = nw30_
        (self.queue).pushCell(d_817_cell_)
        (self.cache).Put((input).identifier, d_817_cell_)
        output = Wrappers.Result_Success(())
        return output

    def DeleteCacheEntry_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_818_cell_: CacheEntry
            d_818_cell_ = (self.cache).Select((input).identifier)
            with _dafny.label("1"):
                (self.cache).Remove((input).identifier)
                pass
            (self.queue).remove(d_818_cell_)
        output = Wrappers.Result_Success(())
        return output

    def UpdateUsageMetadata_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        if (self.cache).HasKey((input).identifier):
            d_819_cell_: CacheEntry
            d_819_cell_ = (self.cache).Select((input).identifier)
            if ((d_819_cell_.messagesUsed) <= ((default__.INT32__MAX__VALUE) - (1))) and ((d_819_cell_.bytesUsed) <= ((default__.INT32__MAX__VALUE) - ((input).bytesUsed))):
                rhs0_ = (d_819_cell_.messagesUsed) + (1)
                rhs1_ = (d_819_cell_.bytesUsed) + ((input).bytesUsed)
                lhs0_ = d_819_cell_
                lhs1_ = d_819_cell_
                lhs0_.messagesUsed = rhs0_
                lhs1_.bytesUsed = rhs1_
            elif True:
                d_820___v4_: tuple
                d_821_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                out125_: Wrappers.Result
                out125_ = (self).DeleteCacheEntry_k(AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput((input).identifier))
                d_821_valueOrError0_ = out125_
                if (d_821_valueOrError0_).IsFailure():
                    output = (d_821_valueOrError0_).PropagateFailure()
                    return output
                d_820___v4_ = (d_821_valueOrError0_).Extract()
        output = Wrappers.Result_Success(())
        return output
        return output

    def pruning(self, now):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        hi6_ = (self).entryPruningTailSize
        for d_822_i_ in range(0, hi6_):
            if (self.queue.tail).is_Ptr:
                if (((self.queue.tail).deref).expiryTime) < (now):
                    d_823___v5_: tuple
                    d_824_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                    out126_: Wrappers.Result
                    out126_ = (self).DeleteCacheEntry_k(AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput_DeleteCacheEntryInput(((self.queue.tail).deref).identifier))
                    d_824_valueOrError0_ = out126_
                    if (d_824_valueOrError0_).IsFailure():
                        output = (d_824_valueOrError0_).PropagateFailure()
                        return output
                    d_823___v5_ = (d_824_valueOrError0_).Extract()
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
        return self._i_entryCapacity
    @property
    def entryPruningTailSize(self):
        return self._i_entryPruningTailSize
