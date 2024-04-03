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
import KMSKeystoreOperations
import DDBKeystoreOperations

# Module: CreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBranchAndBeaconKeys(branchKeyIdentifier, customEncryptionContext, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_190_decryptOnlyEncryptionContext_: _dafny.Map
        d_190_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, (kmsConfiguration).kmsKeyArn, customEncryptionContext)
        d_191_activeEncryptionContext_: _dafny.Map
        d_191_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_190_decryptOnlyEncryptionContext_)
        d_192_beaconEncryptionContext_: _dafny.Map
        d_192_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_190_decryptOnlyEncryptionContext_)
        d_193_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_194_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out18_: Wrappers.Result
        out18_ = KMSKeystoreOperations.default__.GenerateKey(d_190_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_194_valueOrError0_ = out18_
        if (d_194_valueOrError0_).IsFailure():
            output = (d_194_valueOrError0_).PropagateFailure()
            return output
        d_193_wrappedDecryptOnlyBranchKey_ = (d_194_valueOrError0_).Extract()
        d_195_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_196_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out19_: Wrappers.Result
        out19_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_193_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_190_decryptOnlyEncryptionContext_, d_191_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_196_valueOrError1_ = out19_
        if (d_196_valueOrError1_).IsFailure():
            output = (d_196_valueOrError1_).PropagateFailure()
            return output
        d_195_wrappedActiveBranchKey_ = (d_196_valueOrError1_).Extract()
        d_197_wrappedBeaconKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_198_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out20_: Wrappers.Result
        out20_ = KMSKeystoreOperations.default__.GenerateKey(d_192_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_198_valueOrError2_ = out20_
        if (d_198_valueOrError2_).IsFailure():
            output = (d_198_valueOrError2_).PropagateFailure()
            return output
        d_197_wrappedBeaconKey_ = (d_198_valueOrError2_).Extract()
        d_199_decryptOnlyBranchKeyItem_: _dafny.Map
        d_199_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_190_decryptOnlyEncryptionContext_, ((d_193_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_200_activeBranchKeyItem_: _dafny.Map
        d_200_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_191_activeEncryptionContext_, ((d_195_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_201_beaconKeyItem_: _dafny.Map
        d_201_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_192_beaconEncryptionContext_, ((d_197_wrappedBeaconKey_).CiphertextBlob).value)
        d_202___v0_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_203_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out21_: Wrappers.Result
        out21_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_199_decryptOnlyBranchKeyItem_, d_200_activeBranchKeyItem_, d_201_beaconKeyItem_, ddbTableName, ddbClient)
        d_203_valueOrError3_ = out21_
        if (d_203_valueOrError3_).IsFailure():
            output = (d_203_valueOrError3_).PropagateFailure()
            return output
        d_202___v0_ = (d_203_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_204_oldActiveItem_: _dafny.Map
        d_205_valueOrError0_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_205_valueOrError0_ = out22_
        if (d_205_valueOrError0_).IsFailure():
            output = (d_205_valueOrError0_).PropagateFailure()
            return output
        d_204_oldActiveItem_ = (d_205_valueOrError0_).Extract()
        d_206_oldActiveEncryptionContext_: _dafny.Map
        d_206_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_204_oldActiveItem_, logicalKeyStoreName)
        d_207_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_207_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_206_oldActiveEncryptionContext_)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Wrapping AWS KMS key in dynamodb does not match configured AWS KMS information.")))
        if (d_207_valueOrError1_).IsFailure():
            output = (d_207_valueOrError1_).PropagateFailure()
            return output
        d_208___v1_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_209_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out23_: Wrappers.Result
        out23_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_204_oldActiveItem_)[Structure.default__.BRANCH__KEY__FIELD]).B, d_206_oldActiveEncryptionContext_, d_206_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_209_valueOrError2_ = out23_
        if (d_209_valueOrError2_).IsFailure():
            output = (d_209_valueOrError2_).PropagateFailure()
            return output
        d_208___v1_ = (d_209_valueOrError2_).Extract()
        d_210_decryptOnlyEncryptionContext_: _dafny.Map
        d_210_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_206_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_211_activeEncryptionContext_: _dafny.Map
        d_211_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_210_decryptOnlyEncryptionContext_)
        d_212_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_213_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out24_: Wrappers.Result
        out24_ = KMSKeystoreOperations.default__.GenerateKey(d_210_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_213_valueOrError3_ = out24_
        if (d_213_valueOrError3_).IsFailure():
            output = (d_213_valueOrError3_).PropagateFailure()
            return output
        d_212_wrappedDecryptOnlyBranchKey_ = (d_213_valueOrError3_).Extract()
        d_214_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_215_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out25_: Wrappers.Result
        out25_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_212_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_210_decryptOnlyEncryptionContext_, d_211_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_215_valueOrError4_ = out25_
        if (d_215_valueOrError4_).IsFailure():
            output = (d_215_valueOrError4_).PropagateFailure()
            return output
        d_214_wrappedActiveBranchKey_ = (d_215_valueOrError4_).Extract()
        d_216_decryptOnlyBranchKeyItem_: _dafny.Map
        d_216_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_210_decryptOnlyEncryptionContext_, ((d_212_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_217_activeBranchKeyItem_: _dafny.Map
        d_217_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_211_activeEncryptionContext_, ((d_214_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_218___v2_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_219_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out26_: Wrappers.Result
        out26_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_216_decryptOnlyBranchKeyItem_, d_217_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_219_valueOrError5_ = out26_
        if (d_219_valueOrError5_).IsFailure():
            output = (d_219_valueOrError5_).PropagateFailure()
            return output
        d_218___v2_ = (d_219_valueOrError5_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput_VersionKeyOutput())
        return output

