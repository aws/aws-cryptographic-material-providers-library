// Class Tri
// Dafny class Tri compiled into Java
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
public abstract class Tri {
  public Tri() {
  }
  private static final dafny.TypeDescriptor<Tri> _TYPE = dafny.TypeDescriptor.<Tri>referenceWithInitializer(Tri.class, () -> Tri.Default());
  public static dafny.TypeDescriptor<Tri> _typeDescriptor() {
    return (dafny.TypeDescriptor<Tri>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Tri theDefault = GetOpt_Compile.Tri.create_Yes();
  public static Tri Default() {
    return theDefault;
  }
  public static Tri create_Yes() {
    return new Tri_Yes();
  }
  public static Tri create_No() {
    return new Tri_No();
  }
  public static Tri create_Maybe() {
    return new Tri_Maybe();
  }
  public boolean is_Yes() { return this instanceof Tri_Yes; }
  public boolean is_No() { return this instanceof Tri_No; }
  public boolean is_Maybe() { return this instanceof Tri_Maybe; }
  public static java.util.ArrayList<Tri> AllSingletonConstructors() {
    java.util.ArrayList<Tri> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Tri_Yes());
    singleton_iterator.add(new Tri_No());
    singleton_iterator.add(new Tri_Maybe());
    return singleton_iterator;
  }
}
