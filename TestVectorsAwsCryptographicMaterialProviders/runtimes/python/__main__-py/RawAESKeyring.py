import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
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
        d_956_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_956_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_956_encryptedKeyLength_::]))

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
        out200_: Wrappers.Result
        out200_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out200_

    def OnDecrypt(self, input):
        out201_: Wrappers.Result
        out201_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out201_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_957_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_957_materials_ = (input).materials
        d_958_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_958_suite_ = (d_957_materials_).algorithmSuite
        d_959_wrap_: AesWrapKeyMaterial
        nw45_ = AesWrapKeyMaterial()
        nw45_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_959_wrap_ = nw45_
        d_960_generateAndWrap_: AesGenerateAndWrapKeyMaterial
        nw46_ = AesGenerateAndWrapKeyMaterial()
        nw46_.ctor__(d_959_wrap_)
        d_960_generateAndWrap_ = nw46_
        d_961_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_962_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AesWrapInfo.default()))()
        out202_: Wrappers.Result
        out202_ = EdkWrapping.default__.WrapEdkMaterial(d_957_materials_, d_959_wrap_, d_960_generateAndWrap_)
        d_962_valueOrError0_ = out202_
        if (d_962_valueOrError0_).IsFailure():
            output = (d_962_valueOrError0_).PropagateFailure()
            return output
        d_961_wrapOutput_ = (d_962_valueOrError0_).Extract()
        d_963_symmetricSigningKeyList_: Wrappers.Option
        d_963_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_961_wrapOutput_).symmetricSigningKey).value])) if ((d_961_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_964_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_964_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_961_wrapOutput_).wrapInfo).iv), (d_961_wrapOutput_).wrappedMaterial)
        if (d_961_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_965_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_966_valueOrError1_: Wrappers.Result = None
            d_966_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_957_materials_, (d_961_wrapOutput_).plaintextDataKey, _dafny.Seq([d_964_edk_]), d_963_symmetricSigningKeyList_)
            if (d_966_valueOrError1_).IsFailure():
                output = (d_966_valueOrError1_).PropagateFailure()
                return output
            d_965_result_ = (d_966_valueOrError1_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_965_result_))
            return output
        elif (d_961_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_967_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_968_valueOrError2_: Wrappers.Result = None
            d_968_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_957_materials_, _dafny.Seq([d_964_edk_]), d_963_symmetricSigningKeyList_)
            if (d_968_valueOrError2_).IsFailure():
                output = (d_968_valueOrError2_).PropagateFailure()
                return output
            d_967_result_ = (d_968_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_967_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_969_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_969_materials_ = (input).materials
        d_970_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_970_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_969_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_970_valueOrError0_).IsFailure():
            output = (d_970_valueOrError0_).PropagateFailure()
            return output
        d_971_aad_: _dafny.Seq
        d_972_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_972_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_972_valueOrError1_).IsFailure():
            output = (d_972_valueOrError1_).PropagateFailure()
            return output
        d_971_aad_ = (d_972_valueOrError1_).Extract()
        d_973_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_973_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_973_valueOrError2_).IsFailure():
            output = (d_973_valueOrError2_).PropagateFailure()
            return output
        d_974_errors_: _dafny.Seq
        d_974_errors_ = _dafny.Seq([])
        hi9_ = len((input).encryptedDataKeys)
        for d_975_i_ in range(0, hi9_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_975_i_]):
                d_976_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
                d_976_edk_ = ((input).encryptedDataKeys)[d_975_i_]
                d_977_iv_: _dafny.Seq
                d_977_iv_ = (self).GetIvFromProvInfo((d_976_edk_).keyProviderInfo)
                d_978_unwrap_: AesUnwrapKeyMaterial
                nw47_ = AesUnwrapKeyMaterial()
                nw47_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_977_iv_, (self).cryptoPrimitives)
                d_978_unwrap_ = nw47_
                d_979_unwrapOutput_: Wrappers.Result
                out203_: Wrappers.Result
                out203_ = EdkWrapping.default__.UnwrapEdkMaterial((d_976_edk_).ciphertext, d_969_materials_, d_978_unwrap_)
                d_979_unwrapOutput_ = out203_
                if (d_979_unwrapOutput_).is_Success:
                    d_980_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                    d_981_valueOrError3_: Wrappers.Result = None
                    d_981_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_969_materials_, ((d_979_unwrapOutput_).value).plaintextDataKey, ((d_979_unwrapOutput_).value).symmetricSigningKey)
                    if (d_981_valueOrError3_).IsFailure():
                        output = (d_981_valueOrError3_).PropagateFailure()
                        return output
                    d_980_result_ = (d_981_valueOrError3_).Extract()
                    d_982_value_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
                    d_982_value_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_980_result_)
                    output = Wrappers.Result_Success(d_982_value_)
                    return output
                elif True:
                    d_974_errors_ = (d_974_errors_) + (_dafny.Seq([(d_979_unwrapOutput_).error]))
            elif True:
                d_974_errors_ = (d_974_errors_) + (_dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncrypedDataKey ")) + (StandardLibrary_String.default__.Base10Int2String(d_975_i_))) + (_dafny.Seq(" did not match AESKeyring. ")))]))
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_974_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
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
        d_983_generateBytesResult_: Wrappers.Result
        out204_: Wrappers.Result
        out204_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_983_generateBytesResult_ = out204_
        d_984_plaintextMaterial_: _dafny.Seq
        d_985_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda62_(d_986_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_986_e_)

        d_985_valueOrError0_ = (d_983_generateBytesResult_).MapFailure(lambda62_)
        if (d_985_valueOrError0_).IsFailure():
            res = (d_985_valueOrError0_).PropagateFailure()
            return res
        d_984_plaintextMaterial_ = (d_985_valueOrError0_).Extract()
        d_987_wrapOutput_: MaterialWrapping.WrapOutput
        d_988_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        out205_: Wrappers.Result
        out205_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_984_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_988_valueOrError1_ = out205_
        if (d_988_valueOrError1_).IsFailure():
            res = (d_988_valueOrError1_).PropagateFailure()
            return res
        d_987_wrapOutput_ = (d_988_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_984_plaintextMaterial_, (d_987_wrapOutput_).wrappedMaterial, (d_987_wrapOutput_).wrapInfo))
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
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        d_989_aad_: _dafny.Seq
        d_990_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_990_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_990_valueOrError0_).IsFailure():
            res = (d_990_valueOrError0_).PropagateFailure()
            return res
        d_989_aad_ = (d_990_valueOrError0_).Extract()
        d_991_randomIvResult_: Wrappers.Result
        out206_: Wrappers.Result
        out206_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_991_randomIvResult_ = out206_
        d_992_iv_: _dafny.Seq
        d_993_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda63_(d_994_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_994_e_)

        d_993_valueOrError1_ = (d_991_randomIvResult_).MapFailure(lambda63_)
        if (d_993_valueOrError1_).IsFailure():
            res = (d_993_valueOrError1_).PropagateFailure()
            return res
        d_992_iv_ = (d_993_valueOrError1_).Extract()
        d_995_aesEncryptResult_: Wrappers.Result
        out207_: Wrappers.Result
        out207_ = ((self).cryptoPrimitives).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_992_iv_, (self).wrappingKey, (input).plaintextMaterial, d_989_aad_))
        d_995_aesEncryptResult_ = out207_
        d_996_wrappedMaterialResult_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_997_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda64_(d_998_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_998_e_)

        d_997_valueOrError2_ = (d_995_aesEncryptResult_).MapFailure(lambda64_)
        if (d_997_valueOrError2_).IsFailure():
            res = (d_997_valueOrError2_).PropagateFailure()
            return res
        d_996_wrappedMaterialResult_ = (d_997_valueOrError2_).Extract()
        d_999_wrappedMaterial_: _dafny.Seq
        d_999_wrappedMaterial_ = default__.SerializeEDKCiphertext(d_996_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_999_wrappedMaterial_, AesWrapInfo_AesWrapInfo(d_992_iv_)))
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
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(AesUnwrapInfo.default()))()
        d_1000_aad_: _dafny.Seq
        d_1001_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1001_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1001_valueOrError0_).IsFailure():
            res = (d_1001_valueOrError0_).PropagateFailure()
            return res
        d_1000_aad_ = (d_1001_valueOrError0_).Extract()
        d_1002_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1002_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1002_valueOrError1_).IsFailure():
            res = (d_1002_valueOrError1_).PropagateFailure()
            return res
        d_1003_encryptionOutput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1003_encryptionOutput_ = default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1004_maybePtKey_: Wrappers.Result
        out208_: Wrappers.Result
        out208_ = ((self).cryptoPrimitives).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1003_encryptionOutput_).cipherText, (d_1003_encryptionOutput_).authTag, (self).iv, d_1000_aad_))
        d_1004_maybePtKey_ = out208_
        d_1005_ptKey_: _dafny.Seq
        d_1006_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda65_(d_1007_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1007_e_)

        d_1006_valueOrError2_ = (d_1004_maybePtKey_).MapFailure(lambda65_)
        if (d_1006_valueOrError2_).IsFailure():
            res = (d_1006_valueOrError2_).PropagateFailure()
            return res
        d_1005_ptKey_ = (d_1006_valueOrError2_).Extract()
        d_1008_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1008_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1005_ptKey_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1008_valueOrError3_).IsFailure():
            res = (d_1008_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1005_ptKey_, AesUnwrapInfo_AesUnwrapInfo()))
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
