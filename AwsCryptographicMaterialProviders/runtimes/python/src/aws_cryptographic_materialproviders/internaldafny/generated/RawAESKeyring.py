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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring

# Module: RawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_1359_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return AwsCryptographyPrimitivesTypes.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_1359_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_1359_encryptedKeyLength_::]))

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
        out238_: Wrappers.Result
        out238_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out238_

    def OnEncrypt(self, input):
        out239_: Wrappers.Result
        out239_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out239_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1360_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1360_materials_ = (input).materials
        d_1361_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1361_suite_ = (d_1360_materials_).algorithmSuite
        d_1362_wrap_: AesWrapKeyMaterial
        nw56_ = AesWrapKeyMaterial()
        nw56_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_1362_wrap_ = nw56_
        d_1363_generateAndWrap_: AesGenerateAndWrapKeyMaterial
        nw57_ = AesGenerateAndWrapKeyMaterial()
        nw57_.ctor__(d_1362_wrap_)
        d_1363_generateAndWrap_ = nw57_
        d_1364_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1365_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AesWrapInfo.default()))()
        out240_: Wrappers.Result
        out240_ = EdkWrapping.default__.WrapEdkMaterial(d_1360_materials_, d_1362_wrap_, d_1363_generateAndWrap_)
        d_1365_valueOrError0_ = out240_
        if (d_1365_valueOrError0_).IsFailure():
            output = (d_1365_valueOrError0_).PropagateFailure()
            return output
        d_1364_wrapOutput_ = (d_1365_valueOrError0_).Extract()
        d_1366_symmetricSigningKeyList_: Wrappers.Option
        d_1366_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1364_wrapOutput_).symmetricSigningKey).value])) if ((d_1364_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1367_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1367_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_1364_wrapOutput_).wrapInfo).iv), (d_1364_wrapOutput_).wrappedMaterial)
        if (d_1364_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1368_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1369_valueOrError1_: Wrappers.Result = None
            d_1369_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_1360_materials_, (d_1364_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1367_edk_]), d_1366_symmetricSigningKeyList_)
            if (d_1369_valueOrError1_).IsFailure():
                output = (d_1369_valueOrError1_).PropagateFailure()
                return output
            d_1368_result_ = (d_1369_valueOrError1_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1368_result_))
            return output
        elif (d_1364_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1370_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1371_valueOrError2_: Wrappers.Result = None
            d_1371_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1360_materials_, _dafny.Seq([d_1367_edk_]), d_1366_symmetricSigningKeyList_)
            if (d_1371_valueOrError2_).IsFailure():
                output = (d_1371_valueOrError2_).PropagateFailure()
                return output
            d_1370_result_ = (d_1371_valueOrError2_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1370_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1372_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1372_materials_ = (input).materials
        d_1373_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1373_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1372_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1373_valueOrError0_).IsFailure():
            output = (d_1373_valueOrError0_).PropagateFailure()
            return output
        d_1374_aad_: _dafny.Seq
        d_1375_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1375_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1375_valueOrError1_).IsFailure():
            output = (d_1375_valueOrError1_).PropagateFailure()
            return output
        d_1374_aad_ = (d_1375_valueOrError1_).Extract()
        d_1376_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1376_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_1376_valueOrError2_).IsFailure():
            output = (d_1376_valueOrError2_).PropagateFailure()
            return output
        d_1377_errors_: _dafny.Seq
        d_1377_errors_ = _dafny.Seq([])
        hi9_ = len((input).encryptedDataKeys)
        for d_1378_i_ in range(0, hi9_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1378_i_]):
                d_1379_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
                d_1379_edk_ = ((input).encryptedDataKeys)[d_1378_i_]
                d_1380_iv_: _dafny.Seq
                d_1380_iv_ = (self).GetIvFromProvInfo((d_1379_edk_).keyProviderInfo)
                d_1381_unwrap_: AesUnwrapKeyMaterial
                nw58_ = AesUnwrapKeyMaterial()
                nw58_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_1380_iv_, (self).cryptoPrimitives)
                d_1381_unwrap_ = nw58_
                d_1382_unwrapOutput_: Wrappers.Result
                out241_: Wrappers.Result
                out241_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1379_edk_).ciphertext, d_1372_materials_, d_1381_unwrap_)
                d_1382_unwrapOutput_ = out241_
                if (d_1382_unwrapOutput_).is_Success:
                    d_1383_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                    d_1384_valueOrError3_: Wrappers.Result = None
                    d_1384_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1372_materials_, ((d_1382_unwrapOutput_).value).plaintextDataKey, ((d_1382_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1384_valueOrError3_).IsFailure():
                        output = (d_1384_valueOrError3_).PropagateFailure()
                        return output
                    d_1383_result_ = (d_1384_valueOrError3_).Extract()
                    d_1385_value_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
                    d_1385_value_ = AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1383_result_)
                    output = Wrappers.Result_Success(d_1385_value_)
                    return output
                elif True:
                    d_1377_errors_ = (d_1377_errors_) + (_dafny.Seq([(d_1382_unwrapOutput_).error]))
            elif True:
                d_1386_extractedKeyProviderId_: _dafny.Seq
                d_1387_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                def lambda104_(d_1388_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_1388_e_)

                d_1387_valueOrError4_ = (UTF8.default__.Decode((((input).encryptedDataKeys)[d_1378_i_]).keyProviderId)).MapFailure(lambda104_)
                if (d_1387_valueOrError4_).IsFailure():
                    output = (d_1387_valueOrError4_).PropagateFailure()
                    return output
                d_1386_extractedKeyProviderId_ = (d_1387_valueOrError4_).Extract()
                d_1377_errors_ = (d_1377_errors_) + (_dafny.Seq([AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(ErrorMessages.default__.IncorrectRawDataKeys(StandardLibrary_String.default__.Base10Int2String(d_1378_i_), _dafny.Seq("AESKeyring"), d_1386_extractedKeyProviderId_))]))
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1377_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
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
        d_1389_generateBytesResult_: Wrappers.Result
        out242_: Wrappers.Result
        out242_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1389_generateBytesResult_ = out242_
        d_1390_plaintextMaterial_: _dafny.Seq
        d_1391_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda105_(d_1392_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1392_e_)

        d_1391_valueOrError0_ = (d_1389_generateBytesResult_).MapFailure(lambda105_)
        if (d_1391_valueOrError0_).IsFailure():
            res = (d_1391_valueOrError0_).PropagateFailure()
            return res
        d_1390_plaintextMaterial_ = (d_1391_valueOrError0_).Extract()
        d_1393_wrapOutput_: MaterialWrapping.WrapOutput
        d_1394_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        out243_: Wrappers.Result
        out243_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1390_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1394_valueOrError1_ = out243_
        if (d_1394_valueOrError1_).IsFailure():
            res = (d_1394_valueOrError1_).PropagateFailure()
            return res
        d_1393_wrapOutput_ = (d_1394_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1390_plaintextMaterial_, (d_1393_wrapOutput_).wrappedMaterial, (d_1393_wrapOutput_).wrapInfo))
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
        d_1395_aad_: _dafny.Seq
        d_1396_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1396_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1396_valueOrError0_).IsFailure():
            res = (d_1396_valueOrError0_).PropagateFailure()
            return res
        d_1395_aad_ = (d_1396_valueOrError0_).Extract()
        d_1397_randomIvResult_: Wrappers.Result
        out244_: Wrappers.Result
        out244_ = ((self).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_1397_randomIvResult_ = out244_
        d_1398_iv_: _dafny.Seq
        d_1399_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda106_(d_1400_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1400_e_)

        d_1399_valueOrError1_ = (d_1397_randomIvResult_).MapFailure(lambda106_)
        if (d_1399_valueOrError1_).IsFailure():
            res = (d_1399_valueOrError1_).PropagateFailure()
            return res
        d_1398_iv_ = (d_1399_valueOrError1_).Extract()
        d_1401_aesEncryptResult_: Wrappers.Result
        out245_: Wrappers.Result
        out245_ = ((self).cryptoPrimitives).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_1398_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1395_aad_))
        d_1401_aesEncryptResult_ = out245_
        d_1402_wrappedMaterialResult_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1403_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda107_(d_1404_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1404_e_)

        d_1403_valueOrError2_ = (d_1401_aesEncryptResult_).MapFailure(lambda107_)
        if (d_1403_valueOrError2_).IsFailure():
            res = (d_1403_valueOrError2_).PropagateFailure()
            return res
        d_1402_wrappedMaterialResult_ = (d_1403_valueOrError2_).Extract()
        d_1405_wrappedMaterial_: _dafny.Seq
        d_1405_wrappedMaterial_ = default__.SerializeEDKCiphertext(d_1402_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_1405_wrappedMaterial_, AesWrapInfo_AesWrapInfo(d_1398_iv_)))
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
        d_1406_aad_: _dafny.Seq
        d_1407_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1407_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1407_valueOrError0_).IsFailure():
            res = (d_1407_valueOrError0_).PropagateFailure()
            return res
        d_1406_aad_ = (d_1407_valueOrError0_).Extract()
        d_1408_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1408_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1408_valueOrError1_).IsFailure():
            res = (d_1408_valueOrError1_).PropagateFailure()
            return res
        d_1409_encryptionOutput_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1409_encryptionOutput_ = default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1410_maybePtKey_: Wrappers.Result
        out246_: Wrappers.Result
        out246_ = ((self).cryptoPrimitives).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1409_encryptionOutput_).cipherText, (d_1409_encryptionOutput_).authTag, (self).iv, d_1406_aad_))
        d_1410_maybePtKey_ = out246_
        d_1411_ptKey_: _dafny.Seq
        d_1412_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda108_(d_1413_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1413_e_)

        d_1412_valueOrError2_ = (d_1410_maybePtKey_).MapFailure(lambda108_)
        if (d_1412_valueOrError2_).IsFailure():
            res = (d_1412_valueOrError2_).PropagateFailure()
            return res
        d_1411_ptKey_ = (d_1412_valueOrError2_).Extract()
        d_1414_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1414_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1411_ptKey_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1414_valueOrError3_).IsFailure():
            res = (d_1414_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1411_ptKey_, AesUnwrapInfo_AesUnwrapInfo()))
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
