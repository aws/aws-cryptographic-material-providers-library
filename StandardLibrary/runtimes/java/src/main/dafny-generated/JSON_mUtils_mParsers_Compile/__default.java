// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mParsers_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T, __R> Parser__<__T, __R> ParserWitness(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R)
  {
    return JSON_mUtils_mParsers_Compile.Parser__.<__T, __R>create(_td___T, _td___R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>>)(_0___v0_boxed0) -> {
  JSON_mUtils_mCursors_Compile.Cursor__ _0___v0 = ((JSON_mUtils_mCursors_Compile.Cursor__)(java.lang.Object)(_0___v0_boxed0));
  return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>create_Failure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<__R>_typeDescriptor(_td___R), JSON_mUtils_mCursors_Compile.CursorError.<__R>create_EOF(_td___R));
}));
  }
  public static <__T, __R> SubParser__<__T, __R> SubParserWitness(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R)
  {
    return JSON_mUtils_mParsers_Compile.SubParser__.<__T, __R>create(_td___T, _td___R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>>)(_0_cs_boxed0) -> {
  JSON_mUtils_mCursors_Compile.Cursor__ _0_cs = ((JSON_mUtils_mCursors_Compile.Cursor__)(java.lang.Object)(_0_cs_boxed0));
  return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>create_Failure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<__R>_typeDescriptor(_td___R), JSON_mUtils_mCursors_Compile.CursorError.<__R>create_EOF(_td___R));
}));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Parsers._default";
  }
}
