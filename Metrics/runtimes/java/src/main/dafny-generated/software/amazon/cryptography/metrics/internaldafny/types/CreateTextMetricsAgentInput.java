// Class CreateTextMetricsAgentInput
// Dafny class CreateTextMetricsAgentInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateTextMetricsAgentInput {
  public dafny.DafnySequence<? extends Character> _fileName;
  public CreateTextMetricsAgentInput (dafny.DafnySequence<? extends Character> fileName) {
    this._fileName = fileName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateTextMetricsAgentInput o = (CreateTextMetricsAgentInput)other;
    return true && java.util.Objects.equals(this._fileName, o._fileName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._fileName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.CreateTextMetricsAgentInput.CreateTextMetricsAgentInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._fileName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateTextMetricsAgentInput> _TYPE = dafny.TypeDescriptor.<CreateTextMetricsAgentInput>referenceWithInitializer(CreateTextMetricsAgentInput.class, () -> CreateTextMetricsAgentInput.Default());
  public static dafny.TypeDescriptor<CreateTextMetricsAgentInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateTextMetricsAgentInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateTextMetricsAgentInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.CreateTextMetricsAgentInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateTextMetricsAgentInput Default() {
    return theDefault;
  }
  public static CreateTextMetricsAgentInput create(dafny.DafnySequence<? extends Character> fileName) {
    return new CreateTextMetricsAgentInput(fileName);
  }
  public static CreateTextMetricsAgentInput create_CreateTextMetricsAgentInput(dafny.DafnySequence<? extends Character> fileName) {
    return create(fileName);
  }
  public boolean is_CreateTextMetricsAgentInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_fileName() {
    return this._fileName;
  }
}
