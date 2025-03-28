// Class UnescapeError
// Dafny class UnescapeError compiled into Java
package JSON_mUtils_mStr_mCharStrEscaping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class UnescapeError {
  public UnescapeError () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UnescapeError o = (UnescapeError)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("CharStrEscaping.UnescapeError.EscapeAtEOS");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UnescapeError> _TYPE = dafny.TypeDescriptor.<UnescapeError>referenceWithInitializer(UnescapeError.class, () -> UnescapeError.Default());
  public static dafny.TypeDescriptor<UnescapeError> _typeDescriptor() {
    return (dafny.TypeDescriptor<UnescapeError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UnescapeError theDefault = JSON_mUtils_mStr_mCharStrEscaping_Compile.UnescapeError.create();
  public static UnescapeError Default() {
    return theDefault;
  }
  public static UnescapeError create() {
    return new UnescapeError();
  }
  public static UnescapeError create_EscapeAtEOS() {
    return create();
  }
  public boolean is_EscapeAtEOS() { return true; }
  public static java.util.ArrayList<UnescapeError> AllSingletonConstructors() {
    java.util.ArrayList<UnescapeError> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new UnescapeError());
    return singleton_iterator;
  }
}
