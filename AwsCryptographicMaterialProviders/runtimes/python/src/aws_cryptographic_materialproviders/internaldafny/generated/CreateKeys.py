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
        d_175_decryptOnlyEncryptionContext_: _dafny.Map
        d_175_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, (kmsConfiguration).kmsKeyArn, customEncryptionContext)
        d_176_activeEncryptionContext_: _dafny.Map
        d_176_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_175_decryptOnlyEncryptionContext_)
        d_177_beaconEncryptionContext_: _dafny.Map
        d_177_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_175_decryptOnlyEncryptionContext_)
        d_178_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_179_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out18_: Wrappers.Result
        out18_ = KMSKeystoreOperations.default__.GenerateKey(d_175_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_179_valueOrError0_ = out18_
        if (d_179_valueOrError0_).IsFailure():
            output = (d_179_valueOrError0_).PropagateFailure()
            return output
        d_178_wrappedDecryptOnlyBranchKey_ = (d_179_valueOrError0_).Extract()
        d_180_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_181_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out19_: Wrappers.Result
        out19_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_178_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_175_decryptOnlyEncryptionContext_, d_176_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_181_valueOrError1_ = out19_
        if (d_181_valueOrError1_).IsFailure():
            output = (d_181_valueOrError1_).PropagateFailure()
            return output
        d_180_wrappedActiveBranchKey_ = (d_181_valueOrError1_).Extract()
        d_182_wrappedBeaconKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_183_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out20_: Wrappers.Result
        out20_ = KMSKeystoreOperations.default__.GenerateKey(d_177_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_183_valueOrError2_ = out20_
        if (d_183_valueOrError2_).IsFailure():
            output = (d_183_valueOrError2_).PropagateFailure()
            return output
        d_182_wrappedBeaconKey_ = (d_183_valueOrError2_).Extract()
        d_184_decryptOnlyBranchKeyItem_: _dafny.Map
        d_184_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_175_decryptOnlyEncryptionContext_, ((d_178_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_185_activeBranchKeyItem_: _dafny.Map
        d_185_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_176_activeEncryptionContext_, ((d_180_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_186_beaconKeyItem_: _dafny.Map
        d_186_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_177_beaconEncryptionContext_, ((d_182_wrappedBeaconKey_).CiphertextBlob).value)
        d_187___v0_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_188_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out21_: Wrappers.Result
        out21_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_184_decryptOnlyBranchKeyItem_, d_185_activeBranchKeyItem_, d_186_beaconKeyItem_, ddbTableName, ddbClient)
        d_188_valueOrError3_ = out21_
        if (d_188_valueOrError3_).IsFailure():
            output = (d_188_valueOrError3_).PropagateFailure()
            return output
        d_187___v0_ = (d_188_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_189_oldActiveItem_: _dafny.Map
        d_190_valueOrError0_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_190_valueOrError0_ = out22_
        if (d_190_valueOrError0_).IsFailure():
            output = (d_190_valueOrError0_).PropagateFailure()
            return output
        d_189_oldActiveItem_ = (d_190_valueOrError0_).Extract()
        d_191_oldActiveEncryptionContext_: _dafny.Map
        d_191_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_189_oldActiveItem_, logicalKeyStoreName)
        d_192_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_192_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_191_oldActiveEncryptionContext_)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Wrapping AWS KMS key in dynamodb does not match configured AWS KMS information.")))
        if (d_192_valueOrError1_).IsFailure():
            output = (d_192_valueOrError1_).PropagateFailure()
            return output
        d_193___v1_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_194_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out23_: Wrappers.Result
        out23_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_189_oldActiveItem_)[Structure.default__.BRANCH__KEY__FIELD]).B, d_191_oldActiveEncryptionContext_, d_191_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_194_valueOrError2_ = out23_
        if (d_194_valueOrError2_).IsFailure():
            output = (d_194_valueOrError2_).PropagateFailure()
            return output
        d_193___v1_ = (d_194_valueOrError2_).Extract()
        d_195_decryptOnlyEncryptionContext_: _dafny.Map
        d_195_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_191_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_196_activeEncryptionContext_: _dafny.Map
        d_196_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_195_decryptOnlyEncryptionContext_)
        d_197_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_198_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out24_: Wrappers.Result
        out24_ = KMSKeystoreOperations.default__.GenerateKey(d_195_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_198_valueOrError3_ = out24_
        if (d_198_valueOrError3_).IsFailure():
            output = (d_198_valueOrError3_).PropagateFailure()
            return output
        d_197_wrappedDecryptOnlyBranchKey_ = (d_198_valueOrError3_).Extract()
        d_199_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_200_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out25_: Wrappers.Result
        out25_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_197_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_195_decryptOnlyEncryptionContext_, d_196_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_200_valueOrError4_ = out25_
        if (d_200_valueOrError4_).IsFailure():
            output = (d_200_valueOrError4_).PropagateFailure()
            return output
        d_199_wrappedActiveBranchKey_ = (d_200_valueOrError4_).Extract()
        d_201_decryptOnlyBranchKeyItem_: _dafny.Map
        d_201_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_195_decryptOnlyEncryptionContext_, ((d_197_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_202_activeBranchKeyItem_: _dafny.Map
        d_202_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_196_activeEncryptionContext_, ((d_199_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_203___v2_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_204_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out26_: Wrappers.Result
        out26_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_201_decryptOnlyBranchKeyItem_, d_202_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_204_valueOrError5_ = out26_
        if (d_204_valueOrError5_).IsFailure():
            output = (d_204_valueOrError5_).PropagateFailure()
            return output
        d_203___v2_ = (d_204_valueOrError5_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput_VersionKeyOutput())
        return output

