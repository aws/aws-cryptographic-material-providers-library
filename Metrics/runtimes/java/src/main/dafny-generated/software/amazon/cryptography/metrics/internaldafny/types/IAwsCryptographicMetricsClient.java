// Interface IAwsCryptographicMetricsClient
// Dafny trait IAwsCryptographicMetricsClient compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface IAwsCryptographicMetricsClient {
  public Wrappers_Compile.Result<CreateMetricsAgentOutput, Error> CreateTextMetricsAgent(CreateTextMetricsAgentInput input);
  public Wrappers_Compile.Result<CreateMetricsAgentOutput, Error> CreateMultiMetricsAgent(CreateMetricsAgentInput input);
}
