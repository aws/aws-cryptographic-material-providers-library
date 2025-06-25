// Class __default
// Dafny class __default compiled into Java
package TestMetricsAgentText_Compile;


@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestCreateTextMetricsAgent()
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.MetricsClient, software.amazon.cryptography.metrics.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.metrics.internaldafny.__default.Metrics(software.amazon.cryptography.metrics.internaldafny.__default.DefaultMetricsConfig());
    _0_valueOrError0 = _out0;
    if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.metrics.internaldafny.MetricsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.metrics.internaldafny.MetricsClient.class)), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/Metrics/test/TestMetricsAgentText.dfy(14,19): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    software.amazon.cryptography.metrics.internaldafny.MetricsClient _1_metrics;
    _1_metrics = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.metrics.internaldafny.MetricsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.metrics.internaldafny.MetricsClient.class)), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = UUID.__default.GenerateUUID();
    _2_valueOrError1 = _out1;
    if (!(!((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/Metrics/test/TestMetricsAgentText.dfy(16,20): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    dafny.DafnySequence<? extends Character> _3_fileName;
    _3_fileName = (_2_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _4_metricAgent;
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out2;
    _out2 = (_1_metrics).CreateTextMetricsAgent(software.amazon.cryptography.metrics.internaldafny.types.CreateTextMetricsAgentInput.create(_3_fileName));
    _4_metricAgent = _out2;
  }
  @Override
  public java.lang.String toString() {
    return "TestMetricsAgentText._default";
  }
}
