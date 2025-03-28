import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations

# Module: CreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBranchAndBeaconKeys(branchKeyIdentifier, customEncryptionContext, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        d_0_decryptOnlyEncryptionContext_: _dafny.Map
        d_0_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, KMSKeystoreOperations.default__.GetKeyId(kmsConfiguration), customEncryptionContext)
        d_1_activeEncryptionContext_: _dafny.Map
        d_1_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_0_decryptOnlyEncryptionContext_)
        d_2_beaconEncryptionContext_: _dafny.Map
        d_2_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_0_decryptOnlyEncryptionContext_)
        d_3_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError0_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_0_decryptOnlyEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext in CreateBranchAndBeaconKeys.")))
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out0_: Wrappers.Result
        out0_ = KMSKeystoreOperations.default__.GenerateKey(d_0_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_4_valueOrError1_ = out0_
        if (d_4_valueOrError1_).IsFailure():
            output = (d_4_valueOrError1_).PropagateFailure()
            return output
        d_5_wrappedDecryptOnlyBranchKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_5_wrappedDecryptOnlyBranchKey_ = (d_4_valueOrError1_).Extract()
        d_6_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_1_activeEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for ReEncrypt in CreateBranchAndBeaconKeys.")))
        if (d_6_valueOrError2_).IsFailure():
            output = (d_6_valueOrError2_).PropagateFailure()
            return output
        d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out1_: Wrappers.Result
        out1_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_5_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_0_decryptOnlyEncryptionContext_, d_1_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_7_valueOrError3_ = out1_
        if (d_7_valueOrError3_).IsFailure():
            output = (d_7_valueOrError3_).PropagateFailure()
            return output
        d_8_wrappedActiveBranchKey_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_8_wrappedActiveBranchKey_ = (d_7_valueOrError3_).Extract()
        d_9_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_9_valueOrError4_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2_beaconEncryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext(beacon key) in CreateBranchAndBeaconKeys.")))
        if (d_9_valueOrError4_).IsFailure():
            output = (d_9_valueOrError4_).PropagateFailure()
            return output
        d_10_valueOrError5_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out2_: Wrappers.Result
        out2_ = KMSKeystoreOperations.default__.GenerateKey(d_2_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_10_valueOrError5_ = out2_
        if (d_10_valueOrError5_).IsFailure():
            output = (d_10_valueOrError5_).PropagateFailure()
            return output
        d_11_wrappedBeaconKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_11_wrappedBeaconKey_ = (d_10_valueOrError5_).Extract()
        d_12_decryptOnlyBranchKeyItem_: _dafny.Map
        d_12_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_0_decryptOnlyEncryptionContext_, ((d_5_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_13_activeBranchKeyItem_: _dafny.Map
        d_13_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_1_activeEncryptionContext_, ((d_8_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_14_beaconKeyItem_: _dafny.Map
        d_14_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_2_beaconEncryptionContext_, ((d_11_wrappedBeaconKey_).CiphertextBlob).value)
        d_15_valueOrError6_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        out3_: Wrappers.Result
        out3_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_12_decryptOnlyBranchKeyItem_, d_13_activeBranchKeyItem_, d_14_beaconKeyItem_, ddbTableName, ddbClient)
        d_15_valueOrError6_ = out3_
        if (d_15_valueOrError6_).IsFailure():
            output = (d_15_valueOrError6_).PropagateFailure()
            return output
        d_16___v0_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_16___v0_ = (d_15_valueOrError6_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_oldActiveItem_: _dafny.Map
        d_1_oldActiveItem_ = (d_0_valueOrError0_).Extract()
        d_2_oldActiveEncryptionContext_: _dafny.Map
        d_2_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_1_oldActiveItem_, logicalKeyStoreName)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2_oldActiveEncryptionContext_)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.VERSION__KEY__KMS__KEY__ARN__DISAGREEMENT))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out1_: Wrappers.Result
        out1_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_1_oldActiveItem_)[Structure.default__.BRANCH__KEY__FIELD]).B, d_2_oldActiveEncryptionContext_, d_2_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_4_valueOrError2_ = out1_
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5___v1_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_5___v1_ = (d_4_valueOrError2_).Extract()
        d_6_decryptOnlyEncryptionContext_: _dafny.Map
        d_6_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_2_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_7_activeEncryptionContext_: _dafny.Map
        d_7_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_6_decryptOnlyEncryptionContext_)
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        out2_: Wrappers.Result
        out2_ = KMSKeystoreOperations.default__.GenerateKey(d_6_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_8_valueOrError3_ = out2_
        if (d_8_valueOrError3_).IsFailure():
            output = (d_8_valueOrError3_).PropagateFailure()
            return output
        d_9_wrappedDecryptOnlyBranchKey_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_9_wrappedDecryptOnlyBranchKey_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        out3_: Wrappers.Result
        out3_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_9_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_6_decryptOnlyEncryptionContext_, d_7_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_10_valueOrError4_ = out3_
        if (d_10_valueOrError4_).IsFailure():
            output = (d_10_valueOrError4_).PropagateFailure()
            return output
        d_11_wrappedActiveBranchKey_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_11_wrappedActiveBranchKey_ = (d_10_valueOrError4_).Extract()
        d_12_decryptOnlyBranchKeyItem_: _dafny.Map
        d_12_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_6_decryptOnlyEncryptionContext_, ((d_9_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_13_activeBranchKeyItem_: _dafny.Map
        d_13_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_7_activeEncryptionContext_, ((d_11_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_14_valueOrError5_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        out4_: Wrappers.Result
        out4_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_12_decryptOnlyBranchKeyItem_, d_13_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_14_valueOrError5_ = out4_
        if (d_14_valueOrError5_).IsFailure():
            output = (d_14_valueOrError5_).PropagateFailure()
            return output
        d_15___v2_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_15___v2_ = (d_14_valueOrError5_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.VersionKeyOutput_VersionKeyOutput())
        return output

