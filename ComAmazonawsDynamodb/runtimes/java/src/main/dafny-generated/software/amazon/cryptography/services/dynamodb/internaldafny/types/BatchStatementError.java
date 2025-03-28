// Class BatchStatementError
// Dafny class BatchStatementError compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchStatementError {
  public Wrappers_Compile.Option<BatchStatementErrorCodeEnum> _Code;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Message;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public BatchStatementError (Wrappers_Compile.Option<BatchStatementErrorCodeEnum> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    this._Code = Code;
    this._Message = Message;
    this._Item = Item;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchStatementError o = (BatchStatementError)other;
    return true && java.util.Objects.equals(this._Code, o._Code) && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._Item, o._Item);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Code);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchStatementError.BatchStatementError");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Code));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchStatementError> _TYPE = dafny.TypeDescriptor.<BatchStatementError>referenceWithInitializer(BatchStatementError.class, () -> BatchStatementError.Default());
  public static dafny.TypeDescriptor<BatchStatementError> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchStatementError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchStatementError theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementError.create(Wrappers_Compile.Option.<BatchStatementErrorCodeEnum>Default(BatchStatementErrorCodeEnum._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())));
  public static BatchStatementError Default() {
    return theDefault;
  }
  public static BatchStatementError create(Wrappers_Compile.Option<BatchStatementErrorCodeEnum> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return new BatchStatementError(Code, Message, Item);
  }
  public static BatchStatementError create_BatchStatementError(Wrappers_Compile.Option<BatchStatementErrorCodeEnum> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return create(Code, Message, Item);
  }
  public boolean is_BatchStatementError() { return true; }
  public Wrappers_Compile.Option<BatchStatementErrorCodeEnum> dtor_Code() {
    return this._Code;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Message() {
    return this._Message;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    return this._Item;
  }
}
