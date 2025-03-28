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

# Module: AwsArnParsing

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ValidAwsKmsResource(resource):
        return ((resource).Valid()) and ((((resource).resourceType) == (_dafny.Seq("key"))) or (((resource).resourceType) == (_dafny.Seq("alias"))))

    @staticmethod
    def ValidAwsKmsArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("kms")))) and (default__.ValidAwsKmsResource((arn).resource))

    @staticmethod
    def ParseAwsKmsRawResources(identifier):
        d_0_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_1_valueOrError0_ = Wrappers.default__.Need(((d_0_info_)[0]) != (_dafny.Seq("key")), (_dafny.Seq("Malformed raw key id: ")) + (identifier))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif (len(d_0_info_)) == (1):
            return default__.ParseAwsKmsResources((_dafny.Seq("key/")) + (identifier))
        elif True:
            return default__.ParseAwsKmsResources(identifier)

    @staticmethod
    def ParseAwsKmsResources(identifier):
        d_0_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_1_valueOrError0_ = Wrappers.default__.Need((len(d_0_info_)) > (1), (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_resourceType_ = (d_0_info_)[0]
            d_3_value_ = StandardLibrary.default__.Join(_dafny.Seq((d_0_info_)[1::]), _dafny.Seq("/"))
            d_4_resource_ = AwsResource_AwsResource(d_2_resourceType_, d_3_value_)
            d_5_valueOrError1_ = Wrappers.default__.Need(default__.ValidAwsKmsResource(d_4_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
            if (d_5_valueOrError1_).IsFailure():
                return (d_5_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_4_resource_)

    @staticmethod
    def ValidAmazonDynamodbResource(resource):
        return ((resource).Valid()) and (((resource).resourceType) == (_dafny.Seq("table")))

    @staticmethod
    def ValidAmazonDynamodbArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("dynamodb")))) and (default__.ValidAmazonDynamodbResource((arn).resource))

    @staticmethod
    def ParseAmazonDynamodbResources(identifier):
        d_0_info_ = StandardLibrary.default__.SplitOnce_q(identifier, '/')
        d_1_valueOrError0_ = Wrappers.default__.Need((d_0_info_).is_Some, (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_resourceType_ = ((d_0_info_).value)[0]
            d_3_value_ = ((d_0_info_).value)[1]
            d_4_valueOrError1_ = Wrappers.default__.Need(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(d_3_value_), (_dafny.Seq("Table Name invalid: ")) + (identifier))
            if (d_4_valueOrError1_).IsFailure():
                return (d_4_valueOrError1_).PropagateFailure()
            elif True:
                d_5_resource_ = AwsResource_AwsResource(d_2_resourceType_, d_3_value_)
                d_6_valueOrError2_ = Wrappers.default__.Need(default__.ValidAmazonDynamodbResource(d_5_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
                if (d_6_valueOrError2_).IsFailure():
                    return (d_6_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_5_resource_)

    @staticmethod
    def ParseAwsKmsArn(identifier):
        d_0_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_1_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_0_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_valueOrError1_ = default__.ParseAwsKmsResources((d_0_components_)[5])
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_resource_ = (d_2_valueOrError1_).Extract()
                d_4_arn_ = AwsArn_AwsArn((d_0_components_)[0], (d_0_components_)[1], (d_0_components_)[2], (d_0_components_)[3], (d_0_components_)[4], d_3_resource_)
                d_5_valueOrError2_ = Wrappers.default__.Need(default__.ValidAwsKmsArn(d_4_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_5_valueOrError2_).IsFailure():
                    return (d_5_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_4_arn_)

    @staticmethod
    def ParseAmazonDynamodbTableArn(identifier):
        d_0_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_1_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_0_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_valueOrError1_ = default__.ParseAmazonDynamodbResources((d_0_components_)[5])
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_resource_ = (d_2_valueOrError1_).Extract()
                d_4_arn_ = AwsArn_AwsArn((d_0_components_)[0], (d_0_components_)[1], (d_0_components_)[2], (d_0_components_)[3], (d_0_components_)[4], d_3_resource_)
                d_5_valueOrError2_ = Wrappers.default__.Need(default__.ValidAmazonDynamodbArn(d_4_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_5_valueOrError2_).IsFailure():
                    return (d_5_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_4_arn_)

    @staticmethod
    def ParseAwsKmsIdentifier(identifier):
        if (_dafny.Seq("arn:")) <= (identifier):
            d_0_valueOrError0_ = default__.ParseAwsKmsArn(identifier)
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                d_1_arn_ = (d_0_valueOrError0_).Extract()
                return Wrappers.Result_Success(AwsKmsIdentifier_AwsKmsArnIdentifier(d_1_arn_))
        elif True:
            d_2_valueOrError1_ = default__.ParseAwsKmsRawResources(identifier)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_r_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsKmsIdentifier_AwsKmsRawResourceIdentifier(d_3_r_))

    @staticmethod
    def ParseAmazonDynamodbTableName(identifier):
        d_0_valueOrError0_ = default__.ParseAmazonDynamodbTableArn(identifier)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_arn_ = (d_0_valueOrError0_).Extract()
            d_2_tableArn_ = AmazonDynamodbTableName_AmazonDynamodbTableArn(d_1_arn_)
            d_3_tableName_ = (d_2_tableArn_).GetTableName()
            return Wrappers.Result_Success(d_3_tableName_)

    @staticmethod
    def IsMultiRegionAwsKmsArn(arn):
        return default__.IsMultiRegionAwsKmsResource((arn).resource)

    @staticmethod
    def IsMultiRegionAwsKmsIdentifier(identifier):
        source0_ = identifier
        if True:
            if source0_.is_AwsKmsArnIdentifier:
                d_0_arn_ = source0_.a
                return default__.IsMultiRegionAwsKmsArn(d_0_arn_)
        if True:
            d_1_r_ = source0_.r
            return default__.IsMultiRegionAwsKmsResource(d_1_r_)

    @staticmethod
    def IsMultiRegionAwsKmsResource(resource):
        return (((resource).resourceType) == (_dafny.Seq("key"))) and ((_dafny.Seq("mrk-")) <= ((resource).value))

    @staticmethod
    def GetRegion(identifier):
        source0_ = identifier
        if True:
            if source0_.is_AwsKmsArnIdentifier:
                d_0_a_ = source0_.a
                return Wrappers.Option_Some((d_0_a_).region)
        if True:
            return Wrappers.Option_None()

    @staticmethod
    def IsAwsKmsIdentifierString(s):
        d_0_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(s), _dafny.Seq("Not a valid ASCII string."))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_valueOrError1_ = Wrappers.default__.Need(((0) < (len(s))) and ((len(s)) <= (default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), _dafny.Seq("Identifier exceeds maximum length."))
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                return default__.ParseAwsKmsIdentifier(s)

    @staticmethod
    def Error(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def ValidateDdbTableArn(tableArn):
        d_0_valueOrError0_ = (default__.ParseAmazonDynamodbTableName(tableArn)).MapFailure(default__.Error)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1___v1_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(tableArn), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Arn is not ASCII")))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = Wrappers.default__.Need(ComAmazonawsDynamodbTypes.default__.IsValid__TableName((default__.ParseAmazonDynamodbTableName(tableArn)).value), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Name is too long")))
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @_dafny.classproperty
    def MAX__AWS__KMS__IDENTIFIER__LENGTH(instance):
        return 2048

class AwsResource:
    @classmethod
    def default(cls, ):
        return lambda: AwsResource_AwsResource(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsResource(self) -> bool:
        return isinstance(self, AwsResource_AwsResource)
    def Valid(self):
        return (True) and ((0) < (len((self).value)))

    def ToString(self):
        return (((self).resourceType) + (_dafny.Seq("/"))) + ((self).value)


class AwsResource_AwsResource(AwsResource, NamedTuple('AwsResource', [('resourceType', Any), ('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsResource.AwsResource({_dafny.string_of(self.resourceType)}, {_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsResource_AwsResource) and self.resourceType == __o.resourceType and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()


class AwsArn:
    @classmethod
    def default(cls, ):
        return lambda: AwsArn_AwsArn(_dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), _dafny.Seq(""), AwsResource.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsArn(self) -> bool:
        return isinstance(self, AwsArn_AwsArn)
    def Valid(self):
        return (((((((self).arnLiteral) == (_dafny.Seq("arn"))) and ((0) < (len((self).partition)))) and ((0) < (len((self).service)))) and ((0) < (len((self).region)))) and ((0) < (len((self).account)))) and (((self).resource).Valid())

    def ToString(self):
        return (self).ToArnString(Wrappers.Option_None())

    def ToArnString(self, customRegion):
        _this = self
        while True:
            with _dafny.label():
                source0_ = customRegion
                if True:
                    if source0_.is_None:
                        in0_ = _this
                        in1_ = Wrappers.Option_Some((_this).region)
                        _this = in0_
                        
                        customRegion = in1_
                        raise _dafny.TailCall()
                if True:
                    d_0_customRegion_ = source0_.value
                    return StandardLibrary.default__.Join(_dafny.Seq([(_this).arnLiteral, (_this).partition, (_this).service, d_0_customRegion_, (_this).account, ((_this).resource).ToString()]), _dafny.Seq(":"))
                break


class AwsArn_AwsArn(AwsArn, NamedTuple('AwsArn', [('arnLiteral', Any), ('partition', Any), ('service', Any), ('region', Any), ('account', Any), ('resource', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsArn.AwsArn({_dafny.string_of(self.arnLiteral)}, {_dafny.string_of(self.partition)}, {_dafny.string_of(self.service)}, {_dafny.string_of(self.region)}, {_dafny.string_of(self.account)}, {_dafny.string_of(self.resource)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArn_AwsArn) and self.arnLiteral == __o.arnLiteral and self.partition == __o.partition and self.service == __o.service and self.region == __o.region and self.account == __o.account and self.resource == __o.resource
    def __hash__(self) -> int:
        return super().__hash__()


class AwsKmsArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArn.default()()
    def _Is(source__):
        d_1_a_: AwsArn = source__
        return default__.ValidAwsKmsArn(d_1_a_)

class AwsKmsResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsResource.default()()
    def _Is(source__):
        d_2_r_: AwsResource = source__
        return default__.ValidAwsKmsResource(d_2_r_)

class AwsKmsIdentifier:
    @classmethod
    def default(cls, ):
        return lambda: AwsKmsIdentifier_AwsKmsArnIdentifier(AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsKmsArnIdentifier(self) -> bool:
        return isinstance(self, AwsKmsIdentifier_AwsKmsArnIdentifier)
    @property
    def is_AwsKmsRawResourceIdentifier(self) -> bool:
        return isinstance(self, AwsKmsIdentifier_AwsKmsRawResourceIdentifier)
    def ToString(self):
        source0_ = self
        if True:
            if source0_.is_AwsKmsArnIdentifier:
                d_0_a_ = source0_.a
                return (d_0_a_).ToString()
        if True:
            d_1_r_ = source0_.r
            return (d_1_r_).ToString()


class AwsKmsIdentifier_AwsKmsArnIdentifier(AwsKmsIdentifier, NamedTuple('AwsKmsArnIdentifier', [('a', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsKmsIdentifier.AwsKmsArnIdentifier({_dafny.string_of(self.a)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsIdentifier_AwsKmsArnIdentifier) and self.a == __o.a
    def __hash__(self) -> int:
        return super().__hash__()

class AwsKmsIdentifier_AwsKmsRawResourceIdentifier(AwsKmsIdentifier, NamedTuple('AwsKmsRawResourceIdentifier', [('r', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsKmsIdentifier.AwsKmsRawResourceIdentifier({_dafny.string_of(self.r)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsIdentifier_AwsKmsRawResourceIdentifier) and self.r == __o.r
    def __hash__(self) -> int:
        return super().__hash__()


class AmazonDynamodbTableArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArn.default()()
    def _Is(source__):
        d_2_a_: AwsArn = source__
        return default__.ValidAmazonDynamodbArn(d_2_a_)

class AmazonDynamodbResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsResource.default()()
    def _Is(source__):
        d_3_r_: AwsResource = source__
        return default__.ValidAmazonDynamodbResource(d_3_r_)

class AmazonDynamodbTableName:
    @classmethod
    def default(cls, ):
        return lambda: AmazonDynamodbTableName_AmazonDynamodbTableArn(AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AmazonDynamodbTableArn(self) -> bool:
        return isinstance(self, AmazonDynamodbTableName_AmazonDynamodbTableArn)
    def GetTableName(self):
        source0_ = self
        if True:
            d_0_a_ = source0_.a
            return ((d_0_a_).resource).value


class AmazonDynamodbTableName_AmazonDynamodbTableArn(AmazonDynamodbTableName, NamedTuple('AmazonDynamodbTableArn', [('a', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AmazonDynamodbTableName.AmazonDynamodbTableArn({_dafny.string_of(self.a)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AmazonDynamodbTableName_AmazonDynamodbTableArn) and self.a == __o.a
    def __hash__(self) -> int:
        return super().__hash__()


class AwsKmsIdentifierString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_s_: _dafny.Seq = source__
        return (default__.IsAwsKmsIdentifierString(d_1_s_)).is_Success
