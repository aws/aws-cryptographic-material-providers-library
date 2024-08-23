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

# Module: AwsKmsDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv165_ = arn
        pat_let_tv166_ = arn
        def lambda65_():
            source23_ = discoveryFilter
            unmatched23 = True
            if unmatched23:
                if source23_.is_Some:
                    d_660_filter_ = source23_.value
                    unmatched23 = False
                    return (((d_660_filter_).partition) == ((pat_let_tv165_).partition)) and (((d_660_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv166_).account])))
            if unmatched23:
                unmatched23 = False
                return True
            raise Exception("unexpected control point")

        return (True) and (lambda65_())


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnDecrypt(self, input):
        out97_: Wrappers.Result
        out97_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out97_

    def OnEncrypt(self, input):
        out98_: Wrappers.Result
        out98_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out98_

    def ctor__(self, client, discoveryFilter, grantTokens):
        (self)._client = client
        (self)._discoveryFilter = discoveryFilter
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_661_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_661_materials_ = (input).materials
        d_662_encryptedDataKeys_: _dafny.Seq
        d_662_encryptedDataKeys_ = (input).encryptedDataKeys
        d_663_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_663_suite_ = ((input).materials).algorithmSuite
        d_664_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_664_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_661_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_664_valueOrError0_).IsFailure():
            res = (d_664_valueOrError0_).PropagateFailure()
            return res
        d_665_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_665_edkFilter_ = nw9_
        d_666_matchingEdks_: _dafny.Seq
        d_667_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out99_: Wrappers.Result
        out99_ = Actions.default__.FilterWithResult(d_665_edkFilter_, d_662_encryptedDataKeys_)
        d_667_valueOrError1_ = out99_
        if (d_667_valueOrError1_).IsFailure():
            res = (d_667_valueOrError1_).PropagateFailure()
            return res
        d_666_matchingEdks_ = (d_667_valueOrError1_).Extract()
        d_668_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_668_edkTransform_ = nw10_
        d_669_edksToAttempt_: _dafny.Seq
        d_670_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out100_: Wrappers.Result
        out100_ = Actions.default__.DeterministicFlatMapWithResult(d_668_edkTransform_, d_666_matchingEdks_)
        d_670_valueOrError2_ = out100_
        if (d_670_valueOrError2_).IsFailure():
            res = (d_670_valueOrError2_).PropagateFailure()
            return res
        d_669_edksToAttempt_ = (d_670_valueOrError2_).Extract()
        if (0) == (len(d_669_edksToAttempt_)):
            d_671_errorMessage_: _dafny.Seq
            d_672_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_672_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_672_valueOrError3_).IsFailure():
                res = (d_672_valueOrError3_).PropagateFailure()
                return res
            d_671_errorMessage_ = (d_672_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_671_errorMessage_))
            return res
        d_673_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_661_materials_, (self).client, (self).grantTokens)
        d_673_decryptAction_ = nw11_
        d_674_outcome_: Wrappers.Result
        out101_: Wrappers.Result
        out101_ = Actions.default__.ReduceToSuccess(d_673_decryptAction_, d_669_edksToAttempt_)
        d_674_outcome_ = out101_
        def lambda66_():
            source24_ = d_674_outcome_
            unmatched24 = True
            if unmatched24:
                if source24_.is_Success:
                    d_675_mat_ = source24_.value
                    unmatched24 = False
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_675_mat_))
            if unmatched24:
                d_676_errors_ = source24_.error
                unmatched24 = False
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_676_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
            raise Exception("unexpected control point")

        res = lambda66_()
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def discoveryFilter(self):
        return self._discoveryFilter
    @property
    def grantTokens(self):
        return self._grantTokens

class AwsKmsEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter"
    def ctor__(self, discoveryFilter):
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_677_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_677_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_677_valueOrError0_).IsFailure():
            output = (d_677_valueOrError0_).PropagateFailure()
            return output
        d_678_keyId_: _dafny.Seq
        d_679_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_679_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_679_valueOrError1_).IsFailure():
            output = (d_679_valueOrError1_).PropagateFailure()
            return output
        d_678_keyId_ = (d_679_valueOrError1_).Extract()
        d_680_arn_: AwsArnParsing.AwsArn
        d_681_valueOrError2_: Wrappers.Result = None
        d_681_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_678_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_681_valueOrError2_).IsFailure():
            output = (d_681_valueOrError2_).PropagateFailure()
            return output
        d_680_arn_ = (d_681_valueOrError2_).Extract()
        d_682_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_682_valueOrError3_ = Wrappers.default__.Need((((d_680_arn_).resource).resourceType) == (_dafny.Seq("key")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_682_valueOrError3_).IsFailure():
            output = (d_682_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_680_arn_, (self).discoveryFilter)):
            output = Wrappers.Result_Success(False)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @property
    def discoveryFilter(self):
        return self._discoveryFilter

class AwsKmsEncryptedDataKeyTransformer(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer"
    def ctor__(self):
        pass
        pass

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_683_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_683_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_683_valueOrError0_).IsFailure():
            res = (d_683_valueOrError0_).PropagateFailure()
            return res
        d_684_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_684_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_684_valueOrError1_).IsFailure():
            res = (d_684_valueOrError1_).PropagateFailure()
            return res
        d_685_keyId_: _dafny.Seq
        d_686_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_686_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_686_valueOrError2_).IsFailure():
            res = (d_686_valueOrError2_).PropagateFailure()
            return res
        d_685_keyId_ = (d_686_valueOrError2_).Extract()
        d_687_arn_: AwsArnParsing.AwsArn
        d_688_valueOrError3_: Wrappers.Result = None
        d_688_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_685_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_688_valueOrError3_).IsFailure():
            res = (d_688_valueOrError3_).PropagateFailure()
            return res
        d_687_arn_ = (d_688_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_687_arn_)]))
        return res
        return res


class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_689_awsKmsKey_: _dafny.Seq
        d_689_awsKmsKey_ = ((helper).arn).ToString()
        d_690___v0_: tuple
        d_691_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_691_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_691_valueOrError0_).IsFailure():
            res = (d_691_valueOrError0_).PropagateFailure()
            return res
        d_690___v0_ = (d_691_valueOrError0_).Extract()
        d_692_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_689_awsKmsKey_, (self).grantTokens)
        d_692_kmsUnwrap_ = nw12_
        d_693_unwrapOutputRes_: Wrappers.Result
        out102_: Wrappers.Result
        out102_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_692_kmsUnwrap_)
        d_693_unwrapOutputRes_ = out102_
        d_694_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_695_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_695_valueOrError1_ = d_693_unwrapOutputRes_
        if (d_695_valueOrError1_).IsFailure():
            res = (d_695_valueOrError1_).PropagateFailure()
            return res
        d_694_unwrapOutput_ = (d_695_valueOrError1_).Extract()
        d_696_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_697_valueOrError2_: Wrappers.Result = None
        d_697_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_694_unwrapOutput_).plaintextDataKey, (d_694_unwrapOutput_).symmetricSigningKey)
        if (d_697_valueOrError2_).IsFailure():
            res = (d_697_valueOrError2_).PropagateFailure()
            return res
        d_696_result_ = (d_697_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_696_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def grantTokens(self):
        return self._grantTokens
