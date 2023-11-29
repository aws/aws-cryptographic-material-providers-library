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

# Module: DDBKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteNewKeyToStore(versionBranchKeyItem, activeBranchKeyItem, beaconKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        d_1991_items_: _dafny.Seq
        d_1991_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(beaconKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_1992_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_1992_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_1991_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_1993_maybeTransactWriteResponse_: Wrappers.Result
        out352_: Wrappers.Result
        out352_ = (ddbClient).TransactWriteItems(d_1992_transactRequest_)
        d_1993_maybeTransactWriteResponse_ = out352_
        d_1994_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_1995_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda137_(d_1996_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_1996_e_)

        d_1995_valueOrError0_ = (d_1993_maybeTransactWriteResponse_).MapFailure(lambda137_)
        if (d_1995_valueOrError0_).IsFailure():
            output = (d_1995_valueOrError0_).PropagateFailure()
            return output
        d_1994_transactWriteItemsResponse_ = (d_1995_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_1994_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        d_1997_items_: _dafny.Seq
        d_1997_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__EXISTS())])
        d_1998_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_1998_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_1997_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_1999_maybeTransactWriteResponse_: Wrappers.Result
        out353_: Wrappers.Result
        out353_ = (ddbClient).TransactWriteItems(d_1998_transactRequest_)
        d_1999_maybeTransactWriteResponse_ = out353_
        d_2000_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_2001_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda138_(d_2002_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2002_e_)

        d_2001_valueOrError0_ = (d_1999_maybeTransactWriteResponse_).MapFailure(lambda138_)
        if (d_2001_valueOrError0_).IsFailure():
            output = (d_2001_valueOrError0_).PropagateFailure()
            return output
        d_2000_transactWriteItemsResponse_ = (d_2001_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_2000_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_2003_dynamoDbKey_: _dafny.Map
        d_2003_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(Structure.default__.BRANCH__KEY__ACTIVE__TYPE)})
        d_2004_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_2004_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_2003_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2005_maybeGetItem_: Wrappers.Result
        out354_: Wrappers.Result
        out354_ = (ddbClient).GetItem(d_2004_ItemRequest_)
        d_2005_maybeGetItem_ = out354_
        d_2006_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_2007_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda139_(d_2008_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2008_e_)

        d_2007_valueOrError0_ = (d_2005_maybeGetItem_).MapFailure(lambda139_)
        if (d_2007_valueOrError0_).IsFailure():
            output = (d_2007_valueOrError0_).PropagateFailure()
            return output
        d_2006_getItemResponse_ = (d_2007_valueOrError0_).Extract()
        d_2009_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2009_valueOrError1_ = Wrappers.default__.Need(((d_2006_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_2009_valueOrError1_).IsFailure():
            output = (d_2009_valueOrError1_).PropagateFailure()
            return output
        d_2010_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2010_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_2006_getItemResponse_).Item).value)) and ((((((d_2006_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_2010_valueOrError2_).IsFailure():
            output = (d_2010_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_2006_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_2011_dynamoDbKey_: _dafny.Map
        d_2011_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_2012_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_2012_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_2011_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2013_maybeGetItem_: Wrappers.Result
        out355_: Wrappers.Result
        out355_ = (ddbClient).GetItem(d_2012_ItemRequest_)
        d_2013_maybeGetItem_ = out355_
        d_2014_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_2015_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda140_(d_2016_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2016_e_)

        d_2015_valueOrError0_ = (d_2013_maybeGetItem_).MapFailure(lambda140_)
        if (d_2015_valueOrError0_).IsFailure():
            output = (d_2015_valueOrError0_).PropagateFailure()
            return output
        d_2014_getItemResponse_ = (d_2015_valueOrError0_).Extract()
        d_2017_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2017_valueOrError1_ = Wrappers.default__.Need(((d_2014_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_2017_valueOrError1_).IsFailure():
            output = (d_2017_valueOrError1_).PropagateFailure()
            return output
        d_2018_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2018_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_2014_getItemResponse_).Item).value)) and ((((((d_2014_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_2014_getItemResponse_).Item).value)[Structure.default__.TYPE__FIELD]).S) == ((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_2018_valueOrError2_).IsFailure():
            output = (d_2018_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_2014_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_2019_dynamoDbKey_: _dafny.Map
        d_2019_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(Structure.default__.BEACON__KEY__TYPE__VALUE)})
        d_2020_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_2020_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_2019_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2021_maybeGetItem_: Wrappers.Result
        out356_: Wrappers.Result
        out356_ = (ddbClient).GetItem(d_2020_ItemRequest_)
        d_2021_maybeGetItem_ = out356_
        d_2022_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_2023_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda141_(d_2024_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2024_e_)

        d_2023_valueOrError0_ = (d_2021_maybeGetItem_).MapFailure(lambda141_)
        if (d_2023_valueOrError0_).IsFailure():
            output = (d_2023_valueOrError0_).PropagateFailure()
            return output
        d_2022_getItemResponse_ = (d_2023_valueOrError0_).Extract()
        d_2025_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2025_valueOrError1_ = Wrappers.default__.Need(((d_2022_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_2025_valueOrError1_).IsFailure():
            output = (d_2025_valueOrError1_).PropagateFailure()
            return output
        d_2026_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2026_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_2022_getItemResponse_).Item).value)) and ((((((d_2022_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_2026_valueOrError2_).IsFailure():
            output = (d_2026_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_2022_getItemResponse_).Item).value)
        return output

    @staticmethod
    def CreateTransactWritePutItem(item, tableName, ConditionExpression):
        def lambda142_(source63_):
            if source63_.is_BRANCH__KEY__NOT__EXIST:
                return default__.BRANCH__KEY__NOT__EXIST__CONDITION
            elif True:
                return default__.BRANCH__KEY__EXISTS__CONDITION

        return software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItem_TransactWriteItem(Wrappers.Option_None(), Wrappers.Option_Some(software_amazon_cryptography_services_dynamodb_internaldafny_types.Put_Put(item, tableName, Wrappers.Option_Some(lambda142_(ConditionExpression)), Wrappers.Option_Some(default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES), Wrappers.Option_None(), Wrappers.Option_None())), Wrappers.Option_None(), Wrappers.Option_None())

    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME(instance):
        return _dafny.Seq("#BranchKeyIdentifierField")
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES(instance):
        return _dafny.Map({default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME: Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD})
    @_dafny.classproperty
    def BRANCH__KEY__NOT__EXIST__CONDITION(instance):
        return ((_dafny.Seq("attribute_not_exists(")) + (default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__CONDITION(instance):
        return ((_dafny.Seq("attribute_exists(")) + (default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))

class ConditionExpression:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConditionExpression_BRANCH__KEY__NOT__EXIST(), ConditionExpression_BRANCH__KEY__EXISTS()]
    @classmethod
    def default(cls, ):
        return lambda: ConditionExpression_BRANCH__KEY__NOT__EXIST()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BRANCH__KEY__NOT__EXIST(self) -> bool:
        return isinstance(self, ConditionExpression_BRANCH__KEY__NOT__EXIST)
    @property
    def is_BRANCH__KEY__EXISTS(self) -> bool:
        return isinstance(self, ConditionExpression_BRANCH__KEY__EXISTS)

class ConditionExpression_BRANCH__KEY__NOT__EXIST(ConditionExpression, NamedTuple('BRANCH__KEY__NOT__EXIST', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_NOT_EXIST'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionExpression_BRANCH__KEY__NOT__EXIST)
    def __hash__(self) -> int:
        return super().__hash__()

class ConditionExpression_BRANCH__KEY__EXISTS(ConditionExpression, NamedTuple('BRANCH__KEY__EXISTS', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_EXISTS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionExpression_BRANCH__KEY__EXISTS)
    def __hash__(self) -> int:
        return super().__hash__()

