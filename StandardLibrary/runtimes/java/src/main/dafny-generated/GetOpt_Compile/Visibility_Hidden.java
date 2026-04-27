// Class Visibility_Hidden
// Dafny class Visibility_Hidden compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Visibility_Hidden extends Visibility {
  public Visibility_Hidden () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Visibility_Hidden o = (Visibility_Hidden)other;
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
    s.append("GetOpt.Visibility.Hidden");
    return s.toString();
  }
}
