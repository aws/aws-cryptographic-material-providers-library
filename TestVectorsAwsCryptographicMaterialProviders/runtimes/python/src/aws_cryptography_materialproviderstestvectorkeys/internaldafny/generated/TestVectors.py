import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import standard_library.internaldafny.generated.UUID as UUID
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
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyVectors as KeyVectors

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestVectors

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
        d_532_result_: Wrappers.Result
        out51_: Wrappers.Result
        out51_ = ((test).cmm).GetEncryptionMaterials((test).input)
        d_532_result_ = out51_
        pat_let_tv0_ = d_532_result_
        pat_let_tv1_ = d_532_result_
        pat_let_tv2_ = d_532_result_
        def lambda52_(source16_):
            if source16_.is_PositiveEncryptKeyringVector:
                d_533___mcc_h0_ = source16_.name
                d_534___mcc_h1_ = source16_.description
                d_535___mcc_h2_ = source16_.encryptionContext
                d_536___mcc_h3_ = source16_.commitmentPolicy
                d_537___mcc_h4_ = source16_.algorithmSuite
                d_538___mcc_h5_ = source16_.maxPlaintextLength
                d_539___mcc_h6_ = source16_.requiredEncryptionContextKeys
                d_540___mcc_h7_ = source16_.encryptDescription
                d_541___mcc_h8_ = source16_.decryptDescription
                d_542___mcc_h9_ = source16_.reproducedEncryptionContext
                return (pat_let_tv0_).is_Success
            elif source16_.is_PositiveEncryptNegativeDecryptKeyringVector:
                d_543___mcc_h10_ = source16_.name
                d_544___mcc_h11_ = source16_.description
                d_545___mcc_h12_ = source16_.encryptionContext
                d_546___mcc_h13_ = source16_.commitmentPolicy
                d_547___mcc_h14_ = source16_.algorithmSuite
                d_548___mcc_h15_ = source16_.maxPlaintextLength
                d_549___mcc_h16_ = source16_.requiredEncryptionContextKeys
                d_550___mcc_h17_ = source16_.decryptErrorDescription
                d_551___mcc_h18_ = source16_.encryptDescription
                d_552___mcc_h19_ = source16_.decryptDescription
                d_553___mcc_h20_ = source16_.reproducedEncryptionContext
                return (pat_let_tv1_).is_Success
            elif True:
                d_554___mcc_h21_ = source16_.name
                d_555___mcc_h22_ = source16_.description
                d_556___mcc_h23_ = source16_.encryptionContext
                d_557___mcc_h24_ = source16_.commitmentPolicy
                d_558___mcc_h25_ = source16_.algorithmSuite
                d_559___mcc_h26_ = source16_.maxPlaintextLength
                d_560___mcc_h27_ = source16_.requiredEncryptionContextKeys
                d_561___mcc_h28_ = source16_.errorDescription
                d_562___mcc_h29_ = source16_.keyDescription
                return not((pat_let_tv2_).is_Success)

        testResult = lambda52_((test).vector)
        materials = (Wrappers.Option_Some(((d_532_result_).value).encryptionMaterials) if (testResult) and ((d_532_result_).is_Success) else Wrappers.Option_None())
        if not(testResult):
            if (((test).vector).is_PositiveEncryptKeyringVector) or (((test).vector).is_PositiveEncryptNegativeDecryptKeyringVector):
                _dafny.print(_dafny.string_of((d_532_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return testResult, materials

    @staticmethod
    def TestDecryptMaterials(test):
        output: bool = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeDecryptKeyringTest else _dafny.Seq("\n"))))
        d_563_result_: Wrappers.Result
        out52_: Wrappers.Result
        out52_ = ((test).cmm).DecryptMaterials((test).input)
        d_563_result_ = out52_
        pat_let_tv3_ = d_563_result_
        pat_let_tv4_ = d_563_result_
        pat_let_tv5_ = test
        pat_let_tv6_ = d_563_result_
        pat_let_tv7_ = test
        pat_let_tv8_ = d_563_result_
        pat_let_tv9_ = test
        pat_let_tv10_ = d_563_result_
        def lambda53_(source17_):
            if source17_.is_PositiveDecryptKeyringTest:
                d_564___mcc_h0_ = source17_.name
                d_565___mcc_h1_ = source17_.algorithmSuite
                d_566___mcc_h2_ = source17_.commitmentPolicy
                d_567___mcc_h3_ = source17_.encryptedDataKeys
                d_568___mcc_h4_ = source17_.encryptionContext
                d_569___mcc_h5_ = source17_.keyDescription
                d_570___mcc_h6_ = source17_.expectedResult
                d_571___mcc_h7_ = source17_.description
                d_572___mcc_h8_ = source17_.reproducedEncryptionContext
                return ((((pat_let_tv3_).is_Success) and (((((pat_let_tv4_).value).decryptionMaterials).plaintextDataKey) == ((((pat_let_tv5_).vector).expectedResult).plaintextDataKey))) and (((((pat_let_tv6_).value).decryptionMaterials).symmetricSigningKey) == ((((pat_let_tv7_).vector).expectedResult).symmetricSigningKey))) and (((((pat_let_tv8_).value).decryptionMaterials).requiredEncryptionContextKeys) == ((((pat_let_tv9_).vector).expectedResult).requiredEncryptionContextKeys))
            elif True:
                d_573___mcc_h9_ = source17_.name
                d_574___mcc_h10_ = source17_.algorithmSuite
                d_575___mcc_h11_ = source17_.commitmentPolicy
                d_576___mcc_h12_ = source17_.encryptedDataKeys
                d_577___mcc_h13_ = source17_.encryptionContext
                d_578___mcc_h14_ = source17_.errorDescription
                d_579___mcc_h15_ = source17_.keyDescription
                d_580___mcc_h16_ = source17_.reproducedEncryptionContext
                d_581___mcc_h17_ = source17_.description
                return not((pat_let_tv10_).is_Success)

        output = lambda53_((test).vector)
        if not(output):
            if (((test).vector).is_PositiveDecryptKeyringTest) and ((d_563_result_).is_Failure):
                _dafny.print(_dafny.string_of((d_563_result_).error))
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
        d_582_input_: AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput
        def lambda54_(source18_):
            if source18_.is_PositiveEncryptKeyringVector:
                d_583___mcc_h0_ = source18_.name
                d_584___mcc_h1_ = source18_.description
                d_585___mcc_h2_ = source18_.encryptionContext
                d_586___mcc_h3_ = source18_.commitmentPolicy
                d_587___mcc_h4_ = source18_.algorithmSuite
                d_588___mcc_h5_ = source18_.maxPlaintextLength
                d_589___mcc_h6_ = source18_.requiredEncryptionContextKeys
                d_590___mcc_h7_ = source18_.encryptDescription
                d_591___mcc_h8_ = source18_.decryptDescription
                d_592___mcc_h9_ = source18_.reproducedEncryptionContext
                return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv11_).encryptionContext, (pat_let_tv12_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv13_).algorithmSuite).id), (pat_let_tv14_).maxPlaintextLength, (pat_let_tv15_).requiredEncryptionContextKeys)
            elif source18_.is_PositiveEncryptNegativeDecryptKeyringVector:
                d_593___mcc_h10_ = source18_.name
                d_594___mcc_h11_ = source18_.description
                d_595___mcc_h12_ = source18_.encryptionContext
                d_596___mcc_h13_ = source18_.commitmentPolicy
                d_597___mcc_h14_ = source18_.algorithmSuite
                d_598___mcc_h15_ = source18_.maxPlaintextLength
                d_599___mcc_h16_ = source18_.requiredEncryptionContextKeys
                d_600___mcc_h17_ = source18_.decryptErrorDescription
                d_601___mcc_h18_ = source18_.encryptDescription
                d_602___mcc_h19_ = source18_.decryptDescription
                d_603___mcc_h20_ = source18_.reproducedEncryptionContext
                return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv16_).encryptionContext, (pat_let_tv17_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv18_).algorithmSuite).id), (pat_let_tv19_).maxPlaintextLength, (pat_let_tv20_).requiredEncryptionContextKeys)
            elif True:
                d_604___mcc_h21_ = source18_.name
                d_605___mcc_h22_ = source18_.description
                d_606___mcc_h23_ = source18_.encryptionContext
                d_607___mcc_h24_ = source18_.commitmentPolicy
                d_608___mcc_h25_ = source18_.algorithmSuite
                d_609___mcc_h26_ = source18_.maxPlaintextLength
                d_610___mcc_h27_ = source18_.requiredEncryptionContextKeys
                d_611___mcc_h28_ = source18_.errorDescription
                d_612___mcc_h29_ = source18_.keyDescription
                return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv21_).encryptionContext, (pat_let_tv22_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv23_).algorithmSuite).id), (pat_let_tv24_).maxPlaintextLength, (pat_let_tv25_).requiredEncryptionContextKeys)

        d_582_input_ = lambda54_(vector)
        d_613_mpl_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_614_valueOrError0_: Wrappers.Result = None
        out53_: Wrappers.Result
        out53_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_614_valueOrError0_ = out53_
        if not(not((d_614_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(133,15): " + _dafny.string_of(d_614_valueOrError0_))
        d_613_mpl_ = (d_614_valueOrError0_).Extract()
        d_615_cmm_k_: Wrappers.Result
        out54_: Wrappers.Result
        out54_ = (keys).CreateWrappedTestVectorCmm(AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput_TestVectorCmmInput(((vector).encryptDescription if (vector).is_PositiveEncryptKeyringVector else ((vector).encryptDescription if (vector).is_PositiveEncryptNegativeDecryptKeyringVector else (vector).keyDescription)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation_ENCRYPT()))
        d_615_cmm_k_ = out54_
        d_616_cmm_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
        d_617_valueOrError1_: Wrappers.Result = None
        def lambda55_(d_618_e_):
            def iife20_(_pat_let7_0):
                def iife21_(d_619___v78_):
                    return _dafny.Seq("Cmm failure")
                return iife21_(_pat_let7_0)
            return iife20_(default__.printErr(d_618_e_))

        d_617_valueOrError1_ = (d_615_cmm_k_).MapFailure(lambda55_)
        if (d_617_valueOrError1_).IsFailure():
            output = (d_617_valueOrError1_).PropagateFailure()
            return output
        d_616_cmm_ = (d_617_valueOrError1_).Extract()
        output = Wrappers.Result_Success(EncryptTest_EncryptTest(d_582_input_, d_616_cmm_, vector))
        return output
        return output

    @staticmethod
    def EncryptTestToDecryptVector(test, materials):
        d_620_keysToRemove_ = Seq.default__.ToSet((((test).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))
        source19_ = (test).vector
        if source19_.is_PositiveEncryptKeyringVector:
            d_621___mcc_h0_ = source19_.name
            d_622___mcc_h1_ = source19_.description
            d_623___mcc_h2_ = source19_.encryptionContext
            d_624___mcc_h3_ = source19_.commitmentPolicy
            d_625___mcc_h4_ = source19_.algorithmSuite
            d_626___mcc_h5_ = source19_.maxPlaintextLength
            d_627___mcc_h6_ = source19_.requiredEncryptionContextKeys
            d_628___mcc_h7_ = source19_.encryptDescription
            d_629___mcc_h8_ = source19_.decryptDescription
            d_630___mcc_h9_ = source19_.reproducedEncryptionContext
            return DecryptTestVector_PositiveDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), ((test).vector).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, ((materials).encryptionContext) - (d_620_keysToRemove_), ((test).vector).decryptDescription, DecryptResult_DecryptResult((materials).plaintextDataKey, (Wrappers.Option_Some((((materials).symmetricSigningKeys).value)[0]) if (((materials).symmetricSigningKeys).is_Some) and ((0) < (len(((materials).symmetricSigningKeys).value))) else Wrappers.Option_None()), (((test).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))), (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()), ((test).vector).reproducedEncryptionContext)
        elif True:
            d_631___mcc_h10_ = source19_.name
            d_632___mcc_h11_ = source19_.description
            d_633___mcc_h12_ = source19_.encryptionContext
            d_634___mcc_h13_ = source19_.commitmentPolicy
            d_635___mcc_h14_ = source19_.algorithmSuite
            d_636___mcc_h15_ = source19_.maxPlaintextLength
            d_637___mcc_h16_ = source19_.requiredEncryptionContextKeys
            d_638___mcc_h17_ = source19_.decryptErrorDescription
            d_639___mcc_h18_ = source19_.encryptDescription
            d_640___mcc_h19_ = source19_.decryptDescription
            d_641___mcc_h20_ = source19_.reproducedEncryptionContext
            return DecryptTestVector_NegativeDecryptKeyringTest((((test).vector).name) + (_dafny.Seq("->Decryption")), ((test).vector).algorithmSuite, ((test).vector).commitmentPolicy, (materials).encryptedDataKeys, (((test).vector).encryptionContext) - (d_620_keysToRemove_), ((test).vector).decryptErrorDescription, ((test).vector).decryptDescription, ((test).vector).reproducedEncryptionContext, (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((test).vector).description).value)) if (((test).vector).description).is_Some else Wrappers.Option_None()))

    @staticmethod
    def DecryptVectorToDecryptTest(keys, vector):
        output: Wrappers.Result = None
        d_642_input_: AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput
        d_642_input_ = AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput_DecryptMaterialsInput(((vector).algorithmSuite).id, (vector).commitmentPolicy, (vector).encryptedDataKeys, (vector).encryptionContext, (vector).reproducedEncryptionContext)
        d_643_mpl_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_644_valueOrError0_: Wrappers.Result = None
        out55_: Wrappers.Result
        out55_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_644_valueOrError0_ = out55_
        if not(not((d_644_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(218,15): " + _dafny.string_of(d_644_valueOrError0_))
        d_643_mpl_ = (d_644_valueOrError0_).Extract()
        d_645_cmm_k_: Wrappers.Result
        out56_: Wrappers.Result
        out56_ = (keys).CreateWrappedTestVectorCmm(AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput_TestVectorCmmInput((vector).keyDescription, AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation_DECRYPT()))
        d_645_cmm_k_ = out56_
        d_646_cmm_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
        d_647_valueOrError1_: Wrappers.Result = None
        d_647_valueOrError1_ = (d_645_cmm_k_).MapFailure(default__.ErrorToString)
        if (d_647_valueOrError1_).IsFailure():
            output = (d_647_valueOrError1_).PropagateFailure()
            return output
        d_646_cmm_ = (d_647_valueOrError1_).Extract()
        output = Wrappers.Result_Success(DecryptTest_DecryptTest(d_642_input_, d_646_cmm_, vector))
        return output
        return output

    @staticmethod
    def ErrorToString(e):
        source20_ = e
        if source20_.is_KeyVectorException:
            d_648___mcc_h0_ = source20_.message
            d_649_message_ = d_648___mcc_h0_
            return d_649_message_
        elif source20_.is_AwsCryptographyMaterialProviders:
            d_650___mcc_h2_ = source20_.AwsCryptographyMaterialProviders
            d_651_mplError_ = d_650___mcc_h2_
            source21_ = d_651_mplError_
            if source21_.is_AwsCryptographicMaterialProvidersException:
                d_652___mcc_h12_ = source21_.message
                d_653_message_ = d_652___mcc_h12_
                return d_653_message_
            elif source21_.is_EntryAlreadyExists:
                d_654___mcc_h14_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_EntryDoesNotExist:
                d_655___mcc_h16_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfo:
                d_656___mcc_h18_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfoOnDecrypt:
                d_657___mcc_h20_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidAlgorithmSuiteInfoOnEncrypt:
                d_658___mcc_h22_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidDecryptionMaterials:
                d_659___mcc_h24_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidDecryptionMaterialsTransition:
                d_660___mcc_h26_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidEncryptionMaterials:
                d_661___mcc_h28_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_InvalidEncryptionMaterialsTransition:
                d_662___mcc_h30_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_AwsCryptographyKeyStore:
                d_663___mcc_h32_ = source21_.AwsCryptographyKeyStore
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_AwsCryptographyPrimitives:
                d_664___mcc_h34_ = source21_.AwsCryptographyPrimitives
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_ComAmazonawsDynamodb:
                d_665___mcc_h36_ = source21_.ComAmazonawsDynamodb
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_ComAmazonawsKms:
                d_666___mcc_h38_ = source21_.ComAmazonawsKms
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif source21_.is_CollectionOfErrors:
                d_667___mcc_h40_ = source21_.list
                d_668___mcc_h41_ = source21_.message
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
            elif True:
                d_669___mcc_h44_ = source21_.obj
                return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
        elif source20_.is_ComAmazonawsKms:
            d_670___mcc_h4_ = source20_.ComAmazonawsKms
            return _dafny.Seq("Unmapped KeyVectorException")
        elif source20_.is_CollectionOfErrors:
            d_671___mcc_h6_ = source20_.list
            d_672___mcc_h7_ = source20_.message
            return _dafny.Seq("Unmapped KeyVectorException")
        elif True:
            d_673___mcc_h10_ = source20_.obj
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
        return lambda: EncryptTest_EncryptTest(AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput.default()(), None, EncryptTestVector.default()())
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
        return lambda: DecryptTest_DecryptTest(AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput.default()(), None, DecryptTestVector.default()())
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
        return lambda: EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq(""), Wrappers.Option.default()(), _dafny.Map({}), AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.default()(), AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.default()(), AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.default()(), Wrappers.Option.default()())
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
        return lambda: DecryptTestVector_PositiveDecryptKeyringTest(_dafny.Seq(""), AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()(), AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.default()(), _dafny.Seq({}), _dafny.Map({}), AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.default()(), DecryptResult.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
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

