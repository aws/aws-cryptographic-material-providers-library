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
        d_235_ddbTableArn_: _dafny.Seq
        d_236_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out35_: Wrappers.Result
        out35_ = CreateKeyStoreTable.default__.CreateKeyStoreTable((config).ddbTableName, (config).ddbClient)
        d_236_valueOrError0_ = out35_
        if (d_236_valueOrError0_).IsFailure():
            output = (d_236_valueOrError0_).PropagateFailure()
            return output
        d_235_ddbTableArn_ = (d_236_valueOrError0_).Extract()
        d_237_tableName_: Wrappers.Result
        d_237_tableName_ = AwsArnParsing.default__.ParseAmazonDynamodbTableName(d_235_ddbTableArn_)
        d_238_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_238_valueOrError1_ = Wrappers.default__.Need(((d_237_tableName_).is_Success) and (((d_237_tableName_).value) == ((config).ddbTableName)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")))
        if (d_238_valueOrError1_).IsFailure():
            output = (d_238_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput_CreateKeyStoreOutput(d_235_ddbTableArn_))
        return output

    @staticmethod
    def CreateKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        d_239_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_239_valueOrError0_ = Wrappers.default__.Need(not (((input).branchKeyIdentifier).is_Some) or ((((input).encryptionContext).is_Some) and ((0) < (len(((input).encryptionContext).value)))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id requires custom encryption context.")))
        if (d_239_valueOrError0_).IsFailure():
            output = (d_239_valueOrError0_).PropagateFailure()
            return output
        d_240_branchKeyIdentifier_: _dafny.Seq = _dafny.Seq({})
        if ((input).branchKeyIdentifier).is_None:
            d_241_maybeBranchKeyId_: Wrappers.Result
            out36_: Wrappers.Result
            out36_ = UUID.default__.GenerateUUID()
            d_241_maybeBranchKeyId_ = out36_
            d_242_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
            def lambda20_(d_243_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_243_e_)

            d_242_valueOrError1_ = (d_241_maybeBranchKeyId_).MapFailure(lambda20_)
            if (d_242_valueOrError1_).IsFailure():
                output = (d_242_valueOrError1_).PropagateFailure()
                return output
            d_240_branchKeyIdentifier_ = (d_242_valueOrError1_).Extract()
        elif True:
            d_244_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_244_valueOrError2_ = Wrappers.default__.Need((0) < (len(((input).branchKeyIdentifier).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Custom branch key id can not be an empty string.")))
            if (d_244_valueOrError2_).IsFailure():
                output = (d_244_valueOrError2_).PropagateFailure()
                return output
            d_240_branchKeyIdentifier_ = ((input).branchKeyIdentifier).value
        d_245_timestamp_: _dafny.Seq
        d_246_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda21_(d_247_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_247_e_)

        d_246_valueOrError3_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda21_)
        if (d_246_valueOrError3_).IsFailure():
            output = (d_246_valueOrError3_).PropagateFailure()
            return output
        d_245_timestamp_ = (d_246_valueOrError3_).Extract()
        d_248_maybeBranchKeyVersion_: Wrappers.Result
        out37_: Wrappers.Result
        out37_ = UUID.default__.GenerateUUID()
        d_248_maybeBranchKeyVersion_ = out37_
        d_249_branchKeyVersion_: _dafny.Seq
        d_250_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda22_(d_251_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_251_e_)

        d_250_valueOrError4_ = (d_248_maybeBranchKeyVersion_).MapFailure(lambda22_)
        if (d_250_valueOrError4_).IsFailure():
            output = (d_250_valueOrError4_).PropagateFailure()
            return output
        d_249_branchKeyVersion_ = (d_250_valueOrError4_).Extract()
        d_252_unwrapEncryptionContext_: _dafny.Map
        d_252_unwrapEncryptionContext_ = ((input).encryptionContext).UnwrapOr(_dafny.Map({}))
        d_253_encodedEncryptionContext_: _dafny.Set
        def iife7_():
            coll7_ = _dafny.Set()
            compr_7_: _dafny.Seq
            for compr_7_ in (d_252_unwrapEncryptionContext_).keys.Elements:
                d_254_k_: _dafny.Seq = compr_7_
                if (d_254_k_) in (d_252_unwrapEncryptionContext_):
                    coll7_ = coll7_.union(_dafny.Set([(UTF8.default__.Decode(d_254_k_), UTF8.default__.Decode((d_252_unwrapEncryptionContext_)[d_254_k_]), d_254_k_)]))
            return _dafny.Set(coll7_)
        d_253_encodedEncryptionContext_ = iife7_()
        
        d_255_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda23_(forall_var_7_):
            def iife8_(_pat_let0_0):
                def iife9_(d_257_encoded_):
                    return ((d_257_encoded_).is_Success) and (((d_256_i_)[2]) == ((d_257_encoded_).value))
                return iife9_(_pat_let0_0)
            d_256_i_: tuple = forall_var_7_
            return not ((d_256_i_) in (d_253_encodedEncryptionContext_)) or ((((((d_256_i_)[0]).is_Success) and (((d_256_i_)[1]).is_Success)) and (software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(((Structure.default__).ENCRYPTION__CONTEXT__PREFIX) + (((d_256_i_)[0]).value)))) and (iife8_(UTF8.default__.Encode(((d_256_i_)[0]).value))))

        d_255_valueOrError5_ = Wrappers.default__.Need(_dafny.quantifier((d_253_encodedEncryptionContext_).Elements, True, lambda23_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_255_valueOrError5_).IsFailure():
            output = (d_255_valueOrError5_).PropagateFailure()
            return output
        def iife10_():
            coll8_ = _dafny.Map()
            compr_8_: tuple
            for compr_8_ in (d_253_encodedEncryptionContext_).Elements:
                d_258_i_: tuple = compr_8_
                if (d_258_i_) in (d_253_encodedEncryptionContext_):
                    coll8_[((d_258_i_)[0]).value] = ((d_258_i_)[1]).value
            return _dafny.Map(coll8_)
        out38_: Wrappers.Result
        out38_ = CreateKeys.default__.CreateBranchAndBeaconKeys(d_240_branchKeyIdentifier_, iife10_()
        , d_245_timestamp_, d_249_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out38_
        return output

    @staticmethod
    def VersionKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        d_259_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_259_valueOrError0_ = Wrappers.default__.Need((0) < (len((input).branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Empty string not supported for identifier.")))
        if (d_259_valueOrError0_).IsFailure():
            output = (d_259_valueOrError0_).PropagateFailure()
            return output
        d_260_timestamp_: _dafny.Seq
        d_261_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda24_(d_262_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_262_e_)

        d_261_valueOrError1_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda24_)
        if (d_261_valueOrError1_).IsFailure():
            output = (d_261_valueOrError1_).PropagateFailure()
            return output
        d_260_timestamp_ = (d_261_valueOrError1_).Extract()
        d_263_maybeBranchKeyVersion_: Wrappers.Result
        out39_: Wrappers.Result
        out39_ = UUID.default__.GenerateUUID()
        d_263_maybeBranchKeyVersion_ = out39_
        d_264_branchKeyVersion_: _dafny.Seq
        d_265_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda25_(d_266_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_266_e_)

        d_265_valueOrError2_ = (d_263_maybeBranchKeyVersion_).MapFailure(lambda25_)
        if (d_265_valueOrError2_).IsFailure():
            output = (d_265_valueOrError2_).PropagateFailure()
            return output
        d_264_branchKeyVersion_ = (d_265_valueOrError2_).Extract()
        out40_: Wrappers.Result
        out40_ = CreateKeys.default__.VersionActiveBranchKey(input, d_260_timestamp_, d_264_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out40_
        return output

    @staticmethod
    def GetActiveBranchKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out41_: Wrappers.Result
        out41_ = GetKeys.default__.GetActiveKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out41_
        return output

    @staticmethod
    def GetBranchKeyVersion(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out42_: Wrappers.Result
        out42_ = GetKeys.default__.GetBranchKeyVersion(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out42_
        return output

    @staticmethod
    def GetBeaconKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out43_: Wrappers.Result
        out43_ = GetKeys.default__.GetBeaconKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out43_
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

