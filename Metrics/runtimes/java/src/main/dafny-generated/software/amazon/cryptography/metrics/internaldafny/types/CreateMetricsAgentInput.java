// Class CreateMetricsAgentInput
// Dafny class CreateMetricsAgentInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateMetricsAgentInput {
  public dafny.DafnySequence<? extends IMetricsAgent> _metricsAgents;
  public CreateMetricsAgentInput (dafny.DafnySequence<? extends IMetricsAgent> metricsAgents) {
    this._metricsAgents = metricsAgents;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateMetricsAgentInput o = (CreateMetricsAgentInput)other;
    return true && java.util.Objects.equals(this._metricsAgents, o._metricsAgents);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._metricsAgents);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.CreateMetricsAgentInput.CreateMetricsAgentInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._metricsAgents));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateMetricsAgentInput> _TYPE = dafny.TypeDescriptor.<CreateMetricsAgentInput>referenceWithInitializer(CreateMetricsAgentInput.class, () -> CreateMetricsAgentInput.Default());
  public static dafny.TypeDescriptor<CreateMetricsAgentInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateMetricsAgentInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateMetricsAgentInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput.create(dafny.DafnySequence.<IMetricsAgent> empty(((dafny.TypeDescriptor<IMetricsAgent>)(java.lang.Object)dafny.TypeDescriptor.reference(IMetricsAgent.class))));
  public static CreateMetricsAgentInput Default() {
    return theDefault;
  }
  public static CreateMetricsAgentInput create(dafny.DafnySequence<? extends IMetricsAgent> metricsAgents) {
    return new CreateMetricsAgentInput(metricsAgents);
  }
  public static CreateMetricsAgentInput create_CreateMetricsAgentInput(dafny.DafnySequence<? extends IMetricsAgent> metricsAgents) {
    return create(metricsAgents);
  }
  public boolean is_CreateMetricsAgentInput() { return true; }
  public dafny.DafnySequence<? extends IMetricsAgent> dtor_metricsAgents() {
    return this._metricsAgents;
  }
}
