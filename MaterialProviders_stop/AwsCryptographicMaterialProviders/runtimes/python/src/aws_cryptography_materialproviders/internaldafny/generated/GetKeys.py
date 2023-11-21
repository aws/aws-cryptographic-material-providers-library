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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
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
        d_211_branchKeyItem_: _dafny.Map
        d_212_valueOrError0_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_212_valueOrError0_ = out29_
        if (d_212_valueOrError0_).IsFailure():
            output = (d_212_valueOrError0_).PropagateFailure()
            return output
        d_211_branchKeyItem_ = (d_212_valueOrError0_).Extract()
        d_213_encryptionContext_: _dafny.Map
        d_213_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_211_branchKeyItem_, logicalKeyStoreName)
        d_214_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_214_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_213_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_214_valueOrError1_).IsFailure():
            output = (d_214_valueOrError1_).PropagateFailure()
            return output
        d_215_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_216_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out30_: Wrappers.Result
        out30_ = KMSKeystoreOperations.default__.DecryptKey(d_213_encryptionContext_, d_211_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_216_valueOrError2_ = out30_
        if (d_216_valueOrError2_).IsFailure():
            output = (d_216_valueOrError2_).PropagateFailure()
            return output
        d_215_branchKey_ = (d_216_valueOrError2_).Extract()
        d_217_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_218_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_218_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_213_encryptionContext_, ((d_215_branchKey_).Plaintext).value)
        if (d_218_valueOrError3_).IsFailure():
            output = (d_218_valueOrError3_).PropagateFailure()
            return output
        d_217_branchKeyMaterials_ = (d_218_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_217_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        d_219_branchKeyItem_: _dafny.Map
        d_220_valueOrError0_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_220_valueOrError0_ = out31_
        if (d_220_valueOrError0_).IsFailure():
            output = (d_220_valueOrError0_).PropagateFailure()
            return output
        d_219_branchKeyItem_ = (d_220_valueOrError0_).Extract()
        d_221_encryptionContext_: _dafny.Map
        d_221_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_219_branchKeyItem_, logicalKeyStoreName)
        d_222_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_222_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_221_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_222_valueOrError1_).IsFailure():
            output = (d_222_valueOrError1_).PropagateFailure()
            return output
        d_223_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_224_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out32_: Wrappers.Result
        out32_ = KMSKeystoreOperations.default__.DecryptKey(d_221_encryptionContext_, d_219_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_224_valueOrError2_ = out32_
        if (d_224_valueOrError2_).IsFailure():
            output = (d_224_valueOrError2_).PropagateFailure()
            return output
        d_223_branchKey_ = (d_224_valueOrError2_).Extract()
        d_225_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_226_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_226_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_221_encryptionContext_, ((d_223_branchKey_).Plaintext).value)
        if (d_226_valueOrError3_).IsFailure():
            output = (d_226_valueOrError3_).PropagateFailure()
            return output
        d_225_branchKeyMaterials_ = (d_226_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_225_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        d_227_branchKeyItem_: _dafny.Map
        d_228_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_228_valueOrError0_ = out33_
        if (d_228_valueOrError0_).IsFailure():
            output = (d_228_valueOrError0_).PropagateFailure()
            return output
        d_227_branchKeyItem_ = (d_228_valueOrError0_).Extract()
        d_229_encryptionContext_: _dafny.Map
        d_229_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_227_branchKeyItem_, logicalKeyStoreName)
        d_230_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_230_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_229_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_230_valueOrError1_).IsFailure():
            output = (d_230_valueOrError1_).PropagateFailure()
            return output
        d_231_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_232_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out34_: Wrappers.Result
        out34_ = KMSKeystoreOperations.default__.DecryptKey(d_229_encryptionContext_, d_227_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_232_valueOrError2_ = out34_
        if (d_232_valueOrError2_).IsFailure():
            output = (d_232_valueOrError2_).PropagateFailure()
            return output
        d_231_branchKey_ = (d_232_valueOrError2_).Extract()
        d_233_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials
        d_234_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials.default())()
        d_234_valueOrError3_ = Structure.default__.ToBeaconKeyMaterials(d_229_encryptionContext_, ((d_231_branchKey_).Plaintext).value)
        if (d_234_valueOrError3_).IsFailure():
            output = (d_234_valueOrError3_).PropagateFailure()
            return output
        d_233_branchKeyMaterials_ = (d_234_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput_GetBeaconKeyOutput(d_233_branchKeyMaterials_))
        return output
        return output

