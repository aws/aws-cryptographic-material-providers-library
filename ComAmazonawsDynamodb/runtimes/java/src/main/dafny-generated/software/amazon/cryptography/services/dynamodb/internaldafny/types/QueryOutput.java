// Class QueryOutput
// Dafny class QueryOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class QueryOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> _Items;
  public Wrappers_Compile.Option<java.lang.Integer> _Count;
  public Wrappers_Compile.Option<java.lang.Integer> _ScannedCount;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _LastEvaluatedKey;
  public Wrappers_Compile.Option<ConsumedCapacity> _ConsumedCapacity;
  public QueryOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<java.lang.Integer> Count, Wrappers_Compile.Option<java.lang.Integer> ScannedCount, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    this._Items = Items;
    this._Count = Count;
    this._ScannedCount = ScannedCount;
    this._LastEvaluatedKey = LastEvaluatedKey;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    QueryOutput o = (QueryOutput)other;
    return true && java.util.Objects.equals(this._Items, o._Items) && java.util.Objects.equals(this._Count, o._Count) && java.util.Objects.equals(this._ScannedCount, o._ScannedCount) && java.util.Objects.equals(this._LastEvaluatedKey, o._LastEvaluatedKey) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Items);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Count);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScannedCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastEvaluatedKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.QueryOutput.QueryOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Items));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Count));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScannedCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastEvaluatedKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<QueryOutput> _TYPE = dafny.TypeDescriptor.<QueryOutput>referenceWithInitializer(QueryOutput.class, () -> QueryOutput.Default());
  public static dafny.TypeDescriptor<QueryOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<QueryOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final QueryOutput theDefault = QueryOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>Default(dafny.DafnySequence.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor()))), Wrappers_Compile.Option.<java.lang.Integer>Default(BoundedInts_Compile.int32._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(BoundedInts_Compile.int32._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ConsumedCapacity>Default(ConsumedCapacity._typeDescriptor()));
  public static QueryOutput Default() {
    return theDefault;
  }
  public static QueryOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<java.lang.Integer> Count, Wrappers_Compile.Option<java.lang.Integer> ScannedCount, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    return new QueryOutput(Items, Count, ScannedCount, LastEvaluatedKey, ConsumedCapacity);
  }
  public static QueryOutput create_QueryOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<java.lang.Integer> Count, Wrappers_Compile.Option<java.lang.Integer> ScannedCount, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    return create(Items, Count, ScannedCount, LastEvaluatedKey, ConsumedCapacity);
  }
  public boolean is_QueryOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> dtor_Items() {
    return this._Items;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Count() {
    return this._Count;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_ScannedCount() {
    return this._ScannedCount;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_LastEvaluatedKey() {
    return this._LastEvaluatedKey;
  }
  public Wrappers_Compile.Option<ConsumedCapacity> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
