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

# assert "RawAESKeyring" == __name__
RawAESKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_1342_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_1342_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_1342_encryptedKeyLength_::]))

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
        out321_: Wrappers.Result
        out321_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out321_

    def OnDecrypt(self, input):
        out322_: Wrappers.Result
        out322_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out322_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1343_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1343_materials_ = (input).materials
        d_1344_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1344_suite_ = (d_1343_materials_).algorithmSuite
        d_1345_wrap_: RawAESKeyring.AesWrapKeyMaterial
        nw46_ = RawAESKeyring.AesWrapKeyMaterial()
        nw46_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_1345_wrap_ = nw46_
        d_1346_generateAndWrap_: RawAESKeyring.AesGenerateAndWrapKeyMaterial
        nw47_ = RawAESKeyring.AesGenerateAndWrapKeyMaterial()
        nw47_.ctor__(d_1345_wrap_)
        d_1346_generateAndWrap_ = nw47_
        d_1347_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1348_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        out323_: Wrappers.Result
        out323_ = EdkWrapping.default__.WrapEdkMaterial(d_1343_materials_, d_1345_wrap_, d_1346_generateAndWrap_)
        d_1348_valueOrError0_ = out323_
        if (d_1348_valueOrError0_).IsFailure():
            output = (d_1348_valueOrError0_).PropagateFailure()
            return output
        d_1347_wrapOutput_ = (d_1348_valueOrError0_).Extract()
        d_1349_symmetricSigningKeyList_: Wrappers.Option
        d_1349_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1347_wrapOutput_).symmetricSigningKey).value])) if ((d_1347_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1350_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1350_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_1347_wrapOutput_).wrapInfo).iv), (d_1347_wrapOutput_).wrappedMaterial)
        if (d_1347_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1351_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1352_valueOrError1_: Wrappers.Result = None
            d_1352_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_1343_materials_, (d_1347_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1350_edk_]), d_1349_symmetricSigningKeyList_)
            if (d_1352_valueOrError1_).IsFailure():
                output = (d_1352_valueOrError1_).PropagateFailure()
                return output
            d_1351_result_ = (d_1352_valueOrError1_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1351_result_))
            return output
        elif (d_1347_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1353_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1354_valueOrError2_: Wrappers.Result = None
            d_1354_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1343_materials_, _dafny.Seq([d_1350_edk_]), d_1349_symmetricSigningKeyList_)
            if (d_1354_valueOrError2_).IsFailure():
                output = (d_1354_valueOrError2_).PropagateFailure()
                return output
            d_1353_result_ = (d_1354_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1353_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1355_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1355_materials_ = (input).materials
        d_1356_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1356_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1355_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1356_valueOrError0_).IsFailure():
            output = (d_1356_valueOrError0_).PropagateFailure()
            return output
        d_1357_aad_: _dafny.Seq
        d_1358_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1358_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1358_valueOrError1_).IsFailure():
            output = (d_1358_valueOrError1_).PropagateFailure()
            return output
        d_1357_aad_ = (d_1358_valueOrError1_).Extract()
        d_1359_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1359_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_1359_valueOrError2_).IsFailure():
            output = (d_1359_valueOrError2_).PropagateFailure()
            return output
        d_1360_errors_: _dafny.Seq
        d_1360_errors_ = _dafny.Seq([])
        hi9_: int = len((input).encryptedDataKeys)
        for d_1361_i_ in range(0, hi9_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1361_i_]):
                d_1362_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
                d_1362_edk_ = ((input).encryptedDataKeys)[d_1361_i_]
                d_1363_iv_: _dafny.Seq
                d_1363_iv_ = (self).GetIvFromProvInfo((d_1362_edk_).keyProviderInfo)
                d_1364_unwrap_: RawAESKeyring.AesUnwrapKeyMaterial
                nw48_ = RawAESKeyring.AesUnwrapKeyMaterial()
                nw48_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_1363_iv_, (self).cryptoPrimitives)
                d_1364_unwrap_ = nw48_
                d_1365_unwrapOutput_: Wrappers.Result
                out324_: Wrappers.Result
                out324_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1362_edk_).ciphertext, d_1355_materials_, d_1364_unwrap_)
                d_1365_unwrapOutput_ = out324_
                if (d_1365_unwrapOutput_).is_Success:
                    d_1366_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                    d_1367_valueOrError3_: Wrappers.Result = None
                    d_1367_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1355_materials_, ((d_1365_unwrapOutput_).value).plaintextDataKey, ((d_1365_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1367_valueOrError3_).IsFailure():
                        output = (d_1367_valueOrError3_).PropagateFailure()
                        return output
                    d_1366_result_ = (d_1367_valueOrError3_).Extract()
                    d_1368_value_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
                    d_1368_value_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1366_result_)
                    output = Wrappers.Result_Success(d_1368_value_)
                    return output
                elif True:
                    d_1360_errors_ = (d_1360_errors_) + (_dafny.Seq([(d_1365_unwrapOutput_).error]))
            elif True:
                d_1360_errors_ = (d_1360_errors_) + (_dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncrypedDataKey ")) + (String.default__.Base10Int2String(d_1361_i_))) + (_dafny.Seq(" did not match AESKeyring. ")))]))
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1360_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
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
        d_1369_generateBytesResult_: Wrappers.Result
        out325_: Wrappers.Result
        out325_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1369_generateBytesResult_ = out325_
        d_1370_plaintextMaterial_: _dafny.Seq
        d_1371_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda85_(d_1372_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1372_e_)

        d_1371_valueOrError0_ = (d_1369_generateBytesResult_).MapFailure(lambda85_)
        if (d_1371_valueOrError0_).IsFailure():
            res = (d_1371_valueOrError0_).PropagateFailure()
            return res
        d_1370_plaintextMaterial_ = (d_1371_valueOrError0_).Extract()
        d_1373_wrapOutput_: MaterialWrapping.WrapOutput
        d_1374_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(RawAESKeyring.AesWrapInfo.default()))()
        out326_: Wrappers.Result
        out326_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1370_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1374_valueOrError1_ = out326_
        if (d_1374_valueOrError1_).IsFailure():
            res = (d_1374_valueOrError1_).PropagateFailure()
            return res
        d_1373_wrapOutput_ = (d_1374_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1370_plaintextMaterial_, (d_1373_wrapOutput_).wrappedMaterial, (d_1373_wrapOutput_).wrapInfo))
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
        d_1375_aad_: _dafny.Seq
        d_1376_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1376_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1376_valueOrError0_).IsFailure():
            res = (d_1376_valueOrError0_).PropagateFailure()
            return res
        d_1375_aad_ = (d_1376_valueOrError0_).Extract()
        d_1377_randomIvResult_: Wrappers.Result
        out327_: Wrappers.Result
        out327_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_1377_randomIvResult_ = out327_
        d_1378_iv_: _dafny.Seq
        d_1379_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda86_(d_1380_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1380_e_)

        d_1379_valueOrError1_ = (d_1377_randomIvResult_).MapFailure(lambda86_)
        if (d_1379_valueOrError1_).IsFailure():
            res = (d_1379_valueOrError1_).PropagateFailure()
            return res
        d_1378_iv_ = (d_1379_valueOrError1_).Extract()
        d_1381_aesEncryptResult_: Wrappers.Result
        out328_: Wrappers.Result
        out328_ = ((self).cryptoPrimitives).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_1378_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1375_aad_))
        d_1381_aesEncryptResult_ = out328_
        d_1382_wrappedMaterialResult_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1383_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda87_(d_1384_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1384_e_)

        d_1383_valueOrError2_ = (d_1381_aesEncryptResult_).MapFailure(lambda87_)
        if (d_1383_valueOrError2_).IsFailure():
            res = (d_1383_valueOrError2_).PropagateFailure()
            return res
        d_1382_wrappedMaterialResult_ = (d_1383_valueOrError2_).Extract()
        d_1385_wrappedMaterial_: _dafny.Seq
        d_1385_wrappedMaterial_ = RawAESKeyring.default__.SerializeEDKCiphertext(d_1382_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_1385_wrappedMaterial_, RawAESKeyring.AesWrapInfo_AesWrapInfo(d_1378_iv_)))
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
        d_1386_aad_: _dafny.Seq
        d_1387_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1387_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1387_valueOrError0_).IsFailure():
            res = (d_1387_valueOrError0_).PropagateFailure()
            return res
        d_1386_aad_ = (d_1387_valueOrError0_).Extract()
        d_1388_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1388_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1388_valueOrError1_).IsFailure():
            res = (d_1388_valueOrError1_).PropagateFailure()
            return res
        d_1389_encryptionOutput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1389_encryptionOutput_ = RawAESKeyring.default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1390_maybePtKey_: Wrappers.Result
        out329_: Wrappers.Result
        out329_ = ((self).cryptoPrimitives).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1389_encryptionOutput_).cipherText, (d_1389_encryptionOutput_).authTag, (self).iv, d_1386_aad_))
        d_1390_maybePtKey_ = out329_
        d_1391_ptKey_: _dafny.Seq
        d_1392_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda88_(d_1393_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1393_e_)

        d_1392_valueOrError2_ = (d_1390_maybePtKey_).MapFailure(lambda88_)
        if (d_1392_valueOrError2_).IsFailure():
            res = (d_1392_valueOrError2_).PropagateFailure()
            return res
        d_1391_ptKey_ = (d_1392_valueOrError2_).Extract()
        d_1394_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1394_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1391_ptKey_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1394_valueOrError3_).IsFailure():
            res = (d_1394_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1391_ptKey_, RawAESKeyring.AesUnwrapInfo_AesUnwrapInfo()))
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
