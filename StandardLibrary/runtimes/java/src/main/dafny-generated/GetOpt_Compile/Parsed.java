// Class Parsed
// Dafny class Parsed compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Parsed {
  public dafny.DafnySequence<? extends Character> _command;
  public dafny.DafnySequence<? extends OneArg> _params;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _files;
  public Wrappers_Compile.Option<Parsed> _subcommand;
  public Parsed (dafny.DafnySequence<? extends Character> command, dafny.DafnySequence<? extends OneArg> params, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> files, Wrappers_Compile.Option<Parsed> subcommand) {
    this._command = command;
    this._params = params;
    this._files = files;
    this._subcommand = subcommand;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Parsed o = (Parsed)other;
    return true && java.util.Objects.equals(this._command, o._command) && java.util.Objects.equals(this._params, o._params) && java.util.Objects.equals(this._files, o._files) && java.util.Objects.equals(this._subcommand, o._subcommand);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._command);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._params);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._files);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._subcommand);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Parsed.Parsed");
    s.append("(");
    s.append(dafny.Helpers.toString(this._command));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._params));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._files));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._subcommand));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Parsed> _TYPE = dafny.TypeDescriptor.<Parsed>referenceWithInitializer(Parsed.class, () -> Parsed.Default());
  public static dafny.TypeDescriptor<Parsed> _typeDescriptor() {
    return (dafny.TypeDescriptor<Parsed>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Parsed theDefault = Parsed.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<Parsed>Default(Parsed._typeDescriptor()));
  public static Parsed Default() {
    return theDefault;
  }
  public static Parsed create(dafny.DafnySequence<? extends Character> command, dafny.DafnySequence<? extends OneArg> params, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> files, Wrappers_Compile.Option<Parsed> subcommand) {
    return new Parsed(command, params, files, subcommand);
  }
  public static Parsed create_Parsed(dafny.DafnySequence<? extends Character> command, dafny.DafnySequence<? extends OneArg> params, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> files, Wrappers_Compile.Option<Parsed> subcommand) {
    return create(command, params, files, subcommand);
  }
  public boolean is_Parsed() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_command() {
    return this._command;
  }
  public dafny.DafnySequence<? extends OneArg> dtor_params() {
    return this._params;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_files() {
    return this._files;
  }
  public Wrappers_Compile.Option<Parsed> dtor_subcommand() {
    return this._subcommand;
  }
}
