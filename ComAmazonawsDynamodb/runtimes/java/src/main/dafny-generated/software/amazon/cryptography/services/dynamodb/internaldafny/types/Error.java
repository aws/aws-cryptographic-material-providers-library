// Class Error
// Dafny class Error compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Error {
  public Error() {
  }
  private static final dafny.TypeDescriptor<Error> _TYPE = dafny.TypeDescriptor.<Error>referenceWithInitializer(Error.class, () -> Error.Default());
  public static dafny.TypeDescriptor<Error> _typeDescriptor() {
    return (dafny.TypeDescriptor<Error>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Error theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.Error.create_BackupInUseException(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static Error Default() {
    return theDefault;
  }
  public static Error create_BackupInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_BackupInUseException(message);
  }
  public static Error create_BackupNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_BackupNotFoundException(message);
  }
  public static Error create_ConditionalCheckFailedException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return new Error_ConditionalCheckFailedException(message, Item);
  }
  public static Error create_ContinuousBackupsUnavailableException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ContinuousBackupsUnavailableException(message);
  }
  public static Error create_DuplicateItemException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_DuplicateItemException(message);
  }
  public static Error create_ExportConflictException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ExportConflictException(message);
  }
  public static Error create_ExportNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ExportNotFoundException(message);
  }
  public static Error create_GlobalTableAlreadyExistsException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_GlobalTableAlreadyExistsException(message);
  }
  public static Error create_GlobalTableNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_GlobalTableNotFoundException(message);
  }
  public static Error create_IdempotentParameterMismatchException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    return new Error_IdempotentParameterMismatchException(Message);
  }
  public static Error create_ImportConflictException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ImportConflictException(message);
  }
  public static Error create_ImportNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ImportNotFoundException(message);
  }
  public static Error create_IndexNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_IndexNotFoundException(message);
  }
  public static Error create_InternalServerError(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InternalServerError(message);
  }
  public static Error create_InvalidEndpointException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    return new Error_InvalidEndpointException(Message);
  }
  public static Error create_InvalidExportTimeException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidExportTimeException(message);
  }
  public static Error create_InvalidRestoreTimeException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidRestoreTimeException(message);
  }
  public static Error create_ItemCollectionSizeLimitExceededException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ItemCollectionSizeLimitExceededException(message);
  }
  public static Error create_LimitExceededException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_LimitExceededException(message);
  }
  public static Error create_PointInTimeRecoveryUnavailableException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_PointInTimeRecoveryUnavailableException(message);
  }
  public static Error create_PolicyNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_PolicyNotFoundException(message);
  }
  public static Error create_ProvisionedThroughputExceededException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ProvisionedThroughputExceededException(message);
  }
  public static Error create_ReplicaAlreadyExistsException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ReplicaAlreadyExistsException(message);
  }
  public static Error create_ReplicaNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ReplicaNotFoundException(message);
  }
  public static Error create_RequestLimitExceeded(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_RequestLimitExceeded(message);
  }
  public static Error create_ResourceInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ResourceInUseException(message);
  }
  public static Error create_ResourceNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ResourceNotFoundException(message);
  }
  public static Error create_TableAlreadyExistsException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_TableAlreadyExistsException(message);
  }
  public static Error create_TableInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_TableInUseException(message);
  }
  public static Error create_TableNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_TableNotFoundException(message);
  }
  public static Error create_TransactionCanceledException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message, Wrappers_Compile.Option<dafny.DafnySequence<? extends CancellationReason>> CancellationReasons) {
    return new Error_TransactionCanceledException(Message, CancellationReasons);
  }
  public static Error create_TransactionConflictException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_TransactionConflictException(message);
  }
  public static Error create_TransactionInProgressException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    return new Error_TransactionInProgressException(Message);
  }
  public static Error create_Opaque(Object obj) {
    return new Error_Opaque(obj);
  }
  public static Error create_OpaqueWithText(Object obj, dafny.DafnySequence<? extends Character> objMessage) {
    return new Error_OpaqueWithText(obj, objMessage);
  }
  public boolean is_BackupInUseException() { return this instanceof Error_BackupInUseException; }
  public boolean is_BackupNotFoundException() { return this instanceof Error_BackupNotFoundException; }
  public boolean is_ConditionalCheckFailedException() { return this instanceof Error_ConditionalCheckFailedException; }
  public boolean is_ContinuousBackupsUnavailableException() { return this instanceof Error_ContinuousBackupsUnavailableException; }
  public boolean is_DuplicateItemException() { return this instanceof Error_DuplicateItemException; }
  public boolean is_ExportConflictException() { return this instanceof Error_ExportConflictException; }
  public boolean is_ExportNotFoundException() { return this instanceof Error_ExportNotFoundException; }
  public boolean is_GlobalTableAlreadyExistsException() { return this instanceof Error_GlobalTableAlreadyExistsException; }
  public boolean is_GlobalTableNotFoundException() { return this instanceof Error_GlobalTableNotFoundException; }
  public boolean is_IdempotentParameterMismatchException() { return this instanceof Error_IdempotentParameterMismatchException; }
  public boolean is_ImportConflictException() { return this instanceof Error_ImportConflictException; }
  public boolean is_ImportNotFoundException() { return this instanceof Error_ImportNotFoundException; }
  public boolean is_IndexNotFoundException() { return this instanceof Error_IndexNotFoundException; }
  public boolean is_InternalServerError() { return this instanceof Error_InternalServerError; }
  public boolean is_InvalidEndpointException() { return this instanceof Error_InvalidEndpointException; }
  public boolean is_InvalidExportTimeException() { return this instanceof Error_InvalidExportTimeException; }
  public boolean is_InvalidRestoreTimeException() { return this instanceof Error_InvalidRestoreTimeException; }
  public boolean is_ItemCollectionSizeLimitExceededException() { return this instanceof Error_ItemCollectionSizeLimitExceededException; }
  public boolean is_LimitExceededException() { return this instanceof Error_LimitExceededException; }
  public boolean is_PointInTimeRecoveryUnavailableException() { return this instanceof Error_PointInTimeRecoveryUnavailableException; }
  public boolean is_PolicyNotFoundException() { return this instanceof Error_PolicyNotFoundException; }
  public boolean is_ProvisionedThroughputExceededException() { return this instanceof Error_ProvisionedThroughputExceededException; }
  public boolean is_ReplicaAlreadyExistsException() { return this instanceof Error_ReplicaAlreadyExistsException; }
  public boolean is_ReplicaNotFoundException() { return this instanceof Error_ReplicaNotFoundException; }
  public boolean is_RequestLimitExceeded() { return this instanceof Error_RequestLimitExceeded; }
  public boolean is_ResourceInUseException() { return this instanceof Error_ResourceInUseException; }
  public boolean is_ResourceNotFoundException() { return this instanceof Error_ResourceNotFoundException; }
  public boolean is_TableAlreadyExistsException() { return this instanceof Error_TableAlreadyExistsException; }
  public boolean is_TableInUseException() { return this instanceof Error_TableInUseException; }
  public boolean is_TableNotFoundException() { return this instanceof Error_TableNotFoundException; }
  public boolean is_TransactionCanceledException() { return this instanceof Error_TransactionCanceledException; }
  public boolean is_TransactionConflictException() { return this instanceof Error_TransactionConflictException; }
  public boolean is_TransactionInProgressException() { return this instanceof Error_TransactionInProgressException; }
  public boolean is_Opaque() { return this instanceof Error_Opaque; }
  public boolean is_OpaqueWithText() { return this instanceof Error_OpaqueWithText; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_message() {
    Error d = this;
    if (d instanceof Error_BackupInUseException) { return ((Error_BackupInUseException)d)._message; }
    if (d instanceof Error_BackupNotFoundException) { return ((Error_BackupNotFoundException)d)._message; }
    if (d instanceof Error_ConditionalCheckFailedException) { return ((Error_ConditionalCheckFailedException)d)._message; }
    if (d instanceof Error_ContinuousBackupsUnavailableException) { return ((Error_ContinuousBackupsUnavailableException)d)._message; }
    if (d instanceof Error_DuplicateItemException) { return ((Error_DuplicateItemException)d)._message; }
    if (d instanceof Error_ExportConflictException) { return ((Error_ExportConflictException)d)._message; }
    if (d instanceof Error_ExportNotFoundException) { return ((Error_ExportNotFoundException)d)._message; }
    if (d instanceof Error_GlobalTableAlreadyExistsException) { return ((Error_GlobalTableAlreadyExistsException)d)._message; }
    if (d instanceof Error_GlobalTableNotFoundException) { return ((Error_GlobalTableNotFoundException)d)._message; }
    if (d instanceof Error_ImportConflictException) { return ((Error_ImportConflictException)d)._message; }
    if (d instanceof Error_ImportNotFoundException) { return ((Error_ImportNotFoundException)d)._message; }
    if (d instanceof Error_IndexNotFoundException) { return ((Error_IndexNotFoundException)d)._message; }
    if (d instanceof Error_InternalServerError) { return ((Error_InternalServerError)d)._message; }
    if (d instanceof Error_InvalidExportTimeException) { return ((Error_InvalidExportTimeException)d)._message; }
    if (d instanceof Error_InvalidRestoreTimeException) { return ((Error_InvalidRestoreTimeException)d)._message; }
    if (d instanceof Error_ItemCollectionSizeLimitExceededException) { return ((Error_ItemCollectionSizeLimitExceededException)d)._message; }
    if (d instanceof Error_LimitExceededException) { return ((Error_LimitExceededException)d)._message; }
    if (d instanceof Error_PointInTimeRecoveryUnavailableException) { return ((Error_PointInTimeRecoveryUnavailableException)d)._message; }
    if (d instanceof Error_PolicyNotFoundException) { return ((Error_PolicyNotFoundException)d)._message; }
    if (d instanceof Error_ProvisionedThroughputExceededException) { return ((Error_ProvisionedThroughputExceededException)d)._message; }
    if (d instanceof Error_ReplicaAlreadyExistsException) { return ((Error_ReplicaAlreadyExistsException)d)._message; }
    if (d instanceof Error_ReplicaNotFoundException) { return ((Error_ReplicaNotFoundException)d)._message; }
    if (d instanceof Error_RequestLimitExceeded) { return ((Error_RequestLimitExceeded)d)._message; }
    if (d instanceof Error_ResourceInUseException) { return ((Error_ResourceInUseException)d)._message; }
    if (d instanceof Error_ResourceNotFoundException) { return ((Error_ResourceNotFoundException)d)._message; }
    if (d instanceof Error_TableAlreadyExistsException) { return ((Error_TableAlreadyExistsException)d)._message; }
    if (d instanceof Error_TableInUseException) { return ((Error_TableInUseException)d)._message; }
    if (d instanceof Error_TableNotFoundException) { return ((Error_TableNotFoundException)d)._message; }
    return ((Error_TransactionConflictException)d)._message;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    Error d = this;
    return ((Error_ConditionalCheckFailedException)d)._Item;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Message() {
    Error d = this;
    if (d instanceof Error_IdempotentParameterMismatchException) { return ((Error_IdempotentParameterMismatchException)d)._Message; }
    if (d instanceof Error_InvalidEndpointException) { return ((Error_InvalidEndpointException)d)._Message; }
    if (d instanceof Error_TransactionCanceledException) { return ((Error_TransactionCanceledException)d)._Message; }
    return ((Error_TransactionInProgressException)d)._Message;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends CancellationReason>> dtor_CancellationReasons() {
    Error d = this;
    return ((Error_TransactionCanceledException)d)._CancellationReasons;
  }
  public Object dtor_obj() {
    Error d = this;
    if (d instanceof Error_Opaque) { return ((Error_Opaque)d)._obj; }
    return ((Error_OpaqueWithText)d)._obj;
  }
  public dafny.DafnySequence<? extends Character> dtor_objMessage() {
    Error d = this;
    return ((Error_OpaqueWithText)d)._objMessage;
  }
}
