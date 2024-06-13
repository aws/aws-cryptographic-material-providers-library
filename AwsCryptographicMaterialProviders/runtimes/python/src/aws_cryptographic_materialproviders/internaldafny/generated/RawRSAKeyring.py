import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring

# Module: RawRSAKeyring


class RawRSAKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._i_keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._i_keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._i_paddingScheme: AwsCryptographyPrimitivesTypes.RSAPaddingMode = AwsCryptographyPrimitivesTypes.RSAPaddingMode.default()()
        self._i_publicKey: Wrappers.Option = Wrappers.Option.default()()
        self._i_privateKey: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RawRSAKeyring"
    def OnDecrypt(self, input):
        out204_: Wrappers.Result
        out204_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out204_

    def OnEncrypt(self, input):
        out205_: Wrappers.Result
        out205_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out205_

    def ctor__(self, namespace, name, publicKey, privateKey, paddingScheme, cryptoPrimitives):
        (self)._i_keyNamespace = namespace
        (self)._i_keyName = name
        (self)._i_paddingScheme = paddingScheme
        (self)._i_publicKey = publicKey
        (self)._i_privateKey = privateKey
        (self)._i_cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1145_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1145_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A RawRSAKeyring without a public key cannot provide OnEncrypt")))
        if (d_1145_valueOrError0_).IsFailure():
            output = (d_1145_valueOrError0_).PropagateFailure()
            return output
        d_1146_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1146_materials_ = (input).materials
        d_1147_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1147_suite_ = (d_1146_materials_).algorithmSuite
        d_1148_wrap_: RsaWrapKeyMaterial
        nw48_ = RsaWrapKeyMaterial()
        nw48_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1148_wrap_ = nw48_
        d_1149_generateAndWrap_: RsaGenerateAndWrapKeyMaterial
        nw49_ = RsaGenerateAndWrapKeyMaterial()
        nw49_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1149_generateAndWrap_ = nw49_
        d_1150_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1151_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(RsaWrapInfo.default()))()
        out206_: Wrappers.Result
        out206_ = EdkWrapping.default__.WrapEdkMaterial(d_1146_materials_, d_1148_wrap_, d_1149_generateAndWrap_)
        d_1151_valueOrError1_ = out206_
        if (d_1151_valueOrError1_).IsFailure():
            output = (d_1151_valueOrError1_).PropagateFailure()
            return output
        d_1150_wrapOutput_ = (d_1151_valueOrError1_).Extract()
        d_1152_symmetricSigningKeyList_: Wrappers.Option
        d_1152_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1150_wrapOutput_).symmetricSigningKey).value])) if ((d_1150_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1153_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1153_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).keyName, (d_1150_wrapOutput_).wrappedMaterial)
        if (d_1150_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1154_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1155_valueOrError2_: Wrappers.Result = None
            d_1155_valueOrError2_ = Materials.default__.EncryptionMaterialAddDataKey(d_1146_materials_, (d_1150_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1153_edk_]), d_1152_symmetricSigningKeyList_)
            if (d_1155_valueOrError2_).IsFailure():
                output = (d_1155_valueOrError2_).PropagateFailure()
                return output
            d_1154_result_ = (d_1155_valueOrError2_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1154_result_))
            return output
        elif (d_1150_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1156_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1157_valueOrError3_: Wrappers.Result = None
            d_1157_valueOrError3_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1146_materials_, _dafny.Seq([d_1153_edk_]), d_1152_symmetricSigningKeyList_)
            if (d_1157_valueOrError3_).IsFailure():
                output = (d_1157_valueOrError3_).PropagateFailure()
                return output
            d_1156_result_ = (d_1157_valueOrError3_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1156_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1158_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1158_valueOrError0_ = Wrappers.default__.Need((((self).privateKey).is_Some) and ((len(((self).privateKey).Extract())) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A RawRSAKeyring without a private key cannot provide OnEncrypt")))
        if (d_1158_valueOrError0_).IsFailure():
            output = (d_1158_valueOrError0_).PropagateFailure()
            return output
        d_1159_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1159_materials_ = (input).materials
        d_1160_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1160_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1159_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1160_valueOrError1_).IsFailure():
            output = (d_1160_valueOrError1_).PropagateFailure()
            return output
        d_1161_errors_: _dafny.Seq
        d_1161_errors_ = _dafny.Seq([])
        hi9_ = len((input).encryptedDataKeys)
        for d_1162_i_ in range(0, hi9_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1162_i_]):
                d_1163_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
                d_1163_edk_ = ((input).encryptedDataKeys)[d_1162_i_]
                d_1164_unwrap_: RsaUnwrapKeyMaterial
                nw50_ = RsaUnwrapKeyMaterial()
                nw50_.ctor__(((self).privateKey).Extract(), (self).paddingScheme, (self).cryptoPrimitives)
                d_1164_unwrap_ = nw50_
                d_1165_unwrapOutput_: Wrappers.Result
                out207_: Wrappers.Result
                out207_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1163_edk_).ciphertext, d_1159_materials_, d_1164_unwrap_)
                d_1165_unwrapOutput_ = out207_
                if (d_1165_unwrapOutput_).is_Success:
                    d_1166_returnMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                    d_1167_valueOrError2_: Wrappers.Result = None
                    d_1167_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1159_materials_, ((d_1165_unwrapOutput_).value).plaintextDataKey, ((d_1165_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1167_valueOrError2_).IsFailure():
                        output = (d_1167_valueOrError2_).PropagateFailure()
                        return output
                    d_1166_returnMaterials_ = (d_1167_valueOrError2_).Extract()
                    output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1166_returnMaterials_))
                    return output
                elif True:
                    d_1161_errors_ = (d_1161_errors_) + (_dafny.Seq([(d_1165_unwrapOutput_).error]))
            elif True:
                d_1168_extractedKeyProviderId_: _dafny.Seq
                d_1169_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                def lambda95_(d_1170_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_1170_e_)

                d_1169_valueOrError3_ = (UTF8.default__.Decode((((input).encryptedDataKeys)[d_1162_i_]).keyProviderId)).MapFailure(lambda95_)
                if (d_1169_valueOrError3_).IsFailure():
                    output = (d_1169_valueOrError3_).PropagateFailure()
                    return output
                d_1168_extractedKeyProviderId_ = (d_1169_valueOrError3_).Extract()
                d_1161_errors_ = (d_1161_errors_) + (_dafny.Seq([AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(ErrorMessages.default__.IncorrectRawDataKeys(StandardLibrary_String.default__.Base10Int2String(d_1162_i_), _dafny.Seq("RSAKeyring"), d_1168_extractedKeyProviderId_))]))
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1161_errors_, _dafny.Seq("Raw RSA Key was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
        return output
        return output

    def ShouldDecryptEDK(self, edk):
        return (((UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)) and (((edk).keyProviderInfo) == ((self).keyName))) and (((edk).keyProviderId) == ((self).keyNamespace))) and ((len((edk).ciphertext)) > (0))

    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
    @property
    def keyNamespace(self):
        return self._i_keyNamespace
    @property
    def keyName(self):
        return self._i_keyName
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def privateKey(self):
        return self._i_privateKey

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
        return isinstance(self, RsaUnwrapInfo_RsaUnwrapInfo)

