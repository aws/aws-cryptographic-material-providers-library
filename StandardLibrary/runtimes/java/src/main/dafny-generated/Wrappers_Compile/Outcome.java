// Class Outcome<E>
// Dafny class Outcome<E> compiled into Java
package Wrappers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Outcome<E> {
  protected dafny.TypeDescriptor<E> _td_E;
  public Outcome(dafny.TypeDescriptor<E> _td_E) {
    this._td_E = _td_E;
  }
  public static <E> dafny.TypeDescriptor<Outcome<E>> _typeDescriptor(dafny.TypeDescriptor<E> _td_E) {
    return (dafny.TypeDescriptor<Outcome<E>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Outcome<E>>referenceWithInitializer(Outcome.class, () -> Outcome.<E>Default(_td_E));
  }

  public static <E> Outcome<E> Default(dafny.TypeDescriptor<E> _td_E) {
    return Outcome.<E>create_Pass(_td_E);
  }
  @Deprecated()
  public static <E> Outcome<E> Default() {
    dafny.TypeDescriptor<E> _td_E = null;
    return Outcome.<E>create_Pass(_td_E);
  }
  public static <E> Outcome<E> create_Pass(dafny.TypeDescriptor<E> _td_E) {
    return new Outcome_Pass<E>(_td_E);
  }
  @Deprecated()
  public static <E> Outcome<E> create_Pass() {
    return new Outcome_Pass<E>(null);
  }
  public static <E> Outcome<E> create_Fail(dafny.TypeDescriptor<E> _td_E, E error) {
    return new Outcome_Fail<E>(_td_E, error);
  }
  @Deprecated()
  public static <E> Outcome<E> create_Fail(E error) {
    return new Outcome_Fail<E>(null, error);
  }
  public boolean is_Pass() { return this instanceof Outcome_Pass; }
  public boolean is_Fail() { return this instanceof Outcome_Fail; }
  public E dtor_error() {
    Outcome<E> d = this;
    return ((Outcome_Fail<E>)d)._error;
  }
  public boolean IsFailure(dafny.TypeDescriptor<E> _td_E) {
    return (this).is_Fail();
  }
  public <__U> Result<__U, E> PropagateFailure(dafny.TypeDescriptor<E> _td_E, dafny.TypeDescriptor<__U> _td___U)
  {
    return Result.<__U, E>create_Failure(_td___U, _td_E, (this).dtor_error());
  }
}
