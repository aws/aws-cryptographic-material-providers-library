// Class PutPropertyInput
// Dafny class PutPropertyInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutPropertyInput {
  public dafny.DafnySequence<? extends Character> _description;
  public dafny.DafnySequence<? extends Character> _value;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _transactionId;
  public PutPropertyInput (dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> value, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    this._description = description;
    this._value = value;
    this._transactionId = transactionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutPropertyInput o = (PutPropertyInput)other;
    return true && java.util.Objects.equals(this._description, o._description) && java.util.Objects.equals(this._value, o._value) && java.util.Objects.equals(this._transactionId, o._transactionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._value);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._transactionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.PutPropertyInput.PutPropertyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._value));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._transactionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutPropertyInput> _TYPE = dafny.TypeDescriptor.<PutPropertyInput>referenceWithInitializer(PutPropertyInput.class, () -> PutPropertyInput.Default());
  public static dafny.TypeDescriptor<PutPropertyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutPropertyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutPropertyInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static PutPropertyInput Default() {
    return theDefault;
  }
  public static PutPropertyInput create(dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> value, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return new PutPropertyInput(description, value, transactionId);
  }
  public static PutPropertyInput create_PutPropertyInput(dafny.DafnySequence<? extends Character> description, dafny.DafnySequence<? extends Character> value, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return create(description, value, transactionId);
  }
  public boolean is_PutPropertyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_description() {
    return this._description;
  }
  public dafny.DafnySequence<? extends Character> dtor_value() {
    return this._value;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_transactionId() {
    return this._transactionId;
  }
}
