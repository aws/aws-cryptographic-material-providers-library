// Class Unused
// Dafny class Unused compiled into Java
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
public abstract class Unused {
  public Unused() {
  }
  private static final dafny.TypeDescriptor<Unused> _TYPE = dafny.TypeDescriptor.<Unused>referenceWithInitializer(Unused.class, () -> Unused.Default());
  public static dafny.TypeDescriptor<Unused> _typeDescriptor() {
    return (dafny.TypeDescriptor<Unused>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Unused theDefault = GetOpt_Compile.Unused.create_UnusedOk();
  public static Unused Default() {
    return theDefault;
  }
  public static Unused create_UnusedOk() {
    return new Unused_UnusedOk();
  }
  public static Unused create_Required() {
    return new Unused_Required();
  }
  public static Unused create_Default(dafny.DafnySequence<? extends Character> val) {
    return new Unused_Default(val);
  }
  public boolean is_UnusedOk() { return this instanceof Unused_UnusedOk; }
  public boolean is_Required() { return this instanceof Unused_Required; }
  public boolean is_Default() { return this instanceof Unused_Default; }
  public dafny.DafnySequence<? extends Character> dtor_val() {
    Unused d = this;
    return ((Unused_Default)d)._val;
  }
}
