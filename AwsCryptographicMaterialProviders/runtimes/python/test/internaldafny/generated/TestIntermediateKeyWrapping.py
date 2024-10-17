import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestLyingBranchKey as TestLyingBranchKey
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
        d_0_encCtx_: _dafny.Map
        d_0_encCtx_ = _dafny.Map({})
        d_1_keyLen_: int
        d_1_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_2_tagLen_: int
        d_2_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_3_pdk_: _dafny.Seq
        d_3_pdk_ = _dafny.Seq([0 for d_4___v2_ in range(d_1_keyLen_)])
        d_5_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw0_ = TestGenerateAndWrapKeyMaterial()
        nw0_.ctor__()
        d_5_testGenerateAndWrap_ = nw0_
        d_6_intermediateWrapOutput_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = IntermediateKeyWrapping.default__.IntermediateWrap(d_5_testGenerateAndWrap_, d_3_pdk_, default__.TEST__ALG__SUITE, d_0_encCtx_)
        d_6_intermediateWrapOutput_ = out0_
        if not((d_6_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_6_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_1_keyLen_) + (d_2_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(37,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_6_intermediateWrapOutput_).value).wrappedMaterial)[(d_1_keyLen_) + (d_2_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_7_testUnwrap_: TestUnwrapKeyMaterial
        nw1_ = TestUnwrapKeyMaterial()
        nw1_.ctor__()
        d_7_testUnwrap_ = nw1_
        d_8_intermediateUnwrapOutput_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_7_testUnwrap_, ((d_6_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_0_encCtx_)
        d_8_intermediateUnwrapOutput_ = out1_
        if not((d_8_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_8_intermediateUnwrapOutput_).value).plaintextDataKey) == (d_3_pdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_6_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_8_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def IntermediateGenerateAndWrapUnwrapTest():
        d_0_encCtx_: _dafny.Map
        d_0_encCtx_ = _dafny.Map({})
        d_1_keyLen_: int
        d_1_keyLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength
        d_2_tagLen_: int
        d_2_tagLen_ = (((default__.TEST__ALG__SUITE).encrypt).AES__GCM).tagLength
        d_3_testGenerateAndWrap_: TestGenerateAndWrapKeyMaterial
        nw0_ = TestGenerateAndWrapKeyMaterial()
        nw0_.ctor__()
        d_3_testGenerateAndWrap_ = nw0_
        d_4_intermediateWrapOutput_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = IntermediateKeyWrapping.default__.IntermediateGenerateAndWrap(d_3_testGenerateAndWrap_, default__.TEST__ALG__SUITE, d_0_encCtx_)
        d_4_intermediateWrapOutput_ = out0_
        if not((d_4_intermediateWrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_4_intermediateWrapOutput_).value).wrappedMaterial)) == (((d_1_keyLen_) + (d_2_tagLen_)) + (len(default__.WRAPPED__MAT)))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((_dafny.Seq((((d_4_intermediateWrapOutput_).value).wrappedMaterial)[(d_1_keyLen_) + (d_2_tagLen_)::])) == (default__.WRAPPED__MAT)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_testUnwrap_: TestUnwrapKeyMaterial
        nw1_ = TestUnwrapKeyMaterial()
        nw1_.ctor__()
        d_5_testUnwrap_ = nw1_
        d_6_intermediateUnwrapOutput_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = IntermediateKeyWrapping.default__.IntermediateUnwrap(d_5_testUnwrap_, ((d_4_intermediateWrapOutput_).value).wrappedMaterial, default__.TEST__ALG__SUITE, d_0_encCtx_)
        d_6_intermediateUnwrapOutput_ = out1_
        if not((d_6_intermediateUnwrapOutput_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_4_intermediateWrapOutput_).value).plaintextDataKey) == (((d_6_intermediateUnwrapOutput_).value).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_4_intermediateWrapOutput_).value).symmetricSigningKey) == (((d_6_intermediateUnwrapOutput_).value).symmetricSigningKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestIntermediateKeyWrapping.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def TEST__ALG__SUITE(instance):
        return AlgorithmSuites.default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384
    @_dafny.classproperty
    def PLAINTEXT__MAT(instance):
        return _dafny.Seq([1 for d_0___v0_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])
    @_dafny.classproperty
    def WRAPPED__MAT(instance):
        return _dafny.Seq([2 for d_0___v1_ in range((((default__.TEST__ALG__SUITE).encrypt).AES__GCM).keyLength)])

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
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestGenerateAndWrapMaterial")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
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
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(((input).wrappedMaterial) == (default__.WRAPPED__MAT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need(((input).algorithmSuite) == (default__.TEST__ALG__SUITE), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected input on TestUnwrapMaterial")))
        if (d_1_valueOrError1_).IsFailure():
            res = (d_1_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(default__.PLAINTEXT__MAT, TestInfo_TestInfo()))
        return res
        return res

