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

# Module: EdkWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WrapEdkMaterial(encryptionMaterials, wrap, generateAndWrap):
        ret: Wrappers.Result = None
        d_400_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_400_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for encryption.")))
        if (d_400_valueOrError0_).IsFailure():
            ret = (d_400_valueOrError0_).PropagateFailure()
            return ret
        if (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_401_directOutput_: MaterialWrapping.WrapOutput
            d_402_valueOrError1_: Wrappers.Result = None
            out82_: Wrappers.Result
            out82_ = (wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_402_valueOrError1_ = out82_
            if (d_402_valueOrError1_).IsFailure():
                ret = (d_402_valueOrError1_).PropagateFailure()
                return ret
            d_401_directOutput_ = (d_402_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_401_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_401_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_Some) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_403_intermediateOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
            d_404_valueOrError2_: Wrappers.Result = None
            out83_: Wrappers.Result
            out83_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, ((encryptionMaterials).plaintextDataKey).value, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_404_valueOrError2_ = out83_
            if (d_404_valueOrError2_).IsFailure():
                ret = (d_404_valueOrError2_).PropagateFailure()
                return ret
            d_403_intermediateOutput_ = (d_404_valueOrError2_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput((d_403_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_403_intermediateOutput_).symmetricSigningKey), (d_403_intermediateOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING):
            d_405_directOutput_: MaterialWrapping.GenerateAndWrapOutput
            d_406_valueOrError3_: Wrappers.Result = None
            out84_: Wrappers.Result
            out84_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext))
            d_406_valueOrError3_ = out84_
            if (d_406_valueOrError3_).IsFailure():
                ret = (d_406_valueOrError3_).PropagateFailure()
                return ret
            d_405_directOutput_ = (d_406_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_405_directOutput_).plaintextMaterial, (d_405_directOutput_).wrappedMaterial, Wrappers.Option_None(), (d_405_directOutput_).wrapInfo))
            return ret
        elif (((encryptionMaterials).plaintextDataKey).is_None) and ((((encryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping):
            d_407_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_407_valueOrError4_ = Wrappers.default__.Need((((encryptionMaterials).algorithmSuite).commitment).is_HKDF, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")))
            if (d_407_valueOrError4_).IsFailure():
                ret = (d_407_valueOrError4_).PropagateFailure()
                return ret
            d_408_intermediateOutput_: IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput
            d_409_valueOrError5_: Wrappers.Result = None
            out85_: Wrappers.Result
            out85_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(generateAndWrap, (encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext)
            d_409_valueOrError5_ = out85_
            if (d_409_valueOrError5_).IsFailure():
                ret = (d_409_valueOrError5_).PropagateFailure()
                return ret
            d_408_intermediateOutput_ = (d_409_valueOrError5_).Extract()
            ret = Wrappers.Result_Success(WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput((d_408_intermediateOutput_).plaintextDataKey, (d_408_intermediateOutput_).wrappedMaterial, Wrappers.Option_Some((d_408_intermediateOutput_).symmetricSigningKey), (d_408_intermediateOutput_).wrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def UnwrapEdkMaterial(wrappedMaterial, decryptionMaterials, unwrap):
        ret: Wrappers.Result = None
        d_410_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_410_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidDecryptionMaterials(decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid materials for decryption.")))
        if (d_410_valueOrError0_).IsFailure():
            ret = (d_410_valueOrError0_).PropagateFailure()
            return ret
        if (((decryptionMaterials).algorithmSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            d_411_directOutput_: MaterialWrapping.UnwrapOutput
            d_412_valueOrError1_: Wrappers.Result = None
            out86_: Wrappers.Result
            out86_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext))
            d_412_valueOrError1_ = out86_
            if (d_412_valueOrError1_).IsFailure():
                ret = (d_412_valueOrError1_).PropagateFailure()
                return ret
            d_411_directOutput_ = (d_412_valueOrError1_).Extract()
            ret = Wrappers.Result_Success(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_411_directOutput_).unwrappedMaterial, Wrappers.Option_None(), (d_411_directOutput_).unwrapInfo))
            return ret
        elif (((decryptionMaterials).algorithmSuite).edkWrapping).is_IntermediateKeyWrapping:
            d_413_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_413_valueOrError2_ = Wrappers.default__.Need((len(wrappedMaterial)) >= ((((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).keyLength) + (((((decryptionMaterials).algorithmSuite).encrypt).AES__GCM).tagLength)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid material for Intermediate Unwrapping")))
            if (d_413_valueOrError2_).IsFailure():
                ret = (d_413_valueOrError2_).PropagateFailure()
                return ret
            d_414_intermediateOutput_: IntermediateKeyWrapping.IntermediateUnwrapOutput
            d_415_valueOrError3_: Wrappers.Result = None
            out87_: Wrappers.Result
            out87_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(unwrap, wrappedMaterial, (decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext)
            d_415_valueOrError3_ = out87_
            if (d_415_valueOrError3_).IsFailure():
                ret = (d_415_valueOrError3_).PropagateFailure()
                return ret
            d_414_intermediateOutput_ = (d_415_valueOrError3_).Extract()
            ret = Wrappers.Result_Success(UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput((d_414_intermediateOutput_).plaintextDataKey, Wrappers.Option_Some((d_414_intermediateOutput_).symmetricSigningKey), (d_414_intermediateOutput_).unwrapInfo))
            return ret
        elif True:
            pass
        return ret

    @staticmethod
    def GetProviderWrappedMaterial(material, algSuite):
        if ((algSuite).edkWrapping).is_DIRECT__KEY__WRAPPING:
            return Wrappers.Result_Success(material)
        elif True:
            d_416_deserializedWrappedRes_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(material, algSuite)
            if (d_416_deserializedWrappedRes_).is_Failure:
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material.")))
            elif True:
                return Wrappers.Result_Success(((d_416_deserializedWrappedRes_).value).providerWrappedIkm)


class WrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapOnlyEdkMaterialOutput(self) -> bool:
        return isinstance(self, WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput)
    @property
    def is_GenerateAndWrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput)

class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('WrapOnlyEdkMaterialOutput', [('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.WrapOnlyEdkMaterialOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()

class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput(WrapEdkMaterialOutput, NamedTuple('GenerateAndWrapEdkMaterialOutput', [('plaintextDataKey', Any), ('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.WrapEdkMaterialOutput.GenerateAndWrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapEdkMaterialOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(_dafny.Seq({}), Wrappers.Option.default()(), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapEdkMaterialOutput(self) -> bool:
        return isinstance(self, UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput)

class UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput(UnwrapEdkMaterialOutput, NamedTuple('UnwrapEdkMaterialOutput', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'EdkWrapping.UnwrapEdkMaterialOutput.UnwrapEdkMaterialOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapEdkMaterialOutput_UnwrapEdkMaterialOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()

