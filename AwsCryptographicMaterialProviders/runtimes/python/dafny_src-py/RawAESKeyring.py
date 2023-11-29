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
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring

assert "RawAESKeyring" == __name__
RawAESKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_1143_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_1143_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_1143_encryptedKeyLength_::]))

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @_dafny.classproperty
    def AUTH__TAG__LEN__LEN(instance):
        return 4
    @_dafny.classproperty
    def IV__LEN__LEN(instance):
        return 4

class RawAESKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.RawAESKeyring"
    def OnEncrypt(self, input):
        out244_: Wrappers.Result
        out244_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out244_

    def OnDecrypt(self, input):
        out245_: Wrappers.Result
        out245_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out245_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1144_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1144_materials_ = (input).materials
        d_1145_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1145_suite_ = (d_1144_materials_).algorithmSuite
        d_1146_wrap_: RawAESKeyring.AesWrapKeyMaterial
        nw46_ = RawAESKeyring.AesWrapKeyMaterial()
        nw46_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_1146_wrap_ = nw46_
        d_1147_generateAndWrap_: RawAESKeyring.AesGenerateAndWrapKeyMaterial
        nw47_ = RawAESKeyring.AesGenerateAndWrapKeyMaterial()
        nw47_.ctor__(d_1146_wrap_)
        d_1147_generateAndWrap_ = nw47_
        d_1148_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1149_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        out246_: Wrappers.Result
        out246_ = EdkWrapping.default__.WrapEdkMaterial(d_1144_materials_, d_1146_wrap_, d_1147_generateAndWrap_)
        d_1149_valueOrError0_ = out246_
        if (d_1149_valueOrError0_).IsFailure():
            output = (d_1149_valueOrError0_).PropagateFailure()
            return output
        d_1148_wrapOutput_ = (d_1149_valueOrError0_).Extract()
        d_1150_symmetricSigningKeyList_: Wrappers.Option
        d_1150_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1148_wrapOutput_).symmetricSigningKey).value])) if ((d_1148_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1151_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1151_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_1148_wrapOutput_).wrapInfo).iv), (d_1148_wrapOutput_).wrappedMaterial)
        if (d_1148_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1152_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1153_valueOrError1_: Wrappers.Result = None
            d_1153_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_1144_materials_, (d_1148_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1151_edk_]), d_1150_symmetricSigningKeyList_)
            if (d_1153_valueOrError1_).IsFailure():
                output = (d_1153_valueOrError1_).PropagateFailure()
                return output
            d_1152_result_ = (d_1153_valueOrError1_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1152_result_))
            return output
        elif (d_1148_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1154_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1155_valueOrError2_: Wrappers.Result = None
            d_1155_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1144_materials_, _dafny.Seq([d_1151_edk_]), d_1150_symmetricSigningKeyList_)
            if (d_1155_valueOrError2_).IsFailure():
                output = (d_1155_valueOrError2_).PropagateFailure()
                return output
            d_1154_result_ = (d_1155_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1154_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1156_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1156_materials_ = (input).materials
        d_1157_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1157_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1156_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1157_valueOrError0_).IsFailure():
            output = (d_1157_valueOrError0_).PropagateFailure()
            return output
        d_1158_aad_: _dafny.Seq
        d_1159_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1159_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1159_valueOrError1_).IsFailure():
            output = (d_1159_valueOrError1_).PropagateFailure()
            return output
        d_1158_aad_ = (d_1159_valueOrError1_).Extract()
        d_1160_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1160_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_1160_valueOrError2_).IsFailure():
            output = (d_1160_valueOrError2_).PropagateFailure()
            return output
        d_1161_errors_: _dafny.Seq
        d_1161_errors_ = _dafny.Seq([])
        hi9_: int = len((input).encryptedDataKeys)
        for d_1162_i_ in range(0, hi9_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1162_i_]):
                d_1163_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
                d_1163_edk_ = ((input).encryptedDataKeys)[d_1162_i_]
                d_1164_iv_: _dafny.Seq
                d_1164_iv_ = (self).GetIvFromProvInfo((d_1163_edk_).keyProviderInfo)
                d_1165_unwrap_: RawAESKeyring.AesUnwrapKeyMaterial
                nw48_ = RawAESKeyring.AesUnwrapKeyMaterial()
                nw48_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_1164_iv_, (self).cryptoPrimitives)
                d_1165_unwrap_ = nw48_
                d_1166_unwrapOutput_: Wrappers.Result
                out247_: Wrappers.Result
                out247_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1163_edk_).ciphertext, d_1156_materials_, d_1165_unwrap_)
                d_1166_unwrapOutput_ = out247_
                if (d_1166_unwrapOutput_).is_Success:
                    d_1167_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                    d_1168_valueOrError3_: Wrappers.Result = None
                    d_1168_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1156_materials_, ((d_1166_unwrapOutput_).value).plaintextDataKey, ((d_1166_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1168_valueOrError3_).IsFailure():
                        output = (d_1168_valueOrError3_).PropagateFailure()
                        return output
                    d_1167_result_ = (d_1168_valueOrError3_).Extract()
                    d_1169_value_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
                    d_1169_value_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1167_result_)
                    output = Wrappers.Result_Success(d_1169_value_)
                    return output
                elif True:
                    d_1161_errors_ = (d_1161_errors_) + (_dafny.Seq([(d_1166_unwrapOutput_).error]))
            elif True:
                d_1161_errors_ = (d_1161_errors_) + (_dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncrypedDataKey ")) + (String.default__.Base10Int2String(d_1162_i_))) + (_dafny.Seq(" did not match AESKeyring. ")))]))
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1161_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
        return output
        return output

    def SerializeProviderInfo(self, iv):
        return ((((self).keyName) + (StandardLibrary_mUInt.default__.UInt32ToSeq((((self).wrappingAlgorithm).tagLength) * (8)))) + (StandardLibrary_mUInt.default__.UInt32ToSeq(((self).wrappingAlgorithm).ivLength))) + (iv)

    def ShouldDecryptEDK(self, edk):
        return (((edk).keyProviderId) == ((self).keyNamespace)) and ((self).ValidProviderInfo((edk).keyProviderInfo))

    def ValidProviderInfo(self, info):
        return ((((((len(info)) == ((((len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN)) + ((RawAESKeyring.default__).IV__LEN__LEN)) + (((self).wrappingAlgorithm).ivLength))) and ((_dafny.Seq((info)[0:len((self).keyName):])) == ((self).keyName))) and ((StandardLibrary_mUInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN):]))) == (128))) and ((StandardLibrary_mUInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN):]))) == ((((self).wrappingAlgorithm).tagLength) * (8)))) and ((StandardLibrary_mUInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN):((len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN)) + ((RawAESKeyring.default__).IV__LEN__LEN):]))) == (((self).wrappingAlgorithm).ivLength))) and ((StandardLibrary_mUInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN):((len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN)) + ((RawAESKeyring.default__).IV__LEN__LEN):]))) == (12))

    def GetIvFromProvInfo(self, info):
        return _dafny.Seq((info)[((len((self).keyName)) + ((RawAESKeyring.default__).AUTH__TAG__LEN__LEN)) + ((RawAESKeyring.default__).IV__LEN__LEN)::])

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
        return isinstance(self, RawAESKeyring.AesUnwrapInfo_AesUnwrapInfo)

