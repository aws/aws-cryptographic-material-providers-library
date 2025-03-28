// Class Visibility
// Dafny class Visibility compiled into Java
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
public abstract class Visibility {
  public Visibility() {
  }
  private static final dafny.TypeDescriptor<Visibility> _TYPE = dafny.TypeDescriptor.<Visibility>referenceWithInitializer(Visibility.class, () -> Visibility.Default());
  public static dafny.TypeDescriptor<Visibility> _typeDescriptor() {
    return (dafny.TypeDescriptor<Visibility>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Visibility theDefault = GetOpt_Compile.Visibility.create_Normal();
  public static Visibility Default() {
    return theDefault;
  }
  public static Visibility create_Normal() {
    return new Visibility_Normal();
  }
  public static Visibility create_Hidden() {
    return new Visibility_Hidden();
  }
  public static Visibility create_Deprecated() {
    return new Visibility_Deprecated();
  }
  public boolean is_Normal() { return this instanceof Visibility_Normal; }
  public boolean is_Hidden() { return this instanceof Visibility_Hidden; }
  public boolean is_Deprecated() { return this instanceof Visibility_Deprecated; }
  public static java.util.ArrayList<Visibility> AllSingletonConstructors() {
    java.util.ArrayList<Visibility> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Visibility_Normal());
    singleton_iterator.add(new Visibility_Hidden());
    singleton_iterator.add(new Visibility_Deprecated());
    return singleton_iterator;
  }
}
