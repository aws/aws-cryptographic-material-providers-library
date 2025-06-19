// Class Maybe_Empty<T>
// Dafny class Maybe_Empty<T> compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Maybe_Empty<T> extends Maybe<T> {
  public Maybe_Empty (dafny.TypeDescriptor<T> _td_T) {
    super(_td_T);
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Maybe_Empty<T> o = (Maybe_Empty<T>)other;
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
    s.append("Grammar.Maybe.Empty");
    return s.toString();
  }
}
