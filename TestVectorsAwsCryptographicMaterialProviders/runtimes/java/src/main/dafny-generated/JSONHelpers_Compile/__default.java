// Class __default
// Dafny class __default compiled into Java
package JSONHelpers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> Get(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((obj).length())).signum() == 0) {
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>create_Failure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Key: "), key), dafny.DafnySequence.asString(" does not exist")));
      } else if (((((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((obj).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor__0()).equals(key)) {
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((obj).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor__1());
      } else {
        dafny.DafnySequence<? extends Character> _in0 = key;
        dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _in1 = (obj).drop(java.math.BigInteger.ONE);
        key = _in0;
        obj = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> GetString(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).is_String(), dafny.DafnySequence.asString("Not a string"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      } else {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).dtor_str());
      }
    }
  }
  public static Wrappers_Compile.Result<Boolean, dafny.DafnySequence<? extends Character>> GetBool(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<Boolean>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BOOLEAN);
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).is_Bool(), dafny.DafnySequence.asString("Not a bool"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<Boolean>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BOOLEAN);
      } else {
        return Wrappers_Compile.Result.<Boolean, dafny.DafnySequence<? extends Character>>create_Success(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).dtor_b());
      }
    }
  }
  public static Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> GetNat(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<java.math.BigInteger>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BIG_INTEGER);
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).is_Number(), dafny.DafnySequence.asString("Not a number"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<java.math.BigInteger>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BIG_INTEGER);
      } else {
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (((_1_obj).dtor_num()).dtor_n()).signum() == 1, dafny.DafnySequence.asString("Not a nat"));
        if ((_3_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_3_valueOrError2).<java.math.BigInteger>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.TypeDescriptor.BIG_INTEGER);
        } else {
          return Wrappers_Compile.Result.<java.math.BigInteger, dafny.DafnySequence<? extends Character>>create_Success(dafny.TypeDescriptor.BIG_INTEGER, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_1_obj).dtor_num()).dtor_n());
        }
      }
    }
  }
  public static Wrappers_Compile.Result<java.lang.Long, dafny.DafnySequence<? extends Character>> GetPositiveLong(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.GetNat(key, obj);
    if ((_0_valueOrError0).IsFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<java.lang.Long>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.int64._typeDescriptor());
    } else {
      java.math.BigInteger _1_n = (_0_valueOrError0).Extract(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_n).compareTo(java.math.BigInteger.valueOf(BoundedInts_Compile.__default.INT64__MAX())) <= 0, dafny.DafnySequence.asString("Int64 Overflow"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<java.lang.Long>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.int64._typeDescriptor());
      } else {
        return Wrappers_Compile.Result.<java.lang.Long, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.int64._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_n).longValue());
      }
    }
  }
  public static Wrappers_Compile.Result<java.lang.Integer, dafny.DafnySequence<? extends Character>> GetPositiveInteger(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.GetNat(key, obj);
    if ((_0_valueOrError0).IsFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<java.lang.Integer>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.int32._typeDescriptor());
    } else {
      java.math.BigInteger _1_n = (_0_valueOrError0).Extract(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_n).compareTo(java.math.BigInteger.valueOf(BoundedInts_Compile.__default.INT32__MAX())) <= 0, dafny.DafnySequence.asString("Int32 Overflow"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<java.lang.Integer>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.int32._typeDescriptor());
      } else {
        return Wrappers_Compile.Result.<java.lang.Integer, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.int32._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_n).intValue());
      }
    }
  }
  public static Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> GetOptionalString(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Option<JSON_mValues_Compile.JSON> _0_obj = (__default.Get(key, obj)).ToOption(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if ((_0_obj).is_Some()) {
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_0_obj).dtor_value()).is_String(), dafny.DafnySequence.asString("Not a string"));
      if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_1_valueOrError0).<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      } else {
        return Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_0_obj).dtor_value()).dtor_str()));
      }
    } else {
      return Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    }
  }
  public static Wrappers_Compile.Result<Wrappers_Compile.Option<java.lang.Long>, dafny.DafnySequence<? extends Character>> GetOptionalPositiveLong(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Option<JSON_mValues_Compile.JSON> _0_obj = (__default.Get(key, obj)).ToOption(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if ((_0_obj).is_Some()) {
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_0_obj).dtor_value()).is_Number(), dafny.DafnySequence.asString("Not a number"));
      if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_1_valueOrError0).<Wrappers_Compile.Option<java.lang.Long>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>_typeDescriptor(BoundedInts_Compile.int64._typeDescriptor()));
      } else {
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (((((_0_obj).dtor_value()).dtor_num()).dtor_n()).signum() != -1) && (((((_0_obj).dtor_value()).dtor_num()).dtor_n()).compareTo(java.math.BigInteger.valueOf(BoundedInts_Compile.__default.INT64__MAX())) <= 0), dafny.DafnySequence.asString("Int64 Overflow"));
        if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_2_valueOrError1).<Wrappers_Compile.Option<java.lang.Long>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>_typeDescriptor(BoundedInts_Compile.int64._typeDescriptor()));
        } else {
          return Wrappers_Compile.Result.<Wrappers_Compile.Option<java.lang.Long>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<java.lang.Long>_typeDescriptor(BoundedInts_Compile.int64._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>create_Some(BoundedInts_Compile.int64._typeDescriptor(), ((((_0_obj).dtor_value()).dtor_num()).dtor_n()).longValue()));
        }
      }
    } else {
      return Wrappers_Compile.Result.<Wrappers_Compile.Option<java.lang.Long>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<java.lang.Long>_typeDescriptor(BoundedInts_Compile.int64._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>> GetObject(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())));
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).is_Object(), dafny.DafnySequence.asString("Not an object"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())));
      } else {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).dtor_obj());
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, dafny.DafnySequence<? extends Character>> GetArray(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()));
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).is_Array(), dafny.DafnySequence.asString("Not an array"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()));
      } else {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_obj).dtor_arr());
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> GetArrayString(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_1_obj).is_Array()) && (((java.util.function.Function<JSON_mValues_Compile.JSON, Boolean>)(_3_obj) -> dafny.Helpers.Quantifier(((_3_obj).dtor_arr()).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
        JSON_mValues_Compile.JSON _forall_var_0 = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_forall_var_0_boxed0));
        JSON_mValues_Compile.JSON _4_s = (JSON_mValues_Compile.JSON)_forall_var_0;
        return !(((_3_obj).dtor_arr()).contains(_4_s)) || ((_4_s).is_String());
      }))).apply(_1_obj)), dafny.DafnySequence.asString("Not an array of strings"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      } else {
        dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _5_arr = (_1_obj).dtor_arr();
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.Create(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), java.math.BigInteger.valueOf((_5_arr).length()), ((java.util.function.Function<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends Character>>>)(_6_arr) -> ((java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends Character>>)(_7_n_boxed0) -> {
  java.math.BigInteger _7_n = ((java.math.BigInteger)(java.lang.Object)(_7_n_boxed0));
  return (((JSON_mValues_Compile.JSON)(java.lang.Object)((_6_arr).select(dafny.Helpers.toInt((_7_n)))))).dtor_str();
})).apply(_5_arr)));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>, dafny.DafnySequence<? extends Character>> GetArrayObject(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))));
    } else {
      JSON_mValues_Compile.JSON _1_obj = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_1_obj).is_Array()) && (((java.util.function.Function<JSON_mValues_Compile.JSON, Boolean>)(_3_obj) -> dafny.Helpers.Quantifier(((_3_obj).dtor_arr()).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
        JSON_mValues_Compile.JSON _forall_var_0 = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_forall_var_0_boxed0));
        JSON_mValues_Compile.JSON _4_s = (JSON_mValues_Compile.JSON)_forall_var_0;
        return !(((_3_obj).dtor_arr()).contains(_4_s)) || ((_4_s).is_Object());
      }))).apply(_1_obj)), dafny.DafnySequence.asString("Not an array of objects"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))));
      } else {
        dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _5_arr = (_1_obj).dtor_arr();
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.Create(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), java.math.BigInteger.valueOf((_5_arr).length()), ((java.util.function.Function<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>>)(_6_arr) -> ((java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>)(_7_n_boxed0) -> {
  java.math.BigInteger _7_n = ((java.math.BigInteger)(java.lang.Object)(_7_n_boxed0));
  return (((JSON_mValues_Compile.JSON)(java.lang.Object)((_6_arr).select(dafny.Helpers.toInt((_7_n)))))).dtor_obj();
})).apply(_5_arr)));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> SmallObjectToStringStringMap(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.Get(key, obj);
    if ((_0_valueOrError0).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    } else {
      JSON_mValues_Compile.JSON _1_item = (_0_valueOrError0).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      return __default.JsonObjectToStringStringMap(_1_item);
    }
  }
  public static Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>, dafny.DafnySequence<? extends Character>> GetOptionalSmallObjectToStringStringMap(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Option<JSON_mValues_Compile.JSON> _0_item = (__default.Get(key, obj)).ToOption(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if ((_0_item).is_Some()) {
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = __default.JsonObjectToStringStringMap((_0_item).dtor_value());
      if ((_1_valueOrError0).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_1_valueOrError0).<Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
      } else {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_m = (_1_valueOrError0).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        return Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _2_m));
      }
    } else {
      return Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    }
  }
  public static dafny.Tuple0 printJson(JSON_mValues_Compile.JSON j)
  {
    dafny.Tuple0 _hresult = dafny.Tuple0.Default();
    System.out.print(java.lang.String.valueOf(j));
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
    _hresult = dafny.Tuple0.create();
    return _hresult;
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> JsonObjectToStringStringMap(JSON_mValues_Compile.JSON item) {
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (item).is_Object(), dafny.DafnySequence.asString("Not an object"));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    } else {
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _1_obj = (item).dtor_obj();
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, Boolean>)(_3_obj) -> dafny.Helpers.Quantifier((_3_obj).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
        dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _forall_var_0 = ((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)(_forall_var_0_boxed0));
        dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _4_t = (dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)_forall_var_0;
        return !((_3_obj).contains(_4_t)) || (((_4_t).dtor__1()).is_String());
      }))).apply(_1_obj), dafny.DafnySequence.asString("Not a string string object"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      } else {
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, Boolean>)(_6_obj) -> dafny.Helpers.Quantifier(dafny.Helpers.IntegerRange(java.math.BigInteger.ZERO, java.math.BigInteger.valueOf((_6_obj).length())), true, ((_forall_var_1_boxed0) -> {
          java.math.BigInteger _forall_var_1 = ((java.math.BigInteger)(java.lang.Object)(_forall_var_1_boxed0));
          java.math.BigInteger _7_i = (java.math.BigInteger)_forall_var_1;
          return dafny.Helpers.Quantifier(dafny.Helpers.IntegerRange((_7_i).add(java.math.BigInteger.ONE), java.math.BigInteger.valueOf((_6_obj).length())), true, ((_forall_var_2_boxed0) -> {
            java.math.BigInteger _forall_var_2 = ((java.math.BigInteger)(java.lang.Object)(_forall_var_2_boxed0));
            java.math.BigInteger _8_j = (java.math.BigInteger)_forall_var_2;
            return !((((_7_i).signum() != -1) && ((_7_i).compareTo(_8_j) < 0)) && ((_8_j).compareTo(java.math.BigInteger.valueOf((_6_obj).length())) < 0)) || (!((((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((_6_obj).select(dafny.Helpers.toInt((_7_i)))))).dtor__0()).equals((((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((_6_obj).select(dafny.Helpers.toInt((_8_j)))))).dtor__0()));
          }));
        }))).apply(_1_obj), dafny.DafnySequence.asString("JSON serialization Error"));
        if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_5_valueOrError2).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
        } else {
          return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(_9_obj) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(() -> {
  java.util.HashMap<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _coll0 = new java.util.HashMap<>();
  for (dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _compr_0_boxed0 : (_9_obj).Elements()) {
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _compr_0 = ((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)(_compr_0_boxed0));
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _10_t = (dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)_compr_0;
    if ((_9_obj).contains(_10_t)) {
      _coll0.put((_10_t).dtor__0(),((_10_t).dtor__1()).dtor_str());
    }
  }
  return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>>(_coll0);
})).apply()).apply(_1_obj));
        }
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> utf8EncodePair(dafny.DafnySequence<? extends Character> key, dafny.DafnySequence<? extends Character> value)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = UTF8.__default.Encode(key);
    if ((_0_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _1_utf8Key = (_0_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = UTF8.__default.Encode(value);
      if ((_2_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()));
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _3_utf8Value = (_2_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>create(_1_utf8Key, _3_utf8Value));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> utf8EncodeMap(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> mapStringString) {
    if ((java.math.BigInteger.valueOf((mapStringString).size())).signum() == 0) {
      return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.fromElements());
    } else {
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>> _0_encodedResults = ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>>)(_1_mapStringString) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>>)(() -> {
        java.util.HashMap<dafny.DafnySequence<? extends Character>, Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>> _coll0 = new java.util.HashMap<>();
        for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (_1_mapStringString).keySet().Elements()) {
          dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
          dafny.DafnySequence<? extends Character> _2_key = (dafny.DafnySequence<? extends Character>)_compr_0;
          if ((_1_mapStringString).<dafny.DafnySequence<? extends Character>>contains(_2_key)) {
            _coll0.put(_2_key,__default.utf8EncodePair(_2_key, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_1_mapStringString).get(_2_key)))));
          }
        }
        return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>(_coll0);
      })).apply()).apply(mapStringString);
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>, Boolean>)(_4_encodedResults) -> dafny.Helpers.Quantifier(((_4_encodedResults).valueSet()).Elements(), true, ((_forall_var_0_boxed0) -> {
        Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _forall_var_0 = ((Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(_forall_var_0_boxed0));
        Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _5_r = (Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)_forall_var_0;
        return !(((_4_encodedResults).valueSet()).<Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>contains(_5_r)) || ((_5_r).is_Success());
      }))).apply(_0_encodedResults), dafny.DafnySequence.asString("String can not be UTF8 Encoded?"));
      if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_3_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()));
      } else {
        return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(_6_encodedResults) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(() -> {
  java.util.HashMap<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _coll1 = new java.util.HashMap<>();
  for (Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _compr_1_boxed0 : ((_6_encodedResults).valueSet()).Elements()) {
    Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _compr_1 = ((Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(_compr_1_boxed0));
    Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _7_r = (Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)_compr_1;
    if (((_6_encodedResults).valueSet()).<Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>contains(_7_r)) {
      _coll1.put(((_7_r).dtor_value()).dtor__0(),((_7_r).dtor_value()).dtor__1());
    }
  }
  return new dafny.DafnyMap<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>>(_coll1);
})).apply()).apply(_0_encodedResults));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> utf8EncodeSeq(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> seqOfStrings) {
    dafny.DafnySequence<? extends Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _0_encodedResults = dafny.DafnySequence.Create(Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), java.math.BigInteger.valueOf((seqOfStrings).length()), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>)(_1_seqOfStrings) -> ((java.util.function.Function<java.math.BigInteger, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>)(_2_i_boxed0) -> {
      java.math.BigInteger _2_i = ((java.math.BigInteger)(java.lang.Object)(_2_i_boxed0));
      return UTF8.__default.Encode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_1_seqOfStrings).select(dafny.Helpers.toInt((_2_i))))));
    })).apply(seqOfStrings));
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySequence<? extends Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>, Boolean>)(_4_encodedResults) -> dafny.Helpers.Quantifier((_4_encodedResults).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _forall_var_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(_forall_var_0_boxed0));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _5_r = (Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)_forall_var_0;
      return !((_4_encodedResults).contains(_5_r)) || ((_5_r).is_Success());
    }))).apply(_0_encodedResults), dafny.DafnySequence.asString("String can not be UTF8 Encoded?"));
    if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_3_valueOrError0).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()));
    } else {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.Create(UTF8.ValidUTF8Bytes._typeDescriptor(), java.math.BigInteger.valueOf((_0_encodedResults).length()), ((java.util.function.Function<dafny.DafnySequence<? extends Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>, java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends java.lang.Byte>>>)(_6_encodedResults) -> ((java.util.function.Function<java.math.BigInteger, dafny.DafnySequence<? extends java.lang.Byte>>)(_7_i_boxed0) -> {
  java.math.BigInteger _7_i = ((java.math.BigInteger)(java.lang.Object)(_7_i_boxed0));
  return (((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)((_6_encodedResults).select(dafny.Helpers.toInt((_7_i)))))).dtor_value();
})).apply(_0_encodedResults)));
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSONHelpers._default";
  }
}
