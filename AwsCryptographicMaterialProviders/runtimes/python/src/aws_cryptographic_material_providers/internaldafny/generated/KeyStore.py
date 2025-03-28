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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb

# Module: KeyStore

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultKeyStoreConfig():
        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(_dafny.Seq("None"), AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(_dafny.Seq("arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab")), _dafny.Seq("None"), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def KeyStore(config):
        res: Wrappers.Result = None
        d_0_kmsClient_: ComAmazonawsKmsTypes.IKMSClient = None
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient = None
        d_2_inferredRegion_: Wrappers.Option
        d_2_inferredRegion_ = Wrappers.Option_None()
        if KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration):
            d_3_valueOrError0_: Wrappers.Result = None
            d_3_valueOrError0_ = KmsArn.default__.IsValidKeyArn(KMSKeystoreOperations.default__.GetKeyId((config).kmsConfiguration))
            if (d_3_valueOrError0_).IsFailure():
                res = (d_3_valueOrError0_).PropagateFailure()
                return res
            d_4_parsedArn_: AwsArnParsing.AwsArn
            d_4_parsedArn_ = (d_3_valueOrError0_).Extract()
            d_2_inferredRegion_ = Wrappers.Option_Some((d_4_parsedArn_).region)
        elif ((config).kmsConfiguration).is_mrDiscovery:
            d_2_inferredRegion_ = Wrappers.Option_Some((((config).kmsConfiguration).mrDiscovery).region)
        d_5_grantTokens_: Wrappers.Result
        d_5_grantTokens_ = AwsKmsUtils.default__.GetValidGrantTokens((config).grantTokens)
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((True) and ((d_5_grantTokens_).is_Success), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Grant Tokens passed to Key Store configuration are invalid.")))
        if (d_6_valueOrError1_).IsFailure():
            res = (d_6_valueOrError1_).PropagateFailure()
            return res
        d_7_keyStoreId_: _dafny.Seq = _dafny.Seq("")
        if ((config).id).is_Some:
            d_7_keyStoreId_ = ((config).id).value
        elif True:
            d_8_maybeUuid_: Wrappers.Result
            out0_: Wrappers.Result
            out0_ = UUID.default__.GenerateUUID()
            d_8_maybeUuid_ = out0_
            d_9_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda0_(d_10_e_):
                return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_10_e_)

            d_9_valueOrError2_ = (d_8_maybeUuid_).MapFailure(lambda0_)
            if (d_9_valueOrError2_).IsFailure():
                res = (d_9_valueOrError2_).PropagateFailure()
                return res
            d_11_uuid_: _dafny.Seq
            d_11_uuid_ = (d_9_valueOrError2_).Extract()
            d_7_keyStoreId_ = d_11_uuid_
        if ((config).kmsClient).is_Some:
            d_0_kmsClient_ = ((config).kmsClient).value
        elif (((config).kmsClient).is_None) and ((d_2_inferredRegion_).is_Some):
            d_12_maybeKmsClient_: Wrappers.Result
            out1_: Wrappers.Result
            out1_ = Com_Amazonaws_Kms.default__.KMSClientForRegion((d_2_inferredRegion_).value)
            d_12_maybeKmsClient_ = out1_
            d_13_valueOrError3_: Wrappers.Result = None
            def lambda1_(d_14_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_14_e_)

            d_13_valueOrError3_ = (d_12_maybeKmsClient_).MapFailure(lambda1_)
            if (d_13_valueOrError3_).IsFailure():
                res = (d_13_valueOrError3_).PropagateFailure()
                return res
            d_0_kmsClient_ = (d_13_valueOrError3_).Extract()
        elif True:
            d_15_maybeKmsClient_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = Com_Amazonaws_Kms.default__.KMSClient()
            d_15_maybeKmsClient_ = out2_
            d_16_valueOrError4_: Wrappers.Result = None
            def lambda2_(d_17_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_17_e_)

            d_16_valueOrError4_ = (d_15_maybeKmsClient_).MapFailure(lambda2_)
            if (d_16_valueOrError4_).IsFailure():
                res = (d_16_valueOrError4_).PropagateFailure()
                return res
            d_0_kmsClient_ = (d_16_valueOrError4_).Extract()
        if ((config).ddbClient).is_Some:
            d_1_ddbClient_ = ((config).ddbClient).value
        elif (((config).ddbClient).is_None) and ((d_2_inferredRegion_).is_Some):
            d_18_maybeDdbClient_: Wrappers.Result
            out3_: Wrappers.Result
            out3_ = Com_Amazonaws_Dynamodb.default__.DDBClientForRegion((d_2_inferredRegion_).value)
            d_18_maybeDdbClient_ = out3_
            d_19_valueOrError5_: Wrappers.Result = None
            def lambda3_(d_20_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_20_e_)

            d_19_valueOrError5_ = (d_18_maybeDdbClient_).MapFailure(lambda3_)
            if (d_19_valueOrError5_).IsFailure():
                res = (d_19_valueOrError5_).PropagateFailure()
                return res
            d_1_ddbClient_ = (d_19_valueOrError5_).Extract()
        elif True:
            d_21_maybeDdbClient_: Wrappers.Result
            out4_: Wrappers.Result
            out4_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
            d_21_maybeDdbClient_ = out4_
            d_22_valueOrError6_: Wrappers.Result = None
            def lambda4_(d_23_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_23_e_)

            d_22_valueOrError6_ = (d_21_maybeDdbClient_).MapFailure(lambda4_)
            if (d_22_valueOrError6_).IsFailure():
                res = (d_22_valueOrError6_).PropagateFailure()
                return res
            d_1_ddbClient_ = (d_22_valueOrError6_).Extract()
        d_24_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_24_valueOrError7_ = Wrappers.default__.Need(ComAmazonawsDynamodbTypes.default__.IsValid__TableName((config).ddbTableName), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid Amazon DynamoDB Table Name")))
        if (d_24_valueOrError7_).IsFailure():
            res = (d_24_valueOrError7_).PropagateFailure()
            return res
        d_25_client_: KeyStoreClient
        nw0_ = KeyStoreClient()
        nw0_.ctor__(AwsCryptographyKeyStoreOperations.Config_Config(d_7_keyStoreId_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (d_5_grantTokens_).value, d_0_kmsClient_, d_1_ddbClient_))
        d_25_client_ = nw0_
        res = Wrappers.Result_Success(d_25_client_)
        return res
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class KeyStoreClient(AwsCryptographyKeyStoreTypes.IKeyStoreClient):
    def  __init__(self):
        self._config: AwsCryptographyKeyStoreOperations.Config = None
        pass

    def __dafnystr__(self) -> str:
        return "KeyStore.KeyStoreClient"
    def ctor__(self, config):
        (self)._config = config

    def GetKeyStoreInfo(self):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.GetKeyStoreInfo((self).config)
        output = out0_
        return output

    def CreateKeyStore(self, input):
        output: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.CreateKeyStore((self).config, input)
        output = out0_
        return output

    def CreateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.CreateKey((self).config, input)
        output = out0_
        return output

    def VersionKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.VersionKey((self).config, input)
        output = out0_
        return output

    def GetActiveBranchKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.GetActiveBranchKey((self).config, input)
        output = out0_
        return output

    def GetBranchKeyVersion(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.GetBranchKeyVersion((self).config, input)
        output = out0_
        return output

    def GetBeaconKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out0_: Wrappers.Result
        out0_ = AwsCryptographyKeyStoreOperations.default__.GetBeaconKey((self).config, input)
        output = out0_
        return output

    @property
    def config(self):
        return self._config
