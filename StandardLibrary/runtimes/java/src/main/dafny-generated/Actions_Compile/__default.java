// Class __default
// Dafny class __default compiled into Java
package Actions_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__A, __R> dafny.DafnySequence<? extends __R> DeterministicMap(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__R> _td___R, DeterministicAction<__A, __R> action, dafny.DafnySequence<? extends __A> s)
  {
    dafny.DafnySequence<? extends __R> res = dafny.DafnySequence.<__R> empty(_td___R);
    dafny.DafnySequence<? extends __R> _0_rs;
    _0_rs = dafny.DafnySequence.<__R> empty(_td___R);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      @SuppressWarnings({"unchecked", "deprecation"})
      __R _2_r;
      @SuppressWarnings({"unchecked", "deprecation"})
      __R _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_r = _out0;
      _0_rs = dafny.DafnySequence.<__R>concatenate(_0_rs, dafny.DafnySequence.<__R> of(_td___R, _2_r));
    }
    res = _0_rs;
    return res;
  }
  public static <__A, __R, __E> Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> DeterministicMapWithResult(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__R> _td___R, dafny.TypeDescriptor<__E> _td___E, DeterministicActionWithResult<__A, __R, __E> action, dafny.DafnySequence<? extends __A> s)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>Default(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R> empty(_td___R));
    dafny.DafnySequence<? extends __R> _0_rs;
    _0_rs = dafny.DafnySequence.<__R> empty(_td___R);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<__R, __E> _2_valueOrError0 = (Wrappers_Compile.Result<__R, __E>)null;
      Wrappers_Compile.Result<__R, __E> _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(_td___R, _td___E)) {
        res = (_2_valueOrError0).<dafny.DafnySequence<? extends __R>>PropagateFailure(_td___R, _td___E, dafny.DafnySequence.<__R>_typeDescriptor(_td___R));
        return res;
      }
      @SuppressWarnings({"unchecked", "deprecation"})
      __R _3_r;
      _3_r = (_2_valueOrError0).Extract(_td___R, _td___E);
      _0_rs = dafny.DafnySequence.<__R>concatenate(_0_rs, dafny.DafnySequence.<__R> of(_td___R, _3_r));
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>create_Success(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, _0_rs);
    return res;
  }
  public static <__A, __R> dafny.DafnySequence<? extends __R> DeterministicFlatMap(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__R> _td___R, DeterministicAction<__A, dafny.DafnySequence<? extends __R>> action, dafny.DafnySequence<? extends __A> s)
  {
    dafny.DafnySequence<? extends __R> res = dafny.DafnySequence.<__R> empty(_td___R);
    dafny.DafnySequence<? extends __R> _0_rs;
    _0_rs = dafny.DafnySequence.<__R> empty(_td___R);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      dafny.DafnySequence<? extends __R> _2_r;
      dafny.DafnySequence<? extends __R> _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_r = _out0;
      _0_rs = dafny.DafnySequence.<__R>concatenate(_0_rs, _2_r);
    }
    res = _0_rs;
    return res;
  }
  public static <__A, __R, __E> Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> DeterministicFlatMapWithResult(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__R> _td___R, dafny.TypeDescriptor<__E> _td___E, DeterministicActionWithResult<__A, dafny.DafnySequence<? extends __R>, __E> action, dafny.DafnySequence<? extends __A> s)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>Default(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R> empty(_td___R));
    dafny.DafnySequence<? extends __R> _0_rs;
    _0_rs = dafny.DafnySequence.<__R> empty(_td___R);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>Default(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R> empty(_td___R));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E)) {
        res = (_2_valueOrError0).<dafny.DafnySequence<? extends __R>>PropagateFailure(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R>_typeDescriptor(_td___R));
        return res;
      }
      dafny.DafnySequence<? extends __R> _3_r;
      _3_r = (_2_valueOrError0).Extract(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E);
      _0_rs = dafny.DafnySequence.<__R>concatenate(_0_rs, _3_r);
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> _rhs0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>create_Success(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, _0_rs);
    res = _rhs0;
    return res;
  }
  public static <__A> dafny.DafnySequence<? extends __A> Filter(dafny.TypeDescriptor<__A> _td___A, DeterministicAction<__A, Boolean> action, dafny.DafnySequence<? extends __A> s)
  {
    dafny.DafnySequence<? extends __A> res = dafny.DafnySequence.<__A> empty(_td___A);
    dafny.DafnySequence<? extends __A> _0_rs;
    _0_rs = dafny.DafnySequence.<__A> empty(_td___A);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      boolean _2_r;
      boolean _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_r = _out0;
      if (_2_r) {
        _0_rs = dafny.DafnySequence.<__A>concatenate(_0_rs, dafny.DafnySequence.<__A> of(_td___A, ((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i)))))));
      }
    }
    res = _0_rs;
    return res;
  }
  public static <__A, __E> Wrappers_Compile.Result<dafny.DafnySequence<? extends __A>, __E> FilterWithResult(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__E> _td___E, DeterministicActionWithResult<__A, Boolean, __E> action, dafny.DafnySequence<? extends __A> s)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends __A>, __E> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __A>, __E>Default(dafny.DafnySequence.<__A>_typeDescriptor(_td___A), _td___E, dafny.DafnySequence.<__A> empty(_td___A));
    dafny.DafnySequence<? extends __A> _0_rs;
    _0_rs = dafny.DafnySequence.<__A> empty(_td___A);
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<Boolean, __E> _2_valueOrError0 = Wrappers_Compile.Result.<Boolean, __E>Default(dafny.TypeDescriptor.BOOLEAN, _td___E, false);
      Wrappers_Compile.Result<Boolean, __E> _out0;
      _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(dafny.TypeDescriptor.BOOLEAN, _td___E)) {
        res = (_2_valueOrError0).<dafny.DafnySequence<? extends __A>>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, _td___E, dafny.DafnySequence.<__A>_typeDescriptor(_td___A));
        return res;
      }
      boolean _3_r;
      _3_r = (_2_valueOrError0).Extract(dafny.TypeDescriptor.BOOLEAN, _td___E);
      if (_3_r) {
        _0_rs = dafny.DafnySequence.<__A>concatenate(_0_rs, dafny.DafnySequence.<__A> of(_td___A, ((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i)))))));
      }
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends __A>, __E>create_Success(dafny.DafnySequence.<__A>_typeDescriptor(_td___A), _td___E, _0_rs);
    return res;
  }
  public static <__A, __B, __E> Wrappers_Compile.Result<__B, dafny.DafnySequence<? extends __E>> ReduceToSuccess(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__B> _td___B, dafny.TypeDescriptor<__E> _td___E, ActionWithResult<__A, __B, __E> action, dafny.DafnySequence<? extends __A> s)
  {
    Wrappers_Compile.Result<__B, dafny.DafnySequence<? extends __E>> res = (Wrappers_Compile.Result<__B, dafny.DafnySequence<? extends __E>>)null;
    if(true) {
      dafny.DafnySequence<? extends Wrappers_Compile.Result<__B, __E>> _0_attemptedResults;
      _0_attemptedResults = dafny.DafnySequence.<Wrappers_Compile.Result<__B, __E>> empty(Wrappers_Compile.Result.<__B, __E>_typeDescriptor(_td___B, _td___E));
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((s).length());
      for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
        Wrappers_Compile.Result<__B, __E> _2_attempt;
        Wrappers_Compile.Result<__B, __E> _out0;
        _out0 = (action).Invoke(((__A)(java.lang.Object)((s).select(dafny.Helpers.toInt((_1_i))))));
        _2_attempt = _out0;
        _0_attemptedResults = dafny.DafnySequence.<Wrappers_Compile.Result<__B, __E>>concatenate(_0_attemptedResults, dafny.DafnySequence.<Wrappers_Compile.Result<__B, __E>> of(Wrappers_Compile.Result.<__B, __E>_typeDescriptor(_td___B, _td___E), _2_attempt));
        if ((_2_attempt).is_Success()) {
          Wrappers_Compile.Result<__B, dafny.DafnySequence<? extends __E>> _rhs0 = Wrappers_Compile.Result.<__B, dafny.DafnySequence<? extends __E>>create_Success(_td___B, dafny.DafnySequence.<__E>_typeDescriptor(_td___E), (_2_attempt).dtor_value());
          res = _rhs0;
          return res;
        }
      }
      res = Wrappers_Compile.Result.<__B, dafny.DafnySequence<? extends __E>>create_Failure(_td___B, dafny.DafnySequence.<__E>_typeDescriptor(_td___E), Seq_Compile.__default.<Wrappers_Compile.Result<__B, __E>, __E>Map(Wrappers_Compile.Result.<__B, __E>_typeDescriptor(_td___B, _td___E), _td___E, (Wrappers_Compile.Result<__B, __E> _eta0) -> __default.<__B, __E>pluckErrors(_td___B, _td___E, ((Wrappers_Compile.Result<__B, __E>)(java.lang.Object)(_eta0))), _0_attemptedResults));
    }
    return res;
  }
  public static <__B, __E> __E pluckErrors(dafny.TypeDescriptor<__B> _td___B, dafny.TypeDescriptor<__E> _td___E, Wrappers_Compile.Result<__B, __E> r)
  {
    return (r).dtor_error();
  }
  @Override
  public java.lang.String toString() {
    return "Actions._default";
  }
}
