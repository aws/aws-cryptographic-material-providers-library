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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring

# Module: AwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextDigest(cryptoPrimitives, encryptionContext):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1024_canonicalEC_: _dafny.Seq
        d_1025_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1025_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_1025_valueOrError0_).IsFailure():
            output = (d_1025_valueOrError0_).PropagateFailure()
            return output
        d_1024_canonicalEC_ = (d_1025_valueOrError0_).Extract()
        d_1026_DigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_1026_DigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), d_1024_canonicalEC_)
        d_1027_maybeDigest_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = (cryptoPrimitives).Digest(d_1026_DigestInput_)
        d_1027_maybeDigest_ = out182_
        d_1028_digest_: _dafny.Seq
        d_1029_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda84_(d_1030_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1030_e_)

        d_1029_valueOrError1_ = (d_1027_maybeDigest_).MapFailure(lambda84_)
        if (d_1029_valueOrError1_).IsFailure():
            output = (d_1029_valueOrError1_).PropagateFailure()
            return output
        d_1028_digest_ = (d_1029_valueOrError1_).Extract()
        output = Wrappers.Result_Success(d_1028_digest_)
        return output
        return output

    @_dafny.classproperty
    def MIN__KMS__RSA__KEY__LEN(instance):
        return 2048

class AwsKmsRsaKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._i_client: Wrappers.Option = Wrappers.Option.default()()
        self._i_paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._i_awsKmsKey: _dafny.Seq = None
        self._i_publicKey: Wrappers.Option = Wrappers.Option.default()()
        self._i_awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.AwsKmsRsaKeyring"
    def OnDecrypt(self, input):
        out183_: Wrappers.Result
        out183_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out183_

    def OnEncrypt(self, input):
        out184_: Wrappers.Result
        out184_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out184_

    def ctor__(self, publicKey, awsKmsKey, paddingScheme, client, cryptoPrimitives, grantTokens):
        d_1031_parsedAwsKmsId_: Wrappers.Result
        d_1031_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._i_publicKey = publicKey
        (self)._i_awsKmsKey = awsKmsKey
        (self)._i_awsKmsArn = (d_1031_parsedAwsKmsId_).value
        (self)._i_paddingScheme = paddingScheme
        (self)._i_client = client
        (self)._i_cryptoPrimitives = cryptoPrimitives
        (self)._i_grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_1032_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1032_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")))
        if (d_1032_valueOrError0_).IsFailure():
            res = (d_1032_valueOrError0_).PropagateFailure()
            return res
        d_1033_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1033_valueOrError1_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_1033_valueOrError1_).IsFailure():
            res = (d_1033_valueOrError1_).PropagateFailure()
            return res
        d_1034_wrap_: KmsRsaWrapKeyMaterial
        nw39_ = KmsRsaWrapKeyMaterial()
        nw39_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1034_wrap_ = nw39_
        d_1035_generateAndWrap_: KmsRsaGenerateAndWrapKeyMaterial
        nw40_ = KmsRsaGenerateAndWrapKeyMaterial()
        nw40_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_1035_generateAndWrap_ = nw40_
        d_1036_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1037_valueOrError2_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsRsaWrapInfo.default()))()
        out185_: Wrappers.Result
        out185_ = EdkWrapping.default__.WrapEdkMaterial((input).materials, d_1034_wrap_, d_1035_generateAndWrap_)
        d_1037_valueOrError2_ = out185_
        if (d_1037_valueOrError2_).IsFailure():
            res = (d_1037_valueOrError2_).PropagateFailure()
            return res
        d_1036_wrapOutput_ = (d_1037_valueOrError2_).Extract()
        d_1038_symmetricSigningKeyList_: Wrappers.Option
        d_1038_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1036_wrapOutput_).symmetricSigningKey).value])) if ((d_1036_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1039_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1039_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.RSA__PROVIDER__ID, (UTF8.default__.Encode((self).awsKmsKey)).value, (d_1036_wrapOutput_).wrappedMaterial)
        d_1040_returnMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        if (d_1036_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1041_valueOrError3_: Wrappers.Result = None
            d_1041_valueOrError3_ = Materials.default__.EncryptionMaterialAddDataKey((input).materials, (d_1036_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1039_edk_]), d_1038_symmetricSigningKeyList_)
            if (d_1041_valueOrError3_).IsFailure():
                res = (d_1041_valueOrError3_).PropagateFailure()
                return res
            d_1040_returnMaterials_ = (d_1041_valueOrError3_).Extract()
        elif (d_1036_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1042_valueOrError4_: Wrappers.Result = None
            d_1042_valueOrError4_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys((input).materials, _dafny.Seq([d_1039_edk_]), d_1038_symmetricSigningKeyList_)
            if (d_1042_valueOrError4_).IsFailure():
                res = (d_1042_valueOrError4_).PropagateFailure()
                return res
            d_1040_returnMaterials_ = (d_1042_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1040_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1043_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1043_valueOrError0_ = Wrappers.default__.Need(((self).client).is_Some, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")))
        if (d_1043_valueOrError0_).IsFailure():
            res = (d_1043_valueOrError0_).PropagateFailure()
            return res
        d_1044_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1044_materials_ = (input).materials
        d_1045_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1045_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1044_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1045_valueOrError1_).IsFailure():
            res = (d_1045_valueOrError1_).PropagateFailure()
            return res
        d_1046_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1046_valueOrError2_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_1046_valueOrError2_).IsFailure():
            res = (d_1046_valueOrError2_).PropagateFailure()
            return res
        d_1047_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw41_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw41_.ctor__((self).awsKmsArn, Constants.default__.RSA__PROVIDER__ID)
        d_1047_filter_ = nw41_
        d_1048_edksToAttempt_: _dafny.Seq
        d_1049_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out186_: Wrappers.Result
        out186_ = Actions.default__.FilterWithResult(d_1047_filter_, (input).encryptedDataKeys)
        d_1049_valueOrError3_ = out186_
        if (d_1049_valueOrError3_).IsFailure():
            res = (d_1049_valueOrError3_).PropagateFailure()
            return res
        d_1048_edksToAttempt_ = (d_1049_valueOrError3_).Extract()
        if (0) == (len(d_1048_edksToAttempt_)):
            d_1050_errorMessage_: _dafny.Seq
            d_1051_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1051_valueOrError4_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_1051_valueOrError4_).IsFailure():
                res = (d_1051_valueOrError4_).PropagateFailure()
                return res
            d_1050_errorMessage_ = (d_1051_valueOrError4_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_1050_errorMessage_))
            return res
        d_1052_encryptionContextDigest_: _dafny.Seq
        d_1053_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out187_: Wrappers.Result
        out187_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (d_1044_materials_).encryptionContext)
        d_1053_valueOrError5_ = out187_
        if (d_1053_valueOrError5_).IsFailure():
            res = (d_1053_valueOrError5_).PropagateFailure()
            return res
        d_1052_encryptionContextDigest_ = (d_1053_valueOrError5_).Extract()
        d_1054_decryptClosure_: Actions.ActionWithResult
        nw42_ = DecryptSingleAWSRSAEncryptedDataKey()
        nw42_.ctor__(d_1044_materials_, ((self).client).value, (self).awsKmsKey, (self).paddingScheme, d_1052_encryptionContextDigest_, (self).grantTokens)
        d_1054_decryptClosure_ = nw42_
        d_1055_outcome_: Wrappers.Result
        out188_: Wrappers.Result
        out188_ = Actions.default__.ReduceToSuccess(d_1054_decryptClosure_, d_1048_edksToAttempt_)
        d_1055_outcome_ = out188_
        d_1056_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1057_valueOrError6_: Wrappers.Result = None
        def lambda85_(d_1058_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1058_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1057_valueOrError6_ = (d_1055_outcome_).MapFailure(lambda85_)
        if (d_1057_valueOrError6_).IsFailure():
            res = (d_1057_valueOrError6_).PropagateFailure()
            return res
        d_1056_SealedDecryptionMaterials_ = (d_1057_valueOrError6_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1056_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
    @property
    def client(self):
        return self._i_client
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def awsKmsKey(self):
        return self._i_awsKmsKey
    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def awsKmsArn(self):
        return self._i_awsKmsArn
    @property
    def grantTokens(self):
        return self._i_grantTokens

class DecryptSingleAWSRSAEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_awsKmsKey: _dafny.Seq = None
        self._i_paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._i_encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        self._i_grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.DecryptSingleAWSRSAEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._i_materials = materials
        (self)._i_client = client
        (self)._i_awsKmsKey = awsKmsKey
        (self)._i_paddingScheme = paddingScheme
        (self)._i_encryptionContextDigest = encryptionContextDigest
        (self)._i_grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_1059_unwrap_: KmsRsaUnwrapKeyMaterial
        nw43_ = KmsRsaUnwrapKeyMaterial()
        nw43_.ctor__((self).client, (self).awsKmsKey, (self).paddingScheme, (self).encryptionContextDigest, (self).grantTokens)
        d_1059_unwrap_ = nw43_
        d_1060_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1061_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsRsaUnwrapInfo.default()))()
        out189_: Wrappers.Result
        out189_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1059_unwrap_)
        d_1061_valueOrError0_ = out189_
        if (d_1061_valueOrError0_).IsFailure():
            res = (d_1061_valueOrError0_).PropagateFailure()
            return res
        d_1060_unwrapOutput_ = (d_1061_valueOrError0_).Extract()
        d_1062_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1063_valueOrError1_: Wrappers.Result = None
        d_1063_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1060_unwrapOutput_).plaintextDataKey, (d_1060_unwrapOutput_).symmetricSigningKey)
        if (d_1063_valueOrError1_).IsFailure():
            res = (d_1063_valueOrError1_).PropagateFailure()
            return res
        d_1062_result_ = (d_1063_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_1062_result_)
        return res
        return res

    @property
    def materials(self):
        return self._i_materials
    @property
    def client(self):
        return self._i_client
    @property
    def awsKmsKey(self):
        return self._i_awsKmsKey
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._i_encryptionContextDigest
    @property
    def grantTokens(self):
        return self._i_grantTokens

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
        self._i_publicKey: _dafny.Seq = _dafny.Seq({})
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._i_paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._i_publicKey = publicKey
        (self)._i_cryptoPrimitives = cryptoPrimitives
        (self)._i_paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsRsaWrapInfo.default()))()
        d_1064_generateBytesResult_: Wrappers.Result
        out190_: Wrappers.Result
        out190_ = ((self).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1064_generateBytesResult_ = out190_
        d_1065_plaintextMaterial_: _dafny.Seq
        d_1066_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda86_(d_1067_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1067_e_)

        d_1066_valueOrError0_ = (d_1064_generateBytesResult_).MapFailure(lambda86_)
        if (d_1066_valueOrError0_).IsFailure():
            res = (d_1066_valueOrError0_).PropagateFailure()
            return res
        d_1065_plaintextMaterial_ = (d_1066_valueOrError0_).Extract()
        d_1068_wrap_: KmsRsaWrapKeyMaterial
        nw44_ = KmsRsaWrapKeyMaterial()
        nw44_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_1068_wrap_ = nw44_
        d_1069_wrapOutput_: MaterialWrapping.WrapOutput
        d_1070_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        out191_: Wrappers.Result
        out191_ = (d_1068_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1065_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1070_valueOrError1_ = out191_
        if (d_1070_valueOrError1_).IsFailure():
            res = (d_1070_valueOrError1_).PropagateFailure()
            return res
        d_1069_wrapOutput_ = (d_1070_valueOrError1_).Extract()
        d_1071_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1071_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1065_plaintextMaterial_, (d_1069_wrapOutput_).wrappedMaterial, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1071_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._i_paddingScheme

class KmsRsaWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_publicKey: _dafny.Seq = _dafny.Seq({})
        self._i_cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._i_paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._i_publicKey = publicKey
        (self)._i_cryptoPrimitives = cryptoPrimitives
        (self)._i_paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        d_1072_encryptionContextDigest_: _dafny.Seq
        d_1073_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out192_: Wrappers.Result
        out192_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (input).encryptionContext)
        d_1073_valueOrError0_ = out192_
        if (d_1073_valueOrError0_).IsFailure():
            res = (d_1073_valueOrError0_).PropagateFailure()
            return res
        d_1072_encryptionContextDigest_ = (d_1073_valueOrError0_).Extract()
        d_1074_padding_: AwsCryptographyPrimitivesTypes.RSAPaddingMode
        def lambda87_():
            source30_ = (self).paddingScheme
            unmatched30 = True
            if unmatched30:
                if source30_.is_RSAES__OAEP__SHA__1:
                    unmatched30 = False
                    return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA1()
            if unmatched30:
                unmatched30 = False
                return AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA256()
            raise Exception("unexpected control point")

        d_1074_padding_ = lambda87_()
        d_1075_RSAEncryptOutput_: Wrappers.Result
        out193_: Wrappers.Result
        out193_ = ((self).cryptoPrimitives).RSAEncrypt(AwsCryptographyPrimitivesTypes.RSAEncryptInput_RSAEncryptInput(d_1074_padding_, (self).publicKey, (d_1072_encryptionContextDigest_) + ((input).plaintextMaterial)))
        d_1075_RSAEncryptOutput_ = out193_
        d_1076_ciphertext_: _dafny.Seq
        d_1077_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda88_(d_1078_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1078_e_)

        d_1077_valueOrError1_ = (d_1075_RSAEncryptOutput_).MapFailure(lambda88_)
        if (d_1077_valueOrError1_).IsFailure():
            res = (d_1077_valueOrError1_).PropagateFailure()
            return res
        d_1076_ciphertext_ = (d_1077_valueOrError1_).Extract()
        d_1079_output_: MaterialWrapping.WrapOutput
        d_1079_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_1076_ciphertext_, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_1079_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._i_publicKey
    @property
    def cryptoPrimitives(self):
        return self._i_cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._i_paddingScheme

class KmsRsaUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._i_client: ComAmazonawsKmsTypes.IKMSClient = None
        self._i_grantTokens: _dafny.Seq = None
        self._i_awsKmsKey: _dafny.Seq = None
        self._i_paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._i_encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._i_client = client
        (self)._i_awsKmsKey = awsKmsKey
        (self)._i_paddingScheme = paddingScheme
        (self)._i_encryptionContextDigest = encryptionContextDigest
        (self)._i_grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(KmsRsaUnwrapInfo.default()))()
        d_1080_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1080_valueOrError0_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__CiphertextType((input).wrappedMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_1080_valueOrError0_).IsFailure():
            res = (d_1080_valueOrError0_).PropagateFailure()
            return res
        d_1081_decryptRequest_: ComAmazonawsKmsTypes.DecryptRequest
        d_1081_decryptRequest_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_Some((self).paddingScheme))
        d_1082_maybeDecryptResponse_: Wrappers.Result
        out194_: Wrappers.Result
        out194_ = ((self).client).Decrypt(d_1081_decryptRequest_)
        d_1082_maybeDecryptResponse_ = out194_
        d_1083_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_1084_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda89_(d_1085_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_1085_e_)

        d_1084_valueOrError1_ = (d_1082_maybeDecryptResponse_).MapFailure(lambda89_)
        if (d_1084_valueOrError1_).IsFailure():
            res = (d_1084_valueOrError1_).PropagateFailure()
            return res
        d_1083_decryptResponse_ = (d_1084_valueOrError1_).Extract()
        d_1086_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1086_valueOrError2_ = Wrappers.default__.Need(((((d_1083_decryptResponse_).KeyId).is_Some) and ((((d_1083_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_1083_decryptResponse_).Plaintext).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_1086_valueOrError2_).IsFailure():
            res = (d_1086_valueOrError2_).PropagateFailure()
            return res
        d_1087_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1087_valueOrError3_ = Wrappers.default__.Need((((self).encryptionContextDigest) <= (((d_1083_decryptResponse_).Plaintext).value)) and (((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) + (len((self).encryptionContextDigest))) == (len(((d_1083_decryptResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context digest does not match expected value.")))
        if (d_1087_valueOrError3_).IsFailure():
            res = (d_1087_valueOrError3_).PropagateFailure()
            return res
        d_1088_output_: MaterialWrapping.UnwrapOutput
        d_1088_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(_dafny.Seq((((d_1083_decryptResponse_).Plaintext).value)[len((self).encryptionContextDigest)::]), KmsRsaUnwrapInfo_KmsRsaUnwrapInfo())
        res = Wrappers.Result_Success(d_1088_output_)
        return res
        return res

    @property
    def client(self):
        return self._i_client
    @property
    def grantTokens(self):
        return self._i_grantTokens
    @property
    def awsKmsKey(self):
        return self._i_awsKmsKey
    @property
    def paddingScheme(self):
        return self._i_paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._i_encryptionContextDigest
