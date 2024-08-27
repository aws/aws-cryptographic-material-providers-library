import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
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
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring

# Module: MrkAwareStrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareStrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv169_ = awsKmsKeys
        pat_let_tv170_ = awsKmsKeys
        d_783_allStrings_: _dafny.Seq
        def lambda72_():
            source27_ = generator
            unmatched27 = True
            if unmatched27:
                if source27_.is_Some:
                    d_784_g_ = source27_.value
                    unmatched27 = False
                    return (_dafny.Seq([d_784_g_])) + ((pat_let_tv169_).UnwrapOr(_dafny.Seq([])))
            if unmatched27:
                unmatched27 = False
                return (pat_let_tv170_).UnwrapOr(_dafny.Seq([]))
            raise Exception("unexpected control point")

        d_783_allStrings_ = lambda72_()
        d_785_allIdentifiers_: _dafny.Seq
        d_786_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_786_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_783_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_786_valueOrError0_).IsFailure():
            output = (d_786_valueOrError0_).PropagateFailure()
            return output
        d_785_allIdentifiers_ = (d_786_valueOrError0_).Extract()
        d_787_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_787_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_785_allIdentifiers_)
        if (d_787_valueOrError1_).IsFailure():
            output = (d_787_valueOrError1_).PropagateFailure()
            return output
        d_788_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source28_ = generator
        unmatched28 = True
        if unmatched28:
            if source28_.is_Some:
                d_789_generatorIdentifier_ = source28_.value
                unmatched28 = False
                d_790_arn_: AwsArnParsing.AwsKmsIdentifier
                d_791_valueOrError2_: Wrappers.Result = None
                d_791_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_789_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_791_valueOrError2_).IsFailure():
                    output = (d_791_valueOrError2_).PropagateFailure()
                    return output
                d_790_arn_ = (d_791_valueOrError2_).Extract()
                d_792_region_: Wrappers.Option
                d_792_region_ = AwsArnParsing.default__.GetRegion(d_790_arn_)
                d_793_client_: ComAmazonawsKmsTypes.IKMSClient
                d_794_valueOrError3_: Wrappers.Result = None
                out116_: Wrappers.Result
                out116_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_792_region_).UnwrapOr(_dafny.Seq(""))))
                d_794_valueOrError3_ = out116_
                if (d_794_valueOrError3_).IsFailure():
                    output = (d_794_valueOrError3_).PropagateFailure()
                    return output
                d_793_client_ = (d_794_valueOrError3_).Extract()
                d_795_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw25_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw25_.ctor__(d_793_client_, d_789_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_795_g_ = nw25_
                d_788_generatorKeyring_ = Wrappers.Option_Some(d_795_g_)
        if unmatched28:
            unmatched28 = False
            d_788_generatorKeyring_ = Wrappers.Option_None()
        d_796_children_: _dafny.Seq
        d_796_children_ = _dafny.Seq([])
        source29_ = awsKmsKeys
        unmatched29 = True
        if unmatched29:
            if source29_.is_Some:
                d_797_childIdentifiers_ = source29_.value
                unmatched29 = False
                hi5_ = len(d_797_childIdentifiers_)
                for d_798_index_ in range(0, hi5_):
                    d_799_childIdentifier_: _dafny.Seq
                    d_799_childIdentifier_ = (d_797_childIdentifiers_)[d_798_index_]
                    d_800_info_: AwsArnParsing.AwsKmsIdentifier
                    d_801_valueOrError4_: Wrappers.Result = None
                    d_801_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_799_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                    if (d_801_valueOrError4_).IsFailure():
                        output = (d_801_valueOrError4_).PropagateFailure()
                        return output
                    d_800_info_ = (d_801_valueOrError4_).Extract()
                    d_802_region_: Wrappers.Option
                    d_802_region_ = AwsArnParsing.default__.GetRegion(d_800_info_)
                    d_803_client_: ComAmazonawsKmsTypes.IKMSClient
                    d_804_valueOrError5_: Wrappers.Result = None
                    out117_: Wrappers.Result
                    out117_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_802_region_).UnwrapOr(_dafny.Seq(""))))
                    d_804_valueOrError5_ = out117_
                    if (d_804_valueOrError5_).IsFailure():
                        output = (d_804_valueOrError5_).PropagateFailure()
                        return output
                    d_803_client_ = (d_804_valueOrError5_).Extract()
                    d_805_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                    nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                    nw26_.ctor__(d_803_client_, d_799_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                    d_805_keyring_ = nw26_
                    d_796_children_ = (d_796_children_) + (_dafny.Seq([d_805_keyring_]))
        if unmatched29:
            unmatched29 = False
            d_796_children_ = _dafny.Seq([])
        d_806_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_806_valueOrError6_ = Wrappers.default__.Need(((d_788_generatorKeyring_).is_Some) or ((len(d_796_children_)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_806_valueOrError6_).IsFailure():
            output = (d_806_valueOrError6_).PropagateFailure()
            return output
        d_807_keyring_: MultiKeyring.MultiKeyring
        nw27_ = MultiKeyring.MultiKeyring()
        nw27_.ctor__(d_788_generatorKeyring_, d_796_children_)
        d_807_keyring_ = nw27_
        output = Wrappers.Result_Success(d_807_keyring_)
        return output
        return output
