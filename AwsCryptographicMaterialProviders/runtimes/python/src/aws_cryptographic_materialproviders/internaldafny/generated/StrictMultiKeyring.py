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

# Module: aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrictMultiKeyring(generator, awsKmsKeys, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        pat_let_tv153_ = awsKmsKeys
        pat_let_tv154_ = awsKmsKeys
        d_596_allStrings_: _dafny.Seq
        def lambda57_(source19_):
            if source19_.is_None:
                return (pat_let_tv153_).UnwrapOr(_dafny.Seq([]))
            elif True:
                d_597___mcc_h0_ = source19_.value
                d_598_g_ = d_597___mcc_h0_
                return (_dafny.Seq([d_598_g_])) + ((pat_let_tv154_).UnwrapOr(_dafny.Seq([])))

        d_596_allStrings_ = lambda57_(generator)
        d_599_allIdentifiers_: _dafny.Seq
        d_600_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_600_valueOrError0_ = (Seq.default__.MapWithResult(AwsArnParsing.default__.IsAwsKmsIdentifierString, d_596_allStrings_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_600_valueOrError0_).IsFailure():
            output = (d_600_valueOrError0_).PropagateFailure()
            return output
        d_599_allIdentifiers_ = (d_600_valueOrError0_).Extract()
        d_601_generatorKeyring_: Wrappers.Option = Wrappers.Option.default()()
        source20_ = generator
        if source20_.is_None:
            d_601_generatorKeyring_ = Wrappers.Option_None()
        elif True:
            d_602___mcc_h1_ = source20_.value
            d_603_generatorIdentifier_ = d_602___mcc_h1_
            d_604_arn_: AwsArnParsing.AwsKmsIdentifier
            d_605_valueOrError1_: Wrappers.Result = None
            d_605_valueOrError1_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_603_generatorIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
            if (d_605_valueOrError1_).IsFailure():
                output = (d_605_valueOrError1_).PropagateFailure()
                return output
            d_604_arn_ = (d_605_valueOrError1_).Extract()
            d_606_region_: Wrappers.Option
            d_606_region_ = AwsArnParsing.default__.GetRegion(d_604_arn_)
            d_607_client_: ComAmazonawsKmsTypes.IKMSClient
            d_608_valueOrError2_: Wrappers.Result = None
            out90_: Wrappers.Result
            out90_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_606_region_).UnwrapOr(_dafny.Seq(""))))
            d_608_valueOrError2_ = out90_
            if (d_608_valueOrError2_).IsFailure():
                output = (d_608_valueOrError2_).PropagateFailure()
                return output
            d_607_client_ = (d_608_valueOrError2_).Extract()
            d_609_g_: AwsKmsKeyring.AwsKmsKeyring
            nw6_ = AwsKmsKeyring.AwsKmsKeyring()
            nw6_.ctor__(d_607_client_, d_603_generatorIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_609_g_ = nw6_
            d_601_generatorKeyring_ = Wrappers.Option_Some(d_609_g_)
        d_610_children_: _dafny.Seq
        d_610_children_ = _dafny.Seq([])
        source21_ = awsKmsKeys
        if source21_.is_None:
            d_610_children_ = _dafny.Seq([])
        elif True:
            d_611___mcc_h2_ = source21_.value
            d_612_childIdentifiers_ = d_611___mcc_h2_
            hi2_ = len(d_612_childIdentifiers_)
            for d_613_index_ in range(0, hi2_):
                d_614_childIdentifier_: _dafny.Seq
                d_614_childIdentifier_ = (d_612_childIdentifiers_)[d_613_index_]
                d_615_info_: AwsArnParsing.AwsKmsIdentifier
                d_616_valueOrError3_: Wrappers.Result = None
                d_616_valueOrError3_ = (AwsArnParsing.default__.IsAwsKmsIdentifierString(d_614_childIdentifier_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
                if (d_616_valueOrError3_).IsFailure():
                    output = (d_616_valueOrError3_).PropagateFailure()
                    return output
                d_615_info_ = (d_616_valueOrError3_).Extract()
                d_617_region_: Wrappers.Option
                d_617_region_ = AwsArnParsing.default__.GetRegion(d_615_info_)
                d_618_client_: ComAmazonawsKmsTypes.IKMSClient
                d_619_valueOrError4_: Wrappers.Result = None
                out91_: Wrappers.Result
                out91_ = (clientSupplier).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_617_region_).UnwrapOr(_dafny.Seq(""))))
                d_619_valueOrError4_ = out91_
                if (d_619_valueOrError4_).IsFailure():
                    output = (d_619_valueOrError4_).PropagateFailure()
                    return output
                d_618_client_ = (d_619_valueOrError4_).Extract()
                d_620_keyring_: AwsKmsKeyring.AwsKmsKeyring
                nw7_ = AwsKmsKeyring.AwsKmsKeyring()
                nw7_.ctor__(d_618_client_, d_614_childIdentifier_, (grantTokens).UnwrapOr(_dafny.Seq([])))
                d_620_keyring_ = nw7_
                d_610_children_ = (d_610_children_) + (_dafny.Seq([d_620_keyring_]))
        d_621_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_621_valueOrError5_ = Wrappers.default__.Need(((d_601_generatorKeyring_).is_Some) or ((len(d_610_children_)) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("generatorKeyring or child Keryings needed to create a multi keyring")))
        if (d_621_valueOrError5_).IsFailure():
            output = (d_621_valueOrError5_).PropagateFailure()
            return output
        d_622_keyring_: MultiKeyring.MultiKeyring
        nw8_ = MultiKeyring.MultiKeyring()
        nw8_.ctor__(d_601_generatorKeyring_, d_610_children_)
        d_622_keyring_ = nw8_
        output = Wrappers.Result_Success(d_622_keyring_)
        return output
        return output

