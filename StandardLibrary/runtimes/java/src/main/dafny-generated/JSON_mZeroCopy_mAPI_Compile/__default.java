// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mAPI_Compile;

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
import JSON_mZeroCopy_mDeserializer_mArrayParams_Compile.*;
import JSON_mZeroCopy_mDeserializer_mArrays_Compile.*;
import JSON_mZeroCopy_mDeserializer_mConstants_Compile.*;
import JSON_mZeroCopy_mDeserializer_mValues_Compile.*;
import JSON_mZeroCopy_mDeserializer_mAPI_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Serialize(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), (JSON_mZeroCopy_mSerializer_Compile.__default.Text(js)).Bytes());
  }
  public static Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> SerializeAlloc(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js)
  {
    Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> bs = Wrappers_Compile.Result.<byte[], JSON_mErrors_Compile.SerializationError>Default(dafny.TypeDescriptor.BYTE_ARRAY, JSON_mErrors_Compile.SerializationError._typeDescriptor(), new byte[0]);
    if(true) {
      Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mSerializer_Compile.__default.Serialize(js);
      bs = _out0;
    }
    return bs;
  }
  public static Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> SerializeInto(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js, byte[] bs)
  {
    Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> len = Wrappers_Compile.Result.<java.lang.Integer, JSON_mErrors_Compile.SerializationError>Default(BoundedInts_Compile.uint32._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), 0);
    if(true) {
      Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mSerializer_Compile.__default.SerializeTo(js, bs);
      len = _out0;
    }
    return len;
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError> Deserialize(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    return JSON_mZeroCopy_mDeserializer_mAPI_Compile.__default.OfBytes(bs);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.API._default";
  }
}
