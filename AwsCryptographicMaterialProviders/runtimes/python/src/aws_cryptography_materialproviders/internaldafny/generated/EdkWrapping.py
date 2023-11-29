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

# assert "EdkWrapping" == __name__
EdkWrapping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WrapEdkMaterial(encryptionMaterials, wrap, generateAndWrap):
        ret: Wrappers.Result = None
        d_787_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_787_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for encryption.")))
        if (d_787_valueOrError0_).IsFailure():
            ret = (d_787_valueOrError0_).PropagateFailure()
            return ret
        if (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_788_directOutput_: MaterialWrapping.WrapOutput
            d_789_valueOrError1_: Wrappers.Result = None
            out203_: Wrappers.Result
            out203_ = (wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_789_valueOrError1_ = out203_
            if (d_789_valueOrError1_).IsFailure():
                ret = (d_789_valueOrError1_).PropagateFailure()
                return ret
            d_788_directOutput_ = (d_789_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_788_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_788_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_790_intermediateOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
            d_791_valueOrError2_: Wrappers.Result = None
            out204_: Wrappers.Result
            out204_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, ((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_791_valueOrError2_ = out204_
            if (d_791_valueOrError2_).IsFailure():
                ret = (d_791_valueOrError2_).PropagateFailure()
                return ret
            d_790_intermediateOutput_ = (d_791_valueOrError2_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_790_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_790_intermediateOutput_).symmetricSigningKey), (d_790_intermediateOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_792_directOutput_: MaterialWrapping.GenerateAndWrapOutput
            d_793_valueOrError3_: Wrappers.Result = None
            out205_: Wrappers.Result
            out205_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_793_valueOrError3_ = out205_
            if (d_793_valueOrError3_).IsFailure():
                ret = (d_793_valueOrError3_).PropagateFailure()
                return ret
            d_792_directOutput_ = (d_793_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_792_directOutput_).plaintextMaterial, (d_792_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_792_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_794_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_794_valueOrError4_ = Wrappers.default__.Need((((encryptionMaterials).algorithmSuite).commitment).is_HKDF, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")))
            if (d_794_valueOrError4_).IsFailure():
                ret = (d_794_valueOrError4_).PropagateFailure()
                return ret
            d_795_intermediateOutput_: IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput
            d_796_valueOrError5_: Wrappers.Result = None
            out206_: Wrappers.Result
            out206_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(generateAndWrap, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_796_valueOrError5_ = out206_
            if (d_796_valueOrError5_).IsFailure():
                ret = (d_796_valueOrError5_).PropagateFailure()
                return ret
            d_795_intermediateOutput_ = (d_796_valueOrError5_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_795_intermediateOutput_).plaintextDataKey, (d_795_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_795_intermediateOutput_).symmetricSigningKey), (d_795_intermediateOutput_).wrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def UnwrapEdkMaterial(wrappedMaterial, decryptionMaterials, unwrap):
        ret: Wrappers.Result = None
        d_797_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_797_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidDecryptionMaterials(decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for decryption.")))
        if (d_797_valueOrError0_).IsFailure():
            ret = (d_797_valueOrError0_).PropagateFailure()
            return ret
        if (((decryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            d_798_directOutput_: MaterialWrapping.UnwrapOutput
            d_799_valueOrError1_: Wrappers.Result = None
            out207_: Wrappers.Result
            out207_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext))
            d_799_valueOrError1_ = out207_
            if (d_799_valueOrError1_).IsFailure():
                ret = (d_799_valueOrError1_).PropagateFailure()
                return ret
            d_798_directOutput_ = (d_799_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_798_directOutput_).unwrappedMaterial, Wrappers.Option_None(), (d_798_directOutput_).unwrapInfo))
            return ret
        elif (((decryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping:
            d_800_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_800_valueOrError2_ = Wrappers.default__.Need((len(wrappedMaterial)) >= ((((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).keyLength) + (((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).tagLength)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid material for Intermediate Unwrapping")))
            if (d_800_valueOrError2_).IsFailure():
                ret = (d_800_valueOrError2_).PropagateFailure()
                return ret
            d_801_intermediateOutput_: IntermediateKeyWrapping.IntermediateUnwrapOutput
            d_802_valueOrError3_: Wrappers.Result = None
            out208_: Wrappers.Result
            out208_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(unwrap, wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext)
            d_802_valueOrError3_ = out208_
            if (d_802_valueOrError3_).IsFailure():
                ret = (d_802_valueOrError3_).PropagateFailure()
                return ret
            d_801_intermediateOutput_ = (d_802_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_801_intermediateOutput_).plaintextDataKey, Wrappers.Option_Some((d_801_intermediateOutput_).symmetricSigningKey), (d_801_intermediateOutput_).unwrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def GetProviderWrappedMaterial(material, algSuite):
        if ((algSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            return Wrappers.Result_Success(material)
        elif True:
            d_803_deserializedWrappedRes_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(material, algSuite)
            if (d_803_deserializedWrappedRes_).is_Failure:
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material.")))
            elif True:
                return Wrappers.Result_Success(((d_803_deserializedWrappedRes_).value).providerWrappedIkm)


class WrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option_None.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapOnlyEdkMaterialOutput(self) -> bool:
        return isinstance(self, EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput)
    @property
    def is_GenerateAndWrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput)

class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('WrapOnlyEdkMaterialOutput', [('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.WrapOnlyEdkMaterialOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()

class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('GenerateAndWrapEdkMaterialOutput', [('plaintextDataKey', Any), ('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.GenerateAndWrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option_None.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput)

class UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(UnwrapEdkMaterialOutput, NamedTuple('UnwrapEdkMaterialOutput', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.UnwrapEdkMaterialOutput.UnwrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()

