// Class Chain
// Dafny class Chain compiled into Java
package JSON_mUtils_mViews_mWriters_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Chain {
  public Chain() {
  }
  private static final dafny.TypeDescriptor<Chain> _TYPE = dafny.TypeDescriptor.<Chain>referenceWithInitializer(Chain.class, () -> Chain.Default());
  public static dafny.TypeDescriptor<Chain> _typeDescriptor() {
    return (dafny.TypeDescriptor<Chain>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Chain theDefault = JSON_mUtils_mViews_mWriters_Compile.Chain.create_Empty();
  public static Chain Default() {
    return theDefault;
  }
  public static Chain create_Empty() {
    return new Chain_Empty();
  }
  public static Chain create_Chain(Chain previous, JSON_mUtils_mViews_mCore_Compile.View__ v) {
    return new Chain_Chain(previous, v);
  }
  public boolean is_Empty() { return this instanceof Chain_Empty; }
  public boolean is_Chain() { return this instanceof Chain_Chain; }
  public Chain dtor_previous() {
    Chain d = this;
    return ((Chain_Chain)d)._previous;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_v() {
    Chain d = this;
    return ((Chain_Chain)d)._v;
  }
  public java.math.BigInteger Length() {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    Chain _this = this;
    TAIL_CALL_START: while (true) {
      if ((_this).is_Empty()) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (dafny.Helpers.unsignedToBigInteger(((_this).dtor_v()).Length())).add(_0___accumulator);
        Chain _in0 = (_this).dtor_previous();
        _this = _in0;
        ;
        continue TAIL_CALL_START;
      }
    }
  }
  public java.math.BigInteger Count() {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    Chain _this = this;
    TAIL_CALL_START: while (true) {
      if ((_this).is_Empty()) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (java.math.BigInteger.ONE).add(_0___accumulator);
        Chain _in0 = (_this).dtor_previous();
        _this = _in0;
        ;
        continue TAIL_CALL_START;
      }
    }
  }
  public dafny.DafnySequence<? extends java.lang.Byte> Bytes() {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    Chain _this = this;
    TAIL_CALL_START: while (true) {
      if ((_this).is_Empty()) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), _0___accumulator);
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(((_this).dtor_v()).Bytes(), _0___accumulator);
        Chain _in0 = (_this).dtor_previous();
        _this = _in0;
        ;
        continue TAIL_CALL_START;
      }
    }
  }
  public Chain Append(JSON_mUtils_mViews_mCore_Compile.View__ v_k) {
    if (((this).is_Chain()) && (JSON_mUtils_mViews_mCore_Compile.__default.Adjacent((this).dtor_v(), v_k))) {
      return JSON_mUtils_mViews_mWriters_Compile.Chain.create_Chain((this).dtor_previous(), JSON_mUtils_mViews_mCore_Compile.__default.Merge((this).dtor_v(), v_k));
    } else {
      return JSON_mUtils_mViews_mWriters_Compile.Chain.create_Chain(this, v_k);
    }
  }
  public void CopyTo(byte[] dest, int end)
  {
    Chain _this = this;
    TAIL_CALL_START: while (true) {
      if(true) {
        if ((_this).is_Chain()) {
          int _0_end;
          _0_end = (int) ((end) - (((_this).dtor_v()).Length()));
          ((_this).dtor_v()).CopyTo(dest, _0_end);
          Chain _in0 = (_this).dtor_previous();
          byte[] _in1 = dest;
          int _in2 = _0_end;
          _this = _in0;
          ;
          dest = _in1;
          end = _in2;
          continue TAIL_CALL_START;
        }
      }
      return;
    }
  }
}
