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
import CreateKeys
import CreateKeyStoreTable

# Module: GetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetActiveKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        d_226_branchKeyItem_: _dafny.Map
        d_227_valueOrError0_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_227_valueOrError0_ = out29_
        if (d_227_valueOrError0_).IsFailure():
            output = (d_227_valueOrError0_).PropagateFailure()
            return output
        d_226_branchKeyItem_ = (d_227_valueOrError0_).Extract()
        d_228_encryptionContext_: _dafny.Map
        d_228_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_226_branchKeyItem_, logicalKeyStoreName)
        d_229_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_229_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_228_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_229_valueOrError1_).IsFailure():
            output = (d_229_valueOrError1_).PropagateFailure()
            return output
        d_230_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_231_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out30_: Wrappers.Result
        out30_ = KMSKeystoreOperations.default__.DecryptKey(d_228_encryptionContext_, d_226_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_231_valueOrError2_ = out30_
        if (d_231_valueOrError2_).IsFailure():
            output = (d_231_valueOrError2_).PropagateFailure()
            return output
        d_230_branchKey_ = (d_231_valueOrError2_).Extract()
        d_232_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_233_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_233_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_228_encryptionContext_, ((d_230_branchKey_).Plaintext).value)
        if (d_233_valueOrError3_).IsFailure():
            output = (d_233_valueOrError3_).PropagateFailure()
            return output
        d_232_branchKeyMaterials_ = (d_233_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_232_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        d_234_branchKeyItem_: _dafny.Map
        d_235_valueOrError0_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_235_valueOrError0_ = out31_
        if (d_235_valueOrError0_).IsFailure():
            output = (d_235_valueOrError0_).PropagateFailure()
            return output
        d_234_branchKeyItem_ = (d_235_valueOrError0_).Extract()
        d_236_encryptionContext_: _dafny.Map
        d_236_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_234_branchKeyItem_, logicalKeyStoreName)
        d_237_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_237_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_236_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_237_valueOrError1_).IsFailure():
            output = (d_237_valueOrError1_).PropagateFailure()
            return output
        d_238_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_239_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out32_: Wrappers.Result
        out32_ = KMSKeystoreOperations.default__.DecryptKey(d_236_encryptionContext_, d_234_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_239_valueOrError2_ = out32_
        if (d_239_valueOrError2_).IsFailure():
            output = (d_239_valueOrError2_).PropagateFailure()
            return output
        d_238_branchKey_ = (d_239_valueOrError2_).Extract()
        d_240_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_241_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_241_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_236_encryptionContext_, ((d_238_branchKey_).Plaintext).value)
        if (d_241_valueOrError3_).IsFailure():
            output = (d_241_valueOrError3_).PropagateFailure()
            return output
        d_240_branchKeyMaterials_ = (d_241_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_240_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        d_242_branchKeyItem_: _dafny.Map
        d_243_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_243_valueOrError0_ = out33_
        if (d_243_valueOrError0_).IsFailure():
            output = (d_243_valueOrError0_).PropagateFailure()
            return output
        d_242_branchKeyItem_ = (d_243_valueOrError0_).Extract()
        d_244_encryptionContext_: _dafny.Map
        d_244_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_242_branchKeyItem_, logicalKeyStoreName)
        d_245_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_245_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_244_encryptionContext_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_245_valueOrError1_).IsFailure():
            output = (d_245_valueOrError1_).PropagateFailure()
            return output
        d_246_branchKey_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_247_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        out34_: Wrappers.Result
        out34_ = KMSKeystoreOperations.default__.DecryptKey(d_244_encryptionContext_, d_242_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_247_valueOrError2_ = out34_
        if (d_247_valueOrError2_).IsFailure():
            output = (d_247_valueOrError2_).PropagateFailure()
            return output
        d_246_branchKey_ = (d_247_valueOrError2_).Extract()
        d_248_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials
        d_249_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials.default())()
        d_249_valueOrError3_ = Structure.default__.ToBeaconKeyMaterials(d_244_encryptionContext_, ((d_246_branchKey_).Plaintext).value)
        if (d_249_valueOrError3_).IsFailure():
            output = (d_249_valueOrError3_).PropagateFailure()
            return output
        d_248_branchKeyMaterials_ = (d_249_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput_GetBeaconKeyOutput(d_248_branchKeyMaterials_))
        return output
        return output

