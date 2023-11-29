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

# assert "JSON_mGrammar" == __name__
JSON_mGrammar = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Blank_q(b):
        return ((((b) == (32)) or ((b) == (9))) or ((b) == (10))) or ((b) == (13))

    @staticmethod
    def Digit_q(b):
        return ((ord('0')) <= (b)) and ((b) <= (ord('9')))

    @_dafny.classproperty
    def NULL(instance):
        return _dafny.Seq([ord('n'), ord('u'), ord('l'), ord('l')])
    @_dafny.classproperty
    def TRUE(instance):
        return _dafny.Seq([ord('t'), ord('r'), ord('u'), ord('e')])
    @_dafny.classproperty
    def FALSE(instance):
        return _dafny.Seq([ord('f'), ord('a'), ord('l'), ord('s'), ord('e')])
    @_dafny.classproperty
    def DOUBLEQUOTE(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('\"')]))
    @_dafny.classproperty
    def PERIOD(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('.')]))
    @_dafny.classproperty
    def E(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('e')]))
    @_dafny.classproperty
    def COLON(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord(':')]))
    @_dafny.classproperty
    def COMMA(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord(',')]))
    @_dafny.classproperty
    def LBRACE(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('{')]))
    @_dafny.classproperty
    def RBRACE(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('}')]))
    @_dafny.classproperty
    def LBRACKET(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('[')]))
    @_dafny.classproperty
    def RBRACKET(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord(']')]))
    @_dafny.classproperty
    def MINUS(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('-')]))
    @_dafny.classproperty
    def EMPTY(instance):
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([]))

class jchar:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('b')]))

class jquote:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).DOUBLEQUOTE

class jperiod:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).PERIOD

class je:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).E

class jcolon:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).COLON

class jcomma:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).COMMA

class jlbrace:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).LBRACE

class jrbrace:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).RBRACE

class jlbracket:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).LBRACKET

class jrbracket:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).RBRACKET

class jminus:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).MINUS

class jsign:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return (JSON_mGrammar.default__).EMPTY

class jblanks:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([]))

