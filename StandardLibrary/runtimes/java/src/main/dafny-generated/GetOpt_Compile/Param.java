// Class Param
// Dafny class Param compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Param {
  public Param() {
  }
  private static final dafny.TypeDescriptor<Param> _TYPE = dafny.TypeDescriptor.<Param>referenceWithInitializer(Param.class, () -> Param.Default());
  public static dafny.TypeDescriptor<Param> _typeDescriptor() {
    return (dafny.TypeDescriptor<Param>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Param theDefault = Param.create_Opt(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), 'D', Unused.Default(), false, Visibility.Default(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Tri.Default());
  public static Param Default() {
    return theDefault;
  }
  public static Param create_Opt(dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, dafny.DafnySequence<? extends Character> argName, char short_, Unused unused, boolean inherit, Visibility vis, dafny.DafnySequence<? extends Character> shortAlias, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> longAlias, Tri positional) {
    return new Param_Opt(name, help, argName, short_, unused, inherit, vis, shortAlias, longAlias, positional);
  }
  public static Param create_Flag(dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends Character> help, char short_, boolean solo, boolean inherit, Visibility vis, dafny.DafnySequence<? extends Character> shortAlias, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> longAlias) {
    return new Param_Flag(name, help, short_, solo, inherit, vis, shortAlias, longAlias);
  }
  public static Param create_Command(Options options) {
    return new Param_Command(options);
  }
  public boolean is_Opt() { return this instanceof Param_Opt; }
  public boolean is_Flag() { return this instanceof Param_Flag; }
  public boolean is_Command() { return this instanceof Param_Command; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._name; }
    return ((Param_Flag)d)._name;
  }
  public dafny.DafnySequence<? extends Character> dtor_help() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._help; }
    return ((Param_Flag)d)._help;
  }
  public dafny.DafnySequence<? extends Character> dtor_argName() {
    Param d = this;
    return ((Param_Opt)d)._argName;
  }
  public char dtor_short() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._short; }
    return ((Param_Flag)d)._short;
  }
  public Unused dtor_unused() {
    Param d = this;
    return ((Param_Opt)d)._unused;
  }
  public boolean dtor_inherit() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._inherit; }
    return ((Param_Flag)d)._inherit;
  }
  public Visibility dtor_vis() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._vis; }
    return ((Param_Flag)d)._vis;
  }
  public dafny.DafnySequence<? extends Character> dtor_shortAlias() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._shortAlias; }
    return ((Param_Flag)d)._shortAlias;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_longAlias() {
    Param d = this;
    if (d instanceof Param_Opt) { return ((Param_Opt)d)._longAlias; }
    return ((Param_Flag)d)._longAlias;
  }
  public Tri dtor_positional() {
    Param d = this;
    return ((Param_Opt)d)._positional;
  }
  public boolean dtor_solo() {
    Param d = this;
    return ((Param_Flag)d)._solo;
  }
  public Options dtor_options() {
    Param d = this;
    return ((Param_Command)d)._options;
  }
  public boolean NeedsArg() {
    return (this).is_Opt();
  }
  public boolean Inherits() {
    return (((this).is_Opt()) || ((this).is_Flag())) && ((this).dtor_inherit());
  }
  public boolean ShowHelp() {
    return ((this).is_Command()) || (java.util.Objects.equals((this).dtor_vis(), Visibility.create_Normal()));
  }
  public boolean KeepResult() {
    return ((this).is_Command()) || (!java.util.Objects.equals((this).dtor_vis(), Visibility.create_Deprecated()));
  }
  public dafny.DafnySequence<? extends Character> Name() {
    if ((this).is_Command()) {
      return ((this).dtor_options()).dtor_name();
    } else {
      return (this).dtor_name();
    }
  }
  public dafny.DafnySequence<? extends OneArg> MakeArg(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> value) {
    if ((this).KeepResult()) {
      return dafny.DafnySequence.<OneArg> of(OneArg._typeDescriptor(), OneArg.create((this).Name(), value));
    } else {
      return dafny.DafnySequence.<OneArg> empty(OneArg._typeDescriptor());
    }
  }
  public dafny.DafnySequence<? extends Character> ShortAlias() {
    if ((this).is_Command()) {
      return dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    } else {
      return (this).dtor_shortAlias();
    }
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> LongAlias() {
    if ((this).is_Command()) {
      return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      return (this).dtor_longAlias();
    }
  }
  public boolean Required() {
    return ((this).is_Opt()) && (((this).dtor_unused()).is_Required());
  }
  public boolean HasDefault() {
    return ((this).is_Opt()) && (((this).dtor_unused()).is_Default());
  }
}
