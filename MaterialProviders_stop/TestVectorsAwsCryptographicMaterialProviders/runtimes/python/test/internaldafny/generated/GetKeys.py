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
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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
import CreateKeys
import CreateKeyStoreTable

assert "GetKeys" == __name__
GetKeys = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        d_2060_branchKeyItem_: _dafny.Map
        d_2061_valueOrError0_: Wrappers.Result = None
        out368_: Wrappers.Result
        out368_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_2061_valueOrError0_ = out368_
        if (d_2061_valueOrError0_).IsFailure():
            output = (d_2061_valueOrError0_).PropagateFailure()
            return output
        d_2060_branchKeyItem_ = (d_2061_valueOrError0_).Extract()
        d_2062_encryptionContext_: _dafny.Map
        d_2062_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_2060_branchKeyItem_, logicalKeyStoreName)
        d_2063_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2063_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2062_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_2063_valueOrError1_).IsFailure():
            output = (d_2063_valueOrError1_).PropagateFailure()
            return output
        d_2064_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_2065_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out369_: Wrappers.Result
        out369_ = KMSKeystoreOperations.default__.DecryptKey(d_2062_encryptionContext_, d_2060_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_2065_valueOrError2_ = out369_
        if (d_2065_valueOrError2_).IsFailure():
            output = (d_2065_valueOrError2_).PropagateFailure()
            return output
        d_2064_branchKey_ = (d_2065_valueOrError2_).Extract()
        d_2066_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_2067_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_2067_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_2062_encryptionContext_, ((d_2064_branchKey_).Plaintext).value)
        if (d_2067_valueOrError3_).IsFailure():
            output = (d_2067_valueOrError3_).PropagateFailure()
            return output
        d_2066_branchKeyMaterials_ = (d_2067_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_2066_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        d_2068_branchKeyItem_: _dafny.Map
        d_2069_valueOrError0_: Wrappers.Result = None
        out370_: Wrappers.Result
        out370_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_2069_valueOrError0_ = out370_
        if (d_2069_valueOrError0_).IsFailure():
            output = (d_2069_valueOrError0_).PropagateFailure()
            return output
        d_2068_branchKeyItem_ = (d_2069_valueOrError0_).Extract()
        d_2070_encryptionContext_: _dafny.Map
        d_2070_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_2068_branchKeyItem_, logicalKeyStoreName)
        d_2071_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2071_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2070_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_2071_valueOrError1_).IsFailure():
            output = (d_2071_valueOrError1_).PropagateFailure()
            return output
        d_2072_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_2073_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out371_: Wrappers.Result
        out371_ = KMSKeystoreOperations.default__.DecryptKey(d_2070_encryptionContext_, d_2068_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_2073_valueOrError2_ = out371_
        if (d_2073_valueOrError2_).IsFailure():
            output = (d_2073_valueOrError2_).PropagateFailure()
            return output
        d_2072_branchKey_ = (d_2073_valueOrError2_).Extract()
        d_2074_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_2075_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_2075_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_2070_encryptionContext_, ((d_2072_branchKey_).Plaintext).value)
        if (d_2075_valueOrError3_).IsFailure():
            output = (d_2075_valueOrError3_).PropagateFailure()
            return output
        d_2074_branchKeyMaterials_ = (d_2075_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_2074_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        d_2076_branchKeyItem_: _dafny.Map
        d_2077_valueOrError0_: Wrappers.Result = None
        out372_: Wrappers.Result
        out372_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_2077_valueOrError0_ = out372_
        if (d_2077_valueOrError0_).IsFailure():
            output = (d_2077_valueOrError0_).PropagateFailure()
            return output
        d_2076_branchKeyItem_ = (d_2077_valueOrError0_).Extract()
        d_2078_encryptionContext_: _dafny.Map
        d_2078_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_2076_branchKeyItem_, logicalKeyStoreName)
        d_2079_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2079_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_2078_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_2079_valueOrError1_).IsFailure():
            output = (d_2079_valueOrError1_).PropagateFailure()
            return output
        d_2080_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_2081_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out373_: Wrappers.Result
        out373_ = KMSKeystoreOperations.default__.DecryptKey(d_2078_encryptionContext_, d_2076_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_2081_valueOrError2_ = out373_
        if (d_2081_valueOrError2_).IsFailure():
            output = (d_2081_valueOrError2_).PropagateFailure()
            return output
        d_2080_branchKey_ = (d_2081_valueOrError2_).Extract()
        d_2082_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials
        d_2083_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials.default())()
        d_2083_valueOrError3_ = Structure.default__.ToBeaconKeyMaterials(d_2078_encryptionContext_, ((d_2080_branchKey_).Plaintext).value)
        if (d_2083_valueOrError3_).IsFailure():
            output = (d_2083_valueOrError3_).PropagateFailure()
            return output
        d_2082_branchKeyMaterials_ = (d_2083_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput_GetBeaconKeyOutput(d_2082_branchKeyMaterials_))
        return output
        return output

