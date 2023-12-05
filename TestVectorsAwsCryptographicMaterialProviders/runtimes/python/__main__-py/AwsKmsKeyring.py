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

# Module: AwsKmsKeyring


class AwsKmsKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.AwsKmsKeyring"
    def OnEncrypt(self, input):
        out88_: Wrappers.Result
        out88_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out88_

    def OnDecrypt(self, input):
        out89_: Wrappers.Result
        out89_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out89_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_417_parsedAwsKmsId_: Wrappers.Result
        d_417_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_417_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_418_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_418_materials_ = (input).materials
        d_419_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_419_suite_ = ((input).materials).algorithmSuite
        d_420_stringifiedEncCtx_: _dafny.Map
        d_421_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_421_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_421_valueOrError0_).IsFailure():
            res = (d_421_valueOrError0_).PropagateFailure()
            return res
        d_420_stringifiedEncCtx_ = (d_421_valueOrError0_).Extract()
        d_422_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw1_ = KmsGenerateAndWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_422_kmsGenerateAndWrap_ = nw1_
        d_423_kmsWrap_: KmsWrapKeyMaterial
        nw2_ = KmsWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_423_kmsWrap_ = nw2_
        d_424_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_425_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out90_: Wrappers.Result
        out90_ = EdkWrapping.default__.WrapEdkMaterial(d_418_materials_, d_423_kmsWrap_, d_422_kmsGenerateAndWrap_)
        d_425_valueOrError1_ = out90_
        if (d_425_valueOrError1_).IsFailure():
            res = (d_425_valueOrError1_).PropagateFailure()
            return res
        d_424_wrapOutput_ = (d_425_valueOrError1_).Extract()
        d_426_kmsKeyArn_: _dafny.Seq
        d_426_kmsKeyArn_ = ((d_424_wrapOutput_).wrapInfo).kmsKeyArn
        d_427_symmetricSigningKeyList_: Wrappers.Option
        d_427_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_424_wrapOutput_).symmetricSigningKey).value])) if ((d_424_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_428_providerInfo_: _dafny.Seq
        d_429_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_429_valueOrError2_ = (UTF8.default__.Encode(d_426_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_429_valueOrError2_).IsFailure():
            res = (d_429_valueOrError2_).PropagateFailure()
            return res
        d_428_providerInfo_ = (d_429_valueOrError2_).Extract()
        d_430_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_430_valueOrError3_ = Wrappers.default__.Need((len(d_428_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_430_valueOrError3_).IsFailure():
            res = (d_430_valueOrError3_).PropagateFailure()
            return res
        d_431_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_431_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_428_providerInfo_, (d_424_wrapOutput_).wrappedMaterial)
        if (d_424_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_432_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_433_valueOrError4_: Wrappers.Result = None
            d_433_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_418_materials_, (d_424_wrapOutput_).plaintextDataKey, _dafny.Seq([d_431_edk_]), d_427_symmetricSigningKeyList_)
            if (d_433_valueOrError4_).IsFailure():
                res = (d_433_valueOrError4_).PropagateFailure()
                return res
            d_432_result_ = (d_433_valueOrError4_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_432_result_))
            return res
        elif (d_424_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_434_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_435_valueOrError5_: Wrappers.Result = None
            d_435_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_418_materials_, _dafny.Seq([d_431_edk_]), d_427_symmetricSigningKeyList_)
            if (d_435_valueOrError5_).IsFailure():
                res = (d_435_valueOrError5_).PropagateFailure()
                return res
            d_434_result_ = (d_435_valueOrError5_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_434_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_436_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_436_materials_ = (input).materials
        d_437_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_437_suite_ = ((input).materials).algorithmSuite
        d_438_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_438_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_436_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_438_valueOrError0_).IsFailure():
            res = (d_438_valueOrError0_).PropagateFailure()
            return res
        d_439_filter_: OnDecryptEncryptedDataKeyFilter
        nw3_ = OnDecryptEncryptedDataKeyFilter()
        nw3_.ctor__((self).awsKmsKey)
        d_439_filter_ = nw3_
        d_440_edksToAttempt_: _dafny.Seq
        d_441_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out91_: Wrappers.Result
        out91_ = Actions.default__.FilterWithResult(d_439_filter_, (input).encryptedDataKeys)
        d_441_valueOrError1_ = out91_
        if (d_441_valueOrError1_).IsFailure():
            res = (d_441_valueOrError1_).PropagateFailure()
            return res
        d_440_edksToAttempt_ = (d_441_valueOrError1_).Extract()
        d_442_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_442_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_440_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_442_valueOrError2_).IsFailure():
            res = (d_442_valueOrError2_).PropagateFailure()
            return res
        d_443_decryptClosure_: Actions.ActionWithResult
        nw4_ = DecryptSingleEncryptedDataKey()
        nw4_.ctor__(d_436_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_443_decryptClosure_ = nw4_
        d_444_outcome_: Wrappers.Result
        out92_: Wrappers.Result
        out92_ = Actions.default__.ReduceToSuccess(d_443_decryptClosure_, d_440_edksToAttempt_)
        d_444_outcome_ = out92_
        d_445_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_446_valueOrError3_: Wrappers.Result = None
        def lambda31_(d_447_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_447_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_446_valueOrError3_ = (d_444_outcome_).MapFailure(lambda31_)
        if (d_446_valueOrError3_).IsFailure():
            res = (d_446_valueOrError3_).PropagateFailure()
            return res
        d_445_SealedDecryptionMaterials_ = (d_446_valueOrError3_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_445_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens
    @property
    def awsKmsArn(self):
        return self._awsKmsArn

class OnDecryptEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._awsKmsKey: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.OnDecryptEncryptedDataKeyFilter"
    def ctor__(self, awsKmsKey):
        (self)._awsKmsKey = awsKmsKey

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)):
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_448_keyId_: _dafny.Seq
        d_449_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_449_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_449_valueOrError0_).IsFailure():
            res = (d_449_valueOrError0_).PropagateFailure()
            return res
        d_448_keyId_ = (d_449_valueOrError0_).Extract()
        d_450___v0_: AwsArnParsing.AwsArn
        d_451_valueOrError1_: Wrappers.Result = None
        d_451_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_448_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_451_valueOrError1_).IsFailure():
            res = (d_451_valueOrError1_).PropagateFailure()
            return res
        d_450___v0_ = (d_451_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_448_keyId_))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_452_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw5_ = KmsUnwrapKeyMaterial()
        nw5_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_452_kmsUnwrap_ = nw5_
        d_453_unwrapOutputRes_: Wrappers.Result
        out93_: Wrappers.Result
        out93_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_452_kmsUnwrap_)
        d_453_unwrapOutputRes_ = out93_
        d_454_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_455_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_455_valueOrError0_ = d_453_unwrapOutputRes_
        if (d_455_valueOrError0_).IsFailure():
            res = (d_455_valueOrError0_).PropagateFailure()
            return res
        d_454_unwrapOutput_ = (d_455_valueOrError0_).Extract()
        d_456_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_457_valueOrError1_: Wrappers.Result = None
        d_457_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_454_unwrapOutput_).plaintextDataKey, (d_454_unwrapOutput_).symmetricSigningKey)
        if (d_457_valueOrError1_).IsFailure():
            res = (d_457_valueOrError1_).PropagateFailure()
            return res
        d_456_result_ = (d_457_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_456_result_)
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
    def grantTokens(self):
        return self._grantTokens

class KmsUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsUnwrapInfo_KmsUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsUnwrapInfo_KmsUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsUnwrapInfo(self) -> bool:
        return isinstance(self, KmsUnwrapInfo_KmsUnwrapInfo)

class KmsUnwrapInfo_KmsUnwrapInfo(KmsUnwrapInfo, NamedTuple('KmsUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsUnwrapInfo.KmsUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsUnwrapInfo_KmsUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsWrapInfo:
    @classmethod
    def default(cls, ):
        return lambda: KmsWrapInfo_KmsWrapInfo(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsWrapInfo(self) -> bool:
        return isinstance(self, KmsWrapInfo_KmsWrapInfo)

class KmsWrapInfo_KmsWrapInfo(KmsWrapInfo, NamedTuple('KmsWrapInfo', [('kmsKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsWrapInfo.KmsWrapInfo({_dafny.string_of(self.kmsKeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsWrapInfo_KmsWrapInfo) and self.kmsKeyArn == __o.kmsKeyArn
    def __hash__(self) -> int:
        return super().__hash__()


class KmsUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsKey: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(KmsUnwrapInfo.default()))()
        d_458_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_458_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_458_valueOrError0_).IsFailure():
            res = (d_458_valueOrError0_).PropagateFailure()
            return res
        d_459_stringifiedEncCtx_: _dafny.Map
        d_460_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_460_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_460_valueOrError1_).IsFailure():
            res = (d_460_valueOrError1_).PropagateFailure()
            return res
        d_459_stringifiedEncCtx_ = (d_460_valueOrError1_).Extract()
        d_461_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_461_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_459_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_462_maybeDecryptResponse_: Wrappers.Result
        out94_: Wrappers.Result
        out94_ = ((self).client).Decrypt(d_461_decryptRequest_)
        d_462_maybeDecryptResponse_ = out94_
        d_463_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_464_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda32_(d_465_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_465_e_)

        d_464_valueOrError2_ = (d_462_maybeDecryptResponse_).MapFailure(lambda32_)
        if (d_464_valueOrError2_).IsFailure():
            res = (d_464_valueOrError2_).PropagateFailure()
            return res
        d_463_decryptResponse_ = (d_464_valueOrError2_).Extract()
        d_466_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_466_valueOrError3_ = Wrappers.default__.Need((((((d_463_decryptResponse_).KeyId).is_Some) and ((((d_463_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_463_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_463_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_466_valueOrError3_).IsFailure():
            res = (d_466_valueOrError3_).PropagateFailure()
            return res
        d_467_output_: MaterialWrapping.UnwrapOutput
        d_467_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_463_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_467_output_)
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

class KmsGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsWrapInfo.default()))()
        d_468_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_468_suite_ = (input).algorithmSuite
        d_469_stringifiedEncCtx_: _dafny.Map
        d_470_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_470_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_470_valueOrError0_).IsFailure():
            res = (d_470_valueOrError0_).PropagateFailure()
            return res
        d_469_stringifiedEncCtx_ = (d_470_valueOrError0_).Extract()
        d_471_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_471_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_469_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_468_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_472_maybeGenerateResponse_: Wrappers.Result
        out95_: Wrappers.Result
        out95_ = ((self).client).GenerateDataKey(d_471_generatorRequest_)
        d_472_maybeGenerateResponse_ = out95_
        d_473_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_474_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        def lambda33_(d_475_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_475_e_)

        d_474_valueOrError1_ = (d_472_maybeGenerateResponse_).MapFailure(lambda33_)
        if (d_474_valueOrError1_).IsFailure():
            res = (d_474_valueOrError1_).PropagateFailure()
            return res
        d_473_generateResponse_ = (d_474_valueOrError1_).Extract()
        d_476_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_476_valueOrError2_ = Wrappers.default__.Need((((d_473_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_473_generateResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_476_valueOrError2_).IsFailure():
            res = (d_476_valueOrError2_).PropagateFailure()
            return res
        d_477_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_477_valueOrError3_ = Wrappers.default__.Need((((d_473_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_468_suite_)) == (len(((d_473_generateResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_477_valueOrError3_).IsFailure():
            res = (d_477_valueOrError3_).PropagateFailure()
            return res
        d_478_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_478_valueOrError4_ = Wrappers.default__.Need((((d_473_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_473_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_478_valueOrError4_).IsFailure():
            res = (d_478_valueOrError4_).PropagateFailure()
            return res
        d_479_output_: MaterialWrapping.GenerateAndWrapOutput
        d_479_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_473_generateResponse_).Plaintext).value, ((d_473_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_473_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_479_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens

class KmsWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsWrapInfo.default()))()
        d_480_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_480_suite_ = (input).algorithmSuite
        d_481_stringifiedEncCtx_: _dafny.Map
        d_482_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_482_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_482_valueOrError0_).IsFailure():
            res = (d_482_valueOrError0_).PropagateFailure()
            return res
        d_481_stringifiedEncCtx_ = (d_482_valueOrError0_).Extract()
        d_483_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_483_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__PlaintextType((input).plaintextMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_483_valueOrError1_).IsFailure():
            res = (d_483_valueOrError1_).PropagateFailure()
            return res
        d_484_encryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest
        d_484_encryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_481_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_485_maybeEncryptResponse_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = ((self).client).Encrypt(d_484_encryptRequest_)
        d_485_maybeEncryptResponse_ = out96_
        d_486_encryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse
        d_487_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse.default())()
        def lambda34_(d_488_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_488_e_)

        d_487_valueOrError2_ = (d_485_maybeEncryptResponse_).MapFailure(lambda34_)
        if (d_487_valueOrError2_).IsFailure():
            res = (d_487_valueOrError2_).PropagateFailure()
            return res
        d_486_encryptResponse_ = (d_487_valueOrError2_).Extract()
        d_489_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_489_valueOrError3_ = Wrappers.default__.Need((((d_486_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_486_encryptResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_489_valueOrError3_).IsFailure():
            res = (d_489_valueOrError3_).PropagateFailure()
            return res
        d_490_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_490_valueOrError4_ = Wrappers.default__.Need(((d_486_encryptResponse_).CiphertextBlob).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_490_valueOrError4_).IsFailure():
            res = (d_490_valueOrError4_).PropagateFailure()
            return res
        d_491_output_: MaterialWrapping.WrapOutput
        d_491_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_486_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_486_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_491_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens
