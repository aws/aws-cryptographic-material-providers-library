// Class BatchStatementRequest
// Dafny class BatchStatementRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementRequest {
  public dafny.DafnySequence<? extends Character> _Statement;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> _Parameters;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> _ReturnValuesOnConditionCheckFailure;
  public BatchStatementRequest (dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    this._Statement = Statement;
    this._Parameters = Parameters;
    this._ConsistentRead = ConsistentRead;
    this._ReturnValuesOnConditionCheckFailure = ReturnValuesOnConditionCheckFailure;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementRequest o = (BatchStatementRequest)other;
    return true && java.util.Objects.equals(this._Statement, o._Statement) && java.util.Objects.equals(this._Parameters, o._Parameters) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead) && java.util.Objects.equals(this._ReturnValuesOnConditionCheckFailure, o._ReturnValuesOnConditionCheckFailure);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Statement);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Parameters);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValuesOnConditionCheckFailure);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementRequest.BatchStatementRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Statement));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Parameters));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnValuesOnConditionCheckFailure));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchStatementRequest> _TYPE = dafny.TypeDescriptor.<BatchStatementRequest>referenceWithInitializer(BatchStatementRequest.class, () -> BatchStatementRequest.Default());
  public static dafny.TypeDescriptor<BatchStatementRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchStatementRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchStatementRequest theDefault = BatchStatementRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeValue>>Default(PreparedStatementParameters._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<ReturnValuesOnConditionCheckFailure>Default(ReturnValuesOnConditionCheckFailure._typeDescriptor()));
  public static BatchStatementRequest Default() {
    return theDefault;
  }
  public static BatchStatementRequest create(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return new BatchStatementRequest(Statement, Parameters, ConsistentRead, ReturnValuesOnConditionCheckFailure);
  }
  public static BatchStatementRequest create_BatchStatementRequest(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return create(Statement, Parameters, ConsistentRead, ReturnValuesOnConditionCheckFailure);
  }
  public boolean is_BatchStatementRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_Statement() {
    return this._Statement;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> dtor_Parameters() {
    return this._Parameters;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> dtor_ReturnValuesOnConditionCheckFailure() {
    return this._ReturnValuesOnConditionCheckFailure;
  }
}
