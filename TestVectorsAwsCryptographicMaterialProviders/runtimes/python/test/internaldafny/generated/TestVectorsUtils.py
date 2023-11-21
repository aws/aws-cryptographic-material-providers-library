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

assert "TestVectorsUtils" == __name__
TestVectorsUtils = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateInvalidEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_1232_validUTF8char_: _dafny.Seq
        d_1233_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1233_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1233_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(39,43): " + _dafny.string_of(d_1233_valueOrError0_))
        d_1232_validUTF8char_ = (d_1233_valueOrError0_).Extract()
        d_1234_key_: _dafny.Seq
        d_1234_key_ = _dafny.Seq([])
        while (len(d_1234_key_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT):
            d_1234_key_ = (d_1234_key_) + (d_1232_validUTF8char_)
        encCtx = _dafny.Map({d_1234_key_: _dafny.Seq([0])})
        return encCtx

    @staticmethod
    def GenerateLargeValidEncryptionContext():
        r: _dafny.Map = _dafny.Map({})
        d_1235_numMaxPairs_: int
        d_1235_numMaxPairs_ = 9361
        d_1236_val_: _dafny.Seq
        d_1237_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1237_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1237_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(59,12): " + _dafny.string_of(d_1237_valueOrError0_))
        d_1236_val_ = (d_1237_valueOrError0_).Extract()
        d_1238_encCtx_: _dafny.Map
        d_1238_encCtx_ = _dafny.Map({})
        d_1239_i_: int
        d_1239_i_ = 0
        while ((len(d_1238_encCtx_)) < (d_1235_numMaxPairs_)) and ((d_1239_i_) < (65536)):
            d_1240_key_: _dafny.Seq
            d_1240_key_ = StandardLibrary_mUInt.default__.UInt16ToSeq(d_1239_i_)
            if UTF8.default__.ValidUTF8Seq(d_1240_key_):
                d_1238_encCtx_ = (d_1238_encCtx_).set(d_1240_key_, d_1236_val_)
            d_1239_i_ = (d_1239_i_) + (1)
        r = d_1238_encCtx_
        return r
        return r

    @staticmethod
    def SmallEncryptionContext(v):
        encryptionContext: _dafny.Map = _dafny.Map({})
        d_1241_keyA_: _dafny.Seq
        d_1242_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1242_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_1242_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(86,13): " + _dafny.string_of(d_1242_valueOrError0_))
        d_1241_keyA_ = (d_1242_valueOrError0_).Extract()
        d_1243_valA_: _dafny.Seq
        d_1244_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1244_valueOrError1_ = UTF8.default__.Encode(_dafny.Seq("valA"))
        if not(not((d_1244_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(87,13): " + _dafny.string_of(d_1244_valueOrError1_))
        d_1243_valA_ = (d_1244_valueOrError1_).Extract()
        d_1245_keyB_: _dafny.Seq
        d_1246_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1246_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("keyB"))
        if not(not((d_1246_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(88,13): " + _dafny.string_of(d_1246_valueOrError2_))
        d_1245_keyB_ = (d_1246_valueOrError2_).Extract()
        d_1247_valB_: _dafny.Seq
        d_1248_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1248_valueOrError3_ = UTF8.default__.Encode(_dafny.Seq("valB"))
        if not(not((d_1248_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(89,13): " + _dafny.string_of(d_1248_valueOrError3_))
        d_1247_valB_ = (d_1248_valueOrError3_).Extract()
        source37_ = v
        if source37_.is_Empty:
            encryptionContext = _dafny.Map({})
        elif source37_.is_A:
            encryptionContext = _dafny.Map({d_1241_keyA_: d_1243_valA_})
        elif source37_.is_AB:
            encryptionContext = _dafny.Map({d_1241_keyA_: d_1243_valA_, d_1245_keyB_: d_1247_valB_})
        elif True:
            encryptionContext = _dafny.Map({d_1245_keyB_: d_1247_valB_, d_1241_keyA_: d_1243_valA_})
        return encryptionContext

    @staticmethod
    def GenerateMockEncryptedDataKey(keyProviderId, keyProviderInfo):
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey.default()()
        d_1249_encodedkeyProviderId_: _dafny.Seq
        d_1250_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1250_valueOrError0_ = UTF8.default__.Encode(keyProviderId)
        if not(not((d_1250_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(109,29): " + _dafny.string_of(d_1250_valueOrError0_))
        d_1249_encodedkeyProviderId_ = (d_1250_valueOrError0_).Extract()
        d_1251_encodedKeyProviderInfo_: _dafny.Seq
        d_1252_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1252_valueOrError1_ = UTF8.default__.Encode(keyProviderInfo)
        if not(not((d_1252_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(110,31): " + _dafny.string_of(d_1252_valueOrError1_))
        d_1251_encodedKeyProviderInfo_ = (d_1252_valueOrError1_).Extract()
        d_1253_fakeCiphertext_: _dafny.Seq
        d_1254_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1254_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("fakeCiphertext"))
        if not(not((d_1254_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(111,23): " + _dafny.string_of(d_1254_valueOrError2_))
        d_1253_fakeCiphertext_ = (d_1254_valueOrError2_).Extract()
        edk = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_1249_encodedkeyProviderId_, d_1251_encodedKeyProviderInfo_, d_1253_fakeCiphertext_)
        return edk
        return edk

    @staticmethod
    def NamespaceAndName(n):
        namespace: _dafny.Seq = _dafny.Seq({})
        name: _dafny.Seq = _dafny.Seq({})
        d_1255_s_: _dafny.Seq
        d_1255_s_ = (_dafny.Seq("child")) + (_dafny.Seq([_dafny.plus_char(chr(n), '0')]))
        namespace = (d_1255_s_) + (_dafny.Seq(" Namespace"))
        name = (d_1255_s_) + (_dafny.Seq(" Name"))
        return namespace, name

    @staticmethod
    def GetEncryptionMaterials(mpl, algorithmSuiteId, encryptionContext):
        encryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_1256_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1257_valueOrError0_: Wrappers.Result = None
        out256_: Wrappers.Result
        out256_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1257_valueOrError0_ = out256_
        if not(not((d_1257_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(139,15): " + _dafny.string_of(d_1257_valueOrError0_))
        d_1256_crypto_ = (d_1257_valueOrError0_).Extract()
        d_1258_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1258_suite_ = AlgorithmSuites.default__.GetSuite(algorithmSuiteId)
        d_1259_signingKey_: Wrappers.Option = Wrappers.Option_None.default()()
        d_1260_verificationKey_: Wrappers.Option = Wrappers.Option_None.default()()
        if ((d_1258_suite_).signature).is_ECDSA:
            d_1261_pair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput
            d_1262_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
            out257_: Wrappers.Result
            out257_ = (d_1256_crypto_).GenerateECDSASignatureKey(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_1258_suite_).signature).ECDSA).curve))
            d_1262_valueOrError1_ = out257_
            if not(not((d_1262_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(144,15): " + _dafny.string_of(d_1262_valueOrError1_))
            d_1261_pair_ = (d_1262_valueOrError1_).Extract()
            d_1259_signingKey_ = Wrappers.Option_Some((d_1261_pair_).signingKey)
            d_1260_verificationKey_ = Wrappers.Option_Some((d_1261_pair_).verificationKey)
        elif True:
            d_1259_signingKey_ = Wrappers.Option_None()
            d_1260_verificationKey_ = Wrappers.Option_None()
        d_1263_valueOrError2_: Wrappers.Result = None
        d_1263_valueOrError2_ = (mpl).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(algorithmSuiteId, encryptionContext, _dafny.Seq([]), d_1259_signingKey_, d_1260_verificationKey_))
        if not(not((d_1263_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(157,24): " + _dafny.string_of(d_1263_valueOrError2_))
        encryptionMaterials = (d_1263_valueOrError2_).Extract()
        return encryptionMaterials

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
        return isinstance(self, TestVectorsUtils.SmallEncryptionContextVariation_Empty)
    @property
    def is_A(self) -> bool:
        return isinstance(self, TestVectorsUtils.SmallEncryptionContextVariation_A)
    @property
    def is_AB(self) -> bool:
        return isinstance(self, TestVectorsUtils.SmallEncryptionContextVariation_AB)
    @property
    def is_BA(self) -> bool:
        return isinstance(self, TestVectorsUtils.SmallEncryptionContextVariation_BA)

class SmallEncryptionContextVariation_Empty(SmallEncryptionContextVariation, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorsUtils.SmallEncryptionContextVariation_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_A(SmallEncryptionContextVariation, NamedTuple('A', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.A'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorsUtils.SmallEncryptionContextVariation_A)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_AB(SmallEncryptionContextVariation, NamedTuple('AB', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.AB'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorsUtils.SmallEncryptionContextVariation_AB)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_BA(SmallEncryptionContextVariation, NamedTuple('BA', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.BA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVectorsUtils.SmallEncryptionContextVariation_BA)
    def __hash__(self) -> int:
        return super().__hash__()

