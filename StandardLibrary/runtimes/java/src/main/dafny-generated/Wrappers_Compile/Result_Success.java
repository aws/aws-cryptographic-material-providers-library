// Class Result_Success<T, R>
// Dafny class Result_Success<T, R> compiled into Java
package Wrappers_Compile;


@SuppressWarnings({"unchecked", "deprecation"})
public class Result_Success<T, R> extends Result<T, R> {
  public T _value;
  public Result_Success (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T value) {
    super(_td_T, _td_R);
    this._value = value;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Result_Success<T, R> o = (Result_Success<T, R>)other;
    return true && java.util.Objects.equals(this._value, o._value);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._value);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Wrappers.Result.Success");
    s.append("(");
    s.append(dafny.Helpers.toString(this._value));
    s.append(")");
    return s.toString();
  }
}
