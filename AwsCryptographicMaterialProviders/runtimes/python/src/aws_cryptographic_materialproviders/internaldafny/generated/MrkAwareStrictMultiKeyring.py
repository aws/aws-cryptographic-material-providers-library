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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring

# Module: aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MrkAwareStrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv159_ = awsKmsKeys
        pat_let_tv160_ = awsKmsKeys
        d_749_allStrings_: _dafny.Seq
        def lambda65_(source26_):
            if source26_.is_None:
                return (pat_let_tv159_).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_750___mcc_h0_ = source26_.value
                d_751_g_ = d_750___mcc_h0_
                return (_dafny.Seq([d_751_g_])) + ((pat_let_tv160_).UnwrapOr(_dafny.Seq([])))

        d_749_allStrings_ = lambda65_(generator)
        d_752_allIdentifiers_: _dafny.Seq
        d_753_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_753_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_749_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_753_valueOrError0_).IsFailure():
            output = (d_753_valueOrError0_).PropagateFailure()
            return output
        d_752_allIdentifiers_ = (d_753_valueOrError0_).Extract()
        d_754_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_754_valueOrError1_ = AwsKmsMrkAreUnique.default__.AwsKmsMrkAreUnique(d_752_allIdentifiers_)
        if (d_754_valueOrError1_).IsFailure():
            output = (d_754_valueOrError1_).PropagateFailure()
            return output
        d_755_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source27_ = generator
        if source27_.is_None:
            d_755_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_756___mcc_h1_ = source27_.value
            d_757_generatorIdentifier_ = d_756___mcc_h1_
            d_758_arn_: AwsArnParsing.AwsKmsIdentifier
            d_759_valueOrError2_: Wrappers.Result = None
            d_759_valueOrError2_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_757_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_759_valueOrError2_).IsFailure():
                output = (d_759_valueOrError2_).PropagateFailure()
                return output
            d_758_arn_ = (d_759_valueOrError2_).Extract()
            d_760_region_: Wrappers.Option
            d_760_region_ = AwsArnParsing.default__.GetRegion(d_758_arn_)
            d_761_client_: ComAmazonawsKmsTypes.IKMSClient
            d_762_valueOrError3_: Wrappers.Result = None
            out111_: Wrappers.Result
            out111_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_760_region_).UnwrapOr(_dafny.Seq(""))))
            d_762_valueOrError3_ = out111_
            if (d_762_valueOrError3_).IsFailure():
                output = (d_762_valueOrError3_).PropagateFailure()
                return output
            d_761_client_ = (d_762_valueOrError3_).Extract()
            d_763_g_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
            nw25_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
            nw25_.ctor__(d_761_client_, d_757_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_763_g_ = nw25_
            d_755_generatorKeyring_ = Wrappers.Option_Some(d_763_g_)
        d_764_children_: _dafny.Seq
        d_764_children_ = _dafny.Seq([])
        source28_ = awsKmsKeys
        if source28_.is_None:
            d_764_children_ = _dafny.Seq([])
        elif True:
            d_765___mcc_h2_ = source28_.value
            d_766_childIdentifiers_ = d_765___mcc_h2_
            hi5_ = len(d_766_childIdentifiers_)
            for d_767_index_ in range(0, hi5_):
                d_768_childIdentifier_: _dafny.Seq
                d_768_childIdentifier_ = (d_766_childIdentifiers_)[d_767_index_]
                d_769_info_: AwsArnParsing.AwsKmsIdentifier
                d_770_valueOrError4_: Wrappers.Result = None
                d_770_valueOrError4_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_768_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_770_valueOrError4_).IsFailure():
                    output = (d_770_valueOrError4_).PropagateFailure()
                    return output
                d_769_info_ = (d_770_valueOrError4_).Extract()
                d_771_region_: Wrappers.Option
                d_771_region_ = AwsArnParsing.default__.GetRegion(d_769_info_)
                d_772_client_: ComAmazonawsKmsTypes.IKMSClient
                d_773_valueOrError5_: Wrappers.Result = None
                out112_: Wrappers.Result
                out112_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_771_region_).UnwrapOr(_dafny.Seq(""))))
                d_773_valueOrError5_ = out112_
                if (d_773_valueOrError5_).IsFailure():
                    output = (d_773_valueOrError5_).PropagateFailure()
                    return output
                d_772_client_ = (d_773_valueOrError5_).Extract()
                d_774_keyring_: AwsKmsMrkKeyring.AwsKmsMrkKeyring
                nw26_ = AwsKmsMrkKeyring.AwsKmsMrkKeyring()
                nw26_.ctor__(d_772_client_, d_768_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_774_keyring_ = nw26_
                d_764_children_ = (d_764_children_) + (_dafny.Seq([d_774_keyring_]))
        d_775_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_775_valueOrError6_ = Wrappers.default__.Need(((d_755_generatorKeyring_).is_Some) or ((len(d_764_children_)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keyrings needed to create a multi keyring")))
        if (d_775_valueOrError6_).IsFailure():
            output = (d_775_valueOrError6_).PropagateFailure()
            return output
        d_776_keyring_: MultiKeyring.MultiKeyring
        nw27_ = MultiKeyring.MultiKeyring()
        nw27_.ctor__(d_755_generatorKeyring_, d_764_children_)
        d_776_keyring_ = nw27_
        output = Wrappers.Result_Success(d_776_keyring_)
        return output
        return output

