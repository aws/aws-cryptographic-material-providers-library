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
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer

# assert "JSON_mConcreteSyntax_mSpec" == __name__
JSON_mConcreteSyntax_mSpec = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def View(v):
        return (v).Bytes()

    @staticmethod
    def Structural(self, fT):
        return ((JSON_mConcreteSyntax_mSpec.default__.View((self).before)) + (fT((self).t))) + (JSON_mConcreteSyntax_mSpec.default__.View((self).after))

    @staticmethod
    def StructuralView(self):
        return JSON_mConcreteSyntax_mSpec.default__.Structural(self, JSON_mConcreteSyntax_mSpec.default__.View)

    @staticmethod
    def Maybe(self, fT):
        if (self).is_Empty:
            return _dafny.Seq([])
        elif True:
            return fT((self).t)

    @staticmethod
    def ConcatBytes(ts, fT):
        d_573___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ts)) == (0):
                    return (d_573___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_573___accumulator_ = (d_573___accumulator_) + (fT((ts)[0]))
                    in121_ = _dafny.Seq((ts)[1::])
                    in122_ = fT
                    ts = in121_
                    fT = in122_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Bracketed(self, fDatum):
        return ((JSON_mConcreteSyntax_mSpec.default__.StructuralView((self).l)) + (JSON_mConcreteSyntax_mSpec.default__.ConcatBytes((self).data, fDatum))) + (JSON_mConcreteSyntax_mSpec.default__.StructuralView((self).r))

    @staticmethod
    def KeyValue(self):
        return ((JSON_mConcreteSyntax_mSpec.default__.String((self).k)) + (JSON_mConcreteSyntax_mSpec.default__.StructuralView((self).colon))) + (JSON_mConcreteSyntax_mSpec.default__.Value((self).v))

    @staticmethod
    def Frac(self):
        return (JSON_mConcreteSyntax_mSpec.default__.View((self).period)) + (JSON_mConcreteSyntax_mSpec.default__.View((self).num))

    @staticmethod
    def Exp(self):
        return ((JSON_mConcreteSyntax_mSpec.default__.View((self).e)) + (JSON_mConcreteSyntax_mSpec.default__.View((self).sign))) + (JSON_mConcreteSyntax_mSpec.default__.View((self).num))

    @staticmethod
    def Number(self):
        return (((JSON_mConcreteSyntax_mSpec.default__.View((self).minus)) + (JSON_mConcreteSyntax_mSpec.default__.View((self).num))) + (JSON_mConcreteSyntax_mSpec.default__.Maybe((self).frac, JSON_mConcreteSyntax_mSpec.default__.Frac))) + (JSON_mConcreteSyntax_mSpec.default__.Maybe((self).exp, JSON_mConcreteSyntax_mSpec.default__.Exp))

    @staticmethod
    def String(self):
        return ((JSON_mConcreteSyntax_mSpec.default__.View((self).lq)) + (JSON_mConcreteSyntax_mSpec.default__.View((self).contents))) + (JSON_mConcreteSyntax_mSpec.default__.View((self).rq))

    @staticmethod
    def CommaSuffix(c):
        return JSON_mConcreteSyntax_mSpec.default__.Maybe(c, JSON_mConcreteSyntax_mSpec.default__.StructuralView)

    @staticmethod
    def Member(self):
        return (JSON_mConcreteSyntax_mSpec.default__.KeyValue((self).t)) + (JSON_mConcreteSyntax_mSpec.default__.CommaSuffix((self).suffix))

    @staticmethod
    def Item(self):
        return (JSON_mConcreteSyntax_mSpec.default__.Value((self).t)) + (JSON_mConcreteSyntax_mSpec.default__.CommaSuffix((self).suffix))

    @staticmethod
    def Object(obj):
        def lambda44_(d_574_obj_):
            def lambda45_(d_575_d_):
                return JSON_mConcreteSyntax_mSpec.default__.Member(d_575_d_)

            return lambda45_

        return JSON_mConcreteSyntax_mSpec.default__.Bracketed(obj, lambda44_(obj))

    @staticmethod
    def Array(arr):
        def lambda46_(d_576_arr_):
            def lambda47_(d_577_d_):
                return JSON_mConcreteSyntax_mSpec.default__.Item(d_577_d_)

            return lambda47_

        return JSON_mConcreteSyntax_mSpec.default__.Bracketed(arr, lambda46_(arr))

    @staticmethod
    def Value(self):
        source18_ = self
        if source18_.is_Null:
            d_578___mcc_h0_ = source18_.n
            d_579_n_ = d_578___mcc_h0_
            return JSON_mConcreteSyntax_mSpec.default__.View(d_579_n_)
        elif source18_.is_Bool:
            d_580___mcc_h1_ = source18_.b
            d_581_b_ = d_580___mcc_h1_
            return JSON_mConcreteSyntax_mSpec.default__.View(d_581_b_)
        elif source18_.is_String:
            d_582___mcc_h2_ = source18_.str
            d_583_str_ = d_582___mcc_h2_
            return JSON_mConcreteSyntax_mSpec.default__.String(d_583_str_)
        elif source18_.is_Number:
            d_584___mcc_h3_ = source18_.num
            d_585_num_ = d_584___mcc_h3_
            return JSON_mConcreteSyntax_mSpec.default__.Number(d_585_num_)
        elif source18_.is_Object:
            d_586___mcc_h4_ = source18_.obj
            d_587_obj_ = d_586___mcc_h4_
            return JSON_mConcreteSyntax_mSpec.default__.Object(d_587_obj_)
        elif True:
            d_588___mcc_h5_ = source18_.arr
            d_589_arr_ = d_588___mcc_h5_
            return JSON_mConcreteSyntax_mSpec.default__.Array(d_589_arr_)

    @staticmethod
    def JSON(js):
        return JSON_mConcreteSyntax_mSpec.default__.Structural(js, JSON_mConcreteSyntax_mSpec.default__.Value)

