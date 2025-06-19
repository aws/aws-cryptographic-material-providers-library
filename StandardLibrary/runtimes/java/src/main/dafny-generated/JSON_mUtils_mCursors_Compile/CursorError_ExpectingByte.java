// Class CursorError_ExpectingByte<R>
// Dafny class CursorError_ExpectingByte<R> compiled into Java
package JSON_mUtils_mCursors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CursorError_ExpectingByte<R> extends CursorError<R> {
  public byte _expected;
  public short _b;
  public CursorError_ExpectingByte (dafny.TypeDescriptor<R> _td_R, byte expected, short b) {
    super(_td_R);
    this._expected = expected;
    this._b = b;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CursorError_ExpectingByte<R> o = (CursorError_ExpectingByte<R>)other;
    return true && this._expected == o._expected && this._b == o._b;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.lang.Byte.hashCode(this._expected);
    hash = ((hash << 5) + hash) + java.lang.Short.hashCode(this._b);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Cursors.CursorError.ExpectingByte");
    s.append("(");
    s.append(this._expected);
    s.append(", ");
    s.append(this._b);
    s.append(")");
    return s.toString();
  }
}
