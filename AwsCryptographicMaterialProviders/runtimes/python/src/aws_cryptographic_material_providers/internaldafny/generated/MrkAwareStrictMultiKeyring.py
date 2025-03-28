import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
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
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
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

# Module: MrkAwareStrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareStrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_0_allStrings_: _dafny.Seq
        source0_ = generator
        with _dafny.label("match0"):
            if True:
                if source0_.is_Some:
                    d_1_g_ = source0_.value
                    d_0_allStrings_ = (_dafny.Seq([d_1_g_])) + ((awsKmsKeys).UnwrapOr(_dafny.Seq([])))
                    raise _dafny.Break("match0")
            if True:
                d_0_allStrings_ = (awsKmsKeys).UnwrapOr(_dafny.Seq([]))
            pass
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_0_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        d_3_allIdentifiers_: _dafny.Seq
        d_3_allIdentifiers_ = (d_2_valueOrError0_).Extract()
        d_4_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_3_allIdentifiers_)
        if (d_4_valueOrError1_).IsFailure():
            output = (d_4_valueOrError1_).PropagateFailure()
            return output
        d_5_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source1_ = generator
        with _dafny.label("match1"):
            if True:
                if source1_.is_Some:
                    d_6_generatorIdentifier_ = source1_.value
                    d_7_valueOrError2_: Wrappers.Result = None
                    d_7_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_6_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                    if (d_7_valueOrError2_).IsFailure():
                        output = (d_7_valueOrError2_).PropagateFailure()
                        return output
                    d_8_arn_: AwsArnParsing.AwsKmsIdentifier
                    d_8_arn_ = (d_7_valueOrError2_).Extract()
                    d_9_region_: Wrappers.Option
                    d_9_region_ = AwsArnParsing.default__.GetRegion(d_8_arn_)
                    d_10_valueOrError3_: Wrappers.Result = None
                    out0_: Wrappers.Result
                    out0_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_9_region_).UnwrapOr(_dafny.Seq(""))))
                    d_10_valueOrError3_ = out0_
                    if (d_10_valueOrError3_).IsFailure():
                        output = (d_10_valueOrError3_).PropagateFailure()
                        return output
                    d_11_client_: ComAmazonawsKmsTypes.IKMSClient
                    d_11_client_ = (d_10_valueOrError3_).Extract()
                    d_12_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                    nw0_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                    nw0_.ctor__(d_11_client_, d_6_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                    d_12_g_ = nw0_
                    d_5_generatorKeyring_ = Wrappers.Option_Some(d_12_g_)
                    raise _dafny.Break("match1")
            if True:
                d_5_generatorKeyring_ = Wrappers.Option_None()
            pass
        d_13_children_: _dafny.Seq
        d_13_children_ = _dafny.Seq([])
        source2_ = awsKmsKeys
        with _dafny.label("match2"):
            if True:
                if source2_.is_Some:
                    d_14_childIdentifiers_ = source2_.value
                    hi0_ = len(d_14_childIdentifiers_)
                    for d_15_index_ in range(0, hi0_):
                        d_16_childIdentifier_: _dafny.Seq
                        d_16_childIdentifier_ = (d_14_childIdentifiers_)[d_15_index_]
                        d_17_valueOrError4_: Wrappers.Result = None
                        d_17_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_16_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                        if (d_17_valueOrError4_).IsFailure():
                            output = (d_17_valueOrError4_).PropagateFailure()
                            return output
                        d_18_info_: AwsArnParsing.AwsKmsIdentifier
                        d_18_info_ = (d_17_valueOrError4_).Extract()
                        d_19_region_: Wrappers.Option
                        d_19_region_ = AwsArnParsing.default__.GetRegion(d_18_info_)
                        d_20_valueOrError5_: Wrappers.Result = None
                        out1_: Wrappers.Result
                        out1_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_19_region_).UnwrapOr(_dafny.Seq(""))))
                        d_20_valueOrError5_ = out1_
                        if (d_20_valueOrError5_).IsFailure():
                            output = (d_20_valueOrError5_).PropagateFailure()
                            return output
                        d_21_client_: ComAmazonawsKmsTypes.IKMSClient
                        d_21_client_ = (d_20_valueOrError5_).Extract()
                        d_22_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                        nw1_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                        nw1_.ctor__(d_21_client_, d_16_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                        d_22_keyring_ = nw1_
                        d_13_children_ = (d_13_children_) + (_dafny.Seq([d_22_keyring_]))
                    raise _dafny.Break("match2")
            if True:
                d_13_children_ = _dafny.Seq([])
            pass
        d_23_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_23_valueOrError6_ = Wrappers.default__.Need(((d_5_generatorKeyring_).is_Some) or ((len(d_13_children_)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_23_valueOrError6_).IsFailure():
            output = (d_23_valueOrError6_).PropagateFailure()
            return output
        d_24_keyring_: MultiKeyring.MultiKeyring
        nw2_ = MultiKeyring.MultiKeyring()
        nw2_.ctor__(d_5_generatorKeyring_, d_13_children_)
        d_24_keyring_ = nw2_
        output = Wrappers.Result_Success(d_24_keyring_)
        return output
        return output

