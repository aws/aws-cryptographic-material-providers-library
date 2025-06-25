// Class CreateLoggerOutput
// Dafny class CreateLoggerOutput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateLoggerOutput {
  public ILogger _logger;
  public CreateLoggerOutput (ILogger logger) {
    this._logger = logger;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateLoggerOutput o = (CreateLoggerOutput)other;
    return true && this._logger == o._logger;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._logger);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMetricsTypes.CreateLoggerOutput.CreateLoggerOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._logger));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateLoggerOutput> _TYPE = dafny.TypeDescriptor.<CreateLoggerOutput>referenceWithInitializer(CreateLoggerOutput.class, () -> CreateLoggerOutput.Default());
  public static dafny.TypeDescriptor<CreateLoggerOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateLoggerOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateLoggerOutput theDefault = software.amazon.cryptography.metrics.internaldafny.types.CreateLoggerOutput.create(null);
  public static CreateLoggerOutput Default() {
    return theDefault;
  }
  public static CreateLoggerOutput create(ILogger logger) {
    return new CreateLoggerOutput(logger);
  }
  public static CreateLoggerOutput create_CreateLoggerOutput(ILogger logger) {
    return create(logger);
  }
  public boolean is_CreateLoggerOutput() { return true; }
  public ILogger dtor_logger() {
    return this._logger;
  }
}
