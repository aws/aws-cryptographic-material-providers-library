// Class Vector
// Dafny class Vector compiled into Java
package JSON_mUtils_mVectors_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class Vector<A> {
  protected dafny.TypeDescriptor<A> _td_A;
  public Vector(dafny.TypeDescriptor<A> _td_A) {
    this._td_A = _td_A;
    this.size = 0;
    this.capacity = 0;
    this.data = (java.lang.Object)_td_A.newArray(0);
    this._a = null;
  }
  public int size;
  public int capacity;
  public java.lang.Object data;
  public void __ctor(A a0, int initial__capacity)
  {
    (this)._a = a0;
    (this).size = 0;
    (this).capacity = initial__capacity;
    java.util.function.Function<java.math.BigInteger, A> _init0 = ((java.util.function.Function<A, java.util.function.Function<java.math.BigInteger, A>>)(_0_a0) -> ((java.util.function.Function<java.math.BigInteger, A>)(_1___v0_boxed0) -> {
      java.math.BigInteger _1___v0 = ((java.math.BigInteger)(java.lang.Object)(_1___v0_boxed0));
      return _0_a0;
    })).apply(a0);
    java.lang.Object _nw0 = (java.lang.Object) _td_A.newArray(dafny.Helpers.toIntChecked((initial__capacity), "Java arrays may be no larger than the maximum 32-bit signed int"));
    for (java.math.BigInteger _i0_0 = java.math.BigInteger.ZERO; _i0_0.compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength(_nw0))) < 0; _i0_0 = _i0_0.add(java.math.BigInteger.ONE)) {
      _td_A.setArrayElement(_nw0, dafny.Helpers.toInt(_i0_0), ((A)(java.lang.Object)(_init0.apply(_i0_0))));
    }
    (this).data = _nw0;
  }
  public A At(int idx) {
    return _td_A.getArrayElement((this.data), (idx));
  }
  public A Top() {
    return _td_A.getArrayElement((this.data), ((int) ((this.size) - (1))));
  }
  public void Put(int idx, A a)
  {
    java.lang.Object _arr0 = this.data;
    _td_A.setArrayElement(_arr0, dafny.Helpers.toInt((idx)), a);
  }
  public void CopyFrom(java.lang.Object new__data, int count)
  {
    int _hi0 = count;
    for (int _0_idx = 0; java.lang.Integer.compareUnsigned(_0_idx, _hi0) < 0; _0_idx++) {
      java.lang.Object _arr0 = this.data;
      _td_A.setArrayElement(_arr0, dafny.Helpers.toInt((_0_idx)), _td_A.getArrayElement((new__data), (_0_idx)));
    }
  }
  public void Realloc(int new__capacity)
  {
    java.lang.Object _0_old__data;
    int _1_old__capacity;
    java.lang.Object _rhs0 = this.data;
    int _rhs1 = this.capacity;
    _0_old__data = _rhs0;
    _1_old__capacity = _rhs1;
    java.util.function.Function<java.math.BigInteger, A> _init0 = ((java.util.function.Function<java.math.BigInteger, A>)(_2___v1_boxed0) -> {
      java.math.BigInteger _2___v1 = ((java.math.BigInteger)(java.lang.Object)(_2___v1_boxed0));
      return (this).a();
    });
    java.lang.Object _nw0 = (java.lang.Object) _td_A.newArray(dafny.Helpers.toIntChecked((new__capacity), "Java arrays may be no larger than the maximum 32-bit signed int"));
    for (java.math.BigInteger _i0_0 = java.math.BigInteger.ZERO; _i0_0.compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength(_nw0))) < 0; _i0_0 = _i0_0.add(java.math.BigInteger.ONE)) {
      _td_A.setArrayElement(_nw0, dafny.Helpers.toInt(_i0_0), ((A)(java.lang.Object)(_init0.apply(_i0_0))));
    }
    java.lang.Object _rhs2 = _nw0;
    int _rhs3 = new__capacity;
    Vector<A> _lhs0 = this;
    Vector<A> _lhs1 = this;
    _lhs0.data = _rhs2;
    _lhs1.capacity = _rhs3;
    (this).CopyFrom(_0_old__data, _1_old__capacity);
  }
  public int DefaultNewCapacity(int capacity) {
    if (java.lang.Integer.compareUnsigned(capacity, (this).MAX__CAPACITY__BEFORE__DOUBLING()) < 0) {
      return (int) ((2) * (capacity));
    } else {
      return (this).MAX__CAPACITY();
    }
  }
  public Wrappers_Compile.Outcome<VectorError> ReallocDefault()
  {
    Wrappers_Compile.Outcome<VectorError> o = Wrappers_Compile.Outcome.<VectorError>Default(VectorError._typeDescriptor());
    if ((this.capacity) == ((this).MAX__CAPACITY())) {
      o = Wrappers_Compile.Outcome.<VectorError>create_Fail(VectorError._typeDescriptor(), JSON_mUtils_mVectors_Compile.VectorError.create());
      return o;
    }
    (this).Realloc((this).DefaultNewCapacity(this.capacity));
    o = Wrappers_Compile.Outcome.<VectorError>create_Pass(VectorError._typeDescriptor());
    return o;
  }
  public Wrappers_Compile.Outcome<VectorError> Ensure(int reserved)
  {
    Wrappers_Compile.Outcome<VectorError> o = Wrappers_Compile.Outcome.<VectorError>Default(VectorError._typeDescriptor());
    if (java.lang.Integer.compareUnsigned(reserved, (int) (((this).MAX__CAPACITY()) - (this.size))) > 0) {
      o = Wrappers_Compile.Outcome.<VectorError>create_Fail(VectorError._typeDescriptor(), JSON_mUtils_mVectors_Compile.VectorError.create());
      return o;
    }
    if (java.lang.Integer.compareUnsigned(reserved, (int) ((this.capacity) - (this.size))) <= 0) {
      o = Wrappers_Compile.Outcome.<VectorError>create_Pass(VectorError._typeDescriptor());
      return o;
    }
    int _0_new__capacity;
    _0_new__capacity = this.capacity;
    while (java.lang.Integer.compareUnsigned(reserved, (int) ((_0_new__capacity) - (this.size))) > 0) {
      _0_new__capacity = (this).DefaultNewCapacity(_0_new__capacity);
    }
    (this).Realloc(_0_new__capacity);
    o = Wrappers_Compile.Outcome.<VectorError>create_Pass(VectorError._typeDescriptor());
    return o;
  }
  public void PopFast()
  {
    (this).size = (int) ((this.size) - (1));
  }
  public void PushFast(A a)
  {
    java.lang.Object _arr0 = this.data;
    int _index0 = this.size;
    _td_A.setArrayElement(_arr0, dafny.Helpers.toInt(_index0), a);
    (this).size = (int) ((this.size) + (1));
  }
  public Wrappers_Compile.Outcome<VectorError> Push(A a)
  {
    Wrappers_Compile.Outcome<VectorError> o = Wrappers_Compile.Outcome.<VectorError>Default(VectorError._typeDescriptor());
    if ((this.size) == (this.capacity)) {
      Wrappers_Compile.Outcome<VectorError> _0_d;
      Wrappers_Compile.Outcome<VectorError> _out0;
      _out0 = (this).ReallocDefault();
      _0_d = _out0;
      if ((_0_d).is_Fail()) {
        o = _0_d;
        return o;
      }
    }
    (this).PushFast(a);
    o = Wrappers_Compile.Outcome.<VectorError>create_Pass(VectorError._typeDescriptor());
    return o;
  }
  public A _a;
  public A a()
  {
    return this._a;
  }
  public int MAX__CAPACITY__BEFORE__DOUBLING()
  {
    return java.lang.Integer.divideUnsigned(BoundedInts_Compile.__default.UINT32__MAX(), 2);
  }
  public int MAX__CAPACITY()
  {
    return BoundedInts_Compile.__default.UINT32__MAX();
  }
  public static <A> dafny.TypeDescriptor<Vector<A>> _typeDescriptor(dafny.TypeDescriptor<A> _td_A) {
    return (dafny.TypeDescriptor<Vector<A>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Vector<A>>referenceWithInitializer(Vector.class, () -> (Vector<A>) null);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Vectors.Vector";
  }
}
