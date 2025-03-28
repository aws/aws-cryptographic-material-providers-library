// Class Options
// Dafny class Options compiled into Java
package GetOpt_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class Options {
  public dafny.DafnySequence<? extends Character> _name;
  public dafny.DafnySequence<? extends Character> _help;
  public dafny.DafnySequence<? extends Param> _params;
  public Options (dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, dafny.DafnySequence<? extends Param> params) {
    this._name = name;
    this._help = help;
    this._params = params;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Options o = (Options)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._help, o._help) && java.util.Objects.equals(this._params, o._params);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._help);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._params);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Options.Options");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._help));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._params));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Options> _TYPE = dafny.TypeDescriptor.<Options>referenceWithInitializer(Options.class, () -> Options.Default());
  public static dafny.TypeDescriptor<Options> _typeDescriptor() {
    return (dafny.TypeDescriptor<Options>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Options theDefault = GetOpt_Compile.Options.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Param> empty(Param._typeDescriptor()));
  public static Options Default() {
    return theDefault;
  }
  public static Options create(dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, dafny.DafnySequence<? extends Param> params) {
    return new Options(name, help, params);
  }
  public static Options create_Options(dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, dafny.DafnySequence<? extends Param> params) {
    return create(name, help, params);
  }
  public boolean is_Options() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    return this._name;
  }
  public dafny.DafnySequence<? extends Character> dtor_help() {
    return this._help;
  }
  public dafny.DafnySequence<? extends Param> dtor_params() {
    return this._params;
  }
}
