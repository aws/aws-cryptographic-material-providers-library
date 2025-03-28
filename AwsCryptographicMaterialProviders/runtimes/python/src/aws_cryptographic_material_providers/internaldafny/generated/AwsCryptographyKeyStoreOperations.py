import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys

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
        output: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = CreateKeyStoreTable.default__.CreateKeyStoreTable((config).ddbTableName, (config).ddbClient)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_ddbTableArn_: _dafny.Seq
        d_1_ddbTableArn_ = (d_0_valueOrError0_).Extract()
        d_2_tableName_: Wrappers.Result
        d_2_tableName_ = AwsArnParsing.default__.ParseAmazonDynamodbTableName(d_1_ddbTableArn_)
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = Wrappers.default__.Need(((d_2_tableName_).is_Success) and (((d_2_tableName_).value) == ((config).ddbTableName)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")))
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput_CreateKeyStoreOutput(d_1_ddbTableArn_))
        return output

    @staticmethod
    def CreateKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(not (((input).branchKeyIdentifier).is_Some) or ((((input).encryptionContext).is_Some) and ((0) < (len(((input).encryptionContext).value)))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.CUSTOM__BRANCH__KEY__ID__NEED__EC))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.DISCOVERY__CREATE__KEY__NOT__SUPPORTED))
        if (d_1_valueOrError1_).IsFailure():
            output = (d_1_valueOrError1_).PropagateFailure()
            return output
        d_2_branchKeyIdentifier_: _dafny.Seq = _dafny.Seq("")
        if ((input).branchKeyIdentifier).is_None:
            d_3_maybeBranchKeyId_: Wrappers.Result
            out0_: Wrappers.Result
            out0_ = UUID.default__.GenerateUUID()
            d_3_maybeBranchKeyId_ = out0_
            d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda0_(d_5_e_):
                return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_5_e_)

            d_4_valueOrError2_ = (d_3_maybeBranchKeyId_).MapFailure(lambda0_)
            if (d_4_valueOrError2_).IsFailure():
                output = (d_4_valueOrError2_).PropagateFailure()
                return output
            d_2_branchKeyIdentifier_ = (d_4_valueOrError2_).Extract()
        elif True:
            d_6_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_6_valueOrError3_ = Wrappers.default__.Need((0) < (len(((input).branchKeyIdentifier).value)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Custom branch key id can not be an empty string.")))
            if (d_6_valueOrError3_).IsFailure():
                output = (d_6_valueOrError3_).PropagateFailure()
                return output
            d_2_branchKeyIdentifier_ = ((input).branchKeyIdentifier).value
        d_7_timestamp_q_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = Time.default__.GetCurrentTimeStamp()
        d_7_timestamp_q_ = out1_
        d_8_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda1_(d_9_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_9_e_)

        d_8_valueOrError4_ = (d_7_timestamp_q_).MapFailure(lambda1_)
        if (d_8_valueOrError4_).IsFailure():
            output = (d_8_valueOrError4_).PropagateFailure()
            return output
        d_10_timestamp_: _dafny.Seq
        d_10_timestamp_ = (d_8_valueOrError4_).Extract()
        d_11_maybeBranchKeyVersion_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = UUID.default__.GenerateUUID()
        d_11_maybeBranchKeyVersion_ = out2_
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda2_(d_13_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_13_e_)

        d_12_valueOrError5_ = (d_11_maybeBranchKeyVersion_).MapFailure(lambda2_)
        if (d_12_valueOrError5_).IsFailure():
            output = (d_12_valueOrError5_).PropagateFailure()
            return output
        d_14_branchKeyVersion_: _dafny.Seq
        d_14_branchKeyVersion_ = (d_12_valueOrError5_).Extract()
        d_15_unwrapEncryptionContext_: _dafny.Map
        d_15_unwrapEncryptionContext_ = ((input).encryptionContext).UnwrapOr(_dafny.Map({}))
        d_16_encodedEncryptionContext_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in (d_15_unwrapEncryptionContext_).keys.Elements:
                d_17_k_: _dafny.Seq = compr_0_
                if UTF8.ValidUTF8Bytes._Is(d_17_k_):
                    if (d_17_k_) in (d_15_unwrapEncryptionContext_):
                        coll0_ = coll0_.union(_dafny.Set([(UTF8.default__.Decode(d_17_k_), UTF8.default__.Decode((d_15_unwrapEncryptionContext_)[d_17_k_]), d_17_k_)]))
            return _dafny.Set(coll0_)
        d_16_encodedEncryptionContext_ = iife0_()
        
        d_18_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda3_(forall_var_0_):
            def iife1_(_pat_let1_0):
                def iife2_(d_20_encoded_):
                    return ((d_20_encoded_).is_Success) and (((d_19_i_)[2]) == ((d_20_encoded_).value))
                return iife2_(_pat_let1_0)
            d_19_i_: tuple = forall_var_0_
            return not ((d_19_i_) in (d_16_encodedEncryptionContext_)) or ((((((d_19_i_)[0]).is_Success) and (((d_19_i_)[1]).is_Success)) and (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (((d_19_i_)[0]).value)))) and (iife1_(UTF8.default__.Encode(((d_19_i_)[0]).value))))

        d_18_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_16_encodedEncryptionContext_).Elements, True, lambda3_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.UTF8__ENCODING__ENCRYPTION__CONTEXT__ERROR))
        if (d_18_valueOrError6_).IsFailure():
            output = (d_18_valueOrError6_).PropagateFailure()
            return output
        out3_: Wrappers.Result
        def iife3_():
            coll1_ = _dafny.Map()
            compr_1_: tuple
            for compr_1_ in (d_16_encodedEncryptionContext_).Elements:
                d_21_i_: tuple = compr_1_
                if (d_21_i_) in (d_16_encodedEncryptionContext_):
                    coll1_[((d_21_i_)[0]).value] = ((d_21_i_)[1]).value
            return _dafny.Map(coll1_)
        out3_ = CreateKeys.default__.CreateBranchAndBeaconKeys(d_2_branchKeyIdentifier_, iife3_()
        , d_10_timestamp_, d_14_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out3_
        return output

    @staticmethod
    def VersionKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.DISCOVERY__VERSION__KEY__NOT__SUPPORTED))
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need((0) < (len((input).branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.BRANCH__KEY__ID__NEEDED))
        if (d_1_valueOrError1_).IsFailure():
            output = (d_1_valueOrError1_).PropagateFailure()
            return output
        d_2_timestamp_q_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = Time.default__.GetCurrentTimeStamp()
        d_2_timestamp_q_ = out0_
        d_3_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_4_e_)

        d_3_valueOrError2_ = (d_2_timestamp_q_).MapFailure(lambda0_)
        if (d_3_valueOrError2_).IsFailure():
            output = (d_3_valueOrError2_).PropagateFailure()
            return output
        d_5_timestamp_: _dafny.Seq
        d_5_timestamp_ = (d_3_valueOrError2_).Extract()
        d_6_maybeBranchKeyVersion_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = UUID.default__.GenerateUUID()
        d_6_maybeBranchKeyVersion_ = out1_
        d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda1_(d_8_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_8_e_)

        d_7_valueOrError3_ = (d_6_maybeBranchKeyVersion_).MapFailure(lambda1_)
        if (d_7_valueOrError3_).IsFailure():
            output = (d_7_valueOrError3_).PropagateFailure()
            return output
        d_9_branchKeyVersion_: _dafny.Seq
        d_9_branchKeyVersion_ = (d_7_valueOrError3_).Extract()
        out2_: Wrappers.Result
        out2_ = CreateKeys.default__.VersionActiveBranchKey(input, d_5_timestamp_, d_9_branchKeyVersion_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out2_
        return output

    @staticmethod
    def GetActiveBranchKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = GetKeys.default__.GetActiveKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out0_
        return output

    @staticmethod
    def GetBranchKeyVersion(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out0_: Wrappers.Result
        out0_ = GetKeys.default__.GetBranchKeyVersion(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out0_
        return output

    @staticmethod
    def GetBeaconKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = GetKeys.default__.GetBeaconKeyAndUnwrap(input, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (config).grantTokens, (config).kmsClient, (config).ddbClient)
        output = out0_
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

