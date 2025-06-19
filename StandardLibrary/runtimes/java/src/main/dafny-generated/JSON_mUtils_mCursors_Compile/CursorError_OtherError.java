// Class CursorError_OtherError<R>
// Dafny class CursorError_OtherError<R> compiled into Java
package JSON_mUtils_mCursors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CursorError_OtherError<R> extends CursorError<R> {
  public R _err;
  public CursorError_OtherError (dafny.TypeDescriptor<R> _td_R, R err) {
    super(_td_R);
    this._err = err;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CursorError_OtherError<R> o = (CursorError_OtherError<R>)other;
    return true && java.util.Objects.equals(this._err, o._err);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._err);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Cursors.CursorError.OtherError");
    s.append("(");
    s.append(dafny.Helpers.toString(this._err));
    s.append(")");
    return s.toString();
  }
}
