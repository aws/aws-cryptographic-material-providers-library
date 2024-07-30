import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils

# Module: TestIntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateWrapUnwrapTest():
        d_410_encCtx_: _dafny.Map
        d_410_encCtx_ = _dafny.Map({})
        d_411_keyLen_: int
        d_411_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_412_tagLen_: int
        d_412_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_413_pdk_: _dafny.Seq
        d_413_pdk_ = _dafny.Seq([0 for d_414___v2_ in range(d_411_keyLen_)])
        d_415_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw0_ = TestGenerateAndWrapKeyMaterial()
        nw0_.ctor__()
        d_415_testGenerateAndWrap_ = nw0_
        d_416_intermediateWrapOutput_: Wrappers.Result
        out145_: Wrappers.Result
        out145_ = IntermediateKeyWrapping.default__.IntermediateWrap(d_415_testGenerateAndWrap_, d_413_pdk_, default__.TEST__ALG__SUITE, d_410_encCtx_)
        d_416_intermediateWrapOutput_ = out145_
        if not((d_416_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_416_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_411_keyLen_) + (d_412_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_416_intermediateWrapOutput_).value).wrappedMaterial)[(d_411_keyLen_) + (d_412_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_417_testUnwrap_: TestUnwrapKeyMaterial
        nw1_ = TestUnwrapKeyMaterial()
        nw1_.ctor__()
        d_417_testUnwrap_ = nw1_
        d_418_intermediateUnwrapOutput_: Wrappers.Result
        out146_: Wrappers.Result
        out146_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_417_testUnwrap_, ((d_416_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_410_encCtx_)
        d_418_intermediateUnwrapOutput_ = out146_
        if not((d_418_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_418_intermediateUnwrapOutput_).value).plaintextDataKey) == (d_413_pdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_416_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_418_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def IntermediateGenerateAndWrapUnwrapTest():
        d_419_encCtx_: _dafny.Map
        d_419_encCtx_ = _dafny.Map({})
        d_420_keyLen_: int
        d_420_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_421_tagLen_: int
        d_421_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_422_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw2_ = TestGenerateAndWrapKeyMaterial()
        nw2_.ctor__()
        d_422_testGenerateAndWrap_ = nw2_
        d_423_intermediateWrapOutput_: Wrappers.Result
        out147_: Wrappers.Result
        out147_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(d_422_testGenerateAndWrap_, default__.TEST__ALG__SUITE, d_419_encCtx_)
        d_423_intermediateWrapOutput_ = out147_
        if not((d_423_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_423_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_420_keyLen_) + (d_421_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_423_intermediateWrapOutput_).value).wrappedMaterial)[(d_420_keyLen_) + (d_421_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_424_testUnwrap_: TestUnwrapKeyMaterial
        nw3_ = TestUnwrapKeyMaterial()
        nw3_.ctor__()
        d_424_testUnwrap_ = nw3_
        d_425_intermediateUnwrapOutput_: Wrappers.Result
        out148_: Wrappers.Result
        out148_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_424_testUnwrap_, ((d_423_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_419_encCtx_)
        d_425_intermediateUnwrapOutput_ = out148_
        if not((d_425_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_423_intermediateWrapOutput_).value).plaintextDataKey) == (((d_425_intermediateUnwrapOutput_).value).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_423_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_425_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def TEST__ALG__SUITE(instance):
        return AlgorithmSuites.default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384
    @_dafny.classproperty
    def PLAINTEXT__MAT(instance):
        return _dafny.Seq([1 for d_426___v0_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])
    @_dafny.classproperty
    def WRAPPED__MAT(instance):
        return _dafny.Seq([2 for d_427___v1_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])

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
        d_428_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_428_valueOrError0_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestGenerateAndWrapMaterial")))
        if (d_428_valueOrError0_).IsFailure():
            res = (d_428_valueOrError0_).PropagateFailure()
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
        d_429_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_429_valueOrError0_ = Wrappers.default__.Need(((input).wrappedMaterial) == (default__.WRAPPED__MAT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_429_valueOrError0_).IsFailure():
            res = (d_429_valueOrError0_).PropagateFailure()
            return res
        d_430_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_430_valueOrError1_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_430_valueOrError1_).IsFailure():
            res = (d_430_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(default__.PLAINTEXT__MAT, TestInfo_TestInfo()))
        return res
        return res

