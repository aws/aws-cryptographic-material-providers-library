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
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import AwsCryptographyKeyStoreOperations

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
        d_2118_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2118_valueOrError0_ = Wrappers.default__.Need((software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__KeyIdType(((config).kmsConfiguration).kmsKeyArn)) and ((AwsArnParsing.default__.ParseAwsKmsArn(((config).kmsConfiguration).kmsKeyArn)).is_Success), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid AWS KMS Key Arn")))
        if (d_2118_valueOrError0_).IsFailure():
            res = (d_2118_valueOrError0_).PropagateFailure()
            return res
        d_2119_grantTokens_: Wrappers.Result
        d_2119_grantTokens_ = AwsKmsUtils.default__.GetValidGrantTokens((config).grantTokens)
        d_2120_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2120_valueOrError1_ = Wrappers.default__.Need((True) and ((d_2119_grantTokens_).is_Success), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("CreateKey received invalid grant tokens")))
        if (d_2120_valueOrError1_).IsFailure():
            res = (d_2120_valueOrError1_).PropagateFailure()
            return res
        d_2121_keyStoreId_: _dafny.Seq = _dafny.Seq({})
        if ((config).id).is_Some:
            d_2121_keyStoreId_ = ((config).id).value
        elif True:
            d_2122_maybeUuid_: Wrappers.Result
            out383_: Wrappers.Result
            out383_ = UUID.default__.GenerateUUID()
            d_2122_maybeUuid_ = out383_
            d_2123_uuid_: _dafny.Seq
            d_2124_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            def lambda149_(d_2125_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_2125_e_)

            d_2124_valueOrError2_ = (d_2122_maybeUuid_).MapFailure(lambda149_)
            if (d_2124_valueOrError2_).IsFailure():
                res = (d_2124_valueOrError2_).PropagateFailure()
                return res
            d_2123_uuid_ = (d_2124_valueOrError2_).Extract()
            d_2121_keyStoreId_ = d_2123_uuid_
        d_2126_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        d_2127_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient = None
        d_2128_keyArn_: Wrappers.Result
        d_2128_keyArn_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(((config).kmsConfiguration).kmsKeyArn)
        d_2129_kmsRegion_: Wrappers.Option
        d_2129_kmsRegion_ = AwsArnParsing.default__.GetRegion((d_2128_keyArn_).value)
        if ((config).kmsClient).is_None:
            d_2130_maybeKmsClient_: Wrappers.Result
            out384_: Wrappers.Result
            out384_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClientForRegion((d_2129_kmsRegion_).value)
            d_2130_maybeKmsClient_ = out384_
            d_2131_valueOrError3_: Wrappers.Result = None
            def lambda150_(d_2132_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_2132_e_)

            d_2131_valueOrError3_ = (d_2130_maybeKmsClient_).MapFailure(lambda150_)
            if (d_2131_valueOrError3_).IsFailure():
                res = (d_2131_valueOrError3_).PropagateFailure()
                return res
            d_2126_kmsClient_ = (d_2131_valueOrError3_).Extract()
        elif True:
            d_2126_kmsClient_ = ((config).kmsClient).value
        if ((config).ddbClient).is_None:
            d_2133_maybeDdbClient_: Wrappers.Result
            out385_: Wrappers.Result
            out385_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DDBClientForRegion((d_2129_kmsRegion_).value)
            d_2133_maybeDdbClient_ = out385_
            d_2134_valueOrError4_: Wrappers.Result = None
            def lambda151_(d_2135_e_):
                return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2135_e_)

            d_2134_valueOrError4_ = (d_2133_maybeDdbClient_).MapFailure(lambda151_)
            if (d_2134_valueOrError4_).IsFailure():
                res = (d_2134_valueOrError4_).PropagateFailure()
                return res
            d_2127_ddbClient_ = (d_2134_valueOrError4_).Extract()
        elif True:
            d_2127_ddbClient_ = ((config).ddbClient).value
        d_2136_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2136_valueOrError5_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName((config).ddbTableName), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid Amazon DynamoDB Table Name")))
        if (d_2136_valueOrError5_).IsFailure():
            res = (d_2136_valueOrError5_).PropagateFailure()
            return res
        d_2137_client_: KeyStoreClient
        nw76_ = KeyStoreClient()
        nw76_.ctor__(AwsCryptographyKeyStoreOperations.Config_Config(d_2121_keyStoreId_, (config).ddbTableName, (config).logicalKeyStoreName, (config).kmsConfiguration, (d_2119_grantTokens_).value, d_2126_kmsClient_, d_2127_ddbClient_))
        d_2137_client_ = nw76_
        res = Wrappers.Result_Success(d_2137_client_)
        return res
        return res


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
        out386_: Wrappers.Result
        out386_ = AwsCryptographyKeyStoreOperations.default__.GetKeyStoreInfo((self).config)
        output = out386_
        return output

    def CreateKeyStore(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        out387_: Wrappers.Result
        out387_ = AwsCryptographyKeyStoreOperations.default__.CreateKeyStore((self).config, input)
        output = out387_
        return output

    def CreateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out388_: Wrappers.Result
        out388_ = AwsCryptographyKeyStoreOperations.default__.CreateKey((self).config, input)
        output = out388_
        return output

    def VersionKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        out389_: Wrappers.Result
        out389_ = AwsCryptographyKeyStoreOperations.default__.VersionKey((self).config, input)
        output = out389_
        return output

    def GetActiveBranchKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out390_: Wrappers.Result
        out390_ = AwsCryptographyKeyStoreOperations.default__.GetActiveBranchKey((self).config, input)
        output = out390_
        return output

    def GetBranchKeyVersion(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out391_: Wrappers.Result
        out391_ = AwsCryptographyKeyStoreOperations.default__.GetBranchKeyVersion((self).config, input)
        output = out391_
        return output

    def GetBeaconKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out392_: Wrappers.Result
        out392_ = AwsCryptographyKeyStoreOperations.default__.GetBeaconKey((self).config, input)
        output = out392_
        return output

    @property
    def config(self):
        return self._config
