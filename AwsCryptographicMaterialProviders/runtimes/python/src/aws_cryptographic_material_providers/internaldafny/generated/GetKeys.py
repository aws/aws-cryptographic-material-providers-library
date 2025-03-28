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
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable

# Module: GetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_branchKeyItem_: _dafny.Map
        d_1_branchKeyItem_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_1_branchKeyItem_, logicalKeyStoreName)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_2_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out1_: Wrappers.Result
        out1_ = KMSKeystoreOperations.default__.DecryptKey(d_2_encryptionContext_, d_1_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_5_valueOrError3_ = out1_
        if (d_5_valueOrError3_).IsFailure():
            output = (d_5_valueOrError3_).PropagateFailure()
            return output
        d_6_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_6_branchKey_ = (d_5_valueOrError3_).Extract()
        d_7_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_7_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_2_encryptionContext_, ((d_6_branchKey_).Plaintext).value)
        if (d_7_valueOrError4_).IsFailure():
            output = (d_7_valueOrError4_).PropagateFailure()
            return output
        d_8_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_8_branchKeyMaterials_ = (d_7_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_8_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_branchKeyItem_: _dafny.Map
        d_1_branchKeyItem_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_1_branchKeyItem_, logicalKeyStoreName)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_2_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out1_: Wrappers.Result
        out1_ = KMSKeystoreOperations.default__.DecryptKey(d_2_encryptionContext_, d_1_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_5_valueOrError3_ = out1_
        if (d_5_valueOrError3_).IsFailure():
            output = (d_5_valueOrError3_).PropagateFailure()
            return output
        d_6_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_6_branchKey_ = (d_5_valueOrError3_).Extract()
        d_7_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_7_valueOrError4_ = Structure.default__.ToBranchKeyMaterials(d_2_encryptionContext_, ((d_6_branchKey_).Plaintext).value)
        if (d_7_valueOrError4_).IsFailure():
            output = (d_7_valueOrError4_).PropagateFailure()
            return output
        d_8_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_8_branchKeyMaterials_ = (d_7_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_8_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_branchKeyItem_: _dafny.Map
        d_1_branchKeyItem_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_1_branchKeyItem_, logicalKeyStoreName)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need(KmsArn.default__.ValidKmsArn_q((d_2_encryptionContext_)[Structure.default__.KMS__FIELD]), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError2_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2_encryptionContext_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_4_valueOrError2_).IsFailure():
            output = (d_4_valueOrError2_).PropagateFailure()
            return output
        d_5_valueOrError3_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        out1_: Wrappers.Result
        out1_ = KMSKeystoreOperations.default__.DecryptKey(d_2_encryptionContext_, d_1_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_5_valueOrError3_ = out1_
        if (d_5_valueOrError3_).IsFailure():
            output = (d_5_valueOrError3_).PropagateFailure()
            return output
        d_6_branchKey_: ComAmazonawsKmsTypes.DecryptResponse
        d_6_branchKey_ = (d_5_valueOrError3_).Extract()
        d_7_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.default())()
        d_7_valueOrError4_ = Structure.default__.ToBeaconKeyMaterials(d_2_encryptionContext_, ((d_6_branchKey_).Plaintext).value)
        if (d_7_valueOrError4_).IsFailure():
            output = (d_7_valueOrError4_).PropagateFailure()
            return output
        d_8_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BeaconKeyMaterials
        d_8_branchKeyMaterials_ = (d_7_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput_GetBeaconKeyOutput(d_8_branchKeyMaterials_))
        return output
        return output

