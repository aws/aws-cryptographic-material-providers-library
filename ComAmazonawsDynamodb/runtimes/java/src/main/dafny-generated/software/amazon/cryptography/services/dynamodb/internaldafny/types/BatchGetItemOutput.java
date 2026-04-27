// Class BatchGetItemOutput
// Dafny class BatchGetItemOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchGetItemOutput {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>> _Responses;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> _UnprocessedKeys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public BatchGetItemOutput (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>> Responses, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> UnprocessedKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    this._Responses = Responses;
    this._UnprocessedKeys = UnprocessedKeys;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchGetItemOutput o = (BatchGetItemOutput)other;
    return true && java.util.Objects.equals(this._Responses, o._Responses) && java.util.Objects.equals(this._UnprocessedKeys, o._UnprocessedKeys) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Responses);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UnprocessedKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchGetItemOutput.BatchGetItemOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Responses));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UnprocessedKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchGetItemOutput> _TYPE = dafny.TypeDescriptor.<BatchGetItemOutput>referenceWithInitializer(BatchGetItemOutput.class, () -> BatchGetItemOutput.Default());
  public static dafny.TypeDescriptor<BatchGetItemOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchGetItemOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchGetItemOutput theDefault = BatchGetItemOutput.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>_typeDescriptor(TableArn._typeDescriptor(), dafny.DafnySequence.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>>Default(BatchGetRequestMap._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())));
  public static BatchGetItemOutput Default() {
    return theDefault;
  }
  public static BatchGetItemOutput create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>> Responses, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> UnprocessedKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return new BatchGetItemOutput(Responses, UnprocessedKeys, ConsumedCapacity);
  }
  public static BatchGetItemOutput create_BatchGetItemOutput(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>> Responses, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> UnprocessedKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return create(Responses, UnprocessedKeys, ConsumedCapacity);
  }
  public boolean is_BatchGetItemOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>> dtor_Responses() {
    return this._Responses;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes>> dtor_UnprocessedKeys() {
    return this._UnprocessedKeys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
