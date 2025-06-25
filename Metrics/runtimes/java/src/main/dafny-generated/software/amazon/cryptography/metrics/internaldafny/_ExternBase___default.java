// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.metrics.internaldafny;

import software.amazon.cryptography.metrics.internaldafny.types.*;
import MetricsAgent_Compile.*;
import MetricsAgentText.*;
import AwsCryptographyMetricsOperations_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig DefaultMetricsConfig() {
    return software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig.create();
  }
  public static Wrappers_Compile.Result<MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> Metrics(software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig config)
  {
    Wrappers_Compile.Result<MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> res = (Wrappers_Compile.Result<MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    MetricsClient _0_logger;
    MetricsClient _nw0 = new MetricsClient();
    _nw0.__ctor(AwsCryptographyMetricsOperations_Compile.Config.create());
    _0_logger = _nw0;
    res = Wrappers_Compile.Result.<MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MetricsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(MetricsClient.class)), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), _0_logger);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient.class)), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.metrics.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient.class)), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "Metrics._default";
  }
}
