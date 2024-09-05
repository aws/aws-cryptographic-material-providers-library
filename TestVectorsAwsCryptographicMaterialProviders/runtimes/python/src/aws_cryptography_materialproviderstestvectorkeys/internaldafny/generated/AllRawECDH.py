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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestVectors as TestVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllHierarchy as AllHierarchy
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKms as AllKms
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAware as AllKmsMrkAware
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAwareDiscovery as AllKmsMrkAwareDiscovery
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsRsa as AllKmsRsa
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsEcdh as AllKmsEcdh
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA

# Module: AllRawECDH

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def ecdhCurveNames(instance):
        return _dafny.Seq([_dafny.Seq("ecc-256"), _dafny.Seq("ecc-384"), _dafny.Seq("ecc-521")])
    @_dafny.classproperty
    def EphemeralKeyDescriptionsEncrypt(instance):
        def iife59_():
            coll27_ = _dafny.Set()
            compr_51_: _dafny.Seq
            for compr_51_ in (default__.ecdhCurveNames).Elements:
                d_645_key_: _dafny.Seq = compr_51_
                if (d_645_key_) in (default__.ecdhCurveNames):
                    coll27_ = coll27_.union(_dafny.Set([AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh(_dafny.Seq("ephemeral"), (d_645_key_) + (_dafny.Seq("-private")), _dafny.Seq("ephemeral"), _dafny.Seq("recipient-material-public-key"), (_dafny.Seq("aws-raw-vectors-persistent-ephemeral ")) + (d_645_key_), d_645_key_, _dafny.Seq("ephemeral")))]))
            return _dafny.Set(coll27_)
        return iife59_()
        
    @_dafny.classproperty
    def DiscoveryKeyDescriptionsDecrypt(instance):
        def iife60_():
            coll28_ = _dafny.Set()
            compr_52_: _dafny.Seq
            for compr_52_ in (default__.ecdhCurveNames).Elements:
                d_646_key_: _dafny.Seq = compr_52_
                if (d_646_key_) in (default__.ecdhCurveNames):
                    coll28_ = coll28_.union(_dafny.Set([AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh(_dafny.Seq("discovery"), (d_646_key_) + (_dafny.Seq("-private")), _dafny.Seq("discovery"), _dafny.Seq("recipient-material-public-key"), (_dafny.Seq("aws-raw-vectors-persistent-discovery ")) + (d_646_key_), d_646_key_, _dafny.Seq("discovery")))]))
            return _dafny.Set(coll28_)
        return iife60_()
        
    @_dafny.classproperty
    def SenderKeyDescriptions(instance):
        def iife61_():
            coll29_ = _dafny.Set()
            compr_53_: _dafny.Seq
            for compr_53_ in (default__.ecdhCurveNames).Elements:
                d_647_key_: _dafny.Seq = compr_53_
                if (d_647_key_) in (default__.ecdhCurveNames):
                    coll29_ = coll29_.union(_dafny.Set([AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh((d_647_key_) + (_dafny.Seq("-private")), (d_647_key_) + (_dafny.Seq("-private")), _dafny.Seq("sender-material-public-key"), _dafny.Seq("recipient-material-public-key"), (_dafny.Seq("aws-raw-vectors-persistent-static ")) + (d_647_key_), d_647_key_, _dafny.Seq("static")))]))
            return _dafny.Set(coll29_)
        return iife61_()
        
    @_dafny.classproperty
    def RecipientKeyDescriptions(instance):
        def iife62_():
            coll30_ = _dafny.Set()
            compr_54_: _dafny.Seq
            for compr_54_ in (default__.ecdhCurveNames).Elements:
                d_648_key_: _dafny.Seq = compr_54_
                if (d_648_key_) in (default__.ecdhCurveNames):
                    coll30_ = coll30_.union(_dafny.Set([AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh((d_648_key_) + (_dafny.Seq("-private")), (d_648_key_) + (_dafny.Seq("-private")), _dafny.Seq("sender-material-public-key"), _dafny.Seq("recipient-material-public-key"), (_dafny.Seq("aws-raw-vectors-persistent-static ")) + (d_648_key_), d_648_key_, _dafny.Seq("static")))]))
            return _dafny.Set(coll30_)
        return iife62_()
        
    @_dafny.classproperty
    def EphemeralDiscoveryTests(instance):
        def iife63_():
            coll31_ = _dafny.Set()
            compr_55_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
            for compr_55_ in (default__.EphemeralKeyDescriptionsEncrypt).Elements:
                d_649_encryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_55_
                if (d_649_encryptKeyDescription_) in (default__.EphemeralKeyDescriptionsEncrypt):
                    compr_56_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    for compr_56_ in (default__.DiscoveryKeyDescriptionsDecrypt).Elements:
                        d_650_decryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_56_
                        if ((d_650_decryptKeyDescription_) in (default__.DiscoveryKeyDescriptionsDecrypt)) and ((((d_650_decryptKeyDescription_).ECDH).curveSpec) == (((d_649_encryptKeyDescription_).ECDH).curveSpec)):
                            compr_57_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
                            for compr_57_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                                d_651_algorithmSuite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = compr_57_
                                if (d_651_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites):
                                    compr_58_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
                                    for compr_58_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_651_algorithmSuite_)]:
                                        d_652_commitmentPolicy_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy = compr_58_
                                        if (d_652_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_651_algorithmSuite_)):
                                            coll31_ = coll31_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((((_dafny.Seq("Generated RawECDH Ephemeral-Discovery ")) + (((d_649_encryptKeyDescription_).ECDH).senderKeyId)) + (_dafny.Seq(" "))) + (((d_650_decryptKeyDescription_).ECDH).recipientKeyId), Wrappers.Option_None(), _dafny.Map({}), d_652_commitmentPolicy_, d_651_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_649_encryptKeyDescription_, d_650_decryptKeyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll31_)
        return iife63_()
        
    @_dafny.classproperty
    def StaticSenderDiscoveryRecipientTests(instance):
        def iife64_():
            coll32_ = _dafny.Set()
            compr_59_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
            for compr_59_ in (default__.SenderKeyDescriptions).Elements:
                d_653_encryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_59_
                if (d_653_encryptKeyDescription_) in (default__.SenderKeyDescriptions):
                    compr_60_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    for compr_60_ in (default__.DiscoveryKeyDescriptionsDecrypt).Elements:
                        d_654_decryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_60_
                        if ((d_654_decryptKeyDescription_) in (default__.DiscoveryKeyDescriptionsDecrypt)) and ((((d_654_decryptKeyDescription_).ECDH).curveSpec) == (((d_653_encryptKeyDescription_).ECDH).curveSpec)):
                            compr_61_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
                            for compr_61_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                                d_655_algorithmSuite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = compr_61_
                                if (d_655_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites):
                                    compr_62_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
                                    for compr_62_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_655_algorithmSuite_)]:
                                        d_656_commitmentPolicy_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy = compr_62_
                                        if (d_656_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_655_algorithmSuite_)):
                                            coll32_ = coll32_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((((_dafny.Seq("Generated RawECDH Static ")) + (((d_653_encryptKeyDescription_).ECDH).senderKeyId)) + (_dafny.Seq(" Discovery "))) + (((d_654_decryptKeyDescription_).ECDH).recipientKeyId), Wrappers.Option_None(), _dafny.Map({}), d_656_commitmentPolicy_, d_655_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_653_encryptKeyDescription_, d_654_decryptKeyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll32_)
        return iife64_()
        
    @_dafny.classproperty
    def StaticSenderRecipientTests(instance):
        def iife65_():
            coll33_ = _dafny.Set()
            compr_63_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
            for compr_63_ in (default__.SenderKeyDescriptions).Elements:
                d_657_encryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_63_
                if (d_657_encryptKeyDescription_) in (default__.SenderKeyDescriptions):
                    compr_64_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    for compr_64_ in (default__.RecipientKeyDescriptions).Elements:
                        d_658_decryptKeyDescription_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = compr_64_
                        if ((d_658_decryptKeyDescription_) in (default__.RecipientKeyDescriptions)) and ((((d_658_decryptKeyDescription_).ECDH).curveSpec) == (((d_657_encryptKeyDescription_).ECDH).curveSpec)):
                            compr_65_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
                            for compr_65_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                                d_659_algorithmSuite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = compr_65_
                                if (d_659_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites):
                                    compr_66_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy
                                    for compr_66_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_659_algorithmSuite_)]:
                                        d_660_commitmentPolicy_: AwsCryptographyMaterialProvidersTypes.CommitmentPolicy = compr_66_
                                        if (d_660_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_659_algorithmSuite_)):
                                            coll33_ = coll33_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((((_dafny.Seq("Generated RawECDH Static ")) + (((d_657_encryptKeyDescription_).ECDH).senderKeyId)) + (_dafny.Seq(" "))) + (((d_658_decryptKeyDescription_).ECDH).senderKeyId), Wrappers.Option_None(), _dafny.Map({}), d_660_commitmentPolicy_, d_659_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_657_encryptKeyDescription_, d_658_decryptKeyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll33_)
        return iife65_()
        
    @_dafny.classproperty
    def Tests(instance):
        return ((default__.EphemeralDiscoveryTests) | (default__.StaticSenderRecipientTests)) | (default__.StaticSenderDiscoveryRecipientTests)
