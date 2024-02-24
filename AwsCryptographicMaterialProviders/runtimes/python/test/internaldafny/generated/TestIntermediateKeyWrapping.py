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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
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
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import TestUtils

# Module: TestIntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateWrapUnwrapTest():
        d_223_encCtx_: _dafny.Map
        d_223_encCtx_ = _dafny.Map({})
        d_224_keyLen_: int
        d_224_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_225_tagLen_: int
        d_225_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_226_pdk_: _dafny.Seq
        d_226_pdk_ = _dafny.Seq([0 for d_227___v2_ in range(d_224_keyLen_)])
        d_228_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw0_ = TestGenerateAndWrapKeyMaterial()
        nw0_.ctor__()
        d_228_testGenerateAndWrap_ = nw0_
        d_229_intermediateWrapOutput_: Wrappers.Result
        out77_: Wrappers.Result
        out77_ = IntermediateKeyWrapping.default__.IntermediateWrap(d_228_testGenerateAndWrap_, d_226_pdk_, default__.TEST__ALG__SUITE, d_223_encCtx_)
        d_229_intermediateWrapOutput_ = out77_
        if not((d_229_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_229_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_224_keyLen_) + (d_225_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_229_intermediateWrapOutput_).value).wrappedMaterial)[(d_224_keyLen_) + (d_225_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_230_testUnwrap_: TestUnwrapKeyMaterial
        nw1_ = TestUnwrapKeyMaterial()
        nw1_.ctor__()
        d_230_testUnwrap_ = nw1_
        d_231_intermediateUnwrapOutput_: Wrappers.Result
        out78_: Wrappers.Result
        out78_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_230_testUnwrap_, ((d_229_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_223_encCtx_)
        d_231_intermediateUnwrapOutput_ = out78_
        if not((d_231_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_231_intermediateUnwrapOutput_).value).plaintextDataKey) == (d_226_pdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_229_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_231_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def IntermediateGenerateAndWrapUnwrapTest():
        d_232_encCtx_: _dafny.Map
        d_232_encCtx_ = _dafny.Map({})
        d_233_keyLen_: int
        d_233_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_234_tagLen_: int
        d_234_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_235_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw2_ = TestGenerateAndWrapKeyMaterial()
        nw2_.ctor__()
        d_235_testGenerateAndWrap_ = nw2_
        d_236_intermediateWrapOutput_: Wrappers.Result
        out79_: Wrappers.Result
        out79_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(d_235_testGenerateAndWrap_, default__.TEST__ALG__SUITE, d_232_encCtx_)
        d_236_intermediateWrapOutput_ = out79_
        if not((d_236_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_236_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_233_keyLen_) + (d_234_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_236_intermediateWrapOutput_).value).wrappedMaterial)[(d_233_keyLen_) + (d_234_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_237_testUnwrap_: TestUnwrapKeyMaterial
        nw3_ = TestUnwrapKeyMaterial()
        nw3_.ctor__()
        d_237_testUnwrap_ = nw3_
        d_238_intermediateUnwrapOutput_: Wrappers.Result
        out80_: Wrappers.Result
        out80_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_237_testUnwrap_, ((d_236_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_232_encCtx_)
        d_238_intermediateUnwrapOutput_ = out80_
        if not((d_238_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_236_intermediateWrapOutput_).value).plaintextDataKey) == (((d_238_intermediateUnwrapOutput_).value).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_236_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_238_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def TEST__ALG__SUITE(instance):
        return AlgorithmSuites.default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384
    @_dafny.classproperty
    def PLAINTEXT__MAT(instance):
        return _dafny.Seq([1 for d_239___v0_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])
    @_dafny.classproperty
    def WRAPPED__MAT(instance):
        return _dafny.Seq([2 for d_240___v1_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])

class TestInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [TestInfo_TestInfo()]
    @classmethod
    def default(cls, ):
        return lambda: TestInfo_TestInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestInfo(self) -> bool:
        return isinstance(self, TestInfo_TestInfo)

class TestInfo_TestInfo(TestInfo, NamedTuple('TestInfo', [])):
    def __dafnystr__(self) -> str:
        return f'TestIntermediateKeyWrapping.TestInfo.TestInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestInfo_TestInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class TestGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial"
    def ctor__(self):
        pass
        pass

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(TestInfo.default()))()
        d_241_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_241_valueOrError0_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestGenerateAndWrapMaterial")))
        if (d_241_valueOrError0_).IsFailure():
            res = (d_241_valueOrError0_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(default__.PLAINTEXT__MAT, default__.WRAPPED__MAT, TestInfo_TestInfo()))
        return res
        return res


class TestUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestIntermediateKeyWrapping.TestUnwrapKeyMaterial"
    def ctor__(self):
        pass
        pass

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(TestInfo.default()))()
        d_242_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_242_valueOrError0_ = Wrappers.default__.Need(((input).wrappedMaterial) == (default__.WRAPPED__MAT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_242_valueOrError0_).IsFailure():
            res = (d_242_valueOrError0_).PropagateFailure()
            return res
        d_243_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_243_valueOrError1_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_243_valueOrError1_).IsFailure():
            res = (d_243_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(default__.PLAINTEXT__MAT, TestInfo_TestInfo()))
        return res
        return res

