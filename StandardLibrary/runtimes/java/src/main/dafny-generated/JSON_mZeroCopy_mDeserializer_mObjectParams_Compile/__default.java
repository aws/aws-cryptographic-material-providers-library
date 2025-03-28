// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mObjectParams_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Colon(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = (cs).<JSON_mErrors_Compile.DeserializationError>AssertChar(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), ':');
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), (_1_cs).Split());
    }
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> KeyValueFromParts(JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring> k, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> colon, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value> v)
  {
    JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> _0_sp = JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>create(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue.create((k).dtor_t(), (colon).dtor_t(), (v).dtor_t()), (v).dtor_cs());
    return _0_sp;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ElementSpec(JSON_mGrammar_Compile.jKeyValue t) {
    return JSON_mConcreteSyntax_mSpec_Compile.__default.KeyValue(t);
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Element(JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mUtils_mParsers_Compile.SubParser__<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.DeserializationError> json)
  {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = JSON_mZeroCopy_mDeserializer_mStrings_Compile.__default.String(cs);
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring> _1_k = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      JSON_mUtils_mParsers_Compile.Parser__<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.DeserializationError> _2_p = JSON_mUtils_mParsers_Compile.Parser__.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.DeserializationError>create(JSON_mGrammar_Compile.jcolon._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), __default::Colon);
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _3_valueOrError1 = JSON_mZeroCopy_mDeserializer_mCore_Compile.__default.<JSON_mUtils_mViews_mCore_Compile.View__>Structural(JSON_mGrammar_Compile.jcolon._typeDescriptor(), (_1_k).dtor_cs(), _2_p);
      if ((_3_valueOrError1).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_3_valueOrError1).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
      } else {
        JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> _4_colon = (_3_valueOrError1).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _5_valueOrError2 = ((Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>)(java.lang.Object)(((json).dtor_fn()).apply((_4_colon).dtor_cs())));
        if ((_5_valueOrError2).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
          return (_5_valueOrError2).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
        } else {
          JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value> _6_v = (_5_valueOrError2).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
          JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> _7_kv = __default.KeyValueFromParts(_1_k, _4_colon, _6_v);
          return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), _7_kv);
        }
      }
    }
  }
  public static byte OPEN()
  {
    return ((byte) ('{'));
  }
  public static byte CLOSE()
  {
    return ((byte) ('}'));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.ObjectParams._default";
  }
}
