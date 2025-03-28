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

# Module: AwsCryptographyKeyStoreTypes

class default__:
    def  __init__(self):
        pass

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
        return f'AwsCryptographyKeyStoreTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class BeaconKeyMaterials:
    @classmethod
    def default(cls, ):
        return lambda: BeaconKeyMaterials_BeaconKeyMaterials(_dafny.Seq(""), _dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BeaconKeyMaterials(self) -> bool:
        return isinstance(self, BeaconKeyMaterials_BeaconKeyMaterials)

class BeaconKeyMaterials_BeaconKeyMaterials(BeaconKeyMaterials, NamedTuple('BeaconKeyMaterials', [('beaconKeyIdentifier', Any), ('encryptionContext', Any), ('beaconKey', Any), ('hmacKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.BeaconKeyMaterials({_dafny.string_of(self.beaconKeyIdentifier)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.beaconKey)}, {_dafny.string_of(self.hmacKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BeaconKeyMaterials_BeaconKeyMaterials) and self.beaconKeyIdentifier == __o.beaconKeyIdentifier and self.encryptionContext == __o.encryptionContext and self.beaconKey == __o.beaconKey and self.hmacKeys == __o.hmacKeys
    def __hash__(self) -> int:
        return super().__hash__()


class BranchKeyMaterials:
    @classmethod
    def default(cls, ):
        return lambda: BranchKeyMaterials_BranchKeyMaterials(_dafny.Seq(""), UTF8.ValidUTF8Bytes.default(), _dafny.Map({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BranchKeyMaterials(self) -> bool:
        return isinstance(self, BranchKeyMaterials_BranchKeyMaterials)

class BranchKeyMaterials_BranchKeyMaterials(BranchKeyMaterials, NamedTuple('BranchKeyMaterials', [('branchKeyIdentifier', Any), ('branchKeyVersion', Any), ('encryptionContext', Any), ('branchKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.BranchKeyMaterials.BranchKeyMaterials({_dafny.string_of(self.branchKeyIdentifier)}, {_dafny.string_of(self.branchKeyVersion)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.branchKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BranchKeyMaterials_BranchKeyMaterials) and self.branchKeyIdentifier == __o.branchKeyIdentifier and self.branchKeyVersion == __o.branchKeyVersion and self.encryptionContext == __o.encryptionContext and self.branchKey == __o.branchKey
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyInput_CreateKeyInput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyInput(self) -> bool:
        return isinstance(self, CreateKeyInput_CreateKeyInput)

class CreateKeyInput_CreateKeyInput(CreateKeyInput, NamedTuple('CreateKeyInput', [('branchKeyIdentifier', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.CreateKeyInput.CreateKeyInput({_dafny.string_of(self.branchKeyIdentifier)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyInput_CreateKeyInput) and self.branchKeyIdentifier == __o.branchKeyIdentifier and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyOutput_CreateKeyOutput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyOutput(self) -> bool:
        return isinstance(self, CreateKeyOutput_CreateKeyOutput)

class CreateKeyOutput_CreateKeyOutput(CreateKeyOutput, NamedTuple('CreateKeyOutput', [('branchKeyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.CreateKeyOutput.CreateKeyOutput({_dafny.string_of(self.branchKeyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyOutput_CreateKeyOutput) and self.branchKeyIdentifier == __o.branchKeyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyStoreInput:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CreateKeyStoreInput_CreateKeyStoreInput()]
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyStoreInput_CreateKeyStoreInput()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyStoreInput(self) -> bool:
        return isinstance(self, CreateKeyStoreInput_CreateKeyStoreInput)

class CreateKeyStoreInput_CreateKeyStoreInput(CreateKeyStoreInput, NamedTuple('CreateKeyStoreInput', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.CreateKeyStoreInput.CreateKeyStoreInput'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyStoreInput_CreateKeyStoreInput)
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyStoreOutput:
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyStoreOutput_CreateKeyStoreOutput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyStoreOutput(self) -> bool:
        return isinstance(self, CreateKeyStoreOutput_CreateKeyStoreOutput)

class CreateKeyStoreOutput_CreateKeyStoreOutput(CreateKeyStoreOutput, NamedTuple('CreateKeyStoreOutput', [('tableArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput.CreateKeyStoreOutput({_dafny.string_of(self.tableArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyStoreOutput_CreateKeyStoreOutput) and self.tableArn == __o.tableArn
    def __hash__(self) -> int:
        return super().__hash__()


class Discovery:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [Discovery_Discovery()]
    @classmethod
    def default(cls, ):
        return lambda: Discovery_Discovery()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Discovery(self) -> bool:
        return isinstance(self, Discovery_Discovery)

class Discovery_Discovery(Discovery, NamedTuple('Discovery', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Discovery.Discovery'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Discovery_Discovery)
    def __hash__(self) -> int:
        return super().__hash__()


class GetActiveBranchKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: GetActiveBranchKeyInput_GetActiveBranchKeyInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetActiveBranchKeyInput(self) -> bool:
        return isinstance(self, GetActiveBranchKeyInput_GetActiveBranchKeyInput)

class GetActiveBranchKeyInput_GetActiveBranchKeyInput(GetActiveBranchKeyInput, NamedTuple('GetActiveBranchKeyInput', [('branchKeyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput.GetActiveBranchKeyInput({_dafny.string_of(self.branchKeyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetActiveBranchKeyInput_GetActiveBranchKeyInput) and self.branchKeyIdentifier == __o.branchKeyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()


class GetActiveBranchKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(BranchKeyMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetActiveBranchKeyOutput(self) -> bool:
        return isinstance(self, GetActiveBranchKeyOutput_GetActiveBranchKeyOutput)

class GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(GetActiveBranchKeyOutput, NamedTuple('GetActiveBranchKeyOutput', [('branchKeyMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.GetActiveBranchKeyOutput({_dafny.string_of(self.branchKeyMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetActiveBranchKeyOutput_GetActiveBranchKeyOutput) and self.branchKeyMaterials == __o.branchKeyMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class GetBeaconKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: GetBeaconKeyInput_GetBeaconKeyInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBeaconKeyInput(self) -> bool:
        return isinstance(self, GetBeaconKeyInput_GetBeaconKeyInput)

class GetBeaconKeyInput_GetBeaconKeyInput(GetBeaconKeyInput, NamedTuple('GetBeaconKeyInput', [('branchKeyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetBeaconKeyInput.GetBeaconKeyInput({_dafny.string_of(self.branchKeyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBeaconKeyInput_GetBeaconKeyInput) and self.branchKeyIdentifier == __o.branchKeyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()


class GetBeaconKeyOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetBeaconKeyOutput_GetBeaconKeyOutput(BeaconKeyMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBeaconKeyOutput(self) -> bool:
        return isinstance(self, GetBeaconKeyOutput_GetBeaconKeyOutput)

class GetBeaconKeyOutput_GetBeaconKeyOutput(GetBeaconKeyOutput, NamedTuple('GetBeaconKeyOutput', [('beaconKeyMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.GetBeaconKeyOutput({_dafny.string_of(self.beaconKeyMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBeaconKeyOutput_GetBeaconKeyOutput) and self.beaconKeyMaterials == __o.beaconKeyMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyVersionInput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyVersionInput_GetBranchKeyVersionInput(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyVersionInput(self) -> bool:
        return isinstance(self, GetBranchKeyVersionInput_GetBranchKeyVersionInput)

class GetBranchKeyVersionInput_GetBranchKeyVersionInput(GetBranchKeyVersionInput, NamedTuple('GetBranchKeyVersionInput', [('branchKeyIdentifier', Any), ('branchKeyVersion', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput.GetBranchKeyVersionInput({_dafny.string_of(self.branchKeyIdentifier)}, {_dafny.string_of(self.branchKeyVersion)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBranchKeyVersionInput_GetBranchKeyVersionInput) and self.branchKeyIdentifier == __o.branchKeyIdentifier and self.branchKeyVersion == __o.branchKeyVersion
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyVersionOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(BranchKeyMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyVersionOutput(self) -> bool:
        return isinstance(self, GetBranchKeyVersionOutput_GetBranchKeyVersionOutput)

class GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(GetBranchKeyVersionOutput, NamedTuple('GetBranchKeyVersionOutput', [('branchKeyMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.GetBranchKeyVersionOutput({_dafny.string_of(self.branchKeyMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetBranchKeyVersionOutput_GetBranchKeyVersionOutput) and self.branchKeyMaterials == __o.branchKeyMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyStoreInfoOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyStoreInfoOutput_GetKeyStoreInfoOutput(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq({}), KMSConfiguration.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyStoreInfoOutput(self) -> bool:
        return isinstance(self, GetKeyStoreInfoOutput_GetKeyStoreInfoOutput)

class GetKeyStoreInfoOutput_GetKeyStoreInfoOutput(GetKeyStoreInfoOutput, NamedTuple('GetKeyStoreInfoOutput', [('keyStoreId', Any), ('keyStoreName', Any), ('logicalKeyStoreName', Any), ('grantTokens', Any), ('kmsConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput.GetKeyStoreInfoOutput({_dafny.string_of(self.keyStoreId)}, {_dafny.string_of(self.keyStoreName)}, {_dafny.string_of(self.logicalKeyStoreName)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.kmsConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyStoreInfoOutput_GetKeyStoreInfoOutput) and self.keyStoreId == __o.keyStoreId and self.keyStoreName == __o.keyStoreName and self.logicalKeyStoreName == __o.logicalKeyStoreName and self.grantTokens == __o.grantTokens and self.kmsConfiguration == __o.kmsConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class IKeyStoreClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyKeyStoreTypes.IKeyStoreClientCallHistory"

class IKeyStoreClient:
    pass
    def GetKeyStoreInfo(self):
        pass

    def CreateKeyStore(self, input):
        pass

    def CreateKey(self, input):
        pass

    def VersionKey(self, input):
        pass

    def GetActiveBranchKey(self, input):
        pass

    def GetBranchKeyVersion(self, input):
        pass

    def GetBeaconKey(self, input):
        pass


class KeyStoreConfig:
    @classmethod
    def default(cls, ):
        return lambda: KeyStoreConfig_KeyStoreConfig(_dafny.Seq(""), KMSConfiguration.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyStoreConfig(self) -> bool:
        return isinstance(self, KeyStoreConfig_KeyStoreConfig)

class KeyStoreConfig_KeyStoreConfig(KeyStoreConfig, NamedTuple('KeyStoreConfig', [('ddbTableName', Any), ('kmsConfiguration', Any), ('logicalKeyStoreName', Any), ('id', Any), ('grantTokens', Any), ('ddbClient', Any), ('kmsClient', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.KeyStoreConfig.KeyStoreConfig({_dafny.string_of(self.ddbTableName)}, {_dafny.string_of(self.kmsConfiguration)}, {_dafny.string_of(self.logicalKeyStoreName)}, {_dafny.string_of(self.id)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.ddbClient)}, {_dafny.string_of(self.kmsClient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyStoreConfig_KeyStoreConfig) and self.ddbTableName == __o.ddbTableName and self.kmsConfiguration == __o.kmsConfiguration and self.logicalKeyStoreName == __o.logicalKeyStoreName and self.id == __o.id and self.grantTokens == __o.grantTokens and self.ddbClient == __o.ddbClient and self.kmsClient == __o.kmsClient
    def __hash__(self) -> int:
        return super().__hash__()


class KMSConfiguration:
    @classmethod
    def default(cls, ):
        return lambda: KMSConfiguration_kmsKeyArn(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_kmsKeyArn(self) -> bool:
        return isinstance(self, KMSConfiguration_kmsKeyArn)
    @property
    def is_kmsMRKeyArn(self) -> bool:
        return isinstance(self, KMSConfiguration_kmsMRKeyArn)
    @property
    def is_discovery(self) -> bool:
        return isinstance(self, KMSConfiguration_discovery)
    @property
    def is_mrDiscovery(self) -> bool:
        return isinstance(self, KMSConfiguration_mrDiscovery)

class KMSConfiguration_kmsKeyArn(KMSConfiguration, NamedTuple('kmsKeyArn', [('kmsKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.KMSConfiguration.kmsKeyArn({_dafny.string_of(self.kmsKeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSConfiguration_kmsKeyArn) and self.kmsKeyArn == __o.kmsKeyArn
    def __hash__(self) -> int:
        return super().__hash__()

class KMSConfiguration_kmsMRKeyArn(KMSConfiguration, NamedTuple('kmsMRKeyArn', [('kmsMRKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.KMSConfiguration.kmsMRKeyArn({_dafny.string_of(self.kmsMRKeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSConfiguration_kmsMRKeyArn) and self.kmsMRKeyArn == __o.kmsMRKeyArn
    def __hash__(self) -> int:
        return super().__hash__()

class KMSConfiguration_discovery(KMSConfiguration, NamedTuple('discovery', [('discovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.KMSConfiguration.discovery({_dafny.string_of(self.discovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSConfiguration_discovery) and self.discovery == __o.discovery
    def __hash__(self) -> int:
        return super().__hash__()

class KMSConfiguration_mrDiscovery(KMSConfiguration, NamedTuple('mrDiscovery', [('mrDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.KMSConfiguration.mrDiscovery({_dafny.string_of(self.mrDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSConfiguration_mrDiscovery) and self.mrDiscovery == __o.mrDiscovery
    def __hash__(self) -> int:
        return super().__hash__()


class MRDiscovery:
    @classmethod
    def default(cls, ):
        return lambda: MRDiscovery_MRDiscovery(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MRDiscovery(self) -> bool:
        return isinstance(self, MRDiscovery_MRDiscovery)

class MRDiscovery_MRDiscovery(MRDiscovery, NamedTuple('MRDiscovery', [('region', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.MRDiscovery.MRDiscovery({_dafny.string_of(self.region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MRDiscovery_MRDiscovery) and self.region == __o.region
    def __hash__(self) -> int:
        return super().__hash__()


class VersionKeyInput:
    @classmethod
    def default(cls, ):
        return lambda: VersionKeyInput_VersionKeyInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VersionKeyInput(self) -> bool:
        return isinstance(self, VersionKeyInput_VersionKeyInput)

class VersionKeyInput_VersionKeyInput(VersionKeyInput, NamedTuple('VersionKeyInput', [('branchKeyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.VersionKeyInput.VersionKeyInput({_dafny.string_of(self.branchKeyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VersionKeyInput_VersionKeyInput) and self.branchKeyIdentifier == __o.branchKeyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()


class VersionKeyOutput:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [VersionKeyOutput_VersionKeyOutput()]
    @classmethod
    def default(cls, ):
        return lambda: VersionKeyOutput_VersionKeyOutput()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VersionKeyOutput(self) -> bool:
        return isinstance(self, VersionKeyOutput_VersionKeyOutput)

class VersionKeyOutput_VersionKeyOutput(VersionKeyOutput, NamedTuple('VersionKeyOutput', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.VersionKeyOutput.VersionKeyOutput'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VersionKeyOutput_VersionKeyOutput)
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_KeyStoreException(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyStoreException(self) -> bool:
        return isinstance(self, Error_KeyStoreException)
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

class Error_KeyStoreException(Error, NamedTuple('KeyStoreException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.KeyStoreException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KeyStoreException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsDynamodb(Error, NamedTuple('ComAmazonawsDynamodb', [('ComAmazonawsDynamodb', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.ComAmazonawsDynamodb({_dafny.string_of(self.ComAmazonawsDynamodb)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsDynamodb) and self.ComAmazonawsDynamodb == __o.ComAmazonawsDynamodb
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()

class Error_OpaqueWithText(Error, NamedTuple('OpaqueWithText', [('obj', Any), ('objMessage', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreTypes.Error.OpaqueWithText({_dafny.string_of(self.obj)}, {_dafny.string_of(self.objMessage)})'
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
        d_0_e_: Error = source__
        return ((d_0_e_).is_Opaque) or ((d_0_e_).is_OpaqueWithText)

class DummySubsetType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
    def _Is(source__):
        d_1_x_: int = source__
        return default__.IsDummySubsetType(d_1_x_)
