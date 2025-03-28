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

# Module: AwsCryptographyMaterialProvidersTypes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsValid__CountingNumber(x):
        return (1) <= (x)

    @staticmethod
    def IsValid__PositiveInteger(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__PositiveLong(x):
        return (0) <= (x)

    @staticmethod
    def IsDummySubsetType(x):
        return (0) < (x)


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class AesWrappingAlg:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16(), AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16(), AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()]
    @classmethod
    def default(cls, ):
        return lambda: AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES128__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16)
    @property
    def is_ALG__AES192__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16)
    @property
    def is_ALG__AES256__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16)

class AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES128__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()

class AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES192__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES192_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()

class AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES256__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()


class AlgorithmSuiteId:
    @classmethod
    def default(cls, ):
        return lambda: AlgorithmSuiteId_ESDK(ESDKAlgorithmSuiteId.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ESDK(self) -> bool:
        return isinstance(self, AlgorithmSuiteId_ESDK)
    @property
    def is_DBE(self) -> bool:
        return isinstance(self, AlgorithmSuiteId_DBE)

class AlgorithmSuiteId_ESDK(AlgorithmSuiteId, NamedTuple('ESDK', [('ESDK', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId.ESDK({_dafny.string_of(self.ESDK)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSuiteId_ESDK) and self.ESDK == __o.ESDK
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSuiteId_DBE(AlgorithmSuiteId, NamedTuple('DBE', [('DBE', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId.DBE({_dafny.string_of(self.DBE)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSuiteId_DBE) and self.DBE == __o.DBE
    def __hash__(self) -> int:
        return super().__hash__()


class AlgorithmSuiteInfo:
    @classmethod
    def default(cls, ):
        return lambda: AlgorithmSuiteInfo_AlgorithmSuiteInfo(AlgorithmSuiteId.default()(), _dafny.Seq({}), int(0), Encrypt.default()(), DerivationAlgorithm.default()(), DerivationAlgorithm.default()(), SignatureAlgorithm.default()(), SymmetricSignatureAlgorithm.default()(), EdkWrappingAlgorithm.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AlgorithmSuiteInfo(self) -> bool:
        return isinstance(self, AlgorithmSuiteInfo_AlgorithmSuiteInfo)

class AlgorithmSuiteInfo_AlgorithmSuiteInfo(AlgorithmSuiteInfo, NamedTuple('AlgorithmSuiteInfo', [('id', Any), ('binaryId', Any), ('messageVersion', Any), ('encrypt', Any), ('kdf', Any), ('commitment', Any), ('signature', Any), ('symmetricSignature', Any), ('edkWrapping', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.AlgorithmSuiteInfo({_dafny.string_of(self.id)}, {_dafny.string_of(self.binaryId)}, {_dafny.string_of(self.messageVersion)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.kdf)}, {_dafny.string_of(self.commitment)}, {_dafny.string_of(self.signature)}, {_dafny.string_of(self.symmetricSignature)}, {_dafny.string_of(self.edkWrapping)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSuiteInfo_AlgorithmSuiteInfo) and self.id == __o.id and self.binaryId == __o.binaryId and self.messageVersion == __o.messageVersion and self.encrypt == __o.encrypt and self.kdf == __o.kdf and self.commitment == __o.commitment and self.signature == __o.signature and self.symmetricSignature == __o.symmetricSignature and self.edkWrapping == __o.edkWrapping
    def __hash__(self) -> int:
        return super().__hash__()


class IAwsCryptographicMaterialProvidersClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClientCallHistory"

class IAwsCryptographicMaterialProvidersClient:
    pass
    def CreateAwsKmsKeyring(self, input):
        pass

    def CreateAwsKmsDiscoveryKeyring(self, input):
        pass

    def CreateAwsKmsMultiKeyring(self, input):
        pass

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        pass

    def CreateAwsKmsMrkKeyring(self, input):
        pass

    def CreateAwsKmsMrkMultiKeyring(self, input):
        pass

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        pass

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        pass

    def CreateAwsKmsHierarchicalKeyring(self, input):
        pass

    def CreateAwsKmsRsaKeyring(self, input):
        pass

    def CreateAwsKmsEcdhKeyring(self, input):
        pass

    def CreateMultiKeyring(self, input):
        pass

    def CreateRawAesKeyring(self, input):
        pass

    def CreateRawRsaKeyring(self, input):
        pass

    def CreateRawEcdhKeyring(self, input):
        pass

    def CreateDefaultCryptographicMaterialsManager(self, input):
        pass

    def CreateRequiredEncryptionContextCMM(self, input):
        pass

    def CreateCryptographicMaterialsCache(self, input):
        pass

    def CreateDefaultClientSupplier(self, input):
        pass


class IBranchKeyIdSupplierCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplierCallHistory"

class IBranchKeyIdSupplier:
    pass
    @staticmethod
    def GetBranchKeyId(self, input):
        pass

    @staticmethod
    def GetBranchKeyId(self, input):
        output: Wrappers.Result = Wrappers.Result.default(GetBranchKeyIdOutput.default())()
        out0_: Wrappers.Result
        out0_ = (self).GetBranchKeyId_k(input)
        output = out0_
        return output

    def GetBranchKeyId_k(self, input):
        pass


class CacheType:
    @classmethod
    def default(cls, ):
        return lambda: CacheType_Default(DefaultCache.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Default(self) -> bool:
        return isinstance(self, CacheType_Default)
    @property
    def is_No(self) -> bool:
        return isinstance(self, CacheType_No)
    @property
    def is_SingleThreaded(self) -> bool:
        return isinstance(self, CacheType_SingleThreaded)
    @property
    def is_MultiThreaded(self) -> bool:
        return isinstance(self, CacheType_MultiThreaded)
    @property
    def is_StormTracking(self) -> bool:
        return isinstance(self, CacheType_StormTracking)
    @property
    def is_Shared(self) -> bool:
        return isinstance(self, CacheType_Shared)

class CacheType_Default(CacheType, NamedTuple('Default', [('Default', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.Default({_dafny.string_of(self.Default)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_Default) and self.Default == __o.Default
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_No(CacheType, NamedTuple('No', [('No', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.No({_dafny.string_of(self.No)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_No) and self.No == __o.No
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_SingleThreaded(CacheType, NamedTuple('SingleThreaded', [('SingleThreaded', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.SingleThreaded({_dafny.string_of(self.SingleThreaded)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_SingleThreaded) and self.SingleThreaded == __o.SingleThreaded
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_MultiThreaded(CacheType, NamedTuple('MultiThreaded', [('MultiThreaded', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.MultiThreaded({_dafny.string_of(self.MultiThreaded)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_MultiThreaded) and self.MultiThreaded == __o.MultiThreaded
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_StormTracking(CacheType, NamedTuple('StormTracking', [('StormTracking', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.StormTracking({_dafny.string_of(self.StormTracking)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_StormTracking) and self.StormTracking == __o.StormTracking
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_Shared(CacheType, NamedTuple('Shared', [('Shared', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.Shared({_dafny.string_of(self.Shared)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheType_Shared) and self.Shared == __o.Shared
    def __hash__(self) -> int:
        return super().__hash__()


class IClientSupplierCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IClientSupplierCallHistory"

class IClientSupplier:
    pass
    @staticmethod
    def GetClient(self, input):
        pass

    @staticmethod
    def GetClient(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).GetClient_k(input)
        output = out0_
        return output

    def GetClient_k(self, input):
        pass


class CommitmentPolicy:
    @classmethod
    def default(cls, ):
        return lambda: CommitmentPolicy_ESDK(ESDKCommitmentPolicy.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ESDK(self) -> bool:
        return isinstance(self, CommitmentPolicy_ESDK)
    @property
    def is_DBE(self) -> bool:
        return isinstance(self, CommitmentPolicy_DBE)

class CommitmentPolicy_ESDK(CommitmentPolicy, NamedTuple('ESDK', [('ESDK', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.ESDK({_dafny.string_of(self.ESDK)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CommitmentPolicy_ESDK) and self.ESDK == __o.ESDK
    def __hash__(self) -> int:
        return super().__hash__()

class CommitmentPolicy_DBE(CommitmentPolicy, NamedTuple('DBE', [('DBE', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.DBE({_dafny.string_of(self.DBE)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CommitmentPolicy_DBE) and self.DBE == __o.DBE
    def __hash__(self) -> int:
        return super().__hash__()


class CountingNumber:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_0_x_: int = source__
        if True:
            return default__.IsValid__CountingNumber(d_0_x_)
        return False

class CreateAwsKmsDiscoveryKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput(None, Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsDiscoveryKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput)

class CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput(CreateAwsKmsDiscoveryKeyringInput, NamedTuple('CreateAwsKmsDiscoveryKeyringInput', [('kmsClient', Any), ('discoveryFilter', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryKeyringInput.CreateAwsKmsDiscoveryKeyringInput({_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput) and self.kmsClient == __o.kmsClient and self.discoveryFilter == __o.discoveryFilter and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsDiscoveryMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsDiscoveryMultiKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput)

class CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput(CreateAwsKmsDiscoveryMultiKeyringInput, NamedTuple('CreateAwsKmsDiscoveryMultiKeyringInput', [('regions', Any), ('discoveryFilter', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryMultiKeyringInput.CreateAwsKmsDiscoveryMultiKeyringInput({_dafny.string_of(self.regions)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput) and self.regions == __o.regions and self.discoveryFilter == __o.discoveryFilter and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsEcdhKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(KmsEcdhStaticConfigurations.default()(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()(), None, Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsEcdhKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput)

class CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(CreateAwsKmsEcdhKeyringInput, NamedTuple('CreateAwsKmsEcdhKeyringInput', [('KeyAgreementScheme', Any), ('curveSpec', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput.CreateAwsKmsEcdhKeyringInput({_dafny.string_of(self.KeyAgreementScheme)}, {_dafny.string_of(self.curveSpec)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput) and self.KeyAgreementScheme == __o.KeyAgreementScheme and self.curveSpec == __o.curveSpec and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsHierarchicalKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option.default()(), Wrappers.Option.default()(), None, int(0), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsHierarchicalKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput)

class CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(CreateAwsKmsHierarchicalKeyringInput, NamedTuple('CreateAwsKmsHierarchicalKeyringInput', [('branchKeyId', Any), ('branchKeyIdSupplier', Any), ('keyStore', Any), ('ttlSeconds', Any), ('cache', Any), ('partitionId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput.CreateAwsKmsHierarchicalKeyringInput({_dafny.string_of(self.branchKeyId)}, {_dafny.string_of(self.branchKeyIdSupplier)}, {_dafny.string_of(self.keyStore)}, {_dafny.string_of(self.ttlSeconds)}, {_dafny.string_of(self.cache)}, {_dafny.string_of(self.partitionId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput) and self.branchKeyId == __o.branchKeyId and self.branchKeyIdSupplier == __o.branchKeyIdSupplier and self.keyStore == __o.keyStore and self.ttlSeconds == __o.ttlSeconds and self.cache == __o.cache and self.partitionId == __o.partitionId
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(_dafny.Seq(""), None, Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput)

class CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(CreateAwsKmsKeyringInput, NamedTuple('CreateAwsKmsKeyringInput', [('kmsKeyId', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput.CreateAwsKmsKeyringInput({_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput) and self.kmsKeyId == __o.kmsKeyId and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkDiscoveryKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput(None, Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkDiscoveryKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput)

class CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput(CreateAwsKmsMrkDiscoveryKeyringInput, NamedTuple('CreateAwsKmsMrkDiscoveryKeyringInput', [('kmsClient', Any), ('discoveryFilter', Any), ('grantTokens', Any), ('region', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryKeyringInput.CreateAwsKmsMrkDiscoveryKeyringInput({_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput) and self.kmsClient == __o.kmsClient and self.discoveryFilter == __o.discoveryFilter and self.grantTokens == __o.grantTokens and self.region == __o.region
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkDiscoveryMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkDiscoveryMultiKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput)

class CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(CreateAwsKmsMrkDiscoveryMultiKeyringInput, NamedTuple('CreateAwsKmsMrkDiscoveryMultiKeyringInput', [('regions', Any), ('discoveryFilter', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput.CreateAwsKmsMrkDiscoveryMultiKeyringInput({_dafny.string_of(self.regions)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput) and self.regions == __o.regions and self.discoveryFilter == __o.discoveryFilter and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(_dafny.Seq(""), None, Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput)

class CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(CreateAwsKmsMrkKeyringInput, NamedTuple('CreateAwsKmsMrkKeyringInput', [('kmsKeyId', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput.CreateAwsKmsMrkKeyringInput({_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput) and self.kmsKeyId == __o.kmsKeyId and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkMultiKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput)

class CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(CreateAwsKmsMrkMultiKeyringInput, NamedTuple('CreateAwsKmsMrkMultiKeyringInput', [('generator', Any), ('kmsKeyIds', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkMultiKeyringInput.CreateAwsKmsMrkMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.kmsKeyIds)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput) and self.generator == __o.generator and self.kmsKeyIds == __o.kmsKeyIds and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMultiKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput)

class CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput(CreateAwsKmsMultiKeyringInput, NamedTuple('CreateAwsKmsMultiKeyringInput', [('generator', Any), ('kmsKeyIds', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMultiKeyringInput.CreateAwsKmsMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.kmsKeyIds)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput) and self.generator == __o.generator and self.kmsKeyIds == __o.kmsKeyIds and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsRsaKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option.default()(), _dafny.Seq(""), ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsRsaKeyringInput(self) -> bool:
        return isinstance(self, CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput)

class CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(CreateAwsKmsRsaKeyringInput, NamedTuple('CreateAwsKmsRsaKeyringInput', [('publicKey', Any), ('kmsKeyId', Any), ('encryptionAlgorithm', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput.CreateAwsKmsRsaKeyringInput({_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.encryptionAlgorithm)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput) and self.publicKey == __o.publicKey and self.kmsKeyId == __o.kmsKeyId and self.encryptionAlgorithm == __o.encryptionAlgorithm and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateCryptographicMaterialsCacheInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(CacheType.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateCryptographicMaterialsCacheInput(self) -> bool:
        return isinstance(self, CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput)

class CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(CreateCryptographicMaterialsCacheInput, NamedTuple('CreateCryptographicMaterialsCacheInput', [('cache', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput.CreateCryptographicMaterialsCacheInput({_dafny.string_of(self.cache)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput) and self.cache == __o.cache
    def __hash__(self) -> int:
        return super().__hash__()


class CreateDefaultClientSupplierInput:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput()]
    @classmethod
    def default(cls, ):
        return lambda: CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateDefaultClientSupplierInput(self) -> bool:
        return isinstance(self, CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput)

class CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput(CreateDefaultClientSupplierInput, NamedTuple('CreateDefaultClientSupplierInput', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput.CreateDefaultClientSupplierInput'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput)
    def __hash__(self) -> int:
        return super().__hash__()


class CreateDefaultCryptographicMaterialsManagerInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateDefaultCryptographicMaterialsManagerInput(self) -> bool:
        return isinstance(self, CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput)

class CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(CreateDefaultCryptographicMaterialsManagerInput, NamedTuple('CreateDefaultCryptographicMaterialsManagerInput', [('keyring', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput.CreateDefaultCryptographicMaterialsManagerInput({_dafny.string_of(self.keyring)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput) and self.keyring == __o.keyring
    def __hash__(self) -> int:
        return super().__hash__()


class CreateMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateMultiKeyringInput(self) -> bool:
        return isinstance(self, CreateMultiKeyringInput_CreateMultiKeyringInput)

class CreateMultiKeyringInput_CreateMultiKeyringInput(CreateMultiKeyringInput, NamedTuple('CreateMultiKeyringInput', [('generator', Any), ('childKeyrings', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput.CreateMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.childKeyrings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateMultiKeyringInput_CreateMultiKeyringInput) and self.generator == __o.generator and self.childKeyrings == __o.childKeyrings
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRawAesKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRawAesKeyringInput_CreateRawAesKeyringInput(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq({}), AesWrappingAlg.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRawAesKeyringInput(self) -> bool:
        return isinstance(self, CreateRawAesKeyringInput_CreateRawAesKeyringInput)

class CreateRawAesKeyringInput_CreateRawAesKeyringInput(CreateRawAesKeyringInput, NamedTuple('CreateRawAesKeyringInput', [('keyNamespace', Any), ('keyName', Any), ('wrappingKey', Any), ('wrappingAlg', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput.CreateRawAesKeyringInput({_dafny.string_of(self.keyNamespace)}, {_dafny.string_of(self.keyName)}, {_dafny.string_of(self.wrappingKey)}, {_dafny.string_of(self.wrappingAlg)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateRawAesKeyringInput_CreateRawAesKeyringInput) and self.keyNamespace == __o.keyNamespace and self.keyName == __o.keyName and self.wrappingKey == __o.wrappingKey and self.wrappingAlg == __o.wrappingAlg
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRawEcdhKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(RawEcdhStaticConfigurations.default()(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRawEcdhKeyringInput(self) -> bool:
        return isinstance(self, CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput)

class CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(CreateRawEcdhKeyringInput, NamedTuple('CreateRawEcdhKeyringInput', [('KeyAgreementScheme', Any), ('curveSpec', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput.CreateRawEcdhKeyringInput({_dafny.string_of(self.KeyAgreementScheme)}, {_dafny.string_of(self.curveSpec)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput) and self.KeyAgreementScheme == __o.KeyAgreementScheme and self.curveSpec == __o.curveSpec
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRawRsaKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(_dafny.Seq(""), _dafny.Seq(""), PaddingScheme.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRawRsaKeyringInput(self) -> bool:
        return isinstance(self, CreateRawRsaKeyringInput_CreateRawRsaKeyringInput)

class CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(CreateRawRsaKeyringInput, NamedTuple('CreateRawRsaKeyringInput', [('keyNamespace', Any), ('keyName', Any), ('paddingScheme', Any), ('publicKey', Any), ('privateKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput.CreateRawRsaKeyringInput({_dafny.string_of(self.keyNamespace)}, {_dafny.string_of(self.keyName)}, {_dafny.string_of(self.paddingScheme)}, {_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.privateKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateRawRsaKeyringInput_CreateRawRsaKeyringInput) and self.keyNamespace == __o.keyNamespace and self.keyName == __o.keyName and self.paddingScheme == __o.paddingScheme and self.publicKey == __o.publicKey and self.privateKey == __o.privateKey
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRequiredEncryptionContextCMMInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRequiredEncryptionContextCMMInput(self) -> bool:
        return isinstance(self, CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput)

class CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(CreateRequiredEncryptionContextCMMInput, NamedTuple('CreateRequiredEncryptionContextCMMInput', [('underlyingCMM', Any), ('keyring', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput.CreateRequiredEncryptionContextCMMInput({_dafny.string_of(self.underlyingCMM)}, {_dafny.string_of(self.keyring)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput) and self.underlyingCMM == __o.underlyingCMM and self.keyring == __o.keyring and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class ICryptographicMaterialsCacheCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCacheCallHistory"

class ICryptographicMaterialsCache:
    pass
    @staticmethod
    def PutCacheEntry(self, input):
        pass

    @staticmethod
    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out0_: Wrappers.Result
        out0_ = (self).PutCacheEntry_k(input)
        output = out0_
        return output

    def PutCacheEntry_k(self, input):
        pass

    @staticmethod
    def UpdateUsageMetadata(self, input):
        pass

    @staticmethod
    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out0_: Wrappers.Result
        out0_ = (self).UpdateUsageMetadata_k(input)
        output = out0_
        return output

    def UpdateUsageMetadata_k(self, input):
        pass

    @staticmethod
    def GetCacheEntry(self, input):
        pass

    @staticmethod
    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).GetCacheEntry_k(input)
        output = out0_
        return output

    def GetCacheEntry_k(self, input):
        pass

    @staticmethod
    def DeleteCacheEntry(self, input):
        pass

    @staticmethod
    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out0_: Wrappers.Result
        out0_ = (self).DeleteCacheEntry_k(input)
        output = out0_
        return output

    def DeleteCacheEntry_k(self, input):
        pass


class ICryptographicMaterialsManagerCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManagerCallHistory"

class ICryptographicMaterialsManager:
    pass
    @staticmethod
    def GetEncryptionMaterials(self, input):
        pass

    @staticmethod
    def GetEncryptionMaterials(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).GetEncryptionMaterials_k(input)
        output = out0_
        return output

    def GetEncryptionMaterials_k(self, input):
        pass

    @staticmethod
    def DecryptMaterials(self, input):
        pass

    @staticmethod
    def DecryptMaterials(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).DecryptMaterials_k(input)
        output = out0_
        return output

    def DecryptMaterials_k(self, input):
        pass


class DBEAlgorithmSuiteId:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(), DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()]
    @classmethod
    def default(cls, ):
        return lambda: DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(self) -> bool:
        return isinstance(self, DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(self) -> bool:
        return isinstance(self, DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384)

class DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(DBEAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384)
    def __hash__(self) -> int:
        return super().__hash__()

class DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(DBEAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384_SYMSIG_HMAC_SHA384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384)
    def __hash__(self) -> int:
        return super().__hash__()


class DBECommitmentPolicy:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(self) -> bool:
        return isinstance(self, DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)

class DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(DBECommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__REQUIRE__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptionMaterials:
    @classmethod
    def default(cls, ):
        return lambda: DecryptionMaterials_DecryptionMaterials(AlgorithmSuiteInfo.default()(), _dafny.Map({}), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptionMaterials(self) -> bool:
        return isinstance(self, DecryptionMaterials_DecryptionMaterials)

class DecryptionMaterials_DecryptionMaterials(DecryptionMaterials, NamedTuple('DecryptionMaterials', [('algorithmSuite', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('verificationKey', Any), ('symmetricSigningKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.DecryptionMaterials({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.symmetricSigningKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptionMaterials_DecryptionMaterials) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.verificationKey == __o.verificationKey and self.symmetricSigningKey == __o.symmetricSigningKey
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: DecryptMaterialsInput_DecryptMaterialsInput(AlgorithmSuiteId.default()(), CommitmentPolicy.default()(), _dafny.Seq({}), _dafny.Map({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptMaterialsInput(self) -> bool:
        return isinstance(self, DecryptMaterialsInput_DecryptMaterialsInput)

class DecryptMaterialsInput_DecryptMaterialsInput(DecryptMaterialsInput, NamedTuple('DecryptMaterialsInput', [('algorithmSuiteId', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput.DecryptMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptMaterialsInput_DecryptMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptMaterialsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DecryptMaterialsOutput_DecryptMaterialsOutput(DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptMaterialsOutput(self) -> bool:
        return isinstance(self, DecryptMaterialsOutput_DecryptMaterialsOutput)

class DecryptMaterialsOutput_DecryptMaterialsOutput(DecryptMaterialsOutput, NamedTuple('DecryptMaterialsOutput', [('decryptionMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput.DecryptMaterialsOutput({_dafny.string_of(self.decryptionMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptMaterialsOutput_DecryptMaterialsOutput) and self.decryptionMaterials == __o.decryptionMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class DefaultCache:
    @classmethod
    def default(cls, ):
        return lambda: DefaultCache_DefaultCache(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DefaultCache(self) -> bool:
        return isinstance(self, DefaultCache_DefaultCache)

class DefaultCache_DefaultCache(DefaultCache, NamedTuple('DefaultCache', [('entryCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DefaultCache.DefaultCache({_dafny.string_of(self.entryCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DefaultCache_DefaultCache) and self.entryCapacity == __o.entryCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteCacheEntryInput_DeleteCacheEntryInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteCacheEntryInput(self) -> bool:
        return isinstance(self, DeleteCacheEntryInput_DeleteCacheEntryInput)

class DeleteCacheEntryInput_DeleteCacheEntryInput(DeleteCacheEntryInput, NamedTuple('DeleteCacheEntryInput', [('identifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput.DeleteCacheEntryInput({_dafny.string_of(self.identifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteCacheEntryInput_DeleteCacheEntryInput) and self.identifier == __o.identifier
    def __hash__(self) -> int:
        return super().__hash__()


class DerivationAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: DerivationAlgorithm_HKDF(HKDF.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HKDF(self) -> bool:
        return isinstance(self, DerivationAlgorithm_HKDF)
    @property
    def is_IDENTITY(self) -> bool:
        return isinstance(self, DerivationAlgorithm_IDENTITY)
    @property
    def is_None(self) -> bool:
        return isinstance(self, DerivationAlgorithm_None)

class DerivationAlgorithm_HKDF(DerivationAlgorithm, NamedTuple('HKDF', [('HKDF', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.HKDF({_dafny.string_of(self.HKDF)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DerivationAlgorithm_HKDF) and self.HKDF == __o.HKDF
    def __hash__(self) -> int:
        return super().__hash__()

class DerivationAlgorithm_IDENTITY(DerivationAlgorithm, NamedTuple('IDENTITY', [('IDENTITY', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.IDENTITY({_dafny.string_of(self.IDENTITY)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DerivationAlgorithm_IDENTITY) and self.IDENTITY == __o.IDENTITY
    def __hash__(self) -> int:
        return super().__hash__()

class DerivationAlgorithm_None(DerivationAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DerivationAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class DIRECT__KEY__WRAPPING:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()]
    @classmethod
    def default(cls, ):
        return lambda: DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DIRECT__KEY__WRAPPING(self) -> bool:
        return isinstance(self, DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING)

class DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING, NamedTuple('DIRECT__KEY__WRAPPING', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DIRECT_KEY_WRAPPING.DIRECT_KEY_WRAPPING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING)
    def __hash__(self) -> int:
        return super().__hash__()


class DiscoveryFilter:
    @classmethod
    def default(cls, ):
        return lambda: DiscoveryFilter_DiscoveryFilter(_dafny.Seq({}), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DiscoveryFilter(self) -> bool:
        return isinstance(self, DiscoveryFilter_DiscoveryFilter)

class DiscoveryFilter_DiscoveryFilter(DiscoveryFilter, NamedTuple('DiscoveryFilter', [('accountIds', Any), ('partition', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DiscoveryFilter.DiscoveryFilter({_dafny.string_of(self.accountIds)}, {_dafny.string_of(self.partition)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DiscoveryFilter_DiscoveryFilter) and self.accountIds == __o.accountIds and self.partition == __o.partition
    def __hash__(self) -> int:
        return super().__hash__()


class ECDSA:
    @classmethod
    def default(cls, ):
        return lambda: ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSA(self) -> bool:
        return isinstance(self, ECDSA_ECDSA)

class ECDSA_ECDSA(ECDSA, NamedTuple('ECDSA', [('curve', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ECDSA.ECDSA({_dafny.string_of(self.curve)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ECDSA_ECDSA) and self.curve == __o.curve
    def __hash__(self) -> int:
        return super().__hash__()


class EdkWrappingAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DIRECT__KEY__WRAPPING(self) -> bool:
        return isinstance(self, EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING)
    @property
    def is_IntermediateKeyWrapping(self) -> bool:
        return isinstance(self, EdkWrappingAlgorithm_IntermediateKeyWrapping)

class EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(EdkWrappingAlgorithm, NamedTuple('DIRECT__KEY__WRAPPING', [('DIRECT__KEY__WRAPPING', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.DIRECT_KEY_WRAPPING({_dafny.string_of(self.DIRECT__KEY__WRAPPING)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING) and self.DIRECT__KEY__WRAPPING == __o.DIRECT__KEY__WRAPPING
    def __hash__(self) -> int:
        return super().__hash__()

class EdkWrappingAlgorithm_IntermediateKeyWrapping(EdkWrappingAlgorithm, NamedTuple('IntermediateKeyWrapping', [('IntermediateKeyWrapping', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.IntermediateKeyWrapping({_dafny.string_of(self.IntermediateKeyWrapping)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EdkWrappingAlgorithm_IntermediateKeyWrapping) and self.IntermediateKeyWrapping == __o.IntermediateKeyWrapping
    def __hash__(self) -> int:
        return super().__hash__()


class Encrypt:
    @classmethod
    def default(cls, ):
        return lambda: Encrypt_AES__GCM(AwsCryptographyPrimitivesTypes.AES__GCM.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES__GCM(self) -> bool:
        return isinstance(self, Encrypt_AES__GCM)

class Encrypt_AES__GCM(Encrypt, NamedTuple('AES__GCM', [('AES__GCM', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Encrypt.AES_GCM({_dafny.string_of(self.AES__GCM)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Encrypt_AES__GCM) and self.AES__GCM == __o.AES__GCM
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptedDataKey:
    @classmethod
    def default(cls, ):
        return lambda: EncryptedDataKey_EncryptedDataKey(UTF8.ValidUTF8Bytes.default(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptedDataKey(self) -> bool:
        return isinstance(self, EncryptedDataKey_EncryptedDataKey)

class EncryptedDataKey_EncryptedDataKey(EncryptedDataKey, NamedTuple('EncryptedDataKey', [('keyProviderId', Any), ('keyProviderInfo', Any), ('ciphertext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.EncryptedDataKey({_dafny.string_of(self.keyProviderId)}, {_dafny.string_of(self.keyProviderInfo)}, {_dafny.string_of(self.ciphertext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptedDataKey_EncryptedDataKey) and self.keyProviderId == __o.keyProviderId and self.keyProviderInfo == __o.keyProviderInfo and self.ciphertext == __o.ciphertext
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptionMaterials:
    @classmethod
    def default(cls, ):
        return lambda: EncryptionMaterials_EncryptionMaterials(AlgorithmSuiteInfo.default()(), _dafny.Map({}), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptionMaterials(self) -> bool:
        return isinstance(self, EncryptionMaterials_EncryptionMaterials)

class EncryptionMaterials_EncryptionMaterials(EncryptionMaterials, NamedTuple('EncryptionMaterials', [('algorithmSuite', Any), ('encryptionContext', Any), ('encryptedDataKeys', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('signingKey', Any), ('symmetricSigningKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EncryptionMaterials.EncryptionMaterials({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.symmetricSigningKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptionMaterials_EncryptionMaterials) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.encryptedDataKeys == __o.encryptedDataKeys and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.signingKey == __o.signingKey and self.symmetricSigningKeys == __o.symmetricSigningKeys
    def __hash__(self) -> int:
        return super().__hash__()


class EphemeralPrivateKeyToStaticPublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EphemeralPrivateKeyToStaticPublicKeyInput(self) -> bool:
        return isinstance(self, EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput)

class EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(EphemeralPrivateKeyToStaticPublicKeyInput, NamedTuple('EphemeralPrivateKeyToStaticPublicKeyInput', [('recipientPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput.EphemeralPrivateKeyToStaticPublicKeyInput({_dafny.string_of(self.recipientPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput) and self.recipientPublicKey == __o.recipientPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class ESDKAlgorithmSuiteId:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()]
    @classmethod
    def default(cls, ):
        return lambda: ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(self) -> bool:
        return isinstance(self, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384)

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()


class ESDKCommitmentPolicy:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT(), ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT(), ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_FORBID__ENCRYPT__ALLOW__DECRYPT(self) -> bool:
        return isinstance(self, ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT)
    @property
    def is_REQUIRE__ENCRYPT__ALLOW__DECRYPT(self) -> bool:
        return isinstance(self, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT)
    @property
    def is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(self) -> bool:
        return isinstance(self, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)

class ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT(ESDKCommitmentPolicy, NamedTuple('FORBID__ENCRYPT__ALLOW__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT(ESDKCommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__ALLOW__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(ESDKCommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__REQUIRE__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyIdInput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyIdInput_GetBranchKeyIdInput(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyIdInput(self) -> bool:
        return isinstance(self, GetBranchKeyIdInput_GetBranchKeyIdInput)

class GetBranchKeyIdInput_GetBranchKeyIdInput(GetBranchKeyIdInput, NamedTuple('GetBranchKeyIdInput', [('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput.GetBranchKeyIdInput({_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBranchKeyIdInput_GetBranchKeyIdInput) and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyIdOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyIdOutput_GetBranchKeyIdOutput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyIdOutput(self) -> bool:
        return isinstance(self, GetBranchKeyIdOutput_GetBranchKeyIdOutput)

class GetBranchKeyIdOutput_GetBranchKeyIdOutput(GetBranchKeyIdOutput, NamedTuple('GetBranchKeyIdOutput', [('branchKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.GetBranchKeyIdOutput({_dafny.string_of(self.branchKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBranchKeyIdOutput_GetBranchKeyIdOutput) and self.branchKeyId == __o.branchKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class GetCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: GetCacheEntryInput_GetCacheEntryInput(_dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetCacheEntryInput(self) -> bool:
        return isinstance(self, GetCacheEntryInput_GetCacheEntryInput)

class GetCacheEntryInput_GetCacheEntryInput(GetCacheEntryInput, NamedTuple('GetCacheEntryInput', [('identifier', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput.GetCacheEntryInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetCacheEntryInput_GetCacheEntryInput) and self.identifier == __o.identifier and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class GetCacheEntryOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetCacheEntryOutput_GetCacheEntryOutput(Materials.default()(), int(0), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetCacheEntryOutput(self) -> bool:
        return isinstance(self, GetCacheEntryOutput_GetCacheEntryOutput)

class GetCacheEntryOutput_GetCacheEntryOutput(GetCacheEntryOutput, NamedTuple('GetCacheEntryOutput', [('materials', Any), ('creationTime', Any), ('expiryTime', Any), ('messagesUsed', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput.GetCacheEntryOutput({_dafny.string_of(self.materials)}, {_dafny.string_of(self.creationTime)}, {_dafny.string_of(self.expiryTime)}, {_dafny.string_of(self.messagesUsed)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetCacheEntryOutput_GetCacheEntryOutput) and self.materials == __o.materials and self.creationTime == __o.creationTime and self.expiryTime == __o.expiryTime and self.messagesUsed == __o.messagesUsed and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class GetClientInput:
    @classmethod
    def default(cls, ):
        return lambda: GetClientInput_GetClientInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetClientInput(self) -> bool:
        return isinstance(self, GetClientInput_GetClientInput)

class GetClientInput_GetClientInput(GetClientInput, NamedTuple('GetClientInput', [('region', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetClientInput.GetClientInput({_dafny.string_of(self.region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetClientInput_GetClientInput) and self.region == __o.region
    def __hash__(self) -> int:
        return super().__hash__()


class GetEncryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(_dafny.Map({}), CommitmentPolicy.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetEncryptionMaterialsInput(self) -> bool:
        return isinstance(self, GetEncryptionMaterialsInput_GetEncryptionMaterialsInput)

class GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(GetEncryptionMaterialsInput, NamedTuple('GetEncryptionMaterialsInput', [('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuiteId', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput.GetEncryptionMaterialsInput({_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetEncryptionMaterialsInput_GetEncryptionMaterialsInput) and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuiteId == __o.algorithmSuiteId and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class GetEncryptionMaterialsOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput(EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetEncryptionMaterialsOutput(self) -> bool:
        return isinstance(self, GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput)

class GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput(GetEncryptionMaterialsOutput, NamedTuple('GetEncryptionMaterialsOutput', [('encryptionMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput.GetEncryptionMaterialsOutput({_dafny.string_of(self.encryptionMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput) and self.encryptionMaterials == __o.encryptionMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class HKDF:
    @classmethod
    def default(cls, ):
        return lambda: HKDF_HKDF(AwsCryptographyPrimitivesTypes.DigestAlgorithm.default()(), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HKDF(self) -> bool:
        return isinstance(self, HKDF_HKDF)

class HKDF_HKDF(HKDF, NamedTuple('HKDF', [('hmac', Any), ('saltLength', Any), ('inputKeyLength', Any), ('outputKeyLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.HKDF.HKDF({_dafny.string_of(self.hmac)}, {_dafny.string_of(self.saltLength)}, {_dafny.string_of(self.inputKeyLength)}, {_dafny.string_of(self.outputKeyLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HKDF_HKDF) and self.hmac == __o.hmac and self.saltLength == __o.saltLength and self.inputKeyLength == __o.inputKeyLength and self.outputKeyLength == __o.outputKeyLength
    def __hash__(self) -> int:
        return super().__hash__()


class IDENTITY:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [IDENTITY_IDENTITY()]
    @classmethod
    def default(cls, ):
        return lambda: IDENTITY_IDENTITY()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IDENTITY(self) -> bool:
        return isinstance(self, IDENTITY_IDENTITY)

class IDENTITY_IDENTITY(IDENTITY, NamedTuple('IDENTITY', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.IDENTITY.IDENTITY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IDENTITY_IDENTITY)
    def __hash__(self) -> int:
        return super().__hash__()


class InitializeDecryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(AlgorithmSuiteId.default()(), _dafny.Map({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InitializeDecryptionMaterialsInput(self) -> bool:
        return isinstance(self, InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput)

class InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(InitializeDecryptionMaterialsInput, NamedTuple('InitializeDecryptionMaterialsInput', [('algorithmSuiteId', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput.InitializeDecryptionMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class InitializeEncryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(AlgorithmSuiteId.default()(), _dafny.Map({}), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InitializeEncryptionMaterialsInput(self) -> bool:
        return isinstance(self, InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput)

class InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(InitializeEncryptionMaterialsInput, NamedTuple('InitializeEncryptionMaterialsInput', [('algorithmSuiteId', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any), ('signingKey', Any), ('verificationKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput.InitializeEncryptionMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.verificationKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.signingKey == __o.signingKey and self.verificationKey == __o.verificationKey
    def __hash__(self) -> int:
        return super().__hash__()


class IntermediateKeyWrapping:
    @classmethod
    def default(cls, ):
        return lambda: IntermediateKeyWrapping_IntermediateKeyWrapping(DerivationAlgorithm.default()(), DerivationAlgorithm.default()(), Encrypt.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IntermediateKeyWrapping(self) -> bool:
        return isinstance(self, IntermediateKeyWrapping_IntermediateKeyWrapping)

class IntermediateKeyWrapping_IntermediateKeyWrapping(IntermediateKeyWrapping, NamedTuple('IntermediateKeyWrapping', [('keyEncryptionKeyKdf', Any), ('macKeyKdf', Any), ('pdkEncryptAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.IntermediateKeyWrapping.IntermediateKeyWrapping({_dafny.string_of(self.keyEncryptionKeyKdf)}, {_dafny.string_of(self.macKeyKdf)}, {_dafny.string_of(self.pdkEncryptAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping_IntermediateKeyWrapping) and self.keyEncryptionKeyKdf == __o.keyEncryptionKeyKdf and self.macKeyKdf == __o.macKeyKdf and self.pdkEncryptAlgorithm == __o.pdkEncryptAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class KeyAgreementScheme:
    @classmethod
    def default(cls, ):
        return lambda: KeyAgreementScheme_StaticConfiguration(StaticConfigurations.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StaticConfiguration(self) -> bool:
        return isinstance(self, KeyAgreementScheme_StaticConfiguration)

class KeyAgreementScheme_StaticConfiguration(KeyAgreementScheme, NamedTuple('StaticConfiguration', [('StaticConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.KeyAgreementScheme.StaticConfiguration({_dafny.string_of(self.StaticConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyAgreementScheme_StaticConfiguration) and self.StaticConfiguration == __o.StaticConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class IKeyringCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IKeyringCallHistory"

class IKeyring:
    pass
    @staticmethod
    def OnEncrypt(self, input):
        pass

    @staticmethod
    def OnEncrypt(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).OnEncrypt_k(input)
        output = out0_
        return output

    def OnEncrypt_k(self, input):
        pass

    @staticmethod
    def OnDecrypt(self, input):
        pass

    @staticmethod
    def OnDecrypt(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = (self).OnDecrypt_k(input)
        output = out0_
        return output

    def OnDecrypt_k(self, input):
        pass


class KmsEcdhStaticConfigurations:
    @classmethod
    def default(cls, ):
        return lambda: KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(KmsPublicKeyDiscoveryInput.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsPublicKeyDiscovery(self) -> bool:
        return isinstance(self, KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery)
    @property
    def is_KmsPrivateKeyToStaticPublicKey(self) -> bool:
        return isinstance(self, KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey)

class KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(KmsEcdhStaticConfigurations, NamedTuple('KmsPublicKeyDiscovery', [('KmsPublicKeyDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.KmsPublicKeyDiscovery({_dafny.string_of(self.KmsPublicKeyDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery) and self.KmsPublicKeyDiscovery == __o.KmsPublicKeyDiscovery
    def __hash__(self) -> int:
        return super().__hash__()

class KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(KmsEcdhStaticConfigurations, NamedTuple('KmsPrivateKeyToStaticPublicKey', [('KmsPrivateKeyToStaticPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey({_dafny.string_of(self.KmsPrivateKeyToStaticPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey) and self.KmsPrivateKeyToStaticPublicKey == __o.KmsPrivateKeyToStaticPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class KmsPrivateKeyToStaticPublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(_dafny.Seq(""), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsPrivateKeyToStaticPublicKeyInput(self) -> bool:
        return isinstance(self, KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput)

class KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(KmsPrivateKeyToStaticPublicKeyInput, NamedTuple('KmsPrivateKeyToStaticPublicKeyInput', [('senderKmsIdentifier', Any), ('senderPublicKey', Any), ('recipientPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput.KmsPrivateKeyToStaticPublicKeyInput({_dafny.string_of(self.senderKmsIdentifier)}, {_dafny.string_of(self.senderPublicKey)}, {_dafny.string_of(self.recipientPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput) and self.senderKmsIdentifier == __o.senderKmsIdentifier and self.senderPublicKey == __o.senderPublicKey and self.recipientPublicKey == __o.recipientPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class KmsPublicKeyDiscoveryInput:
    @classmethod
    def default(cls, ):
        return lambda: KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsPublicKeyDiscoveryInput(self) -> bool:
        return isinstance(self, KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput)

class KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(KmsPublicKeyDiscoveryInput, NamedTuple('KmsPublicKeyDiscoveryInput', [('recipientKmsIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput.KmsPublicKeyDiscoveryInput({_dafny.string_of(self.recipientKmsIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput) and self.recipientKmsIdentifier == __o.recipientKmsIdentifier
    def __hash__(self) -> int:
        return super().__hash__()


class MaterialProvidersConfig:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [MaterialProvidersConfig_MaterialProvidersConfig()]
    @classmethod
    def default(cls, ):
        return lambda: MaterialProvidersConfig_MaterialProvidersConfig()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MaterialProvidersConfig(self) -> bool:
        return isinstance(self, MaterialProvidersConfig_MaterialProvidersConfig)

class MaterialProvidersConfig_MaterialProvidersConfig(MaterialProvidersConfig, NamedTuple('MaterialProvidersConfig', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig.MaterialProvidersConfig'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialProvidersConfig_MaterialProvidersConfig)
    def __hash__(self) -> int:
        return super().__hash__()


class Materials:
    @classmethod
    def default(cls, ):
        return lambda: Materials_Encryption(EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Encryption(self) -> bool:
        return isinstance(self, Materials_Encryption)
    @property
    def is_Decryption(self) -> bool:
        return isinstance(self, Materials_Decryption)
    @property
    def is_BranchKey(self) -> bool:
        return isinstance(self, Materials_BranchKey)
    @property
    def is_BeaconKey(self) -> bool:
        return isinstance(self, Materials_BeaconKey)

class Materials_Encryption(Materials, NamedTuple('Encryption', [('Encryption', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.Encryption({_dafny.string_of(self.Encryption)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Materials_Encryption) and self.Encryption == __o.Encryption
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_Decryption(Materials, NamedTuple('Decryption', [('Decryption', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.Decryption({_dafny.string_of(self.Decryption)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Materials_Decryption) and self.Decryption == __o.Decryption
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_BranchKey(Materials, NamedTuple('BranchKey', [('BranchKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.BranchKey({_dafny.string_of(self.BranchKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Materials_BranchKey) and self.BranchKey == __o.BranchKey
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_BeaconKey(Materials, NamedTuple('BeaconKey', [('BeaconKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.BeaconKey({_dafny.string_of(self.BeaconKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Materials_BeaconKey) and self.BeaconKey == __o.BeaconKey
    def __hash__(self) -> int:
        return super().__hash__()


class MultiThreadedCache:
    @classmethod
    def default(cls, ):
        return lambda: MultiThreadedCache_MultiThreadedCache(int(0), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiThreadedCache(self) -> bool:
        return isinstance(self, MultiThreadedCache_MultiThreadedCache)

class MultiThreadedCache_MultiThreadedCache(MultiThreadedCache, NamedTuple('MultiThreadedCache', [('entryCapacity', Any), ('entryPruningTailSize', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.MultiThreadedCache.MultiThreadedCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiThreadedCache_MultiThreadedCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize
    def __hash__(self) -> int:
        return super().__hash__()


class NoCache:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [NoCache_NoCache()]
    @classmethod
    def default(cls, ):
        return lambda: NoCache_NoCache()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NoCache(self) -> bool:
        return isinstance(self, NoCache_NoCache)

class NoCache_NoCache(NoCache, NamedTuple('NoCache', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.NoCache.NoCache'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, NoCache_NoCache)
    def __hash__(self) -> int:
        return super().__hash__()


class None_:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [None__None()]
    @classmethod
    def default(cls, ):
        return lambda: None__None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, None__None)

class None__None(None_, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.None.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, None__None)
    def __hash__(self) -> int:
        return super().__hash__()


class OnDecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: OnDecryptInput_OnDecryptInput(DecryptionMaterials.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnDecryptInput(self) -> bool:
        return isinstance(self, OnDecryptInput_OnDecryptInput)

class OnDecryptInput_OnDecryptInput(OnDecryptInput, NamedTuple('OnDecryptInput', [('materials', Any), ('encryptedDataKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnDecryptInput.OnDecryptInput({_dafny.string_of(self.materials)}, {_dafny.string_of(self.encryptedDataKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OnDecryptInput_OnDecryptInput) and self.materials == __o.materials and self.encryptedDataKeys == __o.encryptedDataKeys
    def __hash__(self) -> int:
        return super().__hash__()


class OnDecryptOutput:
    @classmethod
    def default(cls, ):
        return lambda: OnDecryptOutput_OnDecryptOutput(DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnDecryptOutput(self) -> bool:
        return isinstance(self, OnDecryptOutput_OnDecryptOutput)

class OnDecryptOutput_OnDecryptOutput(OnDecryptOutput, NamedTuple('OnDecryptOutput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnDecryptOutput.OnDecryptOutput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OnDecryptOutput_OnDecryptOutput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class OnEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: OnEncryptInput_OnEncryptInput(EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnEncryptInput(self) -> bool:
        return isinstance(self, OnEncryptInput_OnEncryptInput)

class OnEncryptInput_OnEncryptInput(OnEncryptInput, NamedTuple('OnEncryptInput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnEncryptInput.OnEncryptInput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OnEncryptInput_OnEncryptInput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class OnEncryptOutput:
    @classmethod
    def default(cls, ):
        return lambda: OnEncryptOutput_OnEncryptOutput(EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnEncryptOutput(self) -> bool:
        return isinstance(self, OnEncryptOutput_OnEncryptOutput)

class OnEncryptOutput_OnEncryptOutput(OnEncryptOutput, NamedTuple('OnEncryptOutput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnEncryptOutput.OnEncryptOutput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OnEncryptOutput_OnEncryptOutput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class PaddingScheme:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [PaddingScheme_PKCS1(), PaddingScheme_OAEP__SHA1__MGF1(), PaddingScheme_OAEP__SHA256__MGF1(), PaddingScheme_OAEP__SHA384__MGF1(), PaddingScheme_OAEP__SHA512__MGF1()]
    @classmethod
    def default(cls, ):
        return lambda: PaddingScheme_PKCS1()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PKCS1(self) -> bool:
        return isinstance(self, PaddingScheme_PKCS1)
    @property
    def is_OAEP__SHA1__MGF1(self) -> bool:
        return isinstance(self, PaddingScheme_OAEP__SHA1__MGF1)
    @property
    def is_OAEP__SHA256__MGF1(self) -> bool:
        return isinstance(self, PaddingScheme_OAEP__SHA256__MGF1)
    @property
    def is_OAEP__SHA384__MGF1(self) -> bool:
        return isinstance(self, PaddingScheme_OAEP__SHA384__MGF1)
    @property
    def is_OAEP__SHA512__MGF1(self) -> bool:
        return isinstance(self, PaddingScheme_OAEP__SHA512__MGF1)

class PaddingScheme_PKCS1(PaddingScheme, NamedTuple('PKCS1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.PKCS1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PaddingScheme_PKCS1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA1__MGF1(PaddingScheme, NamedTuple('OAEP__SHA1__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA1_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PaddingScheme_OAEP__SHA1__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA256__MGF1(PaddingScheme, NamedTuple('OAEP__SHA256__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA256_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PaddingScheme_OAEP__SHA256__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA384__MGF1(PaddingScheme, NamedTuple('OAEP__SHA384__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA384_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PaddingScheme_OAEP__SHA384__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA512__MGF1(PaddingScheme, NamedTuple('OAEP__SHA512__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA512_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PaddingScheme_OAEP__SHA512__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()


class PositiveInteger:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_0_x_: int = source__
        if True:
            return default__.IsValid__PositiveInteger(d_0_x_)
        return False

class PositiveLong:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_1_x_: int = source__
        if True:
            return default__.IsValid__PositiveLong(d_1_x_)
        return False

class PublicKeyDiscoveryInput:
    @classmethod
    def default(cls, ):
        return lambda: PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PublicKeyDiscoveryInput(self) -> bool:
        return isinstance(self, PublicKeyDiscoveryInput_PublicKeyDiscoveryInput)

class PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(PublicKeyDiscoveryInput, NamedTuple('PublicKeyDiscoveryInput', [('recipientStaticPrivateKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput.PublicKeyDiscoveryInput({_dafny.string_of(self.recipientStaticPrivateKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PublicKeyDiscoveryInput_PublicKeyDiscoveryInput) and self.recipientStaticPrivateKey == __o.recipientStaticPrivateKey
    def __hash__(self) -> int:
        return super().__hash__()


class PutCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: PutCacheEntryInput_PutCacheEntryInput(_dafny.Seq({}), Materials.default()(), int(0), int(0), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutCacheEntryInput(self) -> bool:
        return isinstance(self, PutCacheEntryInput_PutCacheEntryInput)

class PutCacheEntryInput_PutCacheEntryInput(PutCacheEntryInput, NamedTuple('PutCacheEntryInput', [('identifier', Any), ('materials', Any), ('creationTime', Any), ('expiryTime', Any), ('messagesUsed', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput.PutCacheEntryInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.materials)}, {_dafny.string_of(self.creationTime)}, {_dafny.string_of(self.expiryTime)}, {_dafny.string_of(self.messagesUsed)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PutCacheEntryInput_PutCacheEntryInput) and self.identifier == __o.identifier and self.materials == __o.materials and self.creationTime == __o.creationTime and self.expiryTime == __o.expiryTime and self.messagesUsed == __o.messagesUsed and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class RawEcdhStaticConfigurations:
    @classmethod
    def default(cls, ):
        return lambda: RawEcdhStaticConfigurations_PublicKeyDiscovery(PublicKeyDiscoveryInput.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PublicKeyDiscovery(self) -> bool:
        return isinstance(self, RawEcdhStaticConfigurations_PublicKeyDiscovery)
    @property
    def is_RawPrivateKeyToStaticPublicKey(self) -> bool:
        return isinstance(self, RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey)
    @property
    def is_EphemeralPrivateKeyToStaticPublicKey(self) -> bool:
        return isinstance(self, RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey)

class RawEcdhStaticConfigurations_PublicKeyDiscovery(RawEcdhStaticConfigurations, NamedTuple('PublicKeyDiscovery', [('PublicKeyDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.PublicKeyDiscovery({_dafny.string_of(self.PublicKeyDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawEcdhStaticConfigurations_PublicKeyDiscovery) and self.PublicKeyDiscovery == __o.PublicKeyDiscovery
    def __hash__(self) -> int:
        return super().__hash__()

class RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(RawEcdhStaticConfigurations, NamedTuple('RawPrivateKeyToStaticPublicKey', [('RawPrivateKeyToStaticPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.RawPrivateKeyToStaticPublicKey({_dafny.string_of(self.RawPrivateKeyToStaticPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey) and self.RawPrivateKeyToStaticPublicKey == __o.RawPrivateKeyToStaticPublicKey
    def __hash__(self) -> int:
        return super().__hash__()

class RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(RawEcdhStaticConfigurations, NamedTuple('EphemeralPrivateKeyToStaticPublicKey', [('EphemeralPrivateKeyToStaticPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.EphemeralPrivateKeyToStaticPublicKey({_dafny.string_of(self.EphemeralPrivateKeyToStaticPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey) and self.EphemeralPrivateKeyToStaticPublicKey == __o.EphemeralPrivateKeyToStaticPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class RawPrivateKeyToStaticPublicKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawPrivateKeyToStaticPublicKeyInput(self) -> bool:
        return isinstance(self, RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput)

class RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(RawPrivateKeyToStaticPublicKeyInput, NamedTuple('RawPrivateKeyToStaticPublicKeyInput', [('senderStaticPrivateKey', Any), ('recipientPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput.RawPrivateKeyToStaticPublicKeyInput({_dafny.string_of(self.senderStaticPrivateKey)}, {_dafny.string_of(self.recipientPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput) and self.senderStaticPrivateKey == __o.senderStaticPrivateKey and self.recipientPublicKey == __o.recipientPublicKey
    def __hash__(self) -> int:
        return super().__hash__()


class SignatureAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: SignatureAlgorithm_ECDSA(ECDSA.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSA(self) -> bool:
        return isinstance(self, SignatureAlgorithm_ECDSA)
    @property
    def is_None(self) -> bool:
        return isinstance(self, SignatureAlgorithm_None)

class SignatureAlgorithm_ECDSA(SignatureAlgorithm, NamedTuple('ECDSA', [('ECDSA', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm.ECDSA({_dafny.string_of(self.ECDSA)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignatureAlgorithm_ECDSA) and self.ECDSA == __o.ECDSA
    def __hash__(self) -> int:
        return super().__hash__()

class SignatureAlgorithm_None(SignatureAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignatureAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class SingleThreadedCache:
    @classmethod
    def default(cls, ):
        return lambda: SingleThreadedCache_SingleThreadedCache(int(0), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SingleThreadedCache(self) -> bool:
        return isinstance(self, SingleThreadedCache_SingleThreadedCache)

class SingleThreadedCache_SingleThreadedCache(SingleThreadedCache, NamedTuple('SingleThreadedCache', [('entryCapacity', Any), ('entryPruningTailSize', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SingleThreadedCache.SingleThreadedCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SingleThreadedCache_SingleThreadedCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize
    def __hash__(self) -> int:
        return super().__hash__()


class StaticConfigurations:
    @classmethod
    def default(cls, ):
        return lambda: StaticConfigurations_AWS__KMS__ECDH(KmsEcdhStaticConfigurations.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AWS__KMS__ECDH(self) -> bool:
        return isinstance(self, StaticConfigurations_AWS__KMS__ECDH)
    @property
    def is_RAW__ECDH(self) -> bool:
        return isinstance(self, StaticConfigurations_RAW__ECDH)

class StaticConfigurations_AWS__KMS__ECDH(StaticConfigurations, NamedTuple('AWS__KMS__ECDH', [('AWS__KMS__ECDH', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.StaticConfigurations.AWS_KMS_ECDH({_dafny.string_of(self.AWS__KMS__ECDH)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StaticConfigurations_AWS__KMS__ECDH) and self.AWS__KMS__ECDH == __o.AWS__KMS__ECDH
    def __hash__(self) -> int:
        return super().__hash__()

class StaticConfigurations_RAW__ECDH(StaticConfigurations, NamedTuple('RAW__ECDH', [('RAW__ECDH', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.StaticConfigurations.RAW_ECDH({_dafny.string_of(self.RAW__ECDH)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StaticConfigurations_RAW__ECDH) and self.RAW__ECDH == __o.RAW__ECDH
    def __hash__(self) -> int:
        return super().__hash__()


class StormTrackingCache:
    @classmethod
    def default(cls, ):
        return lambda: StormTrackingCache_StormTrackingCache(int(0), Wrappers.Option.default()(), int(0), int(0), int(0), int(0), int(0), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StormTrackingCache(self) -> bool:
        return isinstance(self, StormTrackingCache_StormTrackingCache)

class StormTrackingCache_StormTrackingCache(StormTrackingCache, NamedTuple('StormTrackingCache', [('entryCapacity', Any), ('entryPruningTailSize', Any), ('gracePeriod', Any), ('graceInterval', Any), ('fanOut', Any), ('inFlightTTL', Any), ('sleepMilli', Any), ('timeUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.StormTrackingCache.StormTrackingCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)}, {_dafny.string_of(self.gracePeriod)}, {_dafny.string_of(self.graceInterval)}, {_dafny.string_of(self.fanOut)}, {_dafny.string_of(self.inFlightTTL)}, {_dafny.string_of(self.sleepMilli)}, {_dafny.string_of(self.timeUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StormTrackingCache_StormTrackingCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize and self.gracePeriod == __o.gracePeriod and self.graceInterval == __o.graceInterval and self.fanOut == __o.fanOut and self.inFlightTTL == __o.inFlightTTL and self.sleepMilli == __o.sleepMilli and self.timeUnits == __o.timeUnits
    def __hash__(self) -> int:
        return super().__hash__()


class SymmetricSignatureAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: SymmetricSignatureAlgorithm_HMAC(AwsCryptographyPrimitivesTypes.DigestAlgorithm.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HMAC(self) -> bool:
        return isinstance(self, SymmetricSignatureAlgorithm_HMAC)
    @property
    def is_None(self) -> bool:
        return isinstance(self, SymmetricSignatureAlgorithm_None)

class SymmetricSignatureAlgorithm_HMAC(SymmetricSignatureAlgorithm, NamedTuple('HMAC', [('HMAC', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.HMAC({_dafny.string_of(self.HMAC)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SymmetricSignatureAlgorithm_HMAC) and self.HMAC == __o.HMAC
    def __hash__(self) -> int:
        return super().__hash__()

class SymmetricSignatureAlgorithm_None(SymmetricSignatureAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SymmetricSignatureAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class TimeUnits:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [TimeUnits_Seconds(), TimeUnits_Milliseconds()]
    @classmethod
    def default(cls, ):
        return lambda: TimeUnits_Seconds()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Seconds(self) -> bool:
        return isinstance(self, TimeUnits_Seconds)
    @property
    def is_Milliseconds(self) -> bool:
        return isinstance(self, TimeUnits_Milliseconds)

class TimeUnits_Seconds(TimeUnits, NamedTuple('Seconds', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.TimeUnits.Seconds'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeUnits_Seconds)
    def __hash__(self) -> int:
        return super().__hash__()

class TimeUnits_Milliseconds(TimeUnits, NamedTuple('Milliseconds', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.TimeUnits.Milliseconds'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeUnits_Milliseconds)
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateUsageMetadataInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateUsageMetadataInput_UpdateUsageMetadataInput(_dafny.Seq({}), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateUsageMetadataInput(self) -> bool:
        return isinstance(self, UpdateUsageMetadataInput_UpdateUsageMetadataInput)

class UpdateUsageMetadataInput_UpdateUsageMetadataInput(UpdateUsageMetadataInput, NamedTuple('UpdateUsageMetadataInput', [('identifier', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.UpdateUsageMetadataInput.UpdateUsageMetadataInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateUsageMetadataInput_UpdateUsageMetadataInput) and self.identifier == __o.identifier and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class ValidateCommitmentPolicyOnDecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput(AlgorithmSuiteId.default()(), CommitmentPolicy.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidateCommitmentPolicyOnDecryptInput(self) -> bool:
        return isinstance(self, ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput)

class ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput(ValidateCommitmentPolicyOnDecryptInput, NamedTuple('ValidateCommitmentPolicyOnDecryptInput', [('algorithm', Any), ('commitmentPolicy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnDecryptInput.ValidateCommitmentPolicyOnDecryptInput({_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.commitmentPolicy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput) and self.algorithm == __o.algorithm and self.commitmentPolicy == __o.commitmentPolicy
    def __hash__(self) -> int:
        return super().__hash__()


class ValidateCommitmentPolicyOnEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput(AlgorithmSuiteId.default()(), CommitmentPolicy.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidateCommitmentPolicyOnEncryptInput(self) -> bool:
        return isinstance(self, ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput)

class ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput(ValidateCommitmentPolicyOnEncryptInput, NamedTuple('ValidateCommitmentPolicyOnEncryptInput', [('algorithm', Any), ('commitmentPolicy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnEncryptInput.ValidateCommitmentPolicyOnEncryptInput({_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.commitmentPolicy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput) and self.algorithm == __o.algorithm and self.commitmentPolicy == __o.commitmentPolicy
    def __hash__(self) -> int:
        return super().__hash__()


class ValidDecryptionMaterialsTransitionInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(DecryptionMaterials.default()(), DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidDecryptionMaterialsTransitionInput(self) -> bool:
        return isinstance(self, ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput)

class ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(ValidDecryptionMaterialsTransitionInput, NamedTuple('ValidDecryptionMaterialsTransitionInput', [('start', Any), ('stop', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidDecryptionMaterialsTransitionInput.ValidDecryptionMaterialsTransitionInput({_dafny.string_of(self.start)}, {_dafny.string_of(self.stop)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput) and self.start == __o.start and self.stop == __o.stop
    def __hash__(self) -> int:
        return super().__hash__()


class ValidEncryptionMaterialsTransitionInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(EncryptionMaterials.default()(), EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidEncryptionMaterialsTransitionInput(self) -> bool:
        return isinstance(self, ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput)

class ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(ValidEncryptionMaterialsTransitionInput, NamedTuple('ValidEncryptionMaterialsTransitionInput', [('start', Any), ('stop', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidEncryptionMaterialsTransitionInput.ValidEncryptionMaterialsTransitionInput({_dafny.string_of(self.start)}, {_dafny.string_of(self.stop)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput) and self.start == __o.start and self.stop == __o.stop
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_AwsCryptographicMaterialProvidersException(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsCryptographicMaterialProvidersException(self) -> bool:
        return isinstance(self, Error_AwsCryptographicMaterialProvidersException)
    @property
    def is_EntryAlreadyExists(self) -> bool:
        return isinstance(self, Error_EntryAlreadyExists)
    @property
    def is_EntryDoesNotExist(self) -> bool:
        return isinstance(self, Error_EntryDoesNotExist)
    @property
    def is_InFlightTTLExceeded(self) -> bool:
        return isinstance(self, Error_InFlightTTLExceeded)
    @property
    def is_InvalidAlgorithmSuiteInfo(self) -> bool:
        return isinstance(self, Error_InvalidAlgorithmSuiteInfo)
    @property
    def is_InvalidAlgorithmSuiteInfoOnDecrypt(self) -> bool:
        return isinstance(self, Error_InvalidAlgorithmSuiteInfoOnDecrypt)
    @property
    def is_InvalidAlgorithmSuiteInfoOnEncrypt(self) -> bool:
        return isinstance(self, Error_InvalidAlgorithmSuiteInfoOnEncrypt)
    @property
    def is_InvalidDecryptionMaterials(self) -> bool:
        return isinstance(self, Error_InvalidDecryptionMaterials)
    @property
    def is_InvalidDecryptionMaterialsTransition(self) -> bool:
        return isinstance(self, Error_InvalidDecryptionMaterialsTransition)
    @property
    def is_InvalidEncryptionMaterials(self) -> bool:
        return isinstance(self, Error_InvalidEncryptionMaterials)
    @property
    def is_InvalidEncryptionMaterialsTransition(self) -> bool:
        return isinstance(self, Error_InvalidEncryptionMaterialsTransition)
    @property
    def is_AwsCryptographyKeyStore(self) -> bool:
        return isinstance(self, Error_AwsCryptographyKeyStore)
    @property
    def is_AwsCryptographyPrimitives(self) -> bool:
        return isinstance(self, Error_AwsCryptographyPrimitives)
    @property
    def is_ComAmazonawsDynamodb(self) -> bool:
        return isinstance(self, Error_ComAmazonawsDynamodb)
    @property
    def is_ComAmazonawsKms(self) -> bool:
        return isinstance(self, Error_ComAmazonawsKms)
    @property
    def is_CollectionOfErrors(self) -> bool:
        return isinstance(self, Error_CollectionOfErrors)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, Error_Opaque)
    @property
    def is_OpaqueWithText(self) -> bool:
        return isinstance(self, Error_OpaqueWithText)

class Error_AwsCryptographicMaterialProvidersException(Error, NamedTuple('AwsCryptographicMaterialProvidersException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographicMaterialProvidersException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographicMaterialProvidersException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_EntryAlreadyExists(Error, NamedTuple('EntryAlreadyExists', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.EntryAlreadyExists({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_EntryAlreadyExists) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_EntryDoesNotExist(Error, NamedTuple('EntryDoesNotExist', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.EntryDoesNotExist({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_EntryDoesNotExist) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InFlightTTLExceeded(Error, NamedTuple('InFlightTTLExceeded', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InFlightTTLExceeded({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InFlightTTLExceeded) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfo(Error, NamedTuple('InvalidAlgorithmSuiteInfo', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfo({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidAlgorithmSuiteInfo) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfoOnDecrypt(Error, NamedTuple('InvalidAlgorithmSuiteInfoOnDecrypt', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfoOnDecrypt({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidAlgorithmSuiteInfoOnDecrypt) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfoOnEncrypt(Error, NamedTuple('InvalidAlgorithmSuiteInfoOnEncrypt', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfoOnEncrypt({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidAlgorithmSuiteInfoOnEncrypt) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidDecryptionMaterials(Error, NamedTuple('InvalidDecryptionMaterials', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidDecryptionMaterials({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidDecryptionMaterials) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidDecryptionMaterialsTransition(Error, NamedTuple('InvalidDecryptionMaterialsTransition', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidDecryptionMaterialsTransition({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidDecryptionMaterialsTransition) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidEncryptionMaterials(Error, NamedTuple('InvalidEncryptionMaterials', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidEncryptionMaterials({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidEncryptionMaterials) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidEncryptionMaterialsTransition(Error, NamedTuple('InvalidEncryptionMaterialsTransition', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidEncryptionMaterialsTransition({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidEncryptionMaterialsTransition) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyKeyStore(Error, NamedTuple('AwsCryptographyKeyStore', [('AwsCryptographyKeyStore', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographyKeyStore({_dafny.string_of(self.AwsCryptographyKeyStore)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographyKeyStore) and self.AwsCryptographyKeyStore == __o.AwsCryptographyKeyStore
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyPrimitives(Error, NamedTuple('AwsCryptographyPrimitives', [('AwsCryptographyPrimitives', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographyPrimitives({_dafny.string_of(self.AwsCryptographyPrimitives)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographyPrimitives) and self.AwsCryptographyPrimitives == __o.AwsCryptographyPrimitives
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsDynamodb(Error, NamedTuple('ComAmazonawsDynamodb', [('ComAmazonawsDynamodb', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.ComAmazonawsDynamodb({_dafny.string_of(self.ComAmazonawsDynamodb)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsDynamodb) and self.ComAmazonawsDynamodb == __o.ComAmazonawsDynamodb
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()

class Error_OpaqueWithText(Error, NamedTuple('OpaqueWithText', [('obj', Any), ('objMessage', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.OpaqueWithText({_dafny.string_of(self.obj)}, {_dafny.string_of(self.objMessage)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_OpaqueWithText) and self.obj == __o.obj and self.objMessage == __o.objMessage
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
    def _Is(source__):
        d_2_e_: Error = source__
        return ((d_2_e_).is_Opaque) or ((d_2_e_).is_OpaqueWithText)

class DummySubsetType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
    def _Is(source__):
        d_3_x_: int = source__
        return default__.IsDummySubsetType(d_3_x_)
