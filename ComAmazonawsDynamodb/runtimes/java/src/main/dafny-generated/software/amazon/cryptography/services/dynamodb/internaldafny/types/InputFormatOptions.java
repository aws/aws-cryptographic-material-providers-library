// Class InputFormatOptions
// Dafny class InputFormatOptions compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class InputFormatOptions {
  public Wrappers_Compile.Option<CsvOptions> _Csv;
  public InputFormatOptions (Wrappers_Compile.Option<CsvOptions> Csv) {
    this._Csv = Csv;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InputFormatOptions o = (InputFormatOptions)other;
    return true && java.util.Objects.equals(this._Csv, o._Csv);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Csv);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.InputFormatOptions.InputFormatOptions");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Csv));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<InputFormatOptions> _TYPE = dafny.TypeDescriptor.<InputFormatOptions>referenceWithInitializer(InputFormatOptions.class, () -> InputFormatOptions.Default());
  public static dafny.TypeDescriptor<InputFormatOptions> _typeDescriptor() {
    return (dafny.TypeDescriptor<InputFormatOptions>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final InputFormatOptions theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.InputFormatOptions.create(Wrappers_Compile.Option.<CsvOptions>Default(CsvOptions._typeDescriptor()));
  public static InputFormatOptions Default() {
    return theDefault;
  }
  public static InputFormatOptions create(Wrappers_Compile.Option<CsvOptions> Csv) {
    return new InputFormatOptions(Csv);
  }
  public static InputFormatOptions create_InputFormatOptions(Wrappers_Compile.Option<CsvOptions> Csv) {
    return create(Csv);
  }
  public boolean is_InputFormatOptions() { return true; }
  public Wrappers_Compile.Option<CsvOptions> dtor_Csv() {
    return this._Csv;
  }
}
