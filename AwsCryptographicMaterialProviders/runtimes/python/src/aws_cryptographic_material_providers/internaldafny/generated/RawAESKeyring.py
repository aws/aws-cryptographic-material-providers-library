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
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
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

# Module: RawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_0_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return AwsCryptographyPrimitivesTypes.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_0_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_0_encryptedKeyLength_::]))

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @_dafny.classproperty
    def AUTH__TAG__LEN__LEN(instance):
        return 4
    @_dafny.classproperty
    def IV__LEN__LEN(instance):
        return 4

class RawAESKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: AwsCryptographyPrimitivesTypes.AES__GCM = None
        self._keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.RawAESKeyring"
    def OnDecrypt(self, input):
        out10_: Wrappers.Result
        out10_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out10_

    def OnEncrypt(self, input):
        out10_: Wrappers.Result
        out10_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out10_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = (d_0_materials_).algorithmSuite
        d_2_wrap_: AesWrapKeyMaterial
        nw0_ = AesWrapKeyMaterial()
        nw0_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_2_wrap_ = nw0_
        d_3_generateAndWrap_: AesGenerateAndWrapKeyMaterial
        nw1_ = AesGenerateAndWrapKeyMaterial()
        nw1_.ctor__(d_2_wrap_)
        d_3_generateAndWrap_ = nw1_
        d_4_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AesWrapInfo.default()))()
        out0_: Wrappers.Result
        out0_ = EdkWrapping.default__.WrapEdkMaterial(d_0_materials_, d_2_wrap_, d_3_generateAndWrap_)
        d_4_valueOrError0_ = out0_
        if (d_4_valueOrError0_).IsFailure():
            output = (d_4_valueOrError0_).PropagateFailure()
            return output
        d_5_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_5_wrapOutput_ = (d_4_valueOrError0_).Extract()
        d_6_symmetricSigningKeyList_: Wrappers.Option
        if ((d_5_wrapOutput_).symmetricSigningKey).is_Some:
            d_6_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_5_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_6_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_7_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_7_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_5_wrapOutput_).wrapInfo).iv), (d_5_wrapOutput_).wrappedMaterial)
        if (d_5_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_8_valueOrError1_: Wrappers.Result = None
            d_8_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_0_materials_, (d_5_wrapOutput_).plaintextDataKey, _dafny.Seq([d_7_edk_]), d_6_symmetricSigningKeyList_)
            if (d_8_valueOrError1_).IsFailure():
                output = (d_8_valueOrError1_).PropagateFailure()
                return output
            d_9_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_9_result_ = (d_8_valueOrError1_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_9_result_))
            return output
        elif (d_5_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_10_valueOrError2_: Wrappers.Result = None
            d_10_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_0_materials_, _dafny.Seq([d_7_edk_]), d_6_symmetricSigningKeyList_)
            if (d_10_valueOrError2_).IsFailure():
                output = (d_10_valueOrError2_).PropagateFailure()
                return output
            d_11_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_11_result_ = (d_10_valueOrError2_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_11_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_0_materials_ = (input).materials
        d_1_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_0_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1_valueOrError0_).IsFailure():
            output = (d_1_valueOrError0_).PropagateFailure()
            return output
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_2_valueOrError1_).IsFailure():
            output = (d_2_valueOrError1_).PropagateFailure()
            return output
        d_3_aad_: _dafny.Seq
        d_3_aad_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_errors_: _dafny.Seq
        d_5_errors_ = _dafny.Seq([])
        hi0_ = len((input).encryptedDataKeys)
        for d_6_i_ in range(0, hi0_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_6_i_]):
                d_7_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
                d_7_edk_ = ((input).encryptedDataKeys)[d_6_i_]
                d_8_iv_: _dafny.Seq
                d_8_iv_ = (self).GetIvFromProvInfo((d_7_edk_).keyProviderInfo)
                d_9_unwrap_: AesUnwrapKeyMaterial
                nw0_ = AesUnwrapKeyMaterial()
                nw0_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_8_iv_, (self).cryptoPrimitives)
                d_9_unwrap_ = nw0_
                d_10_unwrapOutput_: Wrappers.Result
                out0_: Wrappers.Result
                out0_ = EdkWrapping.default__.UnwrapEdkMaterial((d_7_edk_).ciphertext, d_0_materials_, d_9_unwrap_)
                d_10_unwrapOutput_ = out0_
                if (d_10_unwrapOutput_).is_Success:
                    d_11_valueOrError3_: Wrappers.Result = None
                    d_11_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_0_materials_, ((d_10_unwrapOutput_).value).plaintextDataKey, ((d_10_unwrapOutput_).value).symmetricSigningKey)
                    if (d_11_valueOrError3_).IsFailure():
                        output = (d_11_valueOrError3_).PropagateFailure()
                        return output
                    d_12_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                    d_12_result_ = (d_11_valueOrError3_).Extract()
                    d_13_value_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
                    d_13_value_ = AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_12_result_)
                    output = Wrappers.Result_Success(d_13_value_)
                    return output
                elif True:
                    d_5_errors_ = (d_5_errors_) + (_dafny.Seq([(d_10_unwrapOutput_).error]))
            elif True:
                d_14_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                def lambda0_(d_15_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_15_e_)

                d_14_valueOrError4_ = (UTF8.default__.Decode((((input).encryptedDataKeys)[d_6_i_]).keyProviderId)).MapFailure(lambda0_)
                if (d_14_valueOrError4_).IsFailure():
                    output = (d_14_valueOrError4_).PropagateFailure()
                    return output
                d_16_extractedKeyProviderId_: _dafny.Seq
                d_16_extractedKeyProviderId_ = (d_14_valueOrError4_).Extract()
                d_5_errors_ = (d_5_errors_) + (_dafny.Seq([AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(ErrorMessages.default__.IncorrectRawDataKeys(StandardLibrary_String.default__.Base10Int2String(d_6_i_), _dafny.Seq("AESKeyring"), d_16_extractedKeyProviderId_))]))
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_5_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
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
        d_0_generateBytesResult_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_0_generateBytesResult_ = out0_
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_generateBytesResult_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_plaintextMaterial_: _dafny.Seq
        d_3_plaintextMaterial_ = (d_1_valueOrError0_).Extract()
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        out1_: Wrappers.Result
        out1_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_3_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_4_valueOrError1_ = out1_
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_5_wrapOutput_: MaterialWrapping.WrapOutput
        d_5_wrapOutput_ = (d_4_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_3_plaintextMaterial_, (d_5_wrapOutput_).wrappedMaterial, (d_5_wrapOutput_).wrapInfo))
        return res

    @property
    def wrap(self):
        return self._wrap

class AesWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: AwsCryptographyPrimitivesTypes.AES__GCM = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesWrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_aad_: _dafny.Seq
        d_1_aad_ = (d_0_valueOrError0_).Extract()
        d_2_randomIvResult_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_2_randomIvResult_ = out0_
        d_3_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_4_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_4_e_)

        d_3_valueOrError1_ = (d_2_randomIvResult_).MapFailure(lambda0_)
        if (d_3_valueOrError1_).IsFailure():
            res = (d_3_valueOrError1_).PropagateFailure()
            return res
        d_5_iv_: _dafny.Seq
        d_5_iv_ = (d_3_valueOrError1_).Extract()
        d_6_aesEncryptResult_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = ((self).cryptoPrimitives).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_5_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1_aad_))
        d_6_aesEncryptResult_ = out1_
        d_7_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda1_(d_8_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_8_e_)

        d_7_valueOrError2_ = (d_6_aesEncryptResult_).MapFailure(lambda1_)
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        d_9_wrappedMaterialResult_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_9_wrappedMaterialResult_ = (d_7_valueOrError2_).Extract()
        d_10_wrappedMaterial_: _dafny.Seq
        d_10_wrappedMaterial_ = default__.SerializeEDKCiphertext(d_9_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_10_wrappedMaterial_, AesWrapInfo_AesWrapInfo(d_5_iv_)))
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
        self._wrappingAlgorithm: AwsCryptographyPrimitivesTypes.AES__GCM = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
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
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_aad_: _dafny.Seq
        d_1_aad_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_2_valueOrError1_).IsFailure():
            res = (d_2_valueOrError1_).PropagateFailure()
            return res
        d_3_encryptionOutput_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_3_encryptionOutput_ = default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_4_maybePtKey_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).cryptoPrimitives).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_3_encryptionOutput_).cipherText, (d_3_encryptionOutput_).authTag, (self).iv, d_1_aad_))
        d_4_maybePtKey_ = out0_
        d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_6_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_6_e_)

        d_5_valueOrError2_ = (d_4_maybePtKey_).MapFailure(lambda0_)
        if (d_5_valueOrError2_).IsFailure():
            res = (d_5_valueOrError2_).PropagateFailure()
            return res
        d_7_ptKey_: _dafny.Seq
        d_7_ptKey_ = (d_5_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_8_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_7_ptKey_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_8_valueOrError3_).IsFailure():
            res = (d_8_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_7_ptKey_, AesUnwrapInfo_AesUnwrapInfo()))
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
