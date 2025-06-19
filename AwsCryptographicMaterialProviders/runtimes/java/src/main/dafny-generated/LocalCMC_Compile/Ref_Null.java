// Class Ref_Null<T>
// Dafny class Ref_Null<T> compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Ref_Null<T> extends Ref<T> {
  public Ref_Null (dafny.TypeDescriptor<T> _td_T) {
    super(_td_T);
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Ref_Null<T> o = (Ref_Null<T>)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("LocalCMC.Ref.Null");
    return s.toString();
  }
}
