// Class Tri_No
// Dafny class Tri_No compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Tri_No extends Tri {
  public Tri_No () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Tri_No o = (Tri_No)other;
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
    s.append("GetOpt.Tri.No");
    return s.toString();
  }
}
