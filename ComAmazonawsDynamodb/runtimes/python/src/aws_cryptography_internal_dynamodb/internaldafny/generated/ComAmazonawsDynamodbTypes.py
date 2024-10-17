import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_internal_dynamodb.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
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
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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

# Module: ComAmazonawsDynamodbTypes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsValid__AttributeName(x):
        return ((0) <= (len(x))) and ((len(x)) <= (65535))

    @staticmethod
    def IsValid__AttributeNameList(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__AutoScalingPolicyName(x):
        return ((1) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__AutoScalingRoleArn(x):
        return ((1) <= (len(x))) and ((len(x)) <= (1600))

    @staticmethod
    def IsValid__BackupArn(x):
        return ((37) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__BackupName(x):
        return ((3) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__BackupsInputLimit(x):
        return ((1) <= (x)) and ((x) <= (100))

    @staticmethod
    def IsValid__BackupSizeBytes(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__BatchGetRequestMap(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__BatchWriteItemRequestMap(x):
        return ((1) <= (len(x))) and ((len(x)) <= (25))

    @staticmethod
    def IsValid__BilledSizeBytes(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__CancellationReasonList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__ClientRequestToken(x):
        return ((1) <= (len(x))) and ((len(x)) <= (36))

    @staticmethod
    def IsValid__CloudWatchLogGroupArn(x):
        return ((1) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__ConsumedCapacityUnits(x):
        return ((8) <= (len(x))) and ((len(x)) <= (8))

    @staticmethod
    def IsValid__CsvDelimiter(x):
        return ((1) <= (len(x))) and ((len(x)) <= (1))

    @staticmethod
    def IsValid__CsvHeader(x):
        return ((1) <= (len(x))) and ((len(x)) <= (65536))

    @staticmethod
    def IsValid__CsvHeaderList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__Double(x):
        return ((8) <= (len(x))) and ((len(x)) <= (8))

    @staticmethod
    def IsValid__ErrorCount(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__ExportArn(x):
        return ((37) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__GlobalSecondaryIndexAutoScalingUpdateList(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__GlobalTableGlobalSecondaryIndexSettingsUpdateList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (20))

    @staticmethod
    def IsValid__ImportArn(x):
        return ((37) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__ImportedItemCount(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__ImportNextToken(x):
        return ((112) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__IndexName(x):
        return ((3) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__ItemCollectionSizeEstimateBound(x):
        return ((8) <= (len(x))) and ((len(x)) <= (8))

    @staticmethod
    def IsValid__ItemCount(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__ItemResponseList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__KeyList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__KeySchema(x):
        return ((1) <= (len(x))) and ((len(x)) <= (2))

    @staticmethod
    def IsValid__KeySchemaAttributeName(x):
        return ((1) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__ListContributorInsightsLimit(x):
        return (x) <= (100)

    @staticmethod
    def IsValid__ListExportsMaxLimit(x):
        return ((1) <= (x)) and ((x) <= (25))

    @staticmethod
    def IsValid__ListImportsMaxLimit(x):
        return ((1) <= (x)) and ((x) <= (25))

    @staticmethod
    def IsValid__ListTablesInputLimit(x):
        return ((1) <= (x)) and ((x) <= (100))

    @staticmethod
    def IsValid__NonKeyAttributeName(x):
        return ((1) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__NonKeyAttributeNameList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (20))

    @staticmethod
    def IsValid__NonNegativeLongObject(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__ParameterizedStatements(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__PartiQLBatchRequest(x):
        return ((1) <= (len(x))) and ((len(x)) <= (25))

    @staticmethod
    def IsValid__PartiQLNextToken(x):
        return ((1) <= (len(x))) and ((len(x)) <= (32768))

    @staticmethod
    def IsValid__PartiQLStatement(x):
        return ((1) <= (len(x))) and ((len(x)) <= (8192))

    @staticmethod
    def IsValid__PositiveIntegerObject(x):
        return (1) <= (x)

    @staticmethod
    def IsValid__PositiveLongObject(x):
        return (1) <= (x)

    @staticmethod
    def IsValid__PreparedStatementParameters(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__ProcessedItemCount(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__ReplicaAutoScalingUpdateList(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__ReplicaGlobalSecondaryIndexList(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__ReplicaGlobalSecondaryIndexSettingsUpdateList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (20))

    @staticmethod
    def IsValid__ReplicaSettingsUpdateList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (50))

    @staticmethod
    def IsValid__ReplicationGroupUpdateList(x):
        return (1) <= (len(x))

    @staticmethod
    def IsValid__ResourceArnString(x):
        return ((1) <= (len(x))) and ((len(x)) <= (1283))

    @staticmethod
    def IsValid__S3Bucket(x):
        return ((0) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__S3Prefix(x):
        return ((0) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__S3SseKmsKeyId(x):
        return ((1) <= (len(x))) and ((len(x)) <= (2048))

    @staticmethod
    def IsValid__ScanSegment(x):
        return ((0) <= (x)) and ((x) <= (999999))

    @staticmethod
    def IsValid__ScanTotalSegments(x):
        return ((1) <= (x)) and ((x) <= (1000000))

    @staticmethod
    def IsValid__StreamArn(x):
        return ((37) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__TableName(x):
        return ((3) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__TagKeyString(x):
        return ((1) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__TagValueString(x):
        return ((0) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__TimeToLiveAttributeName(x):
        return ((1) <= (len(x))) and ((len(x)) <= (255))

    @staticmethod
    def IsValid__TransactGetItemList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__TransactWriteItemList(x):
        return ((1) <= (len(x))) and ((len(x)) <= (100))

    @staticmethod
    def IsValid__WriteRequests(x):
        return ((1) <= (len(x))) and ((len(x)) <= (25))


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class ArchivalSummary:
    @classmethod
    def default(cls, ):
        return lambda: ArchivalSummary_ArchivalSummary(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ArchivalSummary(self) -> bool:
        return isinstance(self, ArchivalSummary_ArchivalSummary)

class ArchivalSummary_ArchivalSummary(ArchivalSummary, NamedTuple('ArchivalSummary', [('ArchivalDateTime', Any), ('ArchivalReason', Any), ('ArchivalBackupArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ArchivalSummary.ArchivalSummary({_dafny.string_of(self.ArchivalDateTime)}, {_dafny.string_of(self.ArchivalReason)}, {_dafny.string_of(self.ArchivalBackupArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ArchivalSummary_ArchivalSummary) and self.ArchivalDateTime == __o.ArchivalDateTime and self.ArchivalReason == __o.ArchivalReason and self.ArchivalBackupArn == __o.ArchivalBackupArn
    def __hash__(self) -> int:
        return super().__hash__()


class AttributeAction:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AttributeAction_ADD(), AttributeAction_PUT(), AttributeAction_DELETE()]
    @classmethod
    def default(cls, ):
        return lambda: AttributeAction_ADD()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ADD(self) -> bool:
        return isinstance(self, AttributeAction_ADD)
    @property
    def is_PUT(self) -> bool:
        return isinstance(self, AttributeAction_PUT)
    @property
    def is_DELETE(self) -> bool:
        return isinstance(self, AttributeAction_DELETE)

class AttributeAction_ADD(AttributeAction, NamedTuple('ADD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeAction.ADD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeAction_ADD)
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeAction_PUT(AttributeAction, NamedTuple('PUT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeAction.PUT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeAction_PUT)
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeAction_DELETE(AttributeAction, NamedTuple('DELETE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeAction.DELETE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeAction_DELETE)
    def __hash__(self) -> int:
        return super().__hash__()


class AttributeDefinition:
    @classmethod
    def default(cls, ):
        return lambda: AttributeDefinition_AttributeDefinition(_dafny.Seq(""), ScalarAttributeType.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AttributeDefinition(self) -> bool:
        return isinstance(self, AttributeDefinition_AttributeDefinition)

class AttributeDefinition_AttributeDefinition(AttributeDefinition, NamedTuple('AttributeDefinition', [('AttributeName', Any), ('AttributeType', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeDefinition.AttributeDefinition({_dafny.string_of(self.AttributeName)}, {_dafny.string_of(self.AttributeType)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeDefinition_AttributeDefinition) and self.AttributeName == __o.AttributeName and self.AttributeType == __o.AttributeType
    def __hash__(self) -> int:
        return super().__hash__()


class AttributeName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_0_x_: _dafny.Seq = source__
        return default__.IsValid__AttributeName(d_0_x_)

class AttributeNameList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_1_x_: _dafny.Seq = source__
        return default__.IsValid__AttributeNameList(d_1_x_)

class AttributeValue:
    @classmethod
    def default(cls, ):
        return lambda: AttributeValue_S(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_S(self) -> bool:
        return isinstance(self, AttributeValue_S)
    @property
    def is_N(self) -> bool:
        return isinstance(self, AttributeValue_N)
    @property
    def is_B(self) -> bool:
        return isinstance(self, AttributeValue_B)
    @property
    def is_SS(self) -> bool:
        return isinstance(self, AttributeValue_SS)
    @property
    def is_NS(self) -> bool:
        return isinstance(self, AttributeValue_NS)
    @property
    def is_BS(self) -> bool:
        return isinstance(self, AttributeValue_BS)
    @property
    def is_M(self) -> bool:
        return isinstance(self, AttributeValue_M)
    @property
    def is_L(self) -> bool:
        return isinstance(self, AttributeValue_L)
    @property
    def is_NULL(self) -> bool:
        return isinstance(self, AttributeValue_NULL)
    @property
    def is_BOOL(self) -> bool:
        return isinstance(self, AttributeValue_BOOL)

class AttributeValue_S(AttributeValue, NamedTuple('S', [('S', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.S({_dafny.string_of(self.S)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_S) and self.S == __o.S
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_N(AttributeValue, NamedTuple('N', [('N', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.N({_dafny.string_of(self.N)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_N) and self.N == __o.N
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_B(AttributeValue, NamedTuple('B', [('B', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.B({_dafny.string_of(self.B)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_B) and self.B == __o.B
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_SS(AttributeValue, NamedTuple('SS', [('SS', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.SS({_dafny.string_of(self.SS)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_SS) and self.SS == __o.SS
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_NS(AttributeValue, NamedTuple('NS', [('NS', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.NS({_dafny.string_of(self.NS)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_NS) and self.NS == __o.NS
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_BS(AttributeValue, NamedTuple('BS', [('BS', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.BS({_dafny.string_of(self.BS)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_BS) and self.BS == __o.BS
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_M(AttributeValue, NamedTuple('M', [('M', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.M({_dafny.string_of(self.M)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_M) and self.M == __o.M
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_L(AttributeValue, NamedTuple('L', [('L', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.L({_dafny.string_of(self.L)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_L) and self.L == __o.L
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_NULL(AttributeValue, NamedTuple('NULL', [('NULL', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.NULL({_dafny.string_of(self.NULL)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_NULL) and self.NULL == __o.NULL
    def __hash__(self) -> int:
        return super().__hash__()

class AttributeValue_BOOL(AttributeValue, NamedTuple('BOOL', [('BOOL', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValue.BOOL({_dafny.string_of(self.BOOL)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValue_BOOL) and self.BOOL == __o.BOOL
    def __hash__(self) -> int:
        return super().__hash__()


class AttributeValueUpdate:
    @classmethod
    def default(cls, ):
        return lambda: AttributeValueUpdate_AttributeValueUpdate(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AttributeValueUpdate(self) -> bool:
        return isinstance(self, AttributeValueUpdate_AttributeValueUpdate)

class AttributeValueUpdate_AttributeValueUpdate(AttributeValueUpdate, NamedTuple('AttributeValueUpdate', [('Value', Any), ('Action', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AttributeValueUpdate.AttributeValueUpdate({_dafny.string_of(self.Value)}, {_dafny.string_of(self.Action)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AttributeValueUpdate_AttributeValueUpdate) and self.Value == __o.Value and self.Action == __o.Action
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingPolicyDescription:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingPolicyDescription_AutoScalingPolicyDescription(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingPolicyDescription(self) -> bool:
        return isinstance(self, AutoScalingPolicyDescription_AutoScalingPolicyDescription)

class AutoScalingPolicyDescription_AutoScalingPolicyDescription(AutoScalingPolicyDescription, NamedTuple('AutoScalingPolicyDescription', [('PolicyName', Any), ('TargetTrackingScalingPolicyConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingPolicyDescription.AutoScalingPolicyDescription({_dafny.string_of(self.PolicyName)}, {_dafny.string_of(self.TargetTrackingScalingPolicyConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingPolicyDescription_AutoScalingPolicyDescription) and self.PolicyName == __o.PolicyName and self.TargetTrackingScalingPolicyConfiguration == __o.TargetTrackingScalingPolicyConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingPolicyName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_2_x_: _dafny.Seq = source__
        return default__.IsValid__AutoScalingPolicyName(d_2_x_)

class AutoScalingPolicyUpdate:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingPolicyUpdate_AutoScalingPolicyUpdate(Wrappers.Option.default()(), AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingPolicyUpdate(self) -> bool:
        return isinstance(self, AutoScalingPolicyUpdate_AutoScalingPolicyUpdate)

class AutoScalingPolicyUpdate_AutoScalingPolicyUpdate(AutoScalingPolicyUpdate, NamedTuple('AutoScalingPolicyUpdate', [('PolicyName', Any), ('TargetTrackingScalingPolicyConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingPolicyUpdate.AutoScalingPolicyUpdate({_dafny.string_of(self.PolicyName)}, {_dafny.string_of(self.TargetTrackingScalingPolicyConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingPolicyUpdate_AutoScalingPolicyUpdate) and self.PolicyName == __o.PolicyName and self.TargetTrackingScalingPolicyConfiguration == __o.TargetTrackingScalingPolicyConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingRoleArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_3_x_: _dafny.Seq = source__
        return default__.IsValid__AutoScalingRoleArn(d_3_x_)

class AutoScalingSettingsDescription:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingSettingsDescription_AutoScalingSettingsDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingSettingsDescription(self) -> bool:
        return isinstance(self, AutoScalingSettingsDescription_AutoScalingSettingsDescription)

class AutoScalingSettingsDescription_AutoScalingSettingsDescription(AutoScalingSettingsDescription, NamedTuple('AutoScalingSettingsDescription', [('MinimumUnits', Any), ('MaximumUnits', Any), ('AutoScalingDisabled', Any), ('AutoScalingRoleArn', Any), ('ScalingPolicies', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingSettingsDescription.AutoScalingSettingsDescription({_dafny.string_of(self.MinimumUnits)}, {_dafny.string_of(self.MaximumUnits)}, {_dafny.string_of(self.AutoScalingDisabled)}, {_dafny.string_of(self.AutoScalingRoleArn)}, {_dafny.string_of(self.ScalingPolicies)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingSettingsDescription_AutoScalingSettingsDescription) and self.MinimumUnits == __o.MinimumUnits and self.MaximumUnits == __o.MaximumUnits and self.AutoScalingDisabled == __o.AutoScalingDisabled and self.AutoScalingRoleArn == __o.AutoScalingRoleArn and self.ScalingPolicies == __o.ScalingPolicies
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingSettingsUpdate:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingSettingsUpdate_AutoScalingSettingsUpdate(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingSettingsUpdate(self) -> bool:
        return isinstance(self, AutoScalingSettingsUpdate_AutoScalingSettingsUpdate)

class AutoScalingSettingsUpdate_AutoScalingSettingsUpdate(AutoScalingSettingsUpdate, NamedTuple('AutoScalingSettingsUpdate', [('MinimumUnits', Any), ('MaximumUnits', Any), ('AutoScalingDisabled', Any), ('AutoScalingRoleArn', Any), ('ScalingPolicyUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingSettingsUpdate.AutoScalingSettingsUpdate({_dafny.string_of(self.MinimumUnits)}, {_dafny.string_of(self.MaximumUnits)}, {_dafny.string_of(self.AutoScalingDisabled)}, {_dafny.string_of(self.AutoScalingRoleArn)}, {_dafny.string_of(self.ScalingPolicyUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingSettingsUpdate_AutoScalingSettingsUpdate) and self.MinimumUnits == __o.MinimumUnits and self.MaximumUnits == __o.MaximumUnits and self.AutoScalingDisabled == __o.AutoScalingDisabled and self.AutoScalingRoleArn == __o.AutoScalingRoleArn and self.ScalingPolicyUpdate == __o.ScalingPolicyUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingTargetTrackingScalingPolicyConfigurationDescription:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingTargetTrackingScalingPolicyConfigurationDescription_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(self) -> bool:
        return isinstance(self, AutoScalingTargetTrackingScalingPolicyConfigurationDescription_AutoScalingTargetTrackingScalingPolicyConfigurationDescription)

class AutoScalingTargetTrackingScalingPolicyConfigurationDescription_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(AutoScalingTargetTrackingScalingPolicyConfigurationDescription, NamedTuple('AutoScalingTargetTrackingScalingPolicyConfigurationDescription', [('DisableScaleIn', Any), ('ScaleInCooldown', Any), ('ScaleOutCooldown', Any), ('TargetValue', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingTargetTrackingScalingPolicyConfigurationDescription.AutoScalingTargetTrackingScalingPolicyConfigurationDescription({_dafny.string_of(self.DisableScaleIn)}, {_dafny.string_of(self.ScaleInCooldown)}, {_dafny.string_of(self.ScaleOutCooldown)}, {_dafny.string_of(self.TargetValue)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingTargetTrackingScalingPolicyConfigurationDescription_AutoScalingTargetTrackingScalingPolicyConfigurationDescription) and self.DisableScaleIn == __o.DisableScaleIn and self.ScaleInCooldown == __o.ScaleInCooldown and self.ScaleOutCooldown == __o.ScaleOutCooldown and self.TargetValue == __o.TargetValue
    def __hash__(self) -> int:
        return super().__hash__()


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate:
    @classmethod
    def default(cls, ):
        return lambda: AutoScalingTargetTrackingScalingPolicyConfigurationUpdate_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(self) -> bool:
        return isinstance(self, AutoScalingTargetTrackingScalingPolicyConfigurationUpdate_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate)

class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(AutoScalingTargetTrackingScalingPolicyConfigurationUpdate, NamedTuple('AutoScalingTargetTrackingScalingPolicyConfigurationUpdate', [('DisableScaleIn', Any), ('ScaleInCooldown', Any), ('ScaleOutCooldown', Any), ('TargetValue', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate({_dafny.string_of(self.DisableScaleIn)}, {_dafny.string_of(self.ScaleInCooldown)}, {_dafny.string_of(self.ScaleOutCooldown)}, {_dafny.string_of(self.TargetValue)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AutoScalingTargetTrackingScalingPolicyConfigurationUpdate_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate) and self.DisableScaleIn == __o.DisableScaleIn and self.ScaleInCooldown == __o.ScaleInCooldown and self.ScaleOutCooldown == __o.ScaleOutCooldown and self.TargetValue == __o.TargetValue
    def __hash__(self) -> int:
        return super().__hash__()


class BackupArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_4_x_: _dafny.Seq = source__
        return default__.IsValid__BackupArn(d_4_x_)

class BackupDescription:
    @classmethod
    def default(cls, ):
        return lambda: BackupDescription_BackupDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BackupDescription(self) -> bool:
        return isinstance(self, BackupDescription_BackupDescription)

class BackupDescription_BackupDescription(BackupDescription, NamedTuple('BackupDescription', [('BackupDetails', Any), ('SourceTableDetails', Any), ('SourceTableFeatureDetails', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupDescription.BackupDescription({_dafny.string_of(self.BackupDetails)}, {_dafny.string_of(self.SourceTableDetails)}, {_dafny.string_of(self.SourceTableFeatureDetails)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupDescription_BackupDescription) and self.BackupDetails == __o.BackupDetails and self.SourceTableDetails == __o.SourceTableDetails and self.SourceTableFeatureDetails == __o.SourceTableFeatureDetails
    def __hash__(self) -> int:
        return super().__hash__()


class BackupDetails:
    @classmethod
    def default(cls, ):
        return lambda: BackupDetails_BackupDetails(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), BackupStatus.default()(), BackupType.default()(), _dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BackupDetails(self) -> bool:
        return isinstance(self, BackupDetails_BackupDetails)

class BackupDetails_BackupDetails(BackupDetails, NamedTuple('BackupDetails', [('BackupArn', Any), ('BackupName', Any), ('BackupSizeBytes', Any), ('BackupStatus', Any), ('BackupType', Any), ('BackupCreationDateTime', Any), ('BackupExpiryDateTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupDetails.BackupDetails({_dafny.string_of(self.BackupArn)}, {_dafny.string_of(self.BackupName)}, {_dafny.string_of(self.BackupSizeBytes)}, {_dafny.string_of(self.BackupStatus)}, {_dafny.string_of(self.BackupType)}, {_dafny.string_of(self.BackupCreationDateTime)}, {_dafny.string_of(self.BackupExpiryDateTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupDetails_BackupDetails) and self.BackupArn == __o.BackupArn and self.BackupName == __o.BackupName and self.BackupSizeBytes == __o.BackupSizeBytes and self.BackupStatus == __o.BackupStatus and self.BackupType == __o.BackupType and self.BackupCreationDateTime == __o.BackupCreationDateTime and self.BackupExpiryDateTime == __o.BackupExpiryDateTime
    def __hash__(self) -> int:
        return super().__hash__()


class BackupName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_5_x_: _dafny.Seq = source__
        return default__.IsValid__BackupName(d_5_x_)

class BackupsInputLimit:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_6_x_: int = source__
        if True:
            return default__.IsValid__BackupsInputLimit(d_6_x_)
        return False

class BackupSizeBytes:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_7_x_: int = source__
        if True:
            return default__.IsValid__BackupSizeBytes(d_7_x_)
        return False

class BackupStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [BackupStatus_CREATING(), BackupStatus_DELETED(), BackupStatus_AVAILABLE()]
    @classmethod
    def default(cls, ):
        return lambda: BackupStatus_CREATING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CREATING(self) -> bool:
        return isinstance(self, BackupStatus_CREATING)
    @property
    def is_DELETED(self) -> bool:
        return isinstance(self, BackupStatus_DELETED)
    @property
    def is_AVAILABLE(self) -> bool:
        return isinstance(self, BackupStatus_AVAILABLE)

class BackupStatus_CREATING(BackupStatus, NamedTuple('CREATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupStatus.CREATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupStatus_CREATING)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupStatus_DELETED(BackupStatus, NamedTuple('DELETED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupStatus.DELETED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupStatus_DELETED)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupStatus_AVAILABLE(BackupStatus, NamedTuple('AVAILABLE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupStatus.AVAILABLE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupStatus_AVAILABLE)
    def __hash__(self) -> int:
        return super().__hash__()


class BackupSummary:
    @classmethod
    def default(cls, ):
        return lambda: BackupSummary_BackupSummary(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BackupSummary(self) -> bool:
        return isinstance(self, BackupSummary_BackupSummary)

class BackupSummary_BackupSummary(BackupSummary, NamedTuple('BackupSummary', [('TableName', Any), ('TableId', Any), ('TableArn', Any), ('BackupArn', Any), ('BackupName', Any), ('BackupCreationDateTime', Any), ('BackupExpiryDateTime', Any), ('BackupStatus', Any), ('BackupType', Any), ('BackupSizeBytes', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupSummary.BackupSummary({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.TableId)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.BackupArn)}, {_dafny.string_of(self.BackupName)}, {_dafny.string_of(self.BackupCreationDateTime)}, {_dafny.string_of(self.BackupExpiryDateTime)}, {_dafny.string_of(self.BackupStatus)}, {_dafny.string_of(self.BackupType)}, {_dafny.string_of(self.BackupSizeBytes)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupSummary_BackupSummary) and self.TableName == __o.TableName and self.TableId == __o.TableId and self.TableArn == __o.TableArn and self.BackupArn == __o.BackupArn and self.BackupName == __o.BackupName and self.BackupCreationDateTime == __o.BackupCreationDateTime and self.BackupExpiryDateTime == __o.BackupExpiryDateTime and self.BackupStatus == __o.BackupStatus and self.BackupType == __o.BackupType and self.BackupSizeBytes == __o.BackupSizeBytes
    def __hash__(self) -> int:
        return super().__hash__()


class BackupType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [BackupType_USER(), BackupType_SYSTEM(), BackupType_AWS__BACKUP()]
    @classmethod
    def default(cls, ):
        return lambda: BackupType_USER()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_USER(self) -> bool:
        return isinstance(self, BackupType_USER)
    @property
    def is_SYSTEM(self) -> bool:
        return isinstance(self, BackupType_SYSTEM)
    @property
    def is_AWS__BACKUP(self) -> bool:
        return isinstance(self, BackupType_AWS__BACKUP)

class BackupType_USER(BackupType, NamedTuple('USER', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupType.USER'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupType_USER)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupType_SYSTEM(BackupType, NamedTuple('SYSTEM', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupType.SYSTEM'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupType_SYSTEM)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupType_AWS__BACKUP(BackupType, NamedTuple('AWS__BACKUP', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupType.AWS_BACKUP'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupType_AWS__BACKUP)
    def __hash__(self) -> int:
        return super().__hash__()


class BackupTypeFilter:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [BackupTypeFilter_USER(), BackupTypeFilter_SYSTEM(), BackupTypeFilter_AWS__BACKUP(), BackupTypeFilter_ALL()]
    @classmethod
    def default(cls, ):
        return lambda: BackupTypeFilter_USER()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_USER(self) -> bool:
        return isinstance(self, BackupTypeFilter_USER)
    @property
    def is_SYSTEM(self) -> bool:
        return isinstance(self, BackupTypeFilter_SYSTEM)
    @property
    def is_AWS__BACKUP(self) -> bool:
        return isinstance(self, BackupTypeFilter_AWS__BACKUP)
    @property
    def is_ALL(self) -> bool:
        return isinstance(self, BackupTypeFilter_ALL)

class BackupTypeFilter_USER(BackupTypeFilter, NamedTuple('USER', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupTypeFilter.USER'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupTypeFilter_USER)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupTypeFilter_SYSTEM(BackupTypeFilter, NamedTuple('SYSTEM', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupTypeFilter.SYSTEM'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupTypeFilter_SYSTEM)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupTypeFilter_AWS__BACKUP(BackupTypeFilter, NamedTuple('AWS__BACKUP', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupTypeFilter.AWS_BACKUP'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupTypeFilter_AWS__BACKUP)
    def __hash__(self) -> int:
        return super().__hash__()

class BackupTypeFilter_ALL(BackupTypeFilter, NamedTuple('ALL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BackupTypeFilter.ALL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BackupTypeFilter_ALL)
    def __hash__(self) -> int:
        return super().__hash__()


class BatchExecuteStatementInput:
    @classmethod
    def default(cls, ):
        return lambda: BatchExecuteStatementInput_BatchExecuteStatementInput(_dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchExecuteStatementInput(self) -> bool:
        return isinstance(self, BatchExecuteStatementInput_BatchExecuteStatementInput)

class BatchExecuteStatementInput_BatchExecuteStatementInput(BatchExecuteStatementInput, NamedTuple('BatchExecuteStatementInput', [('Statements', Any), ('ReturnConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchExecuteStatementInput.BatchExecuteStatementInput({_dafny.string_of(self.Statements)}, {_dafny.string_of(self.ReturnConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchExecuteStatementInput_BatchExecuteStatementInput) and self.Statements == __o.Statements and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class BatchExecuteStatementOutput:
    @classmethod
    def default(cls, ):
        return lambda: BatchExecuteStatementOutput_BatchExecuteStatementOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchExecuteStatementOutput(self) -> bool:
        return isinstance(self, BatchExecuteStatementOutput_BatchExecuteStatementOutput)

class BatchExecuteStatementOutput_BatchExecuteStatementOutput(BatchExecuteStatementOutput, NamedTuple('BatchExecuteStatementOutput', [('Responses', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchExecuteStatementOutput.BatchExecuteStatementOutput({_dafny.string_of(self.Responses)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchExecuteStatementOutput_BatchExecuteStatementOutput) and self.Responses == __o.Responses and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class BatchGetItemInput:
    @classmethod
    def default(cls, ):
        return lambda: BatchGetItemInput_BatchGetItemInput(_dafny.Map({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchGetItemInput(self) -> bool:
        return isinstance(self, BatchGetItemInput_BatchGetItemInput)

class BatchGetItemInput_BatchGetItemInput(BatchGetItemInput, NamedTuple('BatchGetItemInput', [('RequestItems', Any), ('ReturnConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchGetItemInput.BatchGetItemInput({_dafny.string_of(self.RequestItems)}, {_dafny.string_of(self.ReturnConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchGetItemInput_BatchGetItemInput) and self.RequestItems == __o.RequestItems and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class BatchGetItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: BatchGetItemOutput_BatchGetItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchGetItemOutput(self) -> bool:
        return isinstance(self, BatchGetItemOutput_BatchGetItemOutput)

class BatchGetItemOutput_BatchGetItemOutput(BatchGetItemOutput, NamedTuple('BatchGetItemOutput', [('Responses', Any), ('UnprocessedKeys', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchGetItemOutput.BatchGetItemOutput({_dafny.string_of(self.Responses)}, {_dafny.string_of(self.UnprocessedKeys)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchGetItemOutput_BatchGetItemOutput) and self.Responses == __o.Responses and self.UnprocessedKeys == __o.UnprocessedKeys and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class BatchGetRequestMap:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_8_x_: _dafny.Map = source__
        return default__.IsValid__BatchGetRequestMap(d_8_x_)

class BatchStatementError:
    @classmethod
    def default(cls, ):
        return lambda: BatchStatementError_BatchStatementError(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchStatementError(self) -> bool:
        return isinstance(self, BatchStatementError_BatchStatementError)

class BatchStatementError_BatchStatementError(BatchStatementError, NamedTuple('BatchStatementError', [('Code', Any), ('Message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementError.BatchStatementError({_dafny.string_of(self.Code)}, {_dafny.string_of(self.Message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementError_BatchStatementError) and self.Code == __o.Code and self.Message == __o.Message
    def __hash__(self) -> int:
        return super().__hash__()


class BatchStatementErrorCodeEnum:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [BatchStatementErrorCodeEnum_ConditionalCheckFailed(), BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded(), BatchStatementErrorCodeEnum_RequestLimitExceeded(), BatchStatementErrorCodeEnum_ValidationError(), BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded(), BatchStatementErrorCodeEnum_TransactionConflict(), BatchStatementErrorCodeEnum_ThrottlingError(), BatchStatementErrorCodeEnum_InternalServerError(), BatchStatementErrorCodeEnum_ResourceNotFound(), BatchStatementErrorCodeEnum_AccessDenied(), BatchStatementErrorCodeEnum_DuplicateItem()]
    @classmethod
    def default(cls, ):
        return lambda: BatchStatementErrorCodeEnum_ConditionalCheckFailed()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ConditionalCheckFailed(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ConditionalCheckFailed)
    @property
    def is_ItemCollectionSizeLimitExceeded(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded)
    @property
    def is_RequestLimitExceeded(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_RequestLimitExceeded)
    @property
    def is_ValidationError(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ValidationError)
    @property
    def is_ProvisionedThroughputExceeded(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded)
    @property
    def is_TransactionConflict(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_TransactionConflict)
    @property
    def is_ThrottlingError(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ThrottlingError)
    @property
    def is_InternalServerError(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_InternalServerError)
    @property
    def is_ResourceNotFound(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_ResourceNotFound)
    @property
    def is_AccessDenied(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_AccessDenied)
    @property
    def is_DuplicateItem(self) -> bool:
        return isinstance(self, BatchStatementErrorCodeEnum_DuplicateItem)

class BatchStatementErrorCodeEnum_ConditionalCheckFailed(BatchStatementErrorCodeEnum, NamedTuple('ConditionalCheckFailed', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ConditionalCheckFailed'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ConditionalCheckFailed)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded(BatchStatementErrorCodeEnum, NamedTuple('ItemCollectionSizeLimitExceeded', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ItemCollectionSizeLimitExceeded'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_RequestLimitExceeded(BatchStatementErrorCodeEnum, NamedTuple('RequestLimitExceeded', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.RequestLimitExceeded'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_RequestLimitExceeded)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_ValidationError(BatchStatementErrorCodeEnum, NamedTuple('ValidationError', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ValidationError'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ValidationError)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded(BatchStatementErrorCodeEnum, NamedTuple('ProvisionedThroughputExceeded', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ProvisionedThroughputExceeded'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_TransactionConflict(BatchStatementErrorCodeEnum, NamedTuple('TransactionConflict', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.TransactionConflict'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_TransactionConflict)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_ThrottlingError(BatchStatementErrorCodeEnum, NamedTuple('ThrottlingError', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ThrottlingError'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ThrottlingError)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_InternalServerError(BatchStatementErrorCodeEnum, NamedTuple('InternalServerError', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.InternalServerError'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_InternalServerError)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_ResourceNotFound(BatchStatementErrorCodeEnum, NamedTuple('ResourceNotFound', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.ResourceNotFound'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_ResourceNotFound)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_AccessDenied(BatchStatementErrorCodeEnum, NamedTuple('AccessDenied', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.AccessDenied'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_AccessDenied)
    def __hash__(self) -> int:
        return super().__hash__()

class BatchStatementErrorCodeEnum_DuplicateItem(BatchStatementErrorCodeEnum, NamedTuple('DuplicateItem', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementErrorCodeEnum.DuplicateItem'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementErrorCodeEnum_DuplicateItem)
    def __hash__(self) -> int:
        return super().__hash__()


class BatchStatementRequest:
    @classmethod
    def default(cls, ):
        return lambda: BatchStatementRequest_BatchStatementRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchStatementRequest(self) -> bool:
        return isinstance(self, BatchStatementRequest_BatchStatementRequest)

class BatchStatementRequest_BatchStatementRequest(BatchStatementRequest, NamedTuple('BatchStatementRequest', [('Statement', Any), ('Parameters', Any), ('ConsistentRead', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementRequest.BatchStatementRequest({_dafny.string_of(self.Statement)}, {_dafny.string_of(self.Parameters)}, {_dafny.string_of(self.ConsistentRead)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementRequest_BatchStatementRequest) and self.Statement == __o.Statement and self.Parameters == __o.Parameters and self.ConsistentRead == __o.ConsistentRead
    def __hash__(self) -> int:
        return super().__hash__()


class BatchStatementResponse:
    @classmethod
    def default(cls, ):
        return lambda: BatchStatementResponse_BatchStatementResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchStatementResponse(self) -> bool:
        return isinstance(self, BatchStatementResponse_BatchStatementResponse)

class BatchStatementResponse_BatchStatementResponse(BatchStatementResponse, NamedTuple('BatchStatementResponse', [('Error', Any), ('TableName', Any), ('Item', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchStatementResponse.BatchStatementResponse({_dafny.string_of(self.Error)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Item)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchStatementResponse_BatchStatementResponse) and self.Error == __o.Error and self.TableName == __o.TableName and self.Item == __o.Item
    def __hash__(self) -> int:
        return super().__hash__()


class BatchWriteItemInput:
    @classmethod
    def default(cls, ):
        return lambda: BatchWriteItemInput_BatchWriteItemInput(_dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchWriteItemInput(self) -> bool:
        return isinstance(self, BatchWriteItemInput_BatchWriteItemInput)

class BatchWriteItemInput_BatchWriteItemInput(BatchWriteItemInput, NamedTuple('BatchWriteItemInput', [('RequestItems', Any), ('ReturnConsumedCapacity', Any), ('ReturnItemCollectionMetrics', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchWriteItemInput.BatchWriteItemInput({_dafny.string_of(self.RequestItems)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ReturnItemCollectionMetrics)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchWriteItemInput_BatchWriteItemInput) and self.RequestItems == __o.RequestItems and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ReturnItemCollectionMetrics == __o.ReturnItemCollectionMetrics
    def __hash__(self) -> int:
        return super().__hash__()


class BatchWriteItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: BatchWriteItemOutput_BatchWriteItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BatchWriteItemOutput(self) -> bool:
        return isinstance(self, BatchWriteItemOutput_BatchWriteItemOutput)

class BatchWriteItemOutput_BatchWriteItemOutput(BatchWriteItemOutput, NamedTuple('BatchWriteItemOutput', [('UnprocessedItems', Any), ('ItemCollectionMetrics', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BatchWriteItemOutput.BatchWriteItemOutput({_dafny.string_of(self.UnprocessedItems)}, {_dafny.string_of(self.ItemCollectionMetrics)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BatchWriteItemOutput_BatchWriteItemOutput) and self.UnprocessedItems == __o.UnprocessedItems and self.ItemCollectionMetrics == __o.ItemCollectionMetrics and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class BatchWriteItemRequestMap:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_9_x_: _dafny.Map = source__
        return default__.IsValid__BatchWriteItemRequestMap(d_9_x_)

class BilledSizeBytes:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_10_x_: int = source__
        if True:
            return default__.IsValid__BilledSizeBytes(d_10_x_)
        return False

class BillingMode:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [BillingMode_PROVISIONED(), BillingMode_PAY__PER__REQUEST()]
    @classmethod
    def default(cls, ):
        return lambda: BillingMode_PROVISIONED()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PROVISIONED(self) -> bool:
        return isinstance(self, BillingMode_PROVISIONED)
    @property
    def is_PAY__PER__REQUEST(self) -> bool:
        return isinstance(self, BillingMode_PAY__PER__REQUEST)

class BillingMode_PROVISIONED(BillingMode, NamedTuple('PROVISIONED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BillingMode.PROVISIONED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BillingMode_PROVISIONED)
    def __hash__(self) -> int:
        return super().__hash__()

class BillingMode_PAY__PER__REQUEST(BillingMode, NamedTuple('PAY__PER__REQUEST', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BillingMode.PAY_PER_REQUEST'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BillingMode_PAY__PER__REQUEST)
    def __hash__(self) -> int:
        return super().__hash__()


class BillingModeSummary:
    @classmethod
    def default(cls, ):
        return lambda: BillingModeSummary_BillingModeSummary(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BillingModeSummary(self) -> bool:
        return isinstance(self, BillingModeSummary_BillingModeSummary)

class BillingModeSummary_BillingModeSummary(BillingModeSummary, NamedTuple('BillingModeSummary', [('BillingMode', Any), ('LastUpdateToPayPerRequestDateTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.BillingModeSummary.BillingModeSummary({_dafny.string_of(self.BillingMode)}, {_dafny.string_of(self.LastUpdateToPayPerRequestDateTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BillingModeSummary_BillingModeSummary) and self.BillingMode == __o.BillingMode and self.LastUpdateToPayPerRequestDateTime == __o.LastUpdateToPayPerRequestDateTime
    def __hash__(self) -> int:
        return super().__hash__()


class CancellationReason:
    @classmethod
    def default(cls, ):
        return lambda: CancellationReason_CancellationReason(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CancellationReason(self) -> bool:
        return isinstance(self, CancellationReason_CancellationReason)

class CancellationReason_CancellationReason(CancellationReason, NamedTuple('CancellationReason', [('Item', Any), ('Code', Any), ('Message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CancellationReason.CancellationReason({_dafny.string_of(self.Item)}, {_dafny.string_of(self.Code)}, {_dafny.string_of(self.Message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CancellationReason_CancellationReason) and self.Item == __o.Item and self.Code == __o.Code and self.Message == __o.Message
    def __hash__(self) -> int:
        return super().__hash__()


class CancellationReasonList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_11_x_: _dafny.Seq = source__
        return default__.IsValid__CancellationReasonList(d_11_x_)

class Capacity:
    @classmethod
    def default(cls, ):
        return lambda: Capacity_Capacity(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Capacity(self) -> bool:
        return isinstance(self, Capacity_Capacity)

class Capacity_Capacity(Capacity, NamedTuple('Capacity', [('ReadCapacityUnits', Any), ('WriteCapacityUnits', Any), ('CapacityUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Capacity.Capacity({_dafny.string_of(self.ReadCapacityUnits)}, {_dafny.string_of(self.WriteCapacityUnits)}, {_dafny.string_of(self.CapacityUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Capacity_Capacity) and self.ReadCapacityUnits == __o.ReadCapacityUnits and self.WriteCapacityUnits == __o.WriteCapacityUnits and self.CapacityUnits == __o.CapacityUnits
    def __hash__(self) -> int:
        return super().__hash__()


class ClientRequestToken:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_12_x_: _dafny.Seq = source__
        return default__.IsValid__ClientRequestToken(d_12_x_)

class CloudWatchLogGroupArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_13_x_: _dafny.Seq = source__
        return default__.IsValid__CloudWatchLogGroupArn(d_13_x_)

class ComparisonOperator:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ComparisonOperator_EQ(), ComparisonOperator_NE(), ComparisonOperator_IN(), ComparisonOperator_LE(), ComparisonOperator_LT(), ComparisonOperator_GE(), ComparisonOperator_GT(), ComparisonOperator_BETWEEN(), ComparisonOperator_NOT__NULL(), ComparisonOperator_NULL(), ComparisonOperator_CONTAINS(), ComparisonOperator_NOT__CONTAINS(), ComparisonOperator_BEGINS__WITH()]
    @classmethod
    def default(cls, ):
        return lambda: ComparisonOperator_EQ()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EQ(self) -> bool:
        return isinstance(self, ComparisonOperator_EQ)
    @property
    def is_NE(self) -> bool:
        return isinstance(self, ComparisonOperator_NE)
    @property
    def is_IN(self) -> bool:
        return isinstance(self, ComparisonOperator_IN)
    @property
    def is_LE(self) -> bool:
        return isinstance(self, ComparisonOperator_LE)
    @property
    def is_LT(self) -> bool:
        return isinstance(self, ComparisonOperator_LT)
    @property
    def is_GE(self) -> bool:
        return isinstance(self, ComparisonOperator_GE)
    @property
    def is_GT(self) -> bool:
        return isinstance(self, ComparisonOperator_GT)
    @property
    def is_BETWEEN(self) -> bool:
        return isinstance(self, ComparisonOperator_BETWEEN)
    @property
    def is_NOT__NULL(self) -> bool:
        return isinstance(self, ComparisonOperator_NOT__NULL)
    @property
    def is_NULL(self) -> bool:
        return isinstance(self, ComparisonOperator_NULL)
    @property
    def is_CONTAINS(self) -> bool:
        return isinstance(self, ComparisonOperator_CONTAINS)
    @property
    def is_NOT__CONTAINS(self) -> bool:
        return isinstance(self, ComparisonOperator_NOT__CONTAINS)
    @property
    def is_BEGINS__WITH(self) -> bool:
        return isinstance(self, ComparisonOperator_BEGINS__WITH)

class ComparisonOperator_EQ(ComparisonOperator, NamedTuple('EQ', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.EQ'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_EQ)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_NE(ComparisonOperator, NamedTuple('NE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.NE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_NE)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_IN(ComparisonOperator, NamedTuple('IN', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.IN'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_IN)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_LE(ComparisonOperator, NamedTuple('LE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.LE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_LE)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_LT(ComparisonOperator, NamedTuple('LT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.LT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_LT)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_GE(ComparisonOperator, NamedTuple('GE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.GE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_GE)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_GT(ComparisonOperator, NamedTuple('GT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.GT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_GT)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_BETWEEN(ComparisonOperator, NamedTuple('BETWEEN', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.BETWEEN'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_BETWEEN)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_NOT__NULL(ComparisonOperator, NamedTuple('NOT__NULL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.NOT_NULL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_NOT__NULL)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_NULL(ComparisonOperator, NamedTuple('NULL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.NULL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_NULL)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_CONTAINS(ComparisonOperator, NamedTuple('CONTAINS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.CONTAINS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_CONTAINS)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_NOT__CONTAINS(ComparisonOperator, NamedTuple('NOT__CONTAINS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.NOT_CONTAINS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_NOT__CONTAINS)
    def __hash__(self) -> int:
        return super().__hash__()

class ComparisonOperator_BEGINS__WITH(ComparisonOperator, NamedTuple('BEGINS__WITH', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ComparisonOperator.BEGINS_WITH'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ComparisonOperator_BEGINS__WITH)
    def __hash__(self) -> int:
        return super().__hash__()


class Condition:
    @classmethod
    def default(cls, ):
        return lambda: Condition_Condition(Wrappers.Option.default()(), ComparisonOperator.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Condition(self) -> bool:
        return isinstance(self, Condition_Condition)

class Condition_Condition(Condition, NamedTuple('Condition', [('AttributeValueList', Any), ('ComparisonOperator', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Condition.Condition({_dafny.string_of(self.AttributeValueList)}, {_dafny.string_of(self.ComparisonOperator)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Condition_Condition) and self.AttributeValueList == __o.AttributeValueList and self.ComparisonOperator == __o.ComparisonOperator
    def __hash__(self) -> int:
        return super().__hash__()


class ConditionalOperator:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConditionalOperator_AND(), ConditionalOperator_OR()]
    @classmethod
    def default(cls, ):
        return lambda: ConditionalOperator_AND()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AND(self) -> bool:
        return isinstance(self, ConditionalOperator_AND)
    @property
    def is_OR(self) -> bool:
        return isinstance(self, ConditionalOperator_OR)

class ConditionalOperator_AND(ConditionalOperator, NamedTuple('AND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ConditionalOperator.AND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionalOperator_AND)
    def __hash__(self) -> int:
        return super().__hash__()

class ConditionalOperator_OR(ConditionalOperator, NamedTuple('OR', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ConditionalOperator.OR'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionalOperator_OR)
    def __hash__(self) -> int:
        return super().__hash__()


class ConditionCheck:
    @classmethod
    def default(cls, ):
        return lambda: ConditionCheck_ConditionCheck(_dafny.Map({}), _dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ConditionCheck(self) -> bool:
        return isinstance(self, ConditionCheck_ConditionCheck)

class ConditionCheck_ConditionCheck(ConditionCheck, NamedTuple('ConditionCheck', [('Key', Any), ('TableName', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any), ('ReturnValuesOnConditionCheckFailure', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ConditionCheck.ConditionCheck({_dafny.string_of(self.Key)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)}, {_dafny.string_of(self.ReturnValuesOnConditionCheckFailure)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionCheck_ConditionCheck) and self.Key == __o.Key and self.TableName == __o.TableName and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues and self.ReturnValuesOnConditionCheckFailure == __o.ReturnValuesOnConditionCheckFailure
    def __hash__(self) -> int:
        return super().__hash__()


class ConsumedCapacity:
    @classmethod
    def default(cls, ):
        return lambda: ConsumedCapacity_ConsumedCapacity(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ConsumedCapacity(self) -> bool:
        return isinstance(self, ConsumedCapacity_ConsumedCapacity)

class ConsumedCapacity_ConsumedCapacity(ConsumedCapacity, NamedTuple('ConsumedCapacity', [('TableName', Any), ('CapacityUnits', Any), ('ReadCapacityUnits', Any), ('WriteCapacityUnits', Any), ('Table', Any), ('LocalSecondaryIndexes', Any), ('GlobalSecondaryIndexes', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ConsumedCapacity.ConsumedCapacity({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.CapacityUnits)}, {_dafny.string_of(self.ReadCapacityUnits)}, {_dafny.string_of(self.WriteCapacityUnits)}, {_dafny.string_of(self.Table)}, {_dafny.string_of(self.LocalSecondaryIndexes)}, {_dafny.string_of(self.GlobalSecondaryIndexes)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConsumedCapacity_ConsumedCapacity) and self.TableName == __o.TableName and self.CapacityUnits == __o.CapacityUnits and self.ReadCapacityUnits == __o.ReadCapacityUnits and self.WriteCapacityUnits == __o.WriteCapacityUnits and self.Table == __o.Table and self.LocalSecondaryIndexes == __o.LocalSecondaryIndexes and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes
    def __hash__(self) -> int:
        return super().__hash__()


class ConsumedCapacityUnits:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_14_x_: _dafny.Seq = source__
        return default__.IsValid__ConsumedCapacityUnits(d_14_x_)

class ContinuousBackupsDescription:
    @classmethod
    def default(cls, ):
        return lambda: ContinuousBackupsDescription_ContinuousBackupsDescription(ContinuousBackupsStatus.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ContinuousBackupsDescription(self) -> bool:
        return isinstance(self, ContinuousBackupsDescription_ContinuousBackupsDescription)

class ContinuousBackupsDescription_ContinuousBackupsDescription(ContinuousBackupsDescription, NamedTuple('ContinuousBackupsDescription', [('ContinuousBackupsStatus', Any), ('PointInTimeRecoveryDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContinuousBackupsDescription.ContinuousBackupsDescription({_dafny.string_of(self.ContinuousBackupsStatus)}, {_dafny.string_of(self.PointInTimeRecoveryDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContinuousBackupsDescription_ContinuousBackupsDescription) and self.ContinuousBackupsStatus == __o.ContinuousBackupsStatus and self.PointInTimeRecoveryDescription == __o.PointInTimeRecoveryDescription
    def __hash__(self) -> int:
        return super().__hash__()


class ContinuousBackupsStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ContinuousBackupsStatus_ENABLED(), ContinuousBackupsStatus_DISABLED()]
    @classmethod
    def default(cls, ):
        return lambda: ContinuousBackupsStatus_ENABLED()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLED(self) -> bool:
        return isinstance(self, ContinuousBackupsStatus_ENABLED)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, ContinuousBackupsStatus_DISABLED)

class ContinuousBackupsStatus_ENABLED(ContinuousBackupsStatus, NamedTuple('ENABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContinuousBackupsStatus.ENABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContinuousBackupsStatus_ENABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class ContinuousBackupsStatus_DISABLED(ContinuousBackupsStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContinuousBackupsStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContinuousBackupsStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()


class ContributorInsightsAction:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ContributorInsightsAction_ENABLE(), ContributorInsightsAction_DISABLE()]
    @classmethod
    def default(cls, ):
        return lambda: ContributorInsightsAction_ENABLE()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLE(self) -> bool:
        return isinstance(self, ContributorInsightsAction_ENABLE)
    @property
    def is_DISABLE(self) -> bool:
        return isinstance(self, ContributorInsightsAction_DISABLE)

class ContributorInsightsAction_ENABLE(ContributorInsightsAction, NamedTuple('ENABLE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsAction.ENABLE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsAction_ENABLE)
    def __hash__(self) -> int:
        return super().__hash__()

class ContributorInsightsAction_DISABLE(ContributorInsightsAction, NamedTuple('DISABLE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsAction.DISABLE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsAction_DISABLE)
    def __hash__(self) -> int:
        return super().__hash__()


class ContributorInsightsStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ContributorInsightsStatus_ENABLING(), ContributorInsightsStatus_ENABLED(), ContributorInsightsStatus_DISABLING(), ContributorInsightsStatus_DISABLED(), ContributorInsightsStatus_FAILED()]
    @classmethod
    def default(cls, ):
        return lambda: ContributorInsightsStatus_ENABLING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLING(self) -> bool:
        return isinstance(self, ContributorInsightsStatus_ENABLING)
    @property
    def is_ENABLED(self) -> bool:
        return isinstance(self, ContributorInsightsStatus_ENABLED)
    @property
    def is_DISABLING(self) -> bool:
        return isinstance(self, ContributorInsightsStatus_DISABLING)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, ContributorInsightsStatus_DISABLED)
    @property
    def is_FAILED(self) -> bool:
        return isinstance(self, ContributorInsightsStatus_FAILED)

class ContributorInsightsStatus_ENABLING(ContributorInsightsStatus, NamedTuple('ENABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsStatus.ENABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsStatus_ENABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class ContributorInsightsStatus_ENABLED(ContributorInsightsStatus, NamedTuple('ENABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsStatus.ENABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsStatus_ENABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class ContributorInsightsStatus_DISABLING(ContributorInsightsStatus, NamedTuple('DISABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsStatus.DISABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsStatus_DISABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class ContributorInsightsStatus_DISABLED(ContributorInsightsStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class ContributorInsightsStatus_FAILED(ContributorInsightsStatus, NamedTuple('FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsStatus.FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsStatus_FAILED)
    def __hash__(self) -> int:
        return super().__hash__()


class ContributorInsightsSummary:
    @classmethod
    def default(cls, ):
        return lambda: ContributorInsightsSummary_ContributorInsightsSummary(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ContributorInsightsSummary(self) -> bool:
        return isinstance(self, ContributorInsightsSummary_ContributorInsightsSummary)

class ContributorInsightsSummary_ContributorInsightsSummary(ContributorInsightsSummary, NamedTuple('ContributorInsightsSummary', [('TableName', Any), ('IndexName', Any), ('ContributorInsightsStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ContributorInsightsSummary.ContributorInsightsSummary({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ContributorInsightsStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ContributorInsightsSummary_ContributorInsightsSummary) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.ContributorInsightsStatus == __o.ContributorInsightsStatus
    def __hash__(self) -> int:
        return super().__hash__()


class CreateBackupInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateBackupInput_CreateBackupInput(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateBackupInput(self) -> bool:
        return isinstance(self, CreateBackupInput_CreateBackupInput)

class CreateBackupInput_CreateBackupInput(CreateBackupInput, NamedTuple('CreateBackupInput', [('TableName', Any), ('BackupName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateBackupInput.CreateBackupInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.BackupName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateBackupInput_CreateBackupInput) and self.TableName == __o.TableName and self.BackupName == __o.BackupName
    def __hash__(self) -> int:
        return super().__hash__()


class CreateBackupOutput:
    @classmethod
    def default(cls, ):
        return lambda: CreateBackupOutput_CreateBackupOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateBackupOutput(self) -> bool:
        return isinstance(self, CreateBackupOutput_CreateBackupOutput)

class CreateBackupOutput_CreateBackupOutput(CreateBackupOutput, NamedTuple('CreateBackupOutput', [('BackupDetails', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateBackupOutput.CreateBackupOutput({_dafny.string_of(self.BackupDetails)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateBackupOutput_CreateBackupOutput) and self.BackupDetails == __o.BackupDetails
    def __hash__(self) -> int:
        return super().__hash__()


class CreateGlobalSecondaryIndexAction:
    @classmethod
    def default(cls, ):
        return lambda: CreateGlobalSecondaryIndexAction_CreateGlobalSecondaryIndexAction(_dafny.Seq(""), _dafny.Seq({}), Projection.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateGlobalSecondaryIndexAction(self) -> bool:
        return isinstance(self, CreateGlobalSecondaryIndexAction_CreateGlobalSecondaryIndexAction)

class CreateGlobalSecondaryIndexAction_CreateGlobalSecondaryIndexAction(CreateGlobalSecondaryIndexAction, NamedTuple('CreateGlobalSecondaryIndexAction', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any), ('ProvisionedThroughput', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateGlobalSecondaryIndexAction.CreateGlobalSecondaryIndexAction({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)}, {_dafny.string_of(self.ProvisionedThroughput)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateGlobalSecondaryIndexAction_CreateGlobalSecondaryIndexAction) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection and self.ProvisionedThroughput == __o.ProvisionedThroughput
    def __hash__(self) -> int:
        return super().__hash__()


class CreateGlobalTableInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateGlobalTableInput_CreateGlobalTableInput(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateGlobalTableInput(self) -> bool:
        return isinstance(self, CreateGlobalTableInput_CreateGlobalTableInput)

class CreateGlobalTableInput_CreateGlobalTableInput(CreateGlobalTableInput, NamedTuple('CreateGlobalTableInput', [('GlobalTableName', Any), ('ReplicationGroup', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateGlobalTableInput.CreateGlobalTableInput({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.ReplicationGroup)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateGlobalTableInput_CreateGlobalTableInput) and self.GlobalTableName == __o.GlobalTableName and self.ReplicationGroup == __o.ReplicationGroup
    def __hash__(self) -> int:
        return super().__hash__()


class CreateGlobalTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: CreateGlobalTableOutput_CreateGlobalTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateGlobalTableOutput(self) -> bool:
        return isinstance(self, CreateGlobalTableOutput_CreateGlobalTableOutput)

class CreateGlobalTableOutput_CreateGlobalTableOutput(CreateGlobalTableOutput, NamedTuple('CreateGlobalTableOutput', [('GlobalTableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateGlobalTableOutput.CreateGlobalTableOutput({_dafny.string_of(self.GlobalTableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateGlobalTableOutput_CreateGlobalTableOutput) and self.GlobalTableDescription == __o.GlobalTableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class CreateReplicaAction:
    @classmethod
    def default(cls, ):
        return lambda: CreateReplicaAction_CreateReplicaAction(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateReplicaAction(self) -> bool:
        return isinstance(self, CreateReplicaAction_CreateReplicaAction)

class CreateReplicaAction_CreateReplicaAction(CreateReplicaAction, NamedTuple('CreateReplicaAction', [('RegionName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateReplicaAction.CreateReplicaAction({_dafny.string_of(self.RegionName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateReplicaAction_CreateReplicaAction) and self.RegionName == __o.RegionName
    def __hash__(self) -> int:
        return super().__hash__()


class CreateReplicationGroupMemberAction:
    @classmethod
    def default(cls, ):
        return lambda: CreateReplicationGroupMemberAction_CreateReplicationGroupMemberAction(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateReplicationGroupMemberAction(self) -> bool:
        return isinstance(self, CreateReplicationGroupMemberAction_CreateReplicationGroupMemberAction)

class CreateReplicationGroupMemberAction_CreateReplicationGroupMemberAction(CreateReplicationGroupMemberAction, NamedTuple('CreateReplicationGroupMemberAction', [('RegionName', Any), ('KMSMasterKeyId', Any), ('ProvisionedThroughputOverride', Any), ('GlobalSecondaryIndexes', Any), ('TableClassOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateReplicationGroupMemberAction.CreateReplicationGroupMemberAction({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.KMSMasterKeyId)}, {_dafny.string_of(self.ProvisionedThroughputOverride)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.TableClassOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateReplicationGroupMemberAction_CreateReplicationGroupMemberAction) and self.RegionName == __o.RegionName and self.KMSMasterKeyId == __o.KMSMasterKeyId and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.TableClassOverride == __o.TableClassOverride
    def __hash__(self) -> int:
        return super().__hash__()


class CreateTableInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateTableInput_CreateTableInput(_dafny.Seq({}), _dafny.Seq(""), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateTableInput(self) -> bool:
        return isinstance(self, CreateTableInput_CreateTableInput)

class CreateTableInput_CreateTableInput(CreateTableInput, NamedTuple('CreateTableInput', [('AttributeDefinitions', Any), ('TableName', Any), ('KeySchema', Any), ('LocalSecondaryIndexes', Any), ('GlobalSecondaryIndexes', Any), ('BillingMode', Any), ('ProvisionedThroughput', Any), ('StreamSpecification', Any), ('SSESpecification', Any), ('Tags', Any), ('TableClass', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateTableInput.CreateTableInput({_dafny.string_of(self.AttributeDefinitions)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.LocalSecondaryIndexes)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.BillingMode)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.StreamSpecification)}, {_dafny.string_of(self.SSESpecification)}, {_dafny.string_of(self.Tags)}, {_dafny.string_of(self.TableClass)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateTableInput_CreateTableInput) and self.AttributeDefinitions == __o.AttributeDefinitions and self.TableName == __o.TableName and self.KeySchema == __o.KeySchema and self.LocalSecondaryIndexes == __o.LocalSecondaryIndexes and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.BillingMode == __o.BillingMode and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.StreamSpecification == __o.StreamSpecification and self.SSESpecification == __o.SSESpecification and self.Tags == __o.Tags and self.TableClass == __o.TableClass
    def __hash__(self) -> int:
        return super().__hash__()


class CreateTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: CreateTableOutput_CreateTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateTableOutput(self) -> bool:
        return isinstance(self, CreateTableOutput_CreateTableOutput)

class CreateTableOutput_CreateTableOutput(CreateTableOutput, NamedTuple('CreateTableOutput', [('TableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CreateTableOutput.CreateTableOutput({_dafny.string_of(self.TableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateTableOutput_CreateTableOutput) and self.TableDescription == __o.TableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class CsvDelimiter:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_15_x_: _dafny.Seq = source__
        return default__.IsValid__CsvDelimiter(d_15_x_)

class CsvHeader:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_16_x_: _dafny.Seq = source__
        return default__.IsValid__CsvHeader(d_16_x_)

class CsvHeaderList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_17_x_: _dafny.Seq = source__
        return default__.IsValid__CsvHeaderList(d_17_x_)

class CsvOptions:
    @classmethod
    def default(cls, ):
        return lambda: CsvOptions_CsvOptions(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CsvOptions(self) -> bool:
        return isinstance(self, CsvOptions_CsvOptions)

class CsvOptions_CsvOptions(CsvOptions, NamedTuple('CsvOptions', [('Delimiter', Any), ('HeaderList', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.CsvOptions.CsvOptions({_dafny.string_of(self.Delimiter)}, {_dafny.string_of(self.HeaderList)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CsvOptions_CsvOptions) and self.Delimiter == __o.Delimiter and self.HeaderList == __o.HeaderList
    def __hash__(self) -> int:
        return super().__hash__()


class Delete:
    @classmethod
    def default(cls, ):
        return lambda: Delete_Delete(_dafny.Map({}), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Delete(self) -> bool:
        return isinstance(self, Delete_Delete)

class Delete_Delete(Delete, NamedTuple('Delete', [('Key', Any), ('TableName', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any), ('ReturnValuesOnConditionCheckFailure', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Delete.Delete({_dafny.string_of(self.Key)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)}, {_dafny.string_of(self.ReturnValuesOnConditionCheckFailure)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Delete_Delete) and self.Key == __o.Key and self.TableName == __o.TableName and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues and self.ReturnValuesOnConditionCheckFailure == __o.ReturnValuesOnConditionCheckFailure
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteBackupInput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteBackupInput_DeleteBackupInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteBackupInput(self) -> bool:
        return isinstance(self, DeleteBackupInput_DeleteBackupInput)

class DeleteBackupInput_DeleteBackupInput(DeleteBackupInput, NamedTuple('DeleteBackupInput', [('BackupArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteBackupInput.DeleteBackupInput({_dafny.string_of(self.BackupArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteBackupInput_DeleteBackupInput) and self.BackupArn == __o.BackupArn
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteBackupOutput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteBackupOutput_DeleteBackupOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteBackupOutput(self) -> bool:
        return isinstance(self, DeleteBackupOutput_DeleteBackupOutput)

class DeleteBackupOutput_DeleteBackupOutput(DeleteBackupOutput, NamedTuple('DeleteBackupOutput', [('BackupDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteBackupOutput.DeleteBackupOutput({_dafny.string_of(self.BackupDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteBackupOutput_DeleteBackupOutput) and self.BackupDescription == __o.BackupDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteGlobalSecondaryIndexAction:
    @classmethod
    def default(cls, ):
        return lambda: DeleteGlobalSecondaryIndexAction_DeleteGlobalSecondaryIndexAction(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteGlobalSecondaryIndexAction(self) -> bool:
        return isinstance(self, DeleteGlobalSecondaryIndexAction_DeleteGlobalSecondaryIndexAction)

class DeleteGlobalSecondaryIndexAction_DeleteGlobalSecondaryIndexAction(DeleteGlobalSecondaryIndexAction, NamedTuple('DeleteGlobalSecondaryIndexAction', [('IndexName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteGlobalSecondaryIndexAction.DeleteGlobalSecondaryIndexAction({_dafny.string_of(self.IndexName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteGlobalSecondaryIndexAction_DeleteGlobalSecondaryIndexAction) and self.IndexName == __o.IndexName
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteItemInput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteItemInput_DeleteItemInput(_dafny.Seq(""), _dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteItemInput(self) -> bool:
        return isinstance(self, DeleteItemInput_DeleteItemInput)

class DeleteItemInput_DeleteItemInput(DeleteItemInput, NamedTuple('DeleteItemInput', [('TableName', Any), ('Key', Any), ('Expected', Any), ('ConditionalOperator', Any), ('ReturnValues', Any), ('ReturnConsumedCapacity', Any), ('ReturnItemCollectionMetrics', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteItemInput.DeleteItemInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Key)}, {_dafny.string_of(self.Expected)}, {_dafny.string_of(self.ConditionalOperator)}, {_dafny.string_of(self.ReturnValues)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ReturnItemCollectionMetrics)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteItemInput_DeleteItemInput) and self.TableName == __o.TableName and self.Key == __o.Key and self.Expected == __o.Expected and self.ConditionalOperator == __o.ConditionalOperator and self.ReturnValues == __o.ReturnValues and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ReturnItemCollectionMetrics == __o.ReturnItemCollectionMetrics and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteItemOutput_DeleteItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteItemOutput(self) -> bool:
        return isinstance(self, DeleteItemOutput_DeleteItemOutput)

class DeleteItemOutput_DeleteItemOutput(DeleteItemOutput, NamedTuple('DeleteItemOutput', [('Attributes', Any), ('ConsumedCapacity', Any), ('ItemCollectionMetrics', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteItemOutput.DeleteItemOutput({_dafny.string_of(self.Attributes)}, {_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.ItemCollectionMetrics)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteItemOutput_DeleteItemOutput) and self.Attributes == __o.Attributes and self.ConsumedCapacity == __o.ConsumedCapacity and self.ItemCollectionMetrics == __o.ItemCollectionMetrics
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteReplicaAction:
    @classmethod
    def default(cls, ):
        return lambda: DeleteReplicaAction_DeleteReplicaAction(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteReplicaAction(self) -> bool:
        return isinstance(self, DeleteReplicaAction_DeleteReplicaAction)

class DeleteReplicaAction_DeleteReplicaAction(DeleteReplicaAction, NamedTuple('DeleteReplicaAction', [('RegionName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteReplicaAction.DeleteReplicaAction({_dafny.string_of(self.RegionName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteReplicaAction_DeleteReplicaAction) and self.RegionName == __o.RegionName
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteReplicationGroupMemberAction:
    @classmethod
    def default(cls, ):
        return lambda: DeleteReplicationGroupMemberAction_DeleteReplicationGroupMemberAction(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteReplicationGroupMemberAction(self) -> bool:
        return isinstance(self, DeleteReplicationGroupMemberAction_DeleteReplicationGroupMemberAction)

class DeleteReplicationGroupMemberAction_DeleteReplicationGroupMemberAction(DeleteReplicationGroupMemberAction, NamedTuple('DeleteReplicationGroupMemberAction', [('RegionName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteReplicationGroupMemberAction.DeleteReplicationGroupMemberAction({_dafny.string_of(self.RegionName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteReplicationGroupMemberAction_DeleteReplicationGroupMemberAction) and self.RegionName == __o.RegionName
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteRequest:
    @classmethod
    def default(cls, ):
        return lambda: DeleteRequest_DeleteRequest(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteRequest(self) -> bool:
        return isinstance(self, DeleteRequest_DeleteRequest)

class DeleteRequest_DeleteRequest(DeleteRequest, NamedTuple('DeleteRequest', [('Key', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteRequest.DeleteRequest({_dafny.string_of(self.Key)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteRequest_DeleteRequest) and self.Key == __o.Key
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteTableInput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteTableInput_DeleteTableInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteTableInput(self) -> bool:
        return isinstance(self, DeleteTableInput_DeleteTableInput)

class DeleteTableInput_DeleteTableInput(DeleteTableInput, NamedTuple('DeleteTableInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteTableInput.DeleteTableInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteTableInput_DeleteTableInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteTableOutput_DeleteTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteTableOutput(self) -> bool:
        return isinstance(self, DeleteTableOutput_DeleteTableOutput)

class DeleteTableOutput_DeleteTableOutput(DeleteTableOutput, NamedTuple('DeleteTableOutput', [('TableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DeleteTableOutput.DeleteTableOutput({_dafny.string_of(self.TableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteTableOutput_DeleteTableOutput) and self.TableDescription == __o.TableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeBackupInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeBackupInput_DescribeBackupInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeBackupInput(self) -> bool:
        return isinstance(self, DescribeBackupInput_DescribeBackupInput)

class DescribeBackupInput_DescribeBackupInput(DescribeBackupInput, NamedTuple('DescribeBackupInput', [('BackupArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeBackupInput.DescribeBackupInput({_dafny.string_of(self.BackupArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeBackupInput_DescribeBackupInput) and self.BackupArn == __o.BackupArn
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeBackupOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeBackupOutput_DescribeBackupOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeBackupOutput(self) -> bool:
        return isinstance(self, DescribeBackupOutput_DescribeBackupOutput)

class DescribeBackupOutput_DescribeBackupOutput(DescribeBackupOutput, NamedTuple('DescribeBackupOutput', [('BackupDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeBackupOutput.DescribeBackupOutput({_dafny.string_of(self.BackupDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeBackupOutput_DescribeBackupOutput) and self.BackupDescription == __o.BackupDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeContinuousBackupsInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeContinuousBackupsInput_DescribeContinuousBackupsInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeContinuousBackupsInput(self) -> bool:
        return isinstance(self, DescribeContinuousBackupsInput_DescribeContinuousBackupsInput)

class DescribeContinuousBackupsInput_DescribeContinuousBackupsInput(DescribeContinuousBackupsInput, NamedTuple('DescribeContinuousBackupsInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeContinuousBackupsInput.DescribeContinuousBackupsInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeContinuousBackupsInput_DescribeContinuousBackupsInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeContinuousBackupsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeContinuousBackupsOutput_DescribeContinuousBackupsOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeContinuousBackupsOutput(self) -> bool:
        return isinstance(self, DescribeContinuousBackupsOutput_DescribeContinuousBackupsOutput)

class DescribeContinuousBackupsOutput_DescribeContinuousBackupsOutput(DescribeContinuousBackupsOutput, NamedTuple('DescribeContinuousBackupsOutput', [('ContinuousBackupsDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeContinuousBackupsOutput.DescribeContinuousBackupsOutput({_dafny.string_of(self.ContinuousBackupsDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeContinuousBackupsOutput_DescribeContinuousBackupsOutput) and self.ContinuousBackupsDescription == __o.ContinuousBackupsDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeContributorInsightsInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeContributorInsightsInput_DescribeContributorInsightsInput(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeContributorInsightsInput(self) -> bool:
        return isinstance(self, DescribeContributorInsightsInput_DescribeContributorInsightsInput)

class DescribeContributorInsightsInput_DescribeContributorInsightsInput(DescribeContributorInsightsInput, NamedTuple('DescribeContributorInsightsInput', [('TableName', Any), ('IndexName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeContributorInsightsInput.DescribeContributorInsightsInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeContributorInsightsInput_DescribeContributorInsightsInput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeContributorInsightsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeContributorInsightsOutput_DescribeContributorInsightsOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeContributorInsightsOutput(self) -> bool:
        return isinstance(self, DescribeContributorInsightsOutput_DescribeContributorInsightsOutput)

class DescribeContributorInsightsOutput_DescribeContributorInsightsOutput(DescribeContributorInsightsOutput, NamedTuple('DescribeContributorInsightsOutput', [('TableName', Any), ('IndexName', Any), ('ContributorInsightsRuleList', Any), ('ContributorInsightsStatus', Any), ('LastUpdateDateTime', Any), ('FailureException', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeContributorInsightsOutput.DescribeContributorInsightsOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ContributorInsightsRuleList)}, {_dafny.string_of(self.ContributorInsightsStatus)}, {_dafny.string_of(self.LastUpdateDateTime)}, {_dafny.string_of(self.FailureException)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeContributorInsightsOutput_DescribeContributorInsightsOutput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.ContributorInsightsRuleList == __o.ContributorInsightsRuleList and self.ContributorInsightsStatus == __o.ContributorInsightsStatus and self.LastUpdateDateTime == __o.LastUpdateDateTime and self.FailureException == __o.FailureException
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeEndpointsRequest:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DescribeEndpointsRequest_DescribeEndpointsRequest()]
    @classmethod
    def default(cls, ):
        return lambda: DescribeEndpointsRequest_DescribeEndpointsRequest()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeEndpointsRequest(self) -> bool:
        return isinstance(self, DescribeEndpointsRequest_DescribeEndpointsRequest)

class DescribeEndpointsRequest_DescribeEndpointsRequest(DescribeEndpointsRequest, NamedTuple('DescribeEndpointsRequest', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeEndpointsRequest.DescribeEndpointsRequest'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeEndpointsRequest_DescribeEndpointsRequest)
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeEndpointsResponse:
    @classmethod
    def default(cls, ):
        return lambda: DescribeEndpointsResponse_DescribeEndpointsResponse(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeEndpointsResponse(self) -> bool:
        return isinstance(self, DescribeEndpointsResponse_DescribeEndpointsResponse)

class DescribeEndpointsResponse_DescribeEndpointsResponse(DescribeEndpointsResponse, NamedTuple('DescribeEndpointsResponse', [('Endpoints', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeEndpointsResponse.DescribeEndpointsResponse({_dafny.string_of(self.Endpoints)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeEndpointsResponse_DescribeEndpointsResponse) and self.Endpoints == __o.Endpoints
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeExportInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeExportInput_DescribeExportInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeExportInput(self) -> bool:
        return isinstance(self, DescribeExportInput_DescribeExportInput)

class DescribeExportInput_DescribeExportInput(DescribeExportInput, NamedTuple('DescribeExportInput', [('ExportArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeExportInput.DescribeExportInput({_dafny.string_of(self.ExportArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeExportInput_DescribeExportInput) and self.ExportArn == __o.ExportArn
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeExportOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeExportOutput_DescribeExportOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeExportOutput(self) -> bool:
        return isinstance(self, DescribeExportOutput_DescribeExportOutput)

class DescribeExportOutput_DescribeExportOutput(DescribeExportOutput, NamedTuple('DescribeExportOutput', [('ExportDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeExportOutput.DescribeExportOutput({_dafny.string_of(self.ExportDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeExportOutput_DescribeExportOutput) and self.ExportDescription == __o.ExportDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeGlobalTableInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeGlobalTableInput_DescribeGlobalTableInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeGlobalTableInput(self) -> bool:
        return isinstance(self, DescribeGlobalTableInput_DescribeGlobalTableInput)

class DescribeGlobalTableInput_DescribeGlobalTableInput(DescribeGlobalTableInput, NamedTuple('DescribeGlobalTableInput', [('GlobalTableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeGlobalTableInput.DescribeGlobalTableInput({_dafny.string_of(self.GlobalTableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeGlobalTableInput_DescribeGlobalTableInput) and self.GlobalTableName == __o.GlobalTableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeGlobalTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeGlobalTableOutput_DescribeGlobalTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeGlobalTableOutput(self) -> bool:
        return isinstance(self, DescribeGlobalTableOutput_DescribeGlobalTableOutput)

class DescribeGlobalTableOutput_DescribeGlobalTableOutput(DescribeGlobalTableOutput, NamedTuple('DescribeGlobalTableOutput', [('GlobalTableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeGlobalTableOutput.DescribeGlobalTableOutput({_dafny.string_of(self.GlobalTableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeGlobalTableOutput_DescribeGlobalTableOutput) and self.GlobalTableDescription == __o.GlobalTableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeGlobalTableSettingsInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeGlobalTableSettingsInput_DescribeGlobalTableSettingsInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeGlobalTableSettingsInput(self) -> bool:
        return isinstance(self, DescribeGlobalTableSettingsInput_DescribeGlobalTableSettingsInput)

class DescribeGlobalTableSettingsInput_DescribeGlobalTableSettingsInput(DescribeGlobalTableSettingsInput, NamedTuple('DescribeGlobalTableSettingsInput', [('GlobalTableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeGlobalTableSettingsInput.DescribeGlobalTableSettingsInput({_dafny.string_of(self.GlobalTableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeGlobalTableSettingsInput_DescribeGlobalTableSettingsInput) and self.GlobalTableName == __o.GlobalTableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeGlobalTableSettingsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeGlobalTableSettingsOutput_DescribeGlobalTableSettingsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeGlobalTableSettingsOutput(self) -> bool:
        return isinstance(self, DescribeGlobalTableSettingsOutput_DescribeGlobalTableSettingsOutput)

class DescribeGlobalTableSettingsOutput_DescribeGlobalTableSettingsOutput(DescribeGlobalTableSettingsOutput, NamedTuple('DescribeGlobalTableSettingsOutput', [('GlobalTableName', Any), ('ReplicaSettings', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeGlobalTableSettingsOutput.DescribeGlobalTableSettingsOutput({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.ReplicaSettings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeGlobalTableSettingsOutput_DescribeGlobalTableSettingsOutput) and self.GlobalTableName == __o.GlobalTableName and self.ReplicaSettings == __o.ReplicaSettings
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeImportInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeImportInput_DescribeImportInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeImportInput(self) -> bool:
        return isinstance(self, DescribeImportInput_DescribeImportInput)

class DescribeImportInput_DescribeImportInput(DescribeImportInput, NamedTuple('DescribeImportInput', [('ImportArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeImportInput.DescribeImportInput({_dafny.string_of(self.ImportArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeImportInput_DescribeImportInput) and self.ImportArn == __o.ImportArn
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeImportOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeImportOutput_DescribeImportOutput(ImportTableDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeImportOutput(self) -> bool:
        return isinstance(self, DescribeImportOutput_DescribeImportOutput)

class DescribeImportOutput_DescribeImportOutput(DescribeImportOutput, NamedTuple('DescribeImportOutput', [('ImportTableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeImportOutput.DescribeImportOutput({_dafny.string_of(self.ImportTableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeImportOutput_DescribeImportOutput) and self.ImportTableDescription == __o.ImportTableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeKinesisStreamingDestinationInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeKinesisStreamingDestinationInput_DescribeKinesisStreamingDestinationInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeKinesisStreamingDestinationInput(self) -> bool:
        return isinstance(self, DescribeKinesisStreamingDestinationInput_DescribeKinesisStreamingDestinationInput)

class DescribeKinesisStreamingDestinationInput_DescribeKinesisStreamingDestinationInput(DescribeKinesisStreamingDestinationInput, NamedTuple('DescribeKinesisStreamingDestinationInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeKinesisStreamingDestinationInput.DescribeKinesisStreamingDestinationInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeKinesisStreamingDestinationInput_DescribeKinesisStreamingDestinationInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeKinesisStreamingDestinationOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeKinesisStreamingDestinationOutput_DescribeKinesisStreamingDestinationOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeKinesisStreamingDestinationOutput(self) -> bool:
        return isinstance(self, DescribeKinesisStreamingDestinationOutput_DescribeKinesisStreamingDestinationOutput)

class DescribeKinesisStreamingDestinationOutput_DescribeKinesisStreamingDestinationOutput(DescribeKinesisStreamingDestinationOutput, NamedTuple('DescribeKinesisStreamingDestinationOutput', [('TableName', Any), ('KinesisDataStreamDestinations', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeKinesisStreamingDestinationOutput.DescribeKinesisStreamingDestinationOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.KinesisDataStreamDestinations)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeKinesisStreamingDestinationOutput_DescribeKinesisStreamingDestinationOutput) and self.TableName == __o.TableName and self.KinesisDataStreamDestinations == __o.KinesisDataStreamDestinations
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeLimitsInput:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DescribeLimitsInput_DescribeLimitsInput()]
    @classmethod
    def default(cls, ):
        return lambda: DescribeLimitsInput_DescribeLimitsInput()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeLimitsInput(self) -> bool:
        return isinstance(self, DescribeLimitsInput_DescribeLimitsInput)

class DescribeLimitsInput_DescribeLimitsInput(DescribeLimitsInput, NamedTuple('DescribeLimitsInput', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeLimitsInput.DescribeLimitsInput'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeLimitsInput_DescribeLimitsInput)
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeLimitsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeLimitsOutput_DescribeLimitsOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeLimitsOutput(self) -> bool:
        return isinstance(self, DescribeLimitsOutput_DescribeLimitsOutput)

class DescribeLimitsOutput_DescribeLimitsOutput(DescribeLimitsOutput, NamedTuple('DescribeLimitsOutput', [('AccountMaxReadCapacityUnits', Any), ('AccountMaxWriteCapacityUnits', Any), ('TableMaxReadCapacityUnits', Any), ('TableMaxWriteCapacityUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeLimitsOutput.DescribeLimitsOutput({_dafny.string_of(self.AccountMaxReadCapacityUnits)}, {_dafny.string_of(self.AccountMaxWriteCapacityUnits)}, {_dafny.string_of(self.TableMaxReadCapacityUnits)}, {_dafny.string_of(self.TableMaxWriteCapacityUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeLimitsOutput_DescribeLimitsOutput) and self.AccountMaxReadCapacityUnits == __o.AccountMaxReadCapacityUnits and self.AccountMaxWriteCapacityUnits == __o.AccountMaxWriteCapacityUnits and self.TableMaxReadCapacityUnits == __o.TableMaxReadCapacityUnits and self.TableMaxWriteCapacityUnits == __o.TableMaxWriteCapacityUnits
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTableInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTableInput_DescribeTableInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTableInput(self) -> bool:
        return isinstance(self, DescribeTableInput_DescribeTableInput)

class DescribeTableInput_DescribeTableInput(DescribeTableInput, NamedTuple('DescribeTableInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTableInput.DescribeTableInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTableInput_DescribeTableInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTableOutput_DescribeTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTableOutput(self) -> bool:
        return isinstance(self, DescribeTableOutput_DescribeTableOutput)

class DescribeTableOutput_DescribeTableOutput(DescribeTableOutput, NamedTuple('DescribeTableOutput', [('Table', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTableOutput.DescribeTableOutput({_dafny.string_of(self.Table)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTableOutput_DescribeTableOutput) and self.Table == __o.Table
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTableReplicaAutoScalingInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTableReplicaAutoScalingInput_DescribeTableReplicaAutoScalingInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTableReplicaAutoScalingInput(self) -> bool:
        return isinstance(self, DescribeTableReplicaAutoScalingInput_DescribeTableReplicaAutoScalingInput)

class DescribeTableReplicaAutoScalingInput_DescribeTableReplicaAutoScalingInput(DescribeTableReplicaAutoScalingInput, NamedTuple('DescribeTableReplicaAutoScalingInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTableReplicaAutoScalingInput.DescribeTableReplicaAutoScalingInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTableReplicaAutoScalingInput_DescribeTableReplicaAutoScalingInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTableReplicaAutoScalingOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTableReplicaAutoScalingOutput_DescribeTableReplicaAutoScalingOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTableReplicaAutoScalingOutput(self) -> bool:
        return isinstance(self, DescribeTableReplicaAutoScalingOutput_DescribeTableReplicaAutoScalingOutput)

class DescribeTableReplicaAutoScalingOutput_DescribeTableReplicaAutoScalingOutput(DescribeTableReplicaAutoScalingOutput, NamedTuple('DescribeTableReplicaAutoScalingOutput', [('TableAutoScalingDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTableReplicaAutoScalingOutput.DescribeTableReplicaAutoScalingOutput({_dafny.string_of(self.TableAutoScalingDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTableReplicaAutoScalingOutput_DescribeTableReplicaAutoScalingOutput) and self.TableAutoScalingDescription == __o.TableAutoScalingDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTimeToLiveInput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTimeToLiveInput_DescribeTimeToLiveInput(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTimeToLiveInput(self) -> bool:
        return isinstance(self, DescribeTimeToLiveInput_DescribeTimeToLiveInput)

class DescribeTimeToLiveInput_DescribeTimeToLiveInput(DescribeTimeToLiveInput, NamedTuple('DescribeTimeToLiveInput', [('TableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTimeToLiveInput.DescribeTimeToLiveInput({_dafny.string_of(self.TableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTimeToLiveInput_DescribeTimeToLiveInput) and self.TableName == __o.TableName
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeTimeToLiveOutput:
    @classmethod
    def default(cls, ):
        return lambda: DescribeTimeToLiveOutput_DescribeTimeToLiveOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeTimeToLiveOutput(self) -> bool:
        return isinstance(self, DescribeTimeToLiveOutput_DescribeTimeToLiveOutput)

class DescribeTimeToLiveOutput_DescribeTimeToLiveOutput(DescribeTimeToLiveOutput, NamedTuple('DescribeTimeToLiveOutput', [('TimeToLiveDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DescribeTimeToLiveOutput.DescribeTimeToLiveOutput({_dafny.string_of(self.TimeToLiveDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeTimeToLiveOutput_DescribeTimeToLiveOutput) and self.TimeToLiveDescription == __o.TimeToLiveDescription
    def __hash__(self) -> int:
        return super().__hash__()


class DestinationStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DestinationStatus_ENABLING(), DestinationStatus_ACTIVE(), DestinationStatus_DISABLING(), DestinationStatus_DISABLED(), DestinationStatus_ENABLE__FAILED()]
    @classmethod
    def default(cls, ):
        return lambda: DestinationStatus_ENABLING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLING(self) -> bool:
        return isinstance(self, DestinationStatus_ENABLING)
    @property
    def is_ACTIVE(self) -> bool:
        return isinstance(self, DestinationStatus_ACTIVE)
    @property
    def is_DISABLING(self) -> bool:
        return isinstance(self, DestinationStatus_DISABLING)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, DestinationStatus_DISABLED)
    @property
    def is_ENABLE__FAILED(self) -> bool:
        return isinstance(self, DestinationStatus_ENABLE__FAILED)

class DestinationStatus_ENABLING(DestinationStatus, NamedTuple('ENABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DestinationStatus.ENABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DestinationStatus_ENABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class DestinationStatus_ACTIVE(DestinationStatus, NamedTuple('ACTIVE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DestinationStatus.ACTIVE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DestinationStatus_ACTIVE)
    def __hash__(self) -> int:
        return super().__hash__()

class DestinationStatus_DISABLING(DestinationStatus, NamedTuple('DISABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DestinationStatus.DISABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DestinationStatus_DISABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class DestinationStatus_DISABLED(DestinationStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DestinationStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DestinationStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class DestinationStatus_ENABLE__FAILED(DestinationStatus, NamedTuple('ENABLE__FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DestinationStatus.ENABLE_FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DestinationStatus_ENABLE__FAILED)
    def __hash__(self) -> int:
        return super().__hash__()


class DisableKinesisStreamingDestinationInput:
    @classmethod
    def default(cls, ):
        return lambda: DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisableKinesisStreamingDestinationInput(self) -> bool:
        return isinstance(self, DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput)

class DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput(DisableKinesisStreamingDestinationInput, NamedTuple('DisableKinesisStreamingDestinationInput', [('TableName', Any), ('StreamArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DisableKinesisStreamingDestinationInput.DisableKinesisStreamingDestinationInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn
    def __hash__(self) -> int:
        return super().__hash__()


class DisableKinesisStreamingDestinationOutput:
    @classmethod
    def default(cls, ):
        return lambda: DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisableKinesisStreamingDestinationOutput(self) -> bool:
        return isinstance(self, DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput)

class DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput(DisableKinesisStreamingDestinationOutput, NamedTuple('DisableKinesisStreamingDestinationOutput', [('TableName', Any), ('StreamArn', Any), ('DestinationStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.DisableKinesisStreamingDestinationOutput.DisableKinesisStreamingDestinationOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)}, {_dafny.string_of(self.DestinationStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn and self.DestinationStatus == __o.DestinationStatus
    def __hash__(self) -> int:
        return super().__hash__()


class Double:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_18_x_: _dafny.Seq = source__
        return default__.IsValid__Double(d_18_x_)

class IDynamoDBClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "ComAmazonawsDynamodbTypes.IDynamoDBClientCallHistory"

class IDynamoDBClient:
    pass
    def BatchExecuteStatement(self, input):
        pass

    def BatchGetItem(self, input):
        pass

    def BatchWriteItem(self, input):
        pass

    def CreateBackup(self, input):
        pass

    def CreateGlobalTable(self, input):
        pass

    def CreateTable(self, input):
        pass

    def DeleteBackup(self, input):
        pass

    def DeleteItem(self, input):
        pass

    def DeleteTable(self, input):
        pass

    def DescribeBackup(self, input):
        pass

    def DescribeContinuousBackups(self, input):
        pass

    def DescribeContributorInsights(self, input):
        pass

    def DescribeEndpoints(self, input):
        pass

    def DescribeExport(self, input):
        pass

    def DescribeGlobalTable(self, input):
        pass

    def DescribeGlobalTableSettings(self, input):
        pass

    def DescribeImport(self, input):
        pass

    def DescribeKinesisStreamingDestination(self, input):
        pass

    def DescribeLimits(self, input):
        pass

    def DescribeTable(self, input):
        pass

    def DescribeTableReplicaAutoScaling(self, input):
        pass

    def DescribeTimeToLive(self, input):
        pass

    def DisableKinesisStreamingDestination(self, input):
        pass

    def EnableKinesisStreamingDestination(self, input):
        pass

    def ExecuteStatement(self, input):
        pass

    def ExecuteTransaction(self, input):
        pass

    def ExportTableToPointInTime(self, input):
        pass

    def GetItem(self, input):
        pass

    def ImportTable(self, input):
        pass

    def ListBackups(self, input):
        pass

    def ListContributorInsights(self, input):
        pass

    def ListExports(self, input):
        pass

    def ListGlobalTables(self, input):
        pass

    def ListImports(self, input):
        pass

    def ListTables(self, input):
        pass

    def ListTagsOfResource(self, input):
        pass

    def PutItem(self, input):
        pass

    def Query(self, input):
        pass

    def RestoreTableFromBackup(self, input):
        pass

    def RestoreTableToPointInTime(self, input):
        pass

    def Scan(self, input):
        pass

    def TagResource(self, input):
        pass

    def TransactGetItems(self, input):
        pass

    def TransactWriteItems(self, input):
        pass

    def UntagResource(self, input):
        pass

    def UpdateContinuousBackups(self, input):
        pass

    def UpdateContributorInsights(self, input):
        pass

    def UpdateGlobalTable(self, input):
        pass

    def UpdateGlobalTableSettings(self, input):
        pass

    def UpdateItem(self, input):
        pass

    def UpdateTable(self, input):
        pass

    def UpdateTableReplicaAutoScaling(self, input):
        pass

    def UpdateTimeToLive(self, input):
        pass


class EnableKinesisStreamingDestinationInput:
    @classmethod
    def default(cls, ):
        return lambda: EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EnableKinesisStreamingDestinationInput(self) -> bool:
        return isinstance(self, EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput)

class EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput(EnableKinesisStreamingDestinationInput, NamedTuple('EnableKinesisStreamingDestinationInput', [('TableName', Any), ('StreamArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.EnableKinesisStreamingDestinationInput.EnableKinesisStreamingDestinationInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn
    def __hash__(self) -> int:
        return super().__hash__()


class EnableKinesisStreamingDestinationOutput:
    @classmethod
    def default(cls, ):
        return lambda: EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EnableKinesisStreamingDestinationOutput(self) -> bool:
        return isinstance(self, EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput)

class EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput(EnableKinesisStreamingDestinationOutput, NamedTuple('EnableKinesisStreamingDestinationOutput', [('TableName', Any), ('StreamArn', Any), ('DestinationStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.EnableKinesisStreamingDestinationOutput.EnableKinesisStreamingDestinationOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)}, {_dafny.string_of(self.DestinationStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn and self.DestinationStatus == __o.DestinationStatus
    def __hash__(self) -> int:
        return super().__hash__()


class Endpoint:
    @classmethod
    def default(cls, ):
        return lambda: Endpoint_Endpoint(_dafny.Seq(""), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Endpoint(self) -> bool:
        return isinstance(self, Endpoint_Endpoint)

class Endpoint_Endpoint(Endpoint, NamedTuple('Endpoint', [('Address', Any), ('CachePeriodInMinutes', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Endpoint.Endpoint({_dafny.string_of(self.Address)}, {_dafny.string_of(self.CachePeriodInMinutes)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Endpoint_Endpoint) and self.Address == __o.Address and self.CachePeriodInMinutes == __o.CachePeriodInMinutes
    def __hash__(self) -> int:
        return super().__hash__()


class ErrorCount:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_0_x_: int = source__
        if True:
            return default__.IsValid__ErrorCount(d_0_x_)
        return False

class ExecuteStatementInput:
    @classmethod
    def default(cls, ):
        return lambda: ExecuteStatementInput_ExecuteStatementInput(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExecuteStatementInput(self) -> bool:
        return isinstance(self, ExecuteStatementInput_ExecuteStatementInput)

class ExecuteStatementInput_ExecuteStatementInput(ExecuteStatementInput, NamedTuple('ExecuteStatementInput', [('Statement', Any), ('Parameters', Any), ('ConsistentRead', Any), ('NextToken', Any), ('ReturnConsumedCapacity', Any), ('Limit', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExecuteStatementInput.ExecuteStatementInput({_dafny.string_of(self.Statement)}, {_dafny.string_of(self.Parameters)}, {_dafny.string_of(self.ConsistentRead)}, {_dafny.string_of(self.NextToken)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.Limit)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExecuteStatementInput_ExecuteStatementInput) and self.Statement == __o.Statement and self.Parameters == __o.Parameters and self.ConsistentRead == __o.ConsistentRead and self.NextToken == __o.NextToken and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.Limit == __o.Limit
    def __hash__(self) -> int:
        return super().__hash__()


class ExecuteStatementOutput:
    @classmethod
    def default(cls, ):
        return lambda: ExecuteStatementOutput_ExecuteStatementOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExecuteStatementOutput(self) -> bool:
        return isinstance(self, ExecuteStatementOutput_ExecuteStatementOutput)

class ExecuteStatementOutput_ExecuteStatementOutput(ExecuteStatementOutput, NamedTuple('ExecuteStatementOutput', [('Items', Any), ('NextToken', Any), ('ConsumedCapacity', Any), ('LastEvaluatedKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExecuteStatementOutput.ExecuteStatementOutput({_dafny.string_of(self.Items)}, {_dafny.string_of(self.NextToken)}, {_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.LastEvaluatedKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExecuteStatementOutput_ExecuteStatementOutput) and self.Items == __o.Items and self.NextToken == __o.NextToken and self.ConsumedCapacity == __o.ConsumedCapacity and self.LastEvaluatedKey == __o.LastEvaluatedKey
    def __hash__(self) -> int:
        return super().__hash__()


class ExecuteTransactionInput:
    @classmethod
    def default(cls, ):
        return lambda: ExecuteTransactionInput_ExecuteTransactionInput(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExecuteTransactionInput(self) -> bool:
        return isinstance(self, ExecuteTransactionInput_ExecuteTransactionInput)

class ExecuteTransactionInput_ExecuteTransactionInput(ExecuteTransactionInput, NamedTuple('ExecuteTransactionInput', [('TransactStatements', Any), ('ClientRequestToken', Any), ('ReturnConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExecuteTransactionInput.ExecuteTransactionInput({_dafny.string_of(self.TransactStatements)}, {_dafny.string_of(self.ClientRequestToken)}, {_dafny.string_of(self.ReturnConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExecuteTransactionInput_ExecuteTransactionInput) and self.TransactStatements == __o.TransactStatements and self.ClientRequestToken == __o.ClientRequestToken and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class ExecuteTransactionOutput:
    @classmethod
    def default(cls, ):
        return lambda: ExecuteTransactionOutput_ExecuteTransactionOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExecuteTransactionOutput(self) -> bool:
        return isinstance(self, ExecuteTransactionOutput_ExecuteTransactionOutput)

class ExecuteTransactionOutput_ExecuteTransactionOutput(ExecuteTransactionOutput, NamedTuple('ExecuteTransactionOutput', [('Responses', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExecuteTransactionOutput.ExecuteTransactionOutput({_dafny.string_of(self.Responses)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExecuteTransactionOutput_ExecuteTransactionOutput) and self.Responses == __o.Responses and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class ExpectedAttributeValue:
    @classmethod
    def default(cls, ):
        return lambda: ExpectedAttributeValue_ExpectedAttributeValue(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExpectedAttributeValue(self) -> bool:
        return isinstance(self, ExpectedAttributeValue_ExpectedAttributeValue)

class ExpectedAttributeValue_ExpectedAttributeValue(ExpectedAttributeValue, NamedTuple('ExpectedAttributeValue', [('Value', Any), ('Exists', Any), ('ComparisonOperator', Any), ('AttributeValueList', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExpectedAttributeValue.ExpectedAttributeValue({_dafny.string_of(self.Value)}, {_dafny.string_of(self.Exists)}, {_dafny.string_of(self.ComparisonOperator)}, {_dafny.string_of(self.AttributeValueList)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExpectedAttributeValue_ExpectedAttributeValue) and self.Value == __o.Value and self.Exists == __o.Exists and self.ComparisonOperator == __o.ComparisonOperator and self.AttributeValueList == __o.AttributeValueList
    def __hash__(self) -> int:
        return super().__hash__()


class ExportArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_x_: _dafny.Seq = source__
        return default__.IsValid__ExportArn(d_1_x_)

class ExportDescription:
    @classmethod
    def default(cls, ):
        return lambda: ExportDescription_ExportDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExportDescription(self) -> bool:
        return isinstance(self, ExportDescription_ExportDescription)

class ExportDescription_ExportDescription(ExportDescription, NamedTuple('ExportDescription', [('ExportArn', Any), ('ExportStatus', Any), ('StartTime', Any), ('EndTime', Any), ('ExportManifest', Any), ('TableArn', Any), ('TableId', Any), ('ExportTime', Any), ('ClientToken', Any), ('S3Bucket', Any), ('S3BucketOwner', Any), ('S3Prefix', Any), ('S3SseAlgorithm', Any), ('S3SseKmsKeyId', Any), ('FailureCode', Any), ('FailureMessage', Any), ('ExportFormat', Any), ('BilledSizeBytes', Any), ('ItemCount', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportDescription.ExportDescription({_dafny.string_of(self.ExportArn)}, {_dafny.string_of(self.ExportStatus)}, {_dafny.string_of(self.StartTime)}, {_dafny.string_of(self.EndTime)}, {_dafny.string_of(self.ExportManifest)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.TableId)}, {_dafny.string_of(self.ExportTime)}, {_dafny.string_of(self.ClientToken)}, {_dafny.string_of(self.S3Bucket)}, {_dafny.string_of(self.S3BucketOwner)}, {_dafny.string_of(self.S3Prefix)}, {_dafny.string_of(self.S3SseAlgorithm)}, {_dafny.string_of(self.S3SseKmsKeyId)}, {_dafny.string_of(self.FailureCode)}, {_dafny.string_of(self.FailureMessage)}, {_dafny.string_of(self.ExportFormat)}, {_dafny.string_of(self.BilledSizeBytes)}, {_dafny.string_of(self.ItemCount)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportDescription_ExportDescription) and self.ExportArn == __o.ExportArn and self.ExportStatus == __o.ExportStatus and self.StartTime == __o.StartTime and self.EndTime == __o.EndTime and self.ExportManifest == __o.ExportManifest and self.TableArn == __o.TableArn and self.TableId == __o.TableId and self.ExportTime == __o.ExportTime and self.ClientToken == __o.ClientToken and self.S3Bucket == __o.S3Bucket and self.S3BucketOwner == __o.S3BucketOwner and self.S3Prefix == __o.S3Prefix and self.S3SseAlgorithm == __o.S3SseAlgorithm and self.S3SseKmsKeyId == __o.S3SseKmsKeyId and self.FailureCode == __o.FailureCode and self.FailureMessage == __o.FailureMessage and self.ExportFormat == __o.ExportFormat and self.BilledSizeBytes == __o.BilledSizeBytes and self.ItemCount == __o.ItemCount
    def __hash__(self) -> int:
        return super().__hash__()


class ExportFormat:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ExportFormat_DYNAMODB__JSON(), ExportFormat_ION()]
    @classmethod
    def default(cls, ):
        return lambda: ExportFormat_DYNAMODB__JSON()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DYNAMODB__JSON(self) -> bool:
        return isinstance(self, ExportFormat_DYNAMODB__JSON)
    @property
    def is_ION(self) -> bool:
        return isinstance(self, ExportFormat_ION)

class ExportFormat_DYNAMODB__JSON(ExportFormat, NamedTuple('DYNAMODB__JSON', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportFormat.DYNAMODB_JSON'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportFormat_DYNAMODB__JSON)
    def __hash__(self) -> int:
        return super().__hash__()

class ExportFormat_ION(ExportFormat, NamedTuple('ION', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportFormat.ION'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportFormat_ION)
    def __hash__(self) -> int:
        return super().__hash__()


class ExportStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ExportStatus_IN__PROGRESS(), ExportStatus_COMPLETED(), ExportStatus_FAILED()]
    @classmethod
    def default(cls, ):
        return lambda: ExportStatus_IN__PROGRESS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IN__PROGRESS(self) -> bool:
        return isinstance(self, ExportStatus_IN__PROGRESS)
    @property
    def is_COMPLETED(self) -> bool:
        return isinstance(self, ExportStatus_COMPLETED)
    @property
    def is_FAILED(self) -> bool:
        return isinstance(self, ExportStatus_FAILED)

class ExportStatus_IN__PROGRESS(ExportStatus, NamedTuple('IN__PROGRESS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportStatus.IN_PROGRESS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportStatus_IN__PROGRESS)
    def __hash__(self) -> int:
        return super().__hash__()

class ExportStatus_COMPLETED(ExportStatus, NamedTuple('COMPLETED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportStatus.COMPLETED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportStatus_COMPLETED)
    def __hash__(self) -> int:
        return super().__hash__()

class ExportStatus_FAILED(ExportStatus, NamedTuple('FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportStatus.FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportStatus_FAILED)
    def __hash__(self) -> int:
        return super().__hash__()


class ExportSummary:
    @classmethod
    def default(cls, ):
        return lambda: ExportSummary_ExportSummary(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExportSummary(self) -> bool:
        return isinstance(self, ExportSummary_ExportSummary)

class ExportSummary_ExportSummary(ExportSummary, NamedTuple('ExportSummary', [('ExportArn', Any), ('ExportStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportSummary.ExportSummary({_dafny.string_of(self.ExportArn)}, {_dafny.string_of(self.ExportStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportSummary_ExportSummary) and self.ExportArn == __o.ExportArn and self.ExportStatus == __o.ExportStatus
    def __hash__(self) -> int:
        return super().__hash__()


class ExportTableToPointInTimeInput:
    @classmethod
    def default(cls, ):
        return lambda: ExportTableToPointInTimeInput_ExportTableToPointInTimeInput(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExportTableToPointInTimeInput(self) -> bool:
        return isinstance(self, ExportTableToPointInTimeInput_ExportTableToPointInTimeInput)

class ExportTableToPointInTimeInput_ExportTableToPointInTimeInput(ExportTableToPointInTimeInput, NamedTuple('ExportTableToPointInTimeInput', [('TableArn', Any), ('ExportTime', Any), ('ClientToken', Any), ('S3Bucket', Any), ('S3BucketOwner', Any), ('S3Prefix', Any), ('S3SseAlgorithm', Any), ('S3SseKmsKeyId', Any), ('ExportFormat', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportTableToPointInTimeInput.ExportTableToPointInTimeInput({_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.ExportTime)}, {_dafny.string_of(self.ClientToken)}, {_dafny.string_of(self.S3Bucket)}, {_dafny.string_of(self.S3BucketOwner)}, {_dafny.string_of(self.S3Prefix)}, {_dafny.string_of(self.S3SseAlgorithm)}, {_dafny.string_of(self.S3SseKmsKeyId)}, {_dafny.string_of(self.ExportFormat)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportTableToPointInTimeInput_ExportTableToPointInTimeInput) and self.TableArn == __o.TableArn and self.ExportTime == __o.ExportTime and self.ClientToken == __o.ClientToken and self.S3Bucket == __o.S3Bucket and self.S3BucketOwner == __o.S3BucketOwner and self.S3Prefix == __o.S3Prefix and self.S3SseAlgorithm == __o.S3SseAlgorithm and self.S3SseKmsKeyId == __o.S3SseKmsKeyId and self.ExportFormat == __o.ExportFormat
    def __hash__(self) -> int:
        return super().__hash__()


class ExportTableToPointInTimeOutput:
    @classmethod
    def default(cls, ):
        return lambda: ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ExportTableToPointInTimeOutput(self) -> bool:
        return isinstance(self, ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput)

class ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput(ExportTableToPointInTimeOutput, NamedTuple('ExportTableToPointInTimeOutput', [('ExportDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ExportTableToPointInTimeOutput.ExportTableToPointInTimeOutput({_dafny.string_of(self.ExportDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput) and self.ExportDescription == __o.ExportDescription
    def __hash__(self) -> int:
        return super().__hash__()


class FailureException:
    @classmethod
    def default(cls, ):
        return lambda: FailureException_FailureException(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_FailureException(self) -> bool:
        return isinstance(self, FailureException_FailureException)

class FailureException_FailureException(FailureException, NamedTuple('FailureException', [('ExceptionName', Any), ('ExceptionDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.FailureException.FailureException({_dafny.string_of(self.ExceptionName)}, {_dafny.string_of(self.ExceptionDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, FailureException_FailureException) and self.ExceptionName == __o.ExceptionName and self.ExceptionDescription == __o.ExceptionDescription
    def __hash__(self) -> int:
        return super().__hash__()


class Get:
    @classmethod
    def default(cls, ):
        return lambda: Get_Get(_dafny.Map({}), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Get(self) -> bool:
        return isinstance(self, Get_Get)

class Get_Get(Get, NamedTuple('Get', [('Key', Any), ('TableName', Any), ('ProjectionExpression', Any), ('ExpressionAttributeNames', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Get.Get({_dafny.string_of(self.Key)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ProjectionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Get_Get) and self.Key == __o.Key and self.TableName == __o.TableName and self.ProjectionExpression == __o.ProjectionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames
    def __hash__(self) -> int:
        return super().__hash__()


class GetItemInput:
    @classmethod
    def default(cls, ):
        return lambda: GetItemInput_GetItemInput(_dafny.Seq(""), _dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetItemInput(self) -> bool:
        return isinstance(self, GetItemInput_GetItemInput)

class GetItemInput_GetItemInput(GetItemInput, NamedTuple('GetItemInput', [('TableName', Any), ('Key', Any), ('AttributesToGet', Any), ('ConsistentRead', Any), ('ReturnConsumedCapacity', Any), ('ProjectionExpression', Any), ('ExpressionAttributeNames', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GetItemInput.GetItemInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Key)}, {_dafny.string_of(self.AttributesToGet)}, {_dafny.string_of(self.ConsistentRead)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ProjectionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetItemInput_GetItemInput) and self.TableName == __o.TableName and self.Key == __o.Key and self.AttributesToGet == __o.AttributesToGet and self.ConsistentRead == __o.ConsistentRead and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ProjectionExpression == __o.ProjectionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames
    def __hash__(self) -> int:
        return super().__hash__()


class GetItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetItemOutput_GetItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetItemOutput(self) -> bool:
        return isinstance(self, GetItemOutput_GetItemOutput)

class GetItemOutput_GetItemOutput(GetItemOutput, NamedTuple('GetItemOutput', [('Item', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GetItemOutput.GetItemOutput({_dafny.string_of(self.Item)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetItemOutput_GetItemOutput) and self.Item == __o.Item and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalSecondaryIndex:
    @classmethod
    def default(cls, ):
        return lambda: GlobalSecondaryIndex_GlobalSecondaryIndex(_dafny.Seq(""), _dafny.Seq({}), Projection.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalSecondaryIndex(self) -> bool:
        return isinstance(self, GlobalSecondaryIndex_GlobalSecondaryIndex)

class GlobalSecondaryIndex_GlobalSecondaryIndex(GlobalSecondaryIndex, NamedTuple('GlobalSecondaryIndex', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any), ('ProvisionedThroughput', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalSecondaryIndex.GlobalSecondaryIndex({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)}, {_dafny.string_of(self.ProvisionedThroughput)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalSecondaryIndex_GlobalSecondaryIndex) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection and self.ProvisionedThroughput == __o.ProvisionedThroughput
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalSecondaryIndexAutoScalingUpdate:
    @classmethod
    def default(cls, ):
        return lambda: GlobalSecondaryIndexAutoScalingUpdate_GlobalSecondaryIndexAutoScalingUpdate(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalSecondaryIndexAutoScalingUpdate(self) -> bool:
        return isinstance(self, GlobalSecondaryIndexAutoScalingUpdate_GlobalSecondaryIndexAutoScalingUpdate)

class GlobalSecondaryIndexAutoScalingUpdate_GlobalSecondaryIndexAutoScalingUpdate(GlobalSecondaryIndexAutoScalingUpdate, NamedTuple('GlobalSecondaryIndexAutoScalingUpdate', [('IndexName', Any), ('ProvisionedWriteCapacityAutoScalingUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalSecondaryIndexAutoScalingUpdate.GlobalSecondaryIndexAutoScalingUpdate({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedWriteCapacityAutoScalingUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalSecondaryIndexAutoScalingUpdate_GlobalSecondaryIndexAutoScalingUpdate) and self.IndexName == __o.IndexName and self.ProvisionedWriteCapacityAutoScalingUpdate == __o.ProvisionedWriteCapacityAutoScalingUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalSecondaryIndexAutoScalingUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_2_x_: _dafny.Seq = source__
        return default__.IsValid__GlobalSecondaryIndexAutoScalingUpdateList(d_2_x_)

class GlobalSecondaryIndexDescription:
    @classmethod
    def default(cls, ):
        return lambda: GlobalSecondaryIndexDescription_GlobalSecondaryIndexDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalSecondaryIndexDescription(self) -> bool:
        return isinstance(self, GlobalSecondaryIndexDescription_GlobalSecondaryIndexDescription)

class GlobalSecondaryIndexDescription_GlobalSecondaryIndexDescription(GlobalSecondaryIndexDescription, NamedTuple('GlobalSecondaryIndexDescription', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any), ('IndexStatus', Any), ('Backfilling', Any), ('ProvisionedThroughput', Any), ('IndexSizeBytes', Any), ('ItemCount', Any), ('IndexArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalSecondaryIndexDescription.GlobalSecondaryIndexDescription({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)}, {_dafny.string_of(self.IndexStatus)}, {_dafny.string_of(self.Backfilling)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.IndexSizeBytes)}, {_dafny.string_of(self.ItemCount)}, {_dafny.string_of(self.IndexArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalSecondaryIndexDescription_GlobalSecondaryIndexDescription) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection and self.IndexStatus == __o.IndexStatus and self.Backfilling == __o.Backfilling and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.IndexSizeBytes == __o.IndexSizeBytes and self.ItemCount == __o.ItemCount and self.IndexArn == __o.IndexArn
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalSecondaryIndexInfo:
    @classmethod
    def default(cls, ):
        return lambda: GlobalSecondaryIndexInfo_GlobalSecondaryIndexInfo(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalSecondaryIndexInfo(self) -> bool:
        return isinstance(self, GlobalSecondaryIndexInfo_GlobalSecondaryIndexInfo)

class GlobalSecondaryIndexInfo_GlobalSecondaryIndexInfo(GlobalSecondaryIndexInfo, NamedTuple('GlobalSecondaryIndexInfo', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any), ('ProvisionedThroughput', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalSecondaryIndexInfo.GlobalSecondaryIndexInfo({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)}, {_dafny.string_of(self.ProvisionedThroughput)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalSecondaryIndexInfo_GlobalSecondaryIndexInfo) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection and self.ProvisionedThroughput == __o.ProvisionedThroughput
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalSecondaryIndexUpdate:
    @classmethod
    def default(cls, ):
        return lambda: GlobalSecondaryIndexUpdate_GlobalSecondaryIndexUpdate(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalSecondaryIndexUpdate(self) -> bool:
        return isinstance(self, GlobalSecondaryIndexUpdate_GlobalSecondaryIndexUpdate)

class GlobalSecondaryIndexUpdate_GlobalSecondaryIndexUpdate(GlobalSecondaryIndexUpdate, NamedTuple('GlobalSecondaryIndexUpdate', [('Update', Any), ('Create', Any), ('Delete', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalSecondaryIndexUpdate.GlobalSecondaryIndexUpdate({_dafny.string_of(self.Update)}, {_dafny.string_of(self.Create)}, {_dafny.string_of(self.Delete)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalSecondaryIndexUpdate_GlobalSecondaryIndexUpdate) and self.Update == __o.Update and self.Create == __o.Create and self.Delete == __o.Delete
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalTable:
    @classmethod
    def default(cls, ):
        return lambda: GlobalTable_GlobalTable(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalTable(self) -> bool:
        return isinstance(self, GlobalTable_GlobalTable)

class GlobalTable_GlobalTable(GlobalTable, NamedTuple('GlobalTable', [('GlobalTableName', Any), ('ReplicationGroup', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTable.GlobalTable({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.ReplicationGroup)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTable_GlobalTable) and self.GlobalTableName == __o.GlobalTableName and self.ReplicationGroup == __o.ReplicationGroup
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalTableDescription:
    @classmethod
    def default(cls, ):
        return lambda: GlobalTableDescription_GlobalTableDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalTableDescription(self) -> bool:
        return isinstance(self, GlobalTableDescription_GlobalTableDescription)

class GlobalTableDescription_GlobalTableDescription(GlobalTableDescription, NamedTuple('GlobalTableDescription', [('ReplicationGroup', Any), ('GlobalTableArn', Any), ('CreationDateTime', Any), ('GlobalTableStatus', Any), ('GlobalTableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableDescription.GlobalTableDescription({_dafny.string_of(self.ReplicationGroup)}, {_dafny.string_of(self.GlobalTableArn)}, {_dafny.string_of(self.CreationDateTime)}, {_dafny.string_of(self.GlobalTableStatus)}, {_dafny.string_of(self.GlobalTableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableDescription_GlobalTableDescription) and self.ReplicationGroup == __o.ReplicationGroup and self.GlobalTableArn == __o.GlobalTableArn and self.CreationDateTime == __o.CreationDateTime and self.GlobalTableStatus == __o.GlobalTableStatus and self.GlobalTableName == __o.GlobalTableName
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalTableGlobalSecondaryIndexSettingsUpdate:
    @classmethod
    def default(cls, ):
        return lambda: GlobalTableGlobalSecondaryIndexSettingsUpdate_GlobalTableGlobalSecondaryIndexSettingsUpdate(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GlobalTableGlobalSecondaryIndexSettingsUpdate(self) -> bool:
        return isinstance(self, GlobalTableGlobalSecondaryIndexSettingsUpdate_GlobalTableGlobalSecondaryIndexSettingsUpdate)

class GlobalTableGlobalSecondaryIndexSettingsUpdate_GlobalTableGlobalSecondaryIndexSettingsUpdate(GlobalTableGlobalSecondaryIndexSettingsUpdate, NamedTuple('GlobalTableGlobalSecondaryIndexSettingsUpdate', [('IndexName', Any), ('ProvisionedWriteCapacityUnits', Any), ('ProvisionedWriteCapacityAutoScalingSettingsUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableGlobalSecondaryIndexSettingsUpdate.GlobalTableGlobalSecondaryIndexSettingsUpdate({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedWriteCapacityUnits)}, {_dafny.string_of(self.ProvisionedWriteCapacityAutoScalingSettingsUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableGlobalSecondaryIndexSettingsUpdate_GlobalTableGlobalSecondaryIndexSettingsUpdate) and self.IndexName == __o.IndexName and self.ProvisionedWriteCapacityUnits == __o.ProvisionedWriteCapacityUnits and self.ProvisionedWriteCapacityAutoScalingSettingsUpdate == __o.ProvisionedWriteCapacityAutoScalingSettingsUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class GlobalTableGlobalSecondaryIndexSettingsUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_3_x_: _dafny.Seq = source__
        return default__.IsValid__GlobalTableGlobalSecondaryIndexSettingsUpdateList(d_3_x_)

class GlobalTableStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [GlobalTableStatus_CREATING(), GlobalTableStatus_ACTIVE(), GlobalTableStatus_DELETING(), GlobalTableStatus_UPDATING()]
    @classmethod
    def default(cls, ):
        return lambda: GlobalTableStatus_CREATING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CREATING(self) -> bool:
        return isinstance(self, GlobalTableStatus_CREATING)
    @property
    def is_ACTIVE(self) -> bool:
        return isinstance(self, GlobalTableStatus_ACTIVE)
    @property
    def is_DELETING(self) -> bool:
        return isinstance(self, GlobalTableStatus_DELETING)
    @property
    def is_UPDATING(self) -> bool:
        return isinstance(self, GlobalTableStatus_UPDATING)

class GlobalTableStatus_CREATING(GlobalTableStatus, NamedTuple('CREATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableStatus.CREATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableStatus_CREATING)
    def __hash__(self) -> int:
        return super().__hash__()

class GlobalTableStatus_ACTIVE(GlobalTableStatus, NamedTuple('ACTIVE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableStatus.ACTIVE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableStatus_ACTIVE)
    def __hash__(self) -> int:
        return super().__hash__()

class GlobalTableStatus_DELETING(GlobalTableStatus, NamedTuple('DELETING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableStatus.DELETING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableStatus_DELETING)
    def __hash__(self) -> int:
        return super().__hash__()

class GlobalTableStatus_UPDATING(GlobalTableStatus, NamedTuple('UPDATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.GlobalTableStatus.UPDATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GlobalTableStatus_UPDATING)
    def __hash__(self) -> int:
        return super().__hash__()


class ImportArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_4_x_: _dafny.Seq = source__
        return default__.IsValid__ImportArn(d_4_x_)

class ImportedItemCount:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_5_x_: int = source__
        if True:
            return default__.IsValid__ImportedItemCount(d_5_x_)
        return False

class ImportNextToken:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_6_x_: _dafny.Seq = source__
        return default__.IsValid__ImportNextToken(d_6_x_)

class ImportStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ImportStatus_IN__PROGRESS(), ImportStatus_COMPLETED(), ImportStatus_CANCELLING(), ImportStatus_CANCELLED(), ImportStatus_FAILED()]
    @classmethod
    def default(cls, ):
        return lambda: ImportStatus_IN__PROGRESS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IN__PROGRESS(self) -> bool:
        return isinstance(self, ImportStatus_IN__PROGRESS)
    @property
    def is_COMPLETED(self) -> bool:
        return isinstance(self, ImportStatus_COMPLETED)
    @property
    def is_CANCELLING(self) -> bool:
        return isinstance(self, ImportStatus_CANCELLING)
    @property
    def is_CANCELLED(self) -> bool:
        return isinstance(self, ImportStatus_CANCELLED)
    @property
    def is_FAILED(self) -> bool:
        return isinstance(self, ImportStatus_FAILED)

class ImportStatus_IN__PROGRESS(ImportStatus, NamedTuple('IN__PROGRESS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportStatus.IN_PROGRESS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportStatus_IN__PROGRESS)
    def __hash__(self) -> int:
        return super().__hash__()

class ImportStatus_COMPLETED(ImportStatus, NamedTuple('COMPLETED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportStatus.COMPLETED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportStatus_COMPLETED)
    def __hash__(self) -> int:
        return super().__hash__()

class ImportStatus_CANCELLING(ImportStatus, NamedTuple('CANCELLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportStatus.CANCELLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportStatus_CANCELLING)
    def __hash__(self) -> int:
        return super().__hash__()

class ImportStatus_CANCELLED(ImportStatus, NamedTuple('CANCELLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportStatus.CANCELLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportStatus_CANCELLED)
    def __hash__(self) -> int:
        return super().__hash__()

class ImportStatus_FAILED(ImportStatus, NamedTuple('FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportStatus.FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportStatus_FAILED)
    def __hash__(self) -> int:
        return super().__hash__()


class ImportSummary:
    @classmethod
    def default(cls, ):
        return lambda: ImportSummary_ImportSummary(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportSummary(self) -> bool:
        return isinstance(self, ImportSummary_ImportSummary)

class ImportSummary_ImportSummary(ImportSummary, NamedTuple('ImportSummary', [('ImportArn', Any), ('ImportStatus', Any), ('TableArn', Any), ('S3BucketSource', Any), ('CloudWatchLogGroupArn', Any), ('InputFormat', Any), ('StartTime', Any), ('EndTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportSummary.ImportSummary({_dafny.string_of(self.ImportArn)}, {_dafny.string_of(self.ImportStatus)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.S3BucketSource)}, {_dafny.string_of(self.CloudWatchLogGroupArn)}, {_dafny.string_of(self.InputFormat)}, {_dafny.string_of(self.StartTime)}, {_dafny.string_of(self.EndTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportSummary_ImportSummary) and self.ImportArn == __o.ImportArn and self.ImportStatus == __o.ImportStatus and self.TableArn == __o.TableArn and self.S3BucketSource == __o.S3BucketSource and self.CloudWatchLogGroupArn == __o.CloudWatchLogGroupArn and self.InputFormat == __o.InputFormat and self.StartTime == __o.StartTime and self.EndTime == __o.EndTime
    def __hash__(self) -> int:
        return super().__hash__()


class ImportTableDescription:
    @classmethod
    def default(cls, ):
        return lambda: ImportTableDescription_ImportTableDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportTableDescription(self) -> bool:
        return isinstance(self, ImportTableDescription_ImportTableDescription)

class ImportTableDescription_ImportTableDescription(ImportTableDescription, NamedTuple('ImportTableDescription', [('ImportArn', Any), ('ImportStatus', Any), ('TableArn', Any), ('TableId', Any), ('ClientToken', Any), ('S3BucketSource', Any), ('ErrorCount', Any), ('CloudWatchLogGroupArn', Any), ('InputFormat', Any), ('InputFormatOptions', Any), ('InputCompressionType', Any), ('TableCreationParameters', Any), ('StartTime', Any), ('EndTime', Any), ('ProcessedSizeBytes', Any), ('ProcessedItemCount', Any), ('ImportedItemCount', Any), ('FailureCode', Any), ('FailureMessage', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportTableDescription.ImportTableDescription({_dafny.string_of(self.ImportArn)}, {_dafny.string_of(self.ImportStatus)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.TableId)}, {_dafny.string_of(self.ClientToken)}, {_dafny.string_of(self.S3BucketSource)}, {_dafny.string_of(self.ErrorCount)}, {_dafny.string_of(self.CloudWatchLogGroupArn)}, {_dafny.string_of(self.InputFormat)}, {_dafny.string_of(self.InputFormatOptions)}, {_dafny.string_of(self.InputCompressionType)}, {_dafny.string_of(self.TableCreationParameters)}, {_dafny.string_of(self.StartTime)}, {_dafny.string_of(self.EndTime)}, {_dafny.string_of(self.ProcessedSizeBytes)}, {_dafny.string_of(self.ProcessedItemCount)}, {_dafny.string_of(self.ImportedItemCount)}, {_dafny.string_of(self.FailureCode)}, {_dafny.string_of(self.FailureMessage)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportTableDescription_ImportTableDescription) and self.ImportArn == __o.ImportArn and self.ImportStatus == __o.ImportStatus and self.TableArn == __o.TableArn and self.TableId == __o.TableId and self.ClientToken == __o.ClientToken and self.S3BucketSource == __o.S3BucketSource and self.ErrorCount == __o.ErrorCount and self.CloudWatchLogGroupArn == __o.CloudWatchLogGroupArn and self.InputFormat == __o.InputFormat and self.InputFormatOptions == __o.InputFormatOptions and self.InputCompressionType == __o.InputCompressionType and self.TableCreationParameters == __o.TableCreationParameters and self.StartTime == __o.StartTime and self.EndTime == __o.EndTime and self.ProcessedSizeBytes == __o.ProcessedSizeBytes and self.ProcessedItemCount == __o.ProcessedItemCount and self.ImportedItemCount == __o.ImportedItemCount and self.FailureCode == __o.FailureCode and self.FailureMessage == __o.FailureMessage
    def __hash__(self) -> int:
        return super().__hash__()


class ImportTableInput:
    @classmethod
    def default(cls, ):
        return lambda: ImportTableInput_ImportTableInput(Wrappers.Option.default()(), S3BucketSource.default()(), InputFormat.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), TableCreationParameters.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportTableInput(self) -> bool:
        return isinstance(self, ImportTableInput_ImportTableInput)

class ImportTableInput_ImportTableInput(ImportTableInput, NamedTuple('ImportTableInput', [('ClientToken', Any), ('S3BucketSource', Any), ('InputFormat', Any), ('InputFormatOptions', Any), ('InputCompressionType', Any), ('TableCreationParameters', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportTableInput.ImportTableInput({_dafny.string_of(self.ClientToken)}, {_dafny.string_of(self.S3BucketSource)}, {_dafny.string_of(self.InputFormat)}, {_dafny.string_of(self.InputFormatOptions)}, {_dafny.string_of(self.InputCompressionType)}, {_dafny.string_of(self.TableCreationParameters)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportTableInput_ImportTableInput) and self.ClientToken == __o.ClientToken and self.S3BucketSource == __o.S3BucketSource and self.InputFormat == __o.InputFormat and self.InputFormatOptions == __o.InputFormatOptions and self.InputCompressionType == __o.InputCompressionType and self.TableCreationParameters == __o.TableCreationParameters
    def __hash__(self) -> int:
        return super().__hash__()


class ImportTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: ImportTableOutput_ImportTableOutput(ImportTableDescription.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportTableOutput(self) -> bool:
        return isinstance(self, ImportTableOutput_ImportTableOutput)

class ImportTableOutput_ImportTableOutput(ImportTableOutput, NamedTuple('ImportTableOutput', [('ImportTableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ImportTableOutput.ImportTableOutput({_dafny.string_of(self.ImportTableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportTableOutput_ImportTableOutput) and self.ImportTableDescription == __o.ImportTableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class IndexName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_7_x_: _dafny.Seq = source__
        return default__.IsValid__IndexName(d_7_x_)

class IndexStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [IndexStatus_CREATING(), IndexStatus_UPDATING(), IndexStatus_DELETING(), IndexStatus_ACTIVE()]
    @classmethod
    def default(cls, ):
        return lambda: IndexStatus_CREATING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CREATING(self) -> bool:
        return isinstance(self, IndexStatus_CREATING)
    @property
    def is_UPDATING(self) -> bool:
        return isinstance(self, IndexStatus_UPDATING)
    @property
    def is_DELETING(self) -> bool:
        return isinstance(self, IndexStatus_DELETING)
    @property
    def is_ACTIVE(self) -> bool:
        return isinstance(self, IndexStatus_ACTIVE)

class IndexStatus_CREATING(IndexStatus, NamedTuple('CREATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.IndexStatus.CREATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IndexStatus_CREATING)
    def __hash__(self) -> int:
        return super().__hash__()

class IndexStatus_UPDATING(IndexStatus, NamedTuple('UPDATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.IndexStatus.UPDATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IndexStatus_UPDATING)
    def __hash__(self) -> int:
        return super().__hash__()

class IndexStatus_DELETING(IndexStatus, NamedTuple('DELETING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.IndexStatus.DELETING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IndexStatus_DELETING)
    def __hash__(self) -> int:
        return super().__hash__()

class IndexStatus_ACTIVE(IndexStatus, NamedTuple('ACTIVE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.IndexStatus.ACTIVE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IndexStatus_ACTIVE)
    def __hash__(self) -> int:
        return super().__hash__()


class InputCompressionType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [InputCompressionType_GZIP(), InputCompressionType_ZSTD(), InputCompressionType_NONE()]
    @classmethod
    def default(cls, ):
        return lambda: InputCompressionType_GZIP()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GZIP(self) -> bool:
        return isinstance(self, InputCompressionType_GZIP)
    @property
    def is_ZSTD(self) -> bool:
        return isinstance(self, InputCompressionType_ZSTD)
    @property
    def is_NONE(self) -> bool:
        return isinstance(self, InputCompressionType_NONE)

class InputCompressionType_GZIP(InputCompressionType, NamedTuple('GZIP', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputCompressionType.GZIP'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputCompressionType_GZIP)
    def __hash__(self) -> int:
        return super().__hash__()

class InputCompressionType_ZSTD(InputCompressionType, NamedTuple('ZSTD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputCompressionType.ZSTD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputCompressionType_ZSTD)
    def __hash__(self) -> int:
        return super().__hash__()

class InputCompressionType_NONE(InputCompressionType, NamedTuple('NONE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputCompressionType.NONE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputCompressionType_NONE)
    def __hash__(self) -> int:
        return super().__hash__()


class InputFormat:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [InputFormat_DYNAMODB__JSON(), InputFormat_ION(), InputFormat_CSV()]
    @classmethod
    def default(cls, ):
        return lambda: InputFormat_DYNAMODB__JSON()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DYNAMODB__JSON(self) -> bool:
        return isinstance(self, InputFormat_DYNAMODB__JSON)
    @property
    def is_ION(self) -> bool:
        return isinstance(self, InputFormat_ION)
    @property
    def is_CSV(self) -> bool:
        return isinstance(self, InputFormat_CSV)

class InputFormat_DYNAMODB__JSON(InputFormat, NamedTuple('DYNAMODB__JSON', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputFormat.DYNAMODB_JSON'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputFormat_DYNAMODB__JSON)
    def __hash__(self) -> int:
        return super().__hash__()

class InputFormat_ION(InputFormat, NamedTuple('ION', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputFormat.ION'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputFormat_ION)
    def __hash__(self) -> int:
        return super().__hash__()

class InputFormat_CSV(InputFormat, NamedTuple('CSV', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputFormat.CSV'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputFormat_CSV)
    def __hash__(self) -> int:
        return super().__hash__()


class InputFormatOptions:
    @classmethod
    def default(cls, ):
        return lambda: InputFormatOptions_InputFormatOptions(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InputFormatOptions(self) -> bool:
        return isinstance(self, InputFormatOptions_InputFormatOptions)

class InputFormatOptions_InputFormatOptions(InputFormatOptions, NamedTuple('InputFormatOptions', [('Csv', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.InputFormatOptions.InputFormatOptions({_dafny.string_of(self.Csv)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InputFormatOptions_InputFormatOptions) and self.Csv == __o.Csv
    def __hash__(self) -> int:
        return super().__hash__()


class ItemCollectionMetrics:
    @classmethod
    def default(cls, ):
        return lambda: ItemCollectionMetrics_ItemCollectionMetrics(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ItemCollectionMetrics(self) -> bool:
        return isinstance(self, ItemCollectionMetrics_ItemCollectionMetrics)

class ItemCollectionMetrics_ItemCollectionMetrics(ItemCollectionMetrics, NamedTuple('ItemCollectionMetrics', [('ItemCollectionKey', Any), ('SizeEstimateRangeGB', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ItemCollectionMetrics.ItemCollectionMetrics({_dafny.string_of(self.ItemCollectionKey)}, {_dafny.string_of(self.SizeEstimateRangeGB)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ItemCollectionMetrics_ItemCollectionMetrics) and self.ItemCollectionKey == __o.ItemCollectionKey and self.SizeEstimateRangeGB == __o.SizeEstimateRangeGB
    def __hash__(self) -> int:
        return super().__hash__()


class ItemCollectionSizeEstimateBound:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_8_x_: _dafny.Seq = source__
        return default__.IsValid__ItemCollectionSizeEstimateBound(d_8_x_)

class ItemCount:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_9_x_: int = source__
        if True:
            return default__.IsValid__ItemCount(d_9_x_)
        return False

class ItemResponse:
    @classmethod
    def default(cls, ):
        return lambda: ItemResponse_ItemResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ItemResponse(self) -> bool:
        return isinstance(self, ItemResponse_ItemResponse)

class ItemResponse_ItemResponse(ItemResponse, NamedTuple('ItemResponse', [('Item', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ItemResponse.ItemResponse({_dafny.string_of(self.Item)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ItemResponse_ItemResponse) and self.Item == __o.Item
    def __hash__(self) -> int:
        return super().__hash__()


class ItemResponseList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_10_x_: _dafny.Seq = source__
        return default__.IsValid__ItemResponseList(d_10_x_)

class KeyList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_11_x_: _dafny.Seq = source__
        return default__.IsValid__KeyList(d_11_x_)

class KeysAndAttributes:
    @classmethod
    def default(cls, ):
        return lambda: KeysAndAttributes_KeysAndAttributes(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeysAndAttributes(self) -> bool:
        return isinstance(self, KeysAndAttributes_KeysAndAttributes)

class KeysAndAttributes_KeysAndAttributes(KeysAndAttributes, NamedTuple('KeysAndAttributes', [('Keys', Any), ('AttributesToGet', Any), ('ConsistentRead', Any), ('ProjectionExpression', Any), ('ExpressionAttributeNames', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KeysAndAttributes.KeysAndAttributes({_dafny.string_of(self.Keys)}, {_dafny.string_of(self.AttributesToGet)}, {_dafny.string_of(self.ConsistentRead)}, {_dafny.string_of(self.ProjectionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeysAndAttributes_KeysAndAttributes) and self.Keys == __o.Keys and self.AttributesToGet == __o.AttributesToGet and self.ConsistentRead == __o.ConsistentRead and self.ProjectionExpression == __o.ProjectionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames
    def __hash__(self) -> int:
        return super().__hash__()


class KeySchema:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_12_x_: _dafny.Seq = source__
        return default__.IsValid__KeySchema(d_12_x_)

class KeySchemaAttributeName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_13_x_: _dafny.Seq = source__
        return default__.IsValid__KeySchemaAttributeName(d_13_x_)

class KeySchemaElement:
    @classmethod
    def default(cls, ):
        return lambda: KeySchemaElement_KeySchemaElement(_dafny.Seq(""), KeyType.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeySchemaElement(self) -> bool:
        return isinstance(self, KeySchemaElement_KeySchemaElement)

class KeySchemaElement_KeySchemaElement(KeySchemaElement, NamedTuple('KeySchemaElement', [('AttributeName', Any), ('KeyType', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KeySchemaElement.KeySchemaElement({_dafny.string_of(self.AttributeName)}, {_dafny.string_of(self.KeyType)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySchemaElement_KeySchemaElement) and self.AttributeName == __o.AttributeName and self.KeyType == __o.KeyType
    def __hash__(self) -> int:
        return super().__hash__()


class KeyType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyType_HASH(), KeyType_RANGE()]
    @classmethod
    def default(cls, ):
        return lambda: KeyType_HASH()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HASH(self) -> bool:
        return isinstance(self, KeyType_HASH)
    @property
    def is_RANGE(self) -> bool:
        return isinstance(self, KeyType_RANGE)

class KeyType_HASH(KeyType, NamedTuple('HASH', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KeyType.HASH'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyType_HASH)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyType_RANGE(KeyType, NamedTuple('RANGE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KeyType.RANGE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyType_RANGE)
    def __hash__(self) -> int:
        return super().__hash__()


class KinesisDataStreamDestination:
    @classmethod
    def default(cls, ):
        return lambda: KinesisDataStreamDestination_KinesisDataStreamDestination(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KinesisDataStreamDestination(self) -> bool:
        return isinstance(self, KinesisDataStreamDestination_KinesisDataStreamDestination)

class KinesisDataStreamDestination_KinesisDataStreamDestination(KinesisDataStreamDestination, NamedTuple('KinesisDataStreamDestination', [('StreamArn', Any), ('DestinationStatus', Any), ('DestinationStatusDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KinesisDataStreamDestination.KinesisDataStreamDestination({_dafny.string_of(self.StreamArn)}, {_dafny.string_of(self.DestinationStatus)}, {_dafny.string_of(self.DestinationStatusDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KinesisDataStreamDestination_KinesisDataStreamDestination) and self.StreamArn == __o.StreamArn and self.DestinationStatus == __o.DestinationStatus and self.DestinationStatusDescription == __o.DestinationStatusDescription
    def __hash__(self) -> int:
        return super().__hash__()


class KinesisStreamingDestinationInput:
    @classmethod
    def default(cls, ):
        return lambda: KinesisStreamingDestinationInput_KinesisStreamingDestinationInput(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KinesisStreamingDestinationInput(self) -> bool:
        return isinstance(self, KinesisStreamingDestinationInput_KinesisStreamingDestinationInput)

class KinesisStreamingDestinationInput_KinesisStreamingDestinationInput(KinesisStreamingDestinationInput, NamedTuple('KinesisStreamingDestinationInput', [('TableName', Any), ('StreamArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KinesisStreamingDestinationInput.KinesisStreamingDestinationInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KinesisStreamingDestinationInput_KinesisStreamingDestinationInput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn
    def __hash__(self) -> int:
        return super().__hash__()


class KinesisStreamingDestinationOutput:
    @classmethod
    def default(cls, ):
        return lambda: KinesisStreamingDestinationOutput_KinesisStreamingDestinationOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KinesisStreamingDestinationOutput(self) -> bool:
        return isinstance(self, KinesisStreamingDestinationOutput_KinesisStreamingDestinationOutput)

class KinesisStreamingDestinationOutput_KinesisStreamingDestinationOutput(KinesisStreamingDestinationOutput, NamedTuple('KinesisStreamingDestinationOutput', [('TableName', Any), ('StreamArn', Any), ('DestinationStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.KinesisStreamingDestinationOutput.KinesisStreamingDestinationOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.StreamArn)}, {_dafny.string_of(self.DestinationStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KinesisStreamingDestinationOutput_KinesisStreamingDestinationOutput) and self.TableName == __o.TableName and self.StreamArn == __o.StreamArn and self.DestinationStatus == __o.DestinationStatus
    def __hash__(self) -> int:
        return super().__hash__()


class ListBackupsInput:
    @classmethod
    def default(cls, ):
        return lambda: ListBackupsInput_ListBackupsInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListBackupsInput(self) -> bool:
        return isinstance(self, ListBackupsInput_ListBackupsInput)

class ListBackupsInput_ListBackupsInput(ListBackupsInput, NamedTuple('ListBackupsInput', [('TableName', Any), ('Limit', Any), ('TimeRangeLowerBound', Any), ('TimeRangeUpperBound', Any), ('ExclusiveStartBackupArn', Any), ('BackupType', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListBackupsInput.ListBackupsInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.TimeRangeLowerBound)}, {_dafny.string_of(self.TimeRangeUpperBound)}, {_dafny.string_of(self.ExclusiveStartBackupArn)}, {_dafny.string_of(self.BackupType)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListBackupsInput_ListBackupsInput) and self.TableName == __o.TableName and self.Limit == __o.Limit and self.TimeRangeLowerBound == __o.TimeRangeLowerBound and self.TimeRangeUpperBound == __o.TimeRangeUpperBound and self.ExclusiveStartBackupArn == __o.ExclusiveStartBackupArn and self.BackupType == __o.BackupType
    def __hash__(self) -> int:
        return super().__hash__()


class ListBackupsOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListBackupsOutput_ListBackupsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListBackupsOutput(self) -> bool:
        return isinstance(self, ListBackupsOutput_ListBackupsOutput)

class ListBackupsOutput_ListBackupsOutput(ListBackupsOutput, NamedTuple('ListBackupsOutput', [('BackupSummaries', Any), ('LastEvaluatedBackupArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListBackupsOutput.ListBackupsOutput({_dafny.string_of(self.BackupSummaries)}, {_dafny.string_of(self.LastEvaluatedBackupArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListBackupsOutput_ListBackupsOutput) and self.BackupSummaries == __o.BackupSummaries and self.LastEvaluatedBackupArn == __o.LastEvaluatedBackupArn
    def __hash__(self) -> int:
        return super().__hash__()


class ListContributorInsightsInput:
    @classmethod
    def default(cls, ):
        return lambda: ListContributorInsightsInput_ListContributorInsightsInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListContributorInsightsInput(self) -> bool:
        return isinstance(self, ListContributorInsightsInput_ListContributorInsightsInput)

class ListContributorInsightsInput_ListContributorInsightsInput(ListContributorInsightsInput, NamedTuple('ListContributorInsightsInput', [('TableName', Any), ('NextToken', Any), ('MaxResults', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListContributorInsightsInput.ListContributorInsightsInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.NextToken)}, {_dafny.string_of(self.MaxResults)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListContributorInsightsInput_ListContributorInsightsInput) and self.TableName == __o.TableName and self.NextToken == __o.NextToken and self.MaxResults == __o.MaxResults
    def __hash__(self) -> int:
        return super().__hash__()


class ListContributorInsightsLimit:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_14_x_: int = source__
        if True:
            return default__.IsValid__ListContributorInsightsLimit(d_14_x_)
        return False

class ListContributorInsightsOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListContributorInsightsOutput_ListContributorInsightsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListContributorInsightsOutput(self) -> bool:
        return isinstance(self, ListContributorInsightsOutput_ListContributorInsightsOutput)

class ListContributorInsightsOutput_ListContributorInsightsOutput(ListContributorInsightsOutput, NamedTuple('ListContributorInsightsOutput', [('ContributorInsightsSummaries', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListContributorInsightsOutput.ListContributorInsightsOutput({_dafny.string_of(self.ContributorInsightsSummaries)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListContributorInsightsOutput_ListContributorInsightsOutput) and self.ContributorInsightsSummaries == __o.ContributorInsightsSummaries and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListExportsInput:
    @classmethod
    def default(cls, ):
        return lambda: ListExportsInput_ListExportsInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListExportsInput(self) -> bool:
        return isinstance(self, ListExportsInput_ListExportsInput)

class ListExportsInput_ListExportsInput(ListExportsInput, NamedTuple('ListExportsInput', [('TableArn', Any), ('MaxResults', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListExportsInput.ListExportsInput({_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.MaxResults)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListExportsInput_ListExportsInput) and self.TableArn == __o.TableArn and self.MaxResults == __o.MaxResults and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListExportsMaxLimit:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_15_x_: int = source__
        if True:
            return default__.IsValid__ListExportsMaxLimit(d_15_x_)
        return False

class ListExportsOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListExportsOutput_ListExportsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListExportsOutput(self) -> bool:
        return isinstance(self, ListExportsOutput_ListExportsOutput)

class ListExportsOutput_ListExportsOutput(ListExportsOutput, NamedTuple('ListExportsOutput', [('ExportSummaries', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListExportsOutput.ListExportsOutput({_dafny.string_of(self.ExportSummaries)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListExportsOutput_ListExportsOutput) and self.ExportSummaries == __o.ExportSummaries and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListGlobalTablesInput:
    @classmethod
    def default(cls, ):
        return lambda: ListGlobalTablesInput_ListGlobalTablesInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListGlobalTablesInput(self) -> bool:
        return isinstance(self, ListGlobalTablesInput_ListGlobalTablesInput)

class ListGlobalTablesInput_ListGlobalTablesInput(ListGlobalTablesInput, NamedTuple('ListGlobalTablesInput', [('ExclusiveStartGlobalTableName', Any), ('Limit', Any), ('RegionName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListGlobalTablesInput.ListGlobalTablesInput({_dafny.string_of(self.ExclusiveStartGlobalTableName)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.RegionName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListGlobalTablesInput_ListGlobalTablesInput) and self.ExclusiveStartGlobalTableName == __o.ExclusiveStartGlobalTableName and self.Limit == __o.Limit and self.RegionName == __o.RegionName
    def __hash__(self) -> int:
        return super().__hash__()


class ListGlobalTablesOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListGlobalTablesOutput_ListGlobalTablesOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListGlobalTablesOutput(self) -> bool:
        return isinstance(self, ListGlobalTablesOutput_ListGlobalTablesOutput)

class ListGlobalTablesOutput_ListGlobalTablesOutput(ListGlobalTablesOutput, NamedTuple('ListGlobalTablesOutput', [('GlobalTables', Any), ('LastEvaluatedGlobalTableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListGlobalTablesOutput.ListGlobalTablesOutput({_dafny.string_of(self.GlobalTables)}, {_dafny.string_of(self.LastEvaluatedGlobalTableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListGlobalTablesOutput_ListGlobalTablesOutput) and self.GlobalTables == __o.GlobalTables and self.LastEvaluatedGlobalTableName == __o.LastEvaluatedGlobalTableName
    def __hash__(self) -> int:
        return super().__hash__()


class ListImportsInput:
    @classmethod
    def default(cls, ):
        return lambda: ListImportsInput_ListImportsInput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListImportsInput(self) -> bool:
        return isinstance(self, ListImportsInput_ListImportsInput)

class ListImportsInput_ListImportsInput(ListImportsInput, NamedTuple('ListImportsInput', [('TableArn', Any), ('PageSize', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListImportsInput.ListImportsInput({_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.PageSize)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListImportsInput_ListImportsInput) and self.TableArn == __o.TableArn and self.PageSize == __o.PageSize and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListImportsMaxLimit:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_16_x_: int = source__
        if True:
            return default__.IsValid__ListImportsMaxLimit(d_16_x_)
        return False

class ListImportsOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListImportsOutput_ListImportsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListImportsOutput(self) -> bool:
        return isinstance(self, ListImportsOutput_ListImportsOutput)

class ListImportsOutput_ListImportsOutput(ListImportsOutput, NamedTuple('ListImportsOutput', [('ImportSummaryList', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListImportsOutput.ListImportsOutput({_dafny.string_of(self.ImportSummaryList)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListImportsOutput_ListImportsOutput) and self.ImportSummaryList == __o.ImportSummaryList and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListTablesInput:
    @classmethod
    def default(cls, ):
        return lambda: ListTablesInput_ListTablesInput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListTablesInput(self) -> bool:
        return isinstance(self, ListTablesInput_ListTablesInput)

class ListTablesInput_ListTablesInput(ListTablesInput, NamedTuple('ListTablesInput', [('ExclusiveStartTableName', Any), ('Limit', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListTablesInput.ListTablesInput({_dafny.string_of(self.ExclusiveStartTableName)}, {_dafny.string_of(self.Limit)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListTablesInput_ListTablesInput) and self.ExclusiveStartTableName == __o.ExclusiveStartTableName and self.Limit == __o.Limit
    def __hash__(self) -> int:
        return super().__hash__()


class ListTablesInputLimit:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_17_x_: int = source__
        if True:
            return default__.IsValid__ListTablesInputLimit(d_17_x_)
        return False

class ListTablesOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListTablesOutput_ListTablesOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListTablesOutput(self) -> bool:
        return isinstance(self, ListTablesOutput_ListTablesOutput)

class ListTablesOutput_ListTablesOutput(ListTablesOutput, NamedTuple('ListTablesOutput', [('TableNames', Any), ('LastEvaluatedTableName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListTablesOutput.ListTablesOutput({_dafny.string_of(self.TableNames)}, {_dafny.string_of(self.LastEvaluatedTableName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListTablesOutput_ListTablesOutput) and self.TableNames == __o.TableNames and self.LastEvaluatedTableName == __o.LastEvaluatedTableName
    def __hash__(self) -> int:
        return super().__hash__()


class ListTagsOfResourceInput:
    @classmethod
    def default(cls, ):
        return lambda: ListTagsOfResourceInput_ListTagsOfResourceInput(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListTagsOfResourceInput(self) -> bool:
        return isinstance(self, ListTagsOfResourceInput_ListTagsOfResourceInput)

class ListTagsOfResourceInput_ListTagsOfResourceInput(ListTagsOfResourceInput, NamedTuple('ListTagsOfResourceInput', [('ResourceArn', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListTagsOfResourceInput.ListTagsOfResourceInput({_dafny.string_of(self.ResourceArn)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListTagsOfResourceInput_ListTagsOfResourceInput) and self.ResourceArn == __o.ResourceArn and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class ListTagsOfResourceOutput:
    @classmethod
    def default(cls, ):
        return lambda: ListTagsOfResourceOutput_ListTagsOfResourceOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListTagsOfResourceOutput(self) -> bool:
        return isinstance(self, ListTagsOfResourceOutput_ListTagsOfResourceOutput)

class ListTagsOfResourceOutput_ListTagsOfResourceOutput(ListTagsOfResourceOutput, NamedTuple('ListTagsOfResourceOutput', [('Tags', Any), ('NextToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ListTagsOfResourceOutput.ListTagsOfResourceOutput({_dafny.string_of(self.Tags)}, {_dafny.string_of(self.NextToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListTagsOfResourceOutput_ListTagsOfResourceOutput) and self.Tags == __o.Tags and self.NextToken == __o.NextToken
    def __hash__(self) -> int:
        return super().__hash__()


class LocalSecondaryIndex:
    @classmethod
    def default(cls, ):
        return lambda: LocalSecondaryIndex_LocalSecondaryIndex(_dafny.Seq(""), _dafny.Seq({}), Projection.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_LocalSecondaryIndex(self) -> bool:
        return isinstance(self, LocalSecondaryIndex_LocalSecondaryIndex)

class LocalSecondaryIndex_LocalSecondaryIndex(LocalSecondaryIndex, NamedTuple('LocalSecondaryIndex', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.LocalSecondaryIndex.LocalSecondaryIndex({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LocalSecondaryIndex_LocalSecondaryIndex) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection
    def __hash__(self) -> int:
        return super().__hash__()


class LocalSecondaryIndexDescription:
    @classmethod
    def default(cls, ):
        return lambda: LocalSecondaryIndexDescription_LocalSecondaryIndexDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_LocalSecondaryIndexDescription(self) -> bool:
        return isinstance(self, LocalSecondaryIndexDescription_LocalSecondaryIndexDescription)

class LocalSecondaryIndexDescription_LocalSecondaryIndexDescription(LocalSecondaryIndexDescription, NamedTuple('LocalSecondaryIndexDescription', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any), ('IndexSizeBytes', Any), ('ItemCount', Any), ('IndexArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.LocalSecondaryIndexDescription.LocalSecondaryIndexDescription({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)}, {_dafny.string_of(self.IndexSizeBytes)}, {_dafny.string_of(self.ItemCount)}, {_dafny.string_of(self.IndexArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LocalSecondaryIndexDescription_LocalSecondaryIndexDescription) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection and self.IndexSizeBytes == __o.IndexSizeBytes and self.ItemCount == __o.ItemCount and self.IndexArn == __o.IndexArn
    def __hash__(self) -> int:
        return super().__hash__()


class LocalSecondaryIndexInfo:
    @classmethod
    def default(cls, ):
        return lambda: LocalSecondaryIndexInfo_LocalSecondaryIndexInfo(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_LocalSecondaryIndexInfo(self) -> bool:
        return isinstance(self, LocalSecondaryIndexInfo_LocalSecondaryIndexInfo)

class LocalSecondaryIndexInfo_LocalSecondaryIndexInfo(LocalSecondaryIndexInfo, NamedTuple('LocalSecondaryIndexInfo', [('IndexName', Any), ('KeySchema', Any), ('Projection', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.LocalSecondaryIndexInfo.LocalSecondaryIndexInfo({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.Projection)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LocalSecondaryIndexInfo_LocalSecondaryIndexInfo) and self.IndexName == __o.IndexName and self.KeySchema == __o.KeySchema and self.Projection == __o.Projection
    def __hash__(self) -> int:
        return super().__hash__()


class NonKeyAttributeName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_18_x_: _dafny.Seq = source__
        return default__.IsValid__NonKeyAttributeName(d_18_x_)

class NonKeyAttributeNameList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_19_x_: _dafny.Seq = source__
        return default__.IsValid__NonKeyAttributeNameList(d_19_x_)

class NonNegativeLongObject:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_20_x_: int = source__
        if True:
            return default__.IsValid__NonNegativeLongObject(d_20_x_)
        return False

class ParameterizedStatement:
    @classmethod
    def default(cls, ):
        return lambda: ParameterizedStatement_ParameterizedStatement(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ParameterizedStatement(self) -> bool:
        return isinstance(self, ParameterizedStatement_ParameterizedStatement)

class ParameterizedStatement_ParameterizedStatement(ParameterizedStatement, NamedTuple('ParameterizedStatement', [('Statement', Any), ('Parameters', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ParameterizedStatement.ParameterizedStatement({_dafny.string_of(self.Statement)}, {_dafny.string_of(self.Parameters)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ParameterizedStatement_ParameterizedStatement) and self.Statement == __o.Statement and self.Parameters == __o.Parameters
    def __hash__(self) -> int:
        return super().__hash__()


class ParameterizedStatements:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_21_x_: _dafny.Seq = source__
        return default__.IsValid__ParameterizedStatements(d_21_x_)

class PartiQLBatchRequest:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_22_x_: _dafny.Seq = source__
        return default__.IsValid__PartiQLBatchRequest(d_22_x_)

class PartiQLNextToken:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_23_x_: _dafny.Seq = source__
        return default__.IsValid__PartiQLNextToken(d_23_x_)

class PartiQLStatement:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_24_x_: _dafny.Seq = source__
        return default__.IsValid__PartiQLStatement(d_24_x_)

class PointInTimeRecoveryDescription:
    @classmethod
    def default(cls, ):
        return lambda: PointInTimeRecoveryDescription_PointInTimeRecoveryDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PointInTimeRecoveryDescription(self) -> bool:
        return isinstance(self, PointInTimeRecoveryDescription_PointInTimeRecoveryDescription)

class PointInTimeRecoveryDescription_PointInTimeRecoveryDescription(PointInTimeRecoveryDescription, NamedTuple('PointInTimeRecoveryDescription', [('PointInTimeRecoveryStatus', Any), ('EarliestRestorableDateTime', Any), ('LatestRestorableDateTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PointInTimeRecoveryDescription.PointInTimeRecoveryDescription({_dafny.string_of(self.PointInTimeRecoveryStatus)}, {_dafny.string_of(self.EarliestRestorableDateTime)}, {_dafny.string_of(self.LatestRestorableDateTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PointInTimeRecoveryDescription_PointInTimeRecoveryDescription) and self.PointInTimeRecoveryStatus == __o.PointInTimeRecoveryStatus and self.EarliestRestorableDateTime == __o.EarliestRestorableDateTime and self.LatestRestorableDateTime == __o.LatestRestorableDateTime
    def __hash__(self) -> int:
        return super().__hash__()


class PointInTimeRecoverySpecification:
    @classmethod
    def default(cls, ):
        return lambda: PointInTimeRecoverySpecification_PointInTimeRecoverySpecification(False)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PointInTimeRecoverySpecification(self) -> bool:
        return isinstance(self, PointInTimeRecoverySpecification_PointInTimeRecoverySpecification)

class PointInTimeRecoverySpecification_PointInTimeRecoverySpecification(PointInTimeRecoverySpecification, NamedTuple('PointInTimeRecoverySpecification', [('PointInTimeRecoveryEnabled', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PointInTimeRecoverySpecification.PointInTimeRecoverySpecification({_dafny.string_of(self.PointInTimeRecoveryEnabled)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PointInTimeRecoverySpecification_PointInTimeRecoverySpecification) and self.PointInTimeRecoveryEnabled == __o.PointInTimeRecoveryEnabled
    def __hash__(self) -> int:
        return super().__hash__()


class PointInTimeRecoveryStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [PointInTimeRecoveryStatus_ENABLED(), PointInTimeRecoveryStatus_DISABLED()]
    @classmethod
    def default(cls, ):
        return lambda: PointInTimeRecoveryStatus_ENABLED()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLED(self) -> bool:
        return isinstance(self, PointInTimeRecoveryStatus_ENABLED)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, PointInTimeRecoveryStatus_DISABLED)

class PointInTimeRecoveryStatus_ENABLED(PointInTimeRecoveryStatus, NamedTuple('ENABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PointInTimeRecoveryStatus.ENABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PointInTimeRecoveryStatus_ENABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class PointInTimeRecoveryStatus_DISABLED(PointInTimeRecoveryStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PointInTimeRecoveryStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PointInTimeRecoveryStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()


class PositiveIntegerObject:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_25_x_: int = source__
        if True:
            return default__.IsValid__PositiveIntegerObject(d_25_x_)
        return False

class PositiveLongObject:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_26_x_: int = source__
        if True:
            return default__.IsValid__PositiveLongObject(d_26_x_)
        return False

class PreparedStatementParameters:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_27_x_: _dafny.Seq = source__
        return default__.IsValid__PreparedStatementParameters(d_27_x_)

class ProcessedItemCount:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_28_x_: int = source__
        if True:
            return default__.IsValid__ProcessedItemCount(d_28_x_)
        return False

class Projection:
    @classmethod
    def default(cls, ):
        return lambda: Projection_Projection(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Projection(self) -> bool:
        return isinstance(self, Projection_Projection)

class Projection_Projection(Projection, NamedTuple('Projection', [('ProjectionType', Any), ('NonKeyAttributes', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Projection.Projection({_dafny.string_of(self.ProjectionType)}, {_dafny.string_of(self.NonKeyAttributes)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Projection_Projection) and self.ProjectionType == __o.ProjectionType and self.NonKeyAttributes == __o.NonKeyAttributes
    def __hash__(self) -> int:
        return super().__hash__()


class ProjectionType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ProjectionType_ALL(), ProjectionType_KEYS__ONLY(), ProjectionType_INCLUDE()]
    @classmethod
    def default(cls, ):
        return lambda: ProjectionType_ALL()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALL(self) -> bool:
        return isinstance(self, ProjectionType_ALL)
    @property
    def is_KEYS__ONLY(self) -> bool:
        return isinstance(self, ProjectionType_KEYS__ONLY)
    @property
    def is_INCLUDE(self) -> bool:
        return isinstance(self, ProjectionType_INCLUDE)

class ProjectionType_ALL(ProjectionType, NamedTuple('ALL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProjectionType.ALL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProjectionType_ALL)
    def __hash__(self) -> int:
        return super().__hash__()

class ProjectionType_KEYS__ONLY(ProjectionType, NamedTuple('KEYS__ONLY', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProjectionType.KEYS_ONLY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProjectionType_KEYS__ONLY)
    def __hash__(self) -> int:
        return super().__hash__()

class ProjectionType_INCLUDE(ProjectionType, NamedTuple('INCLUDE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProjectionType.INCLUDE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProjectionType_INCLUDE)
    def __hash__(self) -> int:
        return super().__hash__()


class ProvisionedThroughput:
    @classmethod
    def default(cls, ):
        return lambda: ProvisionedThroughput_ProvisionedThroughput(int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ProvisionedThroughput(self) -> bool:
        return isinstance(self, ProvisionedThroughput_ProvisionedThroughput)

class ProvisionedThroughput_ProvisionedThroughput(ProvisionedThroughput, NamedTuple('ProvisionedThroughput', [('ReadCapacityUnits', Any), ('WriteCapacityUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProvisionedThroughput.ProvisionedThroughput({_dafny.string_of(self.ReadCapacityUnits)}, {_dafny.string_of(self.WriteCapacityUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProvisionedThroughput_ProvisionedThroughput) and self.ReadCapacityUnits == __o.ReadCapacityUnits and self.WriteCapacityUnits == __o.WriteCapacityUnits
    def __hash__(self) -> int:
        return super().__hash__()


class ProvisionedThroughputDescription:
    @classmethod
    def default(cls, ):
        return lambda: ProvisionedThroughputDescription_ProvisionedThroughputDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ProvisionedThroughputDescription(self) -> bool:
        return isinstance(self, ProvisionedThroughputDescription_ProvisionedThroughputDescription)

class ProvisionedThroughputDescription_ProvisionedThroughputDescription(ProvisionedThroughputDescription, NamedTuple('ProvisionedThroughputDescription', [('LastIncreaseDateTime', Any), ('LastDecreaseDateTime', Any), ('NumberOfDecreasesToday', Any), ('ReadCapacityUnits', Any), ('WriteCapacityUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProvisionedThroughputDescription.ProvisionedThroughputDescription({_dafny.string_of(self.LastIncreaseDateTime)}, {_dafny.string_of(self.LastDecreaseDateTime)}, {_dafny.string_of(self.NumberOfDecreasesToday)}, {_dafny.string_of(self.ReadCapacityUnits)}, {_dafny.string_of(self.WriteCapacityUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProvisionedThroughputDescription_ProvisionedThroughputDescription) and self.LastIncreaseDateTime == __o.LastIncreaseDateTime and self.LastDecreaseDateTime == __o.LastDecreaseDateTime and self.NumberOfDecreasesToday == __o.NumberOfDecreasesToday and self.ReadCapacityUnits == __o.ReadCapacityUnits and self.WriteCapacityUnits == __o.WriteCapacityUnits
    def __hash__(self) -> int:
        return super().__hash__()


class ProvisionedThroughputOverride:
    @classmethod
    def default(cls, ):
        return lambda: ProvisionedThroughputOverride_ProvisionedThroughputOverride(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ProvisionedThroughputOverride(self) -> bool:
        return isinstance(self, ProvisionedThroughputOverride_ProvisionedThroughputOverride)

class ProvisionedThroughputOverride_ProvisionedThroughputOverride(ProvisionedThroughputOverride, NamedTuple('ProvisionedThroughputOverride', [('ReadCapacityUnits', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ProvisionedThroughputOverride.ProvisionedThroughputOverride({_dafny.string_of(self.ReadCapacityUnits)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ProvisionedThroughputOverride_ProvisionedThroughputOverride) and self.ReadCapacityUnits == __o.ReadCapacityUnits
    def __hash__(self) -> int:
        return super().__hash__()


class Put:
    @classmethod
    def default(cls, ):
        return lambda: Put_Put(_dafny.Map({}), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Put(self) -> bool:
        return isinstance(self, Put_Put)

class Put_Put(Put, NamedTuple('Put', [('Item', Any), ('TableName', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any), ('ReturnValuesOnConditionCheckFailure', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Put.Put({_dafny.string_of(self.Item)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)}, {_dafny.string_of(self.ReturnValuesOnConditionCheckFailure)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Put_Put) and self.Item == __o.Item and self.TableName == __o.TableName and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues and self.ReturnValuesOnConditionCheckFailure == __o.ReturnValuesOnConditionCheckFailure
    def __hash__(self) -> int:
        return super().__hash__()


class PutItemInput:
    @classmethod
    def default(cls, ):
        return lambda: PutItemInput_PutItemInput(_dafny.Seq(""), _dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutItemInput(self) -> bool:
        return isinstance(self, PutItemInput_PutItemInput)

class PutItemInput_PutItemInput(PutItemInput, NamedTuple('PutItemInput', [('TableName', Any), ('Item', Any), ('Expected', Any), ('ReturnValues', Any), ('ReturnConsumedCapacity', Any), ('ReturnItemCollectionMetrics', Any), ('ConditionalOperator', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PutItemInput.PutItemInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Item)}, {_dafny.string_of(self.Expected)}, {_dafny.string_of(self.ReturnValues)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ReturnItemCollectionMetrics)}, {_dafny.string_of(self.ConditionalOperator)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PutItemInput_PutItemInput) and self.TableName == __o.TableName and self.Item == __o.Item and self.Expected == __o.Expected and self.ReturnValues == __o.ReturnValues and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ReturnItemCollectionMetrics == __o.ReturnItemCollectionMetrics and self.ConditionalOperator == __o.ConditionalOperator and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues
    def __hash__(self) -> int:
        return super().__hash__()


class PutItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: PutItemOutput_PutItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutItemOutput(self) -> bool:
        return isinstance(self, PutItemOutput_PutItemOutput)

class PutItemOutput_PutItemOutput(PutItemOutput, NamedTuple('PutItemOutput', [('Attributes', Any), ('ConsumedCapacity', Any), ('ItemCollectionMetrics', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PutItemOutput.PutItemOutput({_dafny.string_of(self.Attributes)}, {_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.ItemCollectionMetrics)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PutItemOutput_PutItemOutput) and self.Attributes == __o.Attributes and self.ConsumedCapacity == __o.ConsumedCapacity and self.ItemCollectionMetrics == __o.ItemCollectionMetrics
    def __hash__(self) -> int:
        return super().__hash__()


class PutRequest:
    @classmethod
    def default(cls, ):
        return lambda: PutRequest_PutRequest(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutRequest(self) -> bool:
        return isinstance(self, PutRequest_PutRequest)

class PutRequest_PutRequest(PutRequest, NamedTuple('PutRequest', [('Item', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.PutRequest.PutRequest({_dafny.string_of(self.Item)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PutRequest_PutRequest) and self.Item == __o.Item
    def __hash__(self) -> int:
        return super().__hash__()


class QueryInput:
    @classmethod
    def default(cls, ):
        return lambda: QueryInput_QueryInput(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_QueryInput(self) -> bool:
        return isinstance(self, QueryInput_QueryInput)

class QueryInput_QueryInput(QueryInput, NamedTuple('QueryInput', [('TableName', Any), ('IndexName', Any), ('Select', Any), ('AttributesToGet', Any), ('Limit', Any), ('ConsistentRead', Any), ('KeyConditions', Any), ('QueryFilter', Any), ('ConditionalOperator', Any), ('ScanIndexForward', Any), ('ExclusiveStartKey', Any), ('ReturnConsumedCapacity', Any), ('ProjectionExpression', Any), ('FilterExpression', Any), ('KeyConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.QueryInput.QueryInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.Select)}, {_dafny.string_of(self.AttributesToGet)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.ConsistentRead)}, {_dafny.string_of(self.KeyConditions)}, {_dafny.string_of(self.QueryFilter)}, {_dafny.string_of(self.ConditionalOperator)}, {_dafny.string_of(self.ScanIndexForward)}, {_dafny.string_of(self.ExclusiveStartKey)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ProjectionExpression)}, {_dafny.string_of(self.FilterExpression)}, {_dafny.string_of(self.KeyConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, QueryInput_QueryInput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.Select == __o.Select and self.AttributesToGet == __o.AttributesToGet and self.Limit == __o.Limit and self.ConsistentRead == __o.ConsistentRead and self.KeyConditions == __o.KeyConditions and self.QueryFilter == __o.QueryFilter and self.ConditionalOperator == __o.ConditionalOperator and self.ScanIndexForward == __o.ScanIndexForward and self.ExclusiveStartKey == __o.ExclusiveStartKey and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ProjectionExpression == __o.ProjectionExpression and self.FilterExpression == __o.FilterExpression and self.KeyConditionExpression == __o.KeyConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues
    def __hash__(self) -> int:
        return super().__hash__()


class QueryOutput:
    @classmethod
    def default(cls, ):
        return lambda: QueryOutput_QueryOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_QueryOutput(self) -> bool:
        return isinstance(self, QueryOutput_QueryOutput)

class QueryOutput_QueryOutput(QueryOutput, NamedTuple('QueryOutput', [('Items', Any), ('Count', Any), ('ScannedCount', Any), ('LastEvaluatedKey', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.QueryOutput.QueryOutput({_dafny.string_of(self.Items)}, {_dafny.string_of(self.Count)}, {_dafny.string_of(self.ScannedCount)}, {_dafny.string_of(self.LastEvaluatedKey)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, QueryOutput_QueryOutput) and self.Items == __o.Items and self.Count == __o.Count and self.ScannedCount == __o.ScannedCount and self.LastEvaluatedKey == __o.LastEvaluatedKey and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class Replica:
    @classmethod
    def default(cls, ):
        return lambda: Replica_Replica(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Replica(self) -> bool:
        return isinstance(self, Replica_Replica)

class Replica_Replica(Replica, NamedTuple('Replica', [('RegionName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Replica.Replica({_dafny.string_of(self.RegionName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Replica_Replica) and self.RegionName == __o.RegionName
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaAutoScalingDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaAutoScalingDescription_ReplicaAutoScalingDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaAutoScalingDescription(self) -> bool:
        return isinstance(self, ReplicaAutoScalingDescription_ReplicaAutoScalingDescription)

class ReplicaAutoScalingDescription_ReplicaAutoScalingDescription(ReplicaAutoScalingDescription, NamedTuple('ReplicaAutoScalingDescription', [('RegionName', Any), ('GlobalSecondaryIndexes', Any), ('ReplicaProvisionedReadCapacityAutoScalingSettings', Any), ('ReplicaProvisionedWriteCapacityAutoScalingSettings', Any), ('ReplicaStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaAutoScalingDescription.ReplicaAutoScalingDescription({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityAutoScalingSettings)}, {_dafny.string_of(self.ReplicaProvisionedWriteCapacityAutoScalingSettings)}, {_dafny.string_of(self.ReplicaStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaAutoScalingDescription_ReplicaAutoScalingDescription) and self.RegionName == __o.RegionName and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.ReplicaProvisionedReadCapacityAutoScalingSettings == __o.ReplicaProvisionedReadCapacityAutoScalingSettings and self.ReplicaProvisionedWriteCapacityAutoScalingSettings == __o.ReplicaProvisionedWriteCapacityAutoScalingSettings and self.ReplicaStatus == __o.ReplicaStatus
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaAutoScalingUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaAutoScalingUpdate_ReplicaAutoScalingUpdate(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaAutoScalingUpdate(self) -> bool:
        return isinstance(self, ReplicaAutoScalingUpdate_ReplicaAutoScalingUpdate)

class ReplicaAutoScalingUpdate_ReplicaAutoScalingUpdate(ReplicaAutoScalingUpdate, NamedTuple('ReplicaAutoScalingUpdate', [('RegionName', Any), ('ReplicaGlobalSecondaryIndexUpdates', Any), ('ReplicaProvisionedReadCapacityAutoScalingUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaAutoScalingUpdate.ReplicaAutoScalingUpdate({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.ReplicaGlobalSecondaryIndexUpdates)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityAutoScalingUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaAutoScalingUpdate_ReplicaAutoScalingUpdate) and self.RegionName == __o.RegionName and self.ReplicaGlobalSecondaryIndexUpdates == __o.ReplicaGlobalSecondaryIndexUpdates and self.ReplicaProvisionedReadCapacityAutoScalingUpdate == __o.ReplicaProvisionedReadCapacityAutoScalingUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaAutoScalingUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_29_x_: _dafny.Seq = source__
        return default__.IsValid__ReplicaAutoScalingUpdateList(d_29_x_)

class ReplicaDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaDescription_ReplicaDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaDescription(self) -> bool:
        return isinstance(self, ReplicaDescription_ReplicaDescription)

class ReplicaDescription_ReplicaDescription(ReplicaDescription, NamedTuple('ReplicaDescription', [('RegionName', Any), ('ReplicaStatus', Any), ('ReplicaStatusDescription', Any), ('ReplicaStatusPercentProgress', Any), ('KMSMasterKeyId', Any), ('ProvisionedThroughputOverride', Any), ('GlobalSecondaryIndexes', Any), ('ReplicaInaccessibleDateTime', Any), ('ReplicaTableClassSummary', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaDescription.ReplicaDescription({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.ReplicaStatus)}, {_dafny.string_of(self.ReplicaStatusDescription)}, {_dafny.string_of(self.ReplicaStatusPercentProgress)}, {_dafny.string_of(self.KMSMasterKeyId)}, {_dafny.string_of(self.ProvisionedThroughputOverride)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.ReplicaInaccessibleDateTime)}, {_dafny.string_of(self.ReplicaTableClassSummary)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaDescription_ReplicaDescription) and self.RegionName == __o.RegionName and self.ReplicaStatus == __o.ReplicaStatus and self.ReplicaStatusDescription == __o.ReplicaStatusDescription and self.ReplicaStatusPercentProgress == __o.ReplicaStatusPercentProgress and self.KMSMasterKeyId == __o.KMSMasterKeyId and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.ReplicaInaccessibleDateTime == __o.ReplicaInaccessibleDateTime and self.ReplicaTableClassSummary == __o.ReplicaTableClassSummary
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndex:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndex_ReplicaGlobalSecondaryIndex(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndex(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndex_ReplicaGlobalSecondaryIndex)

class ReplicaGlobalSecondaryIndex_ReplicaGlobalSecondaryIndex(ReplicaGlobalSecondaryIndex, NamedTuple('ReplicaGlobalSecondaryIndex', [('IndexName', Any), ('ProvisionedThroughputOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndex.ReplicaGlobalSecondaryIndex({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedThroughputOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndex_ReplicaGlobalSecondaryIndex) and self.IndexName == __o.IndexName and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexAutoScalingDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndexAutoScalingDescription_ReplicaGlobalSecondaryIndexAutoScalingDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndexAutoScalingDescription(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndexAutoScalingDescription_ReplicaGlobalSecondaryIndexAutoScalingDescription)

class ReplicaGlobalSecondaryIndexAutoScalingDescription_ReplicaGlobalSecondaryIndexAutoScalingDescription(ReplicaGlobalSecondaryIndexAutoScalingDescription, NamedTuple('ReplicaGlobalSecondaryIndexAutoScalingDescription', [('IndexName', Any), ('IndexStatus', Any), ('ProvisionedReadCapacityAutoScalingSettings', Any), ('ProvisionedWriteCapacityAutoScalingSettings', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexAutoScalingDescription.ReplicaGlobalSecondaryIndexAutoScalingDescription({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.IndexStatus)}, {_dafny.string_of(self.ProvisionedReadCapacityAutoScalingSettings)}, {_dafny.string_of(self.ProvisionedWriteCapacityAutoScalingSettings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndexAutoScalingDescription_ReplicaGlobalSecondaryIndexAutoScalingDescription) and self.IndexName == __o.IndexName and self.IndexStatus == __o.IndexStatus and self.ProvisionedReadCapacityAutoScalingSettings == __o.ProvisionedReadCapacityAutoScalingSettings and self.ProvisionedWriteCapacityAutoScalingSettings == __o.ProvisionedWriteCapacityAutoScalingSettings
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexAutoScalingUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndexAutoScalingUpdate_ReplicaGlobalSecondaryIndexAutoScalingUpdate(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndexAutoScalingUpdate(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndexAutoScalingUpdate_ReplicaGlobalSecondaryIndexAutoScalingUpdate)

class ReplicaGlobalSecondaryIndexAutoScalingUpdate_ReplicaGlobalSecondaryIndexAutoScalingUpdate(ReplicaGlobalSecondaryIndexAutoScalingUpdate, NamedTuple('ReplicaGlobalSecondaryIndexAutoScalingUpdate', [('IndexName', Any), ('ProvisionedReadCapacityAutoScalingUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexAutoScalingUpdate.ReplicaGlobalSecondaryIndexAutoScalingUpdate({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedReadCapacityAutoScalingUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndexAutoScalingUpdate_ReplicaGlobalSecondaryIndexAutoScalingUpdate) and self.IndexName == __o.IndexName and self.ProvisionedReadCapacityAutoScalingUpdate == __o.ProvisionedReadCapacityAutoScalingUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndexDescription_ReplicaGlobalSecondaryIndexDescription(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndexDescription(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndexDescription_ReplicaGlobalSecondaryIndexDescription)

class ReplicaGlobalSecondaryIndexDescription_ReplicaGlobalSecondaryIndexDescription(ReplicaGlobalSecondaryIndexDescription, NamedTuple('ReplicaGlobalSecondaryIndexDescription', [('IndexName', Any), ('ProvisionedThroughputOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexDescription.ReplicaGlobalSecondaryIndexDescription({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedThroughputOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndexDescription_ReplicaGlobalSecondaryIndexDescription) and self.IndexName == __o.IndexName and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_30_x_: _dafny.Seq = source__
        return default__.IsValid__ReplicaGlobalSecondaryIndexList(d_30_x_)

class ReplicaGlobalSecondaryIndexSettingsDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndexSettingsDescription_ReplicaGlobalSecondaryIndexSettingsDescription(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndexSettingsDescription(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndexSettingsDescription_ReplicaGlobalSecondaryIndexSettingsDescription)

class ReplicaGlobalSecondaryIndexSettingsDescription_ReplicaGlobalSecondaryIndexSettingsDescription(ReplicaGlobalSecondaryIndexSettingsDescription, NamedTuple('ReplicaGlobalSecondaryIndexSettingsDescription', [('IndexName', Any), ('IndexStatus', Any), ('ProvisionedReadCapacityUnits', Any), ('ProvisionedReadCapacityAutoScalingSettings', Any), ('ProvisionedWriteCapacityUnits', Any), ('ProvisionedWriteCapacityAutoScalingSettings', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexSettingsDescription.ReplicaGlobalSecondaryIndexSettingsDescription({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.IndexStatus)}, {_dafny.string_of(self.ProvisionedReadCapacityUnits)}, {_dafny.string_of(self.ProvisionedReadCapacityAutoScalingSettings)}, {_dafny.string_of(self.ProvisionedWriteCapacityUnits)}, {_dafny.string_of(self.ProvisionedWriteCapacityAutoScalingSettings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndexSettingsDescription_ReplicaGlobalSecondaryIndexSettingsDescription) and self.IndexName == __o.IndexName and self.IndexStatus == __o.IndexStatus and self.ProvisionedReadCapacityUnits == __o.ProvisionedReadCapacityUnits and self.ProvisionedReadCapacityAutoScalingSettings == __o.ProvisionedReadCapacityAutoScalingSettings and self.ProvisionedWriteCapacityUnits == __o.ProvisionedWriteCapacityUnits and self.ProvisionedWriteCapacityAutoScalingSettings == __o.ProvisionedWriteCapacityAutoScalingSettings
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexSettingsUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaGlobalSecondaryIndexSettingsUpdate_ReplicaGlobalSecondaryIndexSettingsUpdate(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaGlobalSecondaryIndexSettingsUpdate(self) -> bool:
        return isinstance(self, ReplicaGlobalSecondaryIndexSettingsUpdate_ReplicaGlobalSecondaryIndexSettingsUpdate)

class ReplicaGlobalSecondaryIndexSettingsUpdate_ReplicaGlobalSecondaryIndexSettingsUpdate(ReplicaGlobalSecondaryIndexSettingsUpdate, NamedTuple('ReplicaGlobalSecondaryIndexSettingsUpdate', [('IndexName', Any), ('ProvisionedReadCapacityUnits', Any), ('ProvisionedReadCapacityAutoScalingSettingsUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexSettingsUpdate.ReplicaGlobalSecondaryIndexSettingsUpdate({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedReadCapacityUnits)}, {_dafny.string_of(self.ProvisionedReadCapacityAutoScalingSettingsUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaGlobalSecondaryIndexSettingsUpdate_ReplicaGlobalSecondaryIndexSettingsUpdate) and self.IndexName == __o.IndexName and self.ProvisionedReadCapacityUnits == __o.ProvisionedReadCapacityUnits and self.ProvisionedReadCapacityAutoScalingSettingsUpdate == __o.ProvisionedReadCapacityAutoScalingSettingsUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaGlobalSecondaryIndexSettingsUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_31_x_: _dafny.Seq = source__
        return default__.IsValid__ReplicaGlobalSecondaryIndexSettingsUpdateList(d_31_x_)

class ReplicaSettingsDescription:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaSettingsDescription_ReplicaSettingsDescription(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaSettingsDescription(self) -> bool:
        return isinstance(self, ReplicaSettingsDescription_ReplicaSettingsDescription)

class ReplicaSettingsDescription_ReplicaSettingsDescription(ReplicaSettingsDescription, NamedTuple('ReplicaSettingsDescription', [('RegionName', Any), ('ReplicaStatus', Any), ('ReplicaBillingModeSummary', Any), ('ReplicaProvisionedReadCapacityUnits', Any), ('ReplicaProvisionedReadCapacityAutoScalingSettings', Any), ('ReplicaProvisionedWriteCapacityUnits', Any), ('ReplicaProvisionedWriteCapacityAutoScalingSettings', Any), ('ReplicaGlobalSecondaryIndexSettings', Any), ('ReplicaTableClassSummary', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaSettingsDescription.ReplicaSettingsDescription({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.ReplicaStatus)}, {_dafny.string_of(self.ReplicaBillingModeSummary)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityUnits)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityAutoScalingSettings)}, {_dafny.string_of(self.ReplicaProvisionedWriteCapacityUnits)}, {_dafny.string_of(self.ReplicaProvisionedWriteCapacityAutoScalingSettings)}, {_dafny.string_of(self.ReplicaGlobalSecondaryIndexSettings)}, {_dafny.string_of(self.ReplicaTableClassSummary)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaSettingsDescription_ReplicaSettingsDescription) and self.RegionName == __o.RegionName and self.ReplicaStatus == __o.ReplicaStatus and self.ReplicaBillingModeSummary == __o.ReplicaBillingModeSummary and self.ReplicaProvisionedReadCapacityUnits == __o.ReplicaProvisionedReadCapacityUnits and self.ReplicaProvisionedReadCapacityAutoScalingSettings == __o.ReplicaProvisionedReadCapacityAutoScalingSettings and self.ReplicaProvisionedWriteCapacityUnits == __o.ReplicaProvisionedWriteCapacityUnits and self.ReplicaProvisionedWriteCapacityAutoScalingSettings == __o.ReplicaProvisionedWriteCapacityAutoScalingSettings and self.ReplicaGlobalSecondaryIndexSettings == __o.ReplicaGlobalSecondaryIndexSettings and self.ReplicaTableClassSummary == __o.ReplicaTableClassSummary
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaSettingsUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaSettingsUpdate_ReplicaSettingsUpdate(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaSettingsUpdate(self) -> bool:
        return isinstance(self, ReplicaSettingsUpdate_ReplicaSettingsUpdate)

class ReplicaSettingsUpdate_ReplicaSettingsUpdate(ReplicaSettingsUpdate, NamedTuple('ReplicaSettingsUpdate', [('RegionName', Any), ('ReplicaProvisionedReadCapacityUnits', Any), ('ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate', Any), ('ReplicaGlobalSecondaryIndexSettingsUpdate', Any), ('ReplicaTableClass', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaSettingsUpdate.ReplicaSettingsUpdate({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityUnits)}, {_dafny.string_of(self.ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate)}, {_dafny.string_of(self.ReplicaGlobalSecondaryIndexSettingsUpdate)}, {_dafny.string_of(self.ReplicaTableClass)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaSettingsUpdate_ReplicaSettingsUpdate) and self.RegionName == __o.RegionName and self.ReplicaProvisionedReadCapacityUnits == __o.ReplicaProvisionedReadCapacityUnits and self.ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate == __o.ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate and self.ReplicaGlobalSecondaryIndexSettingsUpdate == __o.ReplicaGlobalSecondaryIndexSettingsUpdate and self.ReplicaTableClass == __o.ReplicaTableClass
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicaSettingsUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_32_x_: _dafny.Seq = source__
        return default__.IsValid__ReplicaSettingsUpdateList(d_32_x_)

class ReplicaStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ReplicaStatus_CREATING(), ReplicaStatus_CREATION__FAILED(), ReplicaStatus_UPDATING(), ReplicaStatus_DELETING(), ReplicaStatus_ACTIVE(), ReplicaStatus_REGION__DISABLED(), ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS()]
    @classmethod
    def default(cls, ):
        return lambda: ReplicaStatus_CREATING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CREATING(self) -> bool:
        return isinstance(self, ReplicaStatus_CREATING)
    @property
    def is_CREATION__FAILED(self) -> bool:
        return isinstance(self, ReplicaStatus_CREATION__FAILED)
    @property
    def is_UPDATING(self) -> bool:
        return isinstance(self, ReplicaStatus_UPDATING)
    @property
    def is_DELETING(self) -> bool:
        return isinstance(self, ReplicaStatus_DELETING)
    @property
    def is_ACTIVE(self) -> bool:
        return isinstance(self, ReplicaStatus_ACTIVE)
    @property
    def is_REGION__DISABLED(self) -> bool:
        return isinstance(self, ReplicaStatus_REGION__DISABLED)
    @property
    def is_INACCESSIBLE__ENCRYPTION__CREDENTIALS(self) -> bool:
        return isinstance(self, ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)

class ReplicaStatus_CREATING(ReplicaStatus, NamedTuple('CREATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.CREATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_CREATING)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_CREATION__FAILED(ReplicaStatus, NamedTuple('CREATION__FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.CREATION_FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_CREATION__FAILED)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_UPDATING(ReplicaStatus, NamedTuple('UPDATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.UPDATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_UPDATING)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_DELETING(ReplicaStatus, NamedTuple('DELETING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.DELETING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_DELETING)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_ACTIVE(ReplicaStatus, NamedTuple('ACTIVE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.ACTIVE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_ACTIVE)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_REGION__DISABLED(ReplicaStatus, NamedTuple('REGION__DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.REGION_DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_REGION__DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS(ReplicaStatus, NamedTuple('INACCESSIBLE__ENCRYPTION__CREDENTIALS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaStatus.INACCESSIBLE_ENCRYPTION_CREDENTIALS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicationGroupUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicationGroupUpdate_ReplicationGroupUpdate(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicationGroupUpdate(self) -> bool:
        return isinstance(self, ReplicationGroupUpdate_ReplicationGroupUpdate)

class ReplicationGroupUpdate_ReplicationGroupUpdate(ReplicationGroupUpdate, NamedTuple('ReplicationGroupUpdate', [('Create', Any), ('Update', Any), ('Delete', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicationGroupUpdate.ReplicationGroupUpdate({_dafny.string_of(self.Create)}, {_dafny.string_of(self.Update)}, {_dafny.string_of(self.Delete)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicationGroupUpdate_ReplicationGroupUpdate) and self.Create == __o.Create and self.Update == __o.Update and self.Delete == __o.Delete
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicationGroupUpdateList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_33_x_: _dafny.Seq = source__
        return default__.IsValid__ReplicationGroupUpdateList(d_33_x_)

class ReplicaUpdate:
    @classmethod
    def default(cls, ):
        return lambda: ReplicaUpdate_ReplicaUpdate(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicaUpdate(self) -> bool:
        return isinstance(self, ReplicaUpdate_ReplicaUpdate)

class ReplicaUpdate_ReplicaUpdate(ReplicaUpdate, NamedTuple('ReplicaUpdate', [('Create', Any), ('Delete', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReplicaUpdate.ReplicaUpdate({_dafny.string_of(self.Create)}, {_dafny.string_of(self.Delete)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicaUpdate_ReplicaUpdate) and self.Create == __o.Create and self.Delete == __o.Delete
    def __hash__(self) -> int:
        return super().__hash__()


class ResourceArnString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_34_x_: _dafny.Seq = source__
        return default__.IsValid__ResourceArnString(d_34_x_)

class RestoreSummary:
    @classmethod
    def default(cls, ):
        return lambda: RestoreSummary_RestoreSummary(Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""), False)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RestoreSummary(self) -> bool:
        return isinstance(self, RestoreSummary_RestoreSummary)

class RestoreSummary_RestoreSummary(RestoreSummary, NamedTuple('RestoreSummary', [('SourceBackupArn', Any), ('SourceTableArn', Any), ('RestoreDateTime', Any), ('RestoreInProgress', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.RestoreSummary.RestoreSummary({_dafny.string_of(self.SourceBackupArn)}, {_dafny.string_of(self.SourceTableArn)}, {_dafny.string_of(self.RestoreDateTime)}, {_dafny.string_of(self.RestoreInProgress)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RestoreSummary_RestoreSummary) and self.SourceBackupArn == __o.SourceBackupArn and self.SourceTableArn == __o.SourceTableArn and self.RestoreDateTime == __o.RestoreDateTime and self.RestoreInProgress == __o.RestoreInProgress
    def __hash__(self) -> int:
        return super().__hash__()


class RestoreTableFromBackupInput:
    @classmethod
    def default(cls, ):
        return lambda: RestoreTableFromBackupInput_RestoreTableFromBackupInput(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RestoreTableFromBackupInput(self) -> bool:
        return isinstance(self, RestoreTableFromBackupInput_RestoreTableFromBackupInput)

class RestoreTableFromBackupInput_RestoreTableFromBackupInput(RestoreTableFromBackupInput, NamedTuple('RestoreTableFromBackupInput', [('TargetTableName', Any), ('BackupArn', Any), ('BillingModeOverride', Any), ('GlobalSecondaryIndexOverride', Any), ('LocalSecondaryIndexOverride', Any), ('ProvisionedThroughputOverride', Any), ('SSESpecificationOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.RestoreTableFromBackupInput.RestoreTableFromBackupInput({_dafny.string_of(self.TargetTableName)}, {_dafny.string_of(self.BackupArn)}, {_dafny.string_of(self.BillingModeOverride)}, {_dafny.string_of(self.GlobalSecondaryIndexOverride)}, {_dafny.string_of(self.LocalSecondaryIndexOverride)}, {_dafny.string_of(self.ProvisionedThroughputOverride)}, {_dafny.string_of(self.SSESpecificationOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RestoreTableFromBackupInput_RestoreTableFromBackupInput) and self.TargetTableName == __o.TargetTableName and self.BackupArn == __o.BackupArn and self.BillingModeOverride == __o.BillingModeOverride and self.GlobalSecondaryIndexOverride == __o.GlobalSecondaryIndexOverride and self.LocalSecondaryIndexOverride == __o.LocalSecondaryIndexOverride and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride and self.SSESpecificationOverride == __o.SSESpecificationOverride
    def __hash__(self) -> int:
        return super().__hash__()


class RestoreTableFromBackupOutput:
    @classmethod
    def default(cls, ):
        return lambda: RestoreTableFromBackupOutput_RestoreTableFromBackupOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RestoreTableFromBackupOutput(self) -> bool:
        return isinstance(self, RestoreTableFromBackupOutput_RestoreTableFromBackupOutput)

class RestoreTableFromBackupOutput_RestoreTableFromBackupOutput(RestoreTableFromBackupOutput, NamedTuple('RestoreTableFromBackupOutput', [('TableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.RestoreTableFromBackupOutput.RestoreTableFromBackupOutput({_dafny.string_of(self.TableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RestoreTableFromBackupOutput_RestoreTableFromBackupOutput) and self.TableDescription == __o.TableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class RestoreTableToPointInTimeInput:
    @classmethod
    def default(cls, ):
        return lambda: RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput(Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RestoreTableToPointInTimeInput(self) -> bool:
        return isinstance(self, RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput)

class RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput(RestoreTableToPointInTimeInput, NamedTuple('RestoreTableToPointInTimeInput', [('SourceTableArn', Any), ('SourceTableName', Any), ('TargetTableName', Any), ('UseLatestRestorableTime', Any), ('RestoreDateTime', Any), ('BillingModeOverride', Any), ('GlobalSecondaryIndexOverride', Any), ('LocalSecondaryIndexOverride', Any), ('ProvisionedThroughputOverride', Any), ('SSESpecificationOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.RestoreTableToPointInTimeInput.RestoreTableToPointInTimeInput({_dafny.string_of(self.SourceTableArn)}, {_dafny.string_of(self.SourceTableName)}, {_dafny.string_of(self.TargetTableName)}, {_dafny.string_of(self.UseLatestRestorableTime)}, {_dafny.string_of(self.RestoreDateTime)}, {_dafny.string_of(self.BillingModeOverride)}, {_dafny.string_of(self.GlobalSecondaryIndexOverride)}, {_dafny.string_of(self.LocalSecondaryIndexOverride)}, {_dafny.string_of(self.ProvisionedThroughputOverride)}, {_dafny.string_of(self.SSESpecificationOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput) and self.SourceTableArn == __o.SourceTableArn and self.SourceTableName == __o.SourceTableName and self.TargetTableName == __o.TargetTableName and self.UseLatestRestorableTime == __o.UseLatestRestorableTime and self.RestoreDateTime == __o.RestoreDateTime and self.BillingModeOverride == __o.BillingModeOverride and self.GlobalSecondaryIndexOverride == __o.GlobalSecondaryIndexOverride and self.LocalSecondaryIndexOverride == __o.LocalSecondaryIndexOverride and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride and self.SSESpecificationOverride == __o.SSESpecificationOverride
    def __hash__(self) -> int:
        return super().__hash__()


class RestoreTableToPointInTimeOutput:
    @classmethod
    def default(cls, ):
        return lambda: RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RestoreTableToPointInTimeOutput(self) -> bool:
        return isinstance(self, RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput)

class RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput(RestoreTableToPointInTimeOutput, NamedTuple('RestoreTableToPointInTimeOutput', [('TableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.RestoreTableToPointInTimeOutput.RestoreTableToPointInTimeOutput({_dafny.string_of(self.TableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput) and self.TableDescription == __o.TableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class ReturnConsumedCapacity:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ReturnConsumedCapacity_INDEXES(), ReturnConsumedCapacity_TOTAL(), ReturnConsumedCapacity_NONE()]
    @classmethod
    def default(cls, ):
        return lambda: ReturnConsumedCapacity_INDEXES()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_INDEXES(self) -> bool:
        return isinstance(self, ReturnConsumedCapacity_INDEXES)
    @property
    def is_TOTAL(self) -> bool:
        return isinstance(self, ReturnConsumedCapacity_TOTAL)
    @property
    def is_NONE(self) -> bool:
        return isinstance(self, ReturnConsumedCapacity_NONE)

class ReturnConsumedCapacity_INDEXES(ReturnConsumedCapacity, NamedTuple('INDEXES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.INDEXES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnConsumedCapacity_INDEXES)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnConsumedCapacity_TOTAL(ReturnConsumedCapacity, NamedTuple('TOTAL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.TOTAL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnConsumedCapacity_TOTAL)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnConsumedCapacity_NONE(ReturnConsumedCapacity, NamedTuple('NONE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnConsumedCapacity.NONE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnConsumedCapacity_NONE)
    def __hash__(self) -> int:
        return super().__hash__()


class ReturnItemCollectionMetrics:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ReturnItemCollectionMetrics_SIZE(), ReturnItemCollectionMetrics_NONE()]
    @classmethod
    def default(cls, ):
        return lambda: ReturnItemCollectionMetrics_SIZE()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SIZE(self) -> bool:
        return isinstance(self, ReturnItemCollectionMetrics_SIZE)
    @property
    def is_NONE(self) -> bool:
        return isinstance(self, ReturnItemCollectionMetrics_NONE)

class ReturnItemCollectionMetrics_SIZE(ReturnItemCollectionMetrics, NamedTuple('SIZE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnItemCollectionMetrics.SIZE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnItemCollectionMetrics_SIZE)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnItemCollectionMetrics_NONE(ReturnItemCollectionMetrics, NamedTuple('NONE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnItemCollectionMetrics.NONE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnItemCollectionMetrics_NONE)
    def __hash__(self) -> int:
        return super().__hash__()


class ReturnValue:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ReturnValue_NONE(), ReturnValue_ALL__OLD(), ReturnValue_UPDATED__OLD(), ReturnValue_ALL__NEW(), ReturnValue_UPDATED__NEW()]
    @classmethod
    def default(cls, ):
        return lambda: ReturnValue_NONE()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NONE(self) -> bool:
        return isinstance(self, ReturnValue_NONE)
    @property
    def is_ALL__OLD(self) -> bool:
        return isinstance(self, ReturnValue_ALL__OLD)
    @property
    def is_UPDATED__OLD(self) -> bool:
        return isinstance(self, ReturnValue_UPDATED__OLD)
    @property
    def is_ALL__NEW(self) -> bool:
        return isinstance(self, ReturnValue_ALL__NEW)
    @property
    def is_UPDATED__NEW(self) -> bool:
        return isinstance(self, ReturnValue_UPDATED__NEW)

class ReturnValue_NONE(ReturnValue, NamedTuple('NONE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValue.NONE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValue_NONE)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnValue_ALL__OLD(ReturnValue, NamedTuple('ALL__OLD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValue.ALL_OLD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValue_ALL__OLD)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnValue_UPDATED__OLD(ReturnValue, NamedTuple('UPDATED__OLD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValue.UPDATED_OLD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValue_UPDATED__OLD)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnValue_ALL__NEW(ReturnValue, NamedTuple('ALL__NEW', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValue.ALL_NEW'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValue_ALL__NEW)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnValue_UPDATED__NEW(ReturnValue, NamedTuple('UPDATED__NEW', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValue.UPDATED_NEW'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValue_UPDATED__NEW)
    def __hash__(self) -> int:
        return super().__hash__()


class ReturnValuesOnConditionCheckFailure:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ReturnValuesOnConditionCheckFailure_ALL__OLD(), ReturnValuesOnConditionCheckFailure_NONE()]
    @classmethod
    def default(cls, ):
        return lambda: ReturnValuesOnConditionCheckFailure_ALL__OLD()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALL__OLD(self) -> bool:
        return isinstance(self, ReturnValuesOnConditionCheckFailure_ALL__OLD)
    @property
    def is_NONE(self) -> bool:
        return isinstance(self, ReturnValuesOnConditionCheckFailure_NONE)

class ReturnValuesOnConditionCheckFailure_ALL__OLD(ReturnValuesOnConditionCheckFailure, NamedTuple('ALL__OLD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValuesOnConditionCheckFailure.ALL_OLD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValuesOnConditionCheckFailure_ALL__OLD)
    def __hash__(self) -> int:
        return super().__hash__()

class ReturnValuesOnConditionCheckFailure_NONE(ReturnValuesOnConditionCheckFailure, NamedTuple('NONE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ReturnValuesOnConditionCheckFailure.NONE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReturnValuesOnConditionCheckFailure_NONE)
    def __hash__(self) -> int:
        return super().__hash__()


class S3Bucket:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_35_x_: _dafny.Seq = source__
        return default__.IsValid__S3Bucket(d_35_x_)

class S3BucketSource:
    @classmethod
    def default(cls, ):
        return lambda: S3BucketSource_S3BucketSource(Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_S3BucketSource(self) -> bool:
        return isinstance(self, S3BucketSource_S3BucketSource)

class S3BucketSource_S3BucketSource(S3BucketSource, NamedTuple('S3BucketSource', [('S3BucketOwner', Any), ('S3Bucket', Any), ('S3KeyPrefix', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.S3BucketSource.S3BucketSource({_dafny.string_of(self.S3BucketOwner)}, {_dafny.string_of(self.S3Bucket)}, {_dafny.string_of(self.S3KeyPrefix)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, S3BucketSource_S3BucketSource) and self.S3BucketOwner == __o.S3BucketOwner and self.S3Bucket == __o.S3Bucket and self.S3KeyPrefix == __o.S3KeyPrefix
    def __hash__(self) -> int:
        return super().__hash__()


class S3Prefix:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_36_x_: _dafny.Seq = source__
        return default__.IsValid__S3Prefix(d_36_x_)

class S3SseAlgorithm:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [S3SseAlgorithm_AES256(), S3SseAlgorithm_KMS()]
    @classmethod
    def default(cls, ):
        return lambda: S3SseAlgorithm_AES256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES256(self) -> bool:
        return isinstance(self, S3SseAlgorithm_AES256)
    @property
    def is_KMS(self) -> bool:
        return isinstance(self, S3SseAlgorithm_KMS)

class S3SseAlgorithm_AES256(S3SseAlgorithm, NamedTuple('AES256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.S3SseAlgorithm.AES256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, S3SseAlgorithm_AES256)
    def __hash__(self) -> int:
        return super().__hash__()

class S3SseAlgorithm_KMS(S3SseAlgorithm, NamedTuple('KMS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.S3SseAlgorithm.KMS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, S3SseAlgorithm_KMS)
    def __hash__(self) -> int:
        return super().__hash__()


class S3SseKmsKeyId:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_37_x_: _dafny.Seq = source__
        return default__.IsValid__S3SseKmsKeyId(d_37_x_)

class ScalarAttributeType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ScalarAttributeType_S(), ScalarAttributeType_N(), ScalarAttributeType_B()]
    @classmethod
    def default(cls, ):
        return lambda: ScalarAttributeType_S()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_S(self) -> bool:
        return isinstance(self, ScalarAttributeType_S)
    @property
    def is_N(self) -> bool:
        return isinstance(self, ScalarAttributeType_N)
    @property
    def is_B(self) -> bool:
        return isinstance(self, ScalarAttributeType_B)

class ScalarAttributeType_S(ScalarAttributeType, NamedTuple('S', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ScalarAttributeType.S'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScalarAttributeType_S)
    def __hash__(self) -> int:
        return super().__hash__()

class ScalarAttributeType_N(ScalarAttributeType, NamedTuple('N', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ScalarAttributeType.N'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScalarAttributeType_N)
    def __hash__(self) -> int:
        return super().__hash__()

class ScalarAttributeType_B(ScalarAttributeType, NamedTuple('B', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ScalarAttributeType.B'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScalarAttributeType_B)
    def __hash__(self) -> int:
        return super().__hash__()


class ScanInput:
    @classmethod
    def default(cls, ):
        return lambda: ScanInput_ScanInput(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ScanInput(self) -> bool:
        return isinstance(self, ScanInput_ScanInput)

class ScanInput_ScanInput(ScanInput, NamedTuple('ScanInput', [('TableName', Any), ('IndexName', Any), ('AttributesToGet', Any), ('Limit', Any), ('Select', Any), ('ScanFilter', Any), ('ConditionalOperator', Any), ('ExclusiveStartKey', Any), ('ReturnConsumedCapacity', Any), ('TotalSegments', Any), ('Segment', Any), ('ProjectionExpression', Any), ('FilterExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any), ('ConsistentRead', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ScanInput.ScanInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.AttributesToGet)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Select)}, {_dafny.string_of(self.ScanFilter)}, {_dafny.string_of(self.ConditionalOperator)}, {_dafny.string_of(self.ExclusiveStartKey)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.TotalSegments)}, {_dafny.string_of(self.Segment)}, {_dafny.string_of(self.ProjectionExpression)}, {_dafny.string_of(self.FilterExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)}, {_dafny.string_of(self.ConsistentRead)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScanInput_ScanInput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.AttributesToGet == __o.AttributesToGet and self.Limit == __o.Limit and self.Select == __o.Select and self.ScanFilter == __o.ScanFilter and self.ConditionalOperator == __o.ConditionalOperator and self.ExclusiveStartKey == __o.ExclusiveStartKey and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.TotalSegments == __o.TotalSegments and self.Segment == __o.Segment and self.ProjectionExpression == __o.ProjectionExpression and self.FilterExpression == __o.FilterExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues and self.ConsistentRead == __o.ConsistentRead
    def __hash__(self) -> int:
        return super().__hash__()


class ScanOutput:
    @classmethod
    def default(cls, ):
        return lambda: ScanOutput_ScanOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ScanOutput(self) -> bool:
        return isinstance(self, ScanOutput_ScanOutput)

class ScanOutput_ScanOutput(ScanOutput, NamedTuple('ScanOutput', [('Items', Any), ('Count', Any), ('ScannedCount', Any), ('LastEvaluatedKey', Any), ('ConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.ScanOutput.ScanOutput({_dafny.string_of(self.Items)}, {_dafny.string_of(self.Count)}, {_dafny.string_of(self.ScannedCount)}, {_dafny.string_of(self.LastEvaluatedKey)}, {_dafny.string_of(self.ConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScanOutput_ScanOutput) and self.Items == __o.Items and self.Count == __o.Count and self.ScannedCount == __o.ScannedCount and self.LastEvaluatedKey == __o.LastEvaluatedKey and self.ConsumedCapacity == __o.ConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class ScanSegment:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_38_x_: int = source__
        if True:
            return default__.IsValid__ScanSegment(d_38_x_)
        return False

class ScanTotalSegments:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_39_x_: int = source__
        if True:
            return default__.IsValid__ScanTotalSegments(d_39_x_)
        return False

class Select:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [Select_ALL__ATTRIBUTES(), Select_ALL__PROJECTED__ATTRIBUTES(), Select_SPECIFIC__ATTRIBUTES(), Select_COUNT()]
    @classmethod
    def default(cls, ):
        return lambda: Select_ALL__ATTRIBUTES()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALL__ATTRIBUTES(self) -> bool:
        return isinstance(self, Select_ALL__ATTRIBUTES)
    @property
    def is_ALL__PROJECTED__ATTRIBUTES(self) -> bool:
        return isinstance(self, Select_ALL__PROJECTED__ATTRIBUTES)
    @property
    def is_SPECIFIC__ATTRIBUTES(self) -> bool:
        return isinstance(self, Select_SPECIFIC__ATTRIBUTES)
    @property
    def is_COUNT(self) -> bool:
        return isinstance(self, Select_COUNT)

class Select_ALL__ATTRIBUTES(Select, NamedTuple('ALL__ATTRIBUTES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Select.ALL_ATTRIBUTES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Select_ALL__ATTRIBUTES)
    def __hash__(self) -> int:
        return super().__hash__()

class Select_ALL__PROJECTED__ATTRIBUTES(Select, NamedTuple('ALL__PROJECTED__ATTRIBUTES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Select.ALL_PROJECTED_ATTRIBUTES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Select_ALL__PROJECTED__ATTRIBUTES)
    def __hash__(self) -> int:
        return super().__hash__()

class Select_SPECIFIC__ATTRIBUTES(Select, NamedTuple('SPECIFIC__ATTRIBUTES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Select.SPECIFIC_ATTRIBUTES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Select_SPECIFIC__ATTRIBUTES)
    def __hash__(self) -> int:
        return super().__hash__()

class Select_COUNT(Select, NamedTuple('COUNT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Select.COUNT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Select_COUNT)
    def __hash__(self) -> int:
        return super().__hash__()


class SourceTableDetails:
    @classmethod
    def default(cls, ):
        return lambda: SourceTableDetails_SourceTableDetails(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq({}), _dafny.Seq(""), ProvisionedThroughput.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SourceTableDetails(self) -> bool:
        return isinstance(self, SourceTableDetails_SourceTableDetails)

class SourceTableDetails_SourceTableDetails(SourceTableDetails, NamedTuple('SourceTableDetails', [('TableName', Any), ('TableId', Any), ('TableArn', Any), ('TableSizeBytes', Any), ('KeySchema', Any), ('TableCreationDateTime', Any), ('ProvisionedThroughput', Any), ('ItemCount', Any), ('BillingMode', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SourceTableDetails.SourceTableDetails({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.TableId)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.TableSizeBytes)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.TableCreationDateTime)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.ItemCount)}, {_dafny.string_of(self.BillingMode)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SourceTableDetails_SourceTableDetails) and self.TableName == __o.TableName and self.TableId == __o.TableId and self.TableArn == __o.TableArn and self.TableSizeBytes == __o.TableSizeBytes and self.KeySchema == __o.KeySchema and self.TableCreationDateTime == __o.TableCreationDateTime and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.ItemCount == __o.ItemCount and self.BillingMode == __o.BillingMode
    def __hash__(self) -> int:
        return super().__hash__()


class SourceTableFeatureDetails:
    @classmethod
    def default(cls, ):
        return lambda: SourceTableFeatureDetails_SourceTableFeatureDetails(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SourceTableFeatureDetails(self) -> bool:
        return isinstance(self, SourceTableFeatureDetails_SourceTableFeatureDetails)

class SourceTableFeatureDetails_SourceTableFeatureDetails(SourceTableFeatureDetails, NamedTuple('SourceTableFeatureDetails', [('LocalSecondaryIndexes', Any), ('GlobalSecondaryIndexes', Any), ('StreamDescription', Any), ('TimeToLiveDescription', Any), ('SSEDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SourceTableFeatureDetails.SourceTableFeatureDetails({_dafny.string_of(self.LocalSecondaryIndexes)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.StreamDescription)}, {_dafny.string_of(self.TimeToLiveDescription)}, {_dafny.string_of(self.SSEDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SourceTableFeatureDetails_SourceTableFeatureDetails) and self.LocalSecondaryIndexes == __o.LocalSecondaryIndexes and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.StreamDescription == __o.StreamDescription and self.TimeToLiveDescription == __o.TimeToLiveDescription and self.SSEDescription == __o.SSEDescription
    def __hash__(self) -> int:
        return super().__hash__()


class SSEDescription:
    @classmethod
    def default(cls, ):
        return lambda: SSEDescription_SSEDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SSEDescription(self) -> bool:
        return isinstance(self, SSEDescription_SSEDescription)

class SSEDescription_SSEDescription(SSEDescription, NamedTuple('SSEDescription', [('Status', Any), ('SSEType', Any), ('KMSMasterKeyArn', Any), ('InaccessibleEncryptionDateTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEDescription.SSEDescription({_dafny.string_of(self.Status)}, {_dafny.string_of(self.SSEType)}, {_dafny.string_of(self.KMSMasterKeyArn)}, {_dafny.string_of(self.InaccessibleEncryptionDateTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEDescription_SSEDescription) and self.Status == __o.Status and self.SSEType == __o.SSEType and self.KMSMasterKeyArn == __o.KMSMasterKeyArn and self.InaccessibleEncryptionDateTime == __o.InaccessibleEncryptionDateTime
    def __hash__(self) -> int:
        return super().__hash__()


class SSESpecification:
    @classmethod
    def default(cls, ):
        return lambda: SSESpecification_SSESpecification(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SSESpecification(self) -> bool:
        return isinstance(self, SSESpecification_SSESpecification)

class SSESpecification_SSESpecification(SSESpecification, NamedTuple('SSESpecification', [('Enabled', Any), ('SSEType', Any), ('KMSMasterKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSESpecification.SSESpecification({_dafny.string_of(self.Enabled)}, {_dafny.string_of(self.SSEType)}, {_dafny.string_of(self.KMSMasterKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSESpecification_SSESpecification) and self.Enabled == __o.Enabled and self.SSEType == __o.SSEType and self.KMSMasterKeyId == __o.KMSMasterKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class SSEStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [SSEStatus_ENABLING(), SSEStatus_ENABLED(), SSEStatus_DISABLING(), SSEStatus_DISABLED(), SSEStatus_UPDATING()]
    @classmethod
    def default(cls, ):
        return lambda: SSEStatus_ENABLING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLING(self) -> bool:
        return isinstance(self, SSEStatus_ENABLING)
    @property
    def is_ENABLED(self) -> bool:
        return isinstance(self, SSEStatus_ENABLED)
    @property
    def is_DISABLING(self) -> bool:
        return isinstance(self, SSEStatus_DISABLING)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, SSEStatus_DISABLED)
    @property
    def is_UPDATING(self) -> bool:
        return isinstance(self, SSEStatus_UPDATING)

class SSEStatus_ENABLING(SSEStatus, NamedTuple('ENABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEStatus.ENABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEStatus_ENABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class SSEStatus_ENABLED(SSEStatus, NamedTuple('ENABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEStatus.ENABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEStatus_ENABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class SSEStatus_DISABLING(SSEStatus, NamedTuple('DISABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEStatus.DISABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEStatus_DISABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class SSEStatus_DISABLED(SSEStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class SSEStatus_UPDATING(SSEStatus, NamedTuple('UPDATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEStatus.UPDATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEStatus_UPDATING)
    def __hash__(self) -> int:
        return super().__hash__()


class SSEType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [SSEType_AES256(), SSEType_KMS()]
    @classmethod
    def default(cls, ):
        return lambda: SSEType_AES256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES256(self) -> bool:
        return isinstance(self, SSEType_AES256)
    @property
    def is_KMS(self) -> bool:
        return isinstance(self, SSEType_KMS)

class SSEType_AES256(SSEType, NamedTuple('AES256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEType.AES256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEType_AES256)
    def __hash__(self) -> int:
        return super().__hash__()

class SSEType_KMS(SSEType, NamedTuple('KMS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.SSEType.KMS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SSEType_KMS)
    def __hash__(self) -> int:
        return super().__hash__()


class StreamArn:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_40_x_: _dafny.Seq = source__
        return default__.IsValid__StreamArn(d_40_x_)

class StreamSpecification:
    @classmethod
    def default(cls, ):
        return lambda: StreamSpecification_StreamSpecification(False, Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StreamSpecification(self) -> bool:
        return isinstance(self, StreamSpecification_StreamSpecification)

class StreamSpecification_StreamSpecification(StreamSpecification, NamedTuple('StreamSpecification', [('StreamEnabled', Any), ('StreamViewType', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.StreamSpecification.StreamSpecification({_dafny.string_of(self.StreamEnabled)}, {_dafny.string_of(self.StreamViewType)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StreamSpecification_StreamSpecification) and self.StreamEnabled == __o.StreamEnabled and self.StreamViewType == __o.StreamViewType
    def __hash__(self) -> int:
        return super().__hash__()


class StreamViewType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [StreamViewType_NEW__IMAGE(), StreamViewType_OLD__IMAGE(), StreamViewType_NEW__AND__OLD__IMAGES(), StreamViewType_KEYS__ONLY()]
    @classmethod
    def default(cls, ):
        return lambda: StreamViewType_NEW__IMAGE()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NEW__IMAGE(self) -> bool:
        return isinstance(self, StreamViewType_NEW__IMAGE)
    @property
    def is_OLD__IMAGE(self) -> bool:
        return isinstance(self, StreamViewType_OLD__IMAGE)
    @property
    def is_NEW__AND__OLD__IMAGES(self) -> bool:
        return isinstance(self, StreamViewType_NEW__AND__OLD__IMAGES)
    @property
    def is_KEYS__ONLY(self) -> bool:
        return isinstance(self, StreamViewType_KEYS__ONLY)

class StreamViewType_NEW__IMAGE(StreamViewType, NamedTuple('NEW__IMAGE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.StreamViewType.NEW_IMAGE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StreamViewType_NEW__IMAGE)
    def __hash__(self) -> int:
        return super().__hash__()

class StreamViewType_OLD__IMAGE(StreamViewType, NamedTuple('OLD__IMAGE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.StreamViewType.OLD_IMAGE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StreamViewType_OLD__IMAGE)
    def __hash__(self) -> int:
        return super().__hash__()

class StreamViewType_NEW__AND__OLD__IMAGES(StreamViewType, NamedTuple('NEW__AND__OLD__IMAGES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.StreamViewType.NEW_AND_OLD_IMAGES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StreamViewType_NEW__AND__OLD__IMAGES)
    def __hash__(self) -> int:
        return super().__hash__()

class StreamViewType_KEYS__ONLY(StreamViewType, NamedTuple('KEYS__ONLY', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.StreamViewType.KEYS_ONLY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StreamViewType_KEYS__ONLY)
    def __hash__(self) -> int:
        return super().__hash__()


class TableAutoScalingDescription:
    @classmethod
    def default(cls, ):
        return lambda: TableAutoScalingDescription_TableAutoScalingDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TableAutoScalingDescription(self) -> bool:
        return isinstance(self, TableAutoScalingDescription_TableAutoScalingDescription)

class TableAutoScalingDescription_TableAutoScalingDescription(TableAutoScalingDescription, NamedTuple('TableAutoScalingDescription', [('TableName', Any), ('TableStatus', Any), ('Replicas', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableAutoScalingDescription.TableAutoScalingDescription({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.TableStatus)}, {_dafny.string_of(self.Replicas)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableAutoScalingDescription_TableAutoScalingDescription) and self.TableName == __o.TableName and self.TableStatus == __o.TableStatus and self.Replicas == __o.Replicas
    def __hash__(self) -> int:
        return super().__hash__()


class TableClass:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [TableClass_STANDARD(), TableClass_STANDARD__INFREQUENT__ACCESS()]
    @classmethod
    def default(cls, ):
        return lambda: TableClass_STANDARD()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_STANDARD(self) -> bool:
        return isinstance(self, TableClass_STANDARD)
    @property
    def is_STANDARD__INFREQUENT__ACCESS(self) -> bool:
        return isinstance(self, TableClass_STANDARD__INFREQUENT__ACCESS)

class TableClass_STANDARD(TableClass, NamedTuple('STANDARD', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableClass.STANDARD'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableClass_STANDARD)
    def __hash__(self) -> int:
        return super().__hash__()

class TableClass_STANDARD__INFREQUENT__ACCESS(TableClass, NamedTuple('STANDARD__INFREQUENT__ACCESS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableClass.STANDARD_INFREQUENT_ACCESS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableClass_STANDARD__INFREQUENT__ACCESS)
    def __hash__(self) -> int:
        return super().__hash__()


class TableClassSummary:
    @classmethod
    def default(cls, ):
        return lambda: TableClassSummary_TableClassSummary(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TableClassSummary(self) -> bool:
        return isinstance(self, TableClassSummary_TableClassSummary)

class TableClassSummary_TableClassSummary(TableClassSummary, NamedTuple('TableClassSummary', [('TableClass', Any), ('LastUpdateDateTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableClassSummary.TableClassSummary({_dafny.string_of(self.TableClass)}, {_dafny.string_of(self.LastUpdateDateTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableClassSummary_TableClassSummary) and self.TableClass == __o.TableClass and self.LastUpdateDateTime == __o.LastUpdateDateTime
    def __hash__(self) -> int:
        return super().__hash__()


class TableCreationParameters:
    @classmethod
    def default(cls, ):
        return lambda: TableCreationParameters_TableCreationParameters(_dafny.Seq(""), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TableCreationParameters(self) -> bool:
        return isinstance(self, TableCreationParameters_TableCreationParameters)

class TableCreationParameters_TableCreationParameters(TableCreationParameters, NamedTuple('TableCreationParameters', [('TableName', Any), ('AttributeDefinitions', Any), ('KeySchema', Any), ('BillingMode', Any), ('ProvisionedThroughput', Any), ('SSESpecification', Any), ('GlobalSecondaryIndexes', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableCreationParameters.TableCreationParameters({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.AttributeDefinitions)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.BillingMode)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.SSESpecification)}, {_dafny.string_of(self.GlobalSecondaryIndexes)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableCreationParameters_TableCreationParameters) and self.TableName == __o.TableName and self.AttributeDefinitions == __o.AttributeDefinitions and self.KeySchema == __o.KeySchema and self.BillingMode == __o.BillingMode and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.SSESpecification == __o.SSESpecification and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes
    def __hash__(self) -> int:
        return super().__hash__()


class TableDescription:
    @classmethod
    def default(cls, ):
        return lambda: TableDescription_TableDescription(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TableDescription(self) -> bool:
        return isinstance(self, TableDescription_TableDescription)

class TableDescription_TableDescription(TableDescription, NamedTuple('TableDescription', [('AttributeDefinitions', Any), ('TableName', Any), ('KeySchema', Any), ('TableStatus', Any), ('CreationDateTime', Any), ('ProvisionedThroughput', Any), ('TableSizeBytes', Any), ('ItemCount', Any), ('TableArn', Any), ('TableId', Any), ('BillingModeSummary', Any), ('LocalSecondaryIndexes', Any), ('GlobalSecondaryIndexes', Any), ('StreamSpecification', Any), ('LatestStreamLabel', Any), ('LatestStreamArn', Any), ('GlobalTableVersion', Any), ('Replicas', Any), ('RestoreSummary', Any), ('SSEDescription', Any), ('ArchivalSummary', Any), ('TableClassSummary', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableDescription.TableDescription({_dafny.string_of(self.AttributeDefinitions)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.KeySchema)}, {_dafny.string_of(self.TableStatus)}, {_dafny.string_of(self.CreationDateTime)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.TableSizeBytes)}, {_dafny.string_of(self.ItemCount)}, {_dafny.string_of(self.TableArn)}, {_dafny.string_of(self.TableId)}, {_dafny.string_of(self.BillingModeSummary)}, {_dafny.string_of(self.LocalSecondaryIndexes)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.StreamSpecification)}, {_dafny.string_of(self.LatestStreamLabel)}, {_dafny.string_of(self.LatestStreamArn)}, {_dafny.string_of(self.GlobalTableVersion)}, {_dafny.string_of(self.Replicas)}, {_dafny.string_of(self.RestoreSummary)}, {_dafny.string_of(self.SSEDescription)}, {_dafny.string_of(self.ArchivalSummary)}, {_dafny.string_of(self.TableClassSummary)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableDescription_TableDescription) and self.AttributeDefinitions == __o.AttributeDefinitions and self.TableName == __o.TableName and self.KeySchema == __o.KeySchema and self.TableStatus == __o.TableStatus and self.CreationDateTime == __o.CreationDateTime and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.TableSizeBytes == __o.TableSizeBytes and self.ItemCount == __o.ItemCount and self.TableArn == __o.TableArn and self.TableId == __o.TableId and self.BillingModeSummary == __o.BillingModeSummary and self.LocalSecondaryIndexes == __o.LocalSecondaryIndexes and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.StreamSpecification == __o.StreamSpecification and self.LatestStreamLabel == __o.LatestStreamLabel and self.LatestStreamArn == __o.LatestStreamArn and self.GlobalTableVersion == __o.GlobalTableVersion and self.Replicas == __o.Replicas and self.RestoreSummary == __o.RestoreSummary and self.SSEDescription == __o.SSEDescription and self.ArchivalSummary == __o.ArchivalSummary and self.TableClassSummary == __o.TableClassSummary
    def __hash__(self) -> int:
        return super().__hash__()


class TableName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_41_x_: _dafny.Seq = source__
        return default__.IsValid__TableName(d_41_x_)

class TableStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [TableStatus_CREATING(), TableStatus_UPDATING(), TableStatus_DELETING(), TableStatus_ACTIVE(), TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS(), TableStatus_ARCHIVING(), TableStatus_ARCHIVED()]
    @classmethod
    def default(cls, ):
        return lambda: TableStatus_CREATING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CREATING(self) -> bool:
        return isinstance(self, TableStatus_CREATING)
    @property
    def is_UPDATING(self) -> bool:
        return isinstance(self, TableStatus_UPDATING)
    @property
    def is_DELETING(self) -> bool:
        return isinstance(self, TableStatus_DELETING)
    @property
    def is_ACTIVE(self) -> bool:
        return isinstance(self, TableStatus_ACTIVE)
    @property
    def is_INACCESSIBLE__ENCRYPTION__CREDENTIALS(self) -> bool:
        return isinstance(self, TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)
    @property
    def is_ARCHIVING(self) -> bool:
        return isinstance(self, TableStatus_ARCHIVING)
    @property
    def is_ARCHIVED(self) -> bool:
        return isinstance(self, TableStatus_ARCHIVED)

class TableStatus_CREATING(TableStatus, NamedTuple('CREATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.CREATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_CREATING)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_UPDATING(TableStatus, NamedTuple('UPDATING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.UPDATING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_UPDATING)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_DELETING(TableStatus, NamedTuple('DELETING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.DELETING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_DELETING)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_ACTIVE(TableStatus, NamedTuple('ACTIVE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.ACTIVE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_ACTIVE)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS(TableStatus, NamedTuple('INACCESSIBLE__ENCRYPTION__CREDENTIALS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.INACCESSIBLE_ENCRYPTION_CREDENTIALS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_ARCHIVING(TableStatus, NamedTuple('ARCHIVING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.ARCHIVING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_ARCHIVING)
    def __hash__(self) -> int:
        return super().__hash__()

class TableStatus_ARCHIVED(TableStatus, NamedTuple('ARCHIVED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TableStatus.ARCHIVED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TableStatus_ARCHIVED)
    def __hash__(self) -> int:
        return super().__hash__()


class Tag:
    @classmethod
    def default(cls, ):
        return lambda: Tag_Tag(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Tag(self) -> bool:
        return isinstance(self, Tag_Tag)

class Tag_Tag(Tag, NamedTuple('Tag', [('Key', Any), ('Value', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Tag.Tag({_dafny.string_of(self.Key)}, {_dafny.string_of(self.Value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tag_Tag) and self.Key == __o.Key and self.Value == __o.Value
    def __hash__(self) -> int:
        return super().__hash__()


class TagKeyString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_42_x_: _dafny.Seq = source__
        return default__.IsValid__TagKeyString(d_42_x_)

class TagResourceInput:
    @classmethod
    def default(cls, ):
        return lambda: TagResourceInput_TagResourceInput(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TagResourceInput(self) -> bool:
        return isinstance(self, TagResourceInput_TagResourceInput)

class TagResourceInput_TagResourceInput(TagResourceInput, NamedTuple('TagResourceInput', [('ResourceArn', Any), ('Tags', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TagResourceInput.TagResourceInput({_dafny.string_of(self.ResourceArn)}, {_dafny.string_of(self.Tags)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TagResourceInput_TagResourceInput) and self.ResourceArn == __o.ResourceArn and self.Tags == __o.Tags
    def __hash__(self) -> int:
        return super().__hash__()


class TagValueString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_43_x_: _dafny.Seq = source__
        return default__.IsValid__TagValueString(d_43_x_)

class TimeToLiveAttributeName:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_44_x_: _dafny.Seq = source__
        return default__.IsValid__TimeToLiveAttributeName(d_44_x_)

class TimeToLiveDescription:
    @classmethod
    def default(cls, ):
        return lambda: TimeToLiveDescription_TimeToLiveDescription(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TimeToLiveDescription(self) -> bool:
        return isinstance(self, TimeToLiveDescription_TimeToLiveDescription)

class TimeToLiveDescription_TimeToLiveDescription(TimeToLiveDescription, NamedTuple('TimeToLiveDescription', [('TimeToLiveStatus', Any), ('AttributeName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveDescription.TimeToLiveDescription({_dafny.string_of(self.TimeToLiveStatus)}, {_dafny.string_of(self.AttributeName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveDescription_TimeToLiveDescription) and self.TimeToLiveStatus == __o.TimeToLiveStatus and self.AttributeName == __o.AttributeName
    def __hash__(self) -> int:
        return super().__hash__()


class TimeToLiveSpecification:
    @classmethod
    def default(cls, ):
        return lambda: TimeToLiveSpecification_TimeToLiveSpecification(False, _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TimeToLiveSpecification(self) -> bool:
        return isinstance(self, TimeToLiveSpecification_TimeToLiveSpecification)

class TimeToLiveSpecification_TimeToLiveSpecification(TimeToLiveSpecification, NamedTuple('TimeToLiveSpecification', [('Enabled', Any), ('AttributeName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveSpecification.TimeToLiveSpecification({_dafny.string_of(self.Enabled)}, {_dafny.string_of(self.AttributeName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveSpecification_TimeToLiveSpecification) and self.Enabled == __o.Enabled and self.AttributeName == __o.AttributeName
    def __hash__(self) -> int:
        return super().__hash__()


class TimeToLiveStatus:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [TimeToLiveStatus_ENABLING(), TimeToLiveStatus_DISABLING(), TimeToLiveStatus_ENABLED(), TimeToLiveStatus_DISABLED()]
    @classmethod
    def default(cls, ):
        return lambda: TimeToLiveStatus_ENABLING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ENABLING(self) -> bool:
        return isinstance(self, TimeToLiveStatus_ENABLING)
    @property
    def is_DISABLING(self) -> bool:
        return isinstance(self, TimeToLiveStatus_DISABLING)
    @property
    def is_ENABLED(self) -> bool:
        return isinstance(self, TimeToLiveStatus_ENABLED)
    @property
    def is_DISABLED(self) -> bool:
        return isinstance(self, TimeToLiveStatus_DISABLED)

class TimeToLiveStatus_ENABLING(TimeToLiveStatus, NamedTuple('ENABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveStatus.ENABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveStatus_ENABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class TimeToLiveStatus_DISABLING(TimeToLiveStatus, NamedTuple('DISABLING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveStatus.DISABLING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveStatus_DISABLING)
    def __hash__(self) -> int:
        return super().__hash__()

class TimeToLiveStatus_ENABLED(TimeToLiveStatus, NamedTuple('ENABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveStatus.ENABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveStatus_ENABLED)
    def __hash__(self) -> int:
        return super().__hash__()

class TimeToLiveStatus_DISABLED(TimeToLiveStatus, NamedTuple('DISABLED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TimeToLiveStatus.DISABLED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TimeToLiveStatus_DISABLED)
    def __hash__(self) -> int:
        return super().__hash__()


class TransactGetItem:
    @classmethod
    def default(cls, ):
        return lambda: TransactGetItem_TransactGetItem(Get.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactGetItem(self) -> bool:
        return isinstance(self, TransactGetItem_TransactGetItem)

class TransactGetItem_TransactGetItem(TransactGetItem, NamedTuple('TransactGetItem', [('Get', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactGetItem.TransactGetItem({_dafny.string_of(self.Get)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactGetItem_TransactGetItem) and self.Get == __o.Get
    def __hash__(self) -> int:
        return super().__hash__()


class TransactGetItemList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_45_x_: _dafny.Seq = source__
        return default__.IsValid__TransactGetItemList(d_45_x_)

class TransactGetItemsInput:
    @classmethod
    def default(cls, ):
        return lambda: TransactGetItemsInput_TransactGetItemsInput(_dafny.Seq({}), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactGetItemsInput(self) -> bool:
        return isinstance(self, TransactGetItemsInput_TransactGetItemsInput)

class TransactGetItemsInput_TransactGetItemsInput(TransactGetItemsInput, NamedTuple('TransactGetItemsInput', [('TransactItems', Any), ('ReturnConsumedCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactGetItemsInput.TransactGetItemsInput({_dafny.string_of(self.TransactItems)}, {_dafny.string_of(self.ReturnConsumedCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactGetItemsInput_TransactGetItemsInput) and self.TransactItems == __o.TransactItems and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class TransactGetItemsOutput:
    @classmethod
    def default(cls, ):
        return lambda: TransactGetItemsOutput_TransactGetItemsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactGetItemsOutput(self) -> bool:
        return isinstance(self, TransactGetItemsOutput_TransactGetItemsOutput)

class TransactGetItemsOutput_TransactGetItemsOutput(TransactGetItemsOutput, NamedTuple('TransactGetItemsOutput', [('ConsumedCapacity', Any), ('Responses', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactGetItemsOutput.TransactGetItemsOutput({_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.Responses)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactGetItemsOutput_TransactGetItemsOutput) and self.ConsumedCapacity == __o.ConsumedCapacity and self.Responses == __o.Responses
    def __hash__(self) -> int:
        return super().__hash__()


class TransactWriteItem:
    @classmethod
    def default(cls, ):
        return lambda: TransactWriteItem_TransactWriteItem(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactWriteItem(self) -> bool:
        return isinstance(self, TransactWriteItem_TransactWriteItem)

class TransactWriteItem_TransactWriteItem(TransactWriteItem, NamedTuple('TransactWriteItem', [('ConditionCheck', Any), ('Put', Any), ('Delete', Any), ('Update', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactWriteItem.TransactWriteItem({_dafny.string_of(self.ConditionCheck)}, {_dafny.string_of(self.Put)}, {_dafny.string_of(self.Delete)}, {_dafny.string_of(self.Update)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactWriteItem_TransactWriteItem) and self.ConditionCheck == __o.ConditionCheck and self.Put == __o.Put and self.Delete == __o.Delete and self.Update == __o.Update
    def __hash__(self) -> int:
        return super().__hash__()


class TransactWriteItemList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_46_x_: _dafny.Seq = source__
        return default__.IsValid__TransactWriteItemList(d_46_x_)

class TransactWriteItemsInput:
    @classmethod
    def default(cls, ):
        return lambda: TransactWriteItemsInput_TransactWriteItemsInput(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactWriteItemsInput(self) -> bool:
        return isinstance(self, TransactWriteItemsInput_TransactWriteItemsInput)

class TransactWriteItemsInput_TransactWriteItemsInput(TransactWriteItemsInput, NamedTuple('TransactWriteItemsInput', [('TransactItems', Any), ('ReturnConsumedCapacity', Any), ('ReturnItemCollectionMetrics', Any), ('ClientRequestToken', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactWriteItemsInput.TransactWriteItemsInput({_dafny.string_of(self.TransactItems)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ReturnItemCollectionMetrics)}, {_dafny.string_of(self.ClientRequestToken)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactWriteItemsInput_TransactWriteItemsInput) and self.TransactItems == __o.TransactItems and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ReturnItemCollectionMetrics == __o.ReturnItemCollectionMetrics and self.ClientRequestToken == __o.ClientRequestToken
    def __hash__(self) -> int:
        return super().__hash__()


class TransactWriteItemsOutput:
    @classmethod
    def default(cls, ):
        return lambda: TransactWriteItemsOutput_TransactWriteItemsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TransactWriteItemsOutput(self) -> bool:
        return isinstance(self, TransactWriteItemsOutput_TransactWriteItemsOutput)

class TransactWriteItemsOutput_TransactWriteItemsOutput(TransactWriteItemsOutput, NamedTuple('TransactWriteItemsOutput', [('ConsumedCapacity', Any), ('ItemCollectionMetrics', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.TransactWriteItemsOutput({_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.ItemCollectionMetrics)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TransactWriteItemsOutput_TransactWriteItemsOutput) and self.ConsumedCapacity == __o.ConsumedCapacity and self.ItemCollectionMetrics == __o.ItemCollectionMetrics
    def __hash__(self) -> int:
        return super().__hash__()


class UntagResourceInput:
    @classmethod
    def default(cls, ):
        return lambda: UntagResourceInput_UntagResourceInput(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UntagResourceInput(self) -> bool:
        return isinstance(self, UntagResourceInput_UntagResourceInput)

class UntagResourceInput_UntagResourceInput(UntagResourceInput, NamedTuple('UntagResourceInput', [('ResourceArn', Any), ('TagKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UntagResourceInput.UntagResourceInput({_dafny.string_of(self.ResourceArn)}, {_dafny.string_of(self.TagKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UntagResourceInput_UntagResourceInput) and self.ResourceArn == __o.ResourceArn and self.TagKeys == __o.TagKeys
    def __hash__(self) -> int:
        return super().__hash__()


class Update:
    @classmethod
    def default(cls, ):
        return lambda: Update_Update(_dafny.Map({}), _dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Update(self) -> bool:
        return isinstance(self, Update_Update)

class Update_Update(Update, NamedTuple('Update', [('Key', Any), ('UpdateExpression', Any), ('TableName', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any), ('ReturnValuesOnConditionCheckFailure', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Update.Update({_dafny.string_of(self.Key)}, {_dafny.string_of(self.UpdateExpression)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)}, {_dafny.string_of(self.ReturnValuesOnConditionCheckFailure)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Update_Update) and self.Key == __o.Key and self.UpdateExpression == __o.UpdateExpression and self.TableName == __o.TableName and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues and self.ReturnValuesOnConditionCheckFailure == __o.ReturnValuesOnConditionCheckFailure
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateContinuousBackupsInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateContinuousBackupsInput_UpdateContinuousBackupsInput(_dafny.Seq(""), PointInTimeRecoverySpecification.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateContinuousBackupsInput(self) -> bool:
        return isinstance(self, UpdateContinuousBackupsInput_UpdateContinuousBackupsInput)

class UpdateContinuousBackupsInput_UpdateContinuousBackupsInput(UpdateContinuousBackupsInput, NamedTuple('UpdateContinuousBackupsInput', [('TableName', Any), ('PointInTimeRecoverySpecification', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateContinuousBackupsInput.UpdateContinuousBackupsInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.PointInTimeRecoverySpecification)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateContinuousBackupsInput_UpdateContinuousBackupsInput) and self.TableName == __o.TableName and self.PointInTimeRecoverySpecification == __o.PointInTimeRecoverySpecification
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateContinuousBackupsOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateContinuousBackupsOutput(self) -> bool:
        return isinstance(self, UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput)

class UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput(UpdateContinuousBackupsOutput, NamedTuple('UpdateContinuousBackupsOutput', [('ContinuousBackupsDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateContinuousBackupsOutput.UpdateContinuousBackupsOutput({_dafny.string_of(self.ContinuousBackupsDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput) and self.ContinuousBackupsDescription == __o.ContinuousBackupsDescription
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateContributorInsightsInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateContributorInsightsInput_UpdateContributorInsightsInput(_dafny.Seq(""), Wrappers.Option.default()(), ContributorInsightsAction.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateContributorInsightsInput(self) -> bool:
        return isinstance(self, UpdateContributorInsightsInput_UpdateContributorInsightsInput)

class UpdateContributorInsightsInput_UpdateContributorInsightsInput(UpdateContributorInsightsInput, NamedTuple('UpdateContributorInsightsInput', [('TableName', Any), ('IndexName', Any), ('ContributorInsightsAction', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateContributorInsightsInput.UpdateContributorInsightsInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ContributorInsightsAction)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateContributorInsightsInput_UpdateContributorInsightsInput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.ContributorInsightsAction == __o.ContributorInsightsAction
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateContributorInsightsOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateContributorInsightsOutput_UpdateContributorInsightsOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateContributorInsightsOutput(self) -> bool:
        return isinstance(self, UpdateContributorInsightsOutput_UpdateContributorInsightsOutput)

class UpdateContributorInsightsOutput_UpdateContributorInsightsOutput(UpdateContributorInsightsOutput, NamedTuple('UpdateContributorInsightsOutput', [('TableName', Any), ('IndexName', Any), ('ContributorInsightsStatus', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateContributorInsightsOutput.UpdateContributorInsightsOutput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ContributorInsightsStatus)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateContributorInsightsOutput_UpdateContributorInsightsOutput) and self.TableName == __o.TableName and self.IndexName == __o.IndexName and self.ContributorInsightsStatus == __o.ContributorInsightsStatus
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateGlobalSecondaryIndexAction:
    @classmethod
    def default(cls, ):
        return lambda: UpdateGlobalSecondaryIndexAction_UpdateGlobalSecondaryIndexAction(_dafny.Seq(""), ProvisionedThroughput.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateGlobalSecondaryIndexAction(self) -> bool:
        return isinstance(self, UpdateGlobalSecondaryIndexAction_UpdateGlobalSecondaryIndexAction)

class UpdateGlobalSecondaryIndexAction_UpdateGlobalSecondaryIndexAction(UpdateGlobalSecondaryIndexAction, NamedTuple('UpdateGlobalSecondaryIndexAction', [('IndexName', Any), ('ProvisionedThroughput', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateGlobalSecondaryIndexAction.UpdateGlobalSecondaryIndexAction({_dafny.string_of(self.IndexName)}, {_dafny.string_of(self.ProvisionedThroughput)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateGlobalSecondaryIndexAction_UpdateGlobalSecondaryIndexAction) and self.IndexName == __o.IndexName and self.ProvisionedThroughput == __o.ProvisionedThroughput
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateGlobalTableInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateGlobalTableInput_UpdateGlobalTableInput(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateGlobalTableInput(self) -> bool:
        return isinstance(self, UpdateGlobalTableInput_UpdateGlobalTableInput)

class UpdateGlobalTableInput_UpdateGlobalTableInput(UpdateGlobalTableInput, NamedTuple('UpdateGlobalTableInput', [('GlobalTableName', Any), ('ReplicaUpdates', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateGlobalTableInput.UpdateGlobalTableInput({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.ReplicaUpdates)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateGlobalTableInput_UpdateGlobalTableInput) and self.GlobalTableName == __o.GlobalTableName and self.ReplicaUpdates == __o.ReplicaUpdates
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateGlobalTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateGlobalTableOutput_UpdateGlobalTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateGlobalTableOutput(self) -> bool:
        return isinstance(self, UpdateGlobalTableOutput_UpdateGlobalTableOutput)

class UpdateGlobalTableOutput_UpdateGlobalTableOutput(UpdateGlobalTableOutput, NamedTuple('UpdateGlobalTableOutput', [('GlobalTableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateGlobalTableOutput.UpdateGlobalTableOutput({_dafny.string_of(self.GlobalTableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateGlobalTableOutput_UpdateGlobalTableOutput) and self.GlobalTableDescription == __o.GlobalTableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateGlobalTableSettingsInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateGlobalTableSettingsInput(self) -> bool:
        return isinstance(self, UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput)

class UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput(UpdateGlobalTableSettingsInput, NamedTuple('UpdateGlobalTableSettingsInput', [('GlobalTableName', Any), ('GlobalTableBillingMode', Any), ('GlobalTableProvisionedWriteCapacityUnits', Any), ('GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate', Any), ('GlobalTableGlobalSecondaryIndexSettingsUpdate', Any), ('ReplicaSettingsUpdate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateGlobalTableSettingsInput.UpdateGlobalTableSettingsInput({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.GlobalTableBillingMode)}, {_dafny.string_of(self.GlobalTableProvisionedWriteCapacityUnits)}, {_dafny.string_of(self.GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate)}, {_dafny.string_of(self.GlobalTableGlobalSecondaryIndexSettingsUpdate)}, {_dafny.string_of(self.ReplicaSettingsUpdate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput) and self.GlobalTableName == __o.GlobalTableName and self.GlobalTableBillingMode == __o.GlobalTableBillingMode and self.GlobalTableProvisionedWriteCapacityUnits == __o.GlobalTableProvisionedWriteCapacityUnits and self.GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate == __o.GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate and self.GlobalTableGlobalSecondaryIndexSettingsUpdate == __o.GlobalTableGlobalSecondaryIndexSettingsUpdate and self.ReplicaSettingsUpdate == __o.ReplicaSettingsUpdate
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateGlobalTableSettingsOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateGlobalTableSettingsOutput(self) -> bool:
        return isinstance(self, UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput)

class UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput(UpdateGlobalTableSettingsOutput, NamedTuple('UpdateGlobalTableSettingsOutput', [('GlobalTableName', Any), ('ReplicaSettings', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateGlobalTableSettingsOutput.UpdateGlobalTableSettingsOutput({_dafny.string_of(self.GlobalTableName)}, {_dafny.string_of(self.ReplicaSettings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput) and self.GlobalTableName == __o.GlobalTableName and self.ReplicaSettings == __o.ReplicaSettings
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateItemInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateItemInput_UpdateItemInput(_dafny.Seq(""), _dafny.Map({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateItemInput(self) -> bool:
        return isinstance(self, UpdateItemInput_UpdateItemInput)

class UpdateItemInput_UpdateItemInput(UpdateItemInput, NamedTuple('UpdateItemInput', [('TableName', Any), ('Key', Any), ('AttributeUpdates', Any), ('Expected', Any), ('ConditionalOperator', Any), ('ReturnValues', Any), ('ReturnConsumedCapacity', Any), ('ReturnItemCollectionMetrics', Any), ('UpdateExpression', Any), ('ConditionExpression', Any), ('ExpressionAttributeNames', Any), ('ExpressionAttributeValues', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateItemInput.UpdateItemInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.Key)}, {_dafny.string_of(self.AttributeUpdates)}, {_dafny.string_of(self.Expected)}, {_dafny.string_of(self.ConditionalOperator)}, {_dafny.string_of(self.ReturnValues)}, {_dafny.string_of(self.ReturnConsumedCapacity)}, {_dafny.string_of(self.ReturnItemCollectionMetrics)}, {_dafny.string_of(self.UpdateExpression)}, {_dafny.string_of(self.ConditionExpression)}, {_dafny.string_of(self.ExpressionAttributeNames)}, {_dafny.string_of(self.ExpressionAttributeValues)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateItemInput_UpdateItemInput) and self.TableName == __o.TableName and self.Key == __o.Key and self.AttributeUpdates == __o.AttributeUpdates and self.Expected == __o.Expected and self.ConditionalOperator == __o.ConditionalOperator and self.ReturnValues == __o.ReturnValues and self.ReturnConsumedCapacity == __o.ReturnConsumedCapacity and self.ReturnItemCollectionMetrics == __o.ReturnItemCollectionMetrics and self.UpdateExpression == __o.UpdateExpression and self.ConditionExpression == __o.ConditionExpression and self.ExpressionAttributeNames == __o.ExpressionAttributeNames and self.ExpressionAttributeValues == __o.ExpressionAttributeValues
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateItemOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateItemOutput_UpdateItemOutput(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateItemOutput(self) -> bool:
        return isinstance(self, UpdateItemOutput_UpdateItemOutput)

class UpdateItemOutput_UpdateItemOutput(UpdateItemOutput, NamedTuple('UpdateItemOutput', [('Attributes', Any), ('ConsumedCapacity', Any), ('ItemCollectionMetrics', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateItemOutput.UpdateItemOutput({_dafny.string_of(self.Attributes)}, {_dafny.string_of(self.ConsumedCapacity)}, {_dafny.string_of(self.ItemCollectionMetrics)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateItemOutput_UpdateItemOutput) and self.Attributes == __o.Attributes and self.ConsumedCapacity == __o.ConsumedCapacity and self.ItemCollectionMetrics == __o.ItemCollectionMetrics
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateReplicationGroupMemberAction:
    @classmethod
    def default(cls, ):
        return lambda: UpdateReplicationGroupMemberAction_UpdateReplicationGroupMemberAction(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateReplicationGroupMemberAction(self) -> bool:
        return isinstance(self, UpdateReplicationGroupMemberAction_UpdateReplicationGroupMemberAction)

class UpdateReplicationGroupMemberAction_UpdateReplicationGroupMemberAction(UpdateReplicationGroupMemberAction, NamedTuple('UpdateReplicationGroupMemberAction', [('RegionName', Any), ('KMSMasterKeyId', Any), ('ProvisionedThroughputOverride', Any), ('GlobalSecondaryIndexes', Any), ('TableClassOverride', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateReplicationGroupMemberAction.UpdateReplicationGroupMemberAction({_dafny.string_of(self.RegionName)}, {_dafny.string_of(self.KMSMasterKeyId)}, {_dafny.string_of(self.ProvisionedThroughputOverride)}, {_dafny.string_of(self.GlobalSecondaryIndexes)}, {_dafny.string_of(self.TableClassOverride)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateReplicationGroupMemberAction_UpdateReplicationGroupMemberAction) and self.RegionName == __o.RegionName and self.KMSMasterKeyId == __o.KMSMasterKeyId and self.ProvisionedThroughputOverride == __o.ProvisionedThroughputOverride and self.GlobalSecondaryIndexes == __o.GlobalSecondaryIndexes and self.TableClassOverride == __o.TableClassOverride
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTableInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTableInput_UpdateTableInput(Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTableInput(self) -> bool:
        return isinstance(self, UpdateTableInput_UpdateTableInput)

class UpdateTableInput_UpdateTableInput(UpdateTableInput, NamedTuple('UpdateTableInput', [('AttributeDefinitions', Any), ('TableName', Any), ('BillingMode', Any), ('ProvisionedThroughput', Any), ('GlobalSecondaryIndexUpdates', Any), ('StreamSpecification', Any), ('SSESpecification', Any), ('ReplicaUpdates', Any), ('TableClass', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTableInput.UpdateTableInput({_dafny.string_of(self.AttributeDefinitions)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.BillingMode)}, {_dafny.string_of(self.ProvisionedThroughput)}, {_dafny.string_of(self.GlobalSecondaryIndexUpdates)}, {_dafny.string_of(self.StreamSpecification)}, {_dafny.string_of(self.SSESpecification)}, {_dafny.string_of(self.ReplicaUpdates)}, {_dafny.string_of(self.TableClass)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTableInput_UpdateTableInput) and self.AttributeDefinitions == __o.AttributeDefinitions and self.TableName == __o.TableName and self.BillingMode == __o.BillingMode and self.ProvisionedThroughput == __o.ProvisionedThroughput and self.GlobalSecondaryIndexUpdates == __o.GlobalSecondaryIndexUpdates and self.StreamSpecification == __o.StreamSpecification and self.SSESpecification == __o.SSESpecification and self.ReplicaUpdates == __o.ReplicaUpdates and self.TableClass == __o.TableClass
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTableOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTableOutput_UpdateTableOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTableOutput(self) -> bool:
        return isinstance(self, UpdateTableOutput_UpdateTableOutput)

class UpdateTableOutput_UpdateTableOutput(UpdateTableOutput, NamedTuple('UpdateTableOutput', [('TableDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTableOutput.UpdateTableOutput({_dafny.string_of(self.TableDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTableOutput_UpdateTableOutput) and self.TableDescription == __o.TableDescription
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTableReplicaAutoScalingInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput(Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTableReplicaAutoScalingInput(self) -> bool:
        return isinstance(self, UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput)

class UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput(UpdateTableReplicaAutoScalingInput, NamedTuple('UpdateTableReplicaAutoScalingInput', [('GlobalSecondaryIndexUpdates', Any), ('TableName', Any), ('ProvisionedWriteCapacityAutoScalingUpdate', Any), ('ReplicaUpdates', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTableReplicaAutoScalingInput.UpdateTableReplicaAutoScalingInput({_dafny.string_of(self.GlobalSecondaryIndexUpdates)}, {_dafny.string_of(self.TableName)}, {_dafny.string_of(self.ProvisionedWriteCapacityAutoScalingUpdate)}, {_dafny.string_of(self.ReplicaUpdates)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput) and self.GlobalSecondaryIndexUpdates == __o.GlobalSecondaryIndexUpdates and self.TableName == __o.TableName and self.ProvisionedWriteCapacityAutoScalingUpdate == __o.ProvisionedWriteCapacityAutoScalingUpdate and self.ReplicaUpdates == __o.ReplicaUpdates
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTableReplicaAutoScalingOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTableReplicaAutoScalingOutput(self) -> bool:
        return isinstance(self, UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput)

class UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput(UpdateTableReplicaAutoScalingOutput, NamedTuple('UpdateTableReplicaAutoScalingOutput', [('TableAutoScalingDescription', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTableReplicaAutoScalingOutput.UpdateTableReplicaAutoScalingOutput({_dafny.string_of(self.TableAutoScalingDescription)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput) and self.TableAutoScalingDescription == __o.TableAutoScalingDescription
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTimeToLiveInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTimeToLiveInput_UpdateTimeToLiveInput(_dafny.Seq(""), TimeToLiveSpecification.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTimeToLiveInput(self) -> bool:
        return isinstance(self, UpdateTimeToLiveInput_UpdateTimeToLiveInput)

class UpdateTimeToLiveInput_UpdateTimeToLiveInput(UpdateTimeToLiveInput, NamedTuple('UpdateTimeToLiveInput', [('TableName', Any), ('TimeToLiveSpecification', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTimeToLiveInput.UpdateTimeToLiveInput({_dafny.string_of(self.TableName)}, {_dafny.string_of(self.TimeToLiveSpecification)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTimeToLiveInput_UpdateTimeToLiveInput) and self.TableName == __o.TableName and self.TimeToLiveSpecification == __o.TimeToLiveSpecification
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateTimeToLiveOutput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateTimeToLiveOutput_UpdateTimeToLiveOutput(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateTimeToLiveOutput(self) -> bool:
        return isinstance(self, UpdateTimeToLiveOutput_UpdateTimeToLiveOutput)

class UpdateTimeToLiveOutput_UpdateTimeToLiveOutput(UpdateTimeToLiveOutput, NamedTuple('UpdateTimeToLiveOutput', [('TimeToLiveSpecification', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.UpdateTimeToLiveOutput.UpdateTimeToLiveOutput({_dafny.string_of(self.TimeToLiveSpecification)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateTimeToLiveOutput_UpdateTimeToLiveOutput) and self.TimeToLiveSpecification == __o.TimeToLiveSpecification
    def __hash__(self) -> int:
        return super().__hash__()


class WriteRequest:
    @classmethod
    def default(cls, ):
        return lambda: WriteRequest_WriteRequest(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WriteRequest(self) -> bool:
        return isinstance(self, WriteRequest_WriteRequest)

class WriteRequest_WriteRequest(WriteRequest, NamedTuple('WriteRequest', [('PutRequest', Any), ('DeleteRequest', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.WriteRequest.WriteRequest({_dafny.string_of(self.PutRequest)}, {_dafny.string_of(self.DeleteRequest)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WriteRequest_WriteRequest) and self.PutRequest == __o.PutRequest and self.DeleteRequest == __o.DeleteRequest
    def __hash__(self) -> int:
        return super().__hash__()


class WriteRequests:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_47_x_: _dafny.Seq = source__
        return default__.IsValid__WriteRequests(d_47_x_)

class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_BackupInUseException(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BackupInUseException(self) -> bool:
        return isinstance(self, Error_BackupInUseException)
    @property
    def is_BackupNotFoundException(self) -> bool:
        return isinstance(self, Error_BackupNotFoundException)
    @property
    def is_ConditionalCheckFailedException(self) -> bool:
        return isinstance(self, Error_ConditionalCheckFailedException)
    @property
    def is_ContinuousBackupsUnavailableException(self) -> bool:
        return isinstance(self, Error_ContinuousBackupsUnavailableException)
    @property
    def is_DuplicateItemException(self) -> bool:
        return isinstance(self, Error_DuplicateItemException)
    @property
    def is_ExportConflictException(self) -> bool:
        return isinstance(self, Error_ExportConflictException)
    @property
    def is_ExportNotFoundException(self) -> bool:
        return isinstance(self, Error_ExportNotFoundException)
    @property
    def is_GlobalTableAlreadyExistsException(self) -> bool:
        return isinstance(self, Error_GlobalTableAlreadyExistsException)
    @property
    def is_GlobalTableNotFoundException(self) -> bool:
        return isinstance(self, Error_GlobalTableNotFoundException)
    @property
    def is_IdempotentParameterMismatchException(self) -> bool:
        return isinstance(self, Error_IdempotentParameterMismatchException)
    @property
    def is_ImportConflictException(self) -> bool:
        return isinstance(self, Error_ImportConflictException)
    @property
    def is_ImportNotFoundException(self) -> bool:
        return isinstance(self, Error_ImportNotFoundException)
    @property
    def is_IndexNotFoundException(self) -> bool:
        return isinstance(self, Error_IndexNotFoundException)
    @property
    def is_InternalServerError(self) -> bool:
        return isinstance(self, Error_InternalServerError)
    @property
    def is_InvalidEndpointException(self) -> bool:
        return isinstance(self, Error_InvalidEndpointException)
    @property
    def is_InvalidExportTimeException(self) -> bool:
        return isinstance(self, Error_InvalidExportTimeException)
    @property
    def is_InvalidRestoreTimeException(self) -> bool:
        return isinstance(self, Error_InvalidRestoreTimeException)
    @property
    def is_ItemCollectionSizeLimitExceededException(self) -> bool:
        return isinstance(self, Error_ItemCollectionSizeLimitExceededException)
    @property
    def is_LimitExceededException(self) -> bool:
        return isinstance(self, Error_LimitExceededException)
    @property
    def is_PointInTimeRecoveryUnavailableException(self) -> bool:
        return isinstance(self, Error_PointInTimeRecoveryUnavailableException)
    @property
    def is_ProvisionedThroughputExceededException(self) -> bool:
        return isinstance(self, Error_ProvisionedThroughputExceededException)
    @property
    def is_ReplicaAlreadyExistsException(self) -> bool:
        return isinstance(self, Error_ReplicaAlreadyExistsException)
    @property
    def is_ReplicaNotFoundException(self) -> bool:
        return isinstance(self, Error_ReplicaNotFoundException)
    @property
    def is_RequestLimitExceeded(self) -> bool:
        return isinstance(self, Error_RequestLimitExceeded)
    @property
    def is_ResourceInUseException(self) -> bool:
        return isinstance(self, Error_ResourceInUseException)
    @property
    def is_ResourceNotFoundException(self) -> bool:
        return isinstance(self, Error_ResourceNotFoundException)
    @property
    def is_TableAlreadyExistsException(self) -> bool:
        return isinstance(self, Error_TableAlreadyExistsException)
    @property
    def is_TableInUseException(self) -> bool:
        return isinstance(self, Error_TableInUseException)
    @property
    def is_TableNotFoundException(self) -> bool:
        return isinstance(self, Error_TableNotFoundException)
    @property
    def is_TransactionCanceledException(self) -> bool:
        return isinstance(self, Error_TransactionCanceledException)
    @property
    def is_TransactionConflictException(self) -> bool:
        return isinstance(self, Error_TransactionConflictException)
    @property
    def is_TransactionInProgressException(self) -> bool:
        return isinstance(self, Error_TransactionInProgressException)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, Error_Opaque)

class Error_BackupInUseException(Error, NamedTuple('BackupInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.BackupInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_BackupInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_BackupNotFoundException(Error, NamedTuple('BackupNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.BackupNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_BackupNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ConditionalCheckFailedException(Error, NamedTuple('ConditionalCheckFailedException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ConditionalCheckFailedException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ConditionalCheckFailedException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ContinuousBackupsUnavailableException(Error, NamedTuple('ContinuousBackupsUnavailableException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ContinuousBackupsUnavailableException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ContinuousBackupsUnavailableException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_DuplicateItemException(Error, NamedTuple('DuplicateItemException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.DuplicateItemException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_DuplicateItemException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ExportConflictException(Error, NamedTuple('ExportConflictException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ExportConflictException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ExportConflictException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ExportNotFoundException(Error, NamedTuple('ExportNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ExportNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ExportNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_GlobalTableAlreadyExistsException(Error, NamedTuple('GlobalTableAlreadyExistsException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.GlobalTableAlreadyExistsException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_GlobalTableAlreadyExistsException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_GlobalTableNotFoundException(Error, NamedTuple('GlobalTableNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.GlobalTableNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_GlobalTableNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_IdempotentParameterMismatchException(Error, NamedTuple('IdempotentParameterMismatchException', [('Message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.IdempotentParameterMismatchException({_dafny.string_of(self.Message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_IdempotentParameterMismatchException) and self.Message == __o.Message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ImportConflictException(Error, NamedTuple('ImportConflictException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ImportConflictException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ImportConflictException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ImportNotFoundException(Error, NamedTuple('ImportNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ImportNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ImportNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_IndexNotFoundException(Error, NamedTuple('IndexNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.IndexNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_IndexNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InternalServerError(Error, NamedTuple('InternalServerError', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.InternalServerError({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InternalServerError) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidEndpointException(Error, NamedTuple('InvalidEndpointException', [('Message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.InvalidEndpointException({_dafny.string_of(self.Message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidEndpointException) and self.Message == __o.Message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidExportTimeException(Error, NamedTuple('InvalidExportTimeException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.InvalidExportTimeException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidExportTimeException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidRestoreTimeException(Error, NamedTuple('InvalidRestoreTimeException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.InvalidRestoreTimeException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidRestoreTimeException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ItemCollectionSizeLimitExceededException(Error, NamedTuple('ItemCollectionSizeLimitExceededException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ItemCollectionSizeLimitExceededException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ItemCollectionSizeLimitExceededException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_LimitExceededException(Error, NamedTuple('LimitExceededException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.LimitExceededException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_LimitExceededException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_PointInTimeRecoveryUnavailableException(Error, NamedTuple('PointInTimeRecoveryUnavailableException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.PointInTimeRecoveryUnavailableException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_PointInTimeRecoveryUnavailableException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ProvisionedThroughputExceededException(Error, NamedTuple('ProvisionedThroughputExceededException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ProvisionedThroughputExceededException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ProvisionedThroughputExceededException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ReplicaAlreadyExistsException(Error, NamedTuple('ReplicaAlreadyExistsException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ReplicaAlreadyExistsException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ReplicaAlreadyExistsException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ReplicaNotFoundException(Error, NamedTuple('ReplicaNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ReplicaNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ReplicaNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_RequestLimitExceeded(Error, NamedTuple('RequestLimitExceeded', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.RequestLimitExceeded({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_RequestLimitExceeded) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ResourceInUseException(Error, NamedTuple('ResourceInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ResourceInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ResourceInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ResourceNotFoundException(Error, NamedTuple('ResourceNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.ResourceNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ResourceNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TableAlreadyExistsException(Error, NamedTuple('TableAlreadyExistsException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TableAlreadyExistsException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TableAlreadyExistsException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TableInUseException(Error, NamedTuple('TableInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TableInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TableInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TableNotFoundException(Error, NamedTuple('TableNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TableNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TableNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TransactionCanceledException(Error, NamedTuple('TransactionCanceledException', [('Message', Any), ('CancellationReasons', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TransactionCanceledException({_dafny.string_of(self.Message)}, {_dafny.string_of(self.CancellationReasons)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TransactionCanceledException) and self.Message == __o.Message and self.CancellationReasons == __o.CancellationReasons
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TransactionConflictException(Error, NamedTuple('TransactionConflictException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TransactionConflictException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TransactionConflictException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TransactionInProgressException(Error, NamedTuple('TransactionInProgressException', [('Message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.TransactionInProgressException({_dafny.string_of(self.Message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TransactionInProgressException) and self.Message == __o.Message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any), ('alt__text', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsDynamodbTypes.Error.Opaque({_dafny.string_of(self.obj)}, {_dafny.string_of(self.alt__text)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj and self.alt__text == __o.alt__text
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
    def _Is(source__):
        d_48_e_: Error = source__
        return (d_48_e_).is_Opaque
