// Class PutDateInput
// Dafny class PutDateInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutDateInput {
  public dafny.DafnySequence<? extends Character> _description;
  public dafny.DafnySequence<? extends Character> _date;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _transactionId;
  public PutDateInput (dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> date, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    this._description = description;
    this._date = date;
    this._transactionId = transactionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutDateInput o = (PutDateInput)other;
    return true && java.util.Objects.equals(this._description, o._description) && java.util.Objects.equals(this._date, o._date) && java.util.Objects.equals(this._transactionId, o._transactionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._date);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._transactionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.PutDateInput.PutDateInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._date));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._transactionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutDateInput> _TYPE = dafny.TypeDescriptor.<PutDateInput>referenceWithInitializer(PutDateInput.class, () -> PutDateInput.Default());
  public static dafny.TypeDescriptor<PutDateInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutDateInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutDateInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutDateInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static PutDateInput Default() {
    return theDefault;
  }
  public static PutDateInput create(dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> date, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return new PutDateInput(description, date, transactionId);
  }
  public static PutDateInput create_PutDateInput(dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> date, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return create(description, date, transactionId);
  }
  public boolean is_PutDateInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_description() {
    return this._description;
  }
  public dafny.DafnySequence<? extends Character> dtor_date() {
    return this._date;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_transactionId() {
    return this._transactionId;
  }
}
