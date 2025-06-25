// Class CreateMetricsAgentOutput
// Dafny class CreateMetricsAgentOutput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateMetricsAgentOutput {
  public IMetricsAgent _metricsAgent;
  public CreateMetricsAgentOutput (IMetricsAgent metricsAgent) {
    this._metricsAgent = metricsAgent;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateMetricsAgentOutput o = (CreateMetricsAgentOutput)other;
    return true && this._metricsAgent == o._metricsAgent;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._metricsAgent);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.CreateMetricsAgentOutput.CreateMetricsAgentOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._metricsAgent));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateMetricsAgentOutput> _TYPE = dafny.TypeDescriptor.<CreateMetricsAgentOutput>referenceWithInitializer(CreateMetricsAgentOutput.class, () -> CreateMetricsAgentOutput.Default());
  public static dafny.TypeDescriptor<CreateMetricsAgentOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateMetricsAgentOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateMetricsAgentOutput theDefault = software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput.create(null);
  public static CreateMetricsAgentOutput Default() {
    return theDefault;
  }
  public static CreateMetricsAgentOutput create(IMetricsAgent metricsAgent) {
    return new CreateMetricsAgentOutput(metricsAgent);
  }
  public static CreateMetricsAgentOutput create_CreateMetricsAgentOutput(IMetricsAgent metricsAgent) {
    return create(metricsAgent);
  }
  public boolean is_CreateMetricsAgentOutput() { return true; }
  public IMetricsAgent dtor_metricsAgent() {
    return this._metricsAgent;
  }
}
