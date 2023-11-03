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
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures

assert "TestCreateKeyStore" == __name__
TestCreateKeyStore = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateKeyStore():
        d_287_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_288_valueOrError0_: Wrappers.Result = None
        out54_: Wrappers.Result
        out54_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_288_valueOrError0_ = out54_
        if not(not((d_288_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(19,18): " + _dafny.string_of(d_288_valueOrError0_))
        d_287_kmsClient_ = (d_288_valueOrError0_).Extract()
        d_289_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_290_valueOrError1_: Wrappers.Result = None
        out55_: Wrappers.Result
        out55_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_290_valueOrError1_ = out55_
        if not(not((d_290_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(20,18): " + _dafny.string_of(d_290_valueOrError1_))
        d_289_ddbClient_ = (d_290_valueOrError1_).Extract()
        d_291_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_291_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_292_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_292_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_291_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_289_ddbClient_), Wrappers.Option_Some(d_287_kmsClient_))
        d_293_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_294_valueOrError2_: Wrappers.Result = None
        out56_: Wrappers.Result
        out56_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_292_keyStoreConfig_)
        d_294_valueOrError2_ = out56_
        if not(not((d_294_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(33,17): " + _dafny.string_of(d_294_valueOrError2_))
        d_293_keyStore_ = (d_294_valueOrError2_).Extract()
        d_295_keyStoreArn_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput
        d_296_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        out57_: Wrappers.Result
        out57_ = (d_293_keyStore_).CreateKeyStore(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreInput_CreateKeyStoreInput())
        d_296_valueOrError3_ = out57_
        if not(not((d_296_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(36,20): " + _dafny.string_of(d_296_valueOrError3_))
        d_295_keyStoreArn_ = (d_296_valueOrError3_).Extract()
        if not((AwsArnParsing.default__.ParseAmazonDynamodbTableName((d_295_keyStoreArn_).tableArn)).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((AwsArnParsing.default__.ParseAmazonDynamodbTableName((d_295_keyStoreArn_).tableArn)).value) == ((Fixtures.default__).branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

