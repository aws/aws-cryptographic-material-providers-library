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
import KMSKeystoreOperations
import DDBKeystoreOperations

# Module: CreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBranchAndBeaconKeys(branchKeyIdentifier, customEncryptionContext, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_2027_decryptOnlyEncryptionContext_: _dafny.Map
        d_2027_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, (kmsConfiguration).kmsKeyArn, customEncryptionContext)
        d_2028_activeEncryptionContext_: _dafny.Map
        d_2028_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_2027_decryptOnlyEncryptionContext_)
        d_2029_beaconEncryptionContext_: _dafny.Map
        d_2029_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_2027_decryptOnlyEncryptionContext_)
        d_2030_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_2031_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out357_: Wrappers.Result
        out357_ = KMSKeystoreOperations.default__.GenerateKey(d_2027_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2031_valueOrError0_ = out357_
        if (d_2031_valueOrError0_).IsFailure():
            output = (d_2031_valueOrError0_).PropagateFailure()
            return output
        d_2030_wrappedDecryptOnlyBranchKey_ = (d_2031_valueOrError0_).Extract()
        d_2032_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_2033_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out358_: Wrappers.Result
        out358_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_2030_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_2027_decryptOnlyEncryptionContext_, d_2028_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2033_valueOrError1_ = out358_
        if (d_2033_valueOrError1_).IsFailure():
            output = (d_2033_valueOrError1_).PropagateFailure()
            return output
        d_2032_wrappedActiveBranchKey_ = (d_2033_valueOrError1_).Extract()
        d_2034_wrappedBeaconKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_2035_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out359_: Wrappers.Result
        out359_ = KMSKeystoreOperations.default__.GenerateKey(d_2029_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2035_valueOrError2_ = out359_
        if (d_2035_valueOrError2_).IsFailure():
            output = (d_2035_valueOrError2_).PropagateFailure()
            return output
        d_2034_wrappedBeaconKey_ = (d_2035_valueOrError2_).Extract()
        d_2036_decryptOnlyBranchKeyItem_: _dafny.Map
        d_2036_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_2027_decryptOnlyEncryptionContext_, ((d_2030_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_2037_activeBranchKeyItem_: _dafny.Map
        d_2037_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_2028_activeEncryptionContext_, ((d_2032_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_2038_beaconKeyItem_: _dafny.Map
        d_2038_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_2029_beaconEncryptionContext_, ((d_2034_wrappedBeaconKey_).CiphertextBlob).value)
        d_2039___v0_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_2040_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out360_: Wrappers.Result
        out360_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_2036_decryptOnlyBranchKeyItem_, d_2037_activeBranchKeyItem_, d_2038_beaconKeyItem_, ddbTableName, ddbClient)
        d_2040_valueOrError3_ = out360_
        if (d_2040_valueOrError3_).IsFailure():
            output = (d_2040_valueOrError3_).PropagateFailure()
            return output
        d_2039___v0_ = (d_2040_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_2041_oldActiveItem_: _dafny.Map
        d_2042_valueOrError0_: Wrappers.Result = None
        out361_: Wrappers.Result
        out361_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_2042_valueOrError0_ = out361_
        if (d_2042_valueOrError0_).IsFailure():
            output = (d_2042_valueOrError0_).PropagateFailure()
            return output
        d_2041_oldActiveItem_ = (d_2042_valueOrError0_).Extract()
        d_2043_oldActiveEncryptionContext_: _dafny.Map
        d_2043_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_2041_oldActiveItem_, logicalKeyStoreName)
        d_2044_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2044_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2043_oldActiveEncryptionContext_)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Wrapping AWS KMS key in dynamodb does not match configured AWS KMS information.")))
        if (d_2044_valueOrError1_).IsFailure():
            output = (d_2044_valueOrError1_).PropagateFailure()
            return output
        d_2045___v1_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_2046_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out362_: Wrappers.Result
        out362_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_2041_oldActiveItem_)[Structure.default__.BRANCH__KEY__FIELD]).B, d_2043_oldActiveEncryptionContext_, d_2043_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2046_valueOrError2_ = out362_
        if (d_2046_valueOrError2_).IsFailure():
            output = (d_2046_valueOrError2_).PropagateFailure()
            return output
        d_2045___v1_ = (d_2046_valueOrError2_).Extract()
        d_2047_decryptOnlyEncryptionContext_: _dafny.Map
        d_2047_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_2043_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_2048_activeEncryptionContext_: _dafny.Map
        d_2048_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_2047_decryptOnlyEncryptionContext_)
        d_2049_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_2050_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out363_: Wrappers.Result
        out363_ = KMSKeystoreOperations.default__.GenerateKey(d_2047_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2050_valueOrError3_ = out363_
        if (d_2050_valueOrError3_).IsFailure():
            output = (d_2050_valueOrError3_).PropagateFailure()
            return output
        d_2049_wrappedDecryptOnlyBranchKey_ = (d_2050_valueOrError3_).Extract()
        d_2051_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_2052_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out364_: Wrappers.Result
        out364_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_2049_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_2047_decryptOnlyEncryptionContext_, d_2048_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_2052_valueOrError4_ = out364_
        if (d_2052_valueOrError4_).IsFailure():
            output = (d_2052_valueOrError4_).PropagateFailure()
            return output
        d_2051_wrappedActiveBranchKey_ = (d_2052_valueOrError4_).Extract()
        d_2053_decryptOnlyBranchKeyItem_: _dafny.Map
        d_2053_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_2047_decryptOnlyEncryptionContext_, ((d_2049_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_2054_activeBranchKeyItem_: _dafny.Map
        d_2054_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_2048_activeEncryptionContext_, ((d_2051_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_2055___v2_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_2056_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out365_: Wrappers.Result
        out365_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_2053_decryptOnlyBranchKeyItem_, d_2054_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_2056_valueOrError5_ = out365_
        if (d_2056_valueOrError5_).IsFailure():
            output = (d_2056_valueOrError5_).PropagateFailure()
            return output
        d_2055___v2_ = (d_2056_valueOrError5_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput_VersionKeyOutput())
        return output

