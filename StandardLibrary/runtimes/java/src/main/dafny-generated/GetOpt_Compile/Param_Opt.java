// Class Param_Opt
// Dafny class Param_Opt compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Param_Opt extends Param {
  public dafny.DafnySequence<? extends Character> _name;
  public dafny.DafnySequence<? extends Character> _help;
  public dafny.DafnySequence<? extends Character> _argName;
  public char _short;
  public Unused _unused;
  public boolean _inherit;
  public Visibility _vis;
  public dafny.DafnySequence<? extends Character> _shortAlias;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _longAlias;
  public Tri _positional;
  public Param_Opt (dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, dafny.DafnySequence<? extends Character> argName, char short_, Unused unused, boolean inherit, Visibility vis, dafny.DafnySequence<? extends Character> shortAlias, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> longAlias, Tri positional) {
    super();
    this._name = name;
    this._help = help;
    this._argName = argName;
    this._short = short_;
    this._unused = unused;
    this._inherit = inherit;
    this._vis = vis;
    this._shortAlias = shortAlias;
    this._longAlias = longAlias;
    this._positional = positional;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Param_Opt o = (Param_Opt)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._help, o._help) && java.util.Objects.equals(this._argName, o._argName) && this._short == o._short && java.util.Objects.equals(this._unused, o._unused) && this._inherit == o._inherit && java.util.Objects.equals(this._vis, o._vis) && java.util.Objects.equals(this._shortAlias, o._shortAlias) && java.util.Objects.equals(this._longAlias, o._longAlias) && java.util.Objects.equals(this._positional, o._positional);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._help);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._argName);
    hash = ((hash << 5) + hash) + Character.hashCode(this._short);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._unused);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._inherit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._vis);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._shortAlias);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._longAlias);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._positional);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Param.Opt");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._help));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._argName));
    s.append(", ");
    s.append(this._short);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._unused));
    s.append(", ");
    s.append(this._inherit);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._vis));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._shortAlias));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._longAlias));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._positional));
    s.append(")");
    return s.toString();
  }
}
