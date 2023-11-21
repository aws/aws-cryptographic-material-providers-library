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
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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

assert "TestUtils" == __name__
TestUtils = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateInvalidEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_1618_validUTF8char_: _dafny.Seq
        d_1619_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1619_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1619_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(42,43): " + _dafny.string_of(d_1619_valueOrError0_))
        d_1618_validUTF8char_ = (d_1619_valueOrError0_).Extract()
        d_1620_key_: _dafny.Seq
        d_1620_key_ = _dafny.Seq([])
        while (len(d_1620_key_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT):
            d_1620_key_ = (d_1620_key_) + (d_1618_validUTF8char_)
        encCtx = _dafny.Map({d_1620_key_: _dafny.Seq([0])})
        return encCtx

    @staticmethod
    def GenerateLargeValidEncryptionContext():
        r: _dafny.Map = _dafny.Map({})
        d_1621_numMaxPairs_: int
        d_1621_numMaxPairs_ = 9361
        d_1622_val_: _dafny.Seq
        d_1623_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1623_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1623_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(62,12): " + _dafny.string_of(d_1623_valueOrError0_))
        d_1622_val_ = (d_1623_valueOrError0_).Extract()
        d_1624_encCtx_: _dafny.Map
        d_1624_encCtx_ = _dafny.Map({})
        d_1625_i_: int
        d_1625_i_ = 0
        while ((len(d_1624_encCtx_)) < (d_1621_numMaxPairs_)) and ((d_1625_i_) < (65536)):
            d_1626_key_: _dafny.Seq
            d_1626_key_ = StandardLibrary_mUInt.default__.UInt16ToSeq(d_1625_i_)
            if UTF8.default__.ValidUTF8Seq(d_1626_key_):
                d_1624_encCtx_ = (d_1624_encCtx_).set(d_1626_key_, d_1622_val_)
            d_1625_i_ = (d_1625_i_) + (1)
        r = d_1624_encCtx_
        return r
        return r

    @staticmethod
    def SmallEncryptionContext(v):
        encryptionContext: _dafny.Map = _dafny.Map({})
        d_1627_keyA_: _dafny.Seq
        d_1628_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1628_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_1628_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(90,13): " + _dafny.string_of(d_1628_valueOrError0_))
        d_1627_keyA_ = (d_1628_valueOrError0_).Extract()
        d_1629_valA_: _dafny.Seq
        d_1630_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1630_valueOrError1_ = UTF8.default__.Encode(_dafny.Seq("valA"))
        if not(not((d_1630_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(91,13): " + _dafny.string_of(d_1630_valueOrError1_))
        d_1629_valA_ = (d_1630_valueOrError1_).Extract()
        d_1631_keyB_: _dafny.Seq
        d_1632_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1632_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("keyB"))
        if not(not((d_1632_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(92,13): " + _dafny.string_of(d_1632_valueOrError2_))
        d_1631_keyB_ = (d_1632_valueOrError2_).Extract()
        d_1633_valB_: _dafny.Seq
        d_1634_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1634_valueOrError3_ = UTF8.default__.Encode(_dafny.Seq("valB"))
        if not(not((d_1634_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(93,13): " + _dafny.string_of(d_1634_valueOrError3_))
        d_1633_valB_ = (d_1634_valueOrError3_).Extract()
        source39_ = v
        if source39_.is_Empty:
            encryptionContext = _dafny.Map({})
        elif source39_.is_A:
            encryptionContext = _dafny.Map({d_1627_keyA_: d_1629_valA_})
        elif source39_.is_AB:
            encryptionContext = _dafny.Map({d_1627_keyA_: d_1629_valA_, d_1631_keyB_: d_1633_valB_})
        elif True:
            encryptionContext = _dafny.Map({d_1631_keyB_: d_1633_valB_, d_1627_keyA_: d_1629_valA_})
        return encryptionContext

    @staticmethod
    def GenerateMockEncryptedDataKey(keyProviderId, keyProviderInfo):
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey.default()()
        d_1635_encodedkeyProviderId_: _dafny.Seq
        d_1636_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1636_valueOrError0_ = UTF8.default__.Encode(keyProviderId)
        if not(not((d_1636_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(113,29): " + _dafny.string_of(d_1636_valueOrError0_))
        d_1635_encodedkeyProviderId_ = (d_1636_valueOrError0_).Extract()
        d_1637_encodedKeyProviderInfo_: _dafny.Seq
        d_1638_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1638_valueOrError1_ = UTF8.default__.Encode(keyProviderInfo)
        if not(not((d_1638_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(114,31): " + _dafny.string_of(d_1638_valueOrError1_))
        d_1637_encodedKeyProviderInfo_ = (d_1638_valueOrError1_).Extract()
        d_1639_fakeCiphertext_: _dafny.Seq
        d_1640_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1640_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("fakeCiphertext"))
        if not(not((d_1640_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(115,23): " + _dafny.string_of(d_1640_valueOrError2_))
        d_1639_fakeCiphertext_ = (d_1640_valueOrError2_).Extract()
        edk = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_1635_encodedkeyProviderId_, d_1637_encodedKeyProviderInfo_, d_1639_fakeCiphertext_)
        return edk
        return edk

    @staticmethod
    def NamespaceAndName(n):
        namespace: _dafny.Seq = _dafny.Seq({})
        name: _dafny.Seq = _dafny.Seq({})
        d_1641_s_: _dafny.Seq
        d_1641_s_ = (_dafny.Seq("child")) + (_dafny.Seq([_dafny.plus_char(chr(n), '0')]))
        namespace = (d_1641_s_) + (_dafny.Seq(" Namespace"))
        name = (d_1641_s_) + (_dafny.Seq(" Name"))
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
        return isinstance(self, TestUtils.SmallEncryptionContextVariation_Empty)
    @property
    def is_A(self) -> bool:
        return isinstance(self, TestUtils.SmallEncryptionContextVariation_A)
    @property
    def is_AB(self) -> bool:
        return isinstance(self, TestUtils.SmallEncryptionContextVariation_AB)
    @property
    def is_BA(self) -> bool:
        return isinstance(self, TestUtils.SmallEncryptionContextVariation_BA)

class SmallEncryptionContextVariation_Empty(SmallEncryptionContextVariation, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestUtils.SmallEncryptionContextVariation_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_A(SmallEncryptionContextVariation, NamedTuple('A', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.A'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestUtils.SmallEncryptionContextVariation_A)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_AB(SmallEncryptionContextVariation, NamedTuple('AB', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.AB'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestUtils.SmallEncryptionContextVariation_AB)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_BA(SmallEncryptionContextVariation, NamedTuple('BA', [])):
    def __dafnystr__(self) -> str:
        return f'TestUtils.SmallEncryptionContextVariation.BA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestUtils.SmallEncryptionContextVariation_BA)
    def __hash__(self) -> int:
        return super().__hash__()

