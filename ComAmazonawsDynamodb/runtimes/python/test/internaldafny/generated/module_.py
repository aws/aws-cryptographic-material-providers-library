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
import software_amazon_cryptography_services_dynamodb_internaldafny
import TestDDBv2

assert "module_" == __name__
module_ = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_33_success_: bool
        d_33_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDDBv2.BasicQueryTests: ")))
        try:
            if True:
                TestDDBv2.default__.BasicQueryTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_34_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_34_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_33_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDDBv2.BasicGetTests: ")))
        try:
            if True:
                TestDDBv2.default__.BasicGetTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_35_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_35_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_33_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDDBv2.BasicPutTests: ")))
        try:
            if True:
                TestDDBv2.default__.BasicPutTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_36_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_36_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_33_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDDBv2.BatGetItemTests: ")))
        try:
            if True:
                TestDDBv2.default__.BatGetItemTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_37_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_37_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_33_success_ = False
        if not(d_33_success_):
            raise _dafny.HaltException("test/TestDDBv2.dfy(4,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

