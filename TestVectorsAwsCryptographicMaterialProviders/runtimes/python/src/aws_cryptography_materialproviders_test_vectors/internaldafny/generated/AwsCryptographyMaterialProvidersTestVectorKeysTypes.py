import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_ as module_
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders

# Module: AwsCryptographyMaterialProvidersTestVectorKeysTypes

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
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class CmmOperation:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CmmOperation_ENCRYPT(), CmmOperation_DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: CmmOperation_ENCRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENCRYPT(self) -> bool:
        return isinstance(self, CmmOperation_ENCRYPT)
    @property
    def is_DECRYPT(self) -> bool:
        return isinstance(self, CmmOperation_DECRYPT)

class CmmOperation_ENCRYPT(CmmOperation, NamedTuple('ENCRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.ENCRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CmmOperation_ENCRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class CmmOperation_DECRYPT(CmmOperation, NamedTuple('DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation.DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CmmOperation_DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyDescriptionInput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyDescriptionInput_GetKeyDescriptionInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyDescriptionInput(self) -> bool:
        return isinstance(self, GetKeyDescriptionInput_GetKeyDescriptionInput)

class GetKeyDescriptionInput_GetKeyDescriptionInput(GetKeyDescriptionInput, NamedTuple('GetKeyDescriptionInput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput.GetKeyDescriptionInput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyDescriptionInput_GetKeyDescriptionInput) and self.json == __o.json
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyDescriptionOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyDescriptionOutput_GetKeyDescriptionOutput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyDescriptionOutput(self) -> bool:
        return isinstance(self, GetKeyDescriptionOutput_GetKeyDescriptionOutput)

class GetKeyDescriptionOutput_GetKeyDescriptionOutput(GetKeyDescriptionOutput, NamedTuple('GetKeyDescriptionOutput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput.GetKeyDescriptionOutput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyDescriptionOutput_GetKeyDescriptionOutput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class HierarchyKeyring:
    @classmethod
    def default(cls, ):
        return lambda: HierarchyKeyring_HierarchyKeyring(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HierarchyKeyring(self) -> bool:
        return isinstance(self, HierarchyKeyring_HierarchyKeyring)

class HierarchyKeyring_HierarchyKeyring(HierarchyKeyring, NamedTuple('HierarchyKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring.HierarchyKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HierarchyKeyring_HierarchyKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KeyDescription:
    @classmethod
    def default(cls, ):
        return lambda: KeyDescription_Kms(KMSInfo.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Kms(self) -> bool:
        return isinstance(self, KeyDescription_Kms)
    @property
    def is_KmsMrk(self) -> bool:
        return isinstance(self, KeyDescription_KmsMrk)
    @property
    def is_KmsMrkDiscovery(self) -> bool:
        return isinstance(self, KeyDescription_KmsMrkDiscovery)
    @property
    def is_RSA(self) -> bool:
        return isinstance(self, KeyDescription_RSA)
    @property
    def is_AES(self) -> bool:
        return isinstance(self, KeyDescription_AES)
    @property
    def is_ECDH(self) -> bool:
        return isinstance(self, KeyDescription_ECDH)
    @property
    def is_Static(self) -> bool:
        return isinstance(self, KeyDescription_Static)
    @property
    def is_KmsRsa(self) -> bool:
        return isinstance(self, KeyDescription_KmsRsa)
    @property
    def is_KmsECDH(self) -> bool:
        return isinstance(self, KeyDescription_KmsECDH)
    @property
    def is_Hierarchy(self) -> bool:
        return isinstance(self, KeyDescription_Hierarchy)
    @property
    def is_Multi(self) -> bool:
        return isinstance(self, KeyDescription_Multi)
    @property
    def is_RequiredEncryptionContext(self) -> bool:
        return isinstance(self, KeyDescription_RequiredEncryptionContext)

class KeyDescription_Kms(KeyDescription, NamedTuple('Kms', [('Kms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Kms({_dafny.string_of(self.Kms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Kms) and self.Kms == __o.Kms
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrk(KeyDescription, NamedTuple('KmsMrk', [('KmsMrk', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrk({_dafny.string_of(self.KmsMrk)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsMrk) and self.KmsMrk == __o.KmsMrk
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsMrkDiscovery(KeyDescription, NamedTuple('KmsMrkDiscovery', [('KmsMrkDiscovery', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrkDiscovery({_dafny.string_of(self.KmsMrkDiscovery)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsMrkDiscovery) and self.KmsMrkDiscovery == __o.KmsMrkDiscovery
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_RSA(KeyDescription, NamedTuple('RSA', [('RSA', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RSA({_dafny.string_of(self.RSA)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_RSA) and self.RSA == __o.RSA
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_AES(KeyDescription, NamedTuple('AES', [('AES', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.AES({_dafny.string_of(self.AES)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_AES) and self.AES == __o.AES
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_ECDH(KeyDescription, NamedTuple('ECDH', [('ECDH', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.ECDH({_dafny.string_of(self.ECDH)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_ECDH) and self.ECDH == __o.ECDH
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Static(KeyDescription, NamedTuple('Static', [('Static', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Static({_dafny.string_of(self.Static)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Static) and self.Static == __o.Static
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsRsa(KeyDescription, NamedTuple('KmsRsa', [('KmsRsa', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsRsa({_dafny.string_of(self.KmsRsa)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsRsa) and self.KmsRsa == __o.KmsRsa
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_KmsECDH(KeyDescription, NamedTuple('KmsECDH', [('KmsECDH', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsECDH({_dafny.string_of(self.KmsECDH)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_KmsECDH) and self.KmsECDH == __o.KmsECDH
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Hierarchy(KeyDescription, NamedTuple('Hierarchy', [('Hierarchy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Hierarchy({_dafny.string_of(self.Hierarchy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Hierarchy) and self.Hierarchy == __o.Hierarchy
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_Multi(KeyDescription, NamedTuple('Multi', [('Multi', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Multi({_dafny.string_of(self.Multi)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_Multi) and self.Multi == __o.Multi
    def __hash__(self) -> int:
        return super().__hash__()

class KeyDescription_RequiredEncryptionContext(KeyDescription, NamedTuple('RequiredEncryptionContext', [('RequiredEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RequiredEncryptionContext({_dafny.string_of(self.RequiredEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyDescription_RequiredEncryptionContext) and self.RequiredEncryptionContext == __o.RequiredEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class IKeyVectorsClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTestVectorKeysTypes.IKeyVectorsClientCallHistory"

class IKeyVectorsClient:
    pass
    def CreateTestVectorKeyring(self, input):
        pass

    def CreateWrappedTestVectorKeyring(self, input):
        pass

    def CreateWrappedTestVectorCmm(self, input):
        pass


class KeyVectorsConfig:
    @classmethod
    def default(cls, ):
        return lambda: KeyVectorsConfig_KeyVectorsConfig(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyVectorsConfig(self) -> bool:
        return isinstance(self, KeyVectorsConfig_KeyVectorsConfig)

class KeyVectorsConfig_KeyVectorsConfig(KeyVectorsConfig, NamedTuple('KeyVectorsConfig', [('keyManifestPath', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyVectorsConfig.KeyVectorsConfig({_dafny.string_of(self.keyManifestPath)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyVectorsConfig_KeyVectorsConfig) and self.keyManifestPath == __o.keyManifestPath
    def __hash__(self) -> int:
        return super().__hash__()


class KmsEcdhKeyring:
    @classmethod
    def default(cls, ):
        return lambda: KmsEcdhKeyring_KmsEcdhKeyring(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsEcdhKeyring(self) -> bool:
        return isinstance(self, KmsEcdhKeyring_KmsEcdhKeyring)

class KmsEcdhKeyring_KmsEcdhKeyring(KmsEcdhKeyring, NamedTuple('KmsEcdhKeyring', [('senderKeyId', Any), ('recipientKeyId', Any), ('senderPublicKey', Any), ('recipientPublicKey', Any), ('curveSpec', Any), ('keyAgreementScheme', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring.KmsEcdhKeyring({_dafny.string_of(self.senderKeyId)}, {_dafny.string_of(self.recipientKeyId)}, {_dafny.string_of(self.senderPublicKey)}, {_dafny.string_of(self.recipientPublicKey)}, {_dafny.string_of(self.curveSpec)}, {_dafny.string_of(self.keyAgreementScheme)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsEcdhKeyring_KmsEcdhKeyring) and self.senderKeyId == __o.senderKeyId and self.recipientKeyId == __o.recipientKeyId and self.senderPublicKey == __o.senderPublicKey and self.recipientPublicKey == __o.recipientPublicKey and self.curveSpec == __o.curveSpec and self.keyAgreementScheme == __o.keyAgreementScheme
    def __hash__(self) -> int:
        return super().__hash__()


class KMSInfo:
    @classmethod
    def default(cls, ):
        return lambda: KMSInfo_KMSInfo(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KMSInfo(self) -> bool:
        return isinstance(self, KMSInfo_KMSInfo)

class KMSInfo_KMSInfo(KMSInfo, NamedTuple('KMSInfo', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo.KMSInfo({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSInfo_KMSInfo) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KmsMrkAware:
    @classmethod
    def default(cls, ):
        return lambda: KmsMrkAware_KmsMrkAware(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsMrkAware(self) -> bool:
        return isinstance(self, KmsMrkAware_KmsMrkAware)

class KmsMrkAware_KmsMrkAware(KmsMrkAware, NamedTuple('KmsMrkAware', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware.KmsMrkAware({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsMrkAware_KmsMrkAware) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class KmsMrkAwareDiscovery:
    @classmethod
    def default(cls, ):
        return lambda: KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsMrkAwareDiscovery(self) -> bool:
        return isinstance(self, KmsMrkAwareDiscovery_KmsMrkAwareDiscovery)

class KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(KmsMrkAwareDiscovery, NamedTuple('KmsMrkAwareDiscovery', [('keyId', Any), ('defaultMrkRegion', Any), ('awsKmsDiscoveryFilter', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery.KmsMrkAwareDiscovery({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.defaultMrkRegion)}, {_dafny.string_of(self.awsKmsDiscoveryFilter)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsMrkAwareDiscovery_KmsMrkAwareDiscovery) and self.keyId == __o.keyId and self.defaultMrkRegion == __o.defaultMrkRegion and self.awsKmsDiscoveryFilter == __o.awsKmsDiscoveryFilter
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaKeyring:
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaKeyring_KmsRsaKeyring(_dafny.Seq(""), ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaKeyring(self) -> bool:
        return isinstance(self, KmsRsaKeyring_KmsRsaKeyring)

class KmsRsaKeyring_KmsRsaKeyring(KmsRsaKeyring, NamedTuple('KmsRsaKeyring', [('keyId', Any), ('encryptionAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring.KmsRsaKeyring({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.encryptionAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaKeyring_KmsRsaKeyring) and self.keyId == __o.keyId and self.encryptionAlgorithm == __o.encryptionAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class MultiKeyring:
    @classmethod
    def default(cls, ):
        return lambda: MultiKeyring_MultiKeyring(Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiKeyring(self) -> bool:
        return isinstance(self, MultiKeyring_MultiKeyring)

class MultiKeyring_MultiKeyring(MultiKeyring, NamedTuple('MultiKeyring', [('generator', Any), ('childKeyrings', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring.MultiKeyring({_dafny.string_of(self.generator)}, {_dafny.string_of(self.childKeyrings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiKeyring_MultiKeyring) and self.generator == __o.generator and self.childKeyrings == __o.childKeyrings
    def __hash__(self) -> int:
        return super().__hash__()


class RawAES:
    @classmethod
    def default(cls, ):
        return lambda: RawAES_RawAES(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawAES(self) -> bool:
        return isinstance(self, RawAES_RawAES)

class RawAES_RawAES(RawAES, NamedTuple('RawAES', [('keyId', Any), ('providerId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES.RawAES({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawAES_RawAES) and self.keyId == __o.keyId and self.providerId == __o.providerId
    def __hash__(self) -> int:
        return super().__hash__()


class RawEcdh:
    @classmethod
    def default(cls, ):
        return lambda: RawEcdh_RawEcdh(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawEcdh(self) -> bool:
        return isinstance(self, RawEcdh_RawEcdh)

class RawEcdh_RawEcdh(RawEcdh, NamedTuple('RawEcdh', [('senderKeyId', Any), ('recipientKeyId', Any), ('senderPublicKey', Any), ('recipientPublicKey', Any), ('providerId', Any), ('curveSpec', Any), ('keyAgreementScheme', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh.RawEcdh({_dafny.string_of(self.senderKeyId)}, {_dafny.string_of(self.recipientKeyId)}, {_dafny.string_of(self.senderPublicKey)}, {_dafny.string_of(self.recipientPublicKey)}, {_dafny.string_of(self.providerId)}, {_dafny.string_of(self.curveSpec)}, {_dafny.string_of(self.keyAgreementScheme)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawEcdh_RawEcdh) and self.senderKeyId == __o.senderKeyId and self.recipientKeyId == __o.recipientKeyId and self.senderPublicKey == __o.senderPublicKey and self.recipientPublicKey == __o.recipientPublicKey and self.providerId == __o.providerId and self.curveSpec == __o.curveSpec and self.keyAgreementScheme == __o.keyAgreementScheme
    def __hash__(self) -> int:
        return super().__hash__()


class RawRSA:
    @classmethod
    def default(cls, ):
        return lambda: RawRSA_RawRSA(_dafny.Seq(""), _dafny.Seq(""), AwsCryptographyMaterialProvidersTypes.PaddingScheme.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RawRSA(self) -> bool:
        return isinstance(self, RawRSA_RawRSA)

class RawRSA_RawRSA(RawRSA, NamedTuple('RawRSA', [('keyId', Any), ('providerId', Any), ('padding', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA.RawRSA({_dafny.string_of(self.keyId)}, {_dafny.string_of(self.providerId)}, {_dafny.string_of(self.padding)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawRSA_RawRSA) and self.keyId == __o.keyId and self.providerId == __o.providerId and self.padding == __o.padding
    def __hash__(self) -> int:
        return super().__hash__()


class RequiredEncryptionContextCMM:
    @classmethod
    def default(cls, ):
        return lambda: RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(KeyDescription.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RequiredEncryptionContextCMM(self) -> bool:
        return isinstance(self, RequiredEncryptionContextCMM_RequiredEncryptionContextCMM)

class RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(RequiredEncryptionContextCMM, NamedTuple('RequiredEncryptionContextCMM', [('underlying', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM.RequiredEncryptionContextCMM({_dafny.string_of(self.underlying)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RequiredEncryptionContextCMM_RequiredEncryptionContextCMM) and self.underlying == __o.underlying and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class SerializeKeyDescriptionInput:
    @classmethod
    def default(cls, ):
        return lambda: SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SerializeKeyDescriptionInput(self) -> bool:
        return isinstance(self, SerializeKeyDescriptionInput_SerializeKeyDescriptionInput)

class SerializeKeyDescriptionInput_SerializeKeyDescriptionInput(SerializeKeyDescriptionInput, NamedTuple('SerializeKeyDescriptionInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput.SerializeKeyDescriptionInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializeKeyDescriptionInput_SerializeKeyDescriptionInput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class SerializeKeyDescriptionOutput:
    @classmethod
    def default(cls, ):
        return lambda: SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SerializeKeyDescriptionOutput(self) -> bool:
        return isinstance(self, SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput)

class SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(SerializeKeyDescriptionOutput, NamedTuple('SerializeKeyDescriptionOutput', [('json', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput.SerializeKeyDescriptionOutput({_dafny.string_of(self.json)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput) and self.json == __o.json
    def __hash__(self) -> int:
        return super().__hash__()


class StaticKeyring:
    @classmethod
    def default(cls, ):
        return lambda: StaticKeyring_StaticKeyring(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StaticKeyring(self) -> bool:
        return isinstance(self, StaticKeyring_StaticKeyring)

class StaticKeyring_StaticKeyring(StaticKeyring, NamedTuple('StaticKeyring', [('keyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring.StaticKeyring({_dafny.string_of(self.keyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StaticKeyring_StaticKeyring) and self.keyId == __o.keyId
    def __hash__(self) -> int:
        return super().__hash__()


class TestVectorCmmInput:
    @classmethod
    def default(cls, ):
        return lambda: TestVectorCmmInput_TestVectorCmmInput(KeyDescription.default()(), CmmOperation.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVectorCmmInput(self) -> bool:
        return isinstance(self, TestVectorCmmInput_TestVectorCmmInput)

class TestVectorCmmInput_TestVectorCmmInput(TestVectorCmmInput, NamedTuple('TestVectorCmmInput', [('keyDescription', Any), ('forOperation', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput.TestVectorCmmInput({_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.forOperation)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorCmmInput_TestVectorCmmInput) and self.keyDescription == __o.keyDescription and self.forOperation == __o.forOperation
    def __hash__(self) -> int:
        return super().__hash__()


class TestVectorKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: TestVectorKeyringInput_TestVectorKeyringInput(KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVectorKeyringInput(self) -> bool:
        return isinstance(self, TestVectorKeyringInput_TestVectorKeyringInput)

class TestVectorKeyringInput_TestVectorKeyringInput(TestVectorKeyringInput, NamedTuple('TestVectorKeyringInput', [('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput.TestVectorKeyringInput({_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorKeyringInput_TestVectorKeyringInput) and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_KeyVectorException(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyVectorException(self) -> bool:
        return isinstance(self, Error_KeyVectorException)
    @property
    def is_AwsCryptographyMaterialProviders(self) -> bool:
        return isinstance(self, Error_AwsCryptographyMaterialProviders)
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

class Error_KeyVectorException(Error, NamedTuple('KeyVectorException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.KeyVectorException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KeyVectorException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyMaterialProviders(Error, NamedTuple('AwsCryptographyMaterialProviders', [('AwsCryptographyMaterialProviders', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.AwsCryptographyMaterialProviders({_dafny.string_of(self.AwsCryptographyMaterialProviders)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AwsCryptographyMaterialProviders) and self.AwsCryptographyMaterialProviders == __o.AwsCryptographyMaterialProviders
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()

class Error_OpaqueWithText(Error, NamedTuple('OpaqueWithText', [('obj', Any), ('objMessage', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error.OpaqueWithText({_dafny.string_of(self.obj)}, {_dafny.string_of(self.objMessage)})'
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
