// Interface MutableMapTrait
// Dafny trait MutableMapTrait compiled into Java
package DafnyLibraries;

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

@SuppressWarnings({"unchecked", "deprecation"})
public interface MutableMapTrait<K, V> {
  public dafny.DafnyMap<? extends K, ? extends V> content();
  public void Put(K k, V v);
  public dafny.DafnySet<? extends K> Keys();
  public boolean HasKey(K k);
  public dafny.DafnySet<? extends V> Values();
  public dafny.DafnySet<? extends dafny.Tuple2<K, V>> Items();
  public V Select(K k);
  public void Remove(K k);
  public java.math.BigInteger Size();
}
