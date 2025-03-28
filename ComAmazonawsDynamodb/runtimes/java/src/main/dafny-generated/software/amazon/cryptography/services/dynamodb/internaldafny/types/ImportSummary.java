// Class ImportSummary
// Dafny class ImportSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ImportArn;
  public Wrappers_Compile.Option<ImportStatus> _ImportStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<S3BucketSource> _S3BucketSource;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudWatchLogGroupArn;
  public Wrappers_Compile.Option<InputFormat> _InputFormat;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StartTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _EndTime;
  public ImportSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime) {
    this._ImportArn = ImportArn;
    this._ImportStatus = ImportStatus;
    this._TableArn = TableArn;
    this._S3BucketSource = S3BucketSource;
    this._CloudWatchLogGroupArn = CloudWatchLogGroupArn;
    this._InputFormat = InputFormat;
    this._StartTime = StartTime;
    this._EndTime = EndTime;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportSummary o = (ImportSummary)other;
    return true && java.util.Objects.equals(this._ImportArn, o._ImportArn) && java.util.Objects.equals(this._ImportStatus, o._ImportStatus) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._S3BucketSource, o._S3BucketSource) && java.util.Objects.equals(this._CloudWatchLogGroupArn, o._CloudWatchLogGroupArn) && java.util.Objects.equals(this._InputFormat, o._InputFormat) && java.util.Objects.equals(this._StartTime, o._StartTime) && java.util.Objects.equals(this._EndTime, o._EndTime);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketSource);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudWatchLogGroupArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._InputFormat);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StartTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EndTime);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ImportSummary.ImportSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ImportStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3BucketSource));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudWatchLogGroupArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._InputFormat));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StartTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EndTime));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportSummary> _TYPE = dafny.TypeDescriptor.<ImportSummary>referenceWithInitializer(ImportSummary.class, () -> ImportSummary.Default());
  public static dafny.TypeDescriptor<ImportSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportSummary theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ImportArn._typeDescriptor()), Wrappers_Compile.Option.<ImportStatus>Default(ImportStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<S3BucketSource>Default(S3BucketSource._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudWatchLogGroupArn._typeDescriptor()), Wrappers_Compile.Option.<InputFormat>Default(InputFormat._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ImportSummary Default() {
    return theDefault;
  }
  public static ImportSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime) {
    return new ImportSummary(ImportArn, ImportStatus, TableArn, S3BucketSource, CloudWatchLogGroupArn, InputFormat, StartTime, EndTime);
  }
  public static ImportSummary create_ImportSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ImportArn, Wrappers_Compile.Option<ImportStatus> ImportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<S3BucketSource> S3BucketSource, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudWatchLogGroupArn, Wrappers_Compile.Option<InputFormat> InputFormat, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime) {
    return create(ImportArn, ImportStatus, TableArn, S3BucketSource, CloudWatchLogGroupArn, InputFormat, StartTime, EndTime);
  }
  public boolean is_ImportSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ImportArn() {
    return this._ImportArn;
  }
  public Wrappers_Compile.Option<ImportStatus> dtor_ImportStatus() {
    return this._ImportStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<S3BucketSource> dtor_S3BucketSource() {
    return this._S3BucketSource;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudWatchLogGroupArn() {
    return this._CloudWatchLogGroupArn;
  }
  public Wrappers_Compile.Option<InputFormat> dtor_InputFormat() {
    return this._InputFormat;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StartTime() {
    return this._StartTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_EndTime() {
    return this._EndTime;
  }
}
