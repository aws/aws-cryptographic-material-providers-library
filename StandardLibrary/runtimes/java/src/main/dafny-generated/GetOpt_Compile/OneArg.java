// Class OneArg
// Dafny class OneArg compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class OneArg {
  public dafny.DafnySequence<? extends Character> _name;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _value;
  public OneArg (dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> value) {
    this._name = name;
    this._value = value;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OneArg o = (OneArg)other;
    return true && java.util.Objects.equals(this._name, o._name) && java.util.Objects.equals(this._value, o._value);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._value);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("GetOpt.OneArg.OneArg");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._value));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OneArg> _TYPE = dafny.TypeDescriptor.<OneArg>referenceWithInitializer(OneArg.class, () -> OneArg.Default());
  public static dafny.TypeDescriptor<OneArg> _typeDescriptor() {
    return (dafny.TypeDescriptor<OneArg>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OneArg theDefault = OneArg.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static OneArg Default() {
    return theDefault;
  }
  public static OneArg create(dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> value) {
    return new OneArg(name, value);
  }
  public static OneArg create_OneArg(dafny.DafnySequence<? extends Character> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> value) {
    return create(name, value);
  }
  public boolean is_OneArg() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_name() {
    return this._name;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_value() {
    return this._value;
  }
}
