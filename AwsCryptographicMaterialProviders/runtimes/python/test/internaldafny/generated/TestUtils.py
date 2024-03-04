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
import software_amazon_cryptography_keystore_internaldafny_types
import Relations
import Seq_MergeSort
import Math
import Seq
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import UUID
import Time
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import Base64
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
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
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
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
import AesKdfCtr
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
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey

# Module: TestUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateInvalidEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_199_validUTF8char_: _dafny.Seq
        d_200_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_200_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_200_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(42,43): " + _dafny.string_of(d_200_valueOrError0_))
        d_199_validUTF8char_ = (d_200_valueOrError0_).Extract()
        d_201_key_: _dafny.Seq
        d_201_key_ = _dafny.Seq([])
        while (len(d_201_key_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT):
            d_201_key_ = (d_201_key_) + (d_199_validUTF8char_)
        encCtx = _dafny.Map({d_201_key_: _dafny.Seq([0])})
        return encCtx

    @staticmethod
    def GenerateLargeValidEncryptionContext():
        r: _dafny.Map = _dafny.Map({})
        d_202_numMaxPairs_: int
        d_202_numMaxPairs_ = 9361
        d_203_val_: _dafny.Seq
        d_204_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_204_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_204_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(62,12): " + _dafny.string_of(d_204_valueOrError0_))
        d_203_val_ = (d_204_valueOrError0_).Extract()
        d_205_encCtx_: _dafny.Map
        d_205_encCtx_ = _dafny.Map({})
        d_206_i_: int
        d_206_i_ = 0
        while ((len(d_205_encCtx_)) < (d_202_numMaxPairs_)) and ((d_206_i_) < (65536)):
            d_207_key_: _dafny.Seq
            d_207_key_ = StandardLibrary_UInt.default__.UInt16ToSeq(d_206_i_)
            if UTF8.default__.ValidUTF8Seq(d_207_key_):
                d_205_encCtx_ = (d_205_encCtx_).set(d_207_key_, d_203_val_)
            d_206_i_ = (d_206_i_) + (1)
        r = d_205_encCtx_
        return r
        return r

    @staticmethod
    def SmallEncryptionContext(v):
        encryptionContext: _dafny.Map = _dafny.Map({})
        d_208_keyA_: _dafny.Seq
        d_209_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_209_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_209_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(90,13): " + _dafny.string_of(d_209_valueOrError0_))
        d_208_keyA_ = (d_209_valueOrError0_).Extract()
        d_210_valA_: _dafny.Seq
        d_211_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_211_valueOrError1_ = UTF8.default__.Encode(_dafny.Seq("valA"))
        if not(not((d_211_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(91,13): " + _dafny.string_of(d_211_valueOrError1_))
        d_210_valA_ = (d_211_valueOrError1_).Extract()
        d_212_keyB_: _dafny.Seq
        d_213_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_213_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("keyB"))
        if not(not((d_213_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(92,13): " + _dafny.string_of(d_213_valueOrError2_))
        d_212_keyB_ = (d_213_valueOrError2_).Extract()
        d_214_valB_: _dafny.Seq
        d_215_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_215_valueOrError3_ = UTF8.default__.Encode(_dafny.Seq("valB"))
        if not(not((d_215_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(93,13): " + _dafny.string_of(d_215_valueOrError3_))
        d_214_valB_ = (d_215_valueOrError3_).Extract()
        source0_ = v
        if source0_.is_Empty:
            encryptionContext = _dafny.Map({})
        elif source0_.is_A:
            encryptionContext = _dafny.Map({d_208_keyA_: d_210_valA_})
        elif source0_.is_AB:
            encryptionContext = _dafny.Map({d_208_keyA_: d_210_valA_, d_212_keyB_: d_214_valB_})
        elif True:
            encryptionContext = _dafny.Map({d_212_keyB_: d_214_valB_, d_208_keyA_: d_210_valA_})
        return encryptionContext

    @staticmethod
    def GenerateMockEncryptedDataKey(keyProviderId, keyProviderInfo):
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey.default()()
        d_216_encodedkeyProviderId_: _dafny.Seq
        d_217_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_217_valueOrError0_ = UTF8.default__.Encode(keyProviderId)
        if not(not((d_217_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(113,29): " + _dafny.string_of(d_217_valueOrError0_))
        d_216_encodedkeyProviderId_ = (d_217_valueOrError0_).Extract()
        d_218_encodedKeyProviderInfo_: _dafny.Seq
        d_219_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_219_valueOrError1_ = UTF8.default__.Encode(keyProviderInfo)
        if not(not((d_219_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(114,31): " + _dafny.string_of(d_219_valueOrError1_))
        d_218_encodedKeyProviderInfo_ = (d_219_valueOrError1_).Extract()
        d_220_fakeCiphertext_: _dafny.Seq
        d_221_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_221_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("fakeCiphertext"))
        if not(not((d_221_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(115,23): " + _dafny.string_of(d_221_valueOrError2_))
        d_220_fakeCiphertext_ = (d_221_valueOrError2_).Extract()
        edk = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_216_encodedkeyProviderId_, d_218_encodedKeyProviderInfo_, d_220_fakeCiphertext_)
        return edk
        return edk

    @staticmethod
    def NamespaceAndName(n):
        namespace: _dafny.Seq = _dafny.Seq({})
        name: _dafny.Seq = _dafny.Seq({})
        d_222_s_: _dafny.Seq
        d_222_s_ = (_dafny.Seq("child")) + (_dafny.Seq([_dafny.plus_char(chr(n), '0')]))
        namespace = (d_222_s_) + (_dafny.Seq(" Namespace"))
        name = (d_222_s_) + (_dafny.Seq(" Name"))
        return namespace, name

    @_dafny.classproperty
    def KMS__RSA__PUBLIC__KEY(instance):
        return ((((((((_dafny.Seq("-----BEGIN PUBLIC KEY-----\n")) + (_dafny.Seq("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27Uc/fBaMVhxCE/SpCMQ\n"))) + (_dafny.Seq("oSBRSzQJw+o2hBaA+FiPGtiJ/aPy7sn18aCkelaSj4kwoC79b/arNHlkjc7OJFsN\n"))) + (_dafny.Seq("/GoFKgNvaiY4lOeJqEiWQGSSgHtsJLdbO2u4OOSxh8qIRAMKbMgQDVX4FR/PLKeK\n"))) + (_dafny.Seq("fc2aCDvcNSpAM++8NlNmv7+xQBJydr5ce91eISbHkFRkK3/bAM+1iddupoRw4Wo2\n"))) + (_dafny.Seq("r3avzrg5xBHmzR7u1FTab22Op3Hgb2dBLZH43wNKAceVwKqKA8UNAxashFON7xK9\n"))) + (_dafny.Seq("yy4kfOL0Z/nhxRKe4jRZ/5v508qIzgzCksYy7Y3QbMejAtiYnr7s5/d5KWw0swou\n"))) + (_dafny.Seq("twIDAQAB\n"))) + (_dafny.Seq("-----END PUBLIC KEY-----"))
    @_dafny.classproperty
    def KMS__RSA__PRIVATE__KEY__ARN(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
    @_dafny.classproperty
    def SHARED__TEST__KEY__ARN(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
    @_dafny.classproperty
    def ACCOUNT__IDS(instance):
        return _dafny.Seq([_dafny.Seq("658956600833")])
    @_dafny.classproperty
    def PARTITION(instance):
        return _dafny.Seq("aws")

class SmallEncryptionContextVariation:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [SmallEncryptionContextVariation_Empty(), SmallEncryptionContextVariation_A(), SmallEncryptionContextVariation_AB(), SmallEncryptionContextVariation_BA()]
    @classmethod
    def default(cls, ):
        return lambda: SmallEncryptionContextVariation_Empty()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Empty(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_Empty)
    @property
    def is_A(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_A)
    @property
    def is_AB(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_AB)
    @property
    def is_BA(self) -> bool:
        return isinstance(self, SmallEncryptionContextVariation_BA)

class SmallEncryptionContextVariation_Empty(SmallEncryptionContextVariation, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_A(SmallEncryptionContextVariation, NamedTuple('A', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.A'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_A)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_AB(SmallEncryptionContextVariation, NamedTuple('AB', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.AB'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_AB)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_BA(SmallEncryptionContextVariation, NamedTuple('BA', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.BA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_BA)
    def __hash__(self) -> int:
        return super().__hash__()

