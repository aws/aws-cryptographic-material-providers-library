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

# Module: AwsKmsDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv165_ = arn
        pat_let_tv166_ = arn
        def lambda64_():
            source23_ = discoveryFilter
            unmatched23 = True
            if unmatched23:
                if source23_.is_Some:
                    d_656_filter_ = source23_.value
                    unmatched23 = False
                    return (((d_656_filter_).partition) == ((pat_let_tv165_).partition)) and (((d_656_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv166_).account])))
            if unmatched23:
                unmatched23 = False
                return True
            raise Exception("unexpected control point")

        return (True) and (lambda64_())


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnDecrypt(self, input):
        out94_: Wrappers.Result
        out94_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out94_

    def OnEncrypt(self, input):
        out95_: Wrappers.Result
        out95_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out95_

    def ctor__(self, client, discoveryFilter, grantTokens):
        (self)._i_client = client
        (self)._i_discoveryFilter = discoveryFilter
        (self)._i_grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_657_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_657_materials_ = (input).materials
        d_658_encryptedDataKeys_: _dafny.Seq
        d_658_encryptedDataKeys_ = (input).encryptedDataKeys
        d_659_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_659_suite_ = ((input).materials).algorithmSuite
        d_660_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_660_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_657_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_660_valueOrError0_).IsFailure():
            res = (d_660_valueOrError0_).PropagateFailure()
            return res
        d_661_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_661_edkFilter_ = nw9_
        d_662_matchingEdks_: _dafny.Seq
        d_663_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out96_: Wrappers.Result
        out96_ = Actions.default__.FilterWithResult(d_661_edkFilter_, d_658_encryptedDataKeys_)
        d_663_valueOrError1_ = out96_
        if (d_663_valueOrError1_).IsFailure():
            res = (d_663_valueOrError1_).PropagateFailure()
            return res
        d_662_matchingEdks_ = (d_663_valueOrError1_).Extract()
        d_664_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_664_edkTransform_ = nw10_
        d_665_edksToAttempt_: _dafny.Seq
        d_666_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out97_: Wrappers.Result
        out97_ = Actions.default__.DeterministicFlatMapWithResult(d_664_edkTransform_, d_662_matchingEdks_)
        d_666_valueOrError2_ = out97_
        if (d_666_valueOrError2_).IsFailure():
            res = (d_666_valueOrError2_).PropagateFailure()
            return res
        d_665_edksToAttempt_ = (d_666_valueOrError2_).Extract()
        if (0) == (len(d_665_edksToAttempt_)):
            d_667_errorMessage_: _dafny.Seq
            d_668_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_668_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_668_valueOrError3_).IsFailure():
                res = (d_668_valueOrError3_).PropagateFailure()
                return res
            d_667_errorMessage_ = (d_668_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_667_errorMessage_))
            return res
        d_669_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_657_materials_, (self).client, (self).grantTokens)
        d_669_decryptAction_ = nw11_
        d_670_outcome_: Wrappers.Result
        out98_: Wrappers.Result
        out98_ = Actions.default__.ReduceToSuccess(d_669_decryptAction_, d_665_edksToAttempt_)
        d_670_outcome_ = out98_
        def lambda65_():
            source24_ = d_670_outcome_
            unmatched24 = True
            if unmatched24:
                if source24_.is_Success:
                    d_671_mat_ = source24_.value
                    unmatched24 = False
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_671_mat_))
            if unmatched24:
                d_672_errors_ = source24_.error
                unmatched24 = False
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_672_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
            raise Exception("unexpected control point")

        res = lambda65_()
        return res
        return res

    @property
    def client(self):
        return self._i_client
    @property
    def discoveryFilter(self):
        return self._i_discoveryFilter
    @property
    def grantTokens(self):
        return self._i_grantTokens

class AwsKmsEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._i_discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter"
    def ctor__(self, discoveryFilter):
        (self)._i_discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_673_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_673_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_673_valueOrError0_).IsFailure():
            output = (d_673_valueOrError0_).PropagateFailure()
            return output
        d_674_keyId_: _dafny.Seq
        d_675_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_675_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_675_valueOrError1_).IsFailure():
            output = (d_675_valueOrError1_).PropagateFailure()
            return output
        d_674_keyId_ = (d_675_valueOrError1_).Extract()
        d_676_arn_: AwsArnParsing.AwsArn
        d_677_valueOrError2_: Wrappers.Result = None
        d_677_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_674_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_677_valueOrError2_).IsFailure():
            output = (d_677_valueOrError2_).PropagateFailure()
            return output
        d_676_arn_ = (d_677_valueOrError2_).Extract()
        d_678_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_678_valueOrError3_ = Wrappers.default__.Need((((d_676_arn_).resource).resourceType) == (_dafny.Seq("key")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_678_valueOrError3_).IsFailure():
            output = (d_678_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_676_arn_, (self).discoveryFilter)):
            output = Wrappers.Result_Success(False)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @property
    def discoveryFilter(self):
        return self._i_discoveryFilter

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
        d_679_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_679_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_679_valueOrError0_).IsFailure():
            res = (d_679_valueOrError0_).PropagateFailure()
            return res
        d_680_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_680_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_680_valueOrError1_).IsFailure():
            res = (d_680_valueOrError1_).PropagateFailure()
            return res
        d_681_keyId_: _dafny.Seq
        d_682_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_682_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_682_valueOrError2_).IsFailure():
            res = (d_682_valueOrError2_).PropagateFailure()
            return res
        d_681_keyId_ = (d_682_valueOrError2_).Extract()
        d_683_arn_: AwsArnParsing.AwsArn
        d_684_valueOrError3_: Wrappers.Result = None
        d_684_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_681_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_684_valueOrError3_).IsFailure():
            res = (d_684_valueOrError3_).PropagateFailure()
            return res
        d_683_arn_ = (d_684_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_683_arn_)]))
        return res
        return res


class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, grantTokens):
        (self)._i_materials = materials
        (self)._i_client = client
        (self)._i_grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_685_awsKmsKey_: _dafny.Seq
        d_685_awsKmsKey_ = ((helper).arn).ToString()
        d_686___v0_: tuple
        d_687_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_687_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_687_valueOrError0_).IsFailure():
            res = (d_687_valueOrError0_).PropagateFailure()
            return res
        d_686___v0_ = (d_687_valueOrError0_).Extract()
        d_688_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_685_awsKmsKey_, (self).grantTokens)
        d_688_kmsUnwrap_ = nw12_
        d_689_unwrapOutputRes_: Wrappers.Result
        out99_: Wrappers.Result
        out99_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_688_kmsUnwrap_)
        d_689_unwrapOutputRes_ = out99_
        d_690_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_691_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_691_valueOrError1_ = d_689_unwrapOutputRes_
        if (d_691_valueOrError1_).IsFailure():
            res = (d_691_valueOrError1_).PropagateFailure()
            return res
        d_690_unwrapOutput_ = (d_691_valueOrError1_).Extract()
        d_692_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_693_valueOrError2_: Wrappers.Result = None
        d_693_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_690_unwrapOutput_).plaintextDataKey, (d_690_unwrapOutput_).symmetricSigningKey)
        if (d_693_valueOrError2_).IsFailure():
            res = (d_693_valueOrError2_).PropagateFailure()
            return res
        d_692_result_ = (d_693_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_692_result_)
        return res
        return res

    @property
    def materials(self):
        return self._i_materials
    @property
    def client(self):
        return self._i_client
    @property
    def grantTokens(self):
        return self._i_grantTokens
