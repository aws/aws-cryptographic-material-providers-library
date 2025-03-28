// Class _ExternBase___default
// Dafny class __default compiled into Java
package OsLang;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static dafny.DafnySequence<? extends Character> GetPlatformShort() {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(__default.GetLanguageShort(), dafny.DafnySequence.asString(" ")), __default.GetOsShort());
  }
  public static dafny.DafnySequence<? extends Character> GetPlatformLong() {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(__default.GetLanguageLong(), dafny.DafnySequence.asString(" ")), __default.GetOsLong());
  }
  @Override
  public java.lang.String toString() {
    return "OsLang._default";
  }
}
