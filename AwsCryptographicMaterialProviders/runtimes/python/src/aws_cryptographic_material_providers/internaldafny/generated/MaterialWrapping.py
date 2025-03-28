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

# Module: MaterialWrapping


class GenerateAndWrapInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateAndWrapInput_GenerateAndWrapInput(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateAndWrapInput(self) -> bool:
        return isinstance(self, GenerateAndWrapInput_GenerateAndWrapInput)

class GenerateAndWrapInput_GenerateAndWrapInput(GenerateAndWrapInput, NamedTuple('GenerateAndWrapInput', [('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapInput.GenerateAndWrapInput({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateAndWrapInput_GenerateAndWrapInput) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateAndWrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: GenerateAndWrapOutput_GenerateAndWrapOutput(_dafny.Seq({}), _dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateAndWrapOutput(self) -> bool:
        return isinstance(self, GenerateAndWrapOutput_GenerateAndWrapOutput)

class GenerateAndWrapOutput_GenerateAndWrapOutput(GenerateAndWrapOutput, NamedTuple('GenerateAndWrapOutput', [('plaintextMaterial', Any), ('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapOutput.GenerateAndWrapOutput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateAndWrapOutput_GenerateAndWrapOutput) and self.plaintextMaterial == __o.plaintextMaterial and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class WrapInput:
    @classmethod
    def default(cls, ):
        return lambda: WrapInput_WrapInput(_dafny.Seq({}), AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapInput(self) -> bool:
        return isinstance(self, WrapInput_WrapInput)

class WrapInput_WrapInput(WrapInput, NamedTuple('WrapInput', [('plaintextMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapInput.WrapInput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapInput_WrapInput) and self.plaintextMaterial == __o.plaintextMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class WrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: WrapOutput_WrapOutput(_dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapOutput(self) -> bool:
        return isinstance(self, WrapOutput_WrapOutput)

class WrapOutput_WrapOutput(WrapOutput, NamedTuple('WrapOutput', [('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapOutput.WrapOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapOutput_WrapOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapInput:
    @classmethod
    def default(cls, ):
        return lambda: UnwrapInput_UnwrapInput(_dafny.Seq({}), AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapInput(self) -> bool:
        return isinstance(self, UnwrapInput_UnwrapInput)

class UnwrapInput_UnwrapInput(UnwrapInput, NamedTuple('UnwrapInput', [('wrappedMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapInput.UnwrapInput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapInput_UnwrapInput) and self.wrappedMaterial == __o.wrappedMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: UnwrapOutput_UnwrapOutput(_dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapOutput(self) -> bool:
        return isinstance(self, UnwrapOutput_UnwrapOutput)

class UnwrapOutput_UnwrapOutput(UnwrapOutput, NamedTuple('UnwrapOutput', [('unwrappedMaterial', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapOutput.UnwrapOutput({_dafny.string_of(self.unwrappedMaterial)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapOutput_UnwrapOutput) and self.unwrappedMaterial == __o.unwrappedMaterial and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateAndWrapMaterial:
    pass

class WrapMaterial:
    pass

class UnwrapMaterial:
    pass
