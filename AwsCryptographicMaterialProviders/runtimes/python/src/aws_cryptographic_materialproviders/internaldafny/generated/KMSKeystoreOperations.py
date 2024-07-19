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

# Module: KMSKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def replaceRegion(arn, region):
        d_124_parsed_ = AwsArnParsing.default__.ParseAwsKmsArn(arn)
        if (d_124_parsed_).is_Failure:
            return arn
        elif not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn((d_124_parsed_).value)):
            return arn
        elif True:
            d_125_newArn_ = ((d_124_parsed_).value).ToArnString(Wrappers.Option_Some(region))
            if ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_125_newArn_):
                return d_125_newArn_
            elif True:
                return arn

    @staticmethod
    def GetArn(kmsConfiguration, discoverdArn):
        source6_ = kmsConfiguration
        if True:
            if source6_.is_kmsKeyArn:
                d_126_arn_ = source6_.kmsKeyArn
                return d_126_arn_
        if True:
            if source6_.is_kmsMRKeyArn:
                d_127_arn_ = source6_.kmsMRKeyArn
                return d_127_arn_
        if True:
            if source6_.is_discovery:
                d_128_obj_ = source6_.discovery
                return discoverdArn
        if True:
            d_129_region_ = source6_.mrDiscovery
            return default__.replaceRegion(discoverdArn, (d_129_region_).region)

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        source7_ = kmsConfiguration
        if True:
            if source7_.is_kmsKeyArn:
                d_130_arn_ = source7_.kmsKeyArn
                return ((d_130_arn_) == ((encryptionContext)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_130_arn_))
        if True:
            if source7_.is_kmsMRKeyArn:
                d_131_arn_ = source7_.kmsMRKeyArn
                return (default__.MrkMatch(d_131_arn_, (encryptionContext)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_131_arn_))
        if True:
            if source7_.is_discovery:
                d_132_obj_ = source7_.discovery
                return KmsArn.default__.ValidKmsArn_q((encryptionContext)[Structure.default__.KMS__FIELD])
        if True:
            d_133_obj_ = source7_.mrDiscovery
            return KmsArn.default__.ValidKmsArn_q((encryptionContext)[Structure.default__.KMS__FIELD])

    @staticmethod
    def Compatible_q(kmsConfiguration, keyId):
        source8_ = kmsConfiguration
        if True:
            if source8_.is_kmsKeyArn:
                d_134_arn_ = source8_.kmsKeyArn
                return (d_134_arn_) == (keyId)
        if True:
            d_135_arn_ = source8_.kmsMRKeyArn
            return default__.MrkMatch(d_135_arn_, keyId)

    @staticmethod
    def OptCompatible_q(kmsConfiguration, keyId):
        return ((keyId).is_Some) and (default__.Compatible_q(kmsConfiguration, (keyId).value))

    @staticmethod
    def MrkMatch(x, y):
        d_136_xArn_ = AwsArnParsing.default__.ParseAwsKmsArn(x)
        d_137_yArn_ = AwsArnParsing.default__.ParseAwsKmsArn(y)
        if ((d_136_xArn_).is_Failure) or ((d_137_yArn_).is_Failure):
            return False
        elif True:
            return AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt(AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_136_xArn_).value), AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_137_yArn_).value))

    @staticmethod
    def HasKeyId(kmsConfiguration):
        return ((kmsConfiguration).is_kmsKeyArn) or ((kmsConfiguration).is_kmsMRKeyArn)

    @staticmethod
    def GetKeyId(kmsConfiguration):
        source9_ = kmsConfiguration
        if True:
            if source9_.is_kmsKeyArn:
                d_138_arn_ = source9_.kmsKeyArn
                return d_138_arn_
        if True:
            d_139_arn_ = source9_.kmsMRKeyArn
            return d_139_arn_

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_140_kmsKeyArn_: _dafny.Seq
        d_140_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_141_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest
        d_141_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(d_140_kmsKeyArn_, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_142_maybeGenerateResponse_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_141_generatorRequest_)
        d_142_maybeGenerateResponse_ = out10_
        d_143_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda12_(d_144_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_144_e_)

        d_143_valueOrError0_ = (d_142_maybeGenerateResponse_).MapFailure(lambda12_)
        if (d_143_valueOrError0_).IsFailure():
            res = (d_143_valueOrError0_).PropagateFailure()
            return res
        d_145_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_145_generateResponse_ = (d_143_valueOrError0_).Extract()
        d_146_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_146_valueOrError1_ = Wrappers.default__.Need((True) and (((d_145_generateResponse_).KeyId).is_Some), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_146_valueOrError1_).IsFailure():
            res = (d_146_valueOrError1_).PropagateFailure()
            return res
        d_147_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_147_valueOrError2_ = Wrappers.default__.Need((((d_145_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_145_generateResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_147_valueOrError2_).IsFailure():
            res = (d_147_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_145_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        d_148_kmsKeyArn_: _dafny.Seq
        d_148_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_149_reEncryptRequest_: ComAmazonawsKmsTypes.ReEncryptRequest
        d_149_reEncryptRequest_ = ComAmazonawsKmsTypes.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some(d_148_kmsKeyArn_), d_148_kmsKeyArn_, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_150_maybeReEncryptResponse_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (kmsClient).ReEncrypt(d_149_reEncryptRequest_)
        d_150_maybeReEncryptResponse_ = out11_
        d_151_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        def lambda13_(d_152_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_152_e_)

        d_151_valueOrError0_ = (d_150_maybeReEncryptResponse_).MapFailure(lambda13_)
        if (d_151_valueOrError0_).IsFailure():
            res = (d_151_valueOrError0_).PropagateFailure()
            return res
        d_153_reEncryptResponse_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_153_reEncryptResponse_ = (d_151_valueOrError0_).Extract()
        d_154_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_154_valueOrError1_ = Wrappers.default__.Need((((((d_153_reEncryptResponse_).SourceKeyId).is_Some) and (((d_153_reEncryptResponse_).KeyId).is_Some)) and ((((d_153_reEncryptResponse_).SourceKeyId).value) == (d_148_kmsKeyArn_))) and ((((d_153_reEncryptResponse_).KeyId).value) == (d_148_kmsKeyArn_)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS ReEncrypt:: Invalid Key Id")))
        if (d_154_valueOrError1_).IsFailure():
            res = (d_154_valueOrError1_).PropagateFailure()
            return res
        d_155_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_155_valueOrError2_ = Wrappers.default__.Need((((d_153_reEncryptResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_153_reEncryptResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_155_valueOrError2_).IsFailure():
            res = (d_155_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_153_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        d_156_kmsKeyArn_: _dafny.Seq
        d_156_kmsKeyArn_ = default__.GetArn(kmsConfiguration, (encryptionContext)[Structure.default__.KMS__FIELD])
        d_157_maybeDecryptResponse_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (kmsClient).Decrypt(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some(d_156_kmsKeyArn_), Wrappers.Option_None()))
        d_157_maybeDecryptResponse_ = out12_
        d_158_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda14_(d_159_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_159_e_)

        d_158_valueOrError0_ = (d_157_maybeDecryptResponse_).MapFailure(lambda14_)
        if (d_158_valueOrError0_).IsFailure():
            output = (d_158_valueOrError0_).PropagateFailure()
            return output
        d_160_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_160_decryptResponse_ = (d_158_valueOrError0_).Extract()
        d_161_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_161_valueOrError1_ = Wrappers.default__.Need((((d_160_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_160_decryptResponse_).Plaintext).value))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_161_valueOrError1_).IsFailure():
            output = (d_161_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_160_decryptResponse_)
        return output

