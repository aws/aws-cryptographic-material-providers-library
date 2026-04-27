// Class Chain_Empty
// Dafny class Chain_Empty compiled into Java
package JSON_mUtils_mViews_mWriters_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Chain_Empty extends Chain {
  public Chain_Empty () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Chain_Empty o = (Chain_Empty)other;
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
    s.append("Writers.Chain.Empty");
    return s.toString();
  }
}
