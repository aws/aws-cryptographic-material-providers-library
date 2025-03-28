// Class GetItemOutput
// Dafny class GetItemOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetItemOutput {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public Wrappers_Compile.Option<ConsumedCapacity> _ConsumedCapacity;
  public GetItemOutput (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    this._Item = Item;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetItemOutput o = (GetItemOutput)other;
    return true && java.util.Objects.equals(this._Item, o._Item) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GetItemOutput.GetItemOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetItemOutput> _TYPE = dafny.TypeDescriptor.<GetItemOutput>referenceWithInitializer(GetItemOutput.class, () -> GetItemOutput.Default());
  public static dafny.TypeDescriptor<GetItemOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetItemOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetItemOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GetItemOutput.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ConsumedCapacity>Default(ConsumedCapacity._typeDescriptor()));
  public static GetItemOutput Default() {
    return theDefault;
  }
  public static GetItemOutput create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    return new GetItemOutput(Item, ConsumedCapacity);
  }
  public static GetItemOutput create_GetItemOutput(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity) {
    return create(Item, ConsumedCapacity);
  }
  public boolean is_GetItemOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    return this._Item;
  }
  public Wrappers_Compile.Option<ConsumedCapacity> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
