// Interface ILogger
// Dafny trait ILogger compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_ILogger {
  public _Companion_ILogger() {
  }
  private static final dafny.TypeDescriptor<ILogger> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(ILogger.class, () -> null);
  public static dafny.TypeDescriptor<ILogger> _typeDescriptor() {
    return (dafny.TypeDescriptor<ILogger>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<PutOutput, Error> Put(ILogger _this, PutInput input)
  {
    Wrappers_Compile.Result<PutOutput, Error> output = Wrappers_Compile.Result.<PutOutput, Error>Default(PutOutput._typeDescriptor(), Error._typeDescriptor(), PutOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PutOutput, Error> _out0;
      _out0 = (_this).Put_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<PublishOutput, Error> Publish(ILogger _this, PublishInput input)
  {
    Wrappers_Compile.Result<PublishOutput, Error> output = Wrappers_Compile.Result.<PublishOutput, Error>Default(PublishOutput._typeDescriptor(), Error._typeDescriptor(), PublishOutput.Default());
    if(true) {
      Wrappers_Compile.Result<PublishOutput, Error> _out0;
      _out0 = (_this).Publish_k(input);
      output = _out0;
    }
    return output;
  }
}
