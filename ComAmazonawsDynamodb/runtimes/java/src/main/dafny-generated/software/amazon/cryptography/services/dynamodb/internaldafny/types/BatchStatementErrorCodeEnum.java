// Class BatchStatementErrorCodeEnum
// Dafny class BatchStatementErrorCodeEnum compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class BatchStatementErrorCodeEnum {
  public BatchStatementErrorCodeEnum() {
  }
  private static final dafny.TypeDescriptor<BatchStatementErrorCodeEnum> _TYPE = dafny.TypeDescriptor.<BatchStatementErrorCodeEnum>referenceWithInitializer(BatchStatementErrorCodeEnum.class, () -> BatchStatementErrorCodeEnum.Default());
  public static dafny.TypeDescriptor<BatchStatementErrorCodeEnum> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchStatementErrorCodeEnum>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchStatementErrorCodeEnum theDefault = BatchStatementErrorCodeEnum.create_ConditionalCheckFailed();
  public static BatchStatementErrorCodeEnum Default() {
    return theDefault;
  }
  public static BatchStatementErrorCodeEnum create_ConditionalCheckFailed() {
    return new BatchStatementErrorCodeEnum_ConditionalCheckFailed();
  }
  public static BatchStatementErrorCodeEnum create_ItemCollectionSizeLimitExceeded() {
    return new BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded();
  }
  public static BatchStatementErrorCodeEnum create_RequestLimitExceeded() {
    return new BatchStatementErrorCodeEnum_RequestLimitExceeded();
  }
  public static BatchStatementErrorCodeEnum create_ValidationError() {
    return new BatchStatementErrorCodeEnum_ValidationError();
  }
  public static BatchStatementErrorCodeEnum create_ProvisionedThroughputExceeded() {
    return new BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded();
  }
  public static BatchStatementErrorCodeEnum create_TransactionConflict() {
    return new BatchStatementErrorCodeEnum_TransactionConflict();
  }
  public static BatchStatementErrorCodeEnum create_ThrottlingError() {
    return new BatchStatementErrorCodeEnum_ThrottlingError();
  }
  public static BatchStatementErrorCodeEnum create_InternalServerError() {
    return new BatchStatementErrorCodeEnum_InternalServerError();
  }
  public static BatchStatementErrorCodeEnum create_ResourceNotFound() {
    return new BatchStatementErrorCodeEnum_ResourceNotFound();
  }
  public static BatchStatementErrorCodeEnum create_AccessDenied() {
    return new BatchStatementErrorCodeEnum_AccessDenied();
  }
  public static BatchStatementErrorCodeEnum create_DuplicateItem() {
    return new BatchStatementErrorCodeEnum_DuplicateItem();
  }
  public boolean is_ConditionalCheckFailed() { return this instanceof BatchStatementErrorCodeEnum_ConditionalCheckFailed; }
  public boolean is_ItemCollectionSizeLimitExceeded() { return this instanceof BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded; }
  public boolean is_RequestLimitExceeded() { return this instanceof BatchStatementErrorCodeEnum_RequestLimitExceeded; }
  public boolean is_ValidationError() { return this instanceof BatchStatementErrorCodeEnum_ValidationError; }
  public boolean is_ProvisionedThroughputExceeded() { return this instanceof BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded; }
  public boolean is_TransactionConflict() { return this instanceof BatchStatementErrorCodeEnum_TransactionConflict; }
  public boolean is_ThrottlingError() { return this instanceof BatchStatementErrorCodeEnum_ThrottlingError; }
  public boolean is_InternalServerError() { return this instanceof BatchStatementErrorCodeEnum_InternalServerError; }
  public boolean is_ResourceNotFound() { return this instanceof BatchStatementErrorCodeEnum_ResourceNotFound; }
  public boolean is_AccessDenied() { return this instanceof BatchStatementErrorCodeEnum_AccessDenied; }
  public boolean is_DuplicateItem() { return this instanceof BatchStatementErrorCodeEnum_DuplicateItem; }
  public static java.util.ArrayList<BatchStatementErrorCodeEnum> AllSingletonConstructors() {
    java.util.ArrayList<BatchStatementErrorCodeEnum> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ConditionalCheckFailed());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_RequestLimitExceeded());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ValidationError());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_TransactionConflict());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ThrottlingError());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_InternalServerError());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_ResourceNotFound());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_AccessDenied());
    singleton_iterator.add(new BatchStatementErrorCodeEnum_DuplicateItem());
    return singleton_iterator;
  }
}
