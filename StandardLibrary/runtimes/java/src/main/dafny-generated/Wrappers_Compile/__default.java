// Class __default
// Dafny class __default compiled into Java
package Wrappers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__E> Outcome<__E> Need(dafny.TypeDescriptor<__E> _td___E, boolean condition, __E error)
  {
    if (condition) {
      return Outcome.<__E>create_Pass(_td___E);
    } else {
      return Outcome.<__E>create_Fail(_td___E, error);
    }
  }
  public static <__E> Outcome<__E> FNeed(dafny.TypeDescriptor<__E> _td___E, boolean condition, dafny.Function0<__E> error)
  {
    if (condition) {
      return Outcome.<__E>create_Pass(_td___E);
    } else {
      return Outcome.<__E>create_Fail(_td___E, ((__E)(java.lang.Object)((error).apply())));
    }
  }
  @Override
  public java.lang.String toString() {
    return "Wrappers._default";
  }
}
