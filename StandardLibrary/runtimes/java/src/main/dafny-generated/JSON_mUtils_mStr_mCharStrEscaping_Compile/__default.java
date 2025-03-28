// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mStr_mCharStrEscaping_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;
import Utf16EncodingForm_Compile.*;
import UnicodeStrings_Compile.*;
import FileIO_Compile.*;
import MulInternals_Compile.*;
import ModInternals_Compile.*;
import DivInternals_Compile.*;
import Power_Compile.*;
import Logarithm_Compile.*;
import StandardLibraryInterop_Compile.*;
import StandardLibrary_mUInt_Compile.*;
import StandardLibrary_mSequence_Compile.*;
import StandardLibrary_mString_Compile.*;
import StandardLibrary_Compile.*;
import UUID.*;
import UTF8.*;
import OsLang.*;
import Time.*;
import Streams_Compile.*;
import Sorting_Compile.*;
import HexStrings_Compile.*;
import GetOpt_Compile.*;
import FloatCompare_Compile.*;
import ConcurrentCall.*;
import Base64_Compile.*;
import Actions_Compile.*;
import DafnyLibraries.*;
import JSON_mUtils_mViews_mCore_Compile.*;
import JSON_mUtils_mViews_mWriters_Compile.*;
import JSON_mUtils_mLexers_mCore_Compile.*;
import JSON_mUtils_mLexers_mStrings_Compile.*;
import JSON_mUtils_mCursors_Compile.*;
import JSON_mUtils_mParsers_Compile.*;
import JSON_mUtils_mStr_mCharStrConversion_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> Escape(dafny.DafnySequence<? extends Character> str, dafny.DafnySet<? extends Character> special, char escape)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((str).equals(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR))) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, str);
      } else if ((special).<Character>contains(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> of(escape, ((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))));
        dafny.DafnySequence<? extends Character> _in0 = (str).drop(java.math.BigInteger.ONE);
        dafny.DafnySet<? extends Character> _in1 = special;
        char _in2 = escape;
        str = _in0;
        special = _in1;
        escape = _in2;
        continue TAIL_CALL_START;
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))));
        dafny.DafnySequence<? extends Character> _in3 = (str).drop(java.math.BigInteger.ONE);
        dafny.DafnySet<? extends Character> _in4 = special;
        char _in5 = escape;
        str = _in3;
        special = _in4;
        escape = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, UnescapeError> Unescape(dafny.DafnySequence<? extends Character> str, char escape)
  {
    if ((str).equals(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR))) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, UnescapeError>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), str);
    } else if ((((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == (escape)) {
      if ((java.math.BigInteger.valueOf((str).length())).compareTo(java.math.BigInteger.ONE) > 0) {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, UnescapeError> _0_valueOrError0 = __default.Unescape((str).drop(java.math.BigInteger.valueOf(2L)), escape);
        if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor())) {
          return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        } else {
          dafny.DafnySequence<? extends Character> _1_tl = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor());
          return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, UnescapeError>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), _1_tl));
        }
      } else {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, UnescapeError>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), JSON_mUtils_mStr_mCharStrEscaping_Compile.UnescapeError.create());
      }
    } else {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, UnescapeError> _2_valueOrError1 = __default.Unescape((str).drop(java.math.BigInteger.ONE), escape);
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor())) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      } else {
        dafny.DafnySequence<? extends Character> _3_tl = (_2_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor());
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, UnescapeError>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UnescapeError._typeDescriptor(), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), _3_tl));
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Str.CharStrEscaping._default";
  }
}
