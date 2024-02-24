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
    def ToKeyring(mpl, info):
        output: Wrappers.Result = None
        let_tmp_rhs4_ = info
        d_299_description_ = let_tmp_rhs4_.description
        d_300_material_ = let_tmp_rhs4_.material
        source3_ = d_299_description_
        if source3_.is_Kms:
            d_301___mcc_h0_ = source3_.Kms
            source4_ = d_301___mcc_h0_
            d_302___mcc_h1_ = source4_.keyId
            d_303_key_ = d_302___mcc_h1_
            if True:
                d_304_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_304_valueOrError1_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_304_valueOrError1_).IsFailure():
                    output = (d_304_valueOrError1_).PropagateFailure()
                    return output
                d_305_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_306_valueOrError2_: Wrappers.Result = None
                out47_: Wrappers.Result
                out47_ = default__.getKmsClient(mpl, ((d_300_material_).value).keyIdentifier)
                d_306_valueOrError2_ = out47_
                if (d_306_valueOrError2_).IsFailure():
                    output = (d_306_valueOrError2_).PropagateFailure()
                    return output
                d_305_kmsClient_ = (d_306_valueOrError2_).Extract()
                d_307_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput
                d_307_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_300_material_).value).keyIdentifier, d_305_kmsClient_, Wrappers.Option_None())
                d_308_keyring_: Wrappers.Result
                out48_: Wrappers.Result
                out48_ = (mpl).CreateAwsKmsKeyring(d_307_input_)
                d_308_keyring_ = out48_
                def lambda10_(d_309_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_309_e_)

                output = (d_308_keyring_).MapFailure(lambda10_)
                return output
        elif source3_.is_KmsMrk:
            d_310___mcc_h2_ = source3_.KmsMrk
            source5_ = d_310___mcc_h2_
            d_311___mcc_h3_ = source5_.keyId
            d_312_key_ = d_311___mcc_h3_
            if True:
                d_313_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_313_valueOrError3_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_KMS), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_313_valueOrError3_).IsFailure():
                    output = (d_313_valueOrError3_).PropagateFailure()
                    return output
                d_314_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_315_valueOrError4_: Wrappers.Result = None
                out49_: Wrappers.Result
                out49_ = default__.getKmsClient(mpl, ((d_300_material_).value).keyIdentifier)
                d_315_valueOrError4_ = out49_
                if (d_315_valueOrError4_).IsFailure():
                    output = (d_315_valueOrError4_).PropagateFailure()
                    return output
                d_314_kmsClient_ = (d_315_valueOrError4_).Extract()
                d_316_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput
                d_316_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_300_material_).value).keyIdentifier, d_314_kmsClient_, Wrappers.Option_None())
                d_317_keyring_: Wrappers.Result
                out50_: Wrappers.Result
                out50_ = (mpl).CreateAwsKmsMrkKeyring(d_316_input_)
                d_317_keyring_ = out50_
                def lambda11_(d_318_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_318_e_)

                output = (d_317_keyring_).MapFailure(lambda11_)
                return output
        elif source3_.is_KmsMrkDiscovery:
            d_319___mcc_h4_ = source3_.KmsMrkDiscovery
            source6_ = d_319___mcc_h4_
            d_320___mcc_h5_ = source6_.keyId
            d_321___mcc_h6_ = source6_.defaultMrkRegion
            d_322___mcc_h7_ = source6_.awsKmsDiscoveryFilter
            d_323_awsKmsDiscoveryFilter_ = d_322___mcc_h7_
            d_324_defaultMrkRegion_ = d_321___mcc_h6_
            if True:
                d_325_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_325_valueOrError8_ = Wrappers.default__.Need((d_300_material_).is_None, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                if (d_325_valueOrError8_).IsFailure():
                    output = (d_325_valueOrError8_).PropagateFailure()
                    return output
                d_326_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                d_326_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_324_defaultMrkRegion_]), d_323_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                d_327_keyring_: Wrappers.Result
                out51_: Wrappers.Result
                out51_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_326_input_)
                d_327_keyring_ = out51_
                def lambda12_(d_328_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_328_e_)

                output = (d_327_keyring_).MapFailure(lambda12_)
                return output
        elif source3_.is_RSA:
            d_329___mcc_h8_ = source3_.RSA
            source7_ = d_329___mcc_h8_
            d_330___mcc_h9_ = source7_.keyId
            d_331___mcc_h10_ = source7_.providerId
            d_332___mcc_h11_ = source7_.padding
            d_333_padding_ = d_332___mcc_h11_
            d_334_providerId_ = d_331___mcc_h10_
            d_335_key_ = d_330___mcc_h9_
            if True:
                d_336_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_336_valueOrError11_ = Wrappers.default__.Need(((d_300_material_).is_Some) and ((((d_300_material_).value).is_PrivateRSA) or (((d_300_material_).value).is_PublicRSA)), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                if (d_336_valueOrError11_).IsFailure():
                    output = (d_336_valueOrError11_).PropagateFailure()
                    return output
                source8_ = d_300_material_
                d_337___mcc_h22_ = source8_.value
                source9_ = d_337___mcc_h22_
                if source9_.is_PrivateRSA:
                    d_338___mcc_h31_ = source9_.name
                    d_339___mcc_h32_ = source9_.encrypt
                    d_340___mcc_h33_ = source9_.decrypt
                    d_341___mcc_h34_ = source9_.algorithm
                    d_342___mcc_h35_ = source9_.bits
                    d_343___mcc_h36_ = source9_.encoding
                    d_344___mcc_h37_ = source9_.material
                    d_345___mcc_h38_ = source9_.keyIdentifier
                    d_346_keyIdentifier_ = d_345___mcc_h38_
                    d_347_material_ = d_344___mcc_h37_
                    d_348_decrypt_ = d_340___mcc_h33_
                    if True:
                        d_349_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_349_valueOrError12_ = Wrappers.default__.Need(d_348_decrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                        if (d_349_valueOrError12_).IsFailure():
                            output = (d_349_valueOrError12_).PropagateFailure()
                            return output
                        d_350_privateKeyPemBytes_: _dafny.Seq
                        d_351_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda13_(d_352_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_352_e_)

                        d_351_valueOrError13_ = (UTF8.default__.Encode(d_347_material_)).MapFailure(lambda13_)
                        if (d_351_valueOrError13_).IsFailure():
                            output = (d_351_valueOrError13_).PropagateFailure()
                            return output
                        d_350_privateKeyPemBytes_ = (d_351_valueOrError13_).Extract()
                        d_353_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_353_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_334_providerId_, d_346_keyIdentifier_, d_333_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_350_privateKeyPemBytes_))
                        d_354_keyring_: Wrappers.Result
                        out52_: Wrappers.Result
                        out52_ = (mpl).CreateRawRsaKeyring(d_353_input_)
                        d_354_keyring_ = out52_
                        def lambda14_(d_355_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_355_e_)

                        output = (d_354_keyring_).MapFailure(lambda14_)
                        return output
                elif True:
                    d_356___mcc_h39_ = source9_.name
                    d_357___mcc_h40_ = source9_.encrypt
                    d_358___mcc_h41_ = source9_.decrypt
                    d_359___mcc_h42_ = source9_.bits
                    d_360___mcc_h43_ = source9_.algorithm
                    d_361___mcc_h44_ = source9_.encoding
                    d_362___mcc_h45_ = source9_.material
                    d_363___mcc_h46_ = source9_.keyIdentifier
                    d_364_keyIdentifier_ = d_363___mcc_h46_
                    d_365_material_ = d_362___mcc_h45_
                    d_366_encrypt_ = d_357___mcc_h40_
                    if True:
                        d_367_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_367_valueOrError14_ = Wrappers.default__.Need(d_366_encrypt_, software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                        if (d_367_valueOrError14_).IsFailure():
                            output = (d_367_valueOrError14_).PropagateFailure()
                            return output
                        d_368_publicKeyPemBytes_: _dafny.Seq
                        d_369_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda15_(d_370_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_370_e_)

                        d_369_valueOrError15_ = (UTF8.default__.Encode(d_365_material_)).MapFailure(lambda15_)
                        if (d_369_valueOrError15_).IsFailure():
                            output = (d_369_valueOrError15_).PropagateFailure()
                            return output
                        d_368_publicKeyPemBytes_ = (d_369_valueOrError15_).Extract()
                        d_371_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput
                        d_371_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_334_providerId_, d_364_keyIdentifier_, d_333_padding_, Wrappers.Option_Some(d_368_publicKeyPemBytes_), Wrappers.Option_None())
                        d_372_keyring_: Wrappers.Result
                        out53_: Wrappers.Result
                        out53_ = (mpl).CreateRawRsaKeyring(d_371_input_)
                        d_372_keyring_ = out53_
                        def lambda16_(d_373_e_):
                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_373_e_)

                        output = (d_372_keyring_).MapFailure(lambda16_)
                        return output
        elif source3_.is_AES:
            d_374___mcc_h12_ = source3_.AES
            source10_ = d_374___mcc_h12_
            d_375___mcc_h13_ = source10_.keyId
            d_376___mcc_h14_ = source10_.providerId
            d_377_providerId_ = d_376___mcc_h14_
            d_378_key_ = d_375___mcc_h13_
            if True:
                d_379_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_379_valueOrError9_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_Symetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: Symetric")))
                if (d_379_valueOrError9_).IsFailure():
                    output = (d_379_valueOrError9_).PropagateFailure()
                    return output
                d_380_wrappingAlg_: software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg
                d_381_valueOrError10_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg.default())()
                d_381_valueOrError10_ = (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()) if (((d_300_material_).value).bits) == (128) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()) if (((d_300_material_).value).bits) == (192) else (Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()) if (((d_300_material_).value).bits) == (256) else Wrappers.Result_Failure(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not a supported bit length"))))))
                if (d_381_valueOrError10_).IsFailure():
                    output = (d_381_valueOrError10_).PropagateFailure()
                    return output
                d_380_wrappingAlg_ = (d_381_valueOrError10_).Extract()
                d_382_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput
                d_382_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_377_providerId_, ((d_300_material_).value).keyIdentifier, ((d_300_material_).value).wrappingKey, d_380_wrappingAlg_)
                d_383_keyring_: Wrappers.Result
                out54_: Wrappers.Result
                out54_ = (mpl).CreateRawAesKeyring(d_382_input_)
                d_383_keyring_ = out54_
                def lambda17_(d_384_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_384_e_)

                output = (d_383_keyring_).MapFailure(lambda17_)
                return output
        elif source3_.is_Static:
            d_385___mcc_h15_ = source3_.Static
            source11_ = d_385___mcc_h15_
            d_386___mcc_h16_ = source11_.keyId
            d_387_key_ = d_386___mcc_h16_
            if True:
                d_388_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_388_valueOrError0_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_StaticMaterial), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                if (d_388_valueOrError0_).IsFailure():
                    output = (d_388_valueOrError0_).PropagateFailure()
                    return output
                d_389_encrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
                d_389_encrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(((d_300_material_).value).algorithmSuite, ((d_300_material_).value).encryptionContext, ((d_300_material_).value).encryptedDataKeys, ((d_300_material_).value).requiredEncryptionContextKeys, ((d_300_material_).value).plaintextDataKey, ((d_300_material_).value).signingKey, ((d_300_material_).value).symmetricSigningKeys)
                d_390_decrypt_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                d_390_decrypt_ = software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(((d_300_material_).value).algorithmSuite, ((d_300_material_).value).encryptionContext, ((d_300_material_).value).requiredEncryptionContextKeys, ((d_300_material_).value).plaintextDataKey, ((d_300_material_).value).verificationKey, Wrappers.Option_None())
                d_391_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out55_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
                out55_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_389_encrypt_, d_390_decrypt_)
                d_391_keyring_ = out55_
                output = Wrappers.Result_Success(d_391_keyring_)
                return output
        elif source3_.is_KmsRsa:
            d_392___mcc_h17_ = source3_.KmsRsa
            source12_ = d_392___mcc_h17_
            d_393___mcc_h18_ = source12_.keyId
            d_394___mcc_h19_ = source12_.encryptionAlgorithm
            d_395_encryptionAlgorithm_ = d_394___mcc_h19_
            d_396_key_ = d_393___mcc_h18_
            if True:
                d_397_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_397_valueOrError5_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_KMSAsymetric), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                if (d_397_valueOrError5_).IsFailure():
                    output = (d_397_valueOrError5_).PropagateFailure()
                    return output
                d_398_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
                d_399_valueOrError6_: Wrappers.Result = None
                out56_: Wrappers.Result
                out56_ = default__.getKmsClient(mpl, ((d_300_material_).value).keyIdentifier)
                d_399_valueOrError6_ = out56_
                if (d_399_valueOrError6_).IsFailure():
                    output = (d_399_valueOrError6_).PropagateFailure()
                    return output
                d_398_kmsClient_ = (d_399_valueOrError6_).Extract()
                d_400_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput
                d_400_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_300_material_).value).publicKey), ((d_300_material_).value).keyIdentifier, d_395_encryptionAlgorithm_, Wrappers.Option_Some(d_398_kmsClient_), Wrappers.Option_None())
                d_401_keyring_: Wrappers.Result
                out57_: Wrappers.Result
                out57_ = (mpl).CreateAwsKmsRsaKeyring(d_400_input_)
                d_401_keyring_ = out57_
                def lambda18_(d_402_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_402_e_)

                output = (d_401_keyring_).MapFailure(lambda18_)
                return output
        elif True:
            d_403___mcc_h20_ = source3_.Hierarchy
            source13_ = d_403___mcc_h20_
            d_404___mcc_h21_ = source13_.keyId
            d_405_key_ = d_404___mcc_h21_
            if True:
                d_406_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_406_valueOrError7_ = Wrappers.default__.Need(((d_300_material_).is_Some) and (((d_300_material_).value).is_StaticKeyStoreInformation), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                if (d_406_valueOrError7_).IsFailure():
                    output = (d_406_valueOrError7_).PropagateFailure()
                    return output
                d_407_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out58_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
                out58_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_300_material_).value)
                d_407_keyStore_ = out58_
                d_408_input_: software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput
                d_408_input_ = software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_300_material_).value).keyIdentifier), Wrappers.Option_None(), d_407_keyStore_, 0, Wrappers.Option_None())
                d_409_keyring_: Wrappers.Result
                out59_: Wrappers.Result
                out59_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_408_input_)
                d_409_keyring_ = out59_
                def lambda19_(d_410_e_):
                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_410_e_)

                output = (d_409_keyring_).MapFailure(lambda19_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_411_maybeClientSupplier_: Wrappers.Result
        out60_: Wrappers.Result
        out60_ = (mpl).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_411_maybeClientSupplier_ = out60_
        d_412_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_413_valueOrError0_: Wrappers.Result = None
        def lambda20_(d_414_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_414_e_)

        d_413_valueOrError0_ = (d_411_maybeClientSupplier_).MapFailure(lambda20_)
        if (d_413_valueOrError0_).IsFailure():
            output = (d_413_valueOrError0_).PropagateFailure()
            return output
        d_412_clientSupplier_ = (d_413_valueOrError0_).Extract()
        d_415_arn_: AwsArnParsing.AwsArn
        d_416_valueOrError1_: Wrappers.Result = None
        def lambda21_(d_417_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(d_417_e_)

        d_416_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(maybeKmsArn)).MapFailure(lambda21_)
        if (d_416_valueOrError1_).IsFailure():
            output = (d_416_valueOrError1_).PropagateFailure()
            return output
        d_415_arn_ = (d_416_valueOrError1_).Extract()
        d_418_tmp_: Wrappers.Result
        out61_: Wrappers.Result
        out61_ = (d_412_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput((d_415_arn_).region))
        d_418_tmp_ = out61_
        def lambda22_(d_419_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_419_e_)

        output = (d_418_tmp_).MapFailure(lambda22_)
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

