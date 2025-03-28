// Class StringLexerState
// Dafny class StringLexerState compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class StringLexerState {
  public StringLexerState() {
  }
  private static final dafny.TypeDescriptor<StringLexerState> _TYPE = dafny.TypeDescriptor.<StringLexerState>referenceWithInitializer(StringLexerState.class, () -> StringLexerState.Default());
  public static dafny.TypeDescriptor<StringLexerState> _typeDescriptor() {
    return (dafny.TypeDescriptor<StringLexerState>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StringLexerState theDefault = JSON_mUtils_mLexers_mStrings_Compile.StringLexerState.create_Start();
  public static StringLexerState Default() {
    return theDefault;
  }
  public static StringLexerState create_Start() {
    return new StringLexerState_Start();
  }
  public static StringLexerState create_Body(boolean escaped) {
    return new StringLexerState_Body(escaped);
  }
  public static StringLexerState create_End() {
    return new StringLexerState_End();
  }
  public boolean is_Start() { return this instanceof StringLexerState_Start; }
  public boolean is_Body() { return this instanceof StringLexerState_Body; }
  public boolean is_End() { return this instanceof StringLexerState_End; }
  public boolean dtor_escaped() {
    StringLexerState d = this;
    return ((StringLexerState_Body)d)._escaped;
  }
}
