import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure

# Module: KMSKeystoreOperations

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
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_135_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest
        d_135_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest((kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_136_maybeGenerateResponse_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_135_generatorRequest_)
        d_136_maybeGenerateResponse_ = out10_
        d_137_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_138_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda11_(d_139_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_139_e_)

        d_138_valueOrError0_ = (d_136_maybeGenerateResponse_).MapFailure(lambda11_)
        if (d_138_valueOrError0_).IsFailure():
            res = (d_138_valueOrError0_).PropagateFailure()
            return res
        d_137_generateResponse_ = (d_138_valueOrError0_).Extract()
        d_140_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_140_valueOrError1_ = Wrappers.default__.Need((True) and (((d_137_generateResponse_).KeyId).is_Some), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_140_valueOrError1_).IsFailure():
            res = (d_140_valueOrError1_).PropagateFailure()
            return res
        d_141_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_141_valueOrError2_ = Wrappers.default__.Need((((d_137_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_137_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_141_valueOrError2_).IsFailure():
            res = (d_141_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_137_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        d_142_reEncryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest
        d_142_reEncryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), (kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_143_maybeReEncryptResponse_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (kmsClient).ReEncrypt(d_142_reEncryptRequest_)
        d_143_maybeReEncryptResponse_ = out11_
        d_144_reEncryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_145_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        def lambda12_(d_146_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_146_e_)

        d_145_valueOrError0_ = (d_143_maybeReEncryptResponse_).MapFailure(lambda12_)
        if (d_145_valueOrError0_).IsFailure():
            res = (d_145_valueOrError0_).PropagateFailure()
            return res
        d_144_reEncryptResponse_ = (d_145_valueOrError0_).Extract()
        d_147_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_147_valueOrError1_ = Wrappers.default__.Need((((((d_144_reEncryptResponse_).SourceKeyId).is_Some) and (((d_144_reEncryptResponse_).KeyId).is_Some)) and ((((d_144_reEncryptResponse_).SourceKeyId).value) == ((kmsConfiguration).kmsKeyArn))) and ((((d_144_reEncryptResponse_).KeyId).value) == ((kmsConfiguration).kmsKeyArn)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_147_valueOrError1_).IsFailure():
            res = (d_147_valueOrError1_).PropagateFailure()
            return res
        d_148_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_148_valueOrError2_ = Wrappers.default__.Need((((d_144_reEncryptResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_144_reEncryptResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_148_valueOrError2_).IsFailure():
            res = (d_148_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_144_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        d_149_maybeDecryptResponse_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (kmsClient).Decrypt(software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), Wrappers.Option_None()))
        d_149_maybeDecryptResponse_ = out12_
        d_150_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_151_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda13_(d_152_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_152_e_)

        d_151_valueOrError0_ = (d_149_maybeDecryptResponse_).MapFailure(lambda13_)
        if (d_151_valueOrError0_).IsFailure():
            output = (d_151_valueOrError0_).PropagateFailure()
            return output
        d_150_decryptResponse_ = (d_151_valueOrError0_).Extract()
        d_153_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_153_valueOrError1_ = Wrappers.default__.Need((((d_150_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_150_decryptResponse_).Plaintext).value))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_153_valueOrError1_).IsFailure():
            output = (d_153_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_150_decryptResponse_)
        return output

