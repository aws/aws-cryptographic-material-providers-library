import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import CompleteVectors
import ParseJsonManifests
import TestManifests
import WrappedMaterialProvidersMain
import TestWrappedMaterialProvidersMain
import software_amazon_cryptography_services_dynamodb_internaldafny
import Structure

# Module: KMSKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        source62_ = kmsConfiguration
        d_1970___mcc_h0_ = source62_.kmsKeyArn
        d_1971_arn_ = d_1970___mcc_h0_
        return (d_1971_arn_) == ((encryptionContext)[Structure.default__.KMS__FIELD])

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_1972_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest
        d_1972_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest((kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_1973_maybeGenerateResponse_: Wrappers.Result
        out349_: Wrappers.Result
        out349_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_1972_generatorRequest_)
        d_1973_maybeGenerateResponse_ = out349_
        d_1974_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_1975_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda134_(d_1976_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_1976_e_)

        d_1975_valueOrError0_ = (d_1973_maybeGenerateResponse_).MapFailure(lambda134_)
        if (d_1975_valueOrError0_).IsFailure():
            res = (d_1975_valueOrError0_).PropagateFailure()
            return res
        d_1974_generateResponse_ = (d_1975_valueOrError0_).Extract()
        d_1977_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1977_valueOrError1_ = Wrappers.default__.Need((True) and (((d_1974_generateResponse_).KeyId).is_Some), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_1977_valueOrError1_).IsFailure():
            res = (d_1977_valueOrError1_).PropagateFailure()
            return res
        d_1978_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1978_valueOrError2_ = Wrappers.default__.Need((((d_1974_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_1974_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")))
        if (d_1978_valueOrError2_).IsFailure():
            res = (d_1978_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_1974_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        d_1979_reEncryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest
        d_1979_reEncryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), (kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_1980_maybeReEncryptResponse_: Wrappers.Result
        out350_: Wrappers.Result
        out350_ = (kmsClient).ReEncrypt(d_1979_reEncryptRequest_)
        d_1980_maybeReEncryptResponse_ = out350_
        d_1981_reEncryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_1982_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        def lambda135_(d_1983_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_1983_e_)

        d_1982_valueOrError0_ = (d_1980_maybeReEncryptResponse_).MapFailure(lambda135_)
        if (d_1982_valueOrError0_).IsFailure():
            res = (d_1982_valueOrError0_).PropagateFailure()
            return res
        d_1981_reEncryptResponse_ = (d_1982_valueOrError0_).Extract()
        d_1984_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1984_valueOrError1_ = Wrappers.default__.Need((((((d_1981_reEncryptResponse_).SourceKeyId).is_Some) and (((d_1981_reEncryptResponse_).KeyId).is_Some)) and ((((d_1981_reEncryptResponse_).SourceKeyId).value) == ((kmsConfiguration).kmsKeyArn))) and ((((d_1981_reEncryptResponse_).KeyId).value) == ((kmsConfiguration).kmsKeyArn)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_1984_valueOrError1_).IsFailure():
            res = (d_1984_valueOrError1_).PropagateFailure()
            return res
        d_1985_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1985_valueOrError2_ = Wrappers.default__.Need((((d_1981_reEncryptResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_1981_reEncryptResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")))
        if (d_1985_valueOrError2_).IsFailure():
            res = (d_1985_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_1981_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        d_1986_maybeDecryptResponse_: Wrappers.Result
        out351_: Wrappers.Result
        out351_ = (kmsClient).Decrypt(software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest(((item)[Structure.default__.BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), Wrappers.Option_None()))
        d_1986_maybeDecryptResponse_ = out351_
        d_1987_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_1988_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda136_(d_1989_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_1989_e_)

        d_1988_valueOrError0_ = (d_1986_maybeDecryptResponse_).MapFailure(lambda136_)
        if (d_1988_valueOrError0_).IsFailure():
            output = (d_1988_valueOrError0_).PropagateFailure()
            return output
        d_1987_decryptResponse_ = (d_1988_valueOrError0_).Extract()
        d_1990_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1990_valueOrError1_ = Wrappers.default__.Need((((d_1987_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_1987_decryptResponse_).Plaintext).value))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_1990_valueOrError1_).IsFailure():
            output = (d_1990_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_1987_decryptResponse_)
        return output

