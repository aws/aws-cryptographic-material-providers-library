// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mArrayParams_Compile;

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
import JSON_mGrammar_Compile.*;
import JSON_mSerializer_mByteStrConversion_Compile.*;
import JSON_mSerializer_Compile.*;
import JSON_mDeserializer_mUint16StrConversion_Compile.*;
import JSON_mDeserializer_mByteStrConversion_Compile.*;
import JSON_mDeserializer_Compile.*;
import JSON_mConcreteSyntax_mSpec_Compile.*;
import JSON_mZeroCopy_mSerializer_Compile.*;
import JSON_mZeroCopy_mDeserializer_mCore_Compile.*;
import JSON_mZeroCopy_mDeserializer_mStrings_Compile.*;
import JSON_mZeroCopy_mDeserializer_mNumbers_Compile.*;
import JSON_mZeroCopy_mDeserializer_mObjectParams_Compile.*;
import JSON_mZeroCopy_mDeserializer_mObjects_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ElementSpec(JSON_mGrammar_Compile.Value t) {
    return JSON_mConcreteSyntax_mSpec_Compile.__default.Value(t);
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Element(JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mUtils_mParsers_Compile.SubParser__<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.DeserializationError> json)
  {
    return ((Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>)(java.lang.Object)(((json).dtor_fn()).apply(cs)));
  }
  public static byte OPEN()
  {
    return ((byte) ('['));
  }
  public static byte CLOSE()
  {
    return ((byte) (']'));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.ArrayParams._default";
  }
}
