// Class __default
// Dafny class __default compiled into Java
package JSON_mGrammar_Compile;

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
import JSON_mUtils_mStr_mCharStrEscaping_Compile.*;
import JSON_mUtils_mStr_Compile.*;
import JSON_mUtils_mVectors_Compile.*;
import JSON_mErrors_Compile.*;
import JSON_mValues_Compile.*;
import JSON_mSpec_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean Blank_q(byte b) {
    return ((((b) == ((byte) 32)) || ((b) == ((byte) 9))) || ((b) == ((byte) 10))) || ((b) == ((byte) 13));
  }
  public static boolean Digit_q(byte b) {
    return (java.lang.Integer.compareUnsigned(((byte) ('0')), b) <= 0) && (java.lang.Integer.compareUnsigned(b, ((byte) ('9'))) <= 0);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> NULL()
  {
    return dafny.DafnySequence.<java.lang.Byte> of(((byte) ('n')), ((byte) ('u')), ((byte) ('l')), ((byte) ('l')));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> TRUE()
  {
    return dafny.DafnySequence.<java.lang.Byte> of(((byte) ('t')), ((byte) ('r')), ((byte) ('u')), ((byte) ('e')));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> FALSE()
  {
    return dafny.DafnySequence.<java.lang.Byte> of(((byte) ('f')), ((byte) ('a')), ((byte) ('l')), ((byte) ('s')), ((byte) ('e')));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ DOUBLEQUOTE()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('\"'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ PERIOD()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('.'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ E()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('e'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ COLON()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) (':'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ COMMA()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) (','))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ LBRACE()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('{'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ RBRACE()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('}'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ LBRACKET()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('['))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ RBRACKET()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) (']'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ MINUS()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('-'))));
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ EMPTY()
  {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Grammar._default";
  }
}
