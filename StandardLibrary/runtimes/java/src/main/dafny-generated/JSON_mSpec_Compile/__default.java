// Class __default
// Dafny class __default compiled into Java
package JSON_mSpec_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Short> EscapeUnicode(short c) {
    dafny.DafnySequence<? extends Character> _0_sStr = JSON_mUtils_mStr_Compile.__default.OfNat(dafny.Helpers.unsignedToBigInteger(c), java.math.BigInteger.valueOf(16L));
    dafny.DafnySequence<? extends java.lang.Short> _1_s = UnicodeStrings_Compile.__default.ASCIIToUTF16(_0_sStr);
    return dafny.DafnySequence.<java.lang.Short>concatenate(dafny.DafnySequence.Create(BoundedInts_Compile.uint16._typeDescriptor(), (java.math.BigInteger.valueOf(4L)).subtract(java.math.BigInteger.valueOf((_1_s).length())), ((java.util.function.Function<java.math.BigInteger, java.lang.Short>)(_2___v0_boxed0) -> {
      java.math.BigInteger _2___v0 = ((java.math.BigInteger)(java.lang.Object)(_2___v0_boxed0));
      return ((short) ('0'));
    })), _1_s);
  }
  public static dafny.DafnySequence<? extends java.lang.Short> Escape(dafny.DafnySequence<? extends java.lang.Short> str, java.math.BigInteger start)
  {
    dafny.DafnySequence<? extends java.lang.Short> _0___accumulator = dafny.DafnySequence.<java.lang.Short> empty(BoundedInts_Compile.uint16._typeDescriptor());
    TAIL_CALL_START: while (true) {
      dafny.DafnySequence<? extends java.lang.Short> _pat_let_tv0 = str;
      java.math.BigInteger _pat_let_tv1 = start;
      if ((start).compareTo(java.math.BigInteger.valueOf((str).length())) >= 0) {
        return dafny.DafnySequence.<java.lang.Short>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Short> empty(BoundedInts_Compile.uint16._typeDescriptor()));
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Short>concatenate(_0___accumulator, (((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 34)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\\""))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 92)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\\\"))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 8)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\b"))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 12)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\f"))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 10)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\n"))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 13)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\r"))) : ((((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == ((short) 9)) ? (UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\t"))) : (((dafny.DafnySequence<? extends java.lang.Short>)(java.lang.Object)(dafny.Helpers.<java.lang.Short, dafny.DafnySequence<? extends java.lang.Short>>Let(((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start))))), boxed10 -> {
          short _pat_let5_0 = ((short)(java.lang.Object)(boxed10));
          return ((dafny.DafnySequence<? extends java.lang.Short>)(java.lang.Object)(dafny.Helpers.<java.lang.Short, dafny.DafnySequence<? extends java.lang.Short>>Let(_pat_let5_0, boxed11 -> {
            short _1_c = ((short)(java.lang.Object)(boxed11));
            return ((java.lang.Integer.compareUnsigned(_1_c, (short) 31) < 0) ? (dafny.DafnySequence.<java.lang.Short>concatenate(UnicodeStrings_Compile.__default.ASCIIToUTF16(dafny.DafnySequence.asString("\\u")), __default.EscapeUnicode(_1_c))) : (dafny.DafnySequence.<java.lang.Short> of(((short)(java.lang.Object)((_pat_let_tv0).select(dafny.Helpers.toInt((_pat_let_tv1))))))));
          }
          )));
        }
        ))))))))))))))))));
        dafny.DafnySequence<? extends java.lang.Short> _in0 = str;
        java.math.BigInteger _in1 = (start).add(java.math.BigInteger.ONE);
        str = _in0;
        start = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> EscapeToUTF8(dafny.DafnySequence<? extends Character> str, java.math.BigInteger start)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = (UnicodeStrings_Compile.__default.ToUTF16Checked(str)).<JSON_mErrors_Compile.SerializationError>ToResult_k(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mErrors_Compile.SerializationError.create_InvalidUnicode());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Short> _1_utf16 = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Short> _2_escaped = __default.Escape(_1_utf16, java.math.BigInteger.ZERO);
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mErrors_Compile.SerializationError> _3_valueOrError1 = (UnicodeStrings_Compile.__default.FromUTF16Checked(_2_escaped)).<JSON_mErrors_Compile.SerializationError>ToResult_k(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mErrors_Compile.SerializationError.create_InvalidUnicode());
      if ((_3_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_3_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        dafny.DafnySequence<? extends Character> _4_utf32 = (_3_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return (UnicodeStrings_Compile.__default.ToUTF8Checked(_4_utf32)).<JSON_mErrors_Compile.SerializationError>ToResult_k(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mErrors_Compile.SerializationError.create_InvalidUnicode());
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> String(dafny.DafnySequence<? extends Character> str) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.EscapeToUTF8(str, java.math.BigInteger.ZERO);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _1_inBytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("\"")), _1_inBytes), UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("\""))));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> IntToBytes(java.math.BigInteger n) {
    dafny.DafnySequence<? extends Character> _0_s = JSON_mUtils_mStr_Compile.__default.OfInt(n, java.math.BigInteger.valueOf(10L));
    return UnicodeStrings_Compile.__default.ASCIIToUTF8(_0_s);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Number(JSON_mValues_Compile.Decimal dec) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(__default.IntToBytes((dec).dtor_n()), ((((dec).dtor_e10()).signum() == 0) ? (dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor())) : (dafny.DafnySequence.<java.lang.Byte>concatenate(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("e")), __default.IntToBytes((dec).dtor_e10()))))));
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> KeyValue(dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> kv) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.String((kv).dtor__0());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _1_key = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _2_valueOrError1 = __default.JSON((kv).dtor__1());
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _3_value = (_2_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_1_key, UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString(":"))), _3_value));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Join(dafny.DafnySequence<? extends java.lang.Byte> sep, dafny.DafnySequence<? extends Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>> items)
  {
    if ((java.math.BigInteger.valueOf((items).length())).signum() == 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)((items).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _1_first = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        if (java.util.Objects.equals(java.math.BigInteger.valueOf((items).length()), java.math.BigInteger.ONE)) {
          return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), _1_first);
        } else {
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _2_valueOrError1 = __default.Join(sep, (items).drop(java.math.BigInteger.ONE));
          if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
            return (_2_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
          } else {
            dafny.DafnySequence<? extends java.lang.Byte> _3_rest = (_2_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
            return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_1_first, sep), _3_rest));
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Object(dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.Join(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString(",")), dafny.DafnySequence.Create(Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor()), java.math.BigInteger.valueOf((obj).length()), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>>>)(_1_obj) -> ((java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>>)(_2_i_boxed0) -> {
      java.math.BigInteger _2_i = ((java.math.BigInteger)(java.lang.Object)(_2_i_boxed0));
      return __default.KeyValue(((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((_1_obj).select(dafny.Helpers.toInt((_2_i))))));
    })).apply(obj)));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _3_middle = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("{")), _3_middle), UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("}"))));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Array(dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> arr) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.Join(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString(",")), dafny.DafnySequence.Create(Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor()), java.math.BigInteger.valueOf((arr).length()), ((java.util.function.Function<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>>>)(_1_arr) -> ((java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>>)(_2_i_boxed0) -> {
      java.math.BigInteger _2_i = ((java.math.BigInteger)(java.lang.Object)(_2_i_boxed0));
      return __default.JSON(((JSON_mValues_Compile.JSON)(java.lang.Object)((_1_arr).select(dafny.Helpers.toInt((_2_i))))));
    })).apply(arr)));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _3_middle = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("[")), _3_middle), UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("]"))));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> JSON(JSON_mValues_Compile.JSON js) {
    JSON_mValues_Compile.JSON _source0 = js;
    if (_source0.is_Null()) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("null")));
    } else if (_source0.is_Bool()) {
      boolean _0___mcc_h0 = ((JSON_mValues_Compile.JSON_Bool)_source0)._b;
      boolean _1_b = _0___mcc_h0;
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), ((_1_b) ? (UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("true"))) : (UnicodeStrings_Compile.__default.ASCIIToUTF8(dafny.DafnySequence.asString("false")))));
    } else if (_source0.is_String()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((JSON_mValues_Compile.JSON_String)_source0)._str;
      dafny.DafnySequence<? extends Character> _3_str = _2___mcc_h1;
      return __default.String(_3_str);
    } else if (_source0.is_Number()) {
      JSON_mValues_Compile.Decimal _4___mcc_h2 = ((JSON_mValues_Compile.JSON_Number)_source0)._num;
      JSON_mValues_Compile.Decimal _5_dec = _4___mcc_h2;
      return __default.Number(_5_dec);
    } else if (_source0.is_Object()) {
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _6___mcc_h3 = ((JSON_mValues_Compile.JSON_Object)_source0)._obj;
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _7_obj = _6___mcc_h3;
      return __default.Object(_7_obj);
    } else {
      dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _8___mcc_h4 = ((JSON_mValues_Compile.JSON_Array)_source0)._arr;
      dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _9_arr = _8___mcc_h4;
      return __default.Array(_9_arr);
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Spec._default";
  }
}
