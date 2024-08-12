import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys

# Module: AwsCryptographyKeyStoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetKeyStoreInfo(config):
        output: Wrappers.Result = None
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput_GetKeyStoreInfoOutput((config).id, (config).ddbTableName, (config).logicalKeyStoreName, (config).grantTokens, (config).kmsConfiguration))
        return output

    @staticmethod
    def CreateKeyStore(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput.default())()
        d_270_ddbTableArn_: _dafny.Seq
        d_271_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out36_: Wrappers.Result
        out36_ = CreateKeyStoreTable.default__.CreateKeyStoreTable((config).ddbTableName, (config).ddbClient)
        d_271_valueOrError0_ = out36_
        if (d_271_valueOrError0_).IsFailure():
            output = (d_271_valueOrError0_).PropagateFailure()
            return output
        d_270_ddbTableArn_ = (d_271_valueOrError0_).Extract()
        d_272_tableName_: Wrappers.Result
        d_272_tableName_ = AwsArnParsing.default__.ParseAmazonDynamodbTableName(d_270_ddbTableArn_)
        d_273_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_273_valueOrError1_ = Wrappers.default__.Need(((d_272_tableName_).is_Success) and (((d_272_tableName_).value) == ((config).ddbTableName)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")))
        if (d_273_valueOrError1_).IsFailure():
            output = (d_273_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput_CreateKeyStoreOutput(d_270_ddbTableArn_))
        return output

    @staticmethod
    def CreateKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        d_274_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_274_valueOrError0_ = Wrappers.default__.Need(not (((input).branchKeyIdentifier).is_Some) or ((((input).encryptionContext).is_Some) and ((0) < (len(((input).encryptionContext).value)))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.CUSTOM__BRANCH__KEY__ID__NEED__EC))
        if (d_274_valueOrError0_).IsFailure():
            output = (d_274_valueOrError0_).PropagateFailure()
            return output
        d_275_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_275_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.DISCOVERY__CREATE__KEY__NOT__SUPPORTED))
        if (d_275_valueOrError1_).IsFailure():
            output = (d_275_valueOrError1_).PropagateFailure()
            return output
        d_276_branchKeyIdentifier_: _dafny.Seq = _dafny.Seq("")
        if ((input).branchKeyIdentifier).is_None:
            d_277_maybeBranchKeyId_: Wrappers.Result
            out37_: Wrappers.Result
            out37_ = UUID.default__.GenerateUUID()
            d_277_maybeBranchKeyId_ = out37_
            d_278_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda22_(d_279_e_):
                return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_279_e_)

            d_278_valueOrError2_ = (d_277_maybeBranchKeyId_).MapFailure(lambda22_)
            if (d_278_valueOrError2_).IsFailure():
                output = (d_278_valueOrError2_).PropagateFailure()
                return output
            d_276_branchKeyIdentifier_ = (d_278_valueOrError2_).Extract()
        elif True:
            d_280_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_280_valueOrError3_ = Wrappers.default__.Need((0) < (len(((input).branchKeyIdentifier).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Custom branch key id can not be an empty string.")))
            if (d_280_valueOrError3_).IsFailure():
                output = (d_280_valueOrError3_).PropagateFailure()
                return output
            d_276_branchKeyIdentifier_ = ((input).branchKeyIdentifier).value
        d_281_timestamp_: _dafny.Seq
        d_282_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda23_(d_283_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_283_e_)

        d_282_valueOrError4_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda23_)
        if (d_282_valueOrError4_).IsFailure():
            output = (d_282_valueOrError4_).PropagateFailure()
            return output
        d_281_timestamp_ = (d_282_valueOrError4_).Extract()
        d_284_maybeBranchKeyVersion_: Wrappers.Result
        out38_: Wrappers.Result
        out38_ = UUID.default__.GenerateUUID()
        d_284_maybeBranchKeyVersion_ = out38_
        d_285_branchKeyVersion_: _dafny.Seq
        d_286_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda24_(d_287_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_287_e_)

        d_286_valueOrError5_ = (d_284_maybeBranchKeyVersion_).MapFailure(lambda24_)
        if (d_286_valueOrError5_).IsFailure():
            output = (d_286_valueOrError5_).PropagateFailure()
            return output
        d_285_branchKeyVersion_ = (d_286_valueOrError5_).Extract()
        d_288_unwrapEncryptionContext_: _dafny.Map
        d_288_unwrapEncryptionContext_ = ((input).encryptionContext).UnwrapOr(_dafny.Map({}))
        d_289_encodedEncryptionContext_: _dafny.Set
        def iife9_():
            coll7_ = _dafny.Set()
            compr_7_: _dafny.Seq
            for compr_7_ in (d_288_unwrapEncryptionContext_).keys.Elements:
                d_290_k_: _dafny.Seq = compr_7_
                if UTF8.ValidUTF8Bytes._Is(d_290_k_):
                    if (d_290_k_) in (d_288_unwrapEncryptionContext_):
                        coll7_ = coll7_.union(_dafny.Set([(UTF8.default__.Decode(d_290_k_), UTF8.default__.Decode((d_288_unwrapEncryptionContext_)[d_290_k_]), d_290_k_)]))
            return _dafny.Set(coll7_)
        d_289_encodedEncryptionContext_ = iife9_()
        
        d_291_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda25_(forall_var_7_):
            def iife10_(_pat_let1_0):
                def iife11_(d_293_encoded_):
                    return ((d_293_encoded_).is_Success) and (((d_292_i_)[2]) == ((d_293_encoded_).value))
                return iife11_(_pat_let1_0)
            d_292_i_: tuple = forall_var_7_
            return not ((d_292_i_) in (d_289_encodedEncryptionContext_)) or ((((((d_292_i_)[0]).is_Success) and (((d_292_i_)[1]).is_Success)) and (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (((d_292_i_)[0]).value)))) and (iife10_(UTF8.default__.Encode(((d_292_i_)[0]).value))))

        d_291_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_289_encodedEncryptionContext_).Elements, True, lambda25_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.UTF8__ENCODING__ENCRYPTION__CONTEXT__ERROR))
        if (d_291_valueOrError6_).IsFailure():
            output = (d_291_valueOrError6_).PropagateFailure()
            return output
        out39_: Wrappers.Result
        def iife12_():
            coll8_ = _dafny.Map()
            compr_8_: tuple
            for compr_8_ in (d_289_encodedEncryptionContext_).Elements:
                d_294_i_: tuple = compr_8_
                if (d_294_i_) in (d_289_encodedEncryptionContext_):
                    coll8_[((d_294_i_)[0]).value] = ((d_294_i_)[1]).value
            return _dafny.Map(coll8_)
        out39_ = CreateKeys.default__.CreateBranchAndBeaconKeys(d_276_branchKeyIdentifier_, iife12_()
        , d_281_timestamp_, d_285_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out39_
        return output

    @staticmethod
    def VersionKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        d_295_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_295_valueOrError0_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.DISCOVERY__VERSION__KEY__NOT__SUPPORTED))
        if (d_295_valueOrError0_).IsFailure():
            output = (d_295_valueOrError0_).PropagateFailure()
            return output
        d_296_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_296_valueOrError1_ = Wrappers.default__.Need((0) < (len((input).branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.BRANCH__KEY__ID__NEEDED))
        if (d_296_valueOrError1_).IsFailure():
            output = (d_296_valueOrError1_).PropagateFailure()
            return output
        d_297_timestamp_: _dafny.Seq
        d_298_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda26_(d_299_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_299_e_)

        d_298_valueOrError2_ = (Time.default__.GetCurrentTimeStamp()).MapFailure(lambda26_)
        if (d_298_valueOrError2_).IsFailure():
            output = (d_298_valueOrError2_).PropagateFailure()
            return output
        d_297_timestamp_ = (d_298_valueOrError2_).Extract()
        d_300_maybeBranchKeyVersion_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = UUID.default__.GenerateUUID()
        d_300_maybeBranchKeyVersion_ = out40_
        d_301_branchKeyVersion_: _dafny.Seq
        d_302_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda27_(d_303_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_303_e_)

        d_302_valueOrError3_ = (d_300_maybeBranchKeyVersion_).MapFailure(lambda27_)
        if (d_302_valueOrError3_).IsFailure():
            output = (d_302_valueOrError3_).PropagateFailure()
            return output
        d_301_branchKeyVersion_ = (d_302_valueOrError3_).Extract()
        out41_: Wrappers.Result
        out41_ = CreateKeys.default__.VersionActiveBranchKey(input, d_297_timestamp_, d_301_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out41_
        return output

    @staticmethod
    def GetActiveBranchKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out42_: Wrappers.Result
        out42_ = GetKeys.default__.GetActiveKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out42_
        return output

    @staticmethod
    def GetBranchKeyVersion(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out43_: Wrappers.Result
        out43_ = GetKeys.default__.GetBranchKeyVersion(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out43_
        return output

    @staticmethod
    def GetBeaconKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out44_: Wrappers.Result
        out44_ = GetKeys.default__.GetBeaconKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out44_
        return output


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), AwsCryptographyKeyStoreTypes.KMSConfiguration.default()(), _dafny.Seq({}), None, None)
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

