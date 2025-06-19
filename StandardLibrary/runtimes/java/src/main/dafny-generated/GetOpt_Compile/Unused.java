// Class Unused
// Dafny class Unused compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Unused {
  public Unused() {
  }
  private static final dafny.TypeDescriptor<Unused> _TYPE = dafny.TypeDescriptor.<Unused>referenceWithInitializer(Unused.class, () -> Unused.Default());
  public static dafny.TypeDescriptor<Unused> _typeDescriptor() {
    return (dafny.TypeDescriptor<Unused>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Unused theDefault = Unused.create_UnusedOk();
  public static Unused Default() {
    return theDefault;
  }
  public static Unused create_UnusedOk() {
    return new Unused_UnusedOk();
  }
  public static Unused create_Required() {
    return new Unused_Required();
  }
  public static Unused create_Default(dafny.DafnySequence<? extends Character> val) {
    return new Unused_Default(val);
  }
  public boolean is_UnusedOk() { return this instanceof Unused_UnusedOk; }
  public boolean is_Required() { return this instanceof Unused_Required; }
  public boolean is_Default() { return this instanceof Unused_Default; }
  public dafny.DafnySequence<? extends Character> dtor_val() {
    Unused d = this;
    return ((Unused_Default)d)._val;
  }
}
