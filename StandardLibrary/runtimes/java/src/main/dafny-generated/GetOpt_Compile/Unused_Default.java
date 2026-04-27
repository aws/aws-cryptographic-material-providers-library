// Class Unused_Default
// Dafny class Unused_Default compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Unused_Default extends Unused {
  public dafny.DafnySequence<? extends Character> _val;
  public Unused_Default (dafny.DafnySequence<? extends Character> val) {
    super();
    this._val = val;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Unused_Default o = (Unused_Default)other;
    return true && java.util.Objects.equals(this._val, o._val);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._val);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Unused.Default");
    s.append("(");
    s.append(dafny.Helpers.toString(this._val));
    s.append(")");
    return s.toString();
  }
}
