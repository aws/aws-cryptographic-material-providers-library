// Class MetricsClient
// Dafny class MetricsClient compiled into Java
package software.amazon.cryptography.metrics.internaldafny;

import software.amazon.cryptography.metrics.internaldafny.types.*;
import MetricsAgent_Compile.*;
import MetricsAgentText.*;
import AwsCryptographyMetricsOperations_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class MetricsClient implements software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient {
  public MetricsClient() {
    this._config = AwsCryptographyMetricsOperations_Compile.Config.Default();
  }
  public void __ctor(AwsCryptographyMetricsOperations_Compile.Config config)
  {
    (this)._config = config;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateTextMetricsAgent(software.amazon.cryptography.metrics.internaldafny.types.CreateTextMetricsAgentInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMetricsOperations_Compile.__default.CreateTextMetricsAgent((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateMultiMetricsAgent(software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMetricsOperations_Compile.__default.CreateMultiMetricsAgent((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public AwsCryptographyMetricsOperations_Compile.Config _config;
  public AwsCryptographyMetricsOperations_Compile.Config config()
  {
    return this._config;
  }
  private static final dafny.TypeDescriptor<MetricsClient> _TYPE = dafny.TypeDescriptor.<MetricsClient>referenceWithInitializer(MetricsClient.class, () -> (MetricsClient) null);
  public static dafny.TypeDescriptor<MetricsClient> _typeDescriptor() {
    return (dafny.TypeDescriptor<MetricsClient>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "Metrics.MetricsClient";
  }
}
