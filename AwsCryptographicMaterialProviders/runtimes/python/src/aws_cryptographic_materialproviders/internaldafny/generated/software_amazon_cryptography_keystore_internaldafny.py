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
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com

# Module: software_amazon_cryptography_keystore_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultKeyStoreConfig():
        return software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(_dafny.Seq("None"), software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(_dafny.Seq("1234abcd-12ab-34cd-56ef-1234567890ab")), _dafny.Seq("None"), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())

    @staticmethod
    def KeyStore(config):
        res: Wrappers.Result = None
        d_282_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_282_valueOrError0_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType(((config).kmsConfiguration).kmsKeyArn)) and ((AwsArnParsing.default__.ParseAwsKmsArn(((config).kmsConfiguration).kmsKeyArn)).is_Success), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid AWS KMS Key Arn")))
        if (d_282_valueOrError0_).IsFailure():
            res = (d_282_valueOrError0_).PropagateFailure()
            return res
        d_283_grantTokens_: Wrappers.Result
        d_283_grantTokens_ = AwsKmsUtils.default__.GetValidGrantTokens((config).grantTokens)
        d_284_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_284_valueOrError1_ = Wrappers.default__.Need((True) and ((d_283_grantTokens_).is_Success), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("CreateKey received invalid grant tokens")))
        if (d_284_valueOrError1_).IsFailure():
            res = (d_284_valueOrError1_).PropagateFailure()
            return res
        d_285_keyStoreId_: _dafny.Seq = _dafny.Seq("")
        if ((config).id).is_Some:
            d_285_keyStoreId_ = ((config).id).value
        elif True:
            d_286_maybeUuid_: Wrappers.Result
            out44_: Wrappers.Result
            out44_ = UUID.default__.GenerateUUID()
            d_286_maybeUuid_ = out44_
            d_287_uuid_: _dafny.Seq
            d_288_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda26_(d_289_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_289_e_)

            d_288_valueOrError2_ = (d_286_maybeUuid_).MapFailure(lambda26_)
            if (d_288_valueOrError2_).IsFailure():
                res = (d_288_valueOrError2_).PropagateFailure()
                return res
            d_287_uuid_ = (d_288_valueOrError2_).Extract()
            d_285_keyStoreId_ = d_287_uuid_
        d_290_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        d_291_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient = None
        d_292_keyArn_: Wrappers.Result
        d_292_keyArn_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(((config).kmsConfiguration).kmsKeyArn)
        d_293_kmsRegion_: Wrappers.Option
        d_293_kmsRegion_ = AwsArnParsing.default__.GetRegion((d_292_keyArn_).value)
        if ((config).kmsClient).is_None:
            d_294_maybeKmsClient_: Wrappers.Result
            out45_: Wrappers.Result
            out45_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClientForRegion((d_293_kmsRegion_).value)
            d_294_maybeKmsClient_ = out45_
            d_295_valueOrError3_: Wrappers.Result = None
            def lambda27_(d_296_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_296_e_)

            d_295_valueOrError3_ = (d_294_maybeKmsClient_).MapFailure(lambda27_)
            if (d_295_valueOrError3_).IsFailure():
                res = (d_295_valueOrError3_).PropagateFailure()
                return res
            d_290_kmsClient_ = (d_295_valueOrError3_).Extract()
        elif True:
            d_290_kmsClient_ = ((config).kmsClient).value
        if ((config).ddbClient).is_None:
            d_297_maybeDdbClient_: Wrappers.Result
            out46_: Wrappers.Result
            out46_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DDBClientForRegion((d_293_kmsRegion_).value)
            d_297_maybeDdbClient_ = out46_
            d_298_valueOrError4_: Wrappers.Result = None
            def lambda28_(d_299_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_299_e_)

            d_298_valueOrError4_ = (d_297_maybeDdbClient_).MapFailure(lambda28_)
            if (d_298_valueOrError4_).IsFailure():
                res = (d_298_valueOrError4_).PropagateFailure()
                return res
            d_291_ddbClient_ = (d_298_valueOrError4_).Extract()
        elif True:
            d_291_ddbClient_ = ((config).ddbClient).value
        d_300_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_300_valueOrError5_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName((config).ddbTableName), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid Amazon DynamoDB Table Name")))
        if (d_300_valueOrError5_).IsFailure():
            res = (d_300_valueOrError5_).PropagateFailure()
            return res
        d_301_client_: KeyStoreClient
        nw0_ = KeyStoreClient()
        nw0_.ctor__(AwsCryptographyKeyStoreOperations.Config_Config(d_285_keyStoreId_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (d_283_grantTokens_).value, d_290_kmsClient_, d_291_ddbClient_))
        d_301_client_ = nw0_
        res = Wrappers.Result_Success(d_301_client_)
        return res
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class KeyStoreClient(software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient):
    def  __init__(self):
        self._config: AwsCryptographyKeyStoreOperations.Config = None
        pass

    def __dafnystr__(self) -> str:
        return "KeyStore.KeyStoreClient"
    def ctor__(self, config):
        (self)._config = config

    def GetKeyStoreInfo(self):
        output: Wrappers.Result = None
        out47_: Wrappers.Result
        out47_ = AwsCryptographyKeyStoreOperations.default__.GetKeyStoreInfo((self).config)
        output = out47_
        return output

    def CreateKeyStore(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        out48_: Wrappers.Result
        out48_ = AwsCryptographyKeyStoreOperations.default__.CreateKeyStore((self).config, input)
        output = out48_
        return output

    def CreateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out49_: Wrappers.Result
        out49_ = AwsCryptographyKeyStoreOperations.default__.CreateKey((self).config, input)
        output = out49_
        return output

    def VersionKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        out50_: Wrappers.Result
        out50_ = AwsCryptographyKeyStoreOperations.default__.VersionKey((self).config, input)
        output = out50_
        return output

    def GetActiveBranchKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out51_: Wrappers.Result
        out51_ = AwsCryptographyKeyStoreOperations.default__.GetActiveBranchKey((self).config, input)
        output = out51_
        return output

    def GetBranchKeyVersion(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out52_: Wrappers.Result
        out52_ = AwsCryptographyKeyStoreOperations.default__.GetBranchKeyVersion((self).config, input)
        output = out52_
        return output

    def GetBeaconKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out53_: Wrappers.Result
        out53_ = AwsCryptographyKeyStoreOperations.default__.GetBeaconKey((self).config, input)
        output = out53_
        return output

    @property
    def config(self):
        return self._config
