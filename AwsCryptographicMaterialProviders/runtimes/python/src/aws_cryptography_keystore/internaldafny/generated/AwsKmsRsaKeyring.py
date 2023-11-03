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

assert "AwsKmsRsaKeyring" == __name__
AwsKmsRsaKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextDigest(cryptoPrimitives, encryptionContext):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1278_canonicalEC_: _dafny.Seq
        d_1279_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1279_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_1279_valueOrError0_).IsFailure():
            output = (d_1279_valueOrError0_).PropagateFailure()
            return output
        d_1278_canonicalEC_ = (d_1279_valueOrError0_).Extract()
        d_1280_DigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_1280_DigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), d_1278_canonicalEC_)
        d_1281_maybeDigest_: Wrappers.Result
        out308_: Wrappers.Result
        out308_ = (cryptoPrimitives).Digest(d_1280_DigestInput_)
        d_1281_maybeDigest_ = out308_
        d_1282_digest_: _dafny.Seq
        d_1283_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda79_(d_1284_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1284_e_)

        d_1283_valueOrError1_ = (d_1281_maybeDigest_).MapFailure(lambda79_)
        if (d_1283_valueOrError1_).IsFailure():
            output = (d_1283_valueOrError1_).PropagateFailure()
            return output
        d_1282_digest_ = (d_1283_valueOrError1_).Extract()
        output = Wrappers.Result_Success(d_1282_digest_)
        return output
        return output

    @_dafny.classproperty
    def MIN__KMS__RSA__KEY__LEN(instance):
        return 2048

class AwsKmsRsaKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._client: Wrappers.Option = Wrappers.Option_None.default()()
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()()
        self._awsKmsKey: _dafny.Seq = None
        self._publicKey: Wrappers.Option = Wrappers.Option_None.default()()
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.AwsKmsRsaKeyring"
    def OnEncrypt(self, input):
        out309_: Wrappers.Result
        out309_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out309_

    def OnDecrypt(self, input):
        out310_: Wrappers.Result
        out310_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out310_

    def ctor__(self, publicKey, awsKmsKey, paddingScheme, client, cryptoPrimitives, grantTokens):
        d_1285_parsedAwsKmsId_: Wrappers.Result
        d_1285_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._publicKey = publicKey
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_1285_parsedAwsKmsId_).value
        (self)._paddingScheme = paddingScheme
        (self)._client = client
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_1286_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1286_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")))
        if (d_1286_valueOrError0_).IsFailure():
            res = (d_1286_valueOrError0_).PropagateFailure()
            return res
        d_1287_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1287_valueOrError1_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_1287_valueOrError1_).IsFailure():
            res = (d_1287_valueOrError1_).PropagateFailure()
            return res
        d_1288_wrap_: AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial
        nw40_ = AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial()
        nw40_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1288_wrap_ = nw40_
        d_1289_generateAndWrap_: AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial
        nw41_ = AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial()
        nw41_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1289_generateAndWrap_ = nw41_
        d_1290_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1291_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsRsaKeyring.KmsRsaWrapInfo.default()))()
        out311_: Wrappers.Result
        out311_ = EdkWrapping.default__.WrapEdkMaterial((input).materials, d_1288_wrap_, d_1289_generateAndWrap_)
        d_1291_valueOrError2_ = out311_
        if (d_1291_valueOrError2_).IsFailure():
            res = (d_1291_valueOrError2_).PropagateFailure()
            return res
        d_1290_wrapOutput_ = (d_1291_valueOrError2_).Extract()
        d_1292_symmetricSigningKeyList_: Wrappers.Option
        d_1292_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1290_wrapOutput_).symmetricSigningKey).value])) if ((d_1290_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1293_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1293_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).RSA__PROVIDER__ID, (UTF8.default__.Encode((self).awsKmsKey)).value, (d_1290_wrapOutput_).wrappedMaterial)
        d_1294_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        if (d_1290_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1295_valueOrError3_: Wrappers.Result = None
            d_1295_valueOrError3_ = Materials.default__.EncryptionMaterialAddDataKey((input).materials, (d_1290_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1293_edk_]), d_1292_symmetricSigningKeyList_)
            if (d_1295_valueOrError3_).IsFailure():
                res = (d_1295_valueOrError3_).PropagateFailure()
                return res
            d_1294_returnMaterials_ = (d_1295_valueOrError3_).Extract()
        elif (d_1290_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1296_valueOrError4_: Wrappers.Result = None
            d_1296_valueOrError4_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys((input).materials, _dafny.Seq([d_1293_edk_]), d_1292_symmetricSigningKeyList_)
            if (d_1296_valueOrError4_).IsFailure():
                res = (d_1296_valueOrError4_).PropagateFailure()
                return res
            d_1294_returnMaterials_ = (d_1296_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1294_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1297_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1297_valueOrError0_ = Wrappers.default__.Need(((self).client).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")))
        if (d_1297_valueOrError0_).IsFailure():
            res = (d_1297_valueOrError0_).PropagateFailure()
            return res
        d_1298_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1298_materials_ = (input).materials
        d_1299_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1299_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1298_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1299_valueOrError1_).IsFailure():
            res = (d_1299_valueOrError1_).PropagateFailure()
            return res
        d_1300_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1300_valueOrError2_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_1300_valueOrError2_).IsFailure():
            res = (d_1300_valueOrError2_).PropagateFailure()
            return res
        d_1301_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw42_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw42_.ctor__((self).awsKmsArn, (Constants.default__).RSA__PROVIDER__ID)
        d_1301_filter_ = nw42_
        d_1302_edksToAttempt_: _dafny.Seq
        d_1303_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out312_: Wrappers.Result
        out312_ = Actions.default__.FilterWithResult(d_1301_filter_, (input).encryptedDataKeys)
        d_1303_valueOrError3_ = out312_
        if (d_1303_valueOrError3_).IsFailure():
            res = (d_1303_valueOrError3_).PropagateFailure()
            return res
        d_1302_edksToAttempt_ = (d_1303_valueOrError3_).Extract()
        d_1304_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1304_valueOrError4_ = Wrappers.default__.Need((0) < (len(d_1302_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_1304_valueOrError4_).IsFailure():
            res = (d_1304_valueOrError4_).PropagateFailure()
            return res
        d_1305_encryptionContextDigest_: _dafny.Seq
        d_1306_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out313_: Wrappers.Result
        out313_ = AwsKmsRsaKeyring.default__.EncryptionContextDigest((self).cryptoPrimitives, (d_1298_materials_).encryptionContext)
        d_1306_valueOrError5_ = out313_
        if (d_1306_valueOrError5_).IsFailure():
            res = (d_1306_valueOrError5_).PropagateFailure()
            return res
        d_1305_encryptionContextDigest_ = (d_1306_valueOrError5_).Extract()
        d_1307_decryptClosure_: Actions.ActionWithResult
        nw43_ = AwsKmsRsaKeyring.DecryptSingleAWSRSAEncryptedDataKey()
        nw43_.ctor__(d_1298_materials_, ((self).client).value, (self).awsKmsKey, (self).paddingScheme, d_1305_encryptionContextDigest_, (self).grantTokens)
        d_1307_decryptClosure_ = nw43_
        d_1308_outcome_: Wrappers.Result
        out314_: Wrappers.Result
        out314_ = Actions.default__.ReduceToSuccess(d_1307_decryptClosure_, d_1302_edksToAttempt_)
        d_1308_outcome_ = out314_
        d_1309_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1310_valueOrError6_: Wrappers.Result = None
        def lambda80_(d_1311_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1311_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1310_valueOrError6_ = (d_1308_outcome_).MapFailure(lambda80_)
        if (d_1310_valueOrError6_).IsFailure():
            res = (d_1310_valueOrError6_).PropagateFailure()
            return res
        d_1309_SealedDecryptionMaterials_ = (d_1310_valueOrError6_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1309_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def client(self):
        return self._client
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def publicKey(self):
        return self._publicKey
    @property
    def awsKmsArn(self):
        return self._awsKmsArn
    @property
    def grantTokens(self):
        return self._grantTokens

class DecryptSingleAWSRSAEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()()
        self._encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.DecryptSingleAWSRSAEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._paddingScheme = paddingScheme
        (self)._encryptionContextDigest = encryptionContextDigest
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_1312_unwrap_: AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial
        nw44_ = AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial()
        nw44_.ctor__((self).client, (self).awsKmsKey, (self).paddingScheme, (self).encryptionContextDigest, (self).grantTokens)
        d_1312_unwrap_ = nw44_
        d_1313_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1314_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsRsaKeyring.KmsRsaUnwrapInfo.default()))()
        out315_: Wrappers.Result
        out315_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1312_unwrap_)
        d_1314_valueOrError0_ = out315_
        if (d_1314_valueOrError0_).IsFailure():
            res = (d_1314_valueOrError0_).PropagateFailure()
            return res
        d_1313_unwrapOutput_ = (d_1314_valueOrError0_).Extract()
        d_1315_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1316_valueOrError1_: Wrappers.Result = None
        d_1316_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1313_unwrapOutput_).plaintextDataKey, (d_1313_unwrapOutput_).symmetricSigningKey)
        if (d_1316_valueOrError1_).IsFailure():
            res = (d_1316_valueOrError1_).PropagateFailure()
            return res
        d_1315_result_ = (d_1316_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_1315_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._encryptionContextDigest
    @property
    def grantTokens(self):
        return self._grantTokens

class KmsRsaUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsRsaUnwrapInfo_KmsRsaUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaUnwrapInfo_KmsRsaUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaUnwrapInfo(self) -> bool:
        return isinstance(self, AwsKmsRsaKeyring.KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)

class KmsRsaUnwrapInfo_KmsRsaUnwrapInfo(KmsRsaUnwrapInfo, NamedTuple('KmsRsaUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaUnwrapInfo.KmsRsaUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsRsaKeyring.KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaWrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsRsaWrapInfo_KmsRsaWrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaWrapInfo_KmsRsaWrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaWrapInfo(self) -> bool:
        return isinstance(self, AwsKmsRsaKeyring.KmsRsaWrapInfo_KmsRsaWrapInfo)

class KmsRsaWrapInfo_KmsRsaWrapInfo(KmsRsaWrapInfo, NamedTuple('KmsRsaWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaWrapInfo.KmsRsaWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsRsaKeyring.KmsRsaWrapInfo_KmsRsaWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(AwsKmsRsaKeyring.KmsRsaWrapInfo.default()))()
        d_1317_generateBytesResult_: Wrappers.Result
        out316_: Wrappers.Result
        out316_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1317_generateBytesResult_ = out316_
        d_1318_plaintextMaterial_: _dafny.Seq
        d_1319_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda81_(d_1320_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1320_e_)

        d_1319_valueOrError0_ = (d_1317_generateBytesResult_).MapFailure(lambda81_)
        if (d_1319_valueOrError0_).IsFailure():
            res = (d_1319_valueOrError0_).PropagateFailure()
            return res
        d_1318_plaintextMaterial_ = (d_1319_valueOrError0_).Extract()
        d_1321_wrap_: AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial
        nw45_ = AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial()
        nw45_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_1321_wrap_ = nw45_
        d_1322_wrapOutput_: MaterialWrapping.WrapOutput
        d_1323_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsRsaKeyring.KmsRsaWrapInfo.default()))()
        out317_: Wrappers.Result
        out317_ = (d_1321_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1318_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1323_valueOrError1_ = out317_
        if (d_1323_valueOrError1_).IsFailure():
            res = (d_1323_valueOrError1_).PropagateFailure()
            return res
        d_1322_wrapOutput_ = (d_1323_valueOrError1_).Extract()
        d_1324_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1324_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1318_plaintextMaterial_, (d_1322_wrapOutput_).wrappedMaterial, AwsKmsRsaKeyring.KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1324_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._paddingScheme

class KmsRsaWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsRsaKeyring.KmsRsaWrapInfo.default()))()
        d_1325_encryptionContextDigest_: _dafny.Seq
        d_1326_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out318_: Wrappers.Result
        out318_ = AwsKmsRsaKeyring.default__.EncryptionContextDigest((self).cryptoPrimitives, (input).encryptionContext)
        d_1326_valueOrError0_ = out318_
        if (d_1326_valueOrError0_).IsFailure():
            res = (d_1326_valueOrError0_).PropagateFailure()
            return res
        d_1325_encryptionContextDigest_ = (d_1326_valueOrError0_).Extract()
        d_1327_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda82_(source33_):
            if source33_.is_RSAES__OAEP__SHA__1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()

        d_1327_padding_ = lambda82_((self).paddingScheme)
        d_1328_RSAEncryptOutput_: Wrappers.Result
        out319_: Wrappers.Result
        out319_ = ((self).cryptoPrimitives).RSAEncrypt(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(d_1327_padding_, (self).publicKey, (d_1325_encryptionContextDigest_) + ((input).plaintextMaterial)))
        d_1328_RSAEncryptOutput_ = out319_
        d_1329_ciphertext_: _dafny.Seq
        d_1330_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda83_(d_1331_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1331_e_)

        d_1330_valueOrError1_ = (d_1328_RSAEncryptOutput_).MapFailure(lambda83_)
        if (d_1330_valueOrError1_).IsFailure():
            res = (d_1330_valueOrError1_).PropagateFailure()
            return res
        d_1329_ciphertext_ = (d_1330_valueOrError1_).Extract()
        d_1332_output_: MaterialWrapping.WrapOutput
        d_1332_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_1329_ciphertext_, AwsKmsRsaKeyring.KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1332_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._paddingScheme

class KmsRsaUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsKey: _dafny.Seq = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()()
        self._encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._paddingScheme = paddingScheme
        (self)._encryptionContextDigest = encryptionContextDigest
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(AwsKmsRsaKeyring.KmsRsaUnwrapInfo.default()))()
        d_1333_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1333_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_1333_valueOrError0_).IsFailure():
            res = (d_1333_valueOrError0_).PropagateFailure()
            return res
        d_1334_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_1334_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_Some((self).paddingScheme))
        d_1335_maybeDecryptResponse_: Wrappers.Result
        out320_: Wrappers.Result
        out320_ = ((self).client).Decrypt(d_1334_decryptRequest_)
        d_1335_maybeDecryptResponse_ = out320_
        d_1336_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_1337_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda84_(d_1338_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_1338_e_)

        d_1337_valueOrError1_ = (d_1335_maybeDecryptResponse_).MapFailure(lambda84_)
        if (d_1337_valueOrError1_).IsFailure():
            res = (d_1337_valueOrError1_).PropagateFailure()
            return res
        d_1336_decryptResponse_ = (d_1337_valueOrError1_).Extract()
        d_1339_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1339_valueOrError2_ = Wrappers.default__.Need(((((d_1336_decryptResponse_).KeyId).is_Some) and ((((d_1336_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_1336_decryptResponse_).Plaintext).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_1339_valueOrError2_).IsFailure():
            res = (d_1339_valueOrError2_).PropagateFailure()
            return res
        d_1340_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1340_valueOrError3_ = Wrappers.default__.Need((((self).encryptionContextDigest) <= (((d_1336_decryptResponse_).Plaintext).value)) and (((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) + (len((self).encryptionContextDigest))) == (len(((d_1336_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context digest does not match expected value.")))
        if (d_1340_valueOrError3_).IsFailure():
            res = (d_1340_valueOrError3_).PropagateFailure()
            return res
        d_1341_output_: MaterialWrapping.UnwrapOutput
        d_1341_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(_dafny.Seq((((d_1336_decryptResponse_).Plaintext).value)[len((self).encryptionContextDigest)::]), AwsKmsRsaKeyring.KmsRsaUnwrapInfo_KmsRsaUnwrapInfo())
        res = Wrappers.Result_Success(d_1341_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def grantTokens(self):
        return self._grantTokens
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._encryptionContextDigest
