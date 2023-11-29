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

# assert "CreateKeys" == __name__
CreateKeys = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBranchAndBeaconKeys(branchKeyIdentifier, customEncryptionContext, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_176_decryptOnlyEncryptionContext_: _dafny.Map
        d_176_decryptOnlyEncryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, (kmsConfiguration).kmsKeyArn, customEncryptionContext)
        d_177_activeEncryptionContext_: _dafny.Map
        d_177_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_176_decryptOnlyEncryptionContext_)
        d_178_beaconEncryptionContext_: _dafny.Map
        d_178_beaconEncryptionContext_ = Structure.default__.BeaconKeyEncryptionContext(d_176_decryptOnlyEncryptionContext_)
        d_179_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_180_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out18_: Wrappers.Result
        out18_ = KMSKeystoreOperations.default__.GenerateKey(d_176_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_180_valueOrError0_ = out18_
        if (d_180_valueOrError0_).IsFailure():
            output = (d_180_valueOrError0_).PropagateFailure()
            return output
        d_179_wrappedDecryptOnlyBranchKey_ = (d_180_valueOrError0_).Extract()
        d_181_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_182_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out19_: Wrappers.Result
        out19_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_179_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_176_decryptOnlyEncryptionContext_, d_177_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_182_valueOrError1_ = out19_
        if (d_182_valueOrError1_).IsFailure():
            output = (d_182_valueOrError1_).PropagateFailure()
            return output
        d_181_wrappedActiveBranchKey_ = (d_182_valueOrError1_).Extract()
        d_183_wrappedBeaconKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_184_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out20_: Wrappers.Result
        out20_ = KMSKeystoreOperations.default__.GenerateKey(d_178_beaconEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_184_valueOrError2_ = out20_
        if (d_184_valueOrError2_).IsFailure():
            output = (d_184_valueOrError2_).PropagateFailure()
            return output
        d_183_wrappedBeaconKey_ = (d_184_valueOrError2_).Extract()
        d_185_decryptOnlyBranchKeyItem_: _dafny.Map
        d_185_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_176_decryptOnlyEncryptionContext_, ((d_179_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_186_activeBranchKeyItem_: _dafny.Map
        d_186_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_177_activeEncryptionContext_, ((d_181_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_187_beaconKeyItem_: _dafny.Map
        d_187_beaconKeyItem_ = Structure.default__.ToAttributeMap(d_178_beaconEncryptionContext_, ((d_183_wrappedBeaconKey_).CiphertextBlob).value)
        d_188___v0_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_189_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out21_: Wrappers.Result
        out21_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(d_185_decryptOnlyBranchKeyItem_, d_186_activeBranchKeyItem_, d_187_beaconKeyItem_, ddbTableName, ddbClient)
        d_189_valueOrError3_ = out21_
        if (d_189_valueOrError3_).IsFailure():
            output = (d_189_valueOrError3_).PropagateFailure()
            return output
        d_188___v0_ = (d_189_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput_CreateKeyOutput(branchKeyIdentifier))
        return output

    @staticmethod
    def VersionActiveBranchKey(input, timestamp, branchKeyVersion, ddbTableName, logicalKeyStoreName, kmsConfiguration, grantTokens, kmsClient, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_190_oldActiveItem_: _dafny.Map
        d_191_valueOrError0_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = DDBKeystoreOperations.default__.GetActiveBranchKeyItem((input).branchKeyIdentifier, ddbTableName, ddbClient)
        d_191_valueOrError0_ = out22_
        if (d_191_valueOrError0_).IsFailure():
            output = (d_191_valueOrError0_).PropagateFailure()
            return output
        d_190_oldActiveItem_ = (d_191_valueOrError0_).Extract()
        d_192_oldActiveEncryptionContext_: _dafny.Map
        d_192_oldActiveEncryptionContext_ = Structure.default__.ToBranchKeyContext(d_190_oldActiveItem_, logicalKeyStoreName)
        d_193_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_193_valueOrError1_ = Wrappers.default__.Need((True) and (KMSKeystoreOperations.default__.AttemptKmsOperation_q(kmsConfiguration, d_192_oldActiveEncryptionContext_)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Wrapping AWS KMS key in dynamodb does not match configured AWS KMS information.")))
        if (d_193_valueOrError1_).IsFailure():
            output = (d_193_valueOrError1_).PropagateFailure()
            return output
        d_194___v1_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_195_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out23_: Wrappers.Result
        out23_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_190_oldActiveItem_)[(Structure.default__).BRANCH__KEY__FIELD]).B, d_192_oldActiveEncryptionContext_, d_192_oldActiveEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_195_valueOrError2_ = out23_
        if (d_195_valueOrError2_).IsFailure():
            output = (d_195_valueOrError2_).PropagateFailure()
            return output
        d_194___v1_ = (d_195_valueOrError2_).Extract()
        d_196_decryptOnlyEncryptionContext_: _dafny.Map
        d_196_decryptOnlyEncryptionContext_ = Structure.default__.NewVersionFromActiveBranchKeyEncryptionContext(d_192_oldActiveEncryptionContext_, branchKeyVersion, timestamp)
        d_197_activeEncryptionContext_: _dafny.Map
        d_197_activeEncryptionContext_ = Structure.default__.ActiveBranchKeyEncryptionContext(d_196_decryptOnlyEncryptionContext_)
        d_198_wrappedDecryptOnlyBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_199_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        out24_: Wrappers.Result
        out24_ = KMSKeystoreOperations.default__.GenerateKey(d_196_decryptOnlyEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_199_valueOrError3_ = out24_
        if (d_199_valueOrError3_).IsFailure():
            output = (d_199_valueOrError3_).PropagateFailure()
            return output
        d_198_wrappedDecryptOnlyBranchKey_ = (d_199_valueOrError3_).Extract()
        d_200_wrappedActiveBranchKey_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_201_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        out25_: Wrappers.Result
        out25_ = KMSKeystoreOperations.default__.ReEncryptKey(((d_198_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value, d_196_decryptOnlyEncryptionContext_, d_197_activeEncryptionContext_, kmsConfiguration, grantTokens, kmsClient)
        d_201_valueOrError4_ = out25_
        if (d_201_valueOrError4_).IsFailure():
            output = (d_201_valueOrError4_).PropagateFailure()
            return output
        d_200_wrappedActiveBranchKey_ = (d_201_valueOrError4_).Extract()
        d_202_decryptOnlyBranchKeyItem_: _dafny.Map
        d_202_decryptOnlyBranchKeyItem_ = Structure.default__.ToAttributeMap(d_196_decryptOnlyEncryptionContext_, ((d_198_wrappedDecryptOnlyBranchKey_).CiphertextBlob).value)
        d_203_activeBranchKeyItem_: _dafny.Map
        d_203_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(d_197_activeEncryptionContext_, ((d_200_wrappedActiveBranchKey_).CiphertextBlob).value)
        d_204___v2_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_205_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        out26_: Wrappers.Result
        out26_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_202_decryptOnlyBranchKeyItem_, d_203_activeBranchKeyItem_, ddbTableName, ddbClient)
        d_205_valueOrError5_ = out26_
        if (d_205_valueOrError5_).IsFailure():
            output = (d_205_valueOrError5_).PropagateFailure()
            return output
        d_204___v2_ = (d_205_valueOrError5_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput_VersionKeyOutput())
        return output

