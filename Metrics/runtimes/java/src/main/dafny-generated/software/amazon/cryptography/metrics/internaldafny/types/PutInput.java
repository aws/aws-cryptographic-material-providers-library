// Class PutInput
// Dafny class PutInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutInput {
  public dafny.DafnySequence<? extends Character> _message;
  public PutInput (dafny.DafnySequence<? extends Character> message) {
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutInput o = (PutInput)other;
    return true && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.PutInput.PutInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutInput> _TYPE = dafny.TypeDescriptor.<PutInput>referenceWithInitializer(PutInput.class, () -> PutInput.Default());
  public static dafny.TypeDescriptor<PutInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static PutInput Default() {
    return theDefault;
  }
  public static PutInput create(dafny.DafnySequence<? extends Character> message) {
    return new PutInput(message);
  }
  public static PutInput create_PutInput(dafny.DafnySequence<? extends Character> message) {
    return create(message);
  }
  public boolean is_PutInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_message() {
    return this._message;
  }
}
