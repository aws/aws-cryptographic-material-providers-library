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
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
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
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
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
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
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
import standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyVectors as KeyVectors

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
        d_444_result_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = ((test).cmm).GetEncryptionMaterials((test).input)
        d_444_result_ = out35_
        pat_let_tv16_ = d_444_result_
        pat_let_tv17_ = d_444_result_
        pat_let_tv18_ = d_444_result_
        def lambda45_():
            source15_ = (test).vector
            unmatched15 = True
            if unmatched15:
                if source15_.is_PositiveEncryptKeyringVector:
                    d_445___v0_ = source15_.name
                    d_446___v1_ = source15_.description
                    d_447___v2_ = source15_.encryptionContext
                    d_448___v3_ = source15_.commitmentPolicy
                    d_449___v4_ = source15_.algorithmSuite
                    d_450___v5_ = source15_.maxPlaintextLength
                    d_451___v6_ = source15_.requiredEncryptionContextKeys
                    d_452___v7_ = source15_.encryptDescription
                    d_453___v8_ = source15_.decryptDescription
                    d_454___v9_ = source15_.reproducedEncryptionContext
                    unmatched15 = False
                    return (pat_let_tv16_).is_Success
            if unmatched15:
                if source15_.is_PositiveEncryptNegativeDecryptKeyringVector:
                    d_455___v10_ = source15_.name
                    d_456___v11_ = source15_.description
                    d_457___v12_ = source15_.encryptionContext
                    d_458___v13_ = source15_.commitmentPolicy
                    d_459___v14_ = source15_.algorithmSuite
                    d_460___v15_ = source15_.maxPlaintextLength
                    d_461___v16_ = source15_.requiredEncryptionContextKeys
                    d_462___v17_ = source15_.decryptErrorDescription
                    d_463___v18_ = source15_.encryptDescription
                    d_464___v19_ = source15_.decryptDescription
                    d_465___v20_ = source15_.reproducedEncryptionContext
                    unmatched15 = False
                    return (pat_let_tv17_).is_Success
            if unmatched15:
                d_466___v21_ = source15_.name
                d_467___v22_ = source15_.description
                d_468___v23_ = source15_.encryptionContext
                d_469___v24_ = source15_.commitmentPolicy
                d_470___v25_ = source15_.algorithmSuite
                d_471___v26_ = source15_.maxPlaintextLength
                d_472___v27_ = source15_.requiredEncryptionContextKeys
                d_473___v28_ = source15_.errorDescription
                d_474___v29_ = source15_.keyDescription
                unmatched15 = False
                return not((pat_let_tv18_).is_Success)
            raise Exception("unexpected control point")

        testResult = lambda45_()
        materials = (Wrappers.Option_Some(((d_444_result_).value).encryptionMaterials) if (testResult) and ((d_444_result_).is_Success) else Wrappers.Option_None())
        if not(testResult):
            if (((test).vector).is_PositiveEncryptKeyringVector) or (((test).vector).is_PositiveEncryptNegativeDecryptKeyringVector):
                _dafny.print(_dafny.string_of((d_444_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return testResult, materials

    @staticmethod
    def TestDecryptMaterials(test):
        output: bool = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\nTEST===> ")))
        _dafny.print(_dafny.string_of(((test).vector).name))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + ((((test).vector).description).value) if (((test).vector).description).is_Some else _dafny.Seq(""))))
        _dafny.print(_dafny.string_of(((_dafny.Seq("\n")) + (((test).vector).errorDescription) if ((test).vector).is_NegativeDecryptKeyringTest else _dafny.Seq("\n"))))
        d_475_result_: Wrappers.Result
        out36_: Wrappers.Result
        out36_ = ((test).cmm).DecryptMaterials((test).input)
        d_475_result_ = out36_
        pat_let_tv19_ = d_475_result_
        pat_let_tv20_ = d_475_result_
        pat_let_tv21_ = test
        pat_let_tv22_ = d_475_result_
        pat_let_tv23_ = test
        pat_let_tv24_ = d_475_result_
        pat_let_tv25_ = test
        pat_let_tv26_ = d_475_result_
        def lambda46_():
            source16_ = (test).vector
            unmatched16 = True
            if unmatched16:
                if source16_.is_PositiveDecryptKeyringTest:
                    d_476___v30_ = source16_.name
                    d_477___v31_ = source16_.algorithmSuite
                    d_478___v32_ = source16_.commitmentPolicy
                    d_479___v33_ = source16_.encryptedDataKeys
                    d_480___v34_ = source16_.encryptionContext
                    d_481___v35_ = source16_.keyDescription
                    d_482___v36_ = source16_.expectedResult
                    d_483___v37_ = source16_.description
                    d_484___v38_ = source16_.reproducedEncryptionContext
                    unmatched16 = False
                    return ((((pat_let_tv19_).is_Success) and (((((pat_let_tv20_).value).decryptionMaterials).plaintextDataKey) == ((((pat_let_tv21_).vector).expectedResult).plaintextDataKey))) and (((((pat_let_tv22_).value).decryptionMaterials).symmetricSigningKey) == ((((pat_let_tv23_).vector).expectedResult).symmetricSigningKey))) and (((((pat_let_tv24_).value).decryptionMaterials).requiredEncryptionContextKeys) == ((((pat_let_tv25_).vector).expectedResult).requiredEncryptionContextKeys))
            if unmatched16:
                d_485___v39_ = source16_.name
                d_486___v40_ = source16_.algorithmSuite
                d_487___v41_ = source16_.commitmentPolicy
                d_488___v42_ = source16_.encryptedDataKeys
                d_489___v43_ = source16_.encryptionContext
                d_490___v44_ = source16_.errorDescription
                d_491___v45_ = source16_.keyDescription
                d_492___v46_ = source16_.reproducedEncryptionContext
                d_493___v47_ = source16_.description
                unmatched16 = False
                return not((pat_let_tv26_).is_Success)
            raise Exception("unexpected control point")

        output = lambda46_()
        if not(output):
            if (((test).vector).is_PositiveDecryptKeyringTest) and ((d_475_result_).is_Failure):
                _dafny.print(_dafny.string_of((d_475_result_).error))
            _dafny.print(_dafny.string_of(_dafny.Seq("\nFAILED! <-----------\n")))
        return output

    @staticmethod
    def ToEncryptTest(keys, vector):
        output: Wrappers.Result = None
        pat_let_tv27_ = vector
        pat_let_tv28_ = vector
        pat_let_tv29_ = vector
        pat_let_tv30_ = vector
        pat_let_tv31_ = vector
        pat_let_tv32_ = vector
        pat_let_tv33_ = vector
        pat_let_tv34_ = vector
        pat_let_tv35_ = vector
        pat_let_tv36_ = vector
        pat_let_tv37_ = vector
        pat_let_tv38_ = vector
        pat_let_tv39_ = vector
        pat_let_tv40_ = vector
        pat_let_tv41_ = vector
        d_494_input_: AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput
        def lambda47_():
            source17_ = vector
            unmatched17 = True
            if unmatched17:
                if source17_.is_PositiveEncryptKeyringVector:
                    d_495___v48_ = source17_.name
                    d_496___v49_ = source17_.description
                    d_497___v50_ = source17_.encryptionContext
                    d_498___v51_ = source17_.commitmentPolicy
                    d_499___v52_ = source17_.algorithmSuite
                    d_500___v53_ = source17_.maxPlaintextLength
                    d_501___v54_ = source17_.requiredEncryptionContextKeys
                    d_502___v55_ = source17_.encryptDescription
                    d_503___v56_ = source17_.decryptDescription
                    d_504___v57_ = source17_.reproducedEncryptionContext
                    unmatched17 = False
                    return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv27_).encryptionContext, (pat_let_tv28_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv29_).algorithmSuite).id), (pat_let_tv30_).maxPlaintextLength, (pat_let_tv31_).requiredEncryptionContextKeys)
            if unmatched17:
                if source17_.is_NegativeEncryptKeyringVector:
                    d_505___v58_ = source17_.name
                    d_506___v59_ = source17_.description
                    d_507___v60_ = source17_.encryptionContext
                    d_508___v61_ = source17_.commitmentPolicy
                    d_509___v62_ = source17_.algorithmSuite
                    d_510___v63_ = source17_.maxPlaintextLength
                    d_511___v64_ = source17_.requiredEncryptionContextKeys
                    d_512___v65_ = source17_.errorDescription
                    d_513___v66_ = source17_.keyDescription
                    unmatched17 = False
                    return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv32_).encryptionContext, (pat_let_tv33_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv34_).algorithmSuite).id), (pat_let_tv35_).maxPlaintextLength, (pat_let_tv36_).requiredEncryptionContextKeys)
            if unmatched17:
                d_514___v67_ = source17_.name
                d_515___v68_ = source17_.description
                d_516___v69_ = source17_.encryptionContext
                d_517___v70_ = source17_.commitmentPolicy
                d_518___v71_ = source17_.algorithmSuite
                d_519___v72_ = source17_.maxPlaintextLength
                d_520___v73_ = source17_.requiredEncryptionContextKeys
                d_521___v74_ = source17_.decryptErrorDescription
                d_522___v75_ = source17_.encryptDescription
                d_523___v76_ = source17_.decryptDescription
                d_524___v77_ = source17_.reproducedEncryptionContext
                unmatched17 = False
                return AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput((pat_let_tv37_).encryptionContext, (pat_let_tv38_).commitmentPolicy, Wrappers.Option_Some(((pat_let_tv39_).algorithmSuite).id), (pat_let_tv40_).maxPlaintextLength, (pat_let_tv41_).requiredEncryptionContextKeys)
            raise Exception("unexpected control point")

        d_494_input_ = lambda47_()
        d_525_mpl_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_526_valueOrError0_: Wrappers.Result = None
        out37_: Wrappers.Result
        out37_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_526_valueOrError0_ = out37_
        if not(not((d_526_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(133,15): " + _dafny.string_of(d_526_valueOrError0_))
        d_525_mpl_ = (d_526_valueOrError0_).Extract()
        d_527_cmm_k_: Wrappers.Result
        out38_: Wrappers.Result
        out38_ = (keys).CreateWrappedTestVectorCmm(AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput_TestVectorCmmInput(((vector).encryptDescription if (vector).is_PositiveEncryptKeyringVector else ((vector).encryptDescription if (vector).is_PositiveEncryptNegativeDecryptKeyringVector else (vector).keyDescription)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation_ENCRYPT()))
        d_527_cmm_k_ = out38_
        d_528_cmm_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
        d_529_valueOrError1_: Wrappers.Result = None
        def lambda48_(d_530_e_):
            def iife20_(_pat_let7_0):
                def iife21_(d_531___v78_):
                    return _dafny.Seq("Cmm failure")
                return iife21_(_pat_let7_0)
            return iife20_(default__.printErr(d_530_e_))

        d_529_valueOrError1_ = (d_527_cmm_k_).MapFailure(lambda48_)
        if (d_529_valueOrError1_).IsFailure():
            output = (d_529_valueOrError1_).PropagateFailure()
            return output
        d_528_cmm_ = (d_529_valueOrError1_).Extract()
        output = Wrappers.Result_Success(EncryptTest_EncryptTest(d_494_input_, d_528_cmm_, vector))
        return output
        return output

    @staticmethod
    def EncryptTestToDecryptVector(test, materials):
        pat_let_tv42_ = test
        pat_let_tv43_ = test
        pat_let_tv44_ = test
        pat_let_tv45_ = materials
        pat_let_tv46_ = materials
        pat_let_tv47_ = test
        pat_let_tv48_ = materials
        pat_let_tv49_ = materials
        pat_let_tv50_ = materials
        pat_let_tv51_ = materials
        pat_let_tv52_ = test
        pat_let_tv53_ = test
        pat_let_tv54_ = test
        pat_let_tv55_ = test
        pat_let_tv56_ = test
        pat_let_tv57_ = test
        pat_let_tv58_ = test
        pat_let_tv59_ = materials
        pat_let_tv60_ = test
        pat_let_tv61_ = test
        pat_let_tv62_ = test
        pat_let_tv63_ = test
        pat_let_tv64_ = test
        pat_let_tv65_ = test
        d_532_keysToRemove_ = Seq.default__.ToSet((((test).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))
        source18_ = (test).vector
        unmatched18 = True
        if unmatched18:
            if source18_.is_PositiveEncryptKeyringVector:
                d_533___v79_ = source18_.name
                d_534___v80_ = source18_.description
                d_535___v81_ = source18_.encryptionContext
                d_536___v82_ = source18_.commitmentPolicy
                d_537___v83_ = source18_.algorithmSuite
                d_538___v84_ = source18_.maxPlaintextLength
                d_539___v85_ = source18_.requiredEncryptionContextKeys
                d_540___v86_ = source18_.encryptDescription
                d_541___v87_ = source18_.decryptDescription
                d_542___v88_ = source18_.reproducedEncryptionContext
                unmatched18 = False
                return DecryptTestVector_PositiveDecryptKeyringTest((((pat_let_tv42_).vector).name) + (_dafny.Seq("->Decryption")), ((pat_let_tv43_).vector).algorithmSuite, ((pat_let_tv44_).vector).commitmentPolicy, (pat_let_tv45_).encryptedDataKeys, ((pat_let_tv46_).encryptionContext) - (d_532_keysToRemove_), ((pat_let_tv47_).vector).decryptDescription, DecryptResult_DecryptResult((pat_let_tv48_).plaintextDataKey, (Wrappers.Option_Some((((pat_let_tv49_).symmetricSigningKeys).value)[0]) if (((pat_let_tv50_).symmetricSigningKeys).is_Some) and ((0) < (len(((pat_let_tv51_).symmetricSigningKeys).value))) else Wrappers.Option_None()), (((pat_let_tv52_).vector).requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))), (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((pat_let_tv53_).vector).description).value)) if (((pat_let_tv54_).vector).description).is_Some else Wrappers.Option_None()), ((pat_let_tv55_).vector).reproducedEncryptionContext)
        if unmatched18:
            d_543___v89_ = source18_.name
            d_544___v90_ = source18_.description
            d_545___v91_ = source18_.encryptionContext
            d_546___v92_ = source18_.commitmentPolicy
            d_547___v93_ = source18_.algorithmSuite
            d_548___v94_ = source18_.maxPlaintextLength
            d_549___v95_ = source18_.requiredEncryptionContextKeys
            d_550___v96_ = source18_.decryptErrorDescription
            d_551___v97_ = source18_.encryptDescription
            d_552___v98_ = source18_.decryptDescription
            d_553___v99_ = source18_.reproducedEncryptionContext
            unmatched18 = False
            return DecryptTestVector_NegativeDecryptKeyringTest((((pat_let_tv56_).vector).name) + (_dafny.Seq("->Decryption")), ((pat_let_tv57_).vector).algorithmSuite, ((pat_let_tv58_).vector).commitmentPolicy, (pat_let_tv59_).encryptedDataKeys, (((pat_let_tv60_).vector).encryptionContext) - (d_532_keysToRemove_), ((pat_let_tv61_).vector).decryptErrorDescription, ((pat_let_tv62_).vector).decryptDescription, ((pat_let_tv63_).vector).reproducedEncryptionContext, (Wrappers.Option_Some((_dafny.Seq("Decryption for ")) + ((((pat_let_tv64_).vector).description).value)) if (((pat_let_tv65_).vector).description).is_Some else Wrappers.Option_None()))
        raise Exception("unexpected control point")

    @staticmethod
    def DecryptVectorToDecryptTest(keys, vector):
        output: Wrappers.Result = None
        d_554_input_: AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput
        d_554_input_ = AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput_DecryptMaterialsInput(((vector).algorithmSuite).id, (vector).commitmentPolicy, (vector).encryptedDataKeys, (vector).encryptionContext, (vector).reproducedEncryptionContext)
        d_555_mpl_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_556_valueOrError0_: Wrappers.Result = None
        out39_: Wrappers.Result
        out39_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_556_valueOrError0_ = out39_
        if not(not((d_556_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(218,15): " + _dafny.string_of(d_556_valueOrError0_))
        d_555_mpl_ = (d_556_valueOrError0_).Extract()
        d_557_cmm_k_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = (keys).CreateWrappedTestVectorCmm(AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput_TestVectorCmmInput((vector).keyDescription, AwsCryptographyMaterialProvidersTestVectorKeysTypes.CmmOperation_DECRYPT()))
        d_557_cmm_k_ = out40_
        d_558_cmm_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
        d_559_valueOrError1_: Wrappers.Result = None
        d_559_valueOrError1_ = (d_557_cmm_k_).MapFailure(default__.ErrorToString)
        if (d_559_valueOrError1_).IsFailure():
            output = (d_559_valueOrError1_).PropagateFailure()
            return output
        d_558_cmm_ = (d_559_valueOrError1_).Extract()
        output = Wrappers.Result_Success(DecryptTest_DecryptTest(d_554_input_, d_558_cmm_, vector))
        return output
        return output

    @staticmethod
    def ErrorToString(e):
        source19_ = e
        unmatched19 = True
        if unmatched19:
            if source19_.is_KeyVectorException:
                d_560_message_ = source19_.message
                unmatched19 = False
                return d_560_message_
        if unmatched19:
            if source19_.is_AwsCryptographyMaterialProviders:
                d_561_mplError_ = source19_.AwsCryptographyMaterialProviders
                unmatched19 = False
                source20_ = d_561_mplError_
                unmatched20 = True
                if unmatched20:
                    if source20_.is_AwsCryptographicMaterialProvidersException:
                        d_562_message_ = source20_.message
                        unmatched20 = False
                        return d_562_message_
                if unmatched20:
                    d_563___v100_ = source20_
                    unmatched20 = False
                    return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
                raise Exception("unexpected control point")
        if unmatched19:
            d_564___v101_ = source19_
            unmatched19 = False
            return _dafny.Seq("Unmapped KeyVectorException")
        raise Exception("unexpected control point")

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

