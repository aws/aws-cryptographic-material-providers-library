// Class ImportTableDescription
// Dafny class ImportTableDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ImportTableDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ImportArn;
  public Wrappers_Compile.Option<ImportStatus> _ImportStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientToken;
  public Wrappers_Compile.Option<S3BucketSource> _S3BucketSource;
  public Wrappers_Compile.Option<java.lang.Long> _ErrorCount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudWatchLogGroupArn;
  public Wrappers_Compile.Option<InputFormat> _InputFormat;
  public Wrappers_Compile.Option<InputFormatOptions> _InputFormatOptions;
  public Wrappers_Compile.Option<InputCompressionType> _InputCompressionType;
  public Wrappers_Compile.Option<TableCreationParameters> _TableCreationParameters;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StartTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _EndTime;
  public Wrappers_Compile.Option<java.lang.Long> _ProcessedSizeBytes;
  public Wrappers_Compile.Option<java.lang.Long> _ProcessedItemCount;
  public Wrappers_Compile.Option<java.lang.Long> _ImportedItemCount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FailureCode;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FailureMessage;
  public ImportTableDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<java.lang.Long> ErrorCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, Wrappers_Compile.Option<TableCreationParameters> TableCreationParameters, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<java.lang.Long> ProcessedSizeBytes, Wrappers_Compile.Option<java.lang.Long> ProcessedItemCount, Wrappers_Compile.Option<java.lang.Long> ImportedItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage) {
    this._ImportArn = ImportArn;
    this._ImportStatus = ImportStatus;
    this._TableArn = TableArn;
    this._TableId = TableId;
    this._ClientToken = ClientToken;
    this._S3BucketSource = S3BucketSource;
    this._ErrorCount = ErrorCount;
    this._CloudWatchLogGroupArn = CloudWatchLogGroupArn;
    this._InputFormat = InputFormat;
    this._InputFormatOptions = InputFormatOptions;
    this._InputCompressionType = InputCompressionType;
    this._TableCreationParameters = TableCreationParameters;
    this._StartTime = StartTime;
    this._EndTime = EndTime;
    this._ProcessedSizeBytes = ProcessedSizeBytes;
    this._ProcessedItemCount = ProcessedItemCount;
    this._ImportedItemCount = ImportedItemCount;
    this._FailureCode = FailureCode;
    this._FailureMessage = FailureMessage;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportTableDescription o = (ImportTableDescription)other;
    return true && java.util.Objects.equals(this._ImportArn, o._ImportArn) && java.util.Objects.equals(this._ImportStatus, o._ImportStatus) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._TableId, o._TableId) && java.util.Objects.equals(this._ClientToken, o._ClientToken) && java.util.Objects.equals(this._S3BucketSource, o._S3BucketSource) && java.util.Objects.equals(this._ErrorCount, o._ErrorCount) && java.util.Objects.equals(this._CloudWatchLogGroupArn, o._CloudWatchLogGroupArn) && java.util.Objects.equals(this._InputFormat, o._InputFormat) && java.util.Objects.equals(this._InputFormatOptions, o._InputFormatOptions) && java.util.Objects.equals(this._InputCompressionType, o._InputCompressionType) && java.util.Objects.equals(this._TableCreationParameters, o._TableCreationParameters) && java.util.Objects.equals(this._StartTime, o._StartTime) && java.util.Objects.equals(this._EndTime, o._EndTime) && java.util.Objects.equals(this._ProcessedSizeBytes, o._ProcessedSizeBytes) && java.util.Objects.equals(this._ProcessedItemCount, o._ProcessedItemCount) && java.util.Objects.equals(this._ImportedItemCount, o._ImportedItemCount) && java.util.Objects.equals(this._FailureCode, o._FailureCode) && java.util.Objects.equals(this._FailureMessage, o._FailureMessage);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketSource);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ErrorCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudWatchLogGroupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputFormat);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputFormatOptions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputCompressionType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableCreationParameters);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StartTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EndTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProcessedSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProcessedItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportedItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FailureCode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FailureMessage);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportTableDescription.ImportTableDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ImportStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ClientToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3BucketSource));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ErrorCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudWatchLogGroupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputFormat));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputFormatOptions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputCompressionType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableCreationParameters));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StartTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EndTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProcessedSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProcessedItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ImportedItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FailureCode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FailureMessage));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportTableDescription> _TYPE = dafny.TypeDescriptor.<ImportTableDescription>referenceWithInitializer(ImportTableDescription.class, () -> ImportTableDescription.Default());
  public static dafny.TypeDescriptor<ImportTableDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportTableDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportTableDescription theDefault = ImportTableDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ImportArn._typeDescriptor()), Wrappers_Compile.Option.<ImportStatus>Default(ImportStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<S3BucketSource>Default(S3BucketSource._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(ErrorCount._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudWatchLogGroupArn._typeDescriptor()), Wrappers_Compile.Option.<InputFormat>Default(InputFormat._typeDescriptor()), Wrappers_Compile.Option.<InputFormatOptions>Default(InputFormatOptions._typeDescriptor()), Wrappers_Compile.Option.<InputCompressionType>Default(InputCompressionType._typeDescriptor()), Wrappers_Compile.Option.<TableCreationParameters>Default(TableCreationParameters._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(ProcessedItemCount._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(ImportedItemCount._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ImportTableDescription Default() {
    return theDefault;
  }
  public static ImportTableDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<java.lang.Long> ErrorCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, Wrappers_Compile.Option<TableCreationParameters> TableCreationParameters, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<java.lang.Long> ProcessedSizeBytes, Wrappers_Compile.Option<java.lang.Long> ProcessedItemCount, Wrappers_Compile.Option<java.lang.Long> ImportedItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage) {
    return new ImportTableDescription(ImportArn, ImportStatus, TableArn, TableId, ClientToken, S3BucketSource, ErrorCount, CloudWatchLogGroupArn, InputFormat, InputFormatOptions, InputCompressionType, TableCreationParameters, StartTime, EndTime, ProcessedSizeBytes, ProcessedItemCount, ImportedItemCount, FailureCode, FailureMessage);
  }
  public static ImportTableDescription create_ImportTableDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<java.lang.Long> ErrorCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<InputFormatOptions> InputFormatOptions, Wrappers_Compile.Option<InputCompressionType> InputCompressionType, Wrappers_Compile.Option<TableCreationParameters> TableCreationParameters, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<java.lang.Long> ProcessedSizeBytes, Wrappers_Compile.Option<java.lang.Long> ProcessedItemCount, Wrappers_Compile.Option<java.lang.Long> ImportedItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage) {
    return create(ImportArn, ImportStatus, TableArn, TableId, ClientToken, S3BucketSource, ErrorCount, CloudWatchLogGroupArn, InputFormat, InputFormatOptions, InputCompressionType, TableCreationParameters, StartTime, EndTime, ProcessedSizeBytes, ProcessedItemCount, ImportedItemCount, FailureCode, FailureMessage);
  }
  public boolean is_ImportTableDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ImportArn() {
    return this._ImportArn;
  }
  public Wrappers_Compile.Option<ImportStatus> dtor_ImportStatus() {
    return this._ImportStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableId() {
    return this._TableId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientToken() {
    return this._ClientToken;
  }
  public Wrappers_Compile.Option<S3BucketSource> dtor_S3BucketSource() {
    return this._S3BucketSource;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ErrorCount() {
    return this._ErrorCount;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudWatchLogGroupArn() {
    return this._CloudWatchLogGroupArn;
  }
  public Wrappers_Compile.Option<InputFormat> dtor_InputFormat() {
    return this._InputFormat;
  }
  public Wrappers_Compile.Option<InputFormatOptions> dtor_InputFormatOptions() {
    return this._InputFormatOptions;
  }
  public Wrappers_Compile.Option<InputCompressionType> dtor_InputCompressionType() {
    return this._InputCompressionType;
  }
  public Wrappers_Compile.Option<TableCreationParameters> dtor_TableCreationParameters() {
    return this._TableCreationParameters;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StartTime() {
    return this._StartTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_EndTime() {
    return this._EndTime;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProcessedSizeBytes() {
    return this._ProcessedSizeBytes;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProcessedItemCount() {
    return this._ProcessedItemCount;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ImportedItemCount() {
    return this._ImportedItemCount;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FailureCode() {
    return this._FailureCode;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FailureMessage() {
    return this._FailureMessage;
  }
}
