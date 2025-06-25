// Class PutCountInput
// Dafny class PutCountInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutCountInput {
  public dafny.DafnySequence<? extends Character> _description;
  public long _count;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _transactionId;
  public PutCountInput (dafny.DafnySequence<? extends Character> description, long count, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    this._description = description;
    this._count = count;
    this._transactionId = transactionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutCountInput o = (PutCountInput)other;
    return true && java.util.Objects.equals(this._description, o._description) && this._count == o._count && java.util.Objects.equals(this._transactionId, o._transactionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._count);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._transactionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.PutCountInput.PutCountInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(this._count);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._transactionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutCountInput> _TYPE = dafny.TypeDescriptor.<PutCountInput>referenceWithInitializer(PutCountInput.class, () -> PutCountInput.Default());
  public static dafny.TypeDescriptor<PutCountInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutCountInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutCountInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutCountInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), 0L, Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static PutCountInput Default() {
    return theDefault;
  }
  public static PutCountInput create(dafny.DafnySequence<? extends Character> description, long count, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return new PutCountInput(description, count, transactionId);
  }
  public static PutCountInput create_PutCountInput(dafny.DafnySequence<? extends Character> description, long count, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> transactionId) {
    return create(description, count, transactionId);
  }
  public boolean is_PutCountInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_description() {
    return this._description;
  }
  public long dtor_count() {
    return this._count;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_transactionId() {
    return this._transactionId;
  }
}
