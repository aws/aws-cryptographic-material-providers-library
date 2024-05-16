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
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure

# Module: aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        source8_ = kmsConfiguration
        d_133___mcc_h0_ = source8_.kmsKeyArn
        d_134_arn_ = d_133___mcc_h0_
        return (d_134_arn_) == ((encryptionContext)[Structure.default__.KMS__FIELD])

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_135_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest
        d_135_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest((kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_136_maybeGenerateResponse_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_135_generatorRequest_)
        d_136_maybeGenerateResponse_ = out10_
        d_137_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_138_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda11_(d_139_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_139_e_)

        d_138_valueOrError0_ = (d_136_maybeGenerateResponse_).MapFailure(lambda11_)
        if (d_138_valueOrError0_).IsFailure():
            res = (d_138_valueOrError0_).PropagateFailure()
            return res
        d_137_generateResponse_ = (d_138_valueOrError0_).Extract()
        d_140_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_140_valueOrError1_ = Wrappers.default__.Need((True) and (((d_137_generateResponse_).KeyId).is_Some), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_140_valueOrError1_).IsFailure():
            res = (d_140_valueOrError1_).PropagateFailure()
            return res
        d_141_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_141_valueOrError2_ = Wrappers.default__.Need((((d_137_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_137_generateResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_141_valueOrError2_).IsFailure():
            res = (d_141_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_137_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        d_142_reEncryptRequest_: ComAmazonawsKmsTypes.ReEncryptRequest
        d_142_reEncryptRequest_ = ComAmazonawsKmsTypes.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), (kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_143_maybeReEncryptResponse_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (kmsClient).ReEncrypt(d_142_reEncryptRequest_)
        d_143_maybeReEncryptResponse_ = out11_
        d_144_reEncryptResponse_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_145_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        def lambda12_(d_146_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_146_e_)

        d_145_valueOrError0_ = (d_143_maybeReEncryptResponse_).MapFailure(lambda12_)
        if (d_145_valueOrError0_).IsFailure():
            res = (d_145_valueOrError0_).PropagateFailure()
            return res
        d_144_reEncryptResponse_ = (d_145_valueOrError0_).Extract()
        d_147_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_147_valueOrError1_ = Wrappers.default__.Need((((((d_144_reEncryptResponse_).SourceKeyId).is_Some) and (((d_144_reEncryptResponse_).KeyId).is_Some)) and ((((d_144_reEncryptResponse_).SourceKeyId).value) == ((kmsConfiguration).kmsKeyArn))) and ((((d_144_reEncryptResponse_).KeyId).value) == ((kmsConfiguration).kmsKeyArn)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_147_valueOrError1_).IsFailure():
            res = (d_147_valueOrError1_).PropagateFailure()
            return res
        d_148_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_148_valueOrError2_ = Wrappers.default__.Need((((d_144_reEncryptResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_144_reEncryptResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_148_valueOrError2_).IsFailure():
            res = (d_148_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_144_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        d_149_maybeDecryptResponse_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (kmsClient).Decrypt(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), Wrappers.Option_None()))
        d_149_maybeDecryptResponse_ = out12_
        d_150_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_151_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda13_(d_152_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_152_e_)

        d_151_valueOrError0_ = (d_149_maybeDecryptResponse_).MapFailure(lambda13_)
        if (d_151_valueOrError0_).IsFailure():
            output = (d_151_valueOrError0_).PropagateFailure()
            return output
        d_150_decryptResponse_ = (d_151_valueOrError0_).Extract()
        d_153_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_153_valueOrError1_ = Wrappers.default__.Need((((d_150_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_150_decryptResponse_).Plaintext).value))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_153_valueOrError1_).IsFailure():
            output = (d_153_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_150_decryptResponse_)
        return output

