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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring

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
        d_87_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_88_valueOrError0_ = Wrappers.default__.Need(((d_87_info_)[0]) != (_dafny.Seq("key")), (_dafny.Seq("Malformed raw key id: ")) + (identifier))
        if (d_88_valueOrError0_).IsFailure():
            return (d_88_valueOrError0_).PropagateFailure()
        elif (len(d_87_info_)) == (1):
            return AwsArnParsing.default__.ParseAwsKmsResources((_dafny.Seq("key/")) + (identifier))
        elif True:
            return AwsArnParsing.default__.ParseAwsKmsResources(identifier)

    @staticmethod
    def ParseAwsKmsResources(identifier):
        d_89_info_ = StandardLibrary.default__.Split(identifier, '/')
        d_90_valueOrError0_ = Wrappers.default__.Need((len(d_89_info_)) > (1), (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_90_valueOrError0_).IsFailure():
            return (d_90_valueOrError0_).PropagateFailure()
        elif True:
            d_91_resourceType_ = (d_89_info_)[0]
            d_92_value_ = StandardLibrary.default__.Join(_dafny.Seq((d_89_info_)[1::]), _dafny.Seq("/"))
            d_93_resource_ = AwsArnParsing.AwsResource_AwsResource(d_91_resourceType_, d_92_value_)
            d_94_valueOrError1_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAwsKmsResource(d_93_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
            if (d_94_valueOrError1_).IsFailure():
                return (d_94_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_93_resource_)

    @staticmethod
    def ValidAmazonDynamodbResource(resource):
        return ((resource).Valid()) and (((resource).resourceType) == (_dafny.Seq("table")))

    @staticmethod
    def ValidAmazonDynamodbArn(arn):
        return (((arn).Valid()) and (((arn).service) == (_dafny.Seq("dynamodb")))) and (AwsArnParsing.default__.ValidAmazonDynamodbResource((arn).resource))

    @staticmethod
    def ParseAmazonDynamodbResources(identifier):
        d_95_info_ = StandardLibrary.default__.SplitOnce_q(identifier, '/')
        d_96_valueOrError0_ = Wrappers.default__.Need((d_95_info_).is_Some, (_dafny.Seq("Malformed resource: ")) + (identifier))
        if (d_96_valueOrError0_).IsFailure():
            return (d_96_valueOrError0_).PropagateFailure()
        elif True:
            d_97_resourceType_ = ((d_95_info_).value)[0]
            d_98_value_ = ((d_95_info_).value)[1]
            d_99_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName(d_98_value_), (_dafny.Seq("Table Name invalid: ")) + (identifier))
            if (d_99_valueOrError1_).IsFailure():
                return (d_99_valueOrError1_).PropagateFailure()
            elif True:
                d_100_resource_ = AwsArnParsing.AwsResource_AwsResource(d_97_resourceType_, d_98_value_)
                d_101_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAmazonDynamodbResource(d_100_resource_), (_dafny.Seq("Malformed resource: ")) + (identifier))
                if (d_101_valueOrError2_).IsFailure():
                    return (d_101_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_100_resource_)

    @staticmethod
    def ParseAwsKmsArn(identifier):
        d_102_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_103_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_102_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_103_valueOrError0_).IsFailure():
            return (d_103_valueOrError0_).PropagateFailure()
        elif True:
            d_104_valueOrError1_ = AwsArnParsing.default__.ParseAwsKmsResources((d_102_components_)[5])
            if (d_104_valueOrError1_).IsFailure():
                return (d_104_valueOrError1_).PropagateFailure()
            elif True:
                d_105_resource_ = (d_104_valueOrError1_).Extract()
                d_106_arn_ = AwsArnParsing.AwsArn_AwsArn((d_102_components_)[0], (d_102_components_)[1], (d_102_components_)[2], (d_102_components_)[3], (d_102_components_)[4], d_105_resource_)
                d_107_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAwsKmsArn(d_106_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_107_valueOrError2_).IsFailure():
                    return (d_107_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_106_arn_)

    @staticmethod
    def ParseAmazonDynamodbTableArn(identifier):
        d_108_components_ = StandardLibrary.default__.Split(identifier, ':')
        d_109_valueOrError0_ = Wrappers.default__.Need((6) == (len(d_108_components_)), (_dafny.Seq("Malformed arn: ")) + (identifier))
        if (d_109_valueOrError0_).IsFailure():
            return (d_109_valueOrError0_).PropagateFailure()
        elif True:
            d_110_valueOrError1_ = AwsArnParsing.default__.ParseAmazonDynamodbResources((d_108_components_)[5])
            if (d_110_valueOrError1_).IsFailure():
                return (d_110_valueOrError1_).PropagateFailure()
            elif True:
                d_111_resource_ = (d_110_valueOrError1_).Extract()
                d_112_arn_ = AwsArnParsing.AwsArn_AwsArn((d_108_components_)[0], (d_108_components_)[1], (d_108_components_)[2], (d_108_components_)[3], (d_108_components_)[4], d_111_resource_)
                d_113_valueOrError2_ = Wrappers.default__.Need(AwsArnParsing.default__.ValidAmazonDynamodbArn(d_112_arn_), (_dafny.Seq("Malformed Arn:")) + (identifier))
                if (d_113_valueOrError2_).IsFailure():
                    return (d_113_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(d_112_arn_)

    @staticmethod
    def ParseAwsKmsIdentifier(identifier):
        if (_dafny.Seq("arn:")) <= (identifier):
            d_114_valueOrError0_ = AwsArnParsing.default__.ParseAwsKmsArn(identifier)
            if (d_114_valueOrError0_).IsFailure():
                return (d_114_valueOrError0_).PropagateFailure()
            elif True:
                d_115_arn_ = (d_114_valueOrError0_).Extract()
                return Wrappers.Result_Success(AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_115_arn_))
        elif True:
            d_116_valueOrError1_ = AwsArnParsing.default__.ParseAwsKmsRawResources(identifier)
            if (d_116_valueOrError1_).IsFailure():
                return (d_116_valueOrError1_).PropagateFailure()
            elif True:
                d_117_r_ = (d_116_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsArnParsing.AwsKmsIdentifier_AwsKmsRawResourceIdentifier(d_117_r_))

    @staticmethod
    def ParseAmazonDynamodbTableName(identifier):
        d_118_valueOrError0_ = AwsArnParsing.default__.ParseAmazonDynamodbTableArn(identifier)
        if (d_118_valueOrError0_).IsFailure():
            return (d_118_valueOrError0_).PropagateFailure()
        elif True:
            d_119_arn_ = (d_118_valueOrError0_).Extract()
            d_120_tableArn_ = AwsArnParsing.AmazonDynamodbTableName_AmazonDynamodbTableArn(d_119_arn_)
            d_121_tableName_ = (d_120_tableArn_).GetTableName()
            return Wrappers.Result_Success(d_121_tableName_)

    @staticmethod
    def IsMultiRegionAwsKmsArn(arn):
        return AwsArnParsing.default__.IsMultiRegionAwsKmsResource((arn).resource)

    @staticmethod
    def IsMultiRegionAwsKmsIdentifier(identifier):
        source8_ = identifier
        if source8_.is_AwsKmsArnIdentifier:
            d_122___mcc_h0_ = source8_.a
            d_123_arn_ = d_122___mcc_h0_
            return AwsArnParsing.default__.IsMultiRegionAwsKmsArn(d_123_arn_)
        elif True:
            d_124___mcc_h1_ = source8_.r
            d_125_r_ = d_124___mcc_h1_
            return AwsArnParsing.default__.IsMultiRegionAwsKmsResource(d_125_r_)

    @staticmethod
    def IsMultiRegionAwsKmsResource(resource):
        return (((resource).resourceType) == (_dafny.Seq("key"))) and ((_dafny.Seq("mrk-")) <= ((resource).value))

    @staticmethod
    def GetRegion(identifier):
        source9_ = identifier
        if source9_.is_AwsKmsArnIdentifier:
            d_126___mcc_h0_ = source9_.a
            d_127_a_ = d_126___mcc_h0_
            return Wrappers.Option_Some((d_127_a_).region)
        elif True:
            d_128___mcc_h1_ = source9_.r
            return Wrappers.Option_None()

    @staticmethod
    def IsAwsKmsIdentifierString(s):
        d_129_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(s), _dafny.Seq("Not a valid ASCII string."))
        if (d_129_valueOrError0_).IsFailure():
            return (d_129_valueOrError0_).PropagateFailure()
        elif True:
            d_130_valueOrError1_ = Wrappers.default__.Need(((0) < (len(s))) and ((len(s)) <= ((AwsArnParsing.default__).MAX__AWS__KMS__IDENTIFIER__LENGTH)), _dafny.Seq("Identifier exceeds maximum length."))
            if (d_130_valueOrError1_).IsFailure():
                return (d_130_valueOrError1_).PropagateFailure()
            elif True:
                return AwsArnParsing.default__.ParseAwsKmsIdentifier(s)

    @staticmethod
    def Error(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @staticmethod
    def ValidateDdbTableArn(tableArn):
        d_131_valueOrError0_ = (AwsArnParsing.default__.ParseAmazonDynamodbTableName(tableArn)).MapFailure(AwsArnParsing.default__.Error)
        if (d_131_valueOrError0_).IsFailure():
            return (d_131_valueOrError0_).PropagateFailure()
        elif True:
            d_132___v1_ = (d_131_valueOrError0_).Extract()
            d_133_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(tableArn), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Arn is not ASCII")))
            if (d_133_valueOrError1_).IsFailure():
                return (d_133_valueOrError1_).PropagateFailure()
            elif True:
                d_134_valueOrError2_ = Wrappers.default__.Need(software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__TableName((AwsArnParsing.default__.ParseAmazonDynamodbTableName(tableArn)).value), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Table Name is too long")))
                if (d_134_valueOrError2_).IsFailure():
                    return (d_134_valueOrError2_).PropagateFailure()
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
                source10_ = customRegion
                if source10_.is_None:
                    in0_ = _this
                    in1_ = Wrappers.Option_Some((_this).region)
                    _this = in0_
                    customRegion = in1_
                    raise _dafny.TailCall()
                elif True:
                    d_135___mcc_h0_ = source10_.value
                    d_136_customRegion_ = d_135___mcc_h0_
                    return StandardLibrary.default__.Join(_dafny.Seq([(_this).arnLiteral, (_this).partition, (_this).service, d_136_customRegion_, (_this).account, ((_this).resource).ToString()]), _dafny.Seq(":"))
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
        source11_ = self
        if source11_.is_AwsKmsArnIdentifier:
            d_137___mcc_h0_ = source11_.a
            d_138_a_ = d_137___mcc_h0_
            return (d_138_a_).ToString()
        elif True:
            d_139___mcc_h1_ = source11_.r
            d_140_r_ = d_139___mcc_h1_
            return (d_140_r_).ToString()


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
        source12_ = self
        if True:
            d_141___mcc_h0_ = source12_.a
            d_142_a_ = d_141___mcc_h0_
            return ((d_142_a_).resource).value


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
