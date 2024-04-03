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
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types

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
        d_5_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_6_valueOrError0_ = Wrappers.default__.Need(((d_5_info_)[0]) != (_dafny.Seq("key")), (_dafny.Seq("Malformed raw key id: ")) + (identifier))
        if (d_6_valueOrError0_).IsFailure():
            return (d_6_valueOrError0_).PropagateFailure()
        elif (len(d_5_info_)) == (1):
            return default__.ParseAwsKmsResources((_dafny.Seq("key/")) + (identifier))
        elif True:
            return default__.ParseAwsKmsResources(identifier)

    @staticmethod
    def ParseAwsKmsResources(identifier):
        d_7_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_8_valueOrError0_ = Wrappers.default__.Need((len(d_7_info_)) > (1), (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_8_valueOrError0_).IsFailure():
            return (d_8_valueOrError0_).PropagateFailure()
        elif True:
            d_9_resourceType_ = (d_7_info_)[0]
            d_10_value_ = StandardLibrary.default__.Join(_dafny.Seq((d_7_info_)[1::]), _dafny.Seq("/"))
            d_11_resource_ = AwsResource_AwsResource(d_9_resourceType_, d_10_value_)
            d_12_valueOrError1_ = Wrappers.default__.Need(default__.ValidAwsKmsResource(d_11_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
            if (d_12_valueOrError1_).IsFailure():
                return (d_12_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_11_resource_)

    @staticmethod
    def ValidAmazonDynamodbResource(resource):
        return ((resource).Valid()) and (((resource).resourceType) == (_dafny.Seq("table")))

    @staticmethod
    def ValidAmazonDynamodbArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("dynamodb")))) and (default__.ValidAmazonDynamodbResource((arn).resource))

    @staticmethod
    def ParseAmazonDynamodbResources(identifier):
        d_13_info_ = StandardLibrary.default__.SplitOnce_q(identifier, '/')
        d_14_valueOrError0_ = Wrappers.default__.Need((d_13_info_).is_Some, (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_14_valueOrError0_).IsFailure():
            return (d_14_valueOrError0_).PropagateFailure()
        elif True:
            d_15_resourceType_ = ((d_13_info_).value)[0]
            d_16_value_ = ((d_13_info_).value)[1]
            d_17_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName(d_16_value_), (_dafny.Seq("Table Name invalid: ")) + (identifier))
            if (d_17_valueOrError1_).IsFailure():
                return (d_17_valueOrError1_).PropagateFailure()
            elif True:
                d_18_resource_ = AwsResource_AwsResource(d_15_resourceType_, d_16_value_)
                d_19_valueOrError2_ = Wrappers.default__.Need(default__.ValidAmazonDynamodbResource(d_18_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
                if (d_19_valueOrError2_).IsFailure():
                    return (d_19_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_18_resource_)

    @staticmethod
    def ParseAwsKmsArn(identifier):
        d_20_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_21_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_20_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_21_valueOrError0_).IsFailure():
            return (d_21_valueOrError0_).PropagateFailure()
        elif True:
            d_22_valueOrError1_ = default__.ParseAwsKmsResources((d_20_components_)[5])
            if (d_22_valueOrError1_).IsFailure():
                return (d_22_valueOrError1_).PropagateFailure()
            elif True:
                d_23_resource_ = (d_22_valueOrError1_).Extract()
                d_24_arn_ = AwsArn_AwsArn((d_20_components_)[0], (d_20_components_)[1], (d_20_components_)[2], (d_20_components_)[3], (d_20_components_)[4], d_23_resource_)
                d_25_valueOrError2_ = Wrappers.default__.Need(default__.ValidAwsKmsArn(d_24_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_25_valueOrError2_).IsFailure():
                    return (d_25_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_24_arn_)

    @staticmethod
    def ParseAmazonDynamodbTableArn(identifier):
        d_26_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_27_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_26_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_27_valueOrError0_).IsFailure():
            return (d_27_valueOrError0_).PropagateFailure()
        elif True:
            d_28_valueOrError1_ = default__.ParseAmazonDynamodbResources((d_26_components_)[5])
            if (d_28_valueOrError1_).IsFailure():
                return (d_28_valueOrError1_).PropagateFailure()
            elif True:
                d_29_resource_ = (d_28_valueOrError1_).Extract()
                d_30_arn_ = AwsArn_AwsArn((d_26_components_)[0], (d_26_components_)[1], (d_26_components_)[2], (d_26_components_)[3], (d_26_components_)[4], d_29_resource_)
                d_31_valueOrError2_ = Wrappers.default__.Need(default__.ValidAmazonDynamodbArn(d_30_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_31_valueOrError2_).IsFailure():
                    return (d_31_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_30_arn_)

    @staticmethod
    def ParseAwsKmsIdentifier(identifier):
        if (_dafny.Seq("arn:")) <= (identifier):
            d_32_valueOrError0_ = default__.ParseAwsKmsArn(identifier)
            if (d_32_valueOrError0_).IsFailure():
                return (d_32_valueOrError0_).PropagateFailure()
            elif True:
                d_33_arn_ = (d_32_valueOrError0_).Extract()
                return Wrappers.Result_Success(AwsKmsIdentifier_AwsKmsArnIdentifier(d_33_arn_))
        elif True:
            d_34_valueOrError1_ = default__.ParseAwsKmsRawResources(identifier)
            if (d_34_valueOrError1_).IsFailure():
                return (d_34_valueOrError1_).PropagateFailure()
            elif True:
                d_35_r_ = (d_34_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsKmsIdentifier_AwsKmsRawResourceIdentifier(d_35_r_))

    @staticmethod
    def ParseAmazonDynamodbTableName(identifier):
        d_36_valueOrError0_ = default__.ParseAmazonDynamodbTableArn(identifier)
        if (d_36_valueOrError0_).IsFailure():
            return (d_36_valueOrError0_).PropagateFailure()
        elif True:
            d_37_arn_ = (d_36_valueOrError0_).Extract()
            d_38_tableArn_ = AmazonDynamodbTableName_AmazonDynamodbTableArn(d_37_arn_)
            d_39_tableName_ = (d_38_tableArn_).GetTableName()
            return Wrappers.Result_Success(d_39_tableName_)

    @staticmethod
    def IsMultiRegionAwsKmsArn(arn):
        return default__.IsMultiRegionAwsKmsResource((arn).resource)

    @staticmethod
    def IsMultiRegionAwsKmsIdentifier(identifier):
        source0_ = identifier
        if source0_.is_AwsKmsArnIdentifier:
            d_40___mcc_h0_ = source0_.a
            d_41_arn_ = d_40___mcc_h0_
            return default__.IsMultiRegionAwsKmsArn(d_41_arn_)
        elif True:
            d_42___mcc_h1_ = source0_.r
            d_43_r_ = d_42___mcc_h1_
            return default__.IsMultiRegionAwsKmsResource(d_43_r_)

    @staticmethod
    def IsMultiRegionAwsKmsResource(resource):
        return (((resource).resourceType) == (_dafny.Seq("key"))) and ((_dafny.Seq("mrk-")) <= ((resource).value))

    @staticmethod
    def GetRegion(identifier):
        source1_ = identifier
        if source1_.is_AwsKmsArnIdentifier:
            d_44___mcc_h0_ = source1_.a
            d_45_a_ = d_44___mcc_h0_
            return Wrappers.Option_Some((d_45_a_).region)
        elif True:
            d_46___mcc_h1_ = source1_.r
            return Wrappers.Option_None()

    @staticmethod
    def IsAwsKmsIdentifierString(s):
        d_47_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(s), _dafny.Seq("Not a valid ASCII string."))
        if (d_47_valueOrError0_).IsFailure():
            return (d_47_valueOrError0_).PropagateFailure()
        elif True:
            d_48_valueOrError1_ = Wrappers.default__.Need(((0) < (len(s))) and ((len(s)) <= (default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), _dafny.Seq("Identifier exceeds maximum length."))
            if (d_48_valueOrError1_).IsFailure():
                return (d_48_valueOrError1_).PropagateFailure()
            elif True:
                return default__.ParseAwsKmsIdentifier(s)

    @staticmethod
    def Error(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def ValidateDdbTableArn(tableArn):
        d_49_valueOrError0_ = (default__.ParseAmazonDynamodbTableName(tableArn)).MapFailure(default__.Error)
        if (d_49_valueOrError0_).IsFailure():
            return (d_49_valueOrError0_).PropagateFailure()
        elif True:
            d_50___v1_ = (d_49_valueOrError0_).Extract()
            d_51_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(tableArn), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Arn is not ASCII")))
            if (d_51_valueOrError1_).IsFailure():
                return (d_51_valueOrError1_).PropagateFailure()
            elif True:
                d_52_valueOrError2_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName((default__.ParseAmazonDynamodbTableName(tableArn)).value), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Name is too long")))
                if (d_52_valueOrError2_).IsFailure():
                    return (d_52_valueOrError2_).PropagateFailure()
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
                source2_ = customRegion
                if source2_.is_None:
                    in0_ = _this
                    in1_ = Wrappers.Option_Some((_this).region)
                    _this = in0_
                    
                    customRegion = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_53___mcc_h0_ = source2_.value
                    d_54_customRegion_ = d_53___mcc_h0_
                    return StandardLibrary.default__.Join(_dafny.Seq([(_this).arnLiteral, (_this).partition, (_this).service, d_54_customRegion_, (_this).account, ((_this).resource).ToString()]), _dafny.Seq(":"))
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
        d_55_a_: AwsArn = source__
        return default__.ValidAwsKmsArn(d_55_a_)

class AwsKmsResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsResource.default()()
    def _Is(source__):
        d_56_r_: AwsResource = source__
        return default__.ValidAwsKmsResource(d_56_r_)

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
        source3_ = self
        if source3_.is_AwsKmsArnIdentifier:
            d_57___mcc_h0_ = source3_.a
            d_58_a_ = d_57___mcc_h0_
            return (d_58_a_).ToString()
        elif True:
            d_59___mcc_h1_ = source3_.r
            d_60_r_ = d_59___mcc_h1_
            return (d_60_r_).ToString()


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
        d_61_a_: AwsArn = source__
        return default__.ValidAmazonDynamodbArn(d_61_a_)

class AmazonDynamodbResource:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsResource.default()()
    def _Is(source__):
        d_62_r_: AwsResource = source__
        return default__.ValidAmazonDynamodbResource(d_62_r_)

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
        source4_ = self
        d_63___mcc_h0_ = source4_.a
        d_64_a_ = d_63___mcc_h0_
        return ((d_64_a_).resource).value


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
        d_65_s_: _dafny.Seq = source__
        return (default__.IsAwsKmsIdentifierString(d_65_s_)).is_Success
