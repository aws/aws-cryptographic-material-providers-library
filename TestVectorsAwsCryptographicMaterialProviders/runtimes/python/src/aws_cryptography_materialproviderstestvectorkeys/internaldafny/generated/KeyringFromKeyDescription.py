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

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription

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
        source4_ = description
        if source4_.is_Kms:
            d_304___mcc_h0_ = source4_.Kms
            source5_ = d_304___mcc_h0_
            d_305___mcc_h1_ = source5_.keyId
            d_306_key_ = d_305___mcc_h1_
            if True:
                d_307_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_307_valueOrError1_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_307_valueOrError1_).IsFailure():
                    output = (d_307_valueOrError1_).PropagateFailure()
                    return output
                d_308_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                d_309_valueOrError2_: Wrappers.Result = None
                out2_: Wrappers.Result
                out2_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                d_309_valueOrError2_ = out2_
                if (d_309_valueOrError2_).IsFailure():
                    output = (d_309_valueOrError2_).PropagateFailure()
                    return output
                d_308_kmsClient_ = (d_309_valueOrError2_).Extract()
                d_310_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput
                d_310_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_303_material_).value).keyIdentifier, d_308_kmsClient_, Wrappers.Option_None())
                d_311_keyring_: Wrappers.Result
                out3_: Wrappers.Result
                out3_ = (mpl).CreateAwsKmsKeyring(d_310_input_)
                d_311_keyring_ = out3_
                def lambda19_(d_312_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_312_e_)

                output = (d_311_keyring_).MapFailure(lambda19_)
                return output
        elif source4_.is_KmsMrk:
            d_313___mcc_h2_ = source4_.KmsMrk
            source6_ = d_313___mcc_h2_
            d_314___mcc_h3_ = source6_.keyId
            d_315_key_ = d_314___mcc_h3_
            if True:
                d_316_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_316_valueOrError3_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                if (d_316_valueOrError3_).IsFailure():
                    output = (d_316_valueOrError3_).PropagateFailure()
                    return output
                d_317_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                d_318_valueOrError4_: Wrappers.Result = None
                out4_: Wrappers.Result
                out4_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                d_318_valueOrError4_ = out4_
                if (d_318_valueOrError4_).IsFailure():
                    output = (d_318_valueOrError4_).PropagateFailure()
                    return output
                d_317_kmsClient_ = (d_318_valueOrError4_).Extract()
                d_319_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput
                d_319_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_303_material_).value).keyIdentifier, d_317_kmsClient_, Wrappers.Option_None())
                d_320_keyring_: Wrappers.Result
                out5_: Wrappers.Result
                out5_ = (mpl).CreateAwsKmsMrkKeyring(d_319_input_)
                d_320_keyring_ = out5_
                def lambda20_(d_321_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_321_e_)

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
                d_328_valueOrError8_ = Wrappers.default__.Need((d_303_material_).is_None, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                if (d_328_valueOrError8_).IsFailure():
                    output = (d_328_valueOrError8_).PropagateFailure()
                    return output
                d_329_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                d_329_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_327_defaultMrkRegion_]), d_326_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                d_330_keyring_: Wrappers.Result
                out6_: Wrappers.Result
                out6_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_329_input_)
                d_330_keyring_ = out6_
                def lambda21_(d_331_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_331_e_)

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
                d_339_valueOrError11_ = Wrappers.default__.Need(((d_303_material_).is_Some) and ((((d_303_material_).value).is_PrivateRSA) or (((d_303_material_).value).is_PublicRSA)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
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
                        d_352_valueOrError12_ = Wrappers.default__.Need(d_351_decrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                        if (d_352_valueOrError12_).IsFailure():
                            output = (d_352_valueOrError12_).PropagateFailure()
                            return output
                        d_353_privateKeyPemBytes_: _dafny.Seq
                        d_354_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda22_(d_355_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_355_e_)

                        d_354_valueOrError13_ = (UTF8.default__.Encode(d_350_material_)).MapFailure(lambda22_)
                        if (d_354_valueOrError13_).IsFailure():
                            output = (d_354_valueOrError13_).PropagateFailure()
                            return output
                        d_353_privateKeyPemBytes_ = (d_354_valueOrError13_).Extract()
                        d_356_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                        d_356_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_337_providerId_, d_349_keyIdentifier_, d_336_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_353_privateKeyPemBytes_))
                        d_357_keyring_: Wrappers.Result
                        out7_: Wrappers.Result
                        out7_ = (mpl).CreateRawRsaKeyring(d_356_input_)
                        d_357_keyring_ = out7_
                        def lambda23_(d_358_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_358_e_)

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
                        d_370_valueOrError14_ = Wrappers.default__.Need(d_369_encrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                        if (d_370_valueOrError14_).IsFailure():
                            output = (d_370_valueOrError14_).PropagateFailure()
                            return output
                        d_371_publicKeyPemBytes_: _dafny.Seq
                        d_372_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                        def lambda24_(d_373_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_373_e_)

                        d_372_valueOrError15_ = (UTF8.default__.Encode(d_368_material_)).MapFailure(lambda24_)
                        if (d_372_valueOrError15_).IsFailure():
                            output = (d_372_valueOrError15_).PropagateFailure()
                            return output
                        d_371_publicKeyPemBytes_ = (d_372_valueOrError15_).Extract()
                        d_374_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                        d_374_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_337_providerId_, d_367_keyIdentifier_, d_336_padding_, Wrappers.Option_Some(d_371_publicKeyPemBytes_), Wrappers.Option_None())
                        d_375_keyring_: Wrappers.Result
                        out8_: Wrappers.Result
                        out8_ = (mpl).CreateRawRsaKeyring(d_374_input_)
                        d_375_keyring_ = out8_
                        def lambda25_(d_376_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_376_e_)

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
                d_382_valueOrError9_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_Symetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                if (d_382_valueOrError9_).IsFailure():
                    output = (d_382_valueOrError9_).PropagateFailure()
                    return output
                d_383_wrappingAlg_: AwsCryptographyMaterialProvidersTypes.AesWrappingAlg
                d_384_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.default())()
                d_384_valueOrError10_ = (Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (128) else (Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (192) else (Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()) if (((d_303_material_).value).bits) == (256) else Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a supported bit length"))))))
                if (d_384_valueOrError10_).IsFailure():
                    output = (d_384_valueOrError10_).PropagateFailure()
                    return output
                d_383_wrappingAlg_ = (d_384_valueOrError10_).Extract()
                d_385_input_: AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput
                d_385_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_380_providerId_, ((d_303_material_).value).keyIdentifier, ((d_303_material_).value).wrappingKey, d_383_wrappingAlg_)
                d_386_keyring_: Wrappers.Result
                out9_: Wrappers.Result
                out9_ = (mpl).CreateRawAesKeyring(d_385_input_)
                d_386_keyring_ = out9_
                def lambda26_(d_387_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_387_e_)

                output = (d_386_keyring_).MapFailure(lambda26_)
                return output
        elif source4_.is_Static:
            d_388___mcc_h15_ = source4_.Static
            source12_ = d_388___mcc_h15_
            d_389___mcc_h16_ = source12_.keyId
            d_390_key_ = d_389___mcc_h16_
            if True:
                d_391_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_391_valueOrError0_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_StaticMaterial), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                if (d_391_valueOrError0_).IsFailure():
                    output = (d_391_valueOrError0_).PropagateFailure()
                    return output
                d_392_encrypt_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
                d_392_encrypt_ = AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(((d_303_material_).value).algorithmSuite, ((d_303_material_).value).encryptionContext, ((d_303_material_).value).encryptedDataKeys, ((d_303_material_).value).requiredEncryptionContextKeys, ((d_303_material_).value).plaintextDataKey, ((d_303_material_).value).signingKey, ((d_303_material_).value).symmetricSigningKeys)
                d_393_decrypt_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                d_393_decrypt_ = AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(((d_303_material_).value).algorithmSuite, ((d_303_material_).value).encryptionContext, ((d_303_material_).value).requiredEncryptionContextKeys, ((d_303_material_).value).plaintextDataKey, ((d_303_material_).value).verificationKey, Wrappers.Option_None())
                d_394_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                out10_: AwsCryptographyMaterialProvidersTypes.IKeyring
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
                d_400_valueOrError5_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_KMSAsymetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                if (d_400_valueOrError5_).IsFailure():
                    output = (d_400_valueOrError5_).PropagateFailure()
                    return output
                d_401_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                d_402_valueOrError6_: Wrappers.Result = None
                out11_: Wrappers.Result
                out11_ = default__.getKmsClient(mpl, ((d_303_material_).value).keyIdentifier)
                d_402_valueOrError6_ = out11_
                if (d_402_valueOrError6_).IsFailure():
                    output = (d_402_valueOrError6_).PropagateFailure()
                    return output
                d_401_kmsClient_ = (d_402_valueOrError6_).Extract()
                d_403_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput
                d_403_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_303_material_).value).publicKey), ((d_303_material_).value).keyIdentifier, d_398_encryptionAlgorithm_, Wrappers.Option_Some(d_401_kmsClient_), Wrappers.Option_None())
                d_404_keyring_: Wrappers.Result
                out12_: Wrappers.Result
                out12_ = (mpl).CreateAwsKmsRsaKeyring(d_403_input_)
                d_404_keyring_ = out12_
                def lambda27_(d_405_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_405_e_)

                output = (d_404_keyring_).MapFailure(lambda27_)
                return output
        elif source4_.is_Hierarchy:
            d_406___mcc_h20_ = source4_.Hierarchy
            source14_ = d_406___mcc_h20_
            d_407___mcc_h21_ = source14_.keyId
            d_408_key_ = d_407___mcc_h21_
            if True:
                d_409_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                d_409_valueOrError7_ = Wrappers.default__.Need(((d_303_material_).is_Some) and (((d_303_material_).value).is_StaticKeyStoreInformation), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                if (d_409_valueOrError7_).IsFailure():
                    output = (d_409_valueOrError7_).PropagateFailure()
                    return output
                d_410_keyStore_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                out13_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                out13_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_303_material_).value)
                d_410_keyStore_ = out13_
                d_411_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput
                d_411_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_303_material_).value).keyIdentifier), Wrappers.Option_None(), d_410_keyStore_, 0, Wrappers.Option_None())
                d_412_keyring_: Wrappers.Result
                out14_: Wrappers.Result
                out14_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_411_input_)
                d_412_keyring_ = out14_
                def lambda28_(d_413_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_413_e_)

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
                    d_417_valueOrError16_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_415_MultiKeyring_).generator).value), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_417_valueOrError16_).IsFailure():
                        output = (d_417_valueOrError16_).PropagateFailure()
                        return output
                    d_418_generator_k_: AwsCryptographyMaterialProvidersTypes.IKeyring
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
                    d_422_child_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    d_422_child_ = ((d_415_MultiKeyring_).childKeyrings)[d_421_i_]
                    d_423_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_423_valueOrError18_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_422_child_), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_423_valueOrError18_).IsFailure():
                        output = (d_423_valueOrError18_).PropagateFailure()
                        return output
                    d_424_childKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    d_425_valueOrError19_: Wrappers.Result = None
                    out16_: Wrappers.Result
                    out16_ = default__.ToKeyring(mpl, keys, d_422_child_)
                    d_425_valueOrError19_ = out16_
                    if (d_425_valueOrError19_).IsFailure():
                        output = (d_425_valueOrError19_).PropagateFailure()
                        return output
                    d_424_childKeyring_ = (d_425_valueOrError19_).Extract()
                    d_420_childKeyrings_ = (d_420_childKeyrings_) + (_dafny.Seq([d_424_childKeyring_]))
                d_426_input_: AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput
                d_426_input_ = AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(d_416_generator_, d_420_childKeyrings_)
                d_427_keyring_: Wrappers.Result
                out17_: Wrappers.Result
                out17_ = (mpl).CreateMultiKeyring(d_426_input_)
                d_427_keyring_ = out17_
                def lambda29_(d_428_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_428_e_)

                output = (d_427_keyring_).MapFailure(lambda29_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_429_maybeClientSupplier_: Wrappers.Result
        out18_: Wrappers.Result
        out18_ = (mpl).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_429_maybeClientSupplier_ = out18_
        d_430_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_431_valueOrError0_: Wrappers.Result = None
        def lambda30_(d_432_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_432_e_)

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
        out19_ = (d_430_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_434_region_).UnwrapOr(_dafny.Seq(""))))
        d_435_tmp_ = out19_
        def lambda31_(d_436_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_436_e_)

        output = (d_435_tmp_).MapFailure(lambda31_)
        return output


class KeyringInfo:
    @classmethod
    def default(cls, ):
        return lambda: KeyringInfo_KeyringInfo(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.default()(), Wrappers.Option.default()())
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