class Structural:
    @classmethod
    def default(cls, default_T):
        return lambda: Structural_Structural(JSON_mGrammar.jblanks.default(), default_T(), JSON_mGrammar.jblanks.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Structural(self) -> bool:
        return isinstance(self, JSON_mGrammar.Structural_Structural)

class Structural_Structural(Structural, NamedTuple('Structural', [('before', Any), ('t', Any), ('after', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Structural.Structural({_dafny.string_of(self.before)}, {_dafny.string_of(self.t)}, {_dafny.string_of(self.after)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Structural_Structural) and self.before == __o.before and self.t == __o.t and self.after == __o.after
    def __hash__(self) -> int:
        return super().__hash__()


class Maybe:
    @classmethod
    def default(cls, ):
        return lambda: Maybe_Empty()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Empty(self) -> bool:
        return isinstance(self, JSON_mGrammar.Maybe_Empty)
    @property
    def is_NonEmpty(self) -> bool:
        return isinstance(self, JSON_mGrammar.Maybe_NonEmpty)

class Maybe_Empty(Maybe, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Maybe.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Maybe_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class Maybe_NonEmpty(Maybe, NamedTuple('NonEmpty', [('t', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Maybe.NonEmpty({_dafny.string_of(self.t)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Maybe_NonEmpty) and self.t == __o.t
    def __hash__(self) -> int:
        return super().__hash__()


class Suffixed:
    @classmethod
    def default(cls, default_T):
        return lambda: Suffixed_Suffixed(default_T(), JSON_mGrammar.Maybe_Empty.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Suffixed(self) -> bool:
        return isinstance(self, JSON_mGrammar.Suffixed_Suffixed)

class Suffixed_Suffixed(Suffixed, NamedTuple('Suffixed', [('t', Any), ('suffix', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Suffixed.Suffixed({_dafny.string_of(self.t)}, {_dafny.string_of(self.suffix)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Suffixed_Suffixed) and self.t == __o.t and self.suffix == __o.suffix
    def __hash__(self) -> int:
        return super().__hash__()


class SuffixedSequence:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})

class Bracketed:
    @classmethod
    def default(cls, default_L, default_R):
        return lambda: Bracketed_Bracketed(JSON_mGrammar.Structural_Structural.default(default_L)(), _dafny.Seq({}), JSON_mGrammar.Structural_Structural.default(default_R)())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Bracketed(self) -> bool:
        return isinstance(self, JSON_mGrammar.Bracketed_Bracketed)

class Bracketed_Bracketed(Bracketed, NamedTuple('Bracketed', [('l', Any), ('data', Any), ('r', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Bracketed.Bracketed({_dafny.string_of(self.l)}, {_dafny.string_of(self.data)}, {_dafny.string_of(self.r)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Bracketed_Bracketed) and self.l == __o.l and self.data == __o.data and self.r == __o.r
    def __hash__(self) -> int:
        return super().__hash__()


class jnull:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes((JSON_mGrammar.default__).NULL)

class jbool:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes((JSON_mGrammar.default__).TRUE)

class jdigits:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([]))

class jnum:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('0')]))

class jint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([ord('0')]))

class jstr:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([]))

class jstring:
    @classmethod
    def default(cls, ):
        return lambda: jstring_JString(JSON_mGrammar.jquote.default(), JSON_mGrammar.jstr.default(), JSON_mGrammar.jquote.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_JString(self) -> bool:
        return isinstance(self, JSON_mGrammar.jstring_JString)

class jstring_JString(jstring, NamedTuple('JString', [('lq', Any), ('contents', Any), ('rq', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.jstring.JString({_dafny.string_of(self.lq)}, {_dafny.string_of(self.contents)}, {_dafny.string_of(self.rq)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.jstring_JString) and self.lq == __o.lq and self.contents == __o.contents and self.rq == __o.rq
    def __hash__(self) -> int:
        return super().__hash__()


class jKeyValue:
    @classmethod
    def default(cls, ):
        return lambda: jKeyValue_KeyValue(JSON_mGrammar.jstring_JString.default()(), JSON_mGrammar.Structural_Structural.default(JSON_mGrammar.jcolon.default)(), JSON_mGrammar.Value_Null.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyValue(self) -> bool:
        return isinstance(self, JSON_mGrammar.jKeyValue_KeyValue)

class jKeyValue_KeyValue(jKeyValue, NamedTuple('KeyValue', [('k', Any), ('colon', Any), ('v', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.jKeyValue.KeyValue({_dafny.string_of(self.k)}, {_dafny.string_of(self.colon)}, {_dafny.string_of(self.v)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.jKeyValue_KeyValue) and self.k == __o.k and self.colon == __o.colon and self.v == __o.v
    def __hash__(self) -> int:
        return super().__hash__()


class jfrac:
    @classmethod
    def default(cls, ):
        return lambda: jfrac_JFrac(JSON_mGrammar.jperiod.default(), JSON_mGrammar.jnum.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_JFrac(self) -> bool:
        return isinstance(self, JSON_mGrammar.jfrac_JFrac)

class jfrac_JFrac(jfrac, NamedTuple('JFrac', [('period', Any), ('num', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.jfrac.JFrac({_dafny.string_of(self.period)}, {_dafny.string_of(self.num)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.jfrac_JFrac) and self.period == __o.period and self.num == __o.num
    def __hash__(self) -> int:
        return super().__hash__()


class jexp:
    @classmethod
    def default(cls, ):
        return lambda: jexp_JExp(JSON_mGrammar.je.default(), JSON_mGrammar.jsign.default(), JSON_mGrammar.jnum.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_JExp(self) -> bool:
        return isinstance(self, JSON_mGrammar.jexp_JExp)

class jexp_JExp(jexp, NamedTuple('JExp', [('e', Any), ('sign', Any), ('num', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.jexp.JExp({_dafny.string_of(self.e)}, {_dafny.string_of(self.sign)}, {_dafny.string_of(self.num)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.jexp_JExp) and self.e == __o.e and self.sign == __o.sign and self.num == __o.num
    def __hash__(self) -> int:
        return super().__hash__()


class jnumber:
    @classmethod
    def default(cls, ):
        return lambda: jnumber_JNumber(JSON_mGrammar.jminus.default(), JSON_mGrammar.jnum.default(), JSON_mGrammar.Maybe_Empty.default()(), JSON_mGrammar.Maybe_Empty.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_JNumber(self) -> bool:
        return isinstance(self, JSON_mGrammar.jnumber_JNumber)

class jnumber_JNumber(jnumber, NamedTuple('JNumber', [('minus', Any), ('num', Any), ('frac', Any), ('exp', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.jnumber.JNumber({_dafny.string_of(self.minus)}, {_dafny.string_of(self.num)}, {_dafny.string_of(self.frac)}, {_dafny.string_of(self.exp)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.jnumber_JNumber) and self.minus == __o.minus and self.num == __o.num and self.frac == __o.frac and self.exp == __o.exp
    def __hash__(self) -> int:
        return super().__hash__()


class Value:
    @classmethod
    def default(cls, ):
        return lambda: Value_Null(JSON_mGrammar.jnull.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Null(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_Null)
    @property
    def is_Bool(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_Bool)
    @property
    def is_String(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_String)
    @property
    def is_Number(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_Number)
    @property
    def is_Object(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_Object)
    @property
    def is_Array(self) -> bool:
        return isinstance(self, JSON_mGrammar.Value_Array)

class Value_Null(Value, NamedTuple('Null', [('n', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.Null({_dafny.string_of(self.n)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_Null) and self.n == __o.n
    def __hash__(self) -> int:
        return super().__hash__()

class Value_Bool(Value, NamedTuple('Bool', [('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.Bool({_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_Bool) and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class Value_String(Value, NamedTuple('String', [('str', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.String({_dafny.string_of(self.str)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_String) and self.str == __o.str
    def __hash__(self) -> int:
        return super().__hash__()

class Value_Number(Value, NamedTuple('Number', [('num', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.Number({_dafny.string_of(self.num)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_Number) and self.num == __o.num
    def __hash__(self) -> int:
        return super().__hash__()

class Value_Object(Value, NamedTuple('Object', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.Object({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_Object) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()

class Value_Array(Value, NamedTuple('Array', [('arr', Any)])):
    def __dafnystr__(self) -> str:
        return f'Grammar.Value.Array({_dafny.string_of(self.arr)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mGrammar.Value_Array) and self.arr == __o.arr
    def __hash__(self) -> int:
        return super().__hash__()

