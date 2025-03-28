// Class Param_Flag
// Dafny class Param_Flag compiled into Java
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
public class Param_Flag extends Param {
  public dafny.DafnySequence<? extends Character> _name;
  public dafny.DafnySequence<? extends Character> _help;
  public char _short;
  public boolean _solo;
  public boolean _inherit;
  public Visibility _vis;
  public dafny.DafnySequence<? extends Character> _shortAlias;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _longAlias;
  public Param_Flag (dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, char short_, boolean solo, boolean inherit, Visibility vis, dafny.DafnySequence<? extends Character> shortAlias, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> longAlias) {
    super();
    this._name = name;
    this._help = help;
    this._short = short_;
    this._solo = solo;
    this._inherit = inherit;
    this._vis = vis;
    this._shortAlias = shortAlias;
    this._longAlias = longAlias;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Param_Flag o = (Param_Flag)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._help, o._help) && this._short == o._short && this._solo == o._solo && this._inherit == o._inherit && java.util.Objects.equals(this._vis, o._vis) && java.util.Objects.equals(this._shortAlias, o._shortAlias) && java.util.Objects.equals(this._longAlias, o._longAlias);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._help);
    hash = ((hash << 5) + hash) + Character.hashCode(this._short);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._solo);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._inherit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._vis);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._shortAlias);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._longAlias);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Param.Flag");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._help));
    s.append(", ");
    s.append(this._short);
    s.append(", ");
    s.append(this._solo);
    s.append(", ");
    s.append(this._inherit);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._vis));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._shortAlias));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._longAlias));
    s.append(")");
    return s.toString();
  }
}
