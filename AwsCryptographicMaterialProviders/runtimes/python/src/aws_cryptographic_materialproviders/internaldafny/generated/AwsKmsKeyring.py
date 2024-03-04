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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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

# Module: AwsKmsKeyring


class AwsKmsKeyring(Keyring.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring):
    def  __init__(self):
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.AwsKmsKeyring"
    def OnEncrypt(self, input):
        out81_: Wrappers.Result
        out81_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnEncrypt(self, input)
        return out81_

    def OnDecrypt(self, input):
        out82_: Wrappers.Result
        out82_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnDecrypt(self, input)
        return out82_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_501_parsedAwsKmsId_: Wrappers.Result
        d_501_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_501_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_502_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
        d_502_materials_ = (input).materials
        d_503_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_503_suite_ = ((input).materials).algorithmSuite
        d_504_stringifiedEncCtx_: _dafny.Map
        d_505_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_505_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_505_valueOrError0_).IsFailure():
            res = (d_505_valueOrError0_).PropagateFailure()
            return res
        d_504_stringifiedEncCtx_ = (d_505_valueOrError0_).Extract()
        d_506_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw1_ = KmsGenerateAndWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_506_kmsGenerateAndWrap_ = nw1_
        d_507_kmsWrap_: KmsWrapKeyMaterial
        nw2_ = KmsWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_507_kmsWrap_ = nw2_
        d_508_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_509_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out83_: Wrappers.Result
        out83_ = EdkWrapping.default__.WrapEdkMaterial(d_502_materials_, d_507_kmsWrap_, d_506_kmsGenerateAndWrap_)
        d_509_valueOrError1_ = out83_
        if (d_509_valueOrError1_).IsFailure():
            res = (d_509_valueOrError1_).PropagateFailure()
            return res
        d_508_wrapOutput_ = (d_509_valueOrError1_).Extract()
        d_510_kmsKeyArn_: _dafny.Seq
        d_510_kmsKeyArn_ = ((d_508_wrapOutput_).wrapInfo).kmsKeyArn
        d_511_symmetricSigningKeyList_: Wrappers.Option
        d_511_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_508_wrapOutput_).symmetricSigningKey).value])) if ((d_508_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_512_providerInfo_: _dafny.Seq
        d_513_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_513_valueOrError2_ = (UTF8.default__.Encode(d_510_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_513_valueOrError2_).IsFailure():
            res = (d_513_valueOrError2_).PropagateFailure()
            return res
        d_512_providerInfo_ = (d_513_valueOrError2_).Extract()
        d_514_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_514_valueOrError3_ = Wrappers.default__.Need((len(d_512_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_514_valueOrError3_).IsFailure():
            res = (d_514_valueOrError3_).PropagateFailure()
            return res
        d_515_edk_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey
        d_515_edk_ = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_512_providerInfo_, (d_508_wrapOutput_).wrappedMaterial)
        if (d_508_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_516_result_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
            d_517_valueOrError4_: Wrappers.Result = None
            d_517_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_502_materials_, (d_508_wrapOutput_).plaintextDataKey, _dafny.Seq([d_515_edk_]), d_511_symmetricSigningKeyList_)
            if (d_517_valueOrError4_).IsFailure():
                res = (d_517_valueOrError4_).PropagateFailure()
                return res
            d_516_result_ = (d_517_valueOrError4_).Extract()
            res = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput_OnEncryptOutput(d_516_result_))
            return res
        elif (d_508_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_518_result_: software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials
            d_519_valueOrError5_: Wrappers.Result = None
            d_519_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_502_materials_, _dafny.Seq([d_515_edk_]), d_511_symmetricSigningKeyList_)
            if (d_519_valueOrError5_).IsFailure():
                res = (d_519_valueOrError5_).PropagateFailure()
                return res
            d_518_result_ = (d_519_valueOrError5_).Extract()
            res = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput_OnEncryptOutput(d_518_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_520_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_520_materials_ = (input).materials
        d_521_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_521_suite_ = ((input).materials).algorithmSuite
        d_522_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_522_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_520_materials_), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_522_valueOrError0_).IsFailure():
            res = (d_522_valueOrError0_).PropagateFailure()
            return res
        d_523_filter_: OnDecryptEncryptedDataKeyFilter
        nw3_ = OnDecryptEncryptedDataKeyFilter()
        nw3_.ctor__((self).awsKmsKey)
        d_523_filter_ = nw3_
        d_524_edksToAttempt_: _dafny.Seq
        d_525_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out84_: Wrappers.Result
        out84_ = Actions.default__.FilterWithResult(d_523_filter_, (input).encryptedDataKeys)
        d_525_valueOrError1_ = out84_
        if (d_525_valueOrError1_).IsFailure():
            res = (d_525_valueOrError1_).PropagateFailure()
            return res
        d_524_edksToAttempt_ = (d_525_valueOrError1_).Extract()
        d_526_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_526_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_524_edksToAttempt_)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_526_valueOrError2_).IsFailure():
            res = (d_526_valueOrError2_).PropagateFailure()
            return res
        d_527_decryptClosure_: Actions.ActionWithResult
        nw4_ = DecryptSingleEncryptedDataKey()
        nw4_.ctor__(d_520_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_527_decryptClosure_ = nw4_
        d_528_outcome_: Wrappers.Result
        out85_: Wrappers.Result
        out85_ = Actions.default__.ReduceToSuccess(d_527_decryptClosure_, d_524_edksToAttempt_)
        d_528_outcome_ = out85_
        d_529_SealedDecryptionMaterials_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_530_valueOrError3_: Wrappers.Result = None
        def lambda53_(d_531_errors_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors(d_531_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_530_valueOrError3_ = (d_528_outcome_).MapFailure(lambda53_)
        if (d_530_valueOrError3_).IsFailure():
            res = (d_530_valueOrError3_).PropagateFailure()
            return res
        d_529_SealedDecryptionMaterials_ = (d_530_valueOrError3_).Extract()
        res = Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput_OnDecryptOutput(d_529_SealedDecryptionMaterials_))
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
            res = Wrappers.Result_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_532_keyId_: _dafny.Seq
        d_533_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_533_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_533_valueOrError0_).IsFailure():
            res = (d_533_valueOrError0_).PropagateFailure()
            return res
        d_532_keyId_ = (d_533_valueOrError0_).Extract()
        d_534___v0_: AwsArnParsing.AwsArn
        d_535_valueOrError1_: Wrappers.Result = None
        d_535_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_532_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_535_valueOrError1_).IsFailure():
            res = (d_535_valueOrError1_).PropagateFailure()
            return res
        d_534___v0_ = (d_535_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_532_keyId_))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials = None
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
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
        d_536_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw5_ = KmsUnwrapKeyMaterial()
        nw5_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_536_kmsUnwrap_ = nw5_
        d_537_unwrapOutputRes_: Wrappers.Result
        out86_: Wrappers.Result
        out86_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_536_kmsUnwrap_)
        d_537_unwrapOutputRes_ = out86_
        d_538_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_539_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_539_valueOrError0_ = d_537_unwrapOutputRes_
        if (d_539_valueOrError0_).IsFailure():
            res = (d_539_valueOrError0_).PropagateFailure()
            return res
        d_538_unwrapOutput_ = (d_539_valueOrError0_).Extract()
        d_540_result_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_541_valueOrError1_: Wrappers.Result = None
        d_541_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_538_unwrapOutput_).plaintextDataKey, (d_538_unwrapOutput_).symmetricSigningKey)
        if (d_541_valueOrError1_).IsFailure():
            res = (d_541_valueOrError1_).PropagateFailure()
            return res
        d_540_result_ = (d_541_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_540_result_)
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
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
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
        d_542_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_542_valueOrError0_ = Wrappers.default__.Need(software.amazon.cryptography.services.kms.internaldafny.types.default__.IsValid__CiphertextType((input).wrappedMaterial), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_542_valueOrError0_).IsFailure():
            res = (d_542_valueOrError0_).PropagateFailure()
            return res
        d_543_stringifiedEncCtx_: _dafny.Map
        d_544_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_544_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_544_valueOrError1_).IsFailure():
            res = (d_544_valueOrError1_).PropagateFailure()
            return res
        d_543_stringifiedEncCtx_ = (d_544_valueOrError1_).Extract()
        d_545_decryptRequest_: software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest
        d_545_decryptRequest_ = software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_543_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_546_maybeDecryptResponse_: Wrappers.Result
        out87_: Wrappers.Result
        out87_ = ((self).client).Decrypt(d_545_decryptRequest_)
        d_546_maybeDecryptResponse_ = out87_
        d_547_decryptResponse_: software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse
        d_548_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.default())()
        def lambda54_(d_549_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsKms(d_549_e_)

        d_548_valueOrError2_ = (d_546_maybeDecryptResponse_).MapFailure(lambda54_)
        if (d_548_valueOrError2_).IsFailure():
            res = (d_548_valueOrError2_).PropagateFailure()
            return res
        d_547_decryptResponse_ = (d_548_valueOrError2_).Extract()
        d_550_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_550_valueOrError3_ = Wrappers.default__.Need((((((d_547_decryptResponse_).KeyId).is_Some) and ((((d_547_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_547_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_547_decryptResponse_).Plaintext).value))), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_550_valueOrError3_).IsFailure():
            res = (d_550_valueOrError3_).PropagateFailure()
            return res
        d_551_output_: MaterialWrapping.UnwrapOutput
        d_551_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_547_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_551_output_)
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
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
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
        d_552_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_552_suite_ = (input).algorithmSuite
        d_553_stringifiedEncCtx_: _dafny.Map
        d_554_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_554_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_554_valueOrError0_).IsFailure():
            res = (d_554_valueOrError0_).PropagateFailure()
            return res
        d_553_stringifiedEncCtx_ = (d_554_valueOrError0_).Extract()
        d_555_generatorRequest_: software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyRequest
        d_555_generatorRequest_ = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_553_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_552_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_556_maybeGenerateResponse_: Wrappers.Result
        out88_: Wrappers.Result
        out88_ = ((self).client).GenerateDataKey(d_555_generatorRequest_)
        d_556_maybeGenerateResponse_ = out88_
        d_557_generateResponse_: software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse
        d_558_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse.default())()
        def lambda55_(d_559_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsKms(d_559_e_)

        d_558_valueOrError1_ = (d_556_maybeGenerateResponse_).MapFailure(lambda55_)
        if (d_558_valueOrError1_).IsFailure():
            res = (d_558_valueOrError1_).PropagateFailure()
            return res
        d_557_generateResponse_ = (d_558_valueOrError1_).Extract()
        d_560_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_560_valueOrError2_ = Wrappers.default__.Need((((d_557_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_557_generateResponse_).KeyId).value)).is_Success), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_560_valueOrError2_).IsFailure():
            res = (d_560_valueOrError2_).PropagateFailure()
            return res
        d_561_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_561_valueOrError3_ = Wrappers.default__.Need((((d_557_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_552_suite_)) == (len(((d_557_generateResponse_).Plaintext).value))), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_561_valueOrError3_).IsFailure():
            res = (d_561_valueOrError3_).PropagateFailure()
            return res
        d_562_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_562_valueOrError4_ = Wrappers.default__.Need((((d_557_generateResponse_).CiphertextBlob).is_Some) and (software.amazon.cryptography.services.kms.internaldafny.types.default__.IsValid__CiphertextType(((d_557_generateResponse_).CiphertextBlob).value)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_562_valueOrError4_).IsFailure():
            res = (d_562_valueOrError4_).PropagateFailure()
            return res
        d_563_output_: MaterialWrapping.GenerateAndWrapOutput
        d_563_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_557_generateResponse_).Plaintext).value, ((d_557_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_557_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_563_output_)
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
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
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
        d_564_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_564_suite_ = (input).algorithmSuite
        d_565_stringifiedEncCtx_: _dafny.Map
        d_566_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_566_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_566_valueOrError0_).IsFailure():
            res = (d_566_valueOrError0_).PropagateFailure()
            return res
        d_565_stringifiedEncCtx_ = (d_566_valueOrError0_).Extract()
        d_567_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_567_valueOrError1_ = Wrappers.default__.Need(software.amazon.cryptography.services.kms.internaldafny.types.default__.IsValid__PlaintextType((input).plaintextMaterial), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_567_valueOrError1_).IsFailure():
            res = (d_567_valueOrError1_).PropagateFailure()
            return res
        d_568_encryptRequest_: software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest
        d_568_encryptRequest_ = software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_565_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_569_maybeEncryptResponse_: Wrappers.Result
        out89_: Wrappers.Result
        out89_ = ((self).client).Encrypt(d_568_encryptRequest_)
        d_569_maybeEncryptResponse_ = out89_
        d_570_encryptResponse_: software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse
        d_571_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse.default())()
        def lambda56_(d_572_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsKms(d_572_e_)

        d_571_valueOrError2_ = (d_569_maybeEncryptResponse_).MapFailure(lambda56_)
        if (d_571_valueOrError2_).IsFailure():
            res = (d_571_valueOrError2_).PropagateFailure()
            return res
        d_570_encryptResponse_ = (d_571_valueOrError2_).Extract()
        d_573_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_573_valueOrError3_ = Wrappers.default__.Need((((d_570_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_570_encryptResponse_).KeyId).value)).is_Success), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_573_valueOrError3_).IsFailure():
            res = (d_573_valueOrError3_).PropagateFailure()
            return res
        d_574_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_574_valueOrError4_ = Wrappers.default__.Need(((d_570_encryptResponse_).CiphertextBlob).is_Some, software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_574_valueOrError4_).IsFailure():
            res = (d_574_valueOrError4_).PropagateFailure()
            return res
        d_575_output_: MaterialWrapping.WrapOutput
        d_575_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_570_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_570_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_575_output_)
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
