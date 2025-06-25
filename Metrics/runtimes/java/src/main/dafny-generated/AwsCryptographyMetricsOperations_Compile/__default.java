// Class __default
// Dafny class __default compiled into Java
package AwsCryptographyMetricsOperations_Compile;

import software.amazon.cryptography.metrics.internaldafny.types.*;
import MetricsAgent_Compile.*;
import MetricsAgentText.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateTextMetricsAgent(Config config, software.amazon.cryptography.metrics.internaldafny.types.CreateTextMetricsAgentInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.metrics.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.metrics.internaldafny.types.Error>Default(software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.metrics.internaldafny.types.Error>Need(software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf(((input).dtor_fileName()).length())).signum() == 1, software.amazon.cryptography.metrics.internaldafny.types.Error.create_MetricsServiceError(dafny.DafnySequence.asString("Log FileName length MUST be greater than 0.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput>PropagateFailure(software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput._typeDescriptor());
      return output;
    }
    MetricsAgentText.TextLogger _1_logger;
    MetricsAgentText.TextLogger _nw0 = new MetricsAgentText.TextLogger((input).dtor_fileName());
    _1_logger = _nw0;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput.create(_1_logger));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateMultiMetricsAgent(Config config, software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Failure(software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error.create_MetricsServiceError(dafny.DafnySequence.asString("Implement me!")));
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyMetricsOperations._default";
  }
}
