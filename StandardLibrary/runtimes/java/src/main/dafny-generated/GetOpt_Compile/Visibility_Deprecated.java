// Class Visibility_Deprecated
// Dafny class Visibility_Deprecated compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Visibility_Deprecated extends Visibility {
  public Visibility_Deprecated () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Visibility_Deprecated o = (Visibility_Deprecated)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Visibility.Deprecated");
    return s.toString();
  }
}
