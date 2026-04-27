// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mAPI_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static JSON_mErrors_Compile.DeserializationError LiftCursorError(JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError> err) {
    JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError> _source0 = err;
    if (_source0.is_EOF()) {
      return JSON_mErrors_Compile.DeserializationError.create_ReachedEOF();
    } else if (_source0.is_ExpectingByte()) {
      byte _0___mcc_h0 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingByte<JSON_mErrors_Compile.DeserializationError>)_source0)._expected;
      short _1___mcc_h1 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingByte<JSON_mErrors_Compile.DeserializationError>)_source0)._b;
      short _2_b = _1___mcc_h1;
      byte _3_expected = _0___mcc_h0;
      return JSON_mErrors_Compile.DeserializationError.create_ExpectingByte(_3_expected, _2_b);
    } else if (_source0.is_ExpectingAnyByte()) {
      dafny.DafnySequence<? extends java.lang.Byte> _4___mcc_h2 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingAnyByte<JSON_mErrors_Compile.DeserializationError>)_source0)._expected__sq;
      short _5___mcc_h3 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingAnyByte<JSON_mErrors_Compile.DeserializationError>)_source0)._b;
      short _6_b = _5___mcc_h3;
      dafny.DafnySequence<? extends java.lang.Byte> _7_expected__sq = _4___mcc_h2;
      return JSON_mErrors_Compile.DeserializationError.create_ExpectingAnyByte(_7_expected__sq, _6_b);
    } else {
      JSON_mErrors_Compile.DeserializationError _8___mcc_h4 = ((JSON_mUtils_mCursors_Compile.CursorError_OtherError<JSON_mErrors_Compile.DeserializationError>)_source0)._err;
      JSON_mErrors_Compile.DeserializationError _9_err = _8___mcc_h4;
      return _9_err;
    }
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>, JSON_mErrors_Compile.DeserializationError> JSON(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    return (JSON_mZeroCopy_mDeserializer_mCore_Compile.__default.<JSON_mGrammar_Compile.Value>Structural(JSON_mGrammar_Compile.Value._typeDescriptor(), cs, JSON_mUtils_mParsers_Compile.Parser__.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.DeserializationError>create(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mZeroCopy_mDeserializer_mValues_Compile.__default::Value))).<JSON_mErrors_Compile.DeserializationError>MapFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), __default::LiftCursorError);
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError> Text(JSON_mUtils_mViews_mCore_Compile.View__ v) {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>, JSON_mErrors_Compile.DeserializationError> _0_valueOrError0 = __default.JSON(JSON_mUtils_mCursors_Compile.Cursor__.OfView(v));
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>> _let_tmp_rhs0 = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
      JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> _1_text = ((JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>)_let_tmp_rhs0)._t;
      JSON_mUtils_mCursors_Compile.Cursor__ _2_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>)_let_tmp_rhs0)._cs;
      Wrappers_Compile.Outcome<JSON_mErrors_Compile.DeserializationError> _3_valueOrError1 = Wrappers_Compile.__default.<JSON_mErrors_Compile.DeserializationError>Need(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), (_2_cs).EOF_q(), JSON_mErrors_Compile.DeserializationError.create_ExpectingEOF());
      if ((_3_valueOrError1).IsFailure(JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_3_valueOrError1).<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>PropagateFailure(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()));
      } else {
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), _1_text);
      }
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError> OfBytes(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    Wrappers_Compile.Outcome<JSON_mErrors_Compile.DeserializationError> _0_valueOrError0 = Wrappers_Compile.__default.<JSON_mErrors_Compile.DeserializationError>Need(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), (java.math.BigInteger.valueOf((bs).length())).compareTo(BoundedInts_Compile.__default.TWO__TO__THE__32()) < 0, JSON_mErrors_Compile.DeserializationError.create_IntOverflow());
    if ((_0_valueOrError0).IsFailure(JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>PropagateFailure(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()));
    } else {
      return __default.Text(JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(bs));
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.API._default";
  }
}
