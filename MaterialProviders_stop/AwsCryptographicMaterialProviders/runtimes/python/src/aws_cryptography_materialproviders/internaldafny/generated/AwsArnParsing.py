import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types

assert "AwsArnParsing" == __name__
AwsArnParsing = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ValidAwsKmsResource(resource):
        return ((resource).Valid()) and ((((resource).resourceType) == (_dafny.Seq("key"))) or (((resource).resourceType) == (_dafny.Seq("alias"))))

    @staticmethod
    def ValidAwsKmsArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("kms")))) and (AwsArnParsing.default__.ValidAwsKmsResource((arn).resource))

    @staticmethod
    def ParseAwsKmsRawResources(identifier):
        d_1_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_2_valueOrError0_ = Wrappers.default__.Need(((d_1_info_)[0]) != (_dafny.Seq("key")), (_dafny.Seq("Malformed raw key id: ")) + (identifier))
        if (d_2_valueOrError0_).IsFailure():
            return (d_2_valueOrError0_).PropagateFailure()
        elif (len(d_1_info_)) == (1):
            return AwsArnParsing.default__.ParseAwsKmsResources((_dafny.Seq("key/")) + (identifier))
        elif True:
            return AwsArnParsing.default__.ParseAwsKmsResources(identifier)

    @staticmethod
    def ParseAwsKmsResources(identifier):
        d_3_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_4_valueOrError0_ = Wrappers.default__.Need((len(d_3_info_)) > (1), (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_4_valueOrError0_).IsFailure():
            return (d_4_valueOrError0_).PropagateFailure()
        elif True:
            d_5_resourceType_ = (d_3_info_)[0]
            d_6_value_ = StandardLibrary.default__.Join(_dafny.Seq((d_3_info_)[1::]), _dafny.Seq("/"))
            d_7_resource_ = AwsArnParsing.AwsResource_AwsResource(d_5_resourceType_, d_6_value_)
            d_8_valueOrError1_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAwsKmsResource(d_7_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
            if (d_8_valueOrError1_).IsFailure():
                return (d_8_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_7_resource_)

    @staticmethod
    def ValidAmazonDynamodbResource(resource):
        return ((resource).Valid()) and (((resource).resourceType) == (_dafny.Seq("table")))

    @staticmethod
    def ValidAmazonDynamodbArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("dynamodb")))) and (AwsArnParsing.default__.ValidAmazonDynamodbResource((arn).resource))

    @staticmethod
    def ParseAmazonDynamodbResources(identifier):
        d_9_info_ = StandardLibrary.default__.SplitOnce_q(identifier, '/')
        d_10_valueOrError0_ = Wrappers.default__.Need((d_9_info_).is_Some, (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_10_valueOrError0_).IsFailure():
            return (d_10_valueOrError0_).PropagateFailure()
        elif True:
            d_11_resourceType_ = ((d_9_info_).value)[0]
            d_12_value_ = ((d_9_info_).value)[1]
            d_13_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName(d_12_value_), (_dafny.Seq("Table Name invalid: ")) + (identifier))
            if (d_13_valueOrError1_).IsFailure():
                return (d_13_valueOrError1_).PropagateFailure()
            elif True:
                d_14_resource_ = AwsArnParsing.AwsResource_AwsResource(d_11_resourceType_, d_12_value_)
                d_15_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAmazonDynamodbResource(d_14_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
                if (d_15_valueOrError2_).IsFailure():
                    return (d_15_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_14_resource_)

    @staticmethod
    def ParseAwsKmsArn(identifier):
        d_16_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_17_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_16_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_17_valueOrError0_).IsFailure():
            return (d_17_valueOrError0_).PropagateFailure()
        elif True:
            d_18_valueOrError1_ = AwsArnParsing.default__.ParseAwsKmsResources((d_16_components_)[5])
            if (d_18_valueOrError1_).IsFailure():
                return (d_18_valueOrError1_).PropagateFailure()
            elif True:
                d_19_resource_ = (d_18_valueOrError1_).Extract()
                d_20_arn_ = AwsArnParsing.AwsArn_AwsArn((d_16_components_)[0], (d_16_components_)[1], (d_16_components_)[2], (d_16_components_)[3], (d_16_components_)[4], d_19_resource_)
                d_21_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAwsKmsArn(d_20_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_21_valueOrError2_).IsFailure():
                    return (d_21_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_20_arn_)

    @staticmethod
    def ParseAmazonDynamodbTableArn(identifier):
        d_22_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_23_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_22_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_23_valueOrError0_).IsFailure():
            return (d_23_valueOrError0_).PropagateFailure()
        elif True:
            d_24_valueOrError1_ = AwsArnParsing.default__.ParseAmazonDynamodbResources((d_22_components_)[5])
            if (d_24_valueOrError1_).IsFailure():
                return (d_24_valueOrError1_).PropagateFailure()
            elif True:
                d_25_resource_ = (d_24_valueOrError1_).Extract()
                d_26_arn_ = AwsArnParsing.AwsArn_AwsArn((d_22_components_)[0], (d_22_components_)[1], (d_22_components_)[2], (d_22_components_)[3], (d_22_components_)[4], d_25_resource_)
                d_27_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAmazonDynamodbArn(d_26_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_27_valueOrError2_).IsFailure():
                    return (d_27_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_26_arn_)

    @staticmethod
    def ParseAwsKmsIdentifier(identifier):
        if (_dafny.Seq("arn:")) <= (identifier):
            d_28_valueOrError0_ = AwsArnParsing.default__.ParseAwsKmsArn(identifier)
            if (d_28_valueOrError0_).IsFailure():
                return (d_28_valueOrError0_).PropagateFailure()
            elif True:
                d_29_arn_ = (d_28_valueOrError0_).Extract()
                return Wrappers.Result_Success(AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_29_arn_))
        elif True:
            d_30_valueOrError1_ = AwsArnParsing.default__.ParseAwsKmsRawResources(identifier)
            if (d_30_valueOrError1_).IsFailure():
                return (d_30_valueOrError1_).PropagateFailure()
            elif True:
                d_31_r_ = (d_30_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsArnParsing.AwsKmsIdentifier_AwsKmsRawResourceIdentifier(d_31_r_))

    @staticmethod
    def ParseAmazonDynamodbTableName(identifier):
        d_32_valueOrError0_ = AwsArnParsing.default__.ParseAmazonDynamodbTableArn(identifier)
        if (d_32_valueOrError0_).IsFailure():
            return (d_32_valueOrError0_).PropagateFailure()
        elif True:
            d_33_arn_ = (d_32_valueOrError0_).Extract()
            d_34_tableArn_ = AwsArnParsing.AmazonDynamodbTableName_AmazonDynamodbTableArn(d_33_arn_)
            d_35_tableName_ = (d_34_tableArn_).GetTableName()
            return Wrappers.Result_Success(d_35_tableName_)

    @staticmethod
    def IsMultiRegionAwsKmsArn(arn):
        return AwsArnParsing.default__.IsMultiRegionAwsKmsResource((arn).resource)

    @staticmethod
    def IsMultiRegionAwsKmsIdentifier(identifier):
        source0_ = identifier
        if source0_.is_AwsKmsArnIdentifier:
            d_36___mcc_h0_ = source0_.a
            d_37_arn_ = d_36___mcc_h0_
            return AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_37_arn_)
        elif True:
            d_38___mcc_h1_ = source0_.r
            d_39_r_ = d_38___mcc_h1_
            return AwsArnParsing.default__.IsMultiRegionAwsKmsResource(d_39_r_)

    @staticmethod
    def IsMultiRegionAwsKmsResource(resource):
        return (((resource).resourceType) == (_dafny.Seq("key"))) and ((_dafny.Seq("mrk-")) <= ((resource).value))

    @staticmethod
    def GetRegion(identifier):
        source1_ = identifier
        if source1_.is_AwsKmsArnIdentifier:
            d_40___mcc_h0_ = source1_.a
            d_41_a_ = d_40___mcc_h0_
            return Wrappers.Option_Some((d_41_a_).region)
        elif True:
            d_42___mcc_h1_ = source1_.r
            return Wrappers.Option_None()

    @staticmethod
    def IsAwsKmsIdentifierString(s):
        d_43_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(s), _dafny.Seq("Not a valid ASCII string."))
        if (d_43_valueOrError0_).IsFailure():
            return (d_43_valueOrError0_).PropagateFailure()
        elif True:
            d_44_valueOrError1_ = Wrappers.default__.Need(((0) < (len(s))) and ((len(s)) <= ((AwsArnParsing.default__).MAX__AWS__KMS__IDENTIFIER__LENGTH)), _dafny.Seq("Identifier exceeds maximum length."))
            if (d_44_valueOrError1_).IsFailure():
                return (d_44_valueOrError1_).PropagateFailure()
            elif True:
                return AwsArnParsing.default__.ParseAwsKmsIdentifier(s)

    @staticmethod
    def Error(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def ValidateDdbTableArn(tableArn):
        d_45_valueOrError0_ = (AwsArnParsing.default__.ParseAmazonDynamodbTableName(tableArn)).MapFailure(AwsArnParsing.default__.Error)
        if (d_45_valueOrError0_).IsFailure():
            return (d_45_valueOrError0_).PropagateFailure()
        elif True:
            d_46___v1_ = (d_45_valueOrError0_).Extract()
            d_47_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(tableArn), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Arn is not ASCII")))
            if (d_47_valueOrError1_).IsFailure():
                return (d_47_valueOrError1_).PropagateFailure()
            elif True:
                d_48_valueOrError2_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName((AwsArnParsing.default__.ParseAmazonDynamodbTableName(tableArn)).value), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Name is too long")))
                if (d_48_valueOrError2_).IsFailure():
                    return (d_48_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @_dafny.classproperty
    def MAX__AWS__KMS__IDENTIFIER__LENGTH(instance):
        return 2048

class AwsResource:
    @classmethod
    def default(cls, ):
        return lambda: AwsResource_AwsResource(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsResource(self) -> bool:
        return isinstance(self, AwsArnParsing.AwsResource_AwsResource)
    def Valid(self):
        return (True) and ((0) < (len((self).value)))

    def ToString(self):
        return (((self).resourceType) + (_dafny.Seq("/"))) + ((self).value)


class AwsResource_AwsResource(AwsResource, NamedTuple('AwsResource', [('resourceType', Any), ('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsResource.AwsResource({_dafny.string_of(self.resourceType)}, {_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArnParsing.AwsResource_AwsResource) and self.resourceType == __o.resourceType and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()


class AwsArn:
    @classmethod
    def default(cls, ):
        return lambda: AwsArn_AwsArn(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), AwsArnParsing.AwsResource_AwsResource.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsArn(self) -> bool:
        return isinstance(self, AwsArnParsing.AwsArn_AwsArn)
    def Valid(self):
        return (((((((self).arnLiteral) == (_dafny.Seq("arn"))) and ((0) < (len((self).partition)))) and ((0) < (len((self).service)))) and ((0) < (len((self).region)))) and ((0) < (len((self).account)))) and (((self).resource).Valid())

    def ToString(self):
        return (self).ToArnString(Wrappers.Option_None())

    def ToArnString(self, customRegion):
        _this = self
        while True:
            with _dafny.label():
                source2_ = customRegion
                if source2_.is_None:
                    in0_ = _this
                    in1_ = Wrappers.Option_Some((_this).region)
                    _this = in0_
                    customRegion = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_49___mcc_h0_ = source2_.value
                    d_50_customRegion_ = d_49___mcc_h0_
                    return StandardLibrary.default__.Join(_dafny.Seq([(_this).arnLiteral, (_this).partition, (_this).service, d_50_customRegion_, (_this).account, ((_this).resource).ToString()]), _dafny.Seq(":"))
                break


class AwsArn_AwsArn(AwsArn, NamedTuple('AwsArn', [('arnLiteral', Any), ('partition', Any), ('service', Any), ('region', Any), ('account', Any), ('resource', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsArn.AwsArn({_dafny.string_of(self.arnLiteral)}, {_dafny.string_of(self.partition)}, {_dafny.string_of(self.service)}, {_dafny.string_of(self.region)}, {_dafny.string_of(self.account)}, {_dafny.string_of(self.resource)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArnParsing.AwsArn_AwsArn) and self.arnLiteral == __o.arnLiteral and self.partition == __o.partition and self.service == __o.service and self.region == __o.region and self.account == __o.account and self.resource == __o.resource
    def __hash__(self) -> int:
        return super().__hash__()


class AwsKmsArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArnParsing.AwsArn_AwsArn.default()()

class AwsKmsResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArnParsing.AwsResource_AwsResource.default()()

class AwsKmsIdentifier:
    @classmethod
    def default(cls, ):
        return lambda: AwsKmsIdentifier_AwsKmsArnIdentifier(AwsArnParsing.AwsArn_AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsKmsArnIdentifier(self) -> bool:
        return isinstance(self, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier)
    @property
    def is_AwsKmsRawResourceIdentifier(self) -> bool:
        return isinstance(self, AwsArnParsing.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)
    def ToString(self):
        source3_ = self
        if source3_.is_AwsKmsArnIdentifier:
            d_51___mcc_h0_ = source3_.a
            d_52_a_ = d_51___mcc_h0_
            return (d_52_a_).ToString()
        elif True:
            d_53___mcc_h1_ = source3_.r
            d_54_r_ = d_53___mcc_h1_
            return (d_54_r_).ToString()


class AwsKmsIdentifier_AwsKmsArnIdentifier(AwsKmsIdentifier, NamedTuple('AwsKmsArnIdentifier', [('a', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsKmsIdentifier.AwsKmsArnIdentifier({_dafny.string_of(self.a)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier) and self.a == __o.a
    def __hash__(self) -> int:
        return super().__hash__()

class AwsKmsIdentifier_AwsKmsRawResourceIdentifier(AwsKmsIdentifier, NamedTuple('AwsKmsRawResourceIdentifier', [('r', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AwsKmsIdentifier.AwsKmsRawResourceIdentifier({_dafny.string_of(self.r)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArnParsing.AwsKmsIdentifier_AwsKmsRawResourceIdentifier) and self.r == __o.r
    def __hash__(self) -> int:
        return super().__hash__()


class AmazonDynamodbTableArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArnParsing.AwsArn_AwsArn.default()()

class AmazonDynamodbResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsArnParsing.AwsResource_AwsResource.default()()

class AmazonDynamodbTableName:
    @classmethod
    def default(cls, ):
        return lambda: AmazonDynamodbTableName_AmazonDynamodbTableArn(AwsArnParsing.AwsArn_AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AmazonDynamodbTableArn(self) -> bool:
        return isinstance(self, AwsArnParsing.AmazonDynamodbTableName_AmazonDynamodbTableArn)
    def GetTableName(self):
        source4_ = self
        if True:
            d_55___mcc_h0_ = source4_.a
            d_56_a_ = d_55___mcc_h0_
            return ((d_56_a_).resource).value


class AmazonDynamodbTableName_AmazonDynamodbTableArn(AmazonDynamodbTableName, NamedTuple('AmazonDynamodbTableArn', [('a', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsArnParsing.AmazonDynamodbTableName.AmazonDynamodbTableArn({_dafny.string_of(self.a)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsArnParsing.AmazonDynamodbTableName_AmazonDynamodbTableArn) and self.a == __o.a
    def __hash__(self) -> int:
        return super().__hash__()


class AwsKmsIdentifierString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
