// Class TransactWriteItem
// Dafny class TransactWriteItem compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactWriteItem {
  public Wrappers_Compile.Option<ConditionCheck> _ConditionCheck;
  public Wrappers_Compile.Option<Put> _Put;
  public Wrappers_Compile.Option<Delete> _Delete;
  public Wrappers_Compile.Option<Update> _Update;
  public TransactWriteItem (Wrappers_Compile.Option<ConditionCheck> ConditionCheck, Wrappers_Compile.Option<Put> Put, Wrappers_Compile.Option<Delete> Delete, Wrappers_Compile.Option<Update> Update) {
    this._ConditionCheck = ConditionCheck;
    this._Put = Put;
    this._Delete = Delete;
    this._Update = Update;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactWriteItem o = (TransactWriteItem)other;
    return true && java.util.Objects.equals(this._ConditionCheck, o._ConditionCheck) && java.util.Objects.equals(this._Put, o._Put) && java.util.Objects.equals(this._Delete, o._Delete) && java.util.Objects.equals(this._Update, o._Update);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionCheck);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Put);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Delete);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Update);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactWriteItem.TransactWriteItem");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ConditionCheck));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Put));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Delete));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Update));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactWriteItem> _TYPE = dafny.TypeDescriptor.<TransactWriteItem>referenceWithInitializer(TransactWriteItem.class, () -> TransactWriteItem.Default());
  public static dafny.TypeDescriptor<TransactWriteItem> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactWriteItem>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactWriteItem theDefault = TransactWriteItem.create(Wrappers_Compile.Option.<ConditionCheck>Default(ConditionCheck._typeDescriptor()), Wrappers_Compile.Option.<Put>Default(Put._typeDescriptor()), Wrappers_Compile.Option.<Delete>Default(Delete._typeDescriptor()), Wrappers_Compile.Option.<Update>Default(Update._typeDescriptor()));
  public static TransactWriteItem Default() {
    return theDefault;
  }
  public static TransactWriteItem create(Wrappers_Compile.Option<ConditionCheck> ConditionCheck, Wrappers_Compile.Option<Put> Put, Wrappers_Compile.Option<Delete> Delete, Wrappers_Compile.Option<Update> Update) {
    return new TransactWriteItem(ConditionCheck, Put, Delete, Update);
  }
  public static TransactWriteItem create_TransactWriteItem(Wrappers_Compile.Option<ConditionCheck> ConditionCheck, Wrappers_Compile.Option<Put> Put, Wrappers_Compile.Option<Delete> Delete, Wrappers_Compile.Option<Update> Update) {
    return create(ConditionCheck, Put, Delete, Update);
  }
  public boolean is_TransactWriteItem() { return true; }
  public Wrappers_Compile.Option<ConditionCheck> dtor_ConditionCheck() {
    return this._ConditionCheck;
  }
  public Wrappers_Compile.Option<Put> dtor_Put() {
    return this._Put;
  }
  public Wrappers_Compile.Option<Delete> dtor_Delete() {
    return this._Delete;
  }
  public Wrappers_Compile.Option<Update> dtor_Update() {
    return this._Update;
  }
}
