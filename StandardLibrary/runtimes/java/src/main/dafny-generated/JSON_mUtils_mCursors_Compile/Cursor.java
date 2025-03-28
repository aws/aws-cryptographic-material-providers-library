// Class Cursor
// Dafny class Cursor compiled into Java
package JSON_mUtils_mCursors_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class Cursor {
  public Cursor() {
  }
  public static Cursor__ Witness = JSON_mUtils_mCursors_Compile.Cursor__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0, 0);
  public static Cursor__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<Cursor__> _TYPE = dafny.TypeDescriptor.<Cursor__>referenceWithInitializer(Cursor__.class, () -> Cursor.defaultValue());
  public static dafny.TypeDescriptor<Cursor__> _typeDescriptor() {
    return (dafny.TypeDescriptor<Cursor__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
