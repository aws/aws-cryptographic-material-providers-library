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

assert "EdkWrapping" == __name__
EdkWrapping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WrapEdkMaterial(encryptionMaterials, wrap, generateAndWrap):
        ret: Wrappers.Result = None
        d_588_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_588_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for encryption.")))
        if (d_588_valueOrError0_).IsFailure():
            ret = (d_588_valueOrError0_).PropagateFailure()
            return ret
        if (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_589_directOutput_: MaterialWrapping.WrapOutput
            d_590_valueOrError1_: Wrappers.Result = None
            out126_: Wrappers.Result
            out126_ = (wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_590_valueOrError1_ = out126_
            if (d_590_valueOrError1_).IsFailure():
                ret = (d_590_valueOrError1_).PropagateFailure()
                return ret
            d_589_directOutput_ = (d_590_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_589_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_589_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_591_intermediateOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
            d_592_valueOrError2_: Wrappers.Result = None
            out127_: Wrappers.Result
            out127_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, ((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_592_valueOrError2_ = out127_
            if (d_592_valueOrError2_).IsFailure():
                ret = (d_592_valueOrError2_).PropagateFailure()
                return ret
            d_591_intermediateOutput_ = (d_592_valueOrError2_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_591_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_591_intermediateOutput_).symmetricSigningKey), (d_591_intermediateOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_593_directOutput_: MaterialWrapping.GenerateAndWrapOutput
            d_594_valueOrError3_: Wrappers.Result = None
            out128_: Wrappers.Result
            out128_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_594_valueOrError3_ = out128_
            if (d_594_valueOrError3_).IsFailure():
                ret = (d_594_valueOrError3_).PropagateFailure()
                return ret
            d_593_directOutput_ = (d_594_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_593_directOutput_).plaintextMaterial, (d_593_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_593_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_595_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_595_valueOrError4_ = Wrappers.default__.Need((((encryptionMaterials).algorithmSuite).commitment).is_HKDF, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")))
            if (d_595_valueOrError4_).IsFailure():
                ret = (d_595_valueOrError4_).PropagateFailure()
                return ret
            d_596_intermediateOutput_: IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput
            d_597_valueOrError5_: Wrappers.Result = None
            out129_: Wrappers.Result
            out129_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(generateAndWrap, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_597_valueOrError5_ = out129_
            if (d_597_valueOrError5_).IsFailure():
                ret = (d_597_valueOrError5_).PropagateFailure()
                return ret
            d_596_intermediateOutput_ = (d_597_valueOrError5_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_596_intermediateOutput_).plaintextDataKey, (d_596_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_596_intermediateOutput_).symmetricSigningKey), (d_596_intermediateOutput_).wrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def UnwrapEdkMaterial(wrappedMaterial, decryptionMaterials, unwrap):
        ret: Wrappers.Result = None
        d_598_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_598_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidDecryptionMaterials(decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for decryption.")))
        if (d_598_valueOrError0_).IsFailure():
            ret = (d_598_valueOrError0_).PropagateFailure()
            return ret
        if (((decryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            d_599_directOutput_: MaterialWrapping.UnwrapOutput
            d_600_valueOrError1_: Wrappers.Result = None
            out130_: Wrappers.Result
            out130_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext))
            d_600_valueOrError1_ = out130_
            if (d_600_valueOrError1_).IsFailure():
                ret = (d_600_valueOrError1_).PropagateFailure()
                return ret
            d_599_directOutput_ = (d_600_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_599_directOutput_).unwrappedMaterial, Wrappers.Option_None(), (d_599_directOutput_).unwrapInfo))
            return ret
        elif (((decryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping:
            d_601_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_601_valueOrError2_ = Wrappers.default__.Need((len(wrappedMaterial)) >= ((((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).keyLength) + (((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).tagLength)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid material for Intermediate Unwrapping")))
            if (d_601_valueOrError2_).IsFailure():
                ret = (d_601_valueOrError2_).PropagateFailure()
                return ret
            d_602_intermediateOutput_: IntermediateKeyWrapping.IntermediateUnwrapOutput
            d_603_valueOrError3_: Wrappers.Result = None
            out131_: Wrappers.Result
            out131_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(unwrap, wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext)
            d_603_valueOrError3_ = out131_
            if (d_603_valueOrError3_).IsFailure():
                ret = (d_603_valueOrError3_).PropagateFailure()
                return ret
            d_602_intermediateOutput_ = (d_603_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(EdkWrapping.UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_602_intermediateOutput_).plaintextDataKey, Wrappers.Option_Some((d_602_intermediateOutput_).symmetricSigningKey), (d_602_intermediateOutput_).unwrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def GetProviderWrappedMaterial(material, algSuite):
        if ((algSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            return Wrappers.Result_Success(material)
        elif True:
            d_604_deserializedWrappedRes_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(material, algSuite)
            if (d_604_deserializedWrappedRes_).is_Failure:
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material.")))
            elif True:
                return Wrappers.Result_Success(((d_604_deserializedWrappedRes_).value).providerWrappedIkm)


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