class RsaUnwrapInfo_RsaUnwrapInfo(RsaUnwrapInfo, NamedTuple('RsaUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawRSAKeyring.RsaUnwrapInfo.RsaUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RsaUnwrapInfo_RsaUnwrapInfo)
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
        return isinstance(self, RsaWrapInfo_RsaWrapInfo)

class RsaWrapInfo_RsaWrapInfo(RsaWrapInfo, NamedTuple('RsaWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawRSAKeyring.RsaWrapInfo.RsaWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RsaWrapInfo_RsaWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class RsaGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_publicKey: _dafny.Seq = _dafny.Seq({})
        self._i_paddingScheme: AwsCryptographyPrimitivesTypes.RSAPaddingMode = AwsCryptographyPrimitivesTypes.RSAPaddingMode.default()()
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._i_publicKey = publicKey
        (self)._i_paddingScheme = paddingScheme
        (self)._i_cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(RsaWrapInfo.default()))()
        d_1171_generateBytesResult_: Wrappers.Result
        out208_: Wrappers.Result
        out208_ = ((self).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1171_generateBytesResult_ = out208_
        d_1172_plaintextMaterial_: _dafny.Seq
        d_1173_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda96_(d_1174_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1174_e_)

        d_1173_valueOrError0_ = (d_1171_generateBytesResult_).MapFailure(lambda96_)
        if (d_1173_valueOrError0_).IsFailure():
            res = (d_1173_valueOrError0_).PropagateFailure()
            return res
        d_1172_plaintextMaterial_ = (d_1173_valueOrError0_).Extract()
        d_1175_wrap_: RsaWrapKeyMaterial
        nw51_ = RsaWrapKeyMaterial()
        nw51_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_1175_wrap_ = nw51_
        d_1176_wrapOutput_: MaterialWrapping.WrapOutput
        d_1177_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(RsaWrapInfo.default()))()
        out209_: Wrappers.Result
        out209_ = (d_1175_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1172_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1177_valueOrError1_ = out209_
        if (d_1177_valueOrError1_).IsFailure():
            res = (d_1177_valueOrError1_).PropagateFailure()
            return res
        d_1176_wrapOutput_ = (d_1177_valueOrError1_).Extract()
        d_1178_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1178_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1172_plaintextMaterial_, (d_1176_wrapOutput_).wrappedMaterial, RsaWrapInfo_RsaWrapInfo())
        res = Wrappers.Result_Success(d_1178_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives

class RsaWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_publicKey: _dafny.Seq = _dafny.Seq({})
        self._i_paddingScheme: AwsCryptographyPrimitivesTypes.RSAPaddingMode = AwsCryptographyPrimitivesTypes.RSAPaddingMode.default()()
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._i_publicKey = publicKey
        (self)._i_paddingScheme = paddingScheme
        (self)._i_cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(RsaWrapInfo.default()))()
        d_1179_RSAEncryptOutput_: Wrappers.Result
        out210_: Wrappers.Result
        out210_ = ((self).cryptoPrimitives).RSAEncrypt(AwsCryptographyPrimitivesTypes.RSAEncryptInput_RSAEncryptInput((self).paddingScheme, (self).publicKey, (input).plaintextMaterial))
        d_1179_RSAEncryptOutput_ = out210_
        d_1180_ciphertext_: _dafny.Seq
        d_1181_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda97_(d_1182_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1182_e_)

        d_1181_valueOrError0_ = (d_1179_RSAEncryptOutput_).MapFailure(lambda97_)
        if (d_1181_valueOrError0_).IsFailure():
            res = (d_1181_valueOrError0_).PropagateFailure()
            return res
        d_1180_ciphertext_ = (d_1181_valueOrError0_).Extract()
        d_1183_output_: MaterialWrapping.WrapOutput
        d_1183_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_1180_ciphertext_, RsaWrapInfo_RsaWrapInfo())
        res = Wrappers.Result_Success(d_1183_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives

class RsaUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_privateKey: _dafny.Seq = _dafny.Seq({})
        self._i_paddingScheme: AwsCryptographyPrimitivesTypes.RSAPaddingMode = AwsCryptographyPrimitivesTypes.RSAPaddingMode.default()()
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawRSAKeyring.RsaUnwrapKeyMaterial"
    def ctor__(self, privateKey, paddingScheme, cryptoPrimitives):
        (self)._i_privateKey = privateKey
        (self)._i_paddingScheme = paddingScheme
        (self)._i_cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(RsaUnwrapInfo.default()))()
        d_1184_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1184_suite_ = (input).algorithmSuite
        d_1185_wrappedMaterial_: _dafny.Seq
        d_1185_wrappedMaterial_ = (input).wrappedMaterial
        d_1186_aad_: _dafny.Map
        d_1186_aad_ = (input).encryptionContext
        d_1187_maybeDecryptResult_: Wrappers.Result
        out211_: Wrappers.Result
        out211_ = ((self).cryptoPrimitives).RSADecrypt(AwsCryptographyPrimitivesTypes.RSADecryptInput_RSADecryptInput((self).paddingScheme, (self).privateKey, d_1185_wrappedMaterial_))
        d_1187_maybeDecryptResult_ = out211_
        d_1188_decryptResult_: _dafny.Seq
        d_1189_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda98_(d_1190_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1190_e_)

        d_1189_valueOrError0_ = (d_1187_maybeDecryptResult_).MapFailure(lambda98_)
        if (d_1189_valueOrError0_).IsFailure():
            res = (d_1189_valueOrError0_).PropagateFailure()
            return res
        d_1188_decryptResult_ = (d_1189_valueOrError0_).Extract()
        d_1191_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1191_valueOrError1_ = Wrappers.default__.Need((len(d_1188_decryptResult_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(d_1184_suite_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid plaintext length.")))
        if (d_1191_valueOrError1_).IsFailure():
            res = (d_1191_valueOrError1_).PropagateFailure()
            return res
        d_1192_output_: MaterialWrapping.UnwrapOutput
        d_1192_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1188_decryptResult_, RsaUnwrapInfo_RsaUnwrapInfo())
        res = Wrappers.Result_Success(d_1192_output_)
        return res
        return res

    @property
    def privateKey(self):
        return self._i_privateKey
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
