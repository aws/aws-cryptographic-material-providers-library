// Class ExportTableToPointInTimeInput
// Dafny class ExportTableToPointInTimeInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ExportTableToPointInTimeInput {
  public dafny.DafnySequence<? extends Character> _TableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientToken;
  public dafny.DafnySequence<? extends Character> _S3Bucket;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3BucketOwner;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3Prefix;
  public Wrappers_Compile.Option<S3SseAlgorithm> _S3SseAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3SseKmsKeyId;
  public Wrappers_Compile.Option<ExportFormat> _ExportFormat;
  public Wrappers_Compile.Option<ExportType> _ExportType;
  public Wrappers_Compile.Option<IncrementalExportSpecification> _IncrementalExportSpecification;
  public ExportTableToPointInTimeInput (dafny.DafnySequence<? extends Character> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    this._TableArn = TableArn;
    this._ExportTime = ExportTime;
    this._ClientToken = ClientToken;
    this._S3Bucket = S3Bucket;
    this._S3BucketOwner = S3BucketOwner;
    this._S3Prefix = S3Prefix;
    this._S3SseAlgorithm = S3SseAlgorithm;
    this._S3SseKmsKeyId = S3SseKmsKeyId;
    this._ExportFormat = ExportFormat;
    this._ExportType = ExportType;
    this._IncrementalExportSpecification = IncrementalExportSpecification;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportTableToPointInTimeInput o = (ExportTableToPointInTimeInput)other;
    return true && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._ExportTime, o._ExportTime) && java.util.Objects.equals(this._ClientToken, o._ClientToken) && java.util.Objects.equals(this._S3Bucket, o._S3Bucket) && java.util.Objects.equals(this._S3BucketOwner, o._S3BucketOwner) && java.util.Objects.equals(this._S3Prefix, o._S3Prefix) && java.util.Objects.equals(this._S3SseAlgorithm, o._S3SseAlgorithm) && java.util.Objects.equals(this._S3SseKmsKeyId, o._S3SseKmsKeyId) && java.util.Objects.equals(this._ExportFormat, o._ExportFormat) && java.util.Objects.equals(this._ExportType, o._ExportType) && java.util.Objects.equals(this._IncrementalExportSpecification, o._IncrementalExportSpecification);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3Bucket);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketOwner);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3Prefix);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3SseAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3SseKmsKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportFormat);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IncrementalExportSpecification);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExportTableToPointInTimeInput.ExportTableToPointInTimeInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ClientToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3Bucket));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3BucketOwner));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3Prefix));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3SseAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3SseKmsKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportFormat));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IncrementalExportSpecification));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExportTableToPointInTimeInput> _TYPE = dafny.TypeDescriptor.<ExportTableToPointInTimeInput>referenceWithInitializer(ExportTableToPointInTimeInput.class, () -> ExportTableToPointInTimeInput.Default());
  public static dafny.TypeDescriptor<ExportTableToPointInTimeInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportTableToPointInTimeInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportTableToPointInTimeInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportTableToPointInTimeInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3Prefix._typeDescriptor()), Wrappers_Compile.Option.<S3SseAlgorithm>Default(S3SseAlgorithm._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3SseKmsKeyId._typeDescriptor()), Wrappers_Compile.Option.<ExportFormat>Default(ExportFormat._typeDescriptor()), Wrappers_Compile.Option.<ExportType>Default(ExportType._typeDescriptor()), Wrappers_Compile.Option.<IncrementalExportSpecification>Default(IncrementalExportSpecification._typeDescriptor()));
  public static ExportTableToPointInTimeInput Default() {
    return theDefault;
  }
  public static ExportTableToPointInTimeInput create(dafny.DafnySequence<? extends Character> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    return new ExportTableToPointInTimeInput(TableArn, ExportTime, ClientToken, S3Bucket, S3BucketOwner, S3Prefix, S3SseAlgorithm, S3SseKmsKeyId, ExportFormat, ExportType, IncrementalExportSpecification);
  }
  public static ExportTableToPointInTimeInput create_ExportTableToPointInTimeInput(dafny.DafnySequence<? extends Character> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    return create(TableArn, ExportTime, ClientToken, S3Bucket, S3BucketOwner, S3Prefix, S3SseAlgorithm, S3SseKmsKeyId, ExportFormat, ExportType, IncrementalExportSpecification);
  }
  public boolean is_ExportTableToPointInTimeInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportTime() {
    return this._ExportTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientToken() {
    return this._ClientToken;
  }
  public dafny.DafnySequence<? extends Character> dtor_S3Bucket() {
    return this._S3Bucket;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3BucketOwner() {
    return this._S3BucketOwner;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3Prefix() {
    return this._S3Prefix;
  }
  public Wrappers_Compile.Option<S3SseAlgorithm> dtor_S3SseAlgorithm() {
    return this._S3SseAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3SseKmsKeyId() {
    return this._S3SseKmsKeyId;
  }
  public Wrappers_Compile.Option<ExportFormat> dtor_ExportFormat() {
    return this._ExportFormat;
  }
  public Wrappers_Compile.Option<ExportType> dtor_ExportType() {
    return this._ExportType;
  }
  public Wrappers_Compile.Option<IncrementalExportSpecification> dtor_IncrementalExportSpecification() {
    return this._IncrementalExportSpecification;
  }
}
