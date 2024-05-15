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

# Module: aws_cryptographic_materialproviders.internaldafny.generated.GetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        d_226_branchKeyItem_: _dafny.Map
        d_227_valueOrError0_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_227_valueOrError0_ = out29_
        if (d_227_valueOrError0_).IsFailure():
            output = (d_227_valueOrError0_).PropagateFailure()
            return output
        d_226_branchKeyItem_ = (d_227_valueOrError0_).Extract()
        d_228_encryptionContext_: _dafny.Map
        d_228_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_226_branchKeyItem_, logicalKeyStoreName)
        d_229_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_229_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_228_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_229_valueOrError1_).IsFailure():
            output = (d_229_valueOrError1_).PropagateFailure()
            return output
        d_230_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_231_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out30_: Wrappers.Result
        out30_ = KMSKeystoreOperations.default__.DecryptKey(d_228_encryptionContext_, d_226_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_231_valueOrError2_ = out30_
        if (d_231_valueOrError2_).IsFailure():
            output = (d_231_valueOrError2_).PropagateFailure()
            return output
        d_230_branchKey_ = (d_231_valueOrError2_).Extract()
        d_232_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_233_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_233_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_228_encryptionContext_, ((d_230_branchKey_).Plaintext).value)
        if (d_233_valueOrError3_).IsFailure():
            output = (d_233_valueOrError3_).PropagateFailure()
            return output
        d_232_branchKeyMaterials_ = (d_233_valueOrError3_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_232_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        d_234_branchKeyItem_: _dafny.Map
        d_235_valueOrError0_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_235_valueOrError0_ = out31_
        if (d_235_valueOrError0_).IsFailure():
            output = (d_235_valueOrError0_).PropagateFailure()
            return output
        d_234_branchKeyItem_ = (d_235_valueOrError0_).Extract()
        d_236_encryptionContext_: _dafny.Map
        d_236_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_234_branchKeyItem_, logicalKeyStoreName)
        d_237_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_237_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_236_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_237_valueOrError1_).IsFailure():
            output = (d_237_valueOrError1_).PropagateFailure()
            return output
        d_238_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_239_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out32_: Wrappers.Result
        out32_ = KMSKeystoreOperations.default__.DecryptKey(d_236_encryptionContext_, d_234_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_239_valueOrError2_ = out32_
        if (d_239_valueOrError2_).IsFailure():
            output = (d_239_valueOrError2_).PropagateFailure()
            return output
        d_238_branchKey_ = (d_239_valueOrError2_).Extract()
        d_240_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_241_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_241_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_236_encryptionContext_, ((d_238_branchKey_).Plaintext).value)
        if (d_241_valueOrError3_).IsFailure():
            output = (d_241_valueOrError3_).PropagateFailure()
            return output
        d_240_branchKeyMaterials_ = (d_241_valueOrError3_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_240_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        d_242_branchKeyItem_: _dafny.Map
        d_243_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_243_valueOrError0_ = out33_
        if (d_243_valueOrError0_).IsFailure():
            output = (d_243_valueOrError0_).PropagateFailure()
            return output
        d_242_branchKeyItem_ = (d_243_valueOrError0_).Extract()
        d_244_encryptionContext_: _dafny.Map
        d_244_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_242_branchKeyItem_, logicalKeyStoreName)
        d_245_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_245_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_244_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_245_valueOrError1_).IsFailure():
            output = (d_245_valueOrError1_).PropagateFailure()
            return output
        d_246_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_247_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out34_: Wrappers.Result
        out34_ = KMSKeystoreOperations.default__.DecryptKey(d_244_encryptionContext_, d_242_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_247_valueOrError2_ = out34_
        if (d_247_valueOrError2_).IsFailure():
            output = (d_247_valueOrError2_).PropagateFailure()
            return output
        d_246_branchKey_ = (d_247_valueOrError2_).Extract()
        d_248_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BeaconKeyMaterials
        d_249_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.default())()
        d_249_valueOrError3_ = Structure.default__.ToBeaconKeyMaterials(d_244_encryptionContext_, ((d_246_branchKey_).Plaintext).value)
        if (d_249_valueOrError3_).IsFailure():
            output = (d_249_valueOrError3_).PropagateFailure()
            return output
        d_248_branchKeyMaterials_ = (d_249_valueOrError3_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput_GetBeaconKeyOutput(d_248_branchKeyMaterials_))
        return output
        return output

