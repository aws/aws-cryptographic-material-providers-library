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

# Module: AwsKmsMrkDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToStringForRegion(arn, region):
        if AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn):
            return (arn).ToArnString(Wrappers.Option_Some(region))
        elif True:
            return (arn).ToString()

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter, region):
        pat_let_tv167_ = arn
        pat_let_tv168_ = arn
        def lambda66_():
            source25_ = discoveryFilter
            unmatched25 = True
            if unmatched25:
                if source25_.is_Some:
                    d_703_filter_ = source25_.value
                    unmatched25 = False
                    return (((d_703_filter_).partition) == ((pat_let_tv167_).partition)) and (((pat_let_tv168_).account) in ((d_703_filter_).accountIds))
            if unmatched25:
                unmatched25 = False
                return True
            raise Exception("unexpected control point")

        return (lambda66_()) and (((region) == ((arn).region) if not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn)) else True))


class AwsKmsMrkDiscoveryKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_region: _dafny.Seq = _dafny.Seq("")
        self._i_discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring"
    def OnDecrypt(self, input):
        out101_: Wrappers.Result
        out101_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out101_

    def OnEncrypt(self, input):
        out102_: Wrappers.Result
        out102_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out102_

    def ctor__(self, client, region, discoveryFilter, grantTokens):
        (self)._i_client = client
        (self)._i_region = region
        (self)._i_discoveryFilter = discoveryFilter
        (self)._i_grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_704_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_704_materials_ = (input).materials
        d_705_encryptedDataKeys_: _dafny.Seq
        d_705_encryptedDataKeys_ = (input).encryptedDataKeys
        d_706_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_706_suite_ = ((input).materials).algorithmSuite
        d_707_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_707_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_704_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_707_valueOrError0_).IsFailure():
            output = (d_707_valueOrError0_).PropagateFailure()
            return output
        d_708_edkFilterTransform_: AwsKmsEncryptedDataKeyFilterTransform
        nw15_ = AwsKmsEncryptedDataKeyFilterTransform()
        nw15_.ctor__((self).region, (self).discoveryFilter)
        d_708_edkFilterTransform_ = nw15_
        d_709_edksToAttempt_: _dafny.Seq
        d_710_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out103_: Wrappers.Result
        out103_ = Actions.default__.DeterministicFlatMapWithResult(d_708_edkFilterTransform_, d_705_encryptedDataKeys_)
        d_710_valueOrError1_ = out103_
        if (d_710_valueOrError1_).IsFailure():
            output = (d_710_valueOrError1_).PropagateFailure()
            return output
        d_709_edksToAttempt_ = (d_710_valueOrError1_).Extract()
        if (0) == (len(d_709_edksToAttempt_)):
            d_711_errorMessage_: _dafny.Seq
            d_712_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_712_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_712_valueOrError2_).IsFailure():
                output = (d_712_valueOrError2_).PropagateFailure()
                return output
            d_711_errorMessage_ = (d_712_valueOrError2_).Extract()
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_711_errorMessage_))
            return output
        d_713_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw16_ = AwsKmsEncryptedDataKeyDecryptor()
        nw16_.ctor__(d_704_materials_, (self).client, (self).region, (self).grantTokens)
        d_713_decryptAction_ = nw16_
        d_714_outcome_: Wrappers.Result
        out104_: Wrappers.Result
        out104_ = Actions.default__.ReduceToSuccess(d_713_decryptAction_, d_709_edksToAttempt_)
        d_714_outcome_ = out104_
        def lambda67_():
            source26_ = d_714_outcome_
            unmatched26 = True
            if unmatched26:
                if source26_.is_Success:
                    d_715_mat_ = source26_.value
                    unmatched26 = False
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_715_mat_))
            if unmatched26:
                d_716_errors_ = source26_.error
                unmatched26 = False
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_716_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
            raise Exception("unexpected control point")

        output = lambda67_()
        return output
        return output

    @property
    def client(self):
        return self._i_client
    @property
    def region(self):
        return self._i_region
    @property
    def discoveryFilter(self):
        return self._i_discoveryFilter
    @property
    def grantTokens(self):
        return self._i_grantTokens

class AwsKmsEncryptedDataKeyFilterTransform(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._i_region: _dafny.Seq = _dafny.Seq("")
        self._i_discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform"
    def ctor__(self, region, discoveryFilter):
        (self)._i_region = region
        (self)._i_discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        d_717_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_717_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_717_valueOrError0_).IsFailure():
            res = (d_717_valueOrError0_).PropagateFailure()
            return res
        d_718_keyId_: _dafny.Seq
        d_719_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda68_(d_720_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_720_e_)

        d_719_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(lambda68_)
        if (d_719_valueOrError1_).IsFailure():
            res = (d_719_valueOrError1_).PropagateFailure()
            return res
        d_718_keyId_ = (d_719_valueOrError1_).Extract()
        d_721_arn_: AwsArnParsing.AwsArn
        d_722_valueOrError2_: Wrappers.Result = None
        def lambda69_(d_723_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_723_e_)

        d_722_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_718_keyId_)).MapFailure(lambda69_)
        if (d_722_valueOrError2_).IsFailure():
            res = (d_722_valueOrError2_).PropagateFailure()
            return res
        d_721_arn_ = (d_722_valueOrError2_).Extract()
        d_724_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_724_valueOrError3_ = Wrappers.default__.Need((((d_721_arn_).resource).resourceType) == (_dafny.Seq("key")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_724_valueOrError3_).IsFailure():
            res = (d_724_valueOrError3_).PropagateFailure()
            return res
        if not(default__.DiscoveryMatch(d_721_arn_, (self).discoveryFilter, (self).region)):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_721_arn_)]))
        return res
        return res

    @property
    def region(self):
        return self._i_region
    @property
    def discoveryFilter(self):
        return self._i_discoveryFilter

class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_region: _dafny.Seq = _dafny.Seq("")
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, region, grantTokens):
        (self)._i_materials = materials
        (self)._i_client = client
        (self)._i_region = region
        (self)._i_grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_725_awsKmsKey_: _dafny.Seq
        d_725_awsKmsKey_ = default__.ToStringForRegion((helper).arn, (self).region)
        d_726___v0_: tuple
        d_727_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_727_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(d_725_awsKmsKey_)
        if (d_727_valueOrError0_).IsFailure():
            res = (d_727_valueOrError0_).PropagateFailure()
            return res
        d_726___v0_ = (d_727_valueOrError0_).Extract()
        d_728_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw17_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw17_.ctor__((self).client, d_725_awsKmsKey_, (self).grantTokens)
        d_728_kmsUnwrap_ = nw17_
        d_729_unwrapOutputRes_: Wrappers.Result
        out105_: Wrappers.Result
        out105_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_728_kmsUnwrap_)
        d_729_unwrapOutputRes_ = out105_
        d_730_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_731_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_731_valueOrError1_ = d_729_unwrapOutputRes_
        if (d_731_valueOrError1_).IsFailure():
            res = (d_731_valueOrError1_).PropagateFailure()
            return res
        d_730_unwrapOutput_ = (d_731_valueOrError1_).Extract()
        res = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_730_unwrapOutput_).plaintextDataKey, (d_730_unwrapOutput_).symmetricSigningKey)
        return res

    @property
    def materials(self):
        return self._i_materials
    @property
    def client(self):
        return self._i_client
    @property
    def region(self):
        return self._i_region
    @property
    def grantTokens(self):
        return self._i_grantTokens
