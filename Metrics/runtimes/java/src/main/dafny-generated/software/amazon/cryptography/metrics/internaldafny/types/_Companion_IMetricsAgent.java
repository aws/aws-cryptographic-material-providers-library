// Interface IMetricsAgent
// Dafny trait IMetricsAgent compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_IMetricsAgent {
  public _Companion_IMetricsAgent() {
  }
  private static final dafny.TypeDescriptor<IMetricsAgent> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(IMetricsAgent.class, () -> null);
  public static dafny.TypeDescriptor<IMetricsAgent> _typeDescriptor() {
    return (dafny.TypeDescriptor<IMetricsAgent>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<PutOutput, Error> PutCount(IMetricsAgent _this, PutCountInput input)
  {
    Wrappers_Compile.Result<PutOutput, Error> output = Wrappers_Compile.Result.<PutOutput, Error>Default(PutOutput._typeDescriptor(), Error._typeDescriptor(), PutOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PutOutput, Error> _out0;
      _out0 = (_this).PutCount_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<PutOutput, Error> PutDate(IMetricsAgent _this, PutDateInput input)
  {
    Wrappers_Compile.Result<PutOutput, Error> output = Wrappers_Compile.Result.<PutOutput, Error>Default(PutOutput._typeDescriptor(), Error._typeDescriptor(), PutOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PutOutput, Error> _out0;
      _out0 = (_this).PutDate_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<PutOutput, Error> PutTime(IMetricsAgent _this, PutTimeInput input)
  {
    Wrappers_Compile.Result<PutOutput, Error> output = Wrappers_Compile.Result.<PutOutput, Error>Default(PutOutput._typeDescriptor(), Error._typeDescriptor(), PutOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PutOutput, Error> _out0;
      _out0 = (_this).PutTime_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<PutOutput, Error> PutProperty(IMetricsAgent _this, PutPropertyInput input)
  {
    Wrappers_Compile.Result<PutOutput, Error> output = Wrappers_Compile.Result.<PutOutput, Error>Default(PutOutput._typeDescriptor(), Error._typeDescriptor(), PutOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PutOutput, Error> _out0;
      _out0 = (_this).PutProperty_k(input);
      output = _out0;
    }
    return output;
  }
}
