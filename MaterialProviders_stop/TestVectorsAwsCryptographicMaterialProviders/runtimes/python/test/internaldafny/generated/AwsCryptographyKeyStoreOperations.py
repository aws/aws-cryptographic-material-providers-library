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
import GetKeys

assert "AwsCryptographyKeyStoreOperations" == __name__
AwsCryptographyKeyStoreOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetKeyStoreInfo(config):
        output: Wrappers.Result = None
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.GetKeyStoreInfoOutput_GetKeyStoreInfoOutput((config).id, (config).ddbTableName, (config).logicalKeyStoreName, (config).grantTokens, (config).kmsConfiguration))
        return output

    @staticmethod
    def CreateKeyStore(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        d_2084_ddbTableArn_: _dafny.Seq
        d_2085_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out374_: Wrappers.Result
        out374_ = CreateKeyStoreTable.default__.CreateKeyStoreTable((config).ddbTableName, (config).ddbClient)
        d_2085_valueOrError0_ = out374_
        if (d_2085_valueOrError0_).IsFailure():
            output = (d_2085_valueOrError0_).PropagateFailure()
            return output
        d_2084_ddbTableArn_ = (d_2085_valueOrError0_).Extract()
        d_2086_tableName_: Wrappers.Result
        d_2086_tableName_ = AwsArnParsing.default__.ParseAmazonDynamodbTableName(d_2084_ddbTableArn_)
        d_2087_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2087_valueOrError1_ = Wrappers.default__.Need(((d_2086_tableName_).is_Success) and (((d_2086_tableName_).value) == ((config).ddbTableName)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")))
        if (d_2087_valueOrError1_).IsFailure():
            output = (d_2087_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput_CreateKeyStoreOutput(d_2084_ddbTableArn_))
        return output

    @staticmethod
    def CreateKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_2088_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2088_valueOrError0_ = Wrappers.default__.Need(not (((input).branchKeyIdentifier).is_Some) or ((((input).encryptionContext).is_Some) and ((0) < (len(((input).encryptionContext).value)))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id requires custom encryption context.")))
        if (d_2088_valueOrError0_).IsFailure():
            output = (d_2088_valueOrError0_).PropagateFailure()
            return output
        d_2089_branchKeyIdentifier_: _dafny.Seq = _dafny.Seq({})
        if ((input).branchKeyIdentifier).is_None:
            d_2090_maybeBranchKeyId_: Wrappers.Result
            out375_: Wrappers.Result
            out375_ = UUID.default__.GenerateUUID()
            d_2090_maybeBranchKeyId_ = out375_
            d_2091_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
            def lambda143_(d_2092_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2092_e_)

            d_2091_valueOrError1_ = (d_2090_maybeBranchKeyId_).MapFailure(lambda143_)
            if (d_2091_valueOrError1_).IsFailure():
                output = (d_2091_valueOrError1_).PropagateFailure()
                return output
            d_2089_branchKeyIdentifier_ = (d_2091_valueOrError1_).Extract()
        elif True:
            d_2093_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_2093_valueOrError2_ = Wrappers.default__.Need((0) < (len(((input).branchKeyIdentifier).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id can not be an empty string.")))
            if (d_2093_valueOrError2_).IsFailure():
                output = (d_2093_valueOrError2_).PropagateFailure()
                return output
            d_2089_branchKeyIdentifier_ = ((input).branchKeyIdentifier).value
        d_2094_timestamp_: _dafny.Seq
        d_2095_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda144_(d_2096_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2096_e_)

        d_2095_valueOrError3_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda144_)
        if (d_2095_valueOrError3_).IsFailure():
            output = (d_2095_valueOrError3_).PropagateFailure()
            return output
        d_2094_timestamp_ = (d_2095_valueOrError3_).Extract()
        d_2097_maybeBranchKeyVersion_: Wrappers.Result
        out376_: Wrappers.Result
        out376_ = UUID.default__.GenerateUUID()
        d_2097_maybeBranchKeyVersion_ = out376_
        d_2098_branchKeyVersion_: _dafny.Seq
        d_2099_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda145_(d_2100_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2100_e_)

        d_2099_valueOrError4_ = (d_2097_maybeBranchKeyVersion_).MapFailure(lambda145_)
        if (d_2099_valueOrError4_).IsFailure():
            output = (d_2099_valueOrError4_).PropagateFailure()
            return output
        d_2098_branchKeyVersion_ = (d_2099_valueOrError4_).Extract()
        d_2101_unwrapEncryptionContext_: _dafny.Map
        d_2101_unwrapEncryptionContext_ = ((input).encryptionContext).UnwrapOr(_dafny.Map({}))
        d_2102_encodedEncryptionContext_: _dafny.Set
        def iife109_():
            coll25_ = _dafny.Set()
            compr_30_: _dafny.Seq
            for compr_30_ in (d_2101_unwrapEncryptionContext_).keys.Elements:
                d_2103_k_: _dafny.Seq = compr_30_
                if (d_2103_k_) in (d_2101_unwrapEncryptionContext_):
                    coll25_ = coll25_.union(_dafny.Set([(UTF8.default__.Decode(d_2103_k_), UTF8.default__.Decode((d_2101_unwrapEncryptionContext_)[d_2103_k_]), d_2103_k_)]))
            return _dafny.Set(coll25_)
        d_2102_encodedEncryptionContext_ = iife109_()
        
        d_2104_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda146_(forall_var_25_):
            def iife110_(_pat_let42_0):
                def iife111_(d_2106_encoded_):
                    return ((d_2106_encoded_).is_Success) and (((d_2105_i_)[2]) == ((d_2106_encoded_).value))
                return iife111_(_pat_let42_0)
            d_2105_i_: tuple = forall_var_25_
            return not ((d_2105_i_) in (d_2102_encodedEncryptionContext_)) or ((((((d_2105_i_)[0]).is_Success) and (((d_2105_i_)[1]).is_Success)) and (software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(((Structure.default__).ENCRYPTION__CONTEXT__PREFIX) + (((d_2105_i_)[0]).value)))) and (iife110_(UTF8.default__.Encode(((d_2105_i_)[0]).value))))

        d_2104_valueOrError5_ = Wrappers.default__.Need(_dafny.quantifier((d_2102_encodedEncryptionContext_).Elements, True, lambda146_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_2104_valueOrError5_).IsFailure():
            output = (d_2104_valueOrError5_).PropagateFailure()
            return output
        def iife112_():
            coll26_ = _dafny.Map()
            compr_31_: tuple
            for compr_31_ in (d_2102_encodedEncryptionContext_).Elements:
                d_2107_i_: tuple = compr_31_
                if (d_2107_i_) in (d_2102_encodedEncryptionContext_):
                    coll26_[((d_2107_i_)[0]).value] = ((d_2107_i_)[1]).value
            return _dafny.Map(coll26_)
        out377_: Wrappers.Result
        out377_ = CreateKeys.default__.CreateBranchAndBeaconKeys(d_2089_branchKeyIdentifier_, iife112_()
        , d_2094_timestamp_, d_2098_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out377_
        return output

    @staticmethod
    def VersionKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_2108_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_2108_valueOrError0_ = Wrappers.default__.Need((0) < (len((input).branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Empty string not supported for identifier.")))
        if (d_2108_valueOrError0_).IsFailure():
            output = (d_2108_valueOrError0_).PropagateFailure()
            return output
        d_2109_timestamp_: _dafny.Seq
        d_2110_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda147_(d_2111_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2111_e_)

        d_2110_valueOrError1_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda147_)
        if (d_2110_valueOrError1_).IsFailure():
            output = (d_2110_valueOrError1_).PropagateFailure()
            return output
        d_2109_timestamp_ = (d_2110_valueOrError1_).Extract()
        d_2112_maybeBranchKeyVersion_: Wrappers.Result
        out378_: Wrappers.Result
        out378_ = UUID.default__.GenerateUUID()
        d_2112_maybeBranchKeyVersion_ = out378_
        d_2113_branchKeyVersion_: _dafny.Seq
        d_2114_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda148_(d_2115_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2115_e_)

        d_2114_valueOrError2_ = (d_2112_maybeBranchKeyVersion_).MapFailure(lambda148_)
        if (d_2114_valueOrError2_).IsFailure():
            output = (d_2114_valueOrError2_).PropagateFailure()
            return output
        d_2113_branchKeyVersion_ = (d_2114_valueOrError2_).Extract()
        out379_: Wrappers.Result
        out379_ = CreateKeys.default__.VersionActiveBranchKey(input, d_2109_timestamp_, d_2113_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out379_
        return output

    @staticmethod
    def GetActiveBranchKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out380_: Wrappers.Result
        out380_ = GetKeys.default__.GetActiveKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out380_
        return output

    @staticmethod
    def GetBranchKeyVersion(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out381_: Wrappers.Result
        out381_ = GetKeys.default__.GetBranchKeyVersion(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out381_
        return output

    @staticmethod
    def GetBeaconKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out382_: Wrappers.Result
        out382_ = GetKeys.default__.GetBeaconKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out382_
        return output


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn.default()(), _dafny.Seq({}), None, None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, AwsCryptographyKeyStoreOperations.Config_Config)

class Config_Config(Config, NamedTuple('Config', [('id', Any), ('ddbTableName', Any), ('logicalKeyStoreName', Any), ('kmsConfiguration', Any), ('grantTokens', Any), ('kmsClient', Any), ('ddbClient', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreOperations.Config.Config({_dafny.string_of(self.id)}, {_dafny.string_of(self.ddbTableName)}, {_dafny.string_of(self.logicalKeyStoreName)}, {_dafny.string_of(self.kmsConfiguration)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.ddbClient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsCryptographyKeyStoreOperations.Config_Config) and self.id == __o.id and self.ddbTableName == __o.ddbTableName and self.logicalKeyStoreName == __o.logicalKeyStoreName and self.kmsConfiguration == __o.kmsConfiguration and self.grantTokens == __o.grantTokens and self.kmsClient == __o.kmsClient and self.ddbClient == __o.ddbClient
    def __hash__(self) -> int:
        return super().__hash__()

