// Class Maybe_NonEmpty<T>
// Dafny class Maybe_NonEmpty<T> compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Maybe_NonEmpty<T> extends Maybe<T> {
  public T _t;
  public Maybe_NonEmpty (dafny.TypeDescriptor<T> _td_T, T t) {
    super(_td_T);
    this._t = t;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Maybe_NonEmpty<T> o = (Maybe_NonEmpty<T>)other;
    return true && java.util.Objects.equals(this._t, o._t);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._t);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Maybe.NonEmpty");
    s.append("(");
    s.append(dafny.Helpers.toString(this._t));
    s.append(")");
    return s.toString();
  }
}
