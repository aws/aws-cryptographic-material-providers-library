// Class SuffixedSequence
// Dafny class SuffixedSequence compiled into Java
package JSON_mGrammar_Compile;

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
import JSON_mUtils_mStr_mCharStrEscaping_Compile.*;
import JSON_mUtils_mStr_Compile.*;
import JSON_mUtils_mVectors_Compile.*;
import JSON_mErrors_Compile.*;
import JSON_mValues_Compile.*;
import JSON_mSpec_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SuffixedSequence<D, S> {
  protected dafny.TypeDescriptor<D> _td_D;
  protected dafny.TypeDescriptor<S> _td_S;
  public SuffixedSequence(dafny.TypeDescriptor<D> _td_D, dafny.TypeDescriptor<S> _td_S) {
    this._td_D = _td_D;
    this._td_S = _td_S;
  }
  public static <D, S> dafny.TypeDescriptor<dafny.DafnySequence<? extends Suffixed<D, S>>> _typeDescriptor(dafny.TypeDescriptor<D> _td_D, dafny.TypeDescriptor<S> _td_S) {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Suffixed<D, S>>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<dafny.DafnySequence<? extends Suffixed<D, S>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Suffixed<D, S>> empty(Suffixed.<D, S>_typeDescriptor(_td_D, _td_S)));
  }
}
