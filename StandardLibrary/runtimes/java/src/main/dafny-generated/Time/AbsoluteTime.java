// Class AbsoluteTime
// Dafny class AbsoluteTime compiled into Java
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
public class AbsoluteTime {
  public long _ClockTime;
  public long _CpuTime;
  public AbsoluteTime (long ClockTime, long CpuTime) {
    this._ClockTime = ClockTime;
    this._CpuTime = CpuTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AbsoluteTime o = (AbsoluteTime)other;
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
    s.append("Time.AbsoluteTime.AbsoluteTime");
    s.append("(");
    s.append(this._ClockTime);
    s.append(", ");
    s.append(this._CpuTime);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AbsoluteTime> _TYPE = dafny.TypeDescriptor.<AbsoluteTime>referenceWithInitializer(AbsoluteTime.class, () -> AbsoluteTime.Default());
  public static dafny.TypeDescriptor<AbsoluteTime> _typeDescriptor() {
    return (dafny.TypeDescriptor<AbsoluteTime>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AbsoluteTime theDefault = Time.AbsoluteTime.create(0L, 0L);
  public static AbsoluteTime Default() {
    return theDefault;
  }
  public static AbsoluteTime create(long ClockTime, long CpuTime) {
    return new AbsoluteTime(ClockTime, CpuTime);
  }
  public static AbsoluteTime create_AbsoluteTime(long ClockTime, long CpuTime) {
    return create(ClockTime, CpuTime);
  }
  public boolean is_AbsoluteTime() { return true; }
  public long dtor_ClockTime() {
    return this._ClockTime;
  }
  public long dtor_CpuTime() {
    return this._CpuTime;
  }
}
