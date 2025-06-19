// Class CursorError_EOF<R>
// Dafny class CursorError_EOF<R> compiled into Java
package JSON_mUtils_mCursors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CursorError_EOF<R> extends CursorError<R> {
  public CursorError_EOF (dafny.TypeDescriptor<R> _td_R) {
    super(_td_R);
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CursorError_EOF<R> o = (CursorError_EOF<R>)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Cursors.CursorError.EOF");
    return s.toString();
  }
}
