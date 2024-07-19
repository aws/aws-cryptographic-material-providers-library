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

# Module: CreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBranchAndBeaconKeys(branchKeyIdentifier, customEncryptionContext, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        d_198_decryptOnlyEncryptionContext_: _dafny.Map
        d_198_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, KMSKeystoreOperations.default__.GetKeyId(kmsConfiguration), customEncryptionContext)
        d_199_activeEncryptionContext_: _dafny.Map
        d_199_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_198_decryptOnlyEncryptionContext_)
        d_200_beaconEncryptionContext_: _dafny.Map
        d_200_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_198_decryptOnlyEncryptionContext_)
        d_201_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_201_valueOrError0_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_198_decryptOnlyEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext in CreateBranchAndBeaconKeys.")))
        if (d_201_valueOrError0_).IsFailure():
            output = (d_201_valueOrError0_).PropagateFailure()
            return output
        d_202_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out18_: Wrappers.Result
        out18_ = KMSKeystoreOperations.default__.GenerateKey(d_198_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_202_valueOrError1_ = out18_
        if (d_202_valueOrError1_).IsFailure():
            output = (d_202_valueOrError1_).PropagateFailure()
            return output
        d_203_wrappedDecryptOnlyBranchKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_203_wrappedDecryptOnlyBranchKey_ = (d_202_valueOrError1_).Extract()
        d_204_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_204_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_199_activeEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for ReEncrypt in CreateBranchAndBeaconKeys.")))
        if (d_204_valueOrError2_).IsFailure():
            output = (d_204_valueOrError2_).PropagateFailure()
            return output
        d_205_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out19_: Wrappers.Result
        out19_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_203_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_198_decryptOnlyEncryptionContext_, d_199_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_205_valueOrError3_ = out19_
        if (d_205_valueOrError3_).IsFailure():
            output = (d_205_valueOrError3_).PropagateFailure()
            return output
        d_206_wrappedActiveBranchKey_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_206_wrappedActiveBranchKey_ = (d_205_valueOrError3_).Extract()
        d_207_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_207_valueOrError4_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_200_beaconEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext(beacon key) in CreateBranchAndBeaconKeys.")))
        if (d_207_valueOrError4_).IsFailure():
            output = (d_207_valueOrError4_).PropagateFailure()
            return output
        d_208_valueOrError5_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out20_: Wrappers.Result
        out20_ = KMSKeystoreOperations.default__.GenerateKey(d_200_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_208_valueOrError5_ = out20_
        if (d_208_valueOrError5_).IsFailure():
            output = (d_208_valueOrError5_).PropagateFailure()
            return output
        d_209_wrappedBeaconKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_209_wrappedBeaconKey_ = (d_208_valueOrError5_).Extract()
        d_210_decryptOnlyBranchKeyItem_: _dafny.Map
        d_210_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_198_decryptOnlyEncryptionContext_, ((d_203_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_211_activeBranchKeyItem_: _dafny.Map
        d_211_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_199_activeEncryptionContext_, ((d_206_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_212_beaconKeyItem_: _dafny.Map
        d_212_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_200_beaconEncryptionContext_, ((d_209_wrappedBeaconKey_).CiphertextBlob).value)
        d_213_valueOrError6_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        out21_: Wrappers.Result
        out21_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_210_decryptOnlyBranchKeyItem_, d_211_activeBranchKeyItem_, d_212_beaconKeyItem_, ddbTableName, ddbClient)
        d_213_valueOrError6_ = out21_
        if (d_213_valueOrError6_).IsFailure():
            output = (d_213_valueOrError6_).PropagateFailure()
            return output
        d_214___v0_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_214___v0_ = (d_213_valueOrError6_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        d_215_valueOrError0_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_215_valueOrError0_ = out22_
        if (d_215_valueOrError0_).IsFailure():
            output = (d_215_valueOrError0_).PropagateFailure()
            return output
        d_216_oldActiveItem_: _dafny.Map
        d_216_oldActiveItem_ = (d_215_valueOrError0_).Extract()
        d_217_oldActiveEncryptionContext_: _dafny.Map
        d_217_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_216_oldActiveItem_, logicalKeyStoreName)
        d_218_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_218_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_217_oldActiveEncryptionContext_)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.VERSION__KEY__KMS__KEY__ARN__DISAGREEMENT))
        if (d_218_valueOrError1_).IsFailure():
            output = (d_218_valueOrError1_).PropagateFailure()
            return output
        d_219_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out23_: Wrappers.Result
        out23_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_216_oldActiveItem_)[Structure.default__.BRANCH__KEY__FIELD]).B, d_217_oldActiveEncryptionContext_, d_217_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_219_valueOrError2_ = out23_
        if (d_219_valueOrError2_).IsFailure():
            output = (d_219_valueOrError2_).PropagateFailure()
            return output
        d_220___v1_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_220___v1_ = (d_219_valueOrError2_).Extract()
        d_221_decryptOnlyEncryptionContext_: _dafny.Map
        d_221_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_217_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_222_activeEncryptionContext_: _dafny.Map
        d_222_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_221_decryptOnlyEncryptionContext_)
        d_223_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out24_: Wrappers.Result
        out24_ = KMSKeystoreOperations.default__.GenerateKey(d_221_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_223_valueOrError3_ = out24_
        if (d_223_valueOrError3_).IsFailure():
            output = (d_223_valueOrError3_).PropagateFailure()
            return output
        d_224_wrappedDecryptOnlyBranchKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_224_wrappedDecryptOnlyBranchKey_ = (d_223_valueOrError3_).Extract()
        d_225_valueOrError4_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out25_: Wrappers.Result
        out25_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_224_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_221_decryptOnlyEncryptionContext_, d_222_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_225_valueOrError4_ = out25_
        if (d_225_valueOrError4_).IsFailure():
            output = (d_225_valueOrError4_).PropagateFailure()
            return output
        d_226_wrappedActiveBranchKey_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_226_wrappedActiveBranchKey_ = (d_225_valueOrError4_).Extract()
        d_227_decryptOnlyBranchKeyItem_: _dafny.Map
        d_227_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_221_decryptOnlyEncryptionContext_, ((d_224_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_228_activeBranchKeyItem_: _dafny.Map
        d_228_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_222_activeEncryptionContext_, ((d_226_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_229_valueOrError5_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        out26_: Wrappers.Result
        out26_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_227_decryptOnlyBranchKeyItem_, d_228_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_229_valueOrError5_ = out26_
        if (d_229_valueOrError5_).IsFailure():
            output = (d_229_valueOrError5_).PropagateFailure()
            return output
        d_230___v2_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_230___v2_ = (d_229_valueOrError5_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.VersionKeyOutput_VersionKeyOutput())
        return output

