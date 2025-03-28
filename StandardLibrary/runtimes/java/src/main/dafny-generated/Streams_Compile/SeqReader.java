// Class SeqReader
// Dafny class SeqReader compiled into Java
package Streams_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class SeqReader<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public SeqReader(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
    this.pos = java.math.BigInteger.ZERO;
    this._data = dafny.DafnySequence.<T> empty(_td_T);
  }
  public java.math.BigInteger pos;
  public void __ctor(dafny.DafnySequence<? extends T> s)
  {
    (this)._data = s;
    (this).pos = java.math.BigInteger.ZERO;
  }
  public dafny.DafnySequence<? extends T> ReadElements(java.math.BigInteger n)
  {
    dafny.DafnySequence<? extends T> elems = dafny.DafnySequence.<T> empty(_td_T);
    elems = (((this).data()).drop(this.pos)).take(n);
    (this).pos = (this.pos).add(n);
    elems = elems;
    return elems;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends T>, dafny.DafnySequence<? extends Character>> ReadExact(java.math.BigInteger n)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends T>, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends T>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<T>_typeDescriptor(_td_T), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<T> empty(_td_T));
    if(true) {
      if ((n).compareTo((java.math.BigInteger.valueOf(((this).data()).length())).subtract(this.pos)) > 0) {
        res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends T>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<T>_typeDescriptor(_td_T), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("IO Error: Not enough elements left on stream."));
        return res;
      } else {
        dafny.DafnySequence<? extends T> _0_elements;
        dafny.DafnySequence<? extends T> _out0;
        _out0 = (this).ReadElements(n);
        _0_elements = _out0;
        res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends T>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<T>_typeDescriptor(_td_T), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_elements);
        return res;
      }
    }
    return res;
  }
  public dafny.DafnySequence<? extends T> _data;
  public dafny.DafnySequence<? extends T> data()
  {
    return this._data;
  }
  public static <T> dafny.TypeDescriptor<SeqReader<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<SeqReader<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<SeqReader<T>>referenceWithInitializer(SeqReader.class, () -> (SeqReader<T>) null);
  }
  @Override
  public java.lang.String toString() {
    return "Streams.SeqReader";
  }
}
