import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import StandardLibrary_mUInt
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types

# Module: software_amazon_cryptography_services_dynamodb_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultDynamoDBClientConfigType():
        return DynamoDBClientConfigType_DynamoDBClientConfigType()


class DynamoDBClientConfigType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DynamoDBClientConfigType_DynamoDBClientConfigType()]
    @classmethod
    def default(cls, ):
        return lambda: DynamoDBClientConfigType_DynamoDBClientConfigType()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DynamoDBClientConfigType(self) -> bool:
        return isinstance(self, DynamoDBClientConfigType_DynamoDBClientConfigType)

class DynamoDBClientConfigType_DynamoDBClientConfigType(DynamoDBClientConfigType, NamedTuple('DynamoDBClientConfigType', [])):
    def __dafnystr__(self) -> str:
        return f'Com_Amazonaws_Dynamodb.DynamoDBClientConfigType.DynamoDBClientConfigType'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DynamoDBClientConfigType_DynamoDBClientConfigType)
    def __hash__(self) -> int:
        return super().__hash__()

