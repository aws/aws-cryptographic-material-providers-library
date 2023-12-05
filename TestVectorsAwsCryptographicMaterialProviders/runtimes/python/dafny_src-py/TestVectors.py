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
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny

# Module: TestVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetEncryptionMaterials(test):
        testResult: bool = False
        materials: Wrappers.Option = Wrappers.Option.default()()
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeEncryptKeyringVector else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        d_473_result_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = ((test).cmm).GetEncryptionMaterials((test).input)
        d_473_result_ = out70_
        pat_let_tv0_ = d_473_result_
        pat_let_tv1_ = d_473_result_
        def lambda30_(source15_):
            if source15_.is_PositiveEncryptKeyringVector:
                d_474___mcc_h0_ = source15_.name
                d_475___mcc_h1_ = source15_.description
                d_476___mcc_h2_ = source15_.encryptionContext
                d_477___mcc_h3_ = source15_.commitmentPolicy
                d_478___mcc_h4_ = source15_.algorithmSuite
                d_479___mcc_h5_ = source15_.maxPlaintextLength
                d_480___mcc_h6_ = source15_.requiredEncryptionContextKeys
                d_481___mcc_h7_ = source15_.encryptDescription
                d_482___mcc_h8_ = source15_.decryptDescription
                return (pat_let_tv0_).is_Success
            elif True:
                d_483___mcc_h9_ = source15_.name
                d_484___mcc_h10_ = source15_.description
                d_485___mcc_h11_ = source15_.encryptionContext
                d_486___mcc_h12_ = source15_.commitmentPolicy
                d_487___mcc_h13_ = source15_.algorithmSuite
                d_488___mcc_h14_ = source15_.maxPlaintextLength
                d_489___mcc_h15_ = source15_.requiredEncryptionContextKeys
                d_490___mcc_h16_ = source15_.errorDescription
                d_491___mcc_h17_ = source15_.keyDescription
                return not((pat_let_tv1_).is_Success)

        testResult = lambda30_((test).vector)
        materials = (Wrappers.Option_Some(((d_473_result_).value).encryptionMaterials) if (((test).vector).is_PositiveEncryptKeyringVector) and ((d_473_result_).is_Success) else Wrappers.Option_None())
        if not(testResult):
            if ((test).vector).is_PositiveEncryptKeyringVector:
                _dafny.print(_dafny.string_of((d_473_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return testResult, materials

    @staticmethod
    def TestDecryptMaterials(test):
        output: bool = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeDecryptKeyringTest else _dafny.Seq("\n"))))
        d_492_result_: Wrappers.Result
        out71_: Wrappers.Result
        out71_ = ((test).cmm).DecryptMaterials((test).input)
        d_492_result_ = out71_
        pat_let_tv2_ = d_492_result_
        pat_let_tv3_ = d_492_result_
        pat_let_tv4_ = test
        pat_let_tv5_ = d_492_result_
        pat_let_tv6_ = test
        pat_let_tv7_ = d_492_result_
        pat_let_tv8_ = test
        pat_let_tv9_ = d_492_result_
        def lambda31_(source16_):
            if source16_.is_PositiveDecryptKeyringTest:
                d_493___mcc_h0_ = source16_.name
                d_494___mcc_h1_ = source16_.algorithmSuite
                d_495___mcc_h2_ = source16_.commitmentPolicy
                d_496___mcc_h3_ = source16_.encryptedDataKeys
                d_497___mcc_h4_ = source16_.encryptionContext
                d_498___mcc_h5_ = source16_.keyDescription
                d_499___mcc_h6_ = source16_.expectedResult
                d_500___mcc_h7_ = source16_.description
                d_501___mcc_h8_ = source16_.reproducedEncryptionContext
                return ((((pat_let_tv2_).is_Success) and (((((pat_let_tv3_).value).decryptionMaterials).plaintextDataKey) == ((((pat_let_tv4_).vector).expectedResult).plaintextDataKey))) and (((((pat_let_tv5_).value).decryptionMaterials).symmetricSigningKey) == ((((pat_let_tv6_).vector).expectedResult).symmetricSigningKey))) and (((((pat_let_tv7_).value).decryptionMaterials).requiredEncryptionContextKeys) == ((((pat_let_tv8_).vector).expectedResult).requiredEncryptionContextKeys))
            elif True:
                d_502___mcc_h9_ = source16_.name
                d_503___mcc_h10_ = source16_.algorithmSuite
                d_504___mcc_h11_ = source16_.commitmentPolicy
                d_505___mcc_h12_ = source16_.encryptedDataKeys
                d_506___mcc_h13_ = source16_.encryptionContext
                d_507___mcc_h14_ = source16_.errorDescription
                d_508___mcc_h15_ = source16_.keyDescription
                d_509___mcc_h16_ = source16_.reproducedEncryptionContext
                d_510___mcc_h17_ = source16_.description
                return not((pat_let_tv9_).is_Success)

        output = lambda31_((test).vector)
        if not(output):
            if (((test).vector).is_PositiveDecryptKeyringTest) and ((d_492_result_).is_Failure):
                _dafny.print(_dafny.string_of((d_492_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return output

    @staticmethod
    def ToEncryptTest(keys, vector):
        output: Wrappers.Result = None
        d_511_input_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput
        def lambda32_(source17_):
            if source17_.is_PositiveEncryptKeyringVector:
                d_512___mcc_h0_ = source17_.name
                d_513___mcc_h1_ = source17_.description
                d_514___mcc_h2_ = source17_.encryptionContext
                d_515___mcc_h3_ = source17_.commitmentPolicy
                d_516___mcc_h4_ = source17_.algorithmSuite
                d_517___mcc_h5_ = source17_.maxPlaintextLength
                d_518___mcc_h6_ = source17_.requiredEncryptionContextKeys
                d_519___mcc_h7_ = source17_.encryptDescription
                d_520___mcc_h8_ = source17_.decryptDescription
                d_521_requiredEncryptionContextKeys_ = d_518___mcc_h6_
                d_522_maxPlaintextLength_ = d_517___mcc_h5_
                d_523_algorithmSuite_ = d_516___mcc_h4_
                d_524_commitmentPolicy_ = d_515___mcc_h3_
                d_525_encryptionContext_ = d_514___mcc_h2_
                return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(d_525_encryptionContext_, d_524_commitmentPolicy_, Wrappers.Option_Some((d_523_algorithmSuite_).id), d_522_maxPlaintextLength_, d_521_requiredEncryptionContextKeys_)
            elif True:
                d_526___mcc_h9_ = source17_.name
                d_527___mcc_h10_ = source17_.description
                d_528___mcc_h11_ = source17_.encryptionContext
                d_529___mcc_h12_ = source17_.commitmentPolicy
                d_530___mcc_h13_ = source17_.algorithmSuite
                d_531___mcc_h14_ = source17_.maxPlaintextLength
                d_532___mcc_h15_ = source17_.requiredEncryptionContextKeys
                d_533___mcc_h16_ = source17_.errorDescription
                d_534___mcc_h17_ = source17_.keyDescription
                d_535_requiredEncryptionContextKeys_ = d_532___mcc_h15_
                d_536_maxPlaintextLength_ = d_531___mcc_h14_
                d_537_algorithmSuite_ = d_530___mcc_h13_
                d_538_commitmentPolicy_ = d_529___mcc_h12_
                d_539_encryptionContext_ = d_528___mcc_h11_
                return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(d_539_encryptionContext_, d_538_commitmentPolicy_, Wrappers.Option_Some((d_537_algorithmSuite_).id), d_536_maxPlaintextLength_, d_535_requiredEncryptionContextKeys_)

        d_511_input_ = lambda32_(vector)
        d_540_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_541_valueOrError0_: Wrappers.Result = None
        out72_: Wrappers.Result
        out72_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_541_valueOrError0_ = out72_
        if not(not((d_541_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(131,12): " + _dafny.string_of(d_541_valueOrError0_))
        d_540_mpl_ = (d_541_valueOrError0_).Extract()
        d_542_maybeKeyring_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (keys).CreateWappedTestVectorKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput_TestVectorKeyringInput(((vector).encryptDescription if (vector).is_PositiveEncryptKeyringVector else (vector).keyDescription)))
        d_542_maybeKeyring_ = out73_
        d_543_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_544_valueOrError1_: Wrappers.Result = None
        def lambda33_(d_545_e_):
            def iife7_(_pat_let1_0):
                def iife8_(d_546___v44_):
                    return _dafny.Seq("Keyring failure")
                return iife8_(_pat_let1_0)
            return iife7_(default__.printErr(d_545_e_))

        d_544_valueOrError1_ = (d_542_maybeKeyring_).MapFailure(lambda33_)
        if (d_544_valueOrError1_).IsFailure():
            output = (d_544_valueOrError1_).PropagateFailure()
            return output
        d_543_keyring_ = (d_544_valueOrError1_).Extract()
        d_547_maybeCmm_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = (d_540_mpl_).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_543_keyring_))
        d_547_maybeCmm_ = out74_
        d_548_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_549_valueOrError2_: Wrappers.Result = None
        def lambda34_(d_550_e_):
            return _dafny.Seq("CMM failure")

        d_549_valueOrError2_ = (d_547_maybeCmm_).MapFailure(lambda34_)
        if (d_549_valueOrError2_).IsFailure():
            output = (d_549_valueOrError2_).PropagateFailure()
            return output
        d_548_cmm_ = (d_549_valueOrError2_).Extract()
        output = Wrappers.Result_Success(EncryptTest_EncryptTest(d_511_input_, d_548_cmm_, vector))
        return output
        return output

    @staticmethod
    def ToDecryptTest(keys, test, materials):
        output: Wrappers.Result = None
        d_551_reproducedEncryptionContext_: Wrappers.Option
        d_551_reproducedEncryptionContext_ = Wrappers.Option_None()
        d_552_input_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput
        d_552_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput(((materials).algorithmSuite).id, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (materials).encryptionContext, d_551_reproducedEncryptionContext_)
        d_553_vector_: DecryptTestVector
        d_553_vector_ = DecryptTestVector_PositiveDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), (materials).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (materials).encryptionContext, ((test).vector).decryptDescription, DecryptResult_DecryptResult((materials).plaintextDataKey, (Wrappers.Option_Some((((materials).symmetricSigningKeys).value)[0]) if (((materials).symmetricSigningKeys).is_Some) and ((0) < (len(((materials).symmetricSigningKeys).value))) else Wrappers.Option_None()), (materials).requiredEncryptionContextKeys), (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()), d_551_reproducedEncryptionContext_)
        d_554_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_555_valueOrError0_: Wrappers.Result = None
        out75_: Wrappers.Result
        out75_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_555_valueOrError0_ = out75_
        if not(not((d_555_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(196,12): " + _dafny.string_of(d_555_valueOrError0_))
        d_554_mpl_ = (d_555_valueOrError0_).Extract()
        d_556_maybeKeyring_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = (keys).CreateWappedTestVectorKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput_TestVectorKeyringInput((d_553_vector_).keyDescription))
        d_556_maybeKeyring_ = out76_
        d_557_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_558_valueOrError1_: Wrappers.Result = None
        def lambda35_(d_559_e_):
            def iife9_(_pat_let2_0):
                def iife10_(d_560___v45_):
                    return _dafny.Seq("Keyring failure")
                return iife10_(_pat_let2_0)
            return iife9_(default__.printErr(d_559_e_))

        d_558_valueOrError1_ = (d_556_maybeKeyring_).MapFailure(lambda35_)
        if (d_558_valueOrError1_).IsFailure():
            output = (d_558_valueOrError1_).PropagateFailure()
            return output
        d_557_keyring_ = (d_558_valueOrError1_).Extract()
        d_561_maybeCmm_: Wrappers.Result
        out77_: Wrappers.Result
        out77_ = (d_554_mpl_).CreateDefaultCryptographicMaterialsManager(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_557_keyring_))
        d_561_maybeCmm_ = out77_
        d_562_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_563_valueOrError2_: Wrappers.Result = None
        def lambda36_(d_564_e_):
            return _dafny.Seq("CMM failure")

        d_563_valueOrError2_ = (d_561_maybeCmm_).MapFailure(lambda36_)
        if (d_563_valueOrError2_).IsFailure():
            output = (d_563_valueOrError2_).PropagateFailure()
            return output
        d_562_cmm_ = (d_563_valueOrError2_).Extract()
        output = Wrappers.Result_Success(DecryptTest_DecryptTest(d_552_input_, d_562_cmm_, d_553_vector_))
        return output
        return output

    @staticmethod
    def printErr(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_


class EncryptTest:
    @classmethod
    def default(cls, ):
        return lambda: EncryptTest_EncryptTest(software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput.default()(), None, EncryptTestVector.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptTest(self) -> bool:
        return isinstance(self, EncryptTest_EncryptTest)

class EncryptTest_EncryptTest(EncryptTest, NamedTuple('EncryptTest', [('input', Any), ('cmm', Any), ('vector', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTest.EncryptTest({_dafny.string_of(self.input)}, {_dafny.string_of(self.cmm)}, {_dafny.string_of(self.vector)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptTest_EncryptTest) and self.input == __o.input and self.cmm == __o.cmm and self.vector == __o.vector
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptTest:
    @classmethod
    def default(cls, ):
        return lambda: DecryptTest_DecryptTest(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput.default()(), None, DecryptTestVector.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptTest(self) -> bool:
        return isinstance(self, DecryptTest_DecryptTest)

class DecryptTest_DecryptTest(DecryptTest, NamedTuple('DecryptTest', [('input', Any), ('cmm', Any), ('vector', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTest.DecryptTest({_dafny.string_of(self.input)}, {_dafny.string_of(self.cmm)}, {_dafny.string_of(self.vector)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptTest_DecryptTest) and self.input == __o.input and self.cmm == __o.cmm and self.vector == __o.vector
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptTestVector:
    @classmethod
    def default(cls, ):
        return lambda: EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq({}), Wrappers.Option.default()(), _dafny.Map({}), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.default()(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveEncryptKeyringVector(self) -> bool:
        return isinstance(self, EncryptTestVector_PositiveEncryptKeyringVector)
    @property
    def is_NegativeEncryptKeyringVector(self) -> bool:
        return isinstance(self, EncryptTestVector_NegativeEncryptKeyringVector)

class EncryptTestVector_PositiveEncryptKeyringVector(EncryptTestVector, NamedTuple('PositiveEncryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('encryptDescription', Any), ('decryptDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.PositiveEncryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.encryptDescription)}, {_dafny.string_of(self.decryptDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptTestVector_PositiveEncryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.encryptDescription == __o.encryptDescription and self.decryptDescription == __o.decryptDescription
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptTestVector_NegativeEncryptKeyringVector(EncryptTestVector, NamedTuple('NegativeEncryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('errorDescription', Any), ('keyDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.NegativeEncryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.errorDescription)}, {_dafny.string_of(self.keyDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptTestVector_NegativeEncryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.errorDescription == __o.errorDescription and self.keyDescription == __o.keyDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptTestVector:
    @classmethod
    def default(cls, ):
        return lambda: DecryptTestVector_PositiveDecryptKeyringTest(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy.default()(), _dafny.Seq({}), _dafny.Map({}), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.default()(), DecryptResult.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveDecryptKeyringTest(self) -> bool:
        return isinstance(self, DecryptTestVector_PositiveDecryptKeyringTest)
    @property
    def is_NegativeDecryptKeyringTest(self) -> bool:
        return isinstance(self, DecryptTestVector_NegativeDecryptKeyringTest)

class DecryptTestVector_PositiveDecryptKeyringTest(DecryptTestVector, NamedTuple('PositiveDecryptKeyringTest', [('name', Any), ('algorithmSuite', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('keyDescription', Any), ('expectedResult', Any), ('description', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTestVector.PositiveDecryptKeyringTest({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.expectedResult)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptTestVector_PositiveDecryptKeyringTest) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.keyDescription == __o.keyDescription and self.expectedResult == __o.expectedResult and self.description == __o.description and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()

class DecryptTestVector_NegativeDecryptKeyringTest(DecryptTestVector, NamedTuple('NegativeDecryptKeyringTest', [('name', Any), ('algorithmSuite', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('errorDescription', Any), ('keyDescription', Any), ('reproducedEncryptionContext', Any), ('description', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptTestVector.NegativeDecryptKeyringTest({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.errorDescription)}, {_dafny.string_of(self.keyDescription)}, {_dafny.string_of(self.reproducedEncryptionContext)}, {_dafny.string_of(self.description)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptTestVector_NegativeDecryptKeyringTest) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.errorDescription == __o.errorDescription and self.keyDescription == __o.keyDescription and self.reproducedEncryptionContext == __o.reproducedEncryptionContext and self.description == __o.description
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptResult:
    @classmethod
    def default(cls, ):
        return lambda: DecryptResult_DecryptResult(Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptResult(self) -> bool:
        return isinstance(self, DecryptResult_DecryptResult)

class DecryptResult_DecryptResult(DecryptResult, NamedTuple('DecryptResult', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.DecryptResult.DecryptResult({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptResult_DecryptResult) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()

