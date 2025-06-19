// Class Ref_Ptr<T>
// Dafny class Ref_Ptr<T> compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Ref_Ptr<T> extends Ref<T> {
  public T _deref;
  public Ref_Ptr (dafny.TypeDescriptor<T> _td_T, T deref) {
    super(_td_T);
    this._deref = deref;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Ref_Ptr<T> o = (Ref_Ptr<T>)other;
    return true && java.util.Objects.equals(this._deref, o._deref);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._deref);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("LocalCMC.Ref.Ptr");
    s.append("(");
    s.append(dafny.Helpers.toString(this._deref));
    s.append(")");
    return s.toString();
  }
}
