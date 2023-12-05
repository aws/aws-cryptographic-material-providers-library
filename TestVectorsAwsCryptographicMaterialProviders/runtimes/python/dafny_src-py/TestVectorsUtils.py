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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import software_amazon_cryptography_materialproviders_internaldafny_wrapped

# Module: TestVectorsUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateInvalidEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_0_validUTF8char_: _dafny.Seq
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(39,43): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_validUTF8char_ = (d_1_valueOrError0_).Extract()
        d_2_key_: _dafny.Seq
        d_2_key_ = _dafny.Seq([])
        while (len(d_2_key_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT):
            d_2_key_ = (d_2_key_) + (d_0_validUTF8char_)
        encCtx = _dafny.Map({d_2_key_: _dafny.Seq([0])})
        return encCtx

    @staticmethod
    def GenerateLargeValidEncryptionContext():
        r: _dafny.Map = _dafny.Map({})
        d_3_numMaxPairs_: int
        d_3_numMaxPairs_ = 9361
        d_4_val_: _dafny.Seq
        d_5_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_5_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("a"))
        if not(not((d_5_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(59,12): " + _dafny.string_of(d_5_valueOrError0_))
        d_4_val_ = (d_5_valueOrError0_).Extract()
        d_6_encCtx_: _dafny.Map
        d_6_encCtx_ = _dafny.Map({})
        d_7_i_: int
        d_7_i_ = 0
        while ((len(d_6_encCtx_)) < (d_3_numMaxPairs_)) and ((d_7_i_) < (65536)):
            d_8_key_: _dafny.Seq
            d_8_key_ = StandardLibrary_UInt.default__.UInt16ToSeq(d_7_i_)
            if UTF8.default__.ValidUTF8Seq(d_8_key_):
                d_6_encCtx_ = (d_6_encCtx_).set(d_8_key_, d_4_val_)
            d_7_i_ = (d_7_i_) + (1)
        r = d_6_encCtx_
        return r
        return r

    @staticmethod
    def SmallEncryptionContext(v):
        encryptionContext: _dafny.Map = _dafny.Map({})
        d_9_keyA_: _dafny.Seq
        d_10_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_10_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_10_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(86,13): " + _dafny.string_of(d_10_valueOrError0_))
        d_9_keyA_ = (d_10_valueOrError0_).Extract()
        d_11_valA_: _dafny.Seq
        d_12_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_12_valueOrError1_ = UTF8.default__.Encode(_dafny.Seq("valA"))
        if not(not((d_12_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(87,13): " + _dafny.string_of(d_12_valueOrError1_))
        d_11_valA_ = (d_12_valueOrError1_).Extract()
        d_13_keyB_: _dafny.Seq
        d_14_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_14_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("keyB"))
        if not(not((d_14_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(88,13): " + _dafny.string_of(d_14_valueOrError2_))
        d_13_keyB_ = (d_14_valueOrError2_).Extract()
        d_15_valB_: _dafny.Seq
        d_16_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_16_valueOrError3_ = UTF8.default__.Encode(_dafny.Seq("valB"))
        if not(not((d_16_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(89,13): " + _dafny.string_of(d_16_valueOrError3_))
        d_15_valB_ = (d_16_valueOrError3_).Extract()
        source0_ = v
        if source0_.is_Empty:
            encryptionContext = _dafny.Map({})
        elif source0_.is_A:
            encryptionContext = _dafny.Map({d_9_keyA_: d_11_valA_})
        elif source0_.is_AB:
            encryptionContext = _dafny.Map({d_9_keyA_: d_11_valA_, d_13_keyB_: d_15_valB_})
        elif True:
            encryptionContext = _dafny.Map({d_13_keyB_: d_15_valB_, d_9_keyA_: d_11_valA_})
        return encryptionContext

    @staticmethod
    def GenerateMockEncryptedDataKey(keyProviderId, keyProviderInfo):
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey.default()()
        d_17_encodedkeyProviderId_: _dafny.Seq
        d_18_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_18_valueOrError0_ = UTF8.default__.Encode(keyProviderId)
        if not(not((d_18_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(109,29): " + _dafny.string_of(d_18_valueOrError0_))
        d_17_encodedkeyProviderId_ = (d_18_valueOrError0_).Extract()
        d_19_encodedKeyProviderInfo_: _dafny.Seq
        d_20_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_20_valueOrError1_ = UTF8.default__.Encode(keyProviderInfo)
        if not(not((d_20_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(110,31): " + _dafny.string_of(d_20_valueOrError1_))
        d_19_encodedKeyProviderInfo_ = (d_20_valueOrError1_).Extract()
        d_21_fakeCiphertext_: _dafny.Seq
        d_22_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_22_valueOrError2_ = UTF8.default__.Encode(_dafny.Seq("fakeCiphertext"))
        if not(not((d_22_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(111,23): " + _dafny.string_of(d_22_valueOrError2_))
        d_21_fakeCiphertext_ = (d_22_valueOrError2_).Extract()
        edk = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_17_encodedkeyProviderId_, d_19_encodedKeyProviderInfo_, d_21_fakeCiphertext_)
        return edk
        return edk

    @staticmethod
    def NamespaceAndName(n):
        namespace: _dafny.Seq = _dafny.Seq({})
        name: _dafny.Seq = _dafny.Seq({})
        d_23_s_: _dafny.Seq
        d_23_s_ = (_dafny.Seq("child")) + (_dafny.Seq([_dafny.plus_char(chr(n), '0')]))
        namespace = (d_23_s_) + (_dafny.Seq(" Namespace"))
        name = (d_23_s_) + (_dafny.Seq(" Name"))
        return namespace, name

    @staticmethod
    def GetEncryptionMaterials(mpl, algorithmSuiteId, encryptionContext):
        encryptionMaterials: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_24_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_25_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_25_valueOrError0_ = out0_
        if not(not((d_25_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(139,15): " + _dafny.string_of(d_25_valueOrError0_))
        d_24_crypto_ = (d_25_valueOrError0_).Extract()
        d_26_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_26_suite_ = AlgorithmSuites.default__.GetSuite(algorithmSuiteId)
        d_27_signingKey_: Wrappers.Option = Wrappers.Option.default()()
        d_28_verificationKey_: Wrappers.Option = Wrappers.Option.default()()
        if ((d_26_suite_).signature).is_ECDSA:
            d_29_pair_: software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput
            d_30_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
            out1_: Wrappers.Result
            out1_ = (d_24_crypto_).GenerateECDSASignatureKey(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput((((d_26_suite_).signature).ECDSA).curve))
            d_30_valueOrError1_ = out1_
            if not(not((d_30_valueOrError1_).IsFailure())):
                raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(144,15): " + _dafny.string_of(d_30_valueOrError1_))
            d_29_pair_ = (d_30_valueOrError1_).Extract()
            d_27_signingKey_ = Wrappers.Option_Some((d_29_pair_).signingKey)
            d_28_verificationKey_ = Wrappers.Option_Some((d_29_pair_).verificationKey)
        elif True:
            d_27_signingKey_ = Wrappers.Option_None()
            d_28_verificationKey_ = Wrappers.Option_None()
        d_31_valueOrError2_: Wrappers.Result = None
        d_31_valueOrError2_ = (mpl).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(algorithmSuiteId, encryptionContext, _dafny.Seq([]), d_27_signingKey_, d_28_verificationKey_))
        if not(not((d_31_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectorsUtils.dfy(157,24): " + _dafny.string_of(d_31_valueOrError2_))
        encryptionMaterials = (d_31_valueOrError2_).Extract()
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
        return f'TestVectorsUtils.SmallEncryptionContextVariation.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_A(SmallEncryptionContextVariation, NamedTuple('A', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.A'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_A)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_AB(SmallEncryptionContextVariation, NamedTuple('AB', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.AB'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_AB)
    def __hash__(self) -> int:
        return super().__hash__()

class SmallEncryptionContextVariation_BA(SmallEncryptionContextVariation, NamedTuple('BA', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorsUtils.SmallEncryptionContextVariation.BA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SmallEncryptionContextVariation_BA)
    def __hash__(self) -> int:
        return super().__hash__()

