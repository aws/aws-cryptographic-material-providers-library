// Class PutTimeInput
// Dafny class PutTimeInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutTimeInput {
  public dafny.DafnySequence<? extends Character> _description;
  public long _duration;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _transactionId;
  public PutTimeInput (dafny.DafnySequence<? extends Character> description, long duration, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    this._description = description;
    this._duration = duration;
    this._transactionId = transactionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutTimeInput o = (PutTimeInput)other;
    return true && java.util.Objects.equals(this._description, o._description) && this._duration == o._duration && java.util.Objects.equals(this._transactionId, o._transactionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._duration);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._transactionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.PutTimeInput.PutTimeInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(this._duration);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._transactionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutTimeInput> _TYPE = dafny.TypeDescriptor.<PutTimeInput>referenceWithInitializer(PutTimeInput.class, () -> PutTimeInput.Default());
  public static dafny.TypeDescriptor<PutTimeInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutTimeInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutTimeInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), 0L, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static PutTimeInput Default() {
    return theDefault;
  }
  public static PutTimeInput create(dafny.DafnySequence<? extends Character> description, long duration, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return new PutTimeInput(description, duration, transactionId);
  }
  public static PutTimeInput create_PutTimeInput(dafny.DafnySequence<? extends Character> description, long duration, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return create(description, duration, transactionId);
  }
  public boolean is_PutTimeInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_description() {
    return this._description;
  }
  public long dtor_duration() {
    return this._duration;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_transactionId() {
    return this._transactionId;
  }
}
