// Class Unused_UnusedOk
// Dafny class Unused_UnusedOk compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Unused_UnusedOk extends Unused {
  public Unused_UnusedOk () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Unused_UnusedOk o = (Unused_UnusedOk)other;
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
    s.append("GetOpt.Unused.UnusedOk");
    return s.toString();
  }
}
