// Class GlobalSecondaryIndexUpdate
// Dafny class GlobalSecondaryIndexUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndexUpdate {
  public Wrappers_Compile.Option<UpdateGlobalSecondaryIndexAction> _Update;
  public Wrappers_Compile.Option<CreateGlobalSecondaryIndexAction> _Create;
  public Wrappers_Compile.Option<DeleteGlobalSecondaryIndexAction> _Delete;
  public GlobalSecondaryIndexUpdate (Wrappers_Compile.Option<UpdateGlobalSecondaryIndexAction> Update, Wrappers_Compile.Option<CreateGlobalSecondaryIndexAction> Create, Wrappers_Compile.Option<DeleteGlobalSecondaryIndexAction> Delete) {
    this._Update = Update;
    this._Create = Create;
    this._Delete = Delete;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalSecondaryIndexUpdate o = (GlobalSecondaryIndexUpdate)other;
    return true && java.util.Objects.equals(this._Update, o._Update) && java.util.Objects.equals(this._Create, o._Create) && java.util.Objects.equals(this._Delete, o._Delete);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Update);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Create);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Delete);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalSecondaryIndexUpdate.GlobalSecondaryIndexUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Update));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Create));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Delete));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalSecondaryIndexUpdate> _TYPE = dafny.TypeDescriptor.<GlobalSecondaryIndexUpdate>referenceWithInitializer(GlobalSecondaryIndexUpdate.class, () -> GlobalSecondaryIndexUpdate.Default());
  public static dafny.TypeDescriptor<GlobalSecondaryIndexUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalSecondaryIndexUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalSecondaryIndexUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexUpdate.create(Wrappers_Compile.Option.<UpdateGlobalSecondaryIndexAction>Default(UpdateGlobalSecondaryIndexAction._typeDescriptor()), Wrappers_Compile.Option.<CreateGlobalSecondaryIndexAction>Default(CreateGlobalSecondaryIndexAction._typeDescriptor()), Wrappers_Compile.Option.<DeleteGlobalSecondaryIndexAction>Default(DeleteGlobalSecondaryIndexAction._typeDescriptor()));
  public static GlobalSecondaryIndexUpdate Default() {
    return theDefault;
  }
  public static GlobalSecondaryIndexUpdate create(Wrappers_Compile.Option<UpdateGlobalSecondaryIndexAction> Update, Wrappers_Compile.Option<CreateGlobalSecondaryIndexAction> Create, Wrappers_Compile.Option<DeleteGlobalSecondaryIndexAction> Delete) {
    return new GlobalSecondaryIndexUpdate(Update, Create, Delete);
  }
  public static GlobalSecondaryIndexUpdate create_GlobalSecondaryIndexUpdate(Wrappers_Compile.Option<UpdateGlobalSecondaryIndexAction> Update, Wrappers_Compile.Option<CreateGlobalSecondaryIndexAction> Create, Wrappers_Compile.Option<DeleteGlobalSecondaryIndexAction> Delete) {
    return create(Update, Create, Delete);
  }
  public boolean is_GlobalSecondaryIndexUpdate() { return true; }
  public Wrappers_Compile.Option<UpdateGlobalSecondaryIndexAction> dtor_Update() {
    return this._Update;
  }
  public Wrappers_Compile.Option<CreateGlobalSecondaryIndexAction> dtor_Create() {
    return this._Create;
  }
  public Wrappers_Compile.Option<DeleteGlobalSecondaryIndexAction> dtor_Delete() {
    return this._Delete;
  }
}
