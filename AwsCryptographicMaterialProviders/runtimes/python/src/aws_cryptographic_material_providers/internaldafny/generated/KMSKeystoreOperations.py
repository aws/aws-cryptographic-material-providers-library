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

# Module: KMSKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def replaceRegion(arn, region):
        d_0_parsed_ = AwsArnParsing.default__.ParseAwsKmsArn(arn)
        if (d_0_parsed_).is_Failure:
            return arn
        elif not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn((d_0_parsed_).value)):
            return arn
        elif True:
            d_1_newArn_ = ((d_0_parsed_).value).ToArnString(Wrappers.Option_Some(region))
            if ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_1_newArn_):
                return d_1_newArn_
            elif True:
                return arn

    @staticmethod
    def GetArn(kmsConfiguration, discoverdArn):
        source0_ = kmsConfiguration
        if True:
            if source0_.is_kmsKeyArn:
                d_0_arn_ = source0_.kmsKeyArn
                return d_0_arn_
        if True:
            if source0_.is_kmsMRKeyArn:
                d_1_arn_ = source0_.kmsMRKeyArn
                return d_1_arn_
        if True:
            if source0_.is_discovery:
                d_2_obj_ = source0_.discovery
                return discoverdArn
        if True:
            d_3_region_ = source0_.mrDiscovery
            return default__.replaceRegion(discoverdArn, (d_3_region_).region)

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        source0_ = kmsConfiguration
        if True:
            if source0_.is_kmsKeyArn:
                d_0_arn_ = source0_.kmsKeyArn
                return ((d_0_arn_) == ((encryptionContext)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_0_arn_))
        if True:
            if source0_.is_kmsMRKeyArn:
                d_1_arn_ = source0_.kmsMRKeyArn
                return (default__.MrkMatch(d_1_arn_, (encryptionContext)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_1_arn_))
        if True:
            if source0_.is_discovery:
                d_2_obj_ = source0_.discovery
                return KmsArn.default__.ValidKmsArn_q((encryptionContext)[Structure.default__.KMS__FIELD])
        if True:
            d_3_obj_ = source0_.mrDiscovery
            return KmsArn.default__.ValidKmsArn_q((encryptionContext)[Structure.default__.KMS__FIELD])

    @staticmethod
    def Compatible_q(kmsConfiguration, keyId):
        source0_ = kmsConfiguration
        if True:
            if source0_.is_kmsKeyArn:
                d_0_arn_ = source0_.kmsKeyArn
                return (d_0_arn_) == (keyId)
        if True:
            d_1_arn_ = source0_.kmsMRKeyArn
            return default__.MrkMatch(d_1_arn_, keyId)

    @staticmethod
    def OptCompatible_q(kmsConfiguration, keyId):
        return ((keyId).is_Some) and (default__.Compatible_q(kmsConfiguration, (keyId).value))

    @staticmethod
    def MrkMatch(x, y):
        d_0_xArn_ = AwsArnParsing.default__.ParseAwsKmsArn(x)
        d_1_yArn_ = AwsArnParsing.default__.ParseAwsKmsArn(y)
        if ((d_0_xArn_).is_Failure) or ((d_1_yArn_).is_Failure):
            return False
        elif True:
            return AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt(AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_0_xArn_).value), AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_1_yArn_).value))

    @staticmethod
    def HasKeyId(kmsConfiguration):
        return ((kmsConfiguration).is_kmsKeyArn) or ((kmsConfiguration).is_kmsMRKeyArn)

    @staticmethod
    def GetKeyId(kmsConfiguration):
        source0_ = kmsConfiguration
        if True:
            if source0_.is_kmsKeyArn:
                d_0_arn_ = source0_.kmsKeyArn
                return d_0_arn_
        if True:
            d_1_arn_ = source0_.kmsMRKeyArn
            return d_1_arn_

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_0_kmsKeyArn_: _dafny.Seq
        d_0_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_1_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest
        d_1_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(d_0_kmsKeyArn_, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens), Wrappers.Option_None())
        d_2_maybeGenerateResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_1_generatorRequest_)
        d_2_maybeGenerateResponse_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeGenerateResponse_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            res = (d_3_valueOrError0_).PropagateFailure()
            return res
        d_5_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_5_generateResponse_ = (d_3_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((True) and (((d_5_generateResponse_).KeyId).is_Some), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_6_valueOrError1_).IsFailure():
            res = (d_6_valueOrError1_).PropagateFailure()
            return res
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need((((d_5_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_5_generateResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_5_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        d_0_kmsKeyArn_: _dafny.Seq
        d_0_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_1_reEncryptRequest_: ComAmazonawsKmsTypes.ReEncryptRequest
        d_1_reEncryptRequest_ = ComAmazonawsKmsTypes.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some(d_0_kmsKeyArn_), d_0_kmsKeyArn_, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens), Wrappers.Option_None())
        d_2_maybeReEncryptResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (kmsClient).ReEncrypt(d_1_reEncryptRequest_)
        d_2_maybeReEncryptResponse_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeReEncryptResponse_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            res = (d_3_valueOrError0_).PropagateFailure()
            return res
        d_5_reEncryptResponse_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_5_reEncryptResponse_ = (d_3_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((((((d_5_reEncryptResponse_).SourceKeyId).is_Some) and (((d_5_reEncryptResponse_).KeyId).is_Some)) and ((((d_5_reEncryptResponse_).SourceKeyId).value) == (d_0_kmsKeyArn_))) and ((((d_5_reEncryptResponse_).KeyId).value) == (d_0_kmsKeyArn_)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS ReEncrypt:: Invalid Key Id")))
        if (d_6_valueOrError1_).IsFailure():
            res = (d_6_valueOrError1_).PropagateFailure()
            return res
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need((((d_5_reEncryptResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_5_reEncryptResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_5_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        d_0_kmsKeyArn_: _dafny.Seq
        d_0_kmsKeyArn_ = default__.GetArn(kmsConfiguration, (encryptionContext)[Structure.default__.KMS__FIELD])
        d_1_maybeDecryptResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (kmsClient).Decrypt(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some(d_0_kmsKeyArn_), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_1_maybeDecryptResponse_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda0_(d_3_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybeDecryptResponse_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        d_4_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_4_decryptResponse_ = (d_2_valueOrError0_).Extract()
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need((((d_4_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_4_decryptResponse_).Plaintext).value))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_5_valueOrError1_).IsFailure():
            output = (d_5_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_4_decryptResponse_)
        return output

