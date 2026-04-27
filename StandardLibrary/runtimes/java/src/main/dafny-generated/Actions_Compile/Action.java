// Interface Action
// Dafny trait Action compiled into Java
package Actions_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public interface Action<A, R> {
  public R Invoke(A a);
}
