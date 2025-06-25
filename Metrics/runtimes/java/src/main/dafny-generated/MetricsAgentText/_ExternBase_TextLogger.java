// Class _ExternBase_TextLogger
// Dafny class TextLogger compiled into Java
package MetricsAgentText;

import software.amazon.cryptography.metrics.internaldafny.types.*;
import MetricsAgent_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase_TextLogger implements MetricsAgent_Compile.VerifiableInterface, software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent {
  public _ExternBase_TextLogger() {
    this._fileName = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutCount(software.amazon.cryptography.metrics.internaldafny.types.PutCountInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.metrics.internaldafny.types._Companion_IMetricsAgent.PutCount(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutDate(software.amazon.cryptography.metrics.internaldafny.types.PutDateInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.metrics.internaldafny.types._Companion_IMetricsAgent.PutDate(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutProperty(software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.metrics.internaldafny.types._Companion_IMetricsAgent.PutProperty(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutTime(software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.metrics.internaldafny.types._Companion_IMetricsAgent.PutTime(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutCount_k(software.amazon.cryptography.metrics.internaldafny.types.PutCountInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>Default(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.Default());
    boolean _0___v0;
    boolean _out0;
    _out0 = MetricsAgentText.TextLogger.PutCount((input).dtor_description(), (input).dtor_count(), (input).dtor_transactionId());
    _0___v0 = _out0;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.create());
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutDate_k(software.amazon.cryptography.metrics.internaldafny.types.PutDateInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>Default(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.Default());
    boolean _0___v1;
    boolean _out0;
    _out0 = MetricsAgentText.TextLogger.PutDate((input).dtor_description(), (input).dtor_date(), (input).dtor_transactionId());
    _0___v1 = _out0;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.create());
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutTime_k(software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>Default(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.Default());
    boolean _0___v2;
    boolean _out0;
    _out0 = MetricsAgentText.TextLogger.PutTime((input).dtor_description(), (input).dtor_duration(), (input).dtor_transactionId());
    _0___v2 = _out0;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.create());
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> PutProperty_k(software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>Default(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.Default());
    boolean _0___v3;
    boolean _out0;
    _out0 = MetricsAgentText.TextLogger.PutProperty((input).dtor_description(), (input).dtor_value(), (input).dtor_transactionId());
    _0___v3 = _out0;
    output = Wrappers_Compile.Result.<software.amazon.cryptography.metrics.internaldafny.types.PutOutput, software.amazon.cryptography.metrics.internaldafny.types.Error>create_Success(software.amazon.cryptography.metrics.internaldafny.types.PutOutput._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.metrics.internaldafny.types.PutOutput.create());
    return output;
  }
  public dafny.DafnySequence<? extends Character> _fileName;
  public dafny.DafnySequence<? extends Character> fileName()
  {
    return this._fileName;
  }
  private static final dafny.TypeDescriptor<TextLogger> _TYPE = dafny.TypeDescriptor.<TextLogger>referenceWithInitializer(TextLogger.class, () -> (TextLogger) null);
  public static dafny.TypeDescriptor<TextLogger> _typeDescriptor() {
    return (dafny.TypeDescriptor<TextLogger>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "MetricsAgentText.MetricsAgentText";
  }
}
