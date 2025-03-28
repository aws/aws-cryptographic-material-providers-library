// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mViews_mCore_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean Adjacent(View__ lv, View__ rv)
  {
    return (((lv).dtor_end()) == ((rv).dtor_beg())) && (((lv).dtor_s()).equals((rv).dtor_s()));
  }
  public static View__ Merge(View__ lv, View__ rv)
  {
    View__ _0_dt__update__tmp_h0 = lv;
    int _1_dt__update_hend_h0 = (rv).dtor_end();
    return JSON_mUtils_mViews_mCore_Compile.View__.create((_0_dt__update__tmp_h0).dtor_s(), (_0_dt__update__tmp_h0).dtor_beg(), _1_dt__update_hend_h0);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Views.Core._default";
  }
}
