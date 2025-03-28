// Class ImportTableInput
// Dafny class ImportTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportTableInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientToken;
  public S3BucketSource _S3BucketSource;
  public InputFormat _InputFormat;
  public Wrappers_Compile.Option<InputFormatOptions> _InputFormatOptions;
  public Wrappers_Compile.Option<InputCompressionType> _InputCompressionType;
  public TableCreationParameters _TableCreationParameters;
  public ImportTableInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, S3BucketSource S3BucketSource, InputFormat InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, TableCreationParameters TableCreationParameters) {
    this._ClientToken = ClientToken;
    this._S3BucketSource = S3BucketSource;
    this._InputFormat = InputFormat;
    this._InputFormatOptions = InputFormatOptions;
    this._InputCompressionType = InputCompressionType;
    this._TableCreationParameters = TableCreationParameters;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportTableInput o = (ImportTableInput)other;
    return true && java.util.Objects.equals(this._ClientToken, o._ClientToken) && java.util.Objects.equals(this._S3BucketSource, o._S3BucketSource) && java.util.Objects.equals(this._InputFormat, o._InputFormat) && java.util.Objects.equals(this._InputFormatOptions, o._InputFormatOptions) && java.util.Objects.equals(this._InputCompressionType, o._InputCompressionType) && java.util.Objects.equals(this._TableCreationParameters, o._TableCreationParameters);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketSource);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputFormat);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputFormatOptions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputCompressionType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableCreationParameters);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportTableInput.ImportTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ClientToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3BucketSource));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputFormat));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputFormatOptions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputCompressionType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableCreationParameters));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportTableInput> _TYPE = dafny.TypeDescriptor.<ImportTableInput>referenceWithInitializer(ImportTableInput.class, () -> ImportTableInput.Default());
  public static dafny.TypeDescriptor<ImportTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportTableInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), S3BucketSource.Default(), InputFormat.Default(), Wrappers_Compile.Option.<InputFormatOptions>Default(InputFormatOptions._typeDescriptor()), Wrappers_Compile.Option.<InputCompressionType>Default(InputCompressionType._typeDescriptor()), TableCreationParameters.Default());
  public static ImportTableInput Default() {
    return theDefault;
  }
  public static ImportTableInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, S3BucketSource S3BucketSource, InputFormat InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, TableCreationParameters TableCreationParameters) {
    return new ImportTableInput(ClientToken, S3BucketSource, InputFormat, InputFormatOptions, InputCompressionType, TableCreationParameters);
  }
  public static ImportTableInput create_ImportTableInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, S3BucketSource S3BucketSource, InputFormat InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, TableCreationParameters TableCreationParameters) {
    return create(ClientToken, S3BucketSource, InputFormat, InputFormatOptions, InputCompressionType, TableCreationParameters);
  }
  public boolean is_ImportTableInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientToken() {
    return this._ClientToken;
  }
  public S3BucketSource dtor_S3BucketSource() {
    return this._S3BucketSource;
  }
  public InputFormat dtor_InputFormat() {
    return this._InputFormat;
  }
  public Wrappers_Compile.Option<InputFormatOptions> dtor_InputFormatOptions() {
    return this._InputFormatOptions;
  }
  public Wrappers_Compile.Option<InputCompressionType> dtor_InputCompressionType() {
    return this._InputCompressionType;
  }
  public TableCreationParameters dtor_TableCreationParameters() {
    return this._TableCreationParameters;
  }
}
