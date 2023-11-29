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
import TestUtils

# assert "TestIntermediateKeyWrapping" == __name__
TestIntermediateKeyWrapping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateWrapUnwrapTest():
        d_1644_encCtx_: _dafny.Map
        d_1644_encCtx_ = _dafny.Map({})
        d_1645_keyLen_: int
        d_1645_keyLen_ = ((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_1646_tagLen_: int
        d_1646_tagLen_ = ((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_1647_pdk_: _dafny.Seq
        d_1647_pdk_ = _dafny.Seq([0 for d_1648___v2_ in range(d_1645_keyLen_)])
        d_1649_testGenerateAndWrap_: TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial
        nw74_ = TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial()
        nw74_.ctor__()
        d_1649_testGenerateAndWrap_ = nw74_
        d_1650_intermediateWrapOutput_: Wrappers.Result
        out377_: Wrappers.Result
        out377_ = IntermediateKeyWrapping.default__.IntermediateWrap(d_1649_testGenerateAndWrap_, d_1647_pdk_, (TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE, d_1644_encCtx_)
        d_1650_intermediateWrapOutput_ = out377_
        if not((d_1650_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_1650_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_1645_keyLen_) + (d_1646_tagLen_)) + (len((TestIntermediateKeyWrapping.default__).WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_1650_intermediateWrapOutput_).value).wrappedMaterial)[(d_1645_keyLen_) + (d_1646_tagLen_)::])) == ((TestIntermediateKeyWrapping.default__).WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1651_testUnwrap_: TestIntermediateKeyWrapping.TestUnwrapKeyMaterial
        nw75_ = TestIntermediateKeyWrapping.TestUnwrapKeyMaterial()
        nw75_.ctor__()
        d_1651_testUnwrap_ = nw75_
        d_1652_intermediateUnwrapOutput_: Wrappers.Result
        out378_: Wrappers.Result
        out378_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_1651_testUnwrap_, ((d_1650_intermediateWrapOutput_).value).wrappedMaterial, (TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE, d_1644_encCtx_)
        d_1652_intermediateUnwrapOutput_ = out378_
        if not((d_1652_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_1652_intermediateUnwrapOutput_).value).plaintextDataKey) == (d_1647_pdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_1650_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_1652_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def IntermediateGenerateAndWrapUnwrapTest():
        d_1653_encCtx_: _dafny.Map
        d_1653_encCtx_ = _dafny.Map({})
        d_1654_keyLen_: int
        d_1654_keyLen_ = ((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_1655_tagLen_: int
        d_1655_tagLen_ = ((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_1656_testGenerateAndWrap_: TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial
        nw76_ = TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial()
        nw76_.ctor__()
        d_1656_testGenerateAndWrap_ = nw76_
        d_1657_intermediateWrapOutput_: Wrappers.Result
        out379_: Wrappers.Result
        out379_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(d_1656_testGenerateAndWrap_, (TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE, d_1653_encCtx_)
        d_1657_intermediateWrapOutput_ = out379_
        if not((d_1657_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_1657_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_1654_keyLen_) + (d_1655_tagLen_)) + (len((TestIntermediateKeyWrapping.default__).WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_1657_intermediateWrapOutput_).value).wrappedMaterial)[(d_1654_keyLen_) + (d_1655_tagLen_)::])) == ((TestIntermediateKeyWrapping.default__).WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1658_testUnwrap_: TestIntermediateKeyWrapping.TestUnwrapKeyMaterial
        nw77_ = TestIntermediateKeyWrapping.TestUnwrapKeyMaterial()
        nw77_.ctor__()
        d_1658_testUnwrap_ = nw77_
        d_1659_intermediateUnwrapOutput_: Wrappers.Result
        out380_: Wrappers.Result
        out380_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_1658_testUnwrap_, ((d_1657_intermediateWrapOutput_).value).wrappedMaterial, (TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE, d_1653_encCtx_)
        d_1659_intermediateUnwrapOutput_ = out380_
        if not((d_1659_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_1657_intermediateWrapOutput_).value).plaintextDataKey) == (((d_1659_intermediateUnwrapOutput_).value).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_1657_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_1659_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def TEST__ALG__SUITE(instance):
        return (AlgorithmSuites.default__).DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384
    @_dafny.classproperty
    def PLAINTEXT__MAT(instance):
        return _dafny.Seq([1 for d_1660___v0_ in range(((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])
    @_dafny.classproperty
    def WRAPPED__MAT(instance):
        return _dafny.Seq([2 for d_1661___v1_ in range(((((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])

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
        return isinstance(self, TestIntermediateKeyWrapping.TestInfo_TestInfo)

class TestInfo_TestInfo(TestInfo, NamedTuple('TestInfo', [])):
    def __dafnystr__(self) -> str:
        return f'TestIntermediateKeyWrapping.TestInfo.TestInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestIntermediateKeyWrapping.TestInfo_TestInfo)
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
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(TestIntermediateKeyWrapping.TestInfo.default()))()
        d_1662_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1662_valueOrError0_ = Wrappers.default__.Need(((input).algorithmSuite) == ((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestGenerateAndWrapMaterial")))
        if (d_1662_valueOrError0_).IsFailure():
            res = (d_1662_valueOrError0_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput((TestIntermediateKeyWrapping.default__).PLAINTEXT__MAT, (TestIntermediateKeyWrapping.default__).WRAPPED__MAT, TestIntermediateKeyWrapping.TestInfo_TestInfo()))
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
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(TestIntermediateKeyWrapping.TestInfo.default()))()
        d_1663_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1663_valueOrError0_ = Wrappers.default__.Need(((input).wrappedMaterial) == ((TestIntermediateKeyWrapping.default__).WRAPPED__MAT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_1663_valueOrError0_).IsFailure():
            res = (d_1663_valueOrError0_).PropagateFailure()
            return res
        d_1664_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1664_valueOrError1_ = Wrappers.default__.Need(((input).algorithmSuite) == ((TestIntermediateKeyWrapping.default__).TEST__ALG__SUITE), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_1664_valueOrError1_).IsFailure():
            res = (d_1664_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput((TestIntermediateKeyWrapping.default__).PLAINTEXT__MAT, TestIntermediateKeyWrapping.TestInfo_TestInfo()))
        return res
        return res

