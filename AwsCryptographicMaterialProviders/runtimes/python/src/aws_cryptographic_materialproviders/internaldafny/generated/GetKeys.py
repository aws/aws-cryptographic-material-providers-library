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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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
        output: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.default())()
        d_210_branchKeyItem_: _dafny.Map
        d_211_valueOrError0_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_211_valueOrError0_ = out29_
        if (d_211_valueOrError0_).IsFailure():
            output = (d_211_valueOrError0_).PropagateFailure()
            return output
        d_210_branchKeyItem_ = (d_211_valueOrError0_).Extract()
        d_212_encryptionContext_: _dafny.Map
        d_212_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_210_branchKeyItem_, logicalKeyStoreName)
        d_213_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_213_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_212_encryptionContext_), software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_213_valueOrError1_).IsFailure():
            output = (d_213_valueOrError1_).PropagateFailure()
            return output
        d_214_branchKey_: software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse
        d_215_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.default())()
        out30_: Wrappers.Result
        out30_ = KMSKeystoreOperations.default__.DecryptKey(d_212_encryptionContext_, d_210_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_215_valueOrError2_ = out30_
        if (d_215_valueOrError2_).IsFailure():
            output = (d_215_valueOrError2_).PropagateFailure()
            return output
        d_214_branchKey_ = (d_215_valueOrError2_).Extract()
        d_216_branchKeyMaterials_: software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials
        d_217_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.default())()
        d_217_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_212_encryptionContext_, ((d_214_branchKey_).Plaintext).value)
        if (d_217_valueOrError3_).IsFailure():
            output = (d_217_valueOrError3_).PropagateFailure()
            return output
        d_216_branchKeyMaterials_ = (d_217_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput_GetActiveBranchKeyOutput(d_216_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBranchKeyVersion(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.default())()
        d_218_branchKeyItem_: _dafny.Map
        d_219_valueOrError0_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = DDBKeystoreOperations.default__.GetVersionBranchKeyItem((input).branchKeyIdentifier, (input).branchKeyVersion, tableName, ddbClient)
        d_219_valueOrError0_ = out31_
        if (d_219_valueOrError0_).IsFailure():
            output = (d_219_valueOrError0_).PropagateFailure()
            return output
        d_218_branchKeyItem_ = (d_219_valueOrError0_).Extract()
        d_220_encryptionContext_: _dafny.Map
        d_220_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_218_branchKeyItem_, logicalKeyStoreName)
        d_221_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_221_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_220_encryptionContext_), software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_221_valueOrError1_).IsFailure():
            output = (d_221_valueOrError1_).PropagateFailure()
            return output
        d_222_branchKey_: software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse
        d_223_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.default())()
        out32_: Wrappers.Result
        out32_ = KMSKeystoreOperations.default__.DecryptKey(d_220_encryptionContext_, d_218_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_223_valueOrError2_ = out32_
        if (d_223_valueOrError2_).IsFailure():
            output = (d_223_valueOrError2_).PropagateFailure()
            return output
        d_222_branchKey_ = (d_223_valueOrError2_).Extract()
        d_224_branchKeyMaterials_: software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials
        d_225_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.default())()
        d_225_valueOrError3_ = Structure.default__.ToBranchKeyMaterials(d_220_encryptionContext_, ((d_222_branchKey_).Plaintext).value)
        if (d_225_valueOrError3_).IsFailure():
            output = (d_225_valueOrError3_).PropagateFailure()
            return output
        d_224_branchKeyMaterials_ = (d_225_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput_GetBranchKeyVersionOutput(d_224_branchKeyMaterials_))
        return output
        return output

    @staticmethod
    def GetBeaconKeyAndUnwrap(input, tableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.default())()
        d_226_branchKeyItem_: _dafny.Map
        d_227_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = DDBKeystoreOperations.default__.GetBeaconKeyItem((input).branchKeyIdentifier, tableName, ddbClient)
        d_227_valueOrError0_ = out33_
        if (d_227_valueOrError0_).IsFailure():
            output = (d_227_valueOrError0_).PropagateFailure()
            return output
        d_226_branchKeyItem_ = (d_227_valueOrError0_).Extract()
        d_228_encryptionContext_: _dafny.Map
        d_228_encryptionContext_ = Structure.default__.ToBranchKeyContext(d_226_branchKeyItem_, logicalKeyStoreName)
        d_229_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_229_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_228_encryptionContext_), software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException(_dafny.Seq("AWS KMS Key ARN does not match configured value")))
        if (d_229_valueOrError1_).IsFailure():
            output = (d_229_valueOrError1_).PropagateFailure()
            return output
        d_230_branchKey_: software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse
        d_231_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.default())()
        out34_: Wrappers.Result
        out34_ = KMSKeystoreOperations.default__.DecryptKey(d_228_encryptionContext_, d_226_branchKeyItem_, kmsConfiguration, grantTokens, kmsClient)
        d_231_valueOrError2_ = out34_
        if (d_231_valueOrError2_).IsFailure():
            output = (d_231_valueOrError2_).PropagateFailure()
            return output
        d_230_branchKey_ = (d_231_valueOrError2_).Extract()
        d_232_branchKeyMaterials_: software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials
        d_233_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials.default())()
        d_233_valueOrError3_ = Structure.default__.ToBeaconKeyMaterials(d_228_encryptionContext_, ((d_230_branchKey_).Plaintext).value)
        if (d_233_valueOrError3_).IsFailure():
            output = (d_233_valueOrError3_).PropagateFailure()
            return output
        d_232_branchKeyMaterials_ = (d_233_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput_GetBeaconKeyOutput(d_232_branchKeyMaterials_))
        return output
        return output

