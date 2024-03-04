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
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring

# Module: RawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_1040_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_1040_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_1040_encryptedKeyLength_::]))

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @_dafny.classproperty
    def AUTH__TAG__LEN__LEN(instance):
        return 4
    @_dafny.classproperty
    def IV__LEN__LEN(instance):
        return 4

class RawAESKeyring(Keyring.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient = None
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software.amazon.cryptography.primitives.internaldafny.types.AES__GCM = None
        self._keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.RawAESKeyring"
    def OnEncrypt(self, input):
        out193_: Wrappers.Result
        out193_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnEncrypt(self, input)
        return out193_

    def OnDecrypt(self, input):
        out194_: Wrappers.Result
        out194_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnDecrypt(self, input)
        return out194_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1041_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
        d_1041_materials_ = (input).materials
        d_1042_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_1042_suite_ = (d_1041_materials_).algorithmSuite
        d_1043_wrap_: AesWrapKeyMaterial
        nw45_ = AesWrapKeyMaterial()
        nw45_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_1043_wrap_ = nw45_
        d_1044_generateAndWrap_: AesGenerateAndWrapKeyMaterial
        nw46_ = AesGenerateAndWrapKeyMaterial()
        nw46_.ctor__(d_1043_wrap_)
        d_1044_generateAndWrap_ = nw46_
        d_1045_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1046_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AesWrapInfo.default()))()
        out195_: Wrappers.Result
        out195_ = EdkWrapping.default__.WrapEdkMaterial(d_1041_materials_, d_1043_wrap_, d_1044_generateAndWrap_)
        d_1046_valueOrError0_ = out195_
        if (d_1046_valueOrError0_).IsFailure():
            output = (d_1046_valueOrError0_).PropagateFailure()
            return output
        d_1045_wrapOutput_ = (d_1046_valueOrError0_).Extract()
        d_1047_symmetricSigningKeyList_: Wrappers.Option
        d_1047_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1045_wrapOutput_).symmetricSigningKey).value])) if ((d_1045_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1048_edk_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey
        d_1048_edk_ = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_1045_wrapOutput_).wrapInfo).iv), (d_1045_wrapOutput_).wrappedMaterial)
        if (d_1045_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1049_result_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
            d_1050_valueOrError1_: Wrappers.Result = None
            d_1050_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_1041_materials_, (d_1045_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1048_edk_]), d_1047_symmetricSigningKeyList_)
            if (d_1050_valueOrError1_).IsFailure():
                output = (d_1050_valueOrError1_).PropagateFailure()
                return output
            d_1049_result_ = (d_1050_valueOrError1_).Extract()
            output = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput_OnEncryptOutput(d_1049_result_))
            return output
        elif (d_1045_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1051_result_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
            d_1052_valueOrError2_: Wrappers.Result = None
            d_1052_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1041_materials_, _dafny.Seq([d_1048_edk_]), d_1047_symmetricSigningKeyList_)
            if (d_1052_valueOrError2_).IsFailure():
                output = (d_1052_valueOrError2_).PropagateFailure()
                return output
            d_1051_result_ = (d_1052_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput_OnEncryptOutput(d_1051_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1053_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_1053_materials_ = (input).materials
        d_1054_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1054_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1053_materials_), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1054_valueOrError0_).IsFailure():
            output = (d_1054_valueOrError0_).PropagateFailure()
            return output
        d_1055_aad_: _dafny.Seq
        d_1056_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1056_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1056_valueOrError1_).IsFailure():
            output = (d_1056_valueOrError1_).PropagateFailure()
            return output
        d_1055_aad_ = (d_1056_valueOrError1_).Extract()
        d_1057_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1057_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_1057_valueOrError2_).IsFailure():
            output = (d_1057_valueOrError2_).PropagateFailure()
            return output
        d_1058_errors_: _dafny.Seq
        d_1058_errors_ = _dafny.Seq([])
        hi8_ = len((input).encryptedDataKeys)
        for d_1059_i_ in range(0, hi8_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1059_i_]):
                d_1060_edk_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey
                d_1060_edk_ = ((input).encryptedDataKeys)[d_1059_i_]
                d_1061_iv_: _dafny.Seq
                d_1061_iv_ = (self).GetIvFromProvInfo((d_1060_edk_).keyProviderInfo)
                d_1062_unwrap_: AesUnwrapKeyMaterial
                nw47_ = AesUnwrapKeyMaterial()
                nw47_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_1061_iv_, (self).cryptoPrimitives)
                d_1062_unwrap_ = nw47_
                d_1063_unwrapOutput_: Wrappers.Result
                out196_: Wrappers.Result
                out196_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1060_edk_).ciphertext, d_1053_materials_, d_1062_unwrap_)
                d_1063_unwrapOutput_ = out196_
                if (d_1063_unwrapOutput_).is_Success:
                    d_1064_result_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
                    d_1065_valueOrError3_: Wrappers.Result = None
                    d_1065_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1053_materials_, ((d_1063_unwrapOutput_).value).plaintextDataKey, ((d_1063_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1065_valueOrError3_).IsFailure():
                        output = (d_1065_valueOrError3_).PropagateFailure()
                        return output
                    d_1064_result_ = (d_1065_valueOrError3_).Extract()
                    d_1066_value_: software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput
                    d_1066_value_ = software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput_OnDecryptOutput(d_1064_result_)
                    output = Wrappers.Result_Success(d_1066_value_)
                    return output
                elif True:
                    d_1058_errors_ = (d_1058_errors_) + (_dafny.Seq([(d_1063_unwrapOutput_).error]))
            elif True:
                d_1058_errors_ = (d_1058_errors_) + (_dafny.Seq([software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncrypedDataKey ")) + (StandardLibrary_String.default__.Base10Int2String(d_1059_i_))) + (_dafny.Seq(" did not match AESKeyring. ")))]))
        output = Wrappers.Result_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors(d_1058_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
        return output
        return output

    def SerializeProviderInfo(self, iv):
        return ((((self).keyName) + (StandardLibrary_UInt.default__.UInt32ToSeq((((self).wrappingAlgorithm).tagLength) * (8)))) + (StandardLibrary_UInt.default__.UInt32ToSeq(((self).wrappingAlgorithm).ivLength))) + (iv)

    def ShouldDecryptEDK(self, edk):
        return (((edk).keyProviderId) == ((self).keyNamespace)) and ((self).ValidProviderInfo((edk).keyProviderInfo))

    def ValidProviderInfo(self, info):
        return ((((((len(info)) == ((((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN)) + (((self).wrappingAlgorithm).ivLength))) and ((_dafny.Seq((info)[0:len((self).keyName):])) == ((self).keyName))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):]))) == (128))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):]))) == ((((self).wrappingAlgorithm).tagLength) * (8)))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN):]))) == (((self).wrappingAlgorithm).ivLength))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN):]))) == (12))

    def GetIvFromProvInfo(self, info):
        return _dafny.Seq((info)[((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN)::])

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def keyNamespace(self):
        return self._keyNamespace
    @property
    def keyName(self):
        return self._keyName

class AesUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AesUnwrapInfo_AesUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: AesUnwrapInfo_AesUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AesUnwrapInfo(self) -> bool:
        return isinstance(self, AesUnwrapInfo_AesUnwrapInfo)

class AesUnwrapInfo_AesUnwrapInfo(AesUnwrapInfo, NamedTuple('AesUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesUnwrapInfo.AesUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesUnwrapInfo_AesUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class AesWrapInfo:
    @classmethod
    def default(cls, ):
        return lambda: AesWrapInfo_AesWrapInfo(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AesWrapInfo(self) -> bool:
        return isinstance(self, AesWrapInfo_AesWrapInfo)

class AesWrapInfo_AesWrapInfo(AesWrapInfo, NamedTuple('AesWrapInfo', [('iv', Any)])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesWrapInfo.AesWrapInfo({_dafny.string_of(self.iv)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesWrapInfo_AesWrapInfo) and self.iv == __o.iv
    def __hash__(self) -> int:
        return super().__hash__()


class AesGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrap: AesWrapKeyMaterial = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesGenerateAndWrapKeyMaterial"
    def ctor__(self, wrap):
        (self)._wrap = wrap

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(AesWrapInfo.default()))()
        d_1067_generateBytesResult_: Wrappers.Result
        out197_: Wrappers.Result
        out197_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1067_generateBytesResult_ = out197_
        d_1068_plaintextMaterial_: _dafny.Seq
        d_1069_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda84_(d_1070_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_1070_e_)

        d_1069_valueOrError0_ = (d_1067_generateBytesResult_).MapFailure(lambda84_)
        if (d_1069_valueOrError0_).IsFailure():
            res = (d_1069_valueOrError0_).PropagateFailure()
            return res
        d_1068_plaintextMaterial_ = (d_1069_valueOrError0_).Extract()
        d_1071_wrapOutput_: MaterialWrapping.WrapOutput
        d_1072_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        out198_: Wrappers.Result
        out198_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1068_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1072_valueOrError1_ = out198_
        if (d_1072_valueOrError1_).IsFailure():
            res = (d_1072_valueOrError1_).PropagateFailure()
            return res
        d_1071_wrapOutput_ = (d_1072_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1068_plaintextMaterial_, (d_1071_wrapOutput_).wrappedMaterial, (d_1071_wrapOutput_).wrapInfo))
        return res

    @property
    def wrap(self):
        return self._wrap

class AesWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software.amazon.cryptography.primitives.internaldafny.types.AES__GCM = None
        self._cryptoPrimitives: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesWrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        d_1073_aad_: _dafny.Seq
        d_1074_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1074_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1074_valueOrError0_).IsFailure():
            res = (d_1074_valueOrError0_).PropagateFailure()
            return res
        d_1073_aad_ = (d_1074_valueOrError0_).Extract()
        d_1075_randomIvResult_: Wrappers.Result
        out199_: Wrappers.Result
        out199_ = ((self).cryptoPrimitives).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_1075_randomIvResult_ = out199_
        d_1076_iv_: _dafny.Seq
        d_1077_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda85_(d_1078_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_1078_e_)

        d_1077_valueOrError1_ = (d_1075_randomIvResult_).MapFailure(lambda85_)
        if (d_1077_valueOrError1_).IsFailure():
            res = (d_1077_valueOrError1_).PropagateFailure()
            return res
        d_1076_iv_ = (d_1077_valueOrError1_).Extract()
        d_1079_aesEncryptResult_: Wrappers.Result
        out200_: Wrappers.Result
        out200_ = ((self).cryptoPrimitives).AESEncrypt(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_1076_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1073_aad_))
        d_1079_aesEncryptResult_ = out200_
        d_1080_wrappedMaterialResult_: software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput
        d_1081_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.default())()
        def lambda86_(d_1082_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_1082_e_)

        d_1081_valueOrError2_ = (d_1079_aesEncryptResult_).MapFailure(lambda86_)
        if (d_1081_valueOrError2_).IsFailure():
            res = (d_1081_valueOrError2_).PropagateFailure()
            return res
        d_1080_wrappedMaterialResult_ = (d_1081_valueOrError2_).Extract()
        d_1083_wrappedMaterial_: _dafny.Seq
        d_1083_wrappedMaterial_ = default__.SerializeEDKCiphertext(d_1080_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_1083_wrappedMaterial_, AesWrapInfo_AesWrapInfo(d_1076_iv_)))
        return res
        return res

    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives

class AesUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._iv: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software.amazon.cryptography.primitives.internaldafny.types.AES__GCM = None
        self._cryptoPrimitives: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesUnwrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, iv, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._iv = iv
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(AesUnwrapInfo.default()))()
        d_1084_aad_: _dafny.Seq
        d_1085_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1085_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1085_valueOrError0_).IsFailure():
            res = (d_1085_valueOrError0_).PropagateFailure()
            return res
        d_1084_aad_ = (d_1085_valueOrError0_).Extract()
        d_1086_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1086_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1086_valueOrError1_).IsFailure():
            res = (d_1086_valueOrError1_).PropagateFailure()
            return res
        d_1087_encryptionOutput_: software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput
        d_1087_encryptionOutput_ = default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1088_maybePtKey_: Wrappers.Result
        out201_: Wrappers.Result
        out201_ = ((self).cryptoPrimitives).AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1087_encryptionOutput_).cipherText, (d_1087_encryptionOutput_).authTag, (self).iv, d_1084_aad_))
        d_1088_maybePtKey_ = out201_
        d_1089_ptKey_: _dafny.Seq
        d_1090_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda87_(d_1091_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_1091_e_)

        d_1090_valueOrError2_ = (d_1088_maybePtKey_).MapFailure(lambda87_)
        if (d_1090_valueOrError2_).IsFailure():
            res = (d_1090_valueOrError2_).PropagateFailure()
            return res
        d_1089_ptKey_ = (d_1090_valueOrError2_).Extract()
        d_1092_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1092_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1089_ptKey_)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1092_valueOrError3_).IsFailure():
            res = (d_1092_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1089_ptKey_, AesUnwrapInfo_AesUnwrapInfo()))
        return res
        return res

    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def iv(self):
        return self._iv
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
