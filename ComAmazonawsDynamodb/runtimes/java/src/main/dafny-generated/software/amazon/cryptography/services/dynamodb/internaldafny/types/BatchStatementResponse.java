// Class BatchStatementResponse
// Dafny class BatchStatementResponse compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementResponse {
  public Wrappers_Compile.Option<BatchStatementError> _Error;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public BatchStatementResponse (Wrappers_Compile.Option<BatchStatementError> Error, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    this._Error = Error;
    this._TableName = TableName;
    this._Item = Item;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementResponse o = (BatchStatementResponse)other;
    return true && java.util.Objects.equals(this._Error, o._Error) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._Item, o._Item);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Error);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementResponse.BatchStatementResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Error));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchStatementResponse> _TYPE = dafny.TypeDescriptor.<BatchStatementResponse>referenceWithInitializer(BatchStatementResponse.class, () -> BatchStatementResponse.Default());
  public static dafny.TypeDescriptor<BatchStatementResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchStatementResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchStatementResponse theDefault = BatchStatementResponse.create(Wrappers_Compile.Option.<BatchStatementError>Default(BatchStatementError._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())));
  public static BatchStatementResponse Default() {
    return theDefault;
  }
  public static BatchStatementResponse create(Wrappers_Compile.Option<BatchStatementError> Error, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return new BatchStatementResponse(Error, TableName, Item);
  }
  public static BatchStatementResponse create_BatchStatementResponse(Wrappers_Compile.Option<BatchStatementError> Error, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return create(Error, TableName, Item);
  }
  public boolean is_BatchStatementResponse() { return true; }
  public Wrappers_Compile.Option<BatchStatementError> dtor_Error() {
    return this._Error;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    return this._Item;
  }
}
