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
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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
import CmmFromKeyDescription
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
        d_530_result_: Wrappers.Result
        out51_: Wrappers.Result
        out51_ = ((test).cmm).GetEncryptionMaterials((test).input)
        d_530_result_ = out51_
        pat_let_tv0_ = d_530_result_
        pat_let_tv1_ = d_530_result_
        pat_let_tv2_ = d_530_result_
        def lambda52_(source16_):
            if source16_.is_PositiveEncryptKeyringVector:
                d_531___mcc_h0_ = source16_.name
                d_532___mcc_h1_ = source16_.description
                d_533___mcc_h2_ = source16_.encryptionContext
                d_534___mcc_h3_ = source16_.commitmentPolicy
                d_535___mcc_h4_ = source16_.algorithmSuite
                d_536___mcc_h5_ = source16_.maxPlaintextLength
                d_537___mcc_h6_ = source16_.requiredEncryptionContextKeys
                d_538___mcc_h7_ = source16_.encryptDescription
                d_539___mcc_h8_ = source16_.decryptDescription
                d_540___mcc_h9_ = source16_.reproducedEncryptionContext
                return (pat_let_tv0_).is_Success
            elif source16_.is_PositiveEncryptNegativeDecryptKeyringVector:
                d_541___mcc_h10_ = source16_.name
                d_542___mcc_h11_ = source16_.description
                d_543___mcc_h12_ = source16_.encryptionContext
                d_544___mcc_h13_ = source16_.commitmentPolicy
                d_545___mcc_h14_ = source16_.algorithmSuite
                d_546___mcc_h15_ = source16_.maxPlaintextLength
                d_547___mcc_h16_ = source16_.requiredEncryptionContextKeys
                d_548___mcc_h17_ = source16_.decryptErrorDescription
                d_549___mcc_h18_ = source16_.encryptDescription
                d_550___mcc_h19_ = source16_.decryptDescription
                d_551___mcc_h20_ = source16_.reproducedEncryptionContext
                return (pat_let_tv1_).is_Success
            elif True:
                d_552___mcc_h21_ = source16_.name
                d_553___mcc_h22_ = source16_.description
                d_554___mcc_h23_ = source16_.encryptionContext
                d_555___mcc_h24_ = source16_.commitmentPolicy
                d_556___mcc_h25_ = source16_.algorithmSuite
                d_557___mcc_h26_ = source16_.maxPlaintextLength
                d_558___mcc_h27_ = source16_.requiredEncryptionContextKeys
                d_559___mcc_h28_ = source16_.errorDescription
                d_560___mcc_h29_ = source16_.keyDescription
                return not((pat_let_tv2_).is_Success)

        testResult = lambda52_((test).vector)
        materials = (Wrappers.Option_Some(((d_530_result_).value).encryptionMaterials) if (testResult) and ((d_530_result_).is_Success) else Wrappers.Option_None())
        if not(testResult):
            if (((test).vector).is_PositiveEncryptKeyringVector) or (((test).vector).is_PositiveEncryptNegativeDecryptKeyringVector):
                _dafny.print(_dafny.string_of((d_530_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return testResult, materials

    @staticmethod
    def TestDecryptMaterials(test):
        output: bool = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeDecryptKeyringTest else _dafny.Seq("\n"))))
        d_561_result_: Wrappers.Result
        out52_: Wrappers.Result
        out52_ = ((test).cmm).DecryptMaterials((test).input)
        d_561_result_ = out52_
        pat_let_tv3_ = d_561_result_
        pat_let_tv4_ = d_561_result_
        pat_let_tv5_ = test
        pat_let_tv6_ = d_561_result_
        pat_let_tv7_ = test
        pat_let_tv8_ = d_561_result_
        pat_let_tv9_ = test
        pat_let_tv10_ = d_561_result_
        def lambda53_(source17_):
            if source17_.is_PositiveDecryptKeyringTest:
                d_562___mcc_h0_ = source17_.name
                d_563___mcc_h1_ = source17_.algorithmSuite
                d_564___mcc_h2_ = source17_.commitmentPolicy
                d_565___mcc_h3_ = source17_.encryptedDataKeys
                d_566___mcc_h4_ = source17_.encryptionContext
                d_567___mcc_h5_ = source17_.keyDescription
                d_568___mcc_h6_ = source17_.expectedResult
                d_569___mcc_h7_ = source17_.description
                d_570___mcc_h8_ = source17_.reproducedEncryptionContext
                return ((((pat_let_tv3_).is_Success) and (((((pat_let_tv4_).value).decryptionMaterials).plaintextDataKey) == ((((pat_let_tv5_).vector).expectedResult).plaintextDataKey))) and (((((pat_let_tv6_).value).decryptionMaterials).symmetricSigningKey) == ((((pat_let_tv7_).vector).expectedResult).symmetricSigningKey))) and (((((pat_let_tv8_).value).decryptionMaterials).requiredEncryptionContextKeys) == ((((pat_let_tv9_).vector).expectedResult).requiredEncryptionContextKeys))
            elif True:
                d_571___mcc_h9_ = source17_.name
                d_572___mcc_h10_ = source17_.algorithmSuite
                d_573___mcc_h11_ = source17_.commitmentPolicy
                d_574___mcc_h12_ = source17_.encryptedDataKeys
                d_575___mcc_h13_ = source17_.encryptionContext
                d_576___mcc_h14_ = source17_.errorDescription
                d_577___mcc_h15_ = source17_.keyDescription
                d_578___mcc_h16_ = source17_.reproducedEncryptionContext
                d_579___mcc_h17_ = source17_.description
                return not((pat_let_tv10_).is_Success)

        output = lambda53_((test).vector)
        if not(output):
            if (((test).vector).is_PositiveDecryptKeyringTest) and ((d_561_result_).is_Failure):
                _dafny.print(_dafny.string_of((d_561_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return output

    @staticmethod
    def ToEncryptTest(keys, vector):
        output: Wrappers.Result = None
        pat_let_tv11_ = vector
        pat_let_tv12_ = vector
        pat_let_tv13_ = vector
        pat_let_tv14_ = vector
        pat_let_tv15_ = vector
        pat_let_tv16_ = vector
        pat_let_tv17_ = vector
        pat_let_tv18_ = vector
        pat_let_tv19_ = vector
        pat_let_tv20_ = vector
        pat_let_tv21_ = vector
        pat_let_tv22_ = vector
        pat_let_tv23_ = vector
        pat_let_tv24_ = vector
        pat_let_tv25_ = vector
        d_580_input_: software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput
        def lambda54_(source18_):
            if source18_.is_PositiveEncryptKeyringVector:
                d_581___mcc_h0_ = source18_.name
                d_582___mcc_h1_ = source18_.description
                d_583___mcc_h2_ = source18_.encryptionContext
                d_584___mcc_h3_ = source18_.commitmentPolicy
                d_585___mcc_h4_ = source18_.algorithmSuite
                d_586___mcc_h5_ = source18_.maxPlaintextLength
                d_587___mcc_h6_ = source18_.requiredEncryptionContextKeys
                d_588___mcc_h7_ = source18_.encryptDescription
                d_589___mcc_h8_ = source18_.decryptDescription
                d_590___mcc_h9_ = source18_.reproducedEncryptionContext
                return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv11_).encryptionContext, (pat_let_tv12_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv13_).algorithmSuite).id), (pat_let_tv14_).maxPlaintextLength, (pat_let_tv15_).requiredEncryptionContextKeys)
            elif source18_.is_PositiveEncryptNegativeDecryptKeyringVector:
                d_591___mcc_h10_ = source18_.name
                d_592___mcc_h11_ = source18_.description
                d_593___mcc_h12_ = source18_.encryptionContext
                d_594___mcc_h13_ = source18_.commitmentPolicy
                d_595___mcc_h14_ = source18_.algorithmSuite
                d_596___mcc_h15_ = source18_.maxPlaintextLength
                d_597___mcc_h16_ = source18_.requiredEncryptionContextKeys
                d_598___mcc_h17_ = source18_.decryptErrorDescription
                d_599___mcc_h18_ = source18_.encryptDescription
                d_600___mcc_h19_ = source18_.decryptDescription
                d_601___mcc_h20_ = source18_.reproducedEncryptionContext
                return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv16_).encryptionContext, (pat_let_tv17_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv18_).algorithmSuite).id), (pat_let_tv19_).maxPlaintextLength, (pat_let_tv20_).requiredEncryptionContextKeys)
            elif True:
                d_602___mcc_h21_ = source18_.name
                d_603___mcc_h22_ = source18_.description
                d_604___mcc_h23_ = source18_.encryptionContext
                d_605___mcc_h24_ = source18_.commitmentPolicy
                d_606___mcc_h25_ = source18_.algorithmSuite
                d_607___mcc_h26_ = source18_.maxPlaintextLength
                d_608___mcc_h27_ = source18_.requiredEncryptionContextKeys
                d_609___mcc_h28_ = source18_.errorDescription
                d_610___mcc_h29_ = source18_.keyDescription
                return software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv21_).encryptionContext, (pat_let_tv22_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv23_).algorithmSuite).id), (pat_let_tv24_).maxPlaintextLength, (pat_let_tv25_).requiredEncryptionContextKeys)

        d_580_input_ = lambda54_(vector)
        d_611_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_612_valueOrError0_: Wrappers.Result = None
        out53_: Wrappers.Result
        out53_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_612_valueOrError0_ = out53_
        if not(not((d_612_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(133,12): " + _dafny.string_of(d_612_valueOrError0_))
        d_611_mpl_ = (d_612_valueOrError0_).Extract()
        d_613_cmm_k_: Wrappers.Result
        out54_: Wrappers.Result
        out54_ = (keys).CreateWrappedTestVectorCmm(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorCmmInput_TestVectorCmmInput(((vector).encryptDescription if (vector).is_PositiveEncryptKeyringVector else ((vector).encryptDescription if (vector).is_PositiveEncryptNegativeDecryptKeyringVector else (vector).keyDescription)), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.CmmOperation_ENCRYPT()))
        d_613_cmm_k_ = out54_
        d_614_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_615_valueOrError1_: Wrappers.Result = None
        def lambda55_(d_616_e_):
            def iife20_(_pat_let7_0):
                def iife21_(d_617___v78_):
                    return _dafny.Seq("Cmm failure")
                return iife21_(_pat_let7_0)
            return iife20_(default__.printErr(d_616_e_))

        d_615_valueOrError1_ = (d_613_cmm_k_).MapFailure(lambda55_)
        if (d_615_valueOrError1_).IsFailure():
            output = (d_615_valueOrError1_).PropagateFailure()
            return output
        d_614_cmm_ = (d_615_valueOrError1_).Extract()
        output = Wrappers.Result_Success(EncryptTest_EncryptTest(d_580_input_, d_614_cmm_, vector))
        return output
        return output

    @staticmethod
    def EncryptTestToDecryptVector(test, materials):
        d_618_keysToRemove_ = Seq.default__.ToSet((((test).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))
        source19_ = (test).vector
        if source19_.is_PositiveEncryptKeyringVector:
            d_619___mcc_h0_ = source19_.name
            d_620___mcc_h1_ = source19_.description
            d_621___mcc_h2_ = source19_.encryptionContext
            d_622___mcc_h3_ = source19_.commitmentPolicy
            d_623___mcc_h4_ = source19_.algorithmSuite
            d_624___mcc_h5_ = source19_.maxPlaintextLength
            d_625___mcc_h6_ = source19_.requiredEncryptionContextKeys
            d_626___mcc_h7_ = source19_.encryptDescription
            d_627___mcc_h8_ = source19_.decryptDescription
            d_628___mcc_h9_ = source19_.reproducedEncryptionContext
            return DecryptTestVector_PositiveDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), ((test).vector).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, ((materials).encryptionContext) - (d_618_keysToRemove_), ((test).vector).decryptDescription, DecryptResult_DecryptResult((materials).plaintextDataKey, (Wrappers.Option_Some((((materials).symmetricSigningKeys).value)[0]) if (((materials).symmetricSigningKeys).is_Some) and ((0) < (len(((materials).symmetricSigningKeys).value))) else Wrappers.Option_None()), (((test).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))), (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()), ((test).vector).reproducedEncryptionContext)
        elif True:
            d_629___mcc_h10_ = source19_.name
            d_630___mcc_h11_ = source19_.description
            d_631___mcc_h12_ = source19_.encryptionContext
            d_632___mcc_h13_ = source19_.commitmentPolicy
            d_633___mcc_h14_ = source19_.algorithmSuite
            d_634___mcc_h15_ = source19_.maxPlaintextLength
            d_635___mcc_h16_ = source19_.requiredEncryptionContextKeys
            d_636___mcc_h17_ = source19_.decryptErrorDescription
            d_637___mcc_h18_ = source19_.encryptDescription
            d_638___mcc_h19_ = source19_.decryptDescription
            d_639___mcc_h20_ = source19_.reproducedEncryptionContext
            return DecryptTestVector_NegativeDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), ((test).vector).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (((test).vector).encryptionContext) - (d_618_keysToRemove_), ((test).vector).decryptErrorDescription, ((test).vector).decryptDescription, ((test).vector).reproducedEncryptionContext, (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()))

    @staticmethod
    def DecryptVectorToDecryptTest(keys, vector):
        output: Wrappers.Result = None
        d_640_input_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput
        d_640_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput(((vector).algorithmSuite).id, (vector).commitmentPolicy, (vector).encryptedDataKeys, (vector).encryptionContext, (vector).reproducedEncryptionContext)
        d_641_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_642_valueOrError0_: Wrappers.Result = None
        out55_: Wrappers.Result
        out55_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_642_valueOrError0_ = out55_
        if not(not((d_642_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(218,12): " + _dafny.string_of(d_642_valueOrError0_))
        d_641_mpl_ = (d_642_valueOrError0_).Extract()
        d_643_cmm_k_: Wrappers.Result
        out56_: Wrappers.Result
        out56_ = (keys).CreateWrappedTestVectorCmm(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.TestVectorCmmInput_TestVectorCmmInput((vector).keyDescription, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.CmmOperation_DECRYPT()))
        d_643_cmm_k_ = out56_
        d_644_cmm_: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsManager
        d_645_valueOrError1_: Wrappers.Result = None
        d_645_valueOrError1_ = (d_643_cmm_k_).MapFailure(default__.ErrorToString)
        if (d_645_valueOrError1_).IsFailure():
            output = (d_645_valueOrError1_).PropagateFailure()
            return output
        d_644_cmm_ = (d_645_valueOrError1_).Extract()
        output = Wrappers.Result_Success(DecryptTest_DecryptTest(d_640_input_, d_644_cmm_, vector))
        return output
        return output

    @staticmethod
    def ErrorToString(e):
        source20_ = e
        if source20_.is_KeyVectorException:
            d_646___mcc_h0_ = source20_.message
            d_647_message_ = d_646___mcc_h0_
            return d_647_message_
        elif source20_.is_AwsCryptographyMaterialProviders:
            d_648___mcc_h2_ = source20_.AwsCryptographyMaterialProviders
            d_649_mplError_ = d_648___mcc_h2_
            source21_ = d_649_mplError_
            if source21_.is_AwsCryptographicMaterialProvidersException:
                d_650___mcc_h12_ = source21_.message
                d_651_message_ = d_650___mcc_h12_
                return d_651_message_
            elif source21_.is_EntryAlreadyExists:
                d_652___mcc_h14_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_EntryDoesNotExist:
                d_653___mcc_h16_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfo:
                d_654___mcc_h18_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfoOnDecrypt:
                d_655___mcc_h20_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfoOnEncrypt:
                d_656___mcc_h22_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidDecryptionMaterials:
                d_657___mcc_h24_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidDecryptionMaterialsTransition:
                d_658___mcc_h26_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidEncryptionMaterials:
                d_659___mcc_h28_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidEncryptionMaterialsTransition:
                d_660___mcc_h30_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_AwsCryptographyKeyStore:
                d_661___mcc_h32_ = source21_.AwsCryptographyKeyStore
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_AwsCryptographyPrimitives:
                d_662___mcc_h34_ = source21_.AwsCryptographyPrimitives
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_ComAmazonawsDynamodb:
                d_663___mcc_h36_ = source21_.ComAmazonawsDynamodb
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_ComAmazonawsKms:
                d_664___mcc_h38_ = source21_.ComAmazonawsKms
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_CollectionOfErrors:
                d_665___mcc_h40_ = source21_.list
                d_666___mcc_h41_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif True:
                d_667___mcc_h44_ = source21_.obj
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
        elif source20_.is_ComAmazonawsKms:
            d_668___mcc_h4_ = source20_.ComAmazonawsKms
            return _dafny.Seq("Unmapped KeyVectorException")
        elif source20_.is_CollectionOfErrors:
            d_669___mcc_h6_ = source20_.list
            d_670___mcc_h7_ = source20_.message
            return _dafny.Seq("Unmapped KeyVectorException")
        elif True:
            d_671___mcc_h10_ = source20_.obj
            return _dafny.Seq("Unmapped KeyVectorException")

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
        return lambda: EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq({}), Wrappers.Option.default()(), _dafny.Map({}), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription.default()(), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveEncryptKeyringVector(self) -> bool:
        return isinstance(self, EncryptTestVector_PositiveEncryptKeyringVector)
    @property
    def is_PositiveEncryptNegativeDecryptKeyringVector(self) -> bool:
        return isinstance(self, EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)
    @property
    def is_NegativeEncryptKeyringVector(self) -> bool:
        return isinstance(self, EncryptTestVector_NegativeEncryptKeyringVector)

class EncryptTestVector_PositiveEncryptKeyringVector(EncryptTestVector, NamedTuple('PositiveEncryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('encryptDescription', Any), ('decryptDescription', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.PositiveEncryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.encryptDescription)}, {_dafny.string_of(self.decryptDescription)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptTestVector_PositiveEncryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.encryptDescription == __o.encryptDescription and self.decryptDescription == __o.decryptDescription and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(EncryptTestVector, NamedTuple('PositiveEncryptNegativeDecryptKeyringVector', [('name', Any), ('description', Any), ('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuite', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any), ('decryptErrorDescription', Any), ('encryptDescription', Any), ('decryptDescription', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestVectors.EncryptTestVector.PositiveEncryptNegativeDecryptKeyringVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.description)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.decryptErrorDescription)}, {_dafny.string_of(self.encryptDescription)}, {_dafny.string_of(self.decryptDescription)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector) and self.name == __o.name and self.description == __o.description and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuite == __o.algorithmSuite and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.decryptErrorDescription == __o.decryptErrorDescription and self.encryptDescription == __o.encryptDescription and self.decryptDescription == __o.decryptDescription and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
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
        return lambda: DecryptTestVector_PositiveDecryptKeyringTest(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy.default()(), _dafny.Seq({}), _dafny.Map({}), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription.default()(), DecryptResult.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
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

