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

# Module: GetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        d_240_branchKeyItem_: _dafny.Map
        d_241_valueOrError0_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_241_valueOrError0_ = out29_
        if (d_241_valueOrError0_).IsFailure():
            output = (d_241_valueOrError0_).PropagateFailure()
            return output
        d_240_branchKeyItem_ = (d_241_valueOrError0_).Extract()
        d_242_encryptionContext_: _dafny.Map
        d_242_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_240_branchKeyItem_, logicalKeyStoreName)
        d_243_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_243_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_242_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_243_valueOrError1_).IsFailure():
            output = (d_243_valueOrError1_).PropagateFailure()
            return output
        d_244_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_244_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_242_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))
        if (d_244_valueOrError2_).IsFailure():
            output = (d_244_valueOrError2_).PropagateFailure()
            return output
        d_245_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_246_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out30_: Wrappers.Result
        out30_ = KMSKeystoreOperations.default__.DecryptKey(d_242_encryptionContext_, d_240_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_246_valueOrError3_ = out30_
        if (d_246_valueOrError3_).IsFailure():
            output = (d_246_valueOrError3_).PropagateFailure()
            return output
        d_245_branchKey_ = (d_246_valueOrError3_).Extract()
        d_247_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_248_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_248_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_242_encryptionContext_, ((d_245_branchKey_).Plaintext).value)
        if (d_248_valueOrError4_).IsFailure():
            output = (d_248_valueOrError4_).PropagateFailure()
            return output
        d_247_branchKeyMaterials_ = (d_248_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_247_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        d_249_branchKeyItem_: _dafny.Map
        d_250_valueOrError0_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_250_valueOrError0_ = out31_
        if (d_250_valueOrError0_).IsFailure():
            output = (d_250_valueOrError0_).PropagateFailure()
            return output
        d_249_branchKeyItem_ = (d_250_valueOrError0_).Extract()
        d_251_encryptionContext_: _dafny.Map
        d_251_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_249_branchKeyItem_, logicalKeyStoreName)
        d_252_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_252_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_251_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_252_valueOrError1_).IsFailure():
            output = (d_252_valueOrError1_).PropagateFailure()
            return output
        d_253_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_253_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_251_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_253_valueOrError2_).IsFailure():
            output = (d_253_valueOrError2_).PropagateFailure()
            return output
        d_254_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_255_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out32_: Wrappers.Result
        out32_ = KMSKeystoreOperations.default__.DecryptKey(d_251_encryptionContext_, d_249_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_255_valueOrError3_ = out32_
        if (d_255_valueOrError3_).IsFailure():
            output = (d_255_valueOrError3_).PropagateFailure()
            return output
        d_254_branchKey_ = (d_255_valueOrError3_).Extract()
        d_256_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_257_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_257_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_251_encryptionContext_, ((d_254_branchKey_).Plaintext).value)
        if (d_257_valueOrError4_).IsFailure():
            output = (d_257_valueOrError4_).PropagateFailure()
            return output
        d_256_branchKeyMaterials_ = (d_257_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_256_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        d_258_branchKeyItem_: _dafny.Map
        d_259_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_259_valueOrError0_ = out33_
        if (d_259_valueOrError0_).IsFailure():
            output = (d_259_valueOrError0_).PropagateFailure()
            return output
        d_258_branchKeyItem_ = (d_259_valueOrError0_).Extract()
        d_260_encryptionContext_: _dafny.Map
        d_260_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_258_branchKeyItem_, logicalKeyStoreName)
        d_261_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_261_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_260_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_261_valueOrError1_).IsFailure():
            output = (d_261_valueOrError1_).PropagateFailure()
            return output
        d_262_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_262_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_260_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_262_valueOrError2_).IsFailure():
            output = (d_262_valueOrError2_).PropagateFailure()
            return output
        d_263_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_264_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out34_: Wrappers.Result
        out34_ = KMSKeystoreOperations.default__.DecryptKey(d_260_encryptionContext_, d_258_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_264_valueOrError3_ = out34_
        if (d_264_valueOrError3_).IsFailure():
            output = (d_264_valueOrError3_).PropagateFailure()
            return output
        d_263_branchKey_ = (d_264_valueOrError3_).Extract()
        d_265_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BeaconKeyMaterials
        d_266_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.default())()
        d_266_valueOrError4_ = Structure.default__.ToBeaconKeyMaterials(d_260_encryptionContext_, ((d_263_branchKey_).Plaintext).value)
        if (d_266_valueOrError4_).IsFailure():
            output = (d_266_valueOrError4_).PropagateFailure()
            return output
        d_265_branchKeyMaterials_ = (d_266_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput_GetBeaconKeyOutput(d_265_branchKeyMaterials_))
        return output
        return output

