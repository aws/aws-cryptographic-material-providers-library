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
                    d_281___mcc_h0_ = source3_.Kms
                    d_282_i_ = d_281___mcc_h0_
                    return (d_282_i_).keyId
                elif source3_.is_KmsMrk:
                    d_283___mcc_h1_ = source3_.KmsMrk
                    d_284_i_ = d_283___mcc_h1_
                    return (d_284_i_).keyId
                elif source3_.is_KmsMrkDiscovery:
                    d_285___mcc_h2_ = source3_.KmsMrkDiscovery
                    d_286_i_ = d_285___mcc_h2_
                    return (d_286_i_).keyId
                elif source3_.is_RSA:
                    d_287___mcc_h3_ = source3_.RSA
                    d_288_i_ = d_287___mcc_h3_
                    return (d_288_i_).keyId
                elif source3_.is_AES:
                    d_289___mcc_h4_ = source3_.AES
                    d_290_i_ = d_289___mcc_h4_
                    return (d_290_i_).keyId
                elif source3_.is_Static:
                    d_291___mcc_h5_ = source3_.Static
                    d_292_i_ = d_291___mcc_h5_
                    return (d_292_i_).keyId
                elif source3_.is_KmsRsa:
                    d_293___mcc_h6_ = source3_.KmsRsa
                    d_294_i_ = d_293___mcc_h6_
                    return (d_294_i_).keyId
                elif source3_.is_Hierarchy:
                    d_295___mcc_h7_ = source3_.Hierarchy
                    d_296_i_ = d_295___mcc_h7_
                    return (d_296_i_).keyId
                elif source3_.is_Multi:
                    d_297___mcc_h8_ = source3_.Multi
                    return _dafny.Seq("")
                elif True:
                    d_298___mcc_h9_ = source3_.RequiredEncryptionContext
                    d_299_i_ = d_298___mcc_h9_
                    in2_ = (d_299_i_).underlying
                    input = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetKeyMaterial(keys, keyDescription):
        d_300_keyId_ = default__.GetKeyId(keyDescription)
        if (d_300_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_300_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ToKeyring(mpl, keys, description):
        output: Wrappers.Result = None
        d_301_material_: Wrappers.Option
        d_301_material_ = default__.GetKeyMaterial(keys, description)
        source4_ = description
        if source4_.is_Kms:
            d_302___mcc_h0_ = source4_.Kms
            source5_ = d_302___mcc_h0_
            d_303___mcc_h1_ = source5_.keyId
            d_304_key_ = d_303___mcc_h1_
            if True:
                d_305_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_305_valueOrError1_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_305_valueOrError1_).IsFailure():
                    output = (d_305_valueOrError1_).PropagateFailure()
                    return output
                d_306_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_307_valueOrError2_: Wrappers.Result = None
                out2_: Wrappers.Result
                out2_ = default__.getKmsClient(mpl, ((d_301_material_).value).keyIdentifier)
                d_307_valueOrError2_ = out2_
                if (d_307_valueOrError2_).IsFailure():
                    output = (d_307_valueOrError2_).PropagateFailure()
                    return output
                d_306_kmsClient_ = (d_307_valueOrError2_).Extract()
                d_308_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput
                d_308_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_301_material_).value).keyIdentifier, d_306_kmsClient_, Wrappers.Option_None())
                d_309_keyring_: Wrappers.Result
                out3_: Wrappers.Result
                out3_ = (mpl).CreateAwsKmsKeyring(d_308_input_)
                d_309_keyring_ = out3_
                def lambda19_(d_310_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_310_e_)

                output = (d_309_keyring_).MapFailure(lambda19_)
                return output
        elif source4_.is_KmsMrk:
            d_311___mcc_h2_ = source4_.KmsMrk
            source6_ = d_311___mcc_h2_
            d_312___mcc_h3_ = source6_.keyId
            d_313_key_ = d_312___mcc_h3_
            if True:
                d_314_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_314_valueOrError3_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_314_valueOrError3_).IsFailure():
                    output = (d_314_valueOrError3_).PropagateFailure()
                    return output
                d_315_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_316_valueOrError4_: Wrappers.Result = None
                out4_: Wrappers.Result
                out4_ = default__.getKmsClient(mpl, ((d_301_material_).value).keyIdentifier)
                d_316_valueOrError4_ = out4_
                if (d_316_valueOrError4_).IsFailure():
                    output = (d_316_valueOrError4_).PropagateFailure()
                    return output
                d_315_kmsClient_ = (d_316_valueOrError4_).Extract()
                d_317_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput
                d_317_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_301_material_).value).keyIdentifier, d_315_kmsClient_, Wrappers.Option_None())
                d_318_keyring_: Wrappers.Result
                out5_: Wrappers.Result
                out5_ = (mpl).CreateAwsKmsMrkKeyring(d_317_input_)
                d_318_keyring_ = out5_
                def lambda20_(d_319_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_319_e_)

                output = (d_318_keyring_).MapFailure(lambda20_)
                return output
        elif source4_.is_KmsMrkDiscovery:
            d_320___mcc_h4_ = source4_.KmsMrkDiscovery
            source7_ = d_320___mcc_h4_
            d_321___mcc_h5_ = source7_.keyId
            d_322___mcc_h6_ = source7_.defaultMrkRegion
            d_323___mcc_h7_ = source7_.awsKmsDiscoveryFilter
            d_324_awsKmsDiscoveryFilter_ = d_323___mcc_h7_
            d_325_defaultMrkRegion_ = d_322___mcc_h6_
            if True:
                d_326_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_326_valueOrError8_ = Wrappers.default__.Need((d_301_material_).is_None, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                if (d_326_valueOrError8_).IsFailure():
                    output = (d_326_valueOrError8_).PropagateFailure()
                    return output
                d_327_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                d_327_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_325_defaultMrkRegion_]), d_324_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                d_328_keyring_: Wrappers.Result
                out6_: Wrappers.Result
                out6_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_327_input_)
                d_328_keyring_ = out6_
                def lambda21_(d_329_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_329_e_)

                output = (d_328_keyring_).MapFailure(lambda21_)
                return output
        elif source4_.is_RSA:
            d_330___mcc_h8_ = source4_.RSA
            source8_ = d_330___mcc_h8_
            d_331___mcc_h9_ = source8_.keyId
            d_332___mcc_h10_ = source8_.providerId
            d_333___mcc_h11_ = source8_.padding
            d_334_padding_ = d_333___mcc_h11_
            d_335_providerId_ = d_332___mcc_h10_
            d_336_key_ = d_331___mcc_h9_
            if True:
                d_337_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_337_valueOrError11_ = Wrappers.default__.Need(((d_301_material_).is_Some) and ((((d_301_material_).value).is_PrivateRSA) or (((d_301_material_).value).is_PublicRSA)), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                if (d_337_valueOrError11_).IsFailure():
                    output = (d_337_valueOrError11_).PropagateFailure()
                    return output
                source9_ = d_301_material_
                d_338___mcc_h24_ = source9_.value
                source10_ = d_338___mcc_h24_
                if source10_.is_PrivateRSA:
                    d_339___mcc_h33_ = source10_.name
                    d_340___mcc_h34_ = source10_.encrypt
                    d_341___mcc_h35_ = source10_.decrypt
                    d_342___mcc_h36_ = source10_.algorithm
                    d_343___mcc_h37_ = source10_.bits
                    d_344___mcc_h38_ = source10_.encoding
                    d_345___mcc_h39_ = source10_.material
                    d_346___mcc_h40_ = source10_.keyIdentifier
                    d_347_keyIdentifier_ = d_346___mcc_h40_
                    d_348_material_ = d_345___mcc_h39_
                    d_349_decrypt_ = d_341___mcc_h35_
                    if True:
                        d_350_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_350_valueOrError12_ = Wrappers.default__.Need(d_349_decrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                        if (d_350_valueOrError12_).IsFailure():
                            output = (d_350_valueOrError12_).PropagateFailure()
                            return output
                        d_351_privateKeyPemBytes_: _dafny.Seq
                        d_352_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda22_(d_353_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_353_e_)

                        d_352_valueOrError13_ = (UTF8.default__.Encode(d_348_material_)).MapFailure(lambda22_)
                        if (d_352_valueOrError13_).IsFailure():
                            output = (d_352_valueOrError13_).PropagateFailure()
                            return output
                        d_351_privateKeyPemBytes_ = (d_352_valueOrError13_).Extract()
                        d_354_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_354_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_335_providerId_, d_347_keyIdentifier_, d_334_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_351_privateKeyPemBytes_))
                        d_355_keyring_: Wrappers.Result
                        out7_: Wrappers.Result
                        out7_ = (mpl).CreateRawRsaKeyring(d_354_input_)
                        d_355_keyring_ = out7_
                        def lambda23_(d_356_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_356_e_)

                        output = (d_355_keyring_).MapFailure(lambda23_)
                        return output
                elif True:
                    d_357___mcc_h41_ = source10_.name
                    d_358___mcc_h42_ = source10_.encrypt
                    d_359___mcc_h43_ = source10_.decrypt
                    d_360___mcc_h44_ = source10_.bits
                    d_361___mcc_h45_ = source10_.algorithm
                    d_362___mcc_h46_ = source10_.encoding
                    d_363___mcc_h47_ = source10_.material
                    d_364___mcc_h48_ = source10_.keyIdentifier
                    d_365_keyIdentifier_ = d_364___mcc_h48_
                    d_366_material_ = d_363___mcc_h47_
                    d_367_encrypt_ = d_358___mcc_h42_
                    if True:
                        d_368_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_368_valueOrError14_ = Wrappers.default__.Need(d_367_encrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                        if (d_368_valueOrError14_).IsFailure():
                            output = (d_368_valueOrError14_).PropagateFailure()
                            return output
                        d_369_publicKeyPemBytes_: _dafny.Seq
                        d_370_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda24_(d_371_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_371_e_)

                        d_370_valueOrError15_ = (UTF8.default__.Encode(d_366_material_)).MapFailure(lambda24_)
                        if (d_370_valueOrError15_).IsFailure():
                            output = (d_370_valueOrError15_).PropagateFailure()
                            return output
                        d_369_publicKeyPemBytes_ = (d_370_valueOrError15_).Extract()
                        d_372_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_372_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_335_providerId_, d_365_keyIdentifier_, d_334_padding_, Wrappers.Option_Some(d_369_publicKeyPemBytes_), Wrappers.Option_None())
                        d_373_keyring_: Wrappers.Result
                        out8_: Wrappers.Result
                        out8_ = (mpl).CreateRawRsaKeyring(d_372_input_)
                        d_373_keyring_ = out8_
                        def lambda25_(d_374_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_374_e_)

                        output = (d_373_keyring_).MapFailure(lambda25_)
                        return output
        elif source4_.is_AES:
            d_375___mcc_h12_ = source4_.AES
            source11_ = d_375___mcc_h12_
            d_376___mcc_h13_ = source11_.keyId
            d_377___mcc_h14_ = source11_.providerId
            d_378_providerId_ = d_377___mcc_h14_
            d_379_key_ = d_376___mcc_h13_
            if True:
                d_380_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_380_valueOrError9_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_Symetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                if (d_380_valueOrError9_).IsFailure():
                    output = (d_380_valueOrError9_).PropagateFailure()
                    return output
                d_381_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                d_382_valueOrError10_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.default())()
                d_382_valueOrError10_ = (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()) if (((d_301_material_).value).bits) == (128) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()) if (((d_301_material_).value).bits) == (192) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()) if (((d_301_material_).value).bits) == (256) else Wrappers.Result_Failure(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not a supported bit length"))))))
                if (d_382_valueOrError10_).IsFailure():
                    output = (d_382_valueOrError10_).PropagateFailure()
                    return output
                d_381_wrappingAlg_ = (d_382_valueOrError10_).Extract()
                d_383_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput
                d_383_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_378_providerId_, ((d_301_material_).value).keyIdentifier, ((d_301_material_).value).wrappingKey, d_381_wrappingAlg_)
                d_384_keyring_: Wrappers.Result
                out9_: Wrappers.Result
                out9_ = (mpl).CreateRawAesKeyring(d_383_input_)
                d_384_keyring_ = out9_
                def lambda26_(d_385_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_385_e_)

                output = (d_384_keyring_).MapFailure(lambda26_)
                return output
        elif source4_.is_Static:
            d_386___mcc_h15_ = source4_.Static
            source12_ = d_386___mcc_h15_
            d_387___mcc_h16_ = source12_.keyId
            d_388_key_ = d_387___mcc_h16_
            if True:
                d_389_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_389_valueOrError0_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_StaticMaterial), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                if (d_389_valueOrError0_).IsFailure():
                    output = (d_389_valueOrError0_).PropagateFailure()
                    return output
                d_390_encrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
                d_390_encrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(((d_301_material_).value).algorithmSuite, ((d_301_material_).value).encryptionContext, ((d_301_material_).value).encryptedDataKeys, ((d_301_material_).value).requiredEncryptionContextKeys, ((d_301_material_).value).plaintextDataKey, ((d_301_material_).value).signingKey, ((d_301_material_).value).symmetricSigningKeys)
                d_391_decrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                d_391_decrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(((d_301_material_).value).algorithmSuite, ((d_301_material_).value).encryptionContext, ((d_301_material_).value).requiredEncryptionContextKeys, ((d_301_material_).value).plaintextDataKey, ((d_301_material_).value).verificationKey, Wrappers.Option_None())
                d_392_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out10_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out10_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_390_encrypt_, d_391_decrypt_)
                d_392_keyring_ = out10_
                output = Wrappers.Result_Success(d_392_keyring_)
                return output
        elif source4_.is_KmsRsa:
            d_393___mcc_h17_ = source4_.KmsRsa
            source13_ = d_393___mcc_h17_
            d_394___mcc_h18_ = source13_.keyId
            d_395___mcc_h19_ = source13_.encryptionAlgorithm
            d_396_encryptionAlgorithm_ = d_395___mcc_h19_
            d_397_key_ = d_394___mcc_h18_
            if True:
                d_398_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_398_valueOrError5_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_KMSAsymetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                if (d_398_valueOrError5_).IsFailure():
                    output = (d_398_valueOrError5_).PropagateFailure()
                    return output
                d_399_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_400_valueOrError6_: Wrappers.Result = None
                out11_: Wrappers.Result
                out11_ = default__.getKmsClient(mpl, ((d_301_material_).value).keyIdentifier)
                d_400_valueOrError6_ = out11_
                if (d_400_valueOrError6_).IsFailure():
                    output = (d_400_valueOrError6_).PropagateFailure()
                    return output
                d_399_kmsClient_ = (d_400_valueOrError6_).Extract()
                d_401_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput
                d_401_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_301_material_).value).publicKey), ((d_301_material_).value).keyIdentifier, d_396_encryptionAlgorithm_, Wrappers.Option_Some(d_399_kmsClient_), Wrappers.Option_None())
                d_402_keyring_: Wrappers.Result
                out12_: Wrappers.Result
                out12_ = (mpl).CreateAwsKmsRsaKeyring(d_401_input_)
                d_402_keyring_ = out12_
                def lambda27_(d_403_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_403_e_)

                output = (d_402_keyring_).MapFailure(lambda27_)
                return output
        elif source4_.is_Hierarchy:
            d_404___mcc_h20_ = source4_.Hierarchy
            source14_ = d_404___mcc_h20_
            d_405___mcc_h21_ = source14_.keyId
            d_406_key_ = d_405___mcc_h21_
            if True:
                d_407_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_407_valueOrError7_ = Wrappers.default__.Need(((d_301_material_).is_Some) and (((d_301_material_).value).is_StaticKeyStoreInformation), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                if (d_407_valueOrError7_).IsFailure():
                    output = (d_407_valueOrError7_).PropagateFailure()
                    return output
                d_408_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out13_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out13_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_301_material_).value)
                d_408_keyStore_ = out13_
                d_409_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput
                d_409_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_301_material_).value).keyIdentifier), Wrappers.Option_None(), d_408_keyStore_, 0, Wrappers.Option_None())
                d_410_keyring_: Wrappers.Result
                out14_: Wrappers.Result
                out14_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_409_input_)
                d_410_keyring_ = out14_
                def lambda28_(d_411_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_411_e_)

                output = (d_410_keyring_).MapFailure(lambda28_)
                return output
        elif True:
            d_412___mcc_h22_ = source4_.Multi
            d_413_MultiKeyring_ = d_412___mcc_h22_
            if True:
                d_414_generator_: Wrappers.Option
                d_414_generator_ = Wrappers.Option_None()
                if ((d_413_MultiKeyring_).generator).is_Some:
                    d_415_valueOrError16_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_415_valueOrError16_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_413_MultiKeyring_).generator).value), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_415_valueOrError16_).IsFailure():
                        output = (d_415_valueOrError16_).PropagateFailure()
                        return output
                    d_416_generator_k_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                    d_417_valueOrError17_: Wrappers.Result = None
                    out15_: Wrappers.Result
                    out15_ = default__.ToKeyring(mpl, keys, ((d_413_MultiKeyring_).generator).value)
                    d_417_valueOrError17_ = out15_
                    if (d_417_valueOrError17_).IsFailure():
                        output = (d_417_valueOrError17_).PropagateFailure()
                        return output
                    d_416_generator_k_ = (d_417_valueOrError17_).Extract()
                    d_414_generator_ = Wrappers.Option_Some(d_416_generator_k_)
                d_418_childKeyrings_: _dafny.Seq
                d_418_childKeyrings_ = _dafny.Seq([])
                hi0_ = len((d_413_MultiKeyring_).childKeyrings)
                for d_419_i_ in range(0, hi0_):
                    d_420_child_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
                    d_420_child_ = ((d_413_MultiKeyring_).childKeyrings)[d_419_i_]
                    d_421_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_421_valueOrError18_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_420_child_), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_421_valueOrError18_).IsFailure():
                        output = (d_421_valueOrError18_).PropagateFailure()
                        return output
                    d_422_childKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                    d_423_valueOrError19_: Wrappers.Result = None
                    out16_: Wrappers.Result
                    out16_ = default__.ToKeyring(mpl, keys, d_420_child_)
                    d_423_valueOrError19_ = out16_
                    if (d_423_valueOrError19_).IsFailure():
                        output = (d_423_valueOrError19_).PropagateFailure()
                        return output
                    d_422_childKeyring_ = (d_423_valueOrError19_).Extract()
                    d_418_childKeyrings_ = (d_418_childKeyrings_) + (_dafny.Seq([d_422_childKeyring_]))
                d_424_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput
                d_424_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput(d_414_generator_, d_418_childKeyrings_)
                d_425_keyring_: Wrappers.Result
                out17_: Wrappers.Result
                out17_ = (mpl).CreateMultiKeyring(d_424_input_)
                d_425_keyring_ = out17_
                def lambda29_(d_426_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_426_e_)

                output = (d_425_keyring_).MapFailure(lambda29_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_427_maybeClientSupplier_: Wrappers.Result
        out18_: Wrappers.Result
        out18_ = (mpl).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_427_maybeClientSupplier_ = out18_
        d_428_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_429_valueOrError0_: Wrappers.Result = None
        def lambda30_(d_430_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_430_e_)

        d_429_valueOrError0_ = (d_427_maybeClientSupplier_).MapFailure(lambda30_)
        if (d_429_valueOrError0_).IsFailure():
            output = (d_429_valueOrError0_).PropagateFailure()
            return output
        d_428_clientSupplier_ = (d_429_valueOrError0_).Extract()
        d_431_arn_: Wrappers.Result
        d_431_arn_ = AwsArnParsing.default__.IsAwsKmsIdentifierString(maybeKmsArn)
        d_432_region_: Wrappers.Option
        d_432_region_ = (AwsArnParsing.default__.GetRegion((d_431_arn_).value) if (d_431_arn_).is_Success else Wrappers.Option_None())
        d_433_tmp_: Wrappers.Result
        out19_: Wrappers.Result
        out19_ = (d_428_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_432_region_).UnwrapOr(_dafny.Seq(""))))
        d_433_tmp_ = out19_
        def lambda31_(d_434_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_434_e_)

        output = (d_433_tmp_).MapFailure(lambda31_)
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

