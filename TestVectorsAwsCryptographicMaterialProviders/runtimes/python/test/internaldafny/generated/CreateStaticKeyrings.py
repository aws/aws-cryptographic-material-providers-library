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

# Module: CreateStaticKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateStaticMaterialsKeyring(encryptMaterial, decryptMaterial):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        nw73_ = StaticMaterialsKeyring()
        nw73_.ctor__(encryptMaterial, decryptMaterial)
        keyring = nw73_
        return keyring
        return keyring


class StaticMaterialsKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._encryptMaterial: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        self._decryptMaterial: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        pass

    def __dafnystr__(self) -> str:
        return "CreateStaticKeyrings.StaticMaterialsKeyring"
    def OnEncrypt(self, input):
        out301_: Wrappers.Result
        out301_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out301_

    def OnDecrypt(self, input):
        out302_: Wrappers.Result
        out302_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out302_

    def ctor__(self, encryptMaterial, decryptMaterial):
        (self)._encryptMaterial = encryptMaterial
        (self)._decryptMaterial = decryptMaterial

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput((self).encryptMaterial))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput((self).decryptMaterial))
        return res
        return res

    @property
    def encryptMaterial(self):
        return self._encryptMaterial
    @property
    def decryptMaterial(self):
        return self._decryptMaterial
