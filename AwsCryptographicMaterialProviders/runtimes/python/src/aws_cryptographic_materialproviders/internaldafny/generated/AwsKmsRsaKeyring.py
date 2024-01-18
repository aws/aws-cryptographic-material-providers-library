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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
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
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
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
import software_amazon_cryptography_keystore_internaldafny_types
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

# Module: AwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextDigest(cryptoPrimitives, encryptionContext):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_973_canonicalEC_: _dafny.Seq
        d_974_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_974_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_974_valueOrError0_).IsFailure():
            output = (d_974_valueOrError0_).PropagateFailure()
            return output
        d_973_canonicalEC_ = (d_974_valueOrError0_).Extract()
        d_975_DigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_975_DigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), d_973_canonicalEC_)
        d_976_maybeDigest_: Wrappers.Result
        out180_: Wrappers.Result
        out180_ = (cryptoPrimitives).Digest(d_975_DigestInput_)
        d_976_maybeDigest_ = out180_
        d_977_digest_: _dafny.Seq
        d_978_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda78_(d_979_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_979_e_)

        d_978_valueOrError1_ = (d_976_maybeDigest_).MapFailure(lambda78_)
        if (d_978_valueOrError1_).IsFailure():
            output = (d_978_valueOrError1_).PropagateFailure()
            return output
        d_977_digest_ = (d_978_valueOrError1_).Extract()
        output = Wrappers.Result_Success(d_977_digest_)
        return output
        return output

    @_dafny.classproperty
    def MIN__KMS__RSA__KEY__LEN(instance):
        return 2048

class AwsKmsRsaKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._client: Wrappers.Option = Wrappers.Option.default()()
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()()
        self._awsKmsKey: _dafny.Seq = None
        self._publicKey: Wrappers.Option = Wrappers.Option.default()()
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.AwsKmsRsaKeyring"
    def OnEncrypt(self, input):
        out181_: Wrappers.Result
        out181_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out181_

    def OnDecrypt(self, input):
        out182_: Wrappers.Result
        out182_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out182_

    def ctor__(self, publicKey, awsKmsKey, paddingScheme, client, cryptoPrimitives, grantTokens):
        d_980_parsedAwsKmsId_: Wrappers.Result
        d_980_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._publicKey = publicKey
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_980_parsedAwsKmsId_).value
        (self)._paddingScheme = paddingScheme
        (self)._client = client
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_981_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_981_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")))
        if (d_981_valueOrError0_).IsFailure():
            res = (d_981_valueOrError0_).PropagateFailure()
            return res
        d_982_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_982_valueOrError1_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_982_valueOrError1_).IsFailure():
            res = (d_982_valueOrError1_).PropagateFailure()
            return res
        d_983_wrap_: KmsRsaWrapKeyMaterial
        nw39_ = KmsRsaWrapKeyMaterial()
        nw39_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_983_wrap_ = nw39_
        d_984_generateAndWrap_: KmsRsaGenerateAndWrapKeyMaterial
        nw40_ = KmsRsaGenerateAndWrapKeyMaterial()
        nw40_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_984_generateAndWrap_ = nw40_
        d_985_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_986_valueOrError2_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsRsaWrapInfo.default()))()
        out183_: Wrappers.Result
        out183_ = EdkWrapping.default__.WrapEdkMaterial((input).materials, d_983_wrap_, d_984_generateAndWrap_)
        d_986_valueOrError2_ = out183_
        if (d_986_valueOrError2_).IsFailure():
            res = (d_986_valueOrError2_).PropagateFailure()
            return res
        d_985_wrapOutput_ = (d_986_valueOrError2_).Extract()
        d_987_symmetricSigningKeyList_: Wrappers.Option
        d_987_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_985_wrapOutput_).symmetricSigningKey).value])) if ((d_985_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_988_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_988_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.RSA__PROVIDER__ID, (UTF8.default__.Encode((self).awsKmsKey)).value, (d_985_wrapOutput_).wrappedMaterial)
        d_989_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        if (d_985_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_990_valueOrError3_: Wrappers.Result = None
            d_990_valueOrError3_ = Materials.default__.EncryptionMaterialAddDataKey((input).materials, (d_985_wrapOutput_).plaintextDataKey, _dafny.Seq([d_988_edk_]), d_987_symmetricSigningKeyList_)
            if (d_990_valueOrError3_).IsFailure():
                res = (d_990_valueOrError3_).PropagateFailure()
                return res
            d_989_returnMaterials_ = (d_990_valueOrError3_).Extract()
        elif (d_985_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_991_valueOrError4_: Wrappers.Result = None
            d_991_valueOrError4_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys((input).materials, _dafny.Seq([d_988_edk_]), d_987_symmetricSigningKeyList_)
            if (d_991_valueOrError4_).IsFailure():
                res = (d_991_valueOrError4_).PropagateFailure()
                return res
            d_989_returnMaterials_ = (d_991_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_989_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_992_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_992_valueOrError0_ = Wrappers.default__.Need(((self).client).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")))
        if (d_992_valueOrError0_).IsFailure():
            res = (d_992_valueOrError0_).PropagateFailure()
            return res
        d_993_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_993_materials_ = (input).materials
        d_994_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_994_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_993_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_994_valueOrError1_).IsFailure():
            res = (d_994_valueOrError1_).PropagateFailure()
            return res
        d_995_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_995_valueOrError2_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_995_valueOrError2_).IsFailure():
            res = (d_995_valueOrError2_).PropagateFailure()
            return res
        d_996_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw41_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw41_.ctor__((self).awsKmsArn, Constants.default__.RSA__PROVIDER__ID)
        d_996_filter_ = nw41_
        d_997_edksToAttempt_: _dafny.Seq
        d_998_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out184_: Wrappers.Result
        out184_ = Actions.default__.FilterWithResult(d_996_filter_, (input).encryptedDataKeys)
        d_998_valueOrError3_ = out184_
        if (d_998_valueOrError3_).IsFailure():
            res = (d_998_valueOrError3_).PropagateFailure()
            return res
        d_997_edksToAttempt_ = (d_998_valueOrError3_).Extract()
        d_999_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_999_valueOrError4_ = Wrappers.default__.Need((0) < (len(d_997_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_999_valueOrError4_).IsFailure():
            res = (d_999_valueOrError4_).PropagateFailure()
            return res
        d_1000_encryptionContextDigest_: _dafny.Seq
        d_1001_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out185_: Wrappers.Result
        out185_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (d_993_materials_).encryptionContext)
        d_1001_valueOrError5_ = out185_
        if (d_1001_valueOrError5_).IsFailure():
            res = (d_1001_valueOrError5_).PropagateFailure()
            return res
        d_1000_encryptionContextDigest_ = (d_1001_valueOrError5_).Extract()
        d_1002_decryptClosure_: Actions.ActionWithResult
        nw42_ = DecryptSingleAWSRSAEncryptedDataKey()
        nw42_.ctor__(d_993_materials_, ((self).client).value, (self).awsKmsKey, (self).paddingScheme, d_1000_encryptionContextDigest_, (self).grantTokens)
        d_1002_decryptClosure_ = nw42_
        d_1003_outcome_: Wrappers.Result
        out186_: Wrappers.Result
        out186_ = Actions.default__.ReduceToSuccess(d_1002_decryptClosure_, d_997_edksToAttempt_)
        d_1003_outcome_ = out186_
        d_1004_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1005_valueOrError6_: Wrappers.Result = None
        def lambda79_(d_1006_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1006_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1005_valueOrError6_ = (d_1003_outcome_).MapFailure(lambda79_)
        if (d_1005_valueOrError6_).IsFailure():
            res = (d_1005_valueOrError6_).PropagateFailure()
            return res
        d_1004_SealedDecryptionMaterials_ = (d_1005_valueOrError6_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1004_SealedDecryptionMaterials_))
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
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()()
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
        d_1007_unwrap_: KmsRsaUnwrapKeyMaterial
        nw43_ = KmsRsaUnwrapKeyMaterial()
        nw43_.ctor__((self).client, (self).awsKmsKey, (self).paddingScheme, (self).encryptionContextDigest, (self).grantTokens)
        d_1007_unwrap_ = nw43_
        d_1008_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1009_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsRsaUnwrapInfo.default()))()
        out187_: Wrappers.Result
        out187_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1007_unwrap_)
        d_1009_valueOrError0_ = out187_
        if (d_1009_valueOrError0_).IsFailure():
            res = (d_1009_valueOrError0_).PropagateFailure()
            return res
        d_1008_unwrapOutput_ = (d_1009_valueOrError0_).Extract()
        d_1010_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1011_valueOrError1_: Wrappers.Result = None
        d_1011_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1008_unwrapOutput_).plaintextDataKey, (d_1008_unwrapOutput_).symmetricSigningKey)
        if (d_1011_valueOrError1_).IsFailure():
            res = (d_1011_valueOrError1_).PropagateFailure()
            return res
        d_1010_result_ = (d_1011_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_1010_result_)
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
        return isinstance(self, KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)

