// Class ExportDescription
// Dafny class ExportDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExportDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportArn;
  public Wrappers_Compile.Option<ExportStatus> _ExportStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StartTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _EndTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportManifest;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientToken;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3Bucket;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3BucketOwner;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3Prefix;
  public Wrappers_Compile.Option<S3SseAlgorithm> _S3SseAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3SseKmsKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FailureCode;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FailureMessage;
  public Wrappers_Compile.Option<ExportFormat> _ExportFormat;
  public Wrappers_Compile.Option<java.lang.Long> _BilledSizeBytes;
  public Wrappers_Compile.Option<java.lang.Long> _ItemCount;
  public Wrappers_Compile.Option<ExportType> _ExportType;
  public Wrappers_Compile.Option<IncrementalExportSpecification> _IncrementalExportSpecification;
  public ExportDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportManifest, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<java.lang.Long> BilledSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    this._ExportArn = ExportArn;
    this._ExportStatus = ExportStatus;
    this._StartTime = StartTime;
    this._EndTime = EndTime;
    this._ExportManifest = ExportManifest;
    this._TableArn = TableArn;
    this._TableId = TableId;
    this._ExportTime = ExportTime;
    this._ClientToken = ClientToken;
    this._S3Bucket = S3Bucket;
    this._S3BucketOwner = S3BucketOwner;
    this._S3Prefix = S3Prefix;
    this._S3SseAlgorithm = S3SseAlgorithm;
    this._S3SseKmsKeyId = S3SseKmsKeyId;
    this._FailureCode = FailureCode;
    this._FailureMessage = FailureMessage;
    this._ExportFormat = ExportFormat;
    this._BilledSizeBytes = BilledSizeBytes;
    this._ItemCount = ItemCount;
    this._ExportType = ExportType;
    this._IncrementalExportSpecification = IncrementalExportSpecification;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportDescription o = (ExportDescription)other;
    return true && java.util.Objects.equals(this._ExportArn, o._ExportArn) && java.util.Objects.equals(this._ExportStatus, o._ExportStatus) && java.util.Objects.equals(this._StartTime, o._StartTime) && java.util.Objects.equals(this._EndTime, o._EndTime) && java.util.Objects.equals(this._ExportManifest, o._ExportManifest) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._TableId, o._TableId) && java.util.Objects.equals(this._ExportTime, o._ExportTime) && java.util.Objects.equals(this._ClientToken, o._ClientToken) && java.util.Objects.equals(this._S3Bucket, o._S3Bucket) && java.util.Objects.equals(this._S3BucketOwner, o._S3BucketOwner) && java.util.Objects.equals(this._S3Prefix, o._S3Prefix) && java.util.Objects.equals(this._S3SseAlgorithm, o._S3SseAlgorithm) && java.util.Objects.equals(this._S3SseKmsKeyId, o._S3SseKmsKeyId) && java.util.Objects.equals(this._FailureCode, o._FailureCode) && java.util.Objects.equals(this._FailureMessage, o._FailureMessage) && java.util.Objects.equals(this._ExportFormat, o._ExportFormat) && java.util.Objects.equals(this._BilledSizeBytes, o._BilledSizeBytes) && java.util.Objects.equals(this._ItemCount, o._ItemCount) && java.util.Objects.equals(this._ExportType, o._ExportType) && java.util.Objects.equals(this._IncrementalExportSpecification, o._IncrementalExportSpecification);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StartTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EndTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportManifest);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3Bucket);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketOwner);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3Prefix);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3SseAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3SseKmsKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FailureCode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FailureMessage);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportFormat);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BilledSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IncrementalExportSpecification);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExportDescription.ExportDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StartTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EndTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportManifest));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableId));
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
    s.append(dafny.Helpers.toString(this._FailureCode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FailureMessage));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportFormat));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BilledSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IncrementalExportSpecification));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExportDescription> _TYPE = dafny.TypeDescriptor.<ExportDescription>referenceWithInitializer(ExportDescription.class, () -> ExportDescription.Default());
  public static dafny.TypeDescriptor<ExportDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportDescription theDefault = ExportDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ExportArn._typeDescriptor()), Wrappers_Compile.Option.<ExportStatus>Default(ExportStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3Bucket._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3Prefix._typeDescriptor()), Wrappers_Compile.Option.<S3SseAlgorithm>Default(S3SseAlgorithm._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3SseKmsKeyId._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ExportFormat>Default(ExportFormat._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BilledSizeBytes._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(ItemCount._typeDescriptor()), Wrappers_Compile.Option.<ExportType>Default(ExportType._typeDescriptor()), Wrappers_Compile.Option.<IncrementalExportSpecification>Default(IncrementalExportSpecification._typeDescriptor()));
  public static ExportDescription Default() {
    return theDefault;
  }
  public static ExportDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportManifest, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<java.lang.Long> BilledSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    return new ExportDescription(ExportArn, ExportStatus, StartTime, EndTime, ExportManifest, TableArn, TableId, ExportTime, ClientToken, S3Bucket, S3BucketOwner, S3Prefix, S3SseAlgorithm, S3SseKmsKeyId, FailureCode, FailureMessage, ExportFormat, BilledSizeBytes, ItemCount, ExportType, IncrementalExportSpecification);
  }
  public static ExportDescription create_ExportDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StartTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> EndTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportManifest, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3Prefix, Wrappers_Compile.Option<S3SseAlgorithm> S3SseAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3SseKmsKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureCode, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FailureMessage, Wrappers_Compile.Option<ExportFormat> ExportFormat, Wrappers_Compile.Option<java.lang.Long> BilledSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<ExportType> ExportType, Wrappers_Compile.Option<IncrementalExportSpecification> IncrementalExportSpecification) {
    return create(ExportArn, ExportStatus, StartTime, EndTime, ExportManifest, TableArn, TableId, ExportTime, ClientToken, S3Bucket, S3BucketOwner, S3Prefix, S3SseAlgorithm, S3SseKmsKeyId, FailureCode, FailureMessage, ExportFormat, BilledSizeBytes, ItemCount, ExportType, IncrementalExportSpecification);
  }
  public boolean is_ExportDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportArn() {
    return this._ExportArn;
  }
  public Wrappers_Compile.Option<ExportStatus> dtor_ExportStatus() {
    return this._ExportStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StartTime() {
    return this._StartTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_EndTime() {
    return this._EndTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportManifest() {
    return this._ExportManifest;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableId() {
    return this._TableId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportTime() {
    return this._ExportTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientToken() {
    return this._ClientToken;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3Bucket() {
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
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FailureCode() {
    return this._FailureCode;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FailureMessage() {
    return this._FailureMessage;
  }
  public Wrappers_Compile.Option<ExportFormat> dtor_ExportFormat() {
    return this._ExportFormat;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_BilledSizeBytes() {
    return this._BilledSizeBytes;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ItemCount() {
    return this._ItemCount;
  }
  public Wrappers_Compile.Option<ExportType> dtor_ExportType() {
    return this._ExportType;
  }
  public Wrappers_Compile.Option<IncrementalExportSpecification> dtor_IncrementalExportSpecification() {
    return this._IncrementalExportSpecification;
  }
}
