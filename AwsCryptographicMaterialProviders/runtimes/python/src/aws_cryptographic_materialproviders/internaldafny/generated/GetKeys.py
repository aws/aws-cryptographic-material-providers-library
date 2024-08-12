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

# Module: GetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        d_243_branchKeyItem_: _dafny.Map
        d_244_valueOrError0_: Wrappers.Result = None
        out30_: Wrappers.Result
        out30_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_244_valueOrError0_ = out30_
        if (d_244_valueOrError0_).IsFailure():
            output = (d_244_valueOrError0_).PropagateFailure()
            return output
        d_243_branchKeyItem_ = (d_244_valueOrError0_).Extract()
        d_245_encryptionContext_: _dafny.Map
        d_245_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_243_branchKeyItem_, logicalKeyStoreName)
        d_246_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_246_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_245_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_246_valueOrError1_).IsFailure():
            output = (d_246_valueOrError1_).PropagateFailure()
            return output
        d_247_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_247_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_245_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))
        if (d_247_valueOrError2_).IsFailure():
            output = (d_247_valueOrError2_).PropagateFailure()
            return output
        d_248_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_249_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out31_: Wrappers.Result
        out31_ = KMSKeystoreOperations.default__.DecryptKey(d_245_encryptionContext_, d_243_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_249_valueOrError3_ = out31_
        if (d_249_valueOrError3_).IsFailure():
            output = (d_249_valueOrError3_).PropagateFailure()
            return output
        d_248_branchKey_ = (d_249_valueOrError3_).Extract()
        d_250_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_251_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_251_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_245_encryptionContext_, ((d_248_branchKey_).Plaintext).value)
        if (d_251_valueOrError4_).IsFailure():
            output = (d_251_valueOrError4_).PropagateFailure()
            return output
        d_250_branchKeyMaterials_ = (d_251_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_250_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        d_252_branchKeyItem_: _dafny.Map
        d_253_valueOrError0_: Wrappers.Result = None
        out32_: Wrappers.Result
        out32_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_253_valueOrError0_ = out32_
        if (d_253_valueOrError0_).IsFailure():
            output = (d_253_valueOrError0_).PropagateFailure()
            return output
        d_252_branchKeyItem_ = (d_253_valueOrError0_).Extract()
        d_254_encryptionContext_: _dafny.Map
        d_254_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_252_branchKeyItem_, logicalKeyStoreName)
        d_255_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_255_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_254_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_255_valueOrError1_).IsFailure():
            output = (d_255_valueOrError1_).PropagateFailure()
            return output
        d_256_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_256_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_254_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_256_valueOrError2_).IsFailure():
            output = (d_256_valueOrError2_).PropagateFailure()
            return output
        d_257_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_258_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out33_: Wrappers.Result
        out33_ = KMSKeystoreOperations.default__.DecryptKey(d_254_encryptionContext_, d_252_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_258_valueOrError3_ = out33_
        if (d_258_valueOrError3_).IsFailure():
            output = (d_258_valueOrError3_).PropagateFailure()
            return output
        d_257_branchKey_ = (d_258_valueOrError3_).Extract()
        d_259_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_260_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_260_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_254_encryptionContext_, ((d_257_branchKey_).Plaintext).value)
        if (d_260_valueOrError4_).IsFailure():
            output = (d_260_valueOrError4_).PropagateFailure()
            return output
        d_259_branchKeyMaterials_ = (d_260_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_259_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        d_261_branchKeyItem_: _dafny.Map
        d_262_valueOrError0_: Wrappers.Result = None
        out34_: Wrappers.Result
        out34_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_262_valueOrError0_ = out34_
        if (d_262_valueOrError0_).IsFailure():
            output = (d_262_valueOrError0_).PropagateFailure()
            return output
        d_261_branchKeyItem_ = (d_262_valueOrError0_).Extract()
        d_263_encryptionContext_: _dafny.Map
        d_263_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_261_branchKeyItem_, logicalKeyStoreName)
        d_264_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_264_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_263_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_264_valueOrError1_).IsFailure():
            output = (d_264_valueOrError1_).PropagateFailure()
            return output
        d_265_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_265_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_263_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_265_valueOrError2_).IsFailure():
            output = (d_265_valueOrError2_).PropagateFailure()
            return output
        d_266_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_267_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out35_: Wrappers.Result
        out35_ = KMSKeystoreOperations.default__.DecryptKey(d_263_encryptionContext_, d_261_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_267_valueOrError3_ = out35_
        if (d_267_valueOrError3_).IsFailure():
            output = (d_267_valueOrError3_).PropagateFailure()
            return output
        d_266_branchKey_ = (d_267_valueOrError3_).Extract()
        d_268_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BeaconKeyMaterials
        d_269_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.default())()
        d_269_valueOrError4_ = Structure.default__.ToBeaconKeyMaterials(d_263_encryptionContext_, ((d_266_branchKey_).Plaintext).value)
        if (d_269_valueOrError4_).IsFailure():
            output = (d_269_valueOrError4_).PropagateFailure()
            return output
        d_268_branchKeyMaterials_ = (d_269_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput_GetBeaconKeyOutput(d_268_branchKeyMaterials_))
        return output
        return output