class KmsRsaUnwrapInfo_KmsRsaUnwrapInfo(KmsRsaUnwrapInfo, NamedTuple('KmsRsaUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaUnwrapInfo.KmsRsaUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)
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
        return isinstance(self, KmsRsaWrapInfo_KmsRsaWrapInfo)

class KmsRsaWrapInfo_KmsRsaWrapInfo(KmsRsaWrapInfo, NamedTuple('KmsRsaWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaWrapInfo.KmsRsaWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaWrapInfo_KmsRsaWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsRsaWrapInfo.default()))()
        d_1012_generateBytesResult_: Wrappers.Result
        out188_: Wrappers.Result
        out188_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1012_generateBytesResult_ = out188_
        d_1013_plaintextMaterial_: _dafny.Seq
        d_1014_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda80_(d_1015_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1015_e_)

        d_1014_valueOrError0_ = (d_1012_generateBytesResult_).MapFailure(lambda80_)
        if (d_1014_valueOrError0_).IsFailure():
            res = (d_1014_valueOrError0_).PropagateFailure()
            return res
        d_1013_plaintextMaterial_ = (d_1014_valueOrError0_).Extract()
        d_1016_wrap_: KmsRsaWrapKeyMaterial
        nw44_ = KmsRsaWrapKeyMaterial()
        nw44_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_1016_wrap_ = nw44_
        d_1017_wrapOutput_: MaterialWrapping.WrapOutput
        d_1018_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        out189_: Wrappers.Result
        out189_ = (d_1016_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1013_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1018_valueOrError1_ = out189_
        if (d_1018_valueOrError1_).IsFailure():
            res = (d_1018_valueOrError1_).PropagateFailure()
            return res
        d_1017_wrapOutput_ = (d_1018_valueOrError1_).Extract()
        d_1019_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1019_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1013_plaintextMaterial_, (d_1017_wrapOutput_).wrappedMaterial, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1019_output_)
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
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        d_1020_encryptionContextDigest_: _dafny.Seq
        d_1021_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out190_: Wrappers.Result
        out190_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (input).encryptionContext)
        d_1021_valueOrError0_ = out190_
        if (d_1021_valueOrError0_).IsFailure():
            res = (d_1021_valueOrError0_).PropagateFailure()
            return res
        d_1020_encryptionContextDigest_ = (d_1021_valueOrError0_).Extract()
        d_1022_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda81_(source29_):
            if source29_.is_RSAES__OAEP__SHA__1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()

        d_1022_padding_ = lambda81_((self).paddingScheme)
        d_1023_RSAEncryptOutput_: Wrappers.Result
        out191_: Wrappers.Result
        out191_ = ((self).cryptoPrimitives).RSAEncrypt(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(d_1022_padding_, (self).publicKey, (d_1020_encryptionContextDigest_) + ((input).plaintextMaterial)))
        d_1023_RSAEncryptOutput_ = out191_
        d_1024_ciphertext_: _dafny.Seq
        d_1025_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda82_(d_1026_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1026_e_)

        d_1025_valueOrError1_ = (d_1023_RSAEncryptOutput_).MapFailure(lambda82_)
        if (d_1025_valueOrError1_).IsFailure():
            res = (d_1025_valueOrError1_).PropagateFailure()
            return res
        d_1024_ciphertext_ = (d_1025_valueOrError1_).Extract()
        d_1027_output_: MaterialWrapping.WrapOutput
        d_1027_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_1024_ciphertext_, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1027_output_)
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
        self._paddingScheme: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.default()()
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
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(KmsRsaUnwrapInfo.default()))()
        d_1028_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1028_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_1028_valueOrError0_).IsFailure():
            res = (d_1028_valueOrError0_).PropagateFailure()
            return res
        d_1029_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_1029_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_Some((self).paddingScheme))
        d_1030_maybeDecryptResponse_: Wrappers.Result
        out192_: Wrappers.Result
        out192_ = ((self).client).Decrypt(d_1029_decryptRequest_)
        d_1030_maybeDecryptResponse_ = out192_
        d_1031_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_1032_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda83_(d_1033_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_1033_e_)

        d_1032_valueOrError1_ = (d_1030_maybeDecryptResponse_).MapFailure(lambda83_)
        if (d_1032_valueOrError1_).IsFailure():
            res = (d_1032_valueOrError1_).PropagateFailure()
            return res
        d_1031_decryptResponse_ = (d_1032_valueOrError1_).Extract()
        d_1034_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1034_valueOrError2_ = Wrappers.default__.Need(((((d_1031_decryptResponse_).KeyId).is_Some) and ((((d_1031_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_1031_decryptResponse_).Plaintext).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_1034_valueOrError2_).IsFailure():
            res = (d_1034_valueOrError2_).PropagateFailure()
            return res
        d_1035_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1035_valueOrError3_ = Wrappers.default__.Need((((self).encryptionContextDigest) <= (((d_1031_decryptResponse_).Plaintext).value)) and (((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) + (len((self).encryptionContextDigest))) == (len(((d_1031_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context digest does not match expected value.")))
        if (d_1035_valueOrError3_).IsFailure():
            res = (d_1035_valueOrError3_).PropagateFailure()
            return res
        d_1036_output_: MaterialWrapping.UnwrapOutput
        d_1036_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(_dafny.Seq((((d_1031_decryptResponse_).Plaintext).value)[len((self).encryptionContextDigest)::]), KmsRsaUnwrapInfo_KmsRsaUnwrapInfo())
        res = Wrappers.Result_Success(d_1036_output_)
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
