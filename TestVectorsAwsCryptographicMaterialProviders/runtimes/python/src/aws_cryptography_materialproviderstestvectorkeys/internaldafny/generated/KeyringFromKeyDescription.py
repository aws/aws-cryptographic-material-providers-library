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

# Module: KeyringFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetKeyId(input):
        while True:
            with _dafny.label():
                source3_ = input
                if source3_.is_Kms:
                    d_283___mcc_h0_ = source3_.Kms
                    d_284_i_ = d_283___mcc_h0_
                    return (d_284_i_).keyId
                elif source3_.is_KmsMrk:
                    d_285___mcc_h1_ = source3_.KmsMrk
                    d_286_i_ = d_285___mcc_h1_
                    return (d_286_i_).keyId
                elif source3_.is_KmsMrkDiscovery:
                    d_287___mcc_h2_ = source3_.KmsMrkDiscovery
                    d_288_i_ = d_287___mcc_h2_
                    return (d_288_i_).keyId
                elif source3_.is_RSA:
                    d_289___mcc_h3_ = source3_.RSA
                    d_290_i_ = d_289___mcc_h3_
                    return (d_290_i_).keyId
                elif source3_.is_AES:
                    d_291___mcc_h4_ = source3_.AES
                    d_292_i_ = d_291___mcc_h4_
                    return (d_292_i_).keyId
                elif source3_.is_Static:
                    d_293___mcc_h5_ = source3_.Static
                    d_294_i_ = d_293___mcc_h5_
                    return (d_294_i_).keyId
                elif source3_.is_KmsRsa:
                    d_295___mcc_h6_ = source3_.KmsRsa
                    d_296_i_ = d_295___mcc_h6_
                    return (d_296_i_).keyId
                elif source3_.is_Hierarchy:
                    d_297___mcc_h7_ = source3_.Hierarchy
                    d_298_i_ = d_297___mcc_h7_
                    return (d_298_i_).keyId
                elif source3_.is_Multi:
                    d_299___mcc_h8_ = source3_.Multi
                    return _dafny.Seq("")
                elif True:
                    d_300___mcc_h9_ = source3_.RequiredEncryptionContext
                    d_301_i_ = d_300___mcc_h9_
                    in2_ = (d_301_i_).underlying
                    input = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetKeyMaterial(keys, keyDescription):
        d_302_keyId_ = default__.GetKeyId(keyDescription)
        if (d_302_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_302_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ToKeyring(mpl, keys, description):
        output: Wrappers.Result = None
        d_303_material_: Wrappers.Option
        d_303_material_ = default__.GetKeyMaterial(keys, description)
        print(f"{d_303_material_=}")
        source4_ = description
        if source4_.is_Kms:
            d_304___mcc_h0_ = source4_.Kms
            source5_ = d_304___mcc_h0_
            d_305___mcc_h1_ = source5_.keyId
            d_306_key_ = d_305___mcc_h1_
            if True:
                d_307_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_307_valueOrError1_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                print(f"{d_307_valueOrError1_=}")
                if (d_307_valueOrError1_).IsFailure():
                    output = (d_307_valueOrError1_).PropagateFailure()
                    return output
                d_308_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_309_valueOrError2_: Wrappers.Result = None
                out2_: Wrappers.Result
                out2_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                print(f"{out2_=}")
                d_309_valueOrError2_ = out2_
                if (d_309_valueOrError2_).IsFailure():
                    output = (d_309_valueOrError2_).PropagateFailure()
                    return output
                d_308_kmsClient_ = (d_309_valueOrError2_).Extract()
                d_310_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput
                d_310_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_303_material_).value).keyIdentifier, d_308_kmsClient_, Wrappers.Option_None())
                d_311_keyring_: Wrappers.Result
                out3_: Wrappers.Result
                out3_ = (mpl).CreateAwsKmsKeyring(d_310_input_)
                print(f"{out3_=}")
                d_311_keyring_ = out3_
                def lambda19_(d_312_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_312_e_)

                output = (d_311_keyring_).MapFailure(lambda19_)
                return output
        elif source4_.is_KmsMrk:
            d_313___mcc_h2_ = source4_.KmsMrk
            source6_ = d_313___mcc_h2_
            d_314___mcc_h3_ = source6_.keyId
            d_315_key_ = d_314___mcc_h3_
            if True:
                d_316_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_316_valueOrError3_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_316_valueOrError3_).IsFailure():
                    output = (d_316_valueOrError3_).PropagateFailure()
                    return output
                d_317_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_318_valueOrError4_: Wrappers.Result = None
                out4_: Wrappers.Result
                out4_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                d_318_valueOrError4_ = out4_
                if (d_318_valueOrError4_).IsFailure():
                    output = (d_318_valueOrError4_).PropagateFailure()
                    return output
                d_317_kmsClient_ = (d_318_valueOrError4_).Extract()
                d_319_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput
                d_319_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_303_material_).value).keyIdentifier, d_317_kmsClient_, Wrappers.Option_None())
                d_320_keyring_: Wrappers.Result
                out5_: Wrappers.Result
                out5_ = (mpl).CreateAwsKmsMrkKeyring(d_319_input_)
                d_320_keyring_ = out5_
                def lambda20_(d_321_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_321_e_)

                output = (d_320_keyring_).MapFailure(lambda20_)
                return output
        elif source4_.is_KmsMrkDiscovery:
            d_322___mcc_h4_ = source4_.KmsMrkDiscovery
            source7_ = d_322___mcc_h4_
            d_323___mcc_h5_ = source7_.keyId
            d_324___mcc_h6_ = source7_.defaultMrkRegion
            d_325___mcc_h7_ = source7_.awsKmsDiscoveryFilter
            d_326_awsKmsDiscoveryFilter_ = d_325___mcc_h7_
            d_327_defaultMrkRegion_ = d_324___mcc_h6_
            if True:
                d_328_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_328_valueOrError8_ = Wrappers.default__.Need((d_303_material_).is_None, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                if (d_328_valueOrError8_).IsFailure():
                    output = (d_328_valueOrError8_).PropagateFailure()
                    return output
                d_329_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                d_329_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_327_defaultMrkRegion_]), d_326_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                d_330_keyring_: Wrappers.Result
                out6_: Wrappers.Result
                out6_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_329_input_)
                d_330_keyring_ = out6_
                def lambda21_(d_331_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_331_e_)

                output = (d_330_keyring_).MapFailure(lambda21_)
                return output
        elif source4_.is_RSA:
            d_332___mcc_h8_ = source4_.RSA
            source8_ = d_332___mcc_h8_
            d_333___mcc_h9_ = source8_.keyId
            d_334___mcc_h10_ = source8_.providerId
            d_335___mcc_h11_ = source8_.padding
            d_336_padding_ = d_335___mcc_h11_
            d_337_providerId_ = d_334___mcc_h10_
            d_338_key_ = d_333___mcc_h9_
            if True:
                d_339_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_339_valueOrError11_ = Wrappers.default__.Need(((d_303_material_).is_Some) and ((((d_303_material_).value).is_PrivateRSA) or (((d_303_material_).value).is_PublicRSA)), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                if (d_339_valueOrError11_).IsFailure():
                    output = (d_339_valueOrError11_).PropagateFailure()
                    return output
                source9_ = d_303_material_
                d_340___mcc_h24_ = source9_.value
                source10_ = d_340___mcc_h24_
                if source10_.is_PrivateRSA:
                    d_341___mcc_h33_ = source10_.name
                    d_342___mcc_h34_ = source10_.encrypt
                    d_343___mcc_h35_ = source10_.decrypt
                    d_344___mcc_h36_ = source10_.algorithm
                    d_345___mcc_h37_ = source10_.bits
                    d_346___mcc_h38_ = source10_.encoding
                    d_347___mcc_h39_ = source10_.material
                    d_348___mcc_h40_ = source10_.keyIdentifier
                    d_349_keyIdentifier_ = d_348___mcc_h40_
                    d_350_material_ = d_347___mcc_h39_
                    d_351_decrypt_ = d_343___mcc_h35_
                    if True:
                        d_352_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_352_valueOrError12_ = Wrappers.default__.Need(d_351_decrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                        if (d_352_valueOrError12_).IsFailure():
                            output = (d_352_valueOrError12_).PropagateFailure()
                            return output
                        d_353_privateKeyPemBytes_: _dafny.Seq
                        d_354_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda22_(d_355_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_355_e_)

                        d_354_valueOrError13_ = (UTF8.default__.Encode(d_350_material_)).MapFailure(lambda22_)
                        if (d_354_valueOrError13_).IsFailure():
                            output = (d_354_valueOrError13_).PropagateFailure()
                            return output
                        d_353_privateKeyPemBytes_ = (d_354_valueOrError13_).Extract()
                        d_356_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_356_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_337_providerId_, d_349_keyIdentifier_, d_336_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_353_privateKeyPemBytes_))
                        d_357_keyring_: Wrappers.Result
                        out7_: Wrappers.Result
                        out7_ = (mpl).CreateRawRsaKeyring(d_356_input_)
                        d_357_keyring_ = out7_
                        def lambda23_(d_358_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_358_e_)

                        output = (d_357_keyring_).MapFailure(lambda23_)
                        return output
                elif True:
                    d_359___mcc_h41_ = source10_.name
                    d_360___mcc_h42_ = source10_.encrypt
                    d_361___mcc_h43_ = source10_.decrypt
                    d_362___mcc_h44_ = source10_.bits
                    d_363___mcc_h45_ = source10_.algorithm
                    d_364___mcc_h46_ = source10_.encoding
                    d_365___mcc_h47_ = source10_.material
                    d_366___mcc_h48_ = source10_.keyIdentifier
                    d_367_keyIdentifier_ = d_366___mcc_h48_
                    d_368_material_ = d_365___mcc_h47_
                    d_369_encrypt_ = d_360___mcc_h42_
                    if True:
                        d_370_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_370_valueOrError14_ = Wrappers.default__.Need(d_369_encrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                        if (d_370_valueOrError14_).IsFailure():
                            output = (d_370_valueOrError14_).PropagateFailure()
                            return output
                        d_371_publicKeyPemBytes_: _dafny.Seq
                        d_372_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda24_(d_373_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_373_e_)

                        d_372_valueOrError15_ = (UTF8.default__.Encode(d_368_material_)).MapFailure(lambda24_)
                        if (d_372_valueOrError15_).IsFailure():
                            output = (d_372_valueOrError15_).PropagateFailure()
                            return output
                        d_371_publicKeyPemBytes_ = (d_372_valueOrError15_).Extract()
                        d_374_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_374_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_337_providerId_, d_367_keyIdentifier_, d_336_padding_, Wrappers.Option_Some(d_371_publicKeyPemBytes_), Wrappers.Option_None())
                        d_375_keyring_: Wrappers.Result
                        out8_: Wrappers.Result
                        out8_ = (mpl).CreateRawRsaKeyring(d_374_input_)
                        d_375_keyring_ = out8_
                        def lambda25_(d_376_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_376_e_)

                        output = (d_375_keyring_).MapFailure(lambda25_)
                        return output
        elif source4_.is_AES:
            d_377___mcc_h12_ = source4_.AES
            source11_ = d_377___mcc_h12_
            d_378___mcc_h13_ = source11_.keyId
            d_379___mcc_h14_ = source11_.providerId
            d_380_providerId_ = d_379___mcc_h14_
            d_381_key_ = d_378___mcc_h13_
            if True:
                d_382_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_382_valueOrError9_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_Symetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                if (d_382_valueOrError9_).IsFailure():
                    output = (d_382_valueOrError9_).PropagateFailure()
                    return output
                d_383_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                d_384_valueOrError10_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.default())()
                d_384_valueOrError10_ = (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (128) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (192) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (256) else Wrappers.Result_Failure(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not a supported bit length"))))))
                if (d_384_valueOrError10_).IsFailure():
                    output = (d_384_valueOrError10_).PropagateFailure()
                    return output
                d_383_wrappingAlg_ = (d_384_valueOrError10_).Extract()
                d_385_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput
                d_385_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_380_providerId_, ((d_303_material_).value).keyIdentifier, ((d_303_material_).value).wrappingKey, d_383_wrappingAlg_)
                d_386_keyring_: Wrappers.Result
                out9_: Wrappers.Result
                out9_ = (mpl).CreateRawAesKeyring(d_385_input_)
                d_386_keyring_ = out9_
                def lambda26_(d_387_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_387_e_)

                output = (d_386_keyring_).MapFailure(lambda26_)
                return output
        elif source4_.is_Static:
            d_388___mcc_h15_ = source4_.Static
            source12_ = d_388___mcc_h15_
            d_389___mcc_h16_ = source12_.keyId
            d_390_key_ = d_389___mcc_h16_
            if True:
                d_391_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_391_valueOrError0_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_StaticMaterial), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                if (d_391_valueOrError0_).IsFailure():
                    output = (d_391_valueOrError0_).PropagateFailure()
                    return output
                d_392_encrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
                d_392_encrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(((d_303_material_).value).algorithmSuite, ((d_303_material_).value).encryptionContext, ((d_303_material_).value).encryptedDataKeys, ((d_303_material_).value).requiredEncryptionContextKeys, ((d_303_material_).value).plaintextDataKey, ((d_303_material_).value).signingKey, ((d_303_material_).value).symmetricSigningKeys)
                d_393_decrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                d_393_decrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(((d_303_material_).value).algorithmSuite, ((d_303_material_).value).encryptionContext, ((d_303_material_).value).requiredEncryptionContextKeys, ((d_303_material_).value).plaintextDataKey, ((d_303_material_).value).verificationKey, Wrappers.Option_None())
                d_394_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out10_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out10_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_392_encrypt_, d_393_decrypt_)
                d_394_keyring_ = out10_
                output = Wrappers.Result_Success(d_394_keyring_)
                return output
        elif source4_.is_KmsRsa:
            d_395___mcc_h17_ = source4_.KmsRsa
            source13_ = d_395___mcc_h17_
            d_396___mcc_h18_ = source13_.keyId
            d_397___mcc_h19_ = source13_.encryptionAlgorithm
            d_398_encryptionAlgorithm_ = d_397___mcc_h19_
            d_399_key_ = d_396___mcc_h18_
            if True:
                d_400_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_400_valueOrError5_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMSAsymetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                if (d_400_valueOrError5_).IsFailure():
                    output = (d_400_valueOrError5_).PropagateFailure()
                    return output
                d_401_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_402_valueOrError6_: Wrappers.Result = None
                out11_: Wrappers.Result
                out11_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                d_402_valueOrError6_ = out11_
                if (d_402_valueOrError6_).IsFailure():
                    output = (d_402_valueOrError6_).PropagateFailure()
                    return output
                d_401_kmsClient_ = (d_402_valueOrError6_).Extract()
                d_403_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput
                d_403_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_303_material_).value).publicKey), ((d_303_material_).value).keyIdentifier, d_398_encryptionAlgorithm_, Wrappers.Option_Some(d_401_kmsClient_), Wrappers.Option_None())
                d_404_keyring_: Wrappers.Result
                out12_: Wrappers.Result
                out12_ = (mpl).CreateAwsKmsRsaKeyring(d_403_input_)
                d_404_keyring_ = out12_
                def lambda27_(d_405_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_405_e_)

                output = (d_404_keyring_).MapFailure(lambda27_)
                return output
        elif source4_.is_Hierarchy:
            d_406___mcc_h20_ = source4_.Hierarchy
            source14_ = d_406___mcc_h20_
            d_407___mcc_h21_ = source14_.keyId
            d_408_key_ = d_407___mcc_h21_
            if True:
                d_409_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_409_valueOrError7_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_StaticKeyStoreInformation), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                print(f"{d_409_valueOrError7_=}")
                if (d_409_valueOrError7_).IsFailure():
                    output = (d_409_valueOrError7_).PropagateFailure()
                    return output
                d_410_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out13_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out13_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_303_material_).value)
                print(f"{out13_=}")
                d_410_keyStore_ = out13_
                d_411_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput
                d_411_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_303_material_).value).keyIdentifier), Wrappers.Option_None(), d_410_keyStore_, 0, Wrappers.Option_None())
                d_412_keyring_: Wrappers.Result
                out14_: Wrappers.Result
                out14_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_411_input_)
                print(f"{out14_=}")
                d_412_keyring_ = out14_
                def lambda28_(d_413_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_413_e_)

                output = (d_412_keyring_).MapFailure(lambda28_)
                return output
        elif True:
            d_414___mcc_h22_ = source4_.Multi
            d_415_MultiKeyring_ = d_414___mcc_h22_
            if True:
                d_416_generator_: Wrappers.Option
                d_416_generator_ = Wrappers.Option_None()
                if ((d_415_MultiKeyring_).generator).is_Some:
                    d_417_valueOrError16_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_417_valueOrError16_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_415_MultiKeyring_).generator).value), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_417_valueOrError16_).IsFailure():
                        output = (d_417_valueOrError16_).PropagateFailure()
                        return output
                    d_418_generator_k_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                    d_419_valueOrError17_: Wrappers.Result = None
                    out15_: Wrappers.Result
                    out15_ = default__.ToKeyring(mpl, keys, ((d_415_MultiKeyring_).generator).value)
                    d_419_valueOrError17_ = out15_
                    if (d_419_valueOrError17_).IsFailure():
                        output = (d_419_valueOrError17_).PropagateFailure()
                        return output
                    d_418_generator_k_ = (d_419_valueOrError17_).Extract()
                    d_416_generator_ = Wrappers.Option_Some(d_418_generator_k_)
                d_420_childKeyrings_: _dafny.Seq
                d_420_childKeyrings_ = _dafny.Seq([])
                hi0_ = len((d_415_MultiKeyring_).childKeyrings)
                for d_421_i_ in range(0, hi0_):
                    d_422_child_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
                    d_422_child_ = ((d_415_MultiKeyring_).childKeyrings)[d_421_i_]
                    d_423_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_423_valueOrError18_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_422_child_), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_423_valueOrError18_).IsFailure():
                        output = (d_423_valueOrError18_).PropagateFailure()
                        return output
                    d_424_childKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                    d_425_valueOrError19_: Wrappers.Result = None
                    out16_: Wrappers.Result
                    out16_ = default__.ToKeyring(mpl, keys, d_422_child_)
                    d_425_valueOrError19_ = out16_
                    if (d_425_valueOrError19_).IsFailure():
                        output = (d_425_valueOrError19_).PropagateFailure()
                        return output
                    d_424_childKeyring_ = (d_425_valueOrError19_).Extract()
                    d_420_childKeyrings_ = (d_420_childKeyrings_) + (_dafny.Seq([d_424_childKeyring_]))
                d_426_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput
                d_426_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(d_416_generator_, d_420_childKeyrings_)
                d_427_keyring_: Wrappers.Result
                out17_: Wrappers.Result
                out17_ = (mpl).CreateMultiKeyring(d_426_input_)
                d_427_keyring_ = out17_
                def lambda29_(d_428_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_428_e_)

                output = (d_427_keyring_).MapFailure(lambda29_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_429_maybeClientSupplier_: Wrappers.Result
        out18_: Wrappers.Result
        out18_ = (mpl).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_429_maybeClientSupplier_ = out18_
        d_430_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_431_valueOrError0_: Wrappers.Result = None
        def lambda30_(d_432_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_432_e_)

        d_431_valueOrError0_ = (d_429_maybeClientSupplier_).MapFailure(lambda30_)
        if (d_431_valueOrError0_).IsFailure():
            output = (d_431_valueOrError0_).PropagateFailure()
            return output
        d_430_clientSupplier_ = (d_431_valueOrError0_).Extract()
        d_433_arn_: Wrappers.Result
        d_433_arn_ = AwsArnParsing.default__.IsAwsKmsIdentifierString(maybeKmsArn)
        d_434_region_: Wrappers.Option
        d_434_region_ = (AwsArnParsing.default__.GetRegion((d_433_arn_).value) if (d_433_arn_).is_Success else Wrappers.Option_None())
        d_435_tmp_: Wrappers.Result
        out19_: Wrappers.Result
        out19_ = (d_430_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_434_region_).UnwrapOr(_dafny.Seq(""))))
        d_435_tmp_ = out19_
        def lambda31_(d_436_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_436_e_)

        output = (d_435_tmp_).MapFailure(lambda31_)
        return output


class KeyringInfo:
    @classmethod
    def default(cls, ):
        return lambda: KeyringInfo_KeyringInfo(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyringInfo(self) -> bool:
        return isinstance(self, KeyringInfo_KeyringInfo)

class KeyringInfo_KeyringInfo(KeyringInfo, NamedTuple('KeyringInfo', [('description', Any), ('material', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyringFromKeyDescription.KeyringInfo.KeyringInfo({_dafny.string_of(self.description)}, {_dafny.string_of(self.material)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyringInfo_KeyringInfo) and self.description == __o.description and self.material == __o.material
    def __hash__(self) -> int:
        return super().__hash__()

