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
        d_127_parsed_ = AwsArnParsing.default__.ParseAwsKmsArn(arn)
        if (d_127_parsed_).is_Failure:
            return arn
        elif not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn((d_127_parsed_).value)):
            return arn
        elif True:
            d_128_newArn_ = ((d_127_parsed_).value).ToArnString(Wrappers.Option_Some(region))
            if ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_128_newArn_):
                return d_128_newArn_
            elif True:
                return arn

    @staticmethod
    def GetArn(kmsConfiguration, discoverdArn):
        pat_let_tv0_ = discoverdArn
        pat_let_tv1_ = discoverdArn
        source6_ = kmsConfiguration
        unmatched6 = True
        if unmatched6:
            if source6_.is_kmsKeyArn:
                d_129_arn_ = source6_.kmsKeyArn
                unmatched6 = False
                return d_129_arn_
        if unmatched6:
            if source6_.is_kmsMRKeyArn:
                d_130_arn_ = source6_.kmsMRKeyArn
                unmatched6 = False
                return d_130_arn_
        if unmatched6:
            if source6_.is_discovery:
                d_131_obj_ = source6_.discovery
                unmatched6 = False
                return pat_let_tv0_
        if unmatched6:
            d_132_region_ = source6_.mrDiscovery
            unmatched6 = False
            return default__.replaceRegion(pat_let_tv1_, (d_132_region_).region)
        raise Exception("unexpected control point")

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        pat_let_tv2_ = encryptionContext
        pat_let_tv3_ = encryptionContext
        pat_let_tv4_ = encryptionContext
        pat_let_tv5_ = encryptionContext
        source7_ = kmsConfiguration
        unmatched7 = True
        if unmatched7:
            if source7_.is_kmsKeyArn:
                d_133_arn_ = source7_.kmsKeyArn
                unmatched7 = False
                return ((d_133_arn_) == ((pat_let_tv2_)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_133_arn_))
        if unmatched7:
            if source7_.is_kmsMRKeyArn:
                d_134_arn_ = source7_.kmsMRKeyArn
                unmatched7 = False
                return (default__.MrkMatch(d_134_arn_, (pat_let_tv3_)[Structure.default__.KMS__FIELD])) and (KmsArn.default__.ValidKmsArn_q(d_134_arn_))
        if unmatched7:
            if source7_.is_discovery:
                d_135_obj_ = source7_.discovery
                unmatched7 = False
                return KmsArn.default__.ValidKmsArn_q((pat_let_tv4_)[Structure.default__.KMS__FIELD])
        if unmatched7:
            d_136_obj_ = source7_.mrDiscovery
            unmatched7 = False
            return KmsArn.default__.ValidKmsArn_q((pat_let_tv5_)[Structure.default__.KMS__FIELD])
        raise Exception("unexpected control point")

    @staticmethod
    def Compatible_q(kmsConfiguration, keyId):
        pat_let_tv6_ = keyId
        pat_let_tv7_ = keyId
        source8_ = kmsConfiguration
        unmatched8 = True
        if unmatched8:
            if source8_.is_kmsKeyArn:
                d_137_arn_ = source8_.kmsKeyArn
                unmatched8 = False
                return (d_137_arn_) == (pat_let_tv6_)
        if unmatched8:
            d_138_arn_ = source8_.kmsMRKeyArn
            unmatched8 = False
            return default__.MrkMatch(d_138_arn_, pat_let_tv7_)
        raise Exception("unexpected control point")

    @staticmethod
    def OptCompatible_q(kmsConfiguration, keyId):
        return ((keyId).is_Some) and (default__.Compatible_q(kmsConfiguration, (keyId).value))

    @staticmethod
    def MrkMatch(x, y):
        d_139_xArn_ = AwsArnParsing.default__.ParseAwsKmsArn(x)
        d_140_yArn_ = AwsArnParsing.default__.ParseAwsKmsArn(y)
        if ((d_139_xArn_).is_Failure) or ((d_140_yArn_).is_Failure):
            return False
        elif True:
            return AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt(AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_139_xArn_).value), AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier((d_140_yArn_).value))

    @staticmethod
    def HasKeyId(kmsConfiguration):
        return ((kmsConfiguration).is_kmsKeyArn) or ((kmsConfiguration).is_kmsMRKeyArn)

    @staticmethod
    def GetKeyId(kmsConfiguration):
        source9_ = kmsConfiguration
        unmatched9 = True
        if unmatched9:
            if source9_.is_kmsKeyArn:
                d_141_arn_ = source9_.kmsKeyArn
                unmatched9 = False
                return d_141_arn_
        if unmatched9:
            d_142_arn_ = source9_.kmsMRKeyArn
            unmatched9 = False
            return d_142_arn_
        raise Exception("unexpected control point")

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_143_kmsKeyArn_: _dafny.Seq
        d_143_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_144_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest
        d_144_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(d_143_kmsKeyArn_, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_145_maybeGenerateResponse_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_144_generatorRequest_)
        d_145_maybeGenerateResponse_ = out10_
        d_146_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse
        d_147_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda12_(d_148_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_148_e_)

        d_147_valueOrError0_ = (d_145_maybeGenerateResponse_).MapFailure(lambda12_)
        if (d_147_valueOrError0_).IsFailure():
            res = (d_147_valueOrError0_).PropagateFailure()
            return res
        d_146_generateResponse_ = (d_147_valueOrError0_).Extract()
        d_149_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_149_valueOrError1_ = Wrappers.default__.Need((True) and (((d_146_generateResponse_).KeyId).is_Some), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_149_valueOrError1_).IsFailure():
            res = (d_149_valueOrError1_).PropagateFailure()
            return res
        d_150_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_150_valueOrError2_ = Wrappers.default__.Need((((d_146_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_146_generateResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_150_valueOrError2_).IsFailure():
            res = (d_150_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_146_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        d_151_kmsKeyArn_: _dafny.Seq
        d_151_kmsKeyArn_ = default__.GetKeyId(kmsConfiguration)
        d_152_reEncryptRequest_: ComAmazonawsKmsTypes.ReEncryptRequest
        d_152_reEncryptRequest_ = ComAmazonawsKmsTypes.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some(d_151_kmsKeyArn_), d_151_kmsKeyArn_, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_153_maybeReEncryptResponse_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (kmsClient).ReEncrypt(d_152_reEncryptRequest_)
        d_153_maybeReEncryptResponse_ = out11_
        d_154_reEncryptResponse_: ComAmazonawsKmsTypes.ReEncryptResponse
        d_155_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.ReEncryptResponse.default())()
        def lambda13_(d_156_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_156_e_)

        d_155_valueOrError0_ = (d_153_maybeReEncryptResponse_).MapFailure(lambda13_)
        if (d_155_valueOrError0_).IsFailure():
            res = (d_155_valueOrError0_).PropagateFailure()
            return res
        d_154_reEncryptResponse_ = (d_155_valueOrError0_).Extract()
        d_157_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_157_valueOrError1_ = Wrappers.default__.Need((((((d_154_reEncryptResponse_).SourceKeyId).is_Some) and (((d_154_reEncryptResponse_).KeyId).is_Some)) and ((((d_154_reEncryptResponse_).SourceKeyId).value) == (d_151_kmsKeyArn_))) and ((((d_154_reEncryptResponse_).KeyId).value) == (d_151_kmsKeyArn_)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS ReEncrypt:: Invalid Key Id")))
        if (d_157_valueOrError1_).IsFailure():
            res = (d_157_valueOrError1_).PropagateFailure()
            return res
        d_158_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_158_valueOrError2_ = Wrappers.default__.Need((((d_154_reEncryptResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_154_reEncryptResponse_).CiphertextBlob).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_158_valueOrError2_).IsFailure():
            res = (d_158_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_154_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        d_159_kmsKeyArn_: _dafny.Seq
        d_159_kmsKeyArn_ = default__.GetArn(kmsConfiguration, (encryptionContext)[Structure.default__.KMS__FIELD])
        d_160_maybeDecryptResponse_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (kmsClient).Decrypt(ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some(d_159_kmsKeyArn_), Wrappers.Option_None()))
        d_160_maybeDecryptResponse_ = out12_
        d_161_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_162_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda14_(d_163_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_163_e_)

        d_162_valueOrError0_ = (d_160_maybeDecryptResponse_).MapFailure(lambda14_)
        if (d_162_valueOrError0_).IsFailure():
            output = (d_162_valueOrError0_).PropagateFailure()
            return output
        d_161_decryptResponse_ = (d_162_valueOrError0_).Extract()
        d_164_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_164_valueOrError1_ = Wrappers.default__.Need((((d_161_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_161_decryptResponse_).Plaintext).value))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_164_valueOrError1_).IsFailure():
            output = (d_164_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_161_decryptResponse_)
        return output

