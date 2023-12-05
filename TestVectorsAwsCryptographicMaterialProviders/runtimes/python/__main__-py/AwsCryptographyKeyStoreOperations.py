import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import Aws_Cryptography
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
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
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

# Module: AwsCryptographyKeyStoreOperations

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
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        d_2086_ddbTableArn_: _dafny.Seq
        d_2087_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out374_: Wrappers.Result
        out374_ = CreateKeyStoreTable.default__.CreateKeyStoreTable((config).ddbTableName, (config).ddbClient)
        d_2087_valueOrError0_ = out374_
        if (d_2087_valueOrError0_).IsFailure():
            output = (d_2087_valueOrError0_).PropagateFailure()
            return output
        d_2086_ddbTableArn_ = (d_2087_valueOrError0_).Extract()
        d_2088_tableName_: Wrappers.Result
        d_2088_tableName_ = AwsArnParsing.default__.ParseAmazonDynamodbTableName(d_2086_ddbTableArn_)
        d_2089_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2089_valueOrError1_ = Wrappers.default__.Need(((d_2088_tableName_).is_Success) and (((d_2088_tableName_).value) == ((config).ddbTableName)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")))
        if (d_2089_valueOrError1_).IsFailure():
            output = (d_2089_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput_CreateKeyStoreOutput(d_2086_ddbTableArn_))
        return output

    @staticmethod
    def CreateKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_2090_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2090_valueOrError0_ = Wrappers.default__.Need(not (((input).branchKeyIdentifier).is_Some) or ((((input).encryptionContext).is_Some) and ((0) < (len(((input).encryptionContext).value)))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id requires custom encryption context.")))
        if (d_2090_valueOrError0_).IsFailure():
            output = (d_2090_valueOrError0_).PropagateFailure()
            return output
        d_2091_branchKeyIdentifier_: _dafny.Seq = _dafny.Seq({})
        if ((input).branchKeyIdentifier).is_None:
            d_2092_maybeBranchKeyId_: Wrappers.Result
            out375_: Wrappers.Result
            out375_ = UUID.default__.GenerateUUID()
            d_2092_maybeBranchKeyId_ = out375_
            d_2093_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda143_(d_2094_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2094_e_)

            d_2093_valueOrError1_ = (d_2092_maybeBranchKeyId_).MapFailure(lambda143_)
            if (d_2093_valueOrError1_).IsFailure():
                output = (d_2093_valueOrError1_).PropagateFailure()
                return output
            d_2091_branchKeyIdentifier_ = (d_2093_valueOrError1_).Extract()
        elif True:
            d_2095_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_2095_valueOrError2_ = Wrappers.default__.Need((0) < (len(((input).branchKeyIdentifier).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id can not be an empty string.")))
            if (d_2095_valueOrError2_).IsFailure():
                output = (d_2095_valueOrError2_).PropagateFailure()
                return output
            d_2091_branchKeyIdentifier_ = ((input).branchKeyIdentifier).value
        d_2096_timestamp_: _dafny.Seq
        d_2097_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda144_(d_2098_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2098_e_)

        d_2097_valueOrError3_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda144_)
        if (d_2097_valueOrError3_).IsFailure():
            output = (d_2097_valueOrError3_).PropagateFailure()
            return output
        d_2096_timestamp_ = (d_2097_valueOrError3_).Extract()
        d_2099_maybeBranchKeyVersion_: Wrappers.Result
        out376_: Wrappers.Result
        out376_ = UUID.default__.GenerateUUID()
        d_2099_maybeBranchKeyVersion_ = out376_
        d_2100_branchKeyVersion_: _dafny.Seq
        d_2101_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda145_(d_2102_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2102_e_)

        d_2101_valueOrError4_ = (d_2099_maybeBranchKeyVersion_).MapFailure(lambda145_)
        if (d_2101_valueOrError4_).IsFailure():
            output = (d_2101_valueOrError4_).PropagateFailure()
            return output
        d_2100_branchKeyVersion_ = (d_2101_valueOrError4_).Extract()
        d_2103_unwrapEncryptionContext_: _dafny.Map
        d_2103_unwrapEncryptionContext_ = ((input).encryptionContext).UnwrapOr(_dafny.Map({}))
        d_2104_encodedEncryptionContext_: _dafny.Set
        def iife69_():
            coll25_ = _dafny.Set()
            compr_30_: _dafny.Seq
            for compr_30_ in (d_2103_unwrapEncryptionContext_).keys.Elements:
                d_2105_k_: _dafny.Seq = compr_30_
                if (d_2105_k_) in (d_2103_unwrapEncryptionContext_):
                    coll25_ = coll25_.union(_dafny.Set([(UTF8.default__.Decode(d_2105_k_), UTF8.default__.Decode((d_2103_unwrapEncryptionContext_)[d_2105_k_]), d_2105_k_)]))
            return _dafny.Set(coll25_)
        d_2104_encodedEncryptionContext_ = iife69_()
        
        d_2106_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda146_(forall_var_25_):
            def iife70_(_pat_let22_0):
                def iife71_(d_2108_encoded_):
                    return ((d_2108_encoded_).is_Success) and (((d_2107_i_)[2]) == ((d_2108_encoded_).value))
                return iife71_(_pat_let22_0)
            d_2107_i_: tuple = forall_var_25_
            return not ((d_2107_i_) in (d_2104_encodedEncryptionContext_)) or ((((((d_2107_i_)[0]).is_Success) and (((d_2107_i_)[1]).is_Success)) and (software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (((d_2107_i_)[0]).value)))) and (iife70_(UTF8.default__.Encode(((d_2107_i_)[0]).value))))

        d_2106_valueOrError5_ = Wrappers.default__.Need(_dafny.quantifier((d_2104_encodedEncryptionContext_).Elements, True, lambda146_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_2106_valueOrError5_).IsFailure():
            output = (d_2106_valueOrError5_).PropagateFailure()
            return output
        out377_: Wrappers.Result
        def iife72_():
            coll26_ = _dafny.Map()
            compr_31_: tuple
            for compr_31_ in (d_2104_encodedEncryptionContext_).Elements:
                d_2109_i_: tuple = compr_31_
                if (d_2109_i_) in (d_2104_encodedEncryptionContext_):
                    coll26_[((d_2109_i_)[0]).value] = ((d_2109_i_)[1]).value
            return _dafny.Map(coll26_)
        out377_ = CreateKeys.default__.CreateBranchAndBeaconKeys(d_2091_branchKeyIdentifier_, iife72_()
        , d_2096_timestamp_, d_2100_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out377_
        return output

    @staticmethod
    def VersionKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_2110_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2110_valueOrError0_ = Wrappers.default__.Need((0) < (len((input).branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Empty string not supported for identifier.")))
        if (d_2110_valueOrError0_).IsFailure():
            output = (d_2110_valueOrError0_).PropagateFailure()
            return output
        d_2111_timestamp_: _dafny.Seq
        d_2112_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda147_(d_2113_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2113_e_)

        d_2112_valueOrError1_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda147_)
        if (d_2112_valueOrError1_).IsFailure():
            output = (d_2112_valueOrError1_).PropagateFailure()
            return output
        d_2111_timestamp_ = (d_2112_valueOrError1_).Extract()
        d_2114_maybeBranchKeyVersion_: Wrappers.Result
        out378_: Wrappers.Result
        out378_ = UUID.default__.GenerateUUID()
        d_2114_maybeBranchKeyVersion_ = out378_
        d_2115_branchKeyVersion_: _dafny.Seq
        d_2116_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda148_(d_2117_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2117_e_)

        d_2116_valueOrError2_ = (d_2114_maybeBranchKeyVersion_).MapFailure(lambda148_)
        if (d_2116_valueOrError2_).IsFailure():
            output = (d_2116_valueOrError2_).PropagateFailure()
            return output
        d_2115_branchKeyVersion_ = (d_2116_valueOrError2_).Extract()
        out379_: Wrappers.Result
        out379_ = CreateKeys.default__.VersionActiveBranchKey(input, d_2111_timestamp_, d_2115_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out379_
        return output

    @staticmethod
    def GetActiveBranchKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out380_: Wrappers.Result
        out380_ = GetKeys.default__.GetActiveKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out380_
        return output

    @staticmethod
    def GetBranchKeyVersion(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out381_: Wrappers.Result
        out381_ = GetKeys.default__.GetBranchKeyVersion(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out381_
        return output

    @staticmethod
    def GetBeaconKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out382_: Wrappers.Result
        out382_ = GetKeys.default__.GetBeaconKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out382_
        return output


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration.default()(), _dafny.Seq({}), None, None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [('id', Any), ('ddbTableName', Any), ('logicalKeyStoreName', Any), ('kmsConfiguration', Any), ('grantTokens', Any), ('kmsClient', Any), ('ddbClient', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyKeyStoreOperations.Config.Config({_dafny.string_of(self.id)}, {_dafny.string_of(self.ddbTableName)}, {_dafny.string_of(self.logicalKeyStoreName)}, {_dafny.string_of(self.kmsConfiguration)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.ddbClient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config) and self.id == __o.id and self.ddbTableName == __o.ddbTableName and self.logicalKeyStoreName == __o.logicalKeyStoreName and self.kmsConfiguration == __o.kmsConfiguration and self.grantTokens == __o.grantTokens and self.kmsClient == __o.kmsClient and self.ddbClient == __o.ddbClient
    def __hash__(self) -> int:
        return super().__hash__()