class AesUnwrapInfo_AesUnwrapInfo(AesUnwrapInfo, NamedTuple('AesUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesUnwrapInfo.AesUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawAESKeyring.AesUnwrapInfo_AesUnwrapInfo)
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
        return isinstance(self, RawAESKeyring.AesWrapInfo_AesWrapInfo)

class AesWrapInfo_AesWrapInfo(AesWrapInfo, NamedTuple('AesWrapInfo', [('iv', Any)])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesWrapInfo.AesWrapInfo({_dafny.string_of(self.iv)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawAESKeyring.AesWrapInfo_AesWrapInfo) and self.iv == __o.iv
    def __hash__(self) -> int:
        return super().__hash__()


class AesGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrap: RawAESKeyring.AesWrapKeyMaterial = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesGenerateAndWrapKeyMaterial"
    def ctor__(self, wrap):
        (self)._wrap = wrap

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        d_1170_generateBytesResult_: Wrappers.Result
        out248_: Wrappers.Result
        out248_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1170_generateBytesResult_ = out248_
        d_1171_plaintextMaterial_: _dafny.Seq
        d_1172_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda84_(d_1173_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1173_e_)

        d_1172_valueOrError0_ = (d_1170_generateBytesResult_).MapFailure(lambda84_)
        if (d_1172_valueOrError0_).IsFailure():
            res = (d_1172_valueOrError0_).PropagateFailure()
            return res
        d_1171_plaintextMaterial_ = (d_1172_valueOrError0_).Extract()
        d_1174_wrapOutput_: MaterialWrapping.WrapOutput
        d_1175_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        out249_: Wrappers.Result
        out249_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1171_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1175_valueOrError1_ = out249_
        if (d_1175_valueOrError1_).IsFailure():
            res = (d_1175_valueOrError1_).PropagateFailure()
            return res
        d_1174_wrapOutput_ = (d_1175_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1171_plaintextMaterial_, (d_1174_wrapOutput_).wrappedMaterial, (d_1174_wrapOutput_).wrapInfo))
        return res

    @property
    def wrap(self):
        return self._wrap

class AesWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesWrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        d_1176_aad_: _dafny.Seq
        d_1177_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1177_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1177_valueOrError0_).IsFailure():
            res = (d_1177_valueOrError0_).PropagateFailure()
            return res
        d_1176_aad_ = (d_1177_valueOrError0_).Extract()
        d_1178_randomIvResult_: Wrappers.Result
        out250_: Wrappers.Result
        out250_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_1178_randomIvResult_ = out250_
        d_1179_iv_: _dafny.Seq
        d_1180_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda85_(d_1181_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1181_e_)

        d_1180_valueOrError1_ = (d_1178_randomIvResult_).MapFailure(lambda85_)
        if (d_1180_valueOrError1_).IsFailure():
            res = (d_1180_valueOrError1_).PropagateFailure()
            return res
        d_1179_iv_ = (d_1180_valueOrError1_).Extract()
        d_1182_aesEncryptResult_: Wrappers.Result
        out251_: Wrappers.Result
        out251_ = ((self).cryptoPrimitives).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_1179_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1176_aad_))
        d_1182_aesEncryptResult_ = out251_
        d_1183_wrappedMaterialResult_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1184_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda86_(d_1185_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1185_e_)

        d_1184_valueOrError2_ = (d_1182_aesEncryptResult_).MapFailure(lambda86_)
        if (d_1184_valueOrError2_).IsFailure():
            res = (d_1184_valueOrError2_).PropagateFailure()
            return res
        d_1183_wrappedMaterialResult_ = (d_1184_valueOrError2_).Extract()
        d_1186_wrappedMaterial_: _dafny.Seq
        d_1186_wrappedMaterial_ = RawAESKeyring.default__.SerializeEDKCiphertext(d_1183_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_1186_wrappedMaterial_, RawAESKeyring.AesWrapInfo_AesWrapInfo(d_1179_iv_)))
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
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesUnwrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, iv, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._iv = iv
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(RawAESKeyring.AesUnwrapInfo.default()))()
        d_1187_aad_: _dafny.Seq
        d_1188_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1188_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1188_valueOrError0_).IsFailure():
            res = (d_1188_valueOrError0_).PropagateFailure()
            return res
        d_1187_aad_ = (d_1188_valueOrError0_).Extract()
        d_1189_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1189_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1189_valueOrError1_).IsFailure():
            res = (d_1189_valueOrError1_).PropagateFailure()
            return res
        d_1190_encryptionOutput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1190_encryptionOutput_ = RawAESKeyring.default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1191_maybePtKey_: Wrappers.Result
        out252_: Wrappers.Result
        out252_ = ((self).cryptoPrimitives).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1190_encryptionOutput_).cipherText, (d_1190_encryptionOutput_).authTag, (self).iv, d_1187_aad_))
        d_1191_maybePtKey_ = out252_
        d_1192_ptKey_: _dafny.Seq
        d_1193_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda87_(d_1194_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1194_e_)

        d_1193_valueOrError2_ = (d_1191_maybePtKey_).MapFailure(lambda87_)
        if (d_1193_valueOrError2_).IsFailure():
            res = (d_1193_valueOrError2_).PropagateFailure()
            return res
        d_1192_ptKey_ = (d_1193_valueOrError2_).Extract()
        d_1195_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1195_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1192_ptKey_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1195_valueOrError3_).IsFailure():
            res = (d_1195_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1192_ptKey_, RawAESKeyring.AesUnwrapInfo_AesUnwrapInfo()))
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
