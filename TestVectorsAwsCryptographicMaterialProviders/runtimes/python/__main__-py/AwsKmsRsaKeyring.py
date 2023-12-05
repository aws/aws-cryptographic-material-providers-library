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

# Module: AwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextDigest(cryptoPrimitives, encryptionContext):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_892_canonicalEC_: _dafny.Seq
        d_893_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_893_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_893_valueOrError0_).IsFailure():
            output = (d_893_valueOrError0_).PropagateFailure()
            return output
        d_892_canonicalEC_ = (d_893_valueOrError0_).Extract()
        d_894_DigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_894_DigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), d_892_canonicalEC_)
        d_895_maybeDigest_: Wrappers.Result
        out187_: Wrappers.Result
        out187_ = (cryptoPrimitives).Digest(d_894_DigestInput_)
        d_895_maybeDigest_ = out187_
        d_896_digest_: _dafny.Seq
        d_897_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda56_(d_898_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_898_e_)

        d_897_valueOrError1_ = (d_895_maybeDigest_).MapFailure(lambda56_)
        if (d_897_valueOrError1_).IsFailure():
            output = (d_897_valueOrError1_).PropagateFailure()
            return output
        d_896_digest_ = (d_897_valueOrError1_).Extract()
        output = Wrappers.Result_Success(d_896_digest_)
        return output
        return output

    @_dafny.classproperty
    def MIN__KMS__RSA__KEY__LEN(instance):
        return 2048

class AwsKmsRsaKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
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
        out188_: Wrappers.Result
        out188_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out188_

    def OnDecrypt(self, input):
        out189_: Wrappers.Result
        out189_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out189_

    def ctor__(self, publicKey, awsKmsKey, paddingScheme, client, cryptoPrimitives, grantTokens):
        d_899_parsedAwsKmsId_: Wrappers.Result
        d_899_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._publicKey = publicKey
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_899_parsedAwsKmsId_).value
        (self)._paddingScheme = paddingScheme
        (self)._client = client
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_900_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_900_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")))
        if (d_900_valueOrError0_).IsFailure():
            res = (d_900_valueOrError0_).PropagateFailure()
            return res
        d_901_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_901_valueOrError1_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_901_valueOrError1_).IsFailure():
            res = (d_901_valueOrError1_).PropagateFailure()
            return res
        d_902_wrap_: KmsRsaWrapKeyMaterial
        nw39_ = KmsRsaWrapKeyMaterial()
        nw39_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_902_wrap_ = nw39_
        d_903_generateAndWrap_: KmsRsaGenerateAndWrapKeyMaterial
        nw40_ = KmsRsaGenerateAndWrapKeyMaterial()
        nw40_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_903_generateAndWrap_ = nw40_
        d_904_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_905_valueOrError2_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsRsaWrapInfo.default()))()
        out190_: Wrappers.Result
        out190_ = EdkWrapping.default__.WrapEdkMaterial((input).materials, d_902_wrap_, d_903_generateAndWrap_)
        d_905_valueOrError2_ = out190_
        if (d_905_valueOrError2_).IsFailure():
            res = (d_905_valueOrError2_).PropagateFailure()
            return res
        d_904_wrapOutput_ = (d_905_valueOrError2_).Extract()
        d_906_symmetricSigningKeyList_: Wrappers.Option
        d_906_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_904_wrapOutput_).symmetricSigningKey).value])) if ((d_904_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_907_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_907_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.RSA__PROVIDER__ID, (UTF8.default__.Encode((self).awsKmsKey)).value, (d_904_wrapOutput_).wrappedMaterial)
        d_908_returnMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        if (d_904_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_909_valueOrError3_: Wrappers.Result = None
            d_909_valueOrError3_ = Materials.default__.EncryptionMaterialAddDataKey((input).materials, (d_904_wrapOutput_).plaintextDataKey, _dafny.Seq([d_907_edk_]), d_906_symmetricSigningKeyList_)
            if (d_909_valueOrError3_).IsFailure():
                res = (d_909_valueOrError3_).PropagateFailure()
                return res
            d_908_returnMaterials_ = (d_909_valueOrError3_).Extract()
        elif (d_904_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_910_valueOrError4_: Wrappers.Result = None
            d_910_valueOrError4_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys((input).materials, _dafny.Seq([d_907_edk_]), d_906_symmetricSigningKeyList_)
            if (d_910_valueOrError4_).IsFailure():
                res = (d_910_valueOrError4_).PropagateFailure()
                return res
            d_908_returnMaterials_ = (d_910_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_908_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_911_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_911_valueOrError0_ = Wrappers.default__.Need(((self).client).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")))
        if (d_911_valueOrError0_).IsFailure():
            res = (d_911_valueOrError0_).PropagateFailure()
            return res
        d_912_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_912_materials_ = (input).materials
        d_913_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_913_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_912_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_913_valueOrError1_).IsFailure():
            res = (d_913_valueOrError1_).PropagateFailure()
            return res
        d_914_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_914_valueOrError2_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_914_valueOrError2_).IsFailure():
            res = (d_914_valueOrError2_).PropagateFailure()
            return res
        d_915_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw41_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw41_.ctor__((self).awsKmsArn, Constants.default__.RSA__PROVIDER__ID)
        d_915_filter_ = nw41_
        d_916_edksToAttempt_: _dafny.Seq
        d_917_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out191_: Wrappers.Result
        out191_ = Actions.default__.FilterWithResult(d_915_filter_, (input).encryptedDataKeys)
        d_917_valueOrError3_ = out191_
        if (d_917_valueOrError3_).IsFailure():
            res = (d_917_valueOrError3_).PropagateFailure()
            return res
        d_916_edksToAttempt_ = (d_917_valueOrError3_).Extract()
        d_918_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_918_valueOrError4_ = Wrappers.default__.Need((0) < (len(d_916_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_918_valueOrError4_).IsFailure():
            res = (d_918_valueOrError4_).PropagateFailure()
            return res
        d_919_encryptionContextDigest_: _dafny.Seq
        d_920_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out192_: Wrappers.Result
        out192_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (d_912_materials_).encryptionContext)
        d_920_valueOrError5_ = out192_
        if (d_920_valueOrError5_).IsFailure():
            res = (d_920_valueOrError5_).PropagateFailure()
            return res
        d_919_encryptionContextDigest_ = (d_920_valueOrError5_).Extract()
        d_921_decryptClosure_: Actions.ActionWithResult
        nw42_ = DecryptSingleAWSRSAEncryptedDataKey()
        nw42_.ctor__(d_912_materials_, ((self).client).value, (self).awsKmsKey, (self).paddingScheme, d_919_encryptionContextDigest_, (self).grantTokens)
        d_921_decryptClosure_ = nw42_
        d_922_outcome_: Wrappers.Result
        out193_: Wrappers.Result
        out193_ = Actions.default__.ReduceToSuccess(d_921_decryptClosure_, d_916_edksToAttempt_)
        d_922_outcome_ = out193_
        d_923_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_924_valueOrError6_: Wrappers.Result = None
        def lambda57_(d_925_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_925_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_924_valueOrError6_ = (d_922_outcome_).MapFailure(lambda57_)
        if (d_924_valueOrError6_).IsFailure():
            res = (d_924_valueOrError6_).PropagateFailure()
            return res
        d_923_SealedDecryptionMaterials_ = (d_924_valueOrError6_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_923_SealedDecryptionMaterials_))
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
        d_926_unwrap_: KmsRsaUnwrapKeyMaterial
        nw43_ = KmsRsaUnwrapKeyMaterial()
        nw43_.ctor__((self).client, (self).awsKmsKey, (self).paddingScheme, (self).encryptionContextDigest, (self).grantTokens)
        d_926_unwrap_ = nw43_
        d_927_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_928_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsRsaUnwrapInfo.default()))()
        out194_: Wrappers.Result
        out194_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_926_unwrap_)
        d_928_valueOrError0_ = out194_
        if (d_928_valueOrError0_).IsFailure():
            res = (d_928_valueOrError0_).PropagateFailure()
            return res
        d_927_unwrapOutput_ = (d_928_valueOrError0_).Extract()
        d_929_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_930_valueOrError1_: Wrappers.Result = None
        d_930_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_927_unwrapOutput_).plaintextDataKey, (d_927_unwrapOutput_).symmetricSigningKey)
        if (d_930_valueOrError1_).IsFailure():
            res = (d_930_valueOrError1_).PropagateFailure()
            return res
        d_929_result_ = (d_930_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_929_result_)
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
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
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
        d_931_generateBytesResult_: Wrappers.Result
        out195_: Wrappers.Result
        out195_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_931_generateBytesResult_ = out195_
        d_932_plaintextMaterial_: _dafny.Seq
        d_933_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda58_(d_934_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_934_e_)

        d_933_valueOrError0_ = (d_931_generateBytesResult_).MapFailure(lambda58_)
        if (d_933_valueOrError0_).IsFailure():
            res = (d_933_valueOrError0_).PropagateFailure()
            return res
        d_932_plaintextMaterial_ = (d_933_valueOrError0_).Extract()
        d_935_wrap_: KmsRsaWrapKeyMaterial
        nw44_ = KmsRsaWrapKeyMaterial()
        nw44_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_935_wrap_ = nw44_
        d_936_wrapOutput_: MaterialWrapping.WrapOutput
        d_937_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        out196_: Wrappers.Result
        out196_ = (d_935_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_932_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_937_valueOrError1_ = out196_
        if (d_937_valueOrError1_).IsFailure():
            res = (d_937_valueOrError1_).PropagateFailure()
            return res
        d_936_wrapOutput_ = (d_937_valueOrError1_).Extract()
        d_938_output_: MaterialWrapping.GenerateAndWrapOutput
        d_938_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_932_plaintextMaterial_, (d_936_wrapOutput_).wrappedMaterial, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_938_output_)
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
        d_939_encryptionContextDigest_: _dafny.Seq
        d_940_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out197_: Wrappers.Result
        out197_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (input).encryptionContext)
        d_940_valueOrError0_ = out197_
        if (d_940_valueOrError0_).IsFailure():
            res = (d_940_valueOrError0_).PropagateFailure()
            return res
        d_939_encryptionContextDigest_ = (d_940_valueOrError0_).Extract()
        d_941_padding_: software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode
        def lambda59_(source31_):
            if source31_.is_RSAES__OAEP__SHA__1:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA1()
            elif True:
                return software_amazon_cryptography_primitives_internaldafny_types.RSAPaddingMode_OAEP__SHA256()

        d_941_padding_ = lambda59_((self).paddingScheme)
        d_942_RSAEncryptOutput_: Wrappers.Result
        out198_: Wrappers.Result
        out198_ = ((self).cryptoPrimitives).RSAEncrypt(software_amazon_cryptography_primitives_internaldafny_types.RSAEncryptInput_RSAEncryptInput(d_941_padding_, (self).publicKey, (d_939_encryptionContextDigest_) + ((input).plaintextMaterial)))
        d_942_RSAEncryptOutput_ = out198_
        d_943_ciphertext_: _dafny.Seq
        d_944_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda60_(d_945_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_945_e_)

        d_944_valueOrError1_ = (d_942_RSAEncryptOutput_).MapFailure(lambda60_)
        if (d_944_valueOrError1_).IsFailure():
            res = (d_944_valueOrError1_).PropagateFailure()
            return res
        d_943_ciphertext_ = (d_944_valueOrError1_).Extract()
        d_946_output_: MaterialWrapping.WrapOutput
        d_946_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_943_ciphertext_, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_946_output_)
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
        d_947_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_947_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_947_valueOrError0_).IsFailure():
            res = (d_947_valueOrError0_).PropagateFailure()
            return res
        d_948_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_948_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_Some((self).paddingScheme))
        d_949_maybeDecryptResponse_: Wrappers.Result
        out199_: Wrappers.Result
        out199_ = ((self).client).Decrypt(d_948_decryptRequest_)
        d_949_maybeDecryptResponse_ = out199_
        d_950_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_951_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda61_(d_952_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_952_e_)

        d_951_valueOrError1_ = (d_949_maybeDecryptResponse_).MapFailure(lambda61_)
        if (d_951_valueOrError1_).IsFailure():
            res = (d_951_valueOrError1_).PropagateFailure()
            return res
        d_950_decryptResponse_ = (d_951_valueOrError1_).Extract()
        d_953_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_953_valueOrError2_ = Wrappers.default__.Need(((((d_950_decryptResponse_).KeyId).is_Some) and ((((d_950_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_950_decryptResponse_).Plaintext).is_Some), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_953_valueOrError2_).IsFailure():
            res = (d_953_valueOrError2_).PropagateFailure()
            return res
        d_954_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_954_valueOrError3_ = Wrappers.default__.Need((((self).encryptionContextDigest) <= (((d_950_decryptResponse_).Plaintext).value)) and (((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) + (len((self).encryptionContextDigest))) == (len(((d_950_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context digest does not match expected value.")))
        if (d_954_valueOrError3_).IsFailure():
            res = (d_954_valueOrError3_).PropagateFailure()
            return res
        d_955_output_: MaterialWrapping.UnwrapOutput
        d_955_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(_dafny.Seq((((d_950_decryptResponse_).Plaintext).value)[len((self).encryptionContextDigest)::]), KmsRsaUnwrapInfo_KmsRsaUnwrapInfo())
        res = Wrappers.Result_Success(d_955_output_)
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
