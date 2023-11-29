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
import RawAESKeyring

assert "RawRSAKeyring" == __name__
RawRSAKeyring = sys.modules[__name__]


class RawRSAKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._paddingScheme: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1.default()()
        self._publicKey: Wrappers.Option = Wrappers.Option_None.default()()
        self._privateKey: Wrappers.Option = Wrappers.Option_None.default()()
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RawRSAKeyring"
    def OnEncrypt(self, input):
        out209_: Wrappers.Result
        out209_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out209_

    def OnDecrypt(self, input):
        out210_: Wrappers.Result
        out210_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out210_

    def ctor__(self, namespace, name, publicKey, privateKey, paddingScheme, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._paddingScheme = paddingScheme
        (self)._publicKey = publicKey
        (self)._privateKey = privateKey
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1009_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1009_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A RawRSAKeyring without a public key cannot provide OnEncrypt")))
        if (d_1009_valueOrError0_).IsFailure():
            output = (d_1009_valueOrError0_).PropagateFailure()
            return output
        d_1010_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1010_materials_ = (input).materials
        d_1011_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1011_suite_ = (d_1010_materials_).algorithmSuite
        d_1012_wrap_: RawRSAKeyring.RsaWrapKeyMaterial
        nw48_ = RawRSAKeyring.RsaWrapKeyMaterial()
        nw48_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1012_wrap_ = nw48_
        d_1013_generateAndWrap_: RawRSAKeyring.RsaGenerateAndWrapKeyMaterial
        nw49_ = RawRSAKeyring.RsaGenerateAndWrapKeyMaterial()
        nw49_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1013_generateAndWrap_ = nw49_
        d_1014_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1015_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(RawRSAKeyring.RsaWrapInfo.default()))()
        out211_: Wrappers.Result
        out211_ = EdkWrapping.default__.WrapEdkMaterial(d_1010_materials_, d_1012_wrap_, d_1013_generateAndWrap_)
        d_1015_valueOrError1_ = out211_
        if (d_1015_valueOrError1_).IsFailure():
            output = (d_1015_valueOrError1_).PropagateFailure()
            return output
        d_1014_wrapOutput_ = (d_1015_valueOrError1_).Extract()
        d_1016_symmetricSigningKeyList_: Wrappers.Option
        d_1016_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1014_wrapOutput_).symmetricSigningKey).value])) if ((d_1014_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1017_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1017_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).keyName, (d_1014_wrapOutput_).wrappedMaterial)
        if (d_1014_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1018_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1019_valueOrError2_: Wrappers.Result = None
            d_1019_valueOrError2_ = Materials.default__.EncryptionMaterialAddDataKey(d_1010_materials_, (d_1014_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1017_edk_]), d_1016_symmetricSigningKeyList_)
            if (d_1019_valueOrError2_).IsFailure():
                output = (d_1019_valueOrError2_).PropagateFailure()
                return output
            d_1018_result_ = (d_1019_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1018_result_))
            return output
        elif (d_1014_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1020_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1021_valueOrError3_: Wrappers.Result = None
            d_1021_valueOrError3_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1010_materials_, _dafny.Seq([d_1017_edk_]), d_1016_symmetricSigningKeyList_)
            if (d_1021_valueOrError3_).IsFailure():
                output = (d_1021_valueOrError3_).PropagateFailure()
                return output
            d_1020_result_ = (d_1021_valueOrError3_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1020_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1022_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1022_valueOrError0_ = Wrappers.default__.Need((((self).privateKey).is_Some) and ((len(((self).privateKey).Extract())) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A RawRSAKeyring without a private key cannot provide OnEncrypt")))
        if (d_1022_valueOrError0_).IsFailure():
            output = (d_1022_valueOrError0_).PropagateFailure()
            return output
        d_1023_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1023_materials_ = (input).materials
        d_1024_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1024_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1023_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1024_valueOrError1_).IsFailure():
            output = (d_1024_valueOrError1_).PropagateFailure()
            return output
        d_1025_errors_: _dafny.Seq
        d_1025_errors_ = _dafny.Seq([])
        hi10_: int = len((input).encryptedDataKeys)
        for d_1026_i_ in range(0, hi10_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1026_i_]):
                d_1027_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
                d_1027_edk_ = ((input).encryptedDataKeys)[d_1026_i_]
                d_1028_unwrap_: RawRSAKeyring.RsaUnwrapKeyMaterial
                nw50_ = RawRSAKeyring.RsaUnwrapKeyMaterial()
                nw50_.ctor__(((self).privateKey).Extract(), (self).paddingScheme, (self).cryptoPrimitives)
                d_1028_unwrap_ = nw50_
                d_1029_unwrapOutput_: Wrappers.Result
                out212_: Wrappers.Result
                out212_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1027_edk_).ciphertext, d_1023_materials_, d_1028_unwrap_)
                d_1029_unwrapOutput_ = out212_
                if (d_1029_unwrapOutput_).is_Success:
                    d_1030_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                    d_1031_valueOrError2_: Wrappers.Result = None
                    d_1031_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1023_materials_, ((d_1029_unwrapOutput_).value).plaintextDataKey, ((d_1029_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1031_valueOrError2_).IsFailure():
                        output = (d_1031_valueOrError2_).PropagateFailure()
                        return output
                    d_1030_returnMaterials_ = (d_1031_valueOrError2_).Extract()
                    output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1030_returnMaterials_))
                    return output
                elif True:
                    d_1025_errors_ = (d_1025_errors_) + (_dafny.Seq([(d_1029_unwrapOutput_).error]))
            elif True:
                d_1025_errors_ = (d_1025_errors_) + (_dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncryptedDataKey ")) + (String.default__.Base10Int2String(d_1026_i_))) + (_dafny.Seq(" did not match RSAKeyring. ")))]))
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1025_errors_, _dafny.Seq("Raw RSA Key was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
        return output
        return output

    def ShouldDecryptEDK(self, edk):
        return (((UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)) and (((edk).keyProviderInfo) == ((self).keyName))) and (((edk).keyProviderId) == ((self).keyNamespace))) and ((len((edk).ciphertext)) > (0))

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def keyNamespace(self):
        return self._keyNamespace
    @property
    def keyName(self):
        return self._keyName
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def publicKey(self):
        return self._publicKey
    @property
    def privateKey(self):
        return self._privateKey

class RsaUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [RsaUnwrapInfo_RsaUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: RsaUnwrapInfo_RsaUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RsaUnwrapInfo(self) -> bool:
        return isinstance(self, RawRSAKeyring.RsaUnwrapInfo_RsaUnwrapInfo)

class RsaUnwrapInfo_RsaUnwrapInfo(RsaUnwrapInfo, NamedTuple('RsaUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawRSAKeyring.RsaUnwrapInfo.RsaUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawRSAKeyring.RsaUnwrapInfo_RsaUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class RsaWrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [RsaWrapInfo_RsaWrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: RsaWrapInfo_RsaWrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RsaWrapInfo(self) -> bool:
        return isinstance(self, RawRSAKeyring.RsaWrapInfo_RsaWrapInfo)

class RsaWrapInfo_RsaWrapInfo(RsaWrapInfo, NamedTuple('RsaWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawRSAKeyring.RsaWrapInfo.RsaWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RawRSAKeyring.RsaWrapInfo_RsaWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class RsaGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._paddingScheme: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1.default()()
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._paddingScheme = paddingScheme
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(RawRSAKeyring.RsaWrapInfo.default()))()
        d_1032_generateBytesResult_: Wrappers.Result
        out213_: Wrappers.Result
        out213_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1032_generateBytesResult_ = out213_
        d_1033_plaintextMaterial_: _dafny.Seq
        d_1034_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda66_(d_1035_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1035_e_)

        d_1034_valueOrError0_ = (d_1032_generateBytesResult_).MapFailure(lambda66_)
        if (d_1034_valueOrError0_).IsFailure():
            res = (d_1034_valueOrError0_).PropagateFailure()
            return res
        d_1033_plaintextMaterial_ = (d_1034_valueOrError0_).Extract()
        d_1036_wrap_: RawRSAKeyring.RsaWrapKeyMaterial
        nw51_ = RawRSAKeyring.RsaWrapKeyMaterial()
        nw51_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_1036_wrap_ = nw51_
        d_1037_wrapOutput_: MaterialWrapping.WrapOutput
        d_1038_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(RawRSAKeyring.RsaWrapInfo.default()))()
        out214_: Wrappers.Result
        out214_ = (d_1036_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1033_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1038_valueOrError1_ = out214_
        if (d_1038_valueOrError1_).IsFailure():
            res = (d_1038_valueOrError1_).PropagateFailure()
            return res
        d_1037_wrapOutput_ = (d_1038_valueOrError1_).Extract()
        d_1039_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1039_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1033_plaintextMaterial_, (d_1037_wrapOutput_).wrappedMaterial, RawRSAKeyring.RsaWrapInfo_RsaWrapInfo())
        res = Wrappers.Result_Success(d_1039_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives

class RsaWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._paddingScheme: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1.default()()
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._paddingScheme = paddingScheme
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(RawRSAKeyring.RsaWrapInfo.default()))()
        d_1040_RSAEncryptOutput_: Wrappers.Result
        out215_: Wrappers.Result
        out215_ = ((self).cryptoPrimitives).RSAEncrypt(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput((self).paddingScheme, (self).publicKey, (input).plaintextMaterial))
        d_1040_RSAEncryptOutput_ = out215_
        d_1041_ciphertext_: _dafny.Seq
        d_1042_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda67_(d_1043_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1043_e_)

        d_1042_valueOrError0_ = (d_1040_RSAEncryptOutput_).MapFailure(lambda67_)
        if (d_1042_valueOrError0_).IsFailure():
            res = (d_1042_valueOrError0_).PropagateFailure()
            return res
        d_1041_ciphertext_ = (d_1042_valueOrError0_).Extract()
        d_1044_output_: MaterialWrapping.WrapOutput
        d_1044_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_1041_ciphertext_, RawRSAKeyring.RsaWrapInfo_RsaWrapInfo())
        res = Wrappers.Result_Success(d_1044_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives

class RsaUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._privateKey: _dafny.Seq = _dafny.Seq({})
        self._paddingScheme: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode = software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_PKCS1.default()()
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaUnwrapKeyMaterial"
    def ctor__(self, privateKey, paddingScheme, cryptoPrimitives):
        (self)._privateKey = privateKey
        (self)._paddingScheme = paddingScheme
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(RawRSAKeyring.RsaUnwrapInfo.default()))()
        d_1045_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1045_suite_ = (input).algorithmSuite
        d_1046_wrappedMaterial_: _dafny.Seq
        d_1046_wrappedMaterial_ = (input).wrappedMaterial
        d_1047_aad_: _dafny.Map
        d_1047_aad_ = (input).encryptionContext
        d_1048_maybeDecryptResult_: Wrappers.Result
        out216_: Wrappers.Result
        out216_ = ((self).cryptoPrimitives).RSADecrypt(software_amazon_cryptography_primitives_internaldafny_types.RSADecryptInput_RSADecryptInput((self).paddingScheme, (self).privateKey, d_1046_wrappedMaterial_))
        d_1048_maybeDecryptResult_ = out216_
        d_1049_decryptResult_: _dafny.Seq
        d_1050_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda68_(d_1051_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1051_e_)

        d_1050_valueOrError0_ = (d_1048_maybeDecryptResult_).MapFailure(lambda68_)
        if (d_1050_valueOrError0_).IsFailure():
            res = (d_1050_valueOrError0_).PropagateFailure()
            return res
        d_1049_decryptResult_ = (d_1050_valueOrError0_).Extract()
        d_1052_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1052_valueOrError1_ = Wrappers.default__.Need((len(d_1049_decryptResult_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(d_1045_suite_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid plaintext length.")))
        if (d_1052_valueOrError1_).IsFailure():
            res = (d_1052_valueOrError1_).PropagateFailure()
            return res
        d_1053_output_: MaterialWrapping.UnwrapOutput
        d_1053_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1049_decryptResult_, RawRSAKeyring.RsaUnwrapInfo_RsaUnwrapInfo())
        res = Wrappers.Result_Success(d_1053_output_)
        return res
        return res

    @property
    def privateKey(self):
        return self._privateKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
