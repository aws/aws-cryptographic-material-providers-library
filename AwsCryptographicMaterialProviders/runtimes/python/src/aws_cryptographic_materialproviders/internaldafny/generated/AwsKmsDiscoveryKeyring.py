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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring

# Module: aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv155_ = arn
        pat_let_tv156_ = arn
        def lambda58_(source22_):
            if source22_.is_None:
                return True
            elif True:
                d_623___mcc_h0_ = source22_.value
                d_624_filter_ = d_623___mcc_h0_
                return (((d_624_filter_).partition) == ((pat_let_tv155_).partition)) and (((d_624_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv156_).account])))

        return (True) and (lambda58_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnDecrypt(self, input):
        out92_: Wrappers.Result
        out92_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out92_

    def OnEncrypt(self, input):
        out93_: Wrappers.Result
        out93_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out93_

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
        d_625_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_625_materials_ = (input).materials
        d_626_encryptedDataKeys_: _dafny.Seq
        d_626_encryptedDataKeys_ = (input).encryptedDataKeys
        d_627_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_627_suite_ = ((input).materials).algorithmSuite
        d_628_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_628_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_625_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_628_valueOrError0_).IsFailure():
            res = (d_628_valueOrError0_).PropagateFailure()
            return res
        d_629_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_629_edkFilter_ = nw9_
        d_630_matchingEdks_: _dafny.Seq
        d_631_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out94_: Wrappers.Result
        out94_ = Actions.default__.FilterWithResult(d_629_edkFilter_, d_626_encryptedDataKeys_)
        d_631_valueOrError1_ = out94_
        if (d_631_valueOrError1_).IsFailure():
            res = (d_631_valueOrError1_).PropagateFailure()
            return res
        d_630_matchingEdks_ = (d_631_valueOrError1_).Extract()
        d_632_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_632_edkTransform_ = nw10_
        d_633_edksToAttempt_: _dafny.Seq
        d_634_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out95_: Wrappers.Result
        out95_ = Actions.default__.DeterministicFlatMapWithResult(d_632_edkTransform_, d_630_matchingEdks_)
        d_634_valueOrError2_ = out95_
        if (d_634_valueOrError2_).IsFailure():
            res = (d_634_valueOrError2_).PropagateFailure()
            return res
        d_633_edksToAttempt_ = (d_634_valueOrError2_).Extract()
        d_635_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_635_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_633_edksToAttempt_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_635_valueOrError3_).IsFailure():
            res = (d_635_valueOrError3_).PropagateFailure()
            return res
        d_636_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_625_materials_, (self).client, (self).grantTokens)
        d_636_decryptAction_ = nw11_
        d_637_outcome_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = Actions.default__.ReduceToSuccess(d_636_decryptAction_, d_633_edksToAttempt_)
        d_637_outcome_ = out96_
        def lambda59_(source23_):
            if source23_.is_Success:
                d_638___mcc_h0_ = source23_.value
                d_639_mat_ = d_638___mcc_h0_
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_639_mat_))
            elif True:
                d_640___mcc_h1_ = source23_.error
                d_641_errors_ = d_640___mcc_h1_
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_641_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        res = lambda59_(d_637_outcome_)
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
        d_642_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_642_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_642_valueOrError0_).IsFailure():
            output = (d_642_valueOrError0_).PropagateFailure()
            return output
        d_643_keyId_: _dafny.Seq
        d_644_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_644_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_644_valueOrError1_).IsFailure():
            output = (d_644_valueOrError1_).PropagateFailure()
            return output
        d_643_keyId_ = (d_644_valueOrError1_).Extract()
        d_645_arn_: AwsArnParsing.AwsArn
        d_646_valueOrError2_: Wrappers.Result = None
        d_646_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_643_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_646_valueOrError2_).IsFailure():
            output = (d_646_valueOrError2_).PropagateFailure()
            return output
        d_645_arn_ = (d_646_valueOrError2_).Extract()
        d_647_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_647_valueOrError3_ = Wrappers.default__.Need((((d_645_arn_).resource).resourceType) == (_dafny.Seq("key")), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_647_valueOrError3_).IsFailure():
            output = (d_647_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_645_arn_, (self).discoveryFilter)):
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
        d_648_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_648_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_648_valueOrError0_).IsFailure():
            res = (d_648_valueOrError0_).PropagateFailure()
            return res
        d_649_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_649_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_649_valueOrError1_).IsFailure():
            res = (d_649_valueOrError1_).PropagateFailure()
            return res
        d_650_keyId_: _dafny.Seq
        d_651_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_651_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_651_valueOrError2_).IsFailure():
            res = (d_651_valueOrError2_).PropagateFailure()
            return res
        d_650_keyId_ = (d_651_valueOrError2_).Extract()
        d_652_arn_: AwsArnParsing.AwsArn
        d_653_valueOrError3_: Wrappers.Result = None
        d_653_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_650_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_653_valueOrError3_).IsFailure():
            res = (d_653_valueOrError3_).PropagateFailure()
            return res
        d_652_arn_ = (d_653_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_652_arn_)]))
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
        d_654_awsKmsKey_: _dafny.Seq
        d_654_awsKmsKey_ = ((helper).arn).ToString()
        d_655___v0_: tuple
        d_656_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_656_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_656_valueOrError0_).IsFailure():
            res = (d_656_valueOrError0_).PropagateFailure()
            return res
        d_655___v0_ = (d_656_valueOrError0_).Extract()
        d_657_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_654_awsKmsKey_, (self).grantTokens)
        d_657_kmsUnwrap_ = nw12_
        d_658_unwrapOutputRes_: Wrappers.Result
        out97_: Wrappers.Result
        out97_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_657_kmsUnwrap_)
        d_658_unwrapOutputRes_ = out97_
        d_659_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_660_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_660_valueOrError1_ = d_658_unwrapOutputRes_
        if (d_660_valueOrError1_).IsFailure():
            res = (d_660_valueOrError1_).PropagateFailure()
            return res
        d_659_unwrapOutput_ = (d_660_valueOrError1_).Extract()
        d_661_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_662_valueOrError2_: Wrappers.Result = None
        d_662_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_659_unwrapOutput_).plaintextDataKey, (d_659_unwrapOutput_).symmetricSigningKey)
        if (d_662_valueOrError2_).IsFailure():
            res = (d_662_valueOrError2_).PropagateFailure()
            return res
        d_661_result_ = (d_662_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_661_result_)
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
