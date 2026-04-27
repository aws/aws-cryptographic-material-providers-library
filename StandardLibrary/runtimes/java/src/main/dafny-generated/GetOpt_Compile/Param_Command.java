// Class Param_Command
// Dafny class Param_Command compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Param_Command extends Param {
  public Options _options;
  public Param_Command (Options options) {
    super();
    this._options = options;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Param_Command o = (Param_Command)other;
    return true && java.util.Objects.equals(this._options, o._options);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._options);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Param.Command");
    s.append("(");
    s.append(dafny.Helpers.toString(this._options));
    s.append(")");
    return s.toString();
  }
}
