// Class RelativeTime
// Dafny class RelativeTime compiled into Java
package Time;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class RelativeTime {
  public long _ClockTime;
  public long _CpuTime;
  public RelativeTime (long ClockTime, long CpuTime) {
    this._ClockTime = ClockTime;
    this._CpuTime = CpuTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RelativeTime o = (RelativeTime)other;
    return true && this._ClockTime == o._ClockTime && this._CpuTime == o._CpuTime;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._ClockTime);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._CpuTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Time.RelativeTime.RelativeTime");
    s.append("(");
    s.append(this._ClockTime);
    s.append(", ");
    s.append(this._CpuTime);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RelativeTime> _TYPE = dafny.TypeDescriptor.<RelativeTime>referenceWithInitializer(RelativeTime.class, () -> RelativeTime.Default());
  public static dafny.TypeDescriptor<RelativeTime> _typeDescriptor() {
    return (dafny.TypeDescriptor<RelativeTime>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RelativeTime theDefault = Time.RelativeTime.create(0L, 0L);
  public static RelativeTime Default() {
    return theDefault;
  }
  public static RelativeTime create(long ClockTime, long CpuTime) {
    return new RelativeTime(ClockTime, CpuTime);
  }
  public static RelativeTime create_RelativeTime(long ClockTime, long CpuTime) {
    return create(ClockTime, CpuTime);
  }
  public boolean is_RelativeTime() { return true; }
  public long dtor_ClockTime() {
    return this._ClockTime;
  }
  public long dtor_CpuTime() {
    return this._CpuTime;
  }
}
