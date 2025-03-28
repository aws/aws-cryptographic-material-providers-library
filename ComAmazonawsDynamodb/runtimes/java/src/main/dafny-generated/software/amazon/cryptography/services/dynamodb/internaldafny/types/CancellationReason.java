// Class CancellationReason
// Dafny class CancellationReason compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CancellationReason {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Code;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Message;
  public CancellationReason (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    this._Item = Item;
    this._Code = Code;
    this._Message = Message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CancellationReason o = (CancellationReason)other;
    return true && java.util.Objects.equals(this._Item, o._Item) && java.util.Objects.equals(this._Code, o._Code) && java.util.Objects.equals(this._Message, o._Message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Code);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CancellationReason.CancellationReason");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Code));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CancellationReason> _TYPE = dafny.TypeDescriptor.<CancellationReason>referenceWithInitializer(CancellationReason.class, () -> CancellationReason.Default());
  public static dafny.TypeDescriptor<CancellationReason> _typeDescriptor() {
    return (dafny.TypeDescriptor<CancellationReason>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CancellationReason theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CancellationReason.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static CancellationReason Default() {
    return theDefault;
  }
  public static CancellationReason create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    return new CancellationReason(Item, Code, Message);
  }
  public static CancellationReason create_CancellationReason(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Code, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Message) {
    return create(Item, Code, Message);
  }
  public boolean is_CancellationReason() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    return this._Item;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Code() {
    return this._Code;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Message() {
    return this._Message;
  }
}
