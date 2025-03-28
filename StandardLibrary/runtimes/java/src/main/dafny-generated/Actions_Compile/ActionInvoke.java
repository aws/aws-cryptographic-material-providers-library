// Class ActionInvoke<A, R>
// Dafny class ActionInvoke<A, R> compiled into Java
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
public class ActionInvoke<A, R> {
  public A _input;
  public R _output;
  protected dafny.TypeDescriptor<A> _td_A;
  protected dafny.TypeDescriptor<R> _td_R;
  public ActionInvoke (dafny.TypeDescriptor<A> _td_A, dafny.TypeDescriptor<R> _td_R, A input, R output) {
    this._td_A = _td_A;
    this._td_R = _td_R;
    this._input = input;
    this._output = output;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ActionInvoke<A, R> o = (ActionInvoke<A, R>)other;
    return true && java.util.Objects.equals(this._input, o._input) && java.util.Objects.equals(this._output, o._output);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._input);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._output);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Actions.ActionInvoke.ActionInvoke");
    s.append("(");
    s.append(dafny.Helpers.toString(this._input));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._output));
    s.append(")");
    return s.toString();
  }
  public static <A, R> dafny.TypeDescriptor<ActionInvoke<A, R>> _typeDescriptor(dafny.TypeDescriptor<A> _td_A, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<ActionInvoke<A, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<ActionInvoke<A, R>>referenceWithInitializer(ActionInvoke.class, () -> ActionInvoke.<A, R>Default(_td_A, _td_R, _td_A.defaultValue(), _td_R.defaultValue()));
  }

  public static <A, R> ActionInvoke<A, R> Default(dafny.TypeDescriptor<A> _td_A, dafny.TypeDescriptor<R> _td_R, A _default_A, R _default_R) {
    return Actions_Compile.ActionInvoke.<A, R>create(_td_A, _td_R, _default_A, _default_R);
  }
  @Deprecated()
  public static <A, R> ActionInvoke<A, R> Default(A _default_A, R _default_R) {
    dafny.TypeDescriptor<A> _td_A = null;
    dafny.TypeDescriptor<R> _td_R = null;
    return Actions_Compile.ActionInvoke.<A, R>create(_td_A, _td_R, _default_A, _default_R);
  }
  public static <A, R> ActionInvoke<A, R> create(dafny.TypeDescriptor<A> _td_A, dafny.TypeDescriptor<R> _td_R, A input, R output) {
    return new ActionInvoke<A, R>(_td_A, _td_R, input, output);
  }
  @Deprecated()
  public static <A, R> ActionInvoke<A, R> create(A input, R output) {
    return new ActionInvoke<A, R>(null, null, input, output);
  }
  public static <A, R> ActionInvoke<A, R> create_ActionInvoke(dafny.TypeDescriptor<A> _td_A, dafny.TypeDescriptor<R> _td_R, A input, R output) {
    return create(_td_A, _td_R, input, output);
  }
  @Deprecated()
  public static <A, R> ActionInvoke<A, R> create_ActionInvoke(A input, R output) {
    return create(null, null, input, output);
  }
  public boolean is_ActionInvoke() { return true; }
  public A dtor_input() {
    return this._input;
  }
  public R dtor_output() {
    return this._output;
  }
}
