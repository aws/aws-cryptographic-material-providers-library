// Class Chain_Chain
// Dafny class Chain_Chain compiled into Java
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
public class Chain_Chain extends Chain {
  public Chain _previous;
  public JSON_mUtils_mViews_mCore_Compile.View__ _v;
  public Chain_Chain (Chain previous, JSON_mUtils_mViews_mCore_Compile.View__ v) {
    super();
    this._previous = previous;
    this._v = v;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Chain_Chain o = (Chain_Chain)other;
    return true && java.util.Objects.equals(this._previous, o._previous) && java.util.Objects.equals(this._v, o._v);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._previous);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._v);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Writers.Chain.Chain");
    s.append("(");
    s.append(dafny.Helpers.toString(this._previous));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._v));
    s.append(")");
    return s.toString();
  }
}
