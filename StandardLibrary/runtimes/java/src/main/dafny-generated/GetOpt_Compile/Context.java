// Class Context
// Dafny class Context compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Context {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> _longMap;
  public dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> _shortMap;
  public dafny.DafnySequence<? extends Param> _inherits;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _commands;
  public dafny.DafnySequence<? extends Character> _command;
  public Context (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnySequence<? extends Param> inherits, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> commands, dafny.DafnySequence<? extends Character> command) {
    this._longMap = longMap;
    this._shortMap = shortMap;
    this._inherits = inherits;
    this._commands = commands;
    this._command = command;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Context o = (Context)other;
    return true && java.util.Objects.equals(this._longMap, o._longMap) && java.util.Objects.equals(this._shortMap, o._shortMap) && java.util.Objects.equals(this._inherits, o._inherits) && java.util.Objects.equals(this._commands, o._commands) && java.util.Objects.equals(this._command, o._command);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._longMap);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._shortMap);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._inherits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commands);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._command);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.Context.Context");
    s.append("(");
    s.append(dafny.Helpers.toString(this._longMap));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._shortMap));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._inherits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commands));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._command));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Context> _TYPE = dafny.TypeDescriptor.<Context>referenceWithInitializer(Context.class, () -> Context.Default());
  public static dafny.TypeDescriptor<Context> _typeDescriptor() {
    return (dafny.TypeDescriptor<Context>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Context theDefault = Context.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,Param> empty(), dafny.DafnyMap.<Character,dafny.DafnySequence<? extends Character>> empty(), dafny.DafnySequence.<Param> empty(Param._typeDescriptor()), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,Options> empty(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static Context Default() {
    return theDefault;
  }
  public static Context create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnySequence<? extends Param> inherits, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> commands, dafny.DafnySequence<? extends Character> command) {
    return new Context(longMap, shortMap, inherits, commands, command);
  }
  public static Context create_Context(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> longMap, dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> shortMap, dafny.DafnySequence<? extends Param> inherits, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> commands, dafny.DafnySequence<? extends Character> command) {
    return create(longMap, shortMap, inherits, commands, command);
  }
  public boolean is_Context() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Param> dtor_longMap() {
    return this._longMap;
  }
  public dafny.DafnyMap<? extends Character, ? extends dafny.DafnySequence<? extends Character>> dtor_shortMap() {
    return this._shortMap;
  }
  public dafny.DafnySequence<? extends Param> dtor_inherits() {
    return this._inherits;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> dtor_commands() {
    return this._commands;
  }
  public dafny.DafnySequence<? extends Character> dtor_command() {
    return this._command;
  }
}
