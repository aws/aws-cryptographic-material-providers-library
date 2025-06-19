// Interface Callee
// Dafny trait Callee compiled into Java
package ConcurrentCall;

@SuppressWarnings({"unchecked", "deprecation"})
public interface Callee {
  public void call(int serialPos, int concurrentPos);
}
