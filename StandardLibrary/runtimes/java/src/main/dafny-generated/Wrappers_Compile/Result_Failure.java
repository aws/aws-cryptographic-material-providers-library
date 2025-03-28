// Class Result_Failure<T, R>
// Dafny class Result_Failure<T, R> compiled into Java
package Wrappers_Compile;


@SuppressWarnings({"unchecked", "deprecation"})
public class Result_Failure<T, R> extends Result<T, R> {
  public R _error;
  public Result_Failure (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, R error) {
    super(_td_T, _td_R);
    this._error = error;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Result_Failure<T, R> o = (Result_Failure<T, R>)other;
    return true && java.util.Objects.equals(this._error, o._error);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._error);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Wrappers.Result.Failure");
    s.append("(");
    s.append(dafny.Helpers.toString(this._error));
    s.append(")");
    return s.toString();
  }
}
