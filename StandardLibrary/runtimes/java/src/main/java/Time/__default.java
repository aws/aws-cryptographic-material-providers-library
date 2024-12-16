package Time;

import Wrappers_Compile.Result;
import com.sun.management.OperatingSystemMXBean;
import dafny.DafnySequence;
import java.lang.management.ManagementFactory;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

public class __default extends Time._ExternBase___default {

  public static Long CurrentRelativeTime() {
    return System.currentTimeMillis() / 1000;
  }

  public static Long CurrentRelativeTimeMilli() {
    return System.currentTimeMillis();
  }

  public static Long GetProcessCpuTimeMillis() {
    OperatingSystemMXBean bean =
      (com.sun.management.OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
    return new Long(bean.getProcessCpuTime() / 1000000);
  }

  public static Result<
    DafnySequence<? extends Character>,
    DafnySequence<? extends Character>
  > GetCurrentTimeStamp() {
    try {
      TimeZone tz = TimeZone.getTimeZone("UTC");
      DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'"); // Quoted "Z" to indicate UTC, no timezone offset
      df.setTimeZone(tz);
      return CreateGetCurrentTimeStampSuccess(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          df.format(new Date())
        )
      );
    } catch (Exception var1) {
      return CreateGetCurrentTimeStampFailure(
        software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
          "Could not generate a timestamp in ISO8601."
        )
      );
    }
  }
}
