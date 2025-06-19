// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mNumbers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> Digits(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    return ((cs).SkipWhile(JSON_mGrammar_Compile.__default::Digit_q)).Split();
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> NonEmptyDigits(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _0_sp = __default.Digits(cs);
    Wrappers_Compile.Outcome<JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _1_valueOrError0 = Wrappers_Compile.__default.<JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>Need(JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), !(((_0_sp).dtor_t()).Empty_q()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>create_OtherError(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_EmptyNumber()));
    if ((_1_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_1_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jdigits._typeDescriptor()));
    } else {
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jdigits._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), _0_sp);
    }
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> NonZeroInt(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    return __default.NonEmptyDigits(cs);
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> OptionalMinus(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    return ((cs).SkipIf(((java.util.function.Function<java.lang.Byte, Boolean>)(_0_c_boxed0) -> {
      byte _0_c = ((byte)(java.lang.Object)(_0_c_boxed0));
      return (_0_c) == (((byte) ('-')));
    }))).Split();
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> OptionalSign(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    return ((cs).SkipIf(((java.util.function.Function<java.lang.Byte, Boolean>)(_0_c_boxed0) -> {
      byte _0_c = ((byte)(java.lang.Object)(_0_c_boxed0));
      return ((_0_c) == (((byte) ('-')))) || ((_0_c) == (((byte) ('+'))));
    }))).Split();
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> TrimmedInt(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _0_sp = ((cs).SkipIf(((java.util.function.Function<java.lang.Byte, Boolean>)(_1_c_boxed0) -> {
      byte _1_c = ((byte)(java.lang.Object)(_1_c_boxed0));
      return (_1_c) == (((byte) ('0')));
    }))).Split();
    if (((_0_sp).dtor_t()).Empty_q()) {
      return __default.NonZeroInt((_0_sp).dtor_cs());
    } else {
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), _0_sp);
    }
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Exp(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs0 = ((cs).SkipIf(((java.util.function.Function<java.lang.Byte, Boolean>)(_0_c_boxed0) -> {
      byte _0_c = ((byte)(java.lang.Object)(_0_c_boxed0));
      return ((_0_c) == (((byte) ('e')))) || ((_0_c) == (((byte) ('E'))));
    }))).Split();
    JSON_mUtils_mViews_mCore_Compile.View__ _1_e = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _2_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._cs;
    if ((_1_e).Empty_q()) {
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>create(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>create_Empty(JSON_mGrammar_Compile.jexp._typeDescriptor()), _2_cs));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs1 = __default.OptionalSign(_2_cs);
      JSON_mUtils_mViews_mCore_Compile.View__ _3_sign = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._t;
      JSON_mUtils_mCursors_Compile.Cursor__ _4_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._cs;
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _5_valueOrError0 = __default.NonEmptyDigits(_4_cs);
      if ((_5_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_5_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())));
      } else {
        JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs2 = (_5_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        JSON_mUtils_mViews_mCore_Compile.View__ _6_num = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._t;
        JSON_mUtils_mCursors_Compile.Cursor__ _7_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._cs;
        return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>create(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>create_NonEmpty(JSON_mGrammar_Compile.jexp._typeDescriptor(), JSON_mGrammar_Compile.jexp.create(_1_e, _3_sign, _6_num)), _7_cs));
      }
    }
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Frac(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs0 = ((cs).SkipIf(((java.util.function.Function<java.lang.Byte, Boolean>)(_0_c_boxed0) -> {
      byte _0_c = ((byte)(java.lang.Object)(_0_c_boxed0));
      return (_0_c) == (((byte) ('.')));
    }))).Split();
    JSON_mUtils_mViews_mCore_Compile.View__ _1_period = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _2_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._cs;
    if ((_1_period).Empty_q()) {
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>create(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor()), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>create_Empty(JSON_mGrammar_Compile.jfrac._typeDescriptor()), _2_cs));
    } else {
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _3_valueOrError0 = __default.NonEmptyDigits(_2_cs);
      if ((_3_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_3_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())));
      } else {
        JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs1 = (_3_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jnum._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        JSON_mUtils_mViews_mCore_Compile.View__ _4_num = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._t;
        JSON_mUtils_mCursors_Compile.Cursor__ _5_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._cs;
        return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>create(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor()), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>create_NonEmpty(JSON_mGrammar_Compile.jfrac._typeDescriptor(), JSON_mGrammar_Compile.jfrac.create(_1_period, _4_num)), _5_cs));
      }
    }
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber> NumberFromParts(JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> minus, JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> num, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>> frac, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>> exp)
  {
    JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber> _0_sp = JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jnumber>create(JSON_mGrammar_Compile.jnumber._typeDescriptor(), JSON_mGrammar_Compile.jnumber.create((minus).dtor_t(), (num).dtor_t(), (frac).dtor_t(), (exp).dtor_t()), (exp).dtor_cs());
    return _0_sp;
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Number(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _0_minus = __default.OptionalMinus(cs);
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _1_valueOrError0 = __default.TrimmedInt((_0_minus).dtor_cs());
    if ((_1_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jint._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_1_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jint._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jnumber>_typeDescriptor(JSON_mGrammar_Compile.jnumber._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _2_num = (_1_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jint._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _3_valueOrError1 = __default.Frac((_2_num).dtor_cs());
      if ((_3_valueOrError1).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_3_valueOrError1).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jnumber>_typeDescriptor(JSON_mGrammar_Compile.jnumber._typeDescriptor()));
      } else {
        JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>> _4_frac = (_3_valueOrError1).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>_typeDescriptor(JSON_mGrammar_Compile.jfrac._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _5_valueOrError2 = __default.Exp((_4_frac).dtor_cs());
        if ((_5_valueOrError2).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
          return (_5_valueOrError2).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jnumber>_typeDescriptor(JSON_mGrammar_Compile.jnumber._typeDescriptor()));
        } else {
          JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>> _6_exp = (_5_valueOrError2).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>_typeDescriptor(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
          return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jnumber>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jnumber>_typeDescriptor(JSON_mGrammar_Compile.jnumber._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), __default.NumberFromParts(_0_minus, _2_num, _4_frac, _6_exp));
        }
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.Numbers._default";
  }
}
