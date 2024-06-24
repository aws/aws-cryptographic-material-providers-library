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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb

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
        d_301_kmsClient_: ComAmazonawsKmsTypes.IKMSClient = None
        d_302_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient = None
        d_303_inferredRegion_: Wrappers.Option
        d_303_inferredRegion_ = Wrappers.Option_None()
        if KMSKeystoreOperations.default__.HasKeyId((config).kmsConfiguration):
            d_304_parsedArn_: AwsArnParsing.AwsArn
            d_305_valueOrError0_: Wrappers.Result = None
            d_305_valueOrError0_ = KmsArn.default__.IsValidKeyArn(KMSKeystoreOperations.default__.GetKeyId((config).kmsConfiguration))
            if (d_305_valueOrError0_).IsFailure():
                res = (d_305_valueOrError0_).PropagateFailure()
                return res
            d_304_parsedArn_ = (d_305_valueOrError0_).Extract()
            d_303_inferredRegion_ = Wrappers.Option_Some((d_304_parsedArn_).region)
        elif ((config).kmsConfiguration).is_mrDiscovery:
            d_303_inferredRegion_ = Wrappers.Option_Some((((config).kmsConfiguration).mrDiscovery).region)
        d_306_grantTokens_: Wrappers.Result
        d_306_grantTokens_ = AwsKmsUtils.default__.GetValidGrantTokens((config).grantTokens)
        d_307_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_307_valueOrError1_ = Wrappers.default__.Need((True) and ((d_306_grantTokens_).is_Success), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Grant Tokens passed to Key Store configuration are invalid.")))
        if (d_307_valueOrError1_).IsFailure():
            res = (d_307_valueOrError1_).PropagateFailure()
            return res
        d_308_keyStoreId_: _dafny.Seq = _dafny.Seq("")
        if ((config).id).is_Some:
            d_308_keyStoreId_ = ((config).id).value
        elif True:
            d_309_maybeUuid_: Wrappers.Result
            out44_: Wrappers.Result
            out44_ = UUID.default__.GenerateUUID()
            d_309_maybeUuid_ = out44_
            d_310_uuid_: _dafny.Seq
            d_311_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda27_(d_312_e_):
                return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_312_e_)

            d_311_valueOrError2_ = (d_309_maybeUuid_).MapFailure(lambda27_)
            if (d_311_valueOrError2_).IsFailure():
                res = (d_311_valueOrError2_).PropagateFailure()
                return res
            d_310_uuid_ = (d_311_valueOrError2_).Extract()
            d_308_keyStoreId_ = d_310_uuid_
        if ((config).kmsClient).is_Some:
            d_301_kmsClient_ = ((config).kmsClient).value
        elif (((config).kmsClient).is_None) and ((d_303_inferredRegion_).is_Some):
            d_313_maybeKmsClient_: Wrappers.Result
            out45_: Wrappers.Result
            out45_ = Com_Amazonaws_Kms.default__.KMSClientForRegion((d_303_inferredRegion_).value)
            d_313_maybeKmsClient_ = out45_
            d_314_valueOrError3_: Wrappers.Result = None
            def lambda28_(d_315_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_315_e_)

            d_314_valueOrError3_ = (d_313_maybeKmsClient_).MapFailure(lambda28_)
            if (d_314_valueOrError3_).IsFailure():
                res = (d_314_valueOrError3_).PropagateFailure()
                return res
            d_301_kmsClient_ = (d_314_valueOrError3_).Extract()
        elif True:
            d_316_maybeKmsClient_: Wrappers.Result
            out46_: Wrappers.Result
            out46_ = Com_Amazonaws_Kms.default__.KMSClient()
            d_316_maybeKmsClient_ = out46_
            d_317_valueOrError4_: Wrappers.Result = None
            def lambda29_(d_318_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(d_318_e_)

            d_317_valueOrError4_ = (d_316_maybeKmsClient_).MapFailure(lambda29_)
            if (d_317_valueOrError4_).IsFailure():
                res = (d_317_valueOrError4_).PropagateFailure()
                return res
            d_301_kmsClient_ = (d_317_valueOrError4_).Extract()
        if ((config).ddbClient).is_Some:
            d_302_ddbClient_ = ((config).ddbClient).value
        elif (((config).ddbClient).is_None) and ((d_303_inferredRegion_).is_Some):
            d_319_maybeDdbClient_: Wrappers.Result
            out47_: Wrappers.Result
            out47_ = Com_Amazonaws_Dynamodb.default__.DDBClientForRegion((d_303_inferredRegion_).value)
            d_319_maybeDdbClient_ = out47_
            d_320_valueOrError5_: Wrappers.Result = None
            def lambda30_(d_321_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_321_e_)

            d_320_valueOrError5_ = (d_319_maybeDdbClient_).MapFailure(lambda30_)
            if (d_320_valueOrError5_).IsFailure():
                res = (d_320_valueOrError5_).PropagateFailure()
                return res
            d_302_ddbClient_ = (d_320_valueOrError5_).Extract()
        elif True:
            d_322_maybeDdbClient_: Wrappers.Result
            out48_: Wrappers.Result
            out48_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
            d_322_maybeDdbClient_ = out48_
            d_323_valueOrError6_: Wrappers.Result = None
            def lambda31_(d_324_e_):
                return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_324_e_)

            d_323_valueOrError6_ = (d_322_maybeDdbClient_).MapFailure(lambda31_)
            if (d_323_valueOrError6_).IsFailure():
                res = (d_323_valueOrError6_).PropagateFailure()
                return res
            d_302_ddbClient_ = (d_323_valueOrError6_).Extract()
        d_325_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_325_valueOrError7_ = Wrappers.default__.Need(ComAmazonawsDynamodbTypes.default__.IsValid__TableName((config).ddbTableName), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid Amazon DynamoDB Table Name")))
        if (d_325_valueOrError7_).IsFailure():
            res = (d_325_valueOrError7_).PropagateFailure()
            return res
        d_326_client_: KeyStoreClient
        nw0_ = KeyStoreClient()
        nw0_.ctor__(AwsCryptographyKeyStoreOperations.Config_Config(d_308_keyStoreId_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (d_306_grantTokens_).value, d_301_kmsClient_, d_302_ddbClient_))
        d_326_client_ = nw0_
        res = Wrappers.Result_Success(d_326_client_)
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
        out49_: Wrappers.Result
        out49_ = AwsCryptographyKeyStoreOperations.default__.GetKeyStoreInfo((self).config)
        output = out49_
        return output

    def CreateKeyStore(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyStoreOutput.default())()
        out50_: Wrappers.Result
        out50_ = AwsCryptographyKeyStoreOperations.default__.CreateKeyStore((self).config, input)
        output = out50_
        return output

    def CreateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out51_: Wrappers.Result
        out51_ = AwsCryptographyKeyStoreOperations.default__.CreateKey((self).config, input)
        output = out51_
        return output

    def VersionKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out52_: Wrappers.Result
        out52_ = AwsCryptographyKeyStoreOperations.default__.VersionKey((self).config, input)
        output = out52_
        return output

    def GetActiveBranchKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out53_: Wrappers.Result
        out53_ = AwsCryptographyKeyStoreOperations.default__.GetActiveBranchKey((self).config, input)
        output = out53_
        return output

    def GetBranchKeyVersion(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out54_: Wrappers.Result
        out54_ = AwsCryptographyKeyStoreOperations.default__.GetBranchKeyVersion((self).config, input)
        output = out54_
        return output

    def GetBeaconKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out55_: Wrappers.Result
        out55_ = AwsCryptographyKeyStoreOperations.default__.GetBeaconKey((self).config, input)
        output = out55_
        return output

    @property
    def config(self):
        return self._config
