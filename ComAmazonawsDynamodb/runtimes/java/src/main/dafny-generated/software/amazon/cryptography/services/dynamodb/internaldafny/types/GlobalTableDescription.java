// Class GlobalTableDescription
// Dafny class GlobalTableDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTableDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> _ReplicationGroup;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDateTime;
  public Wrappers_Compile.Option<GlobalTableStatus> _GlobalTableStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableName;
  public GlobalTableDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> ReplicationGroup, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<GlobalTableStatus> GlobalTableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName) {
    this._ReplicationGroup = ReplicationGroup;
    this._GlobalTableArn = GlobalTableArn;
    this._CreationDateTime = CreationDateTime;
    this._GlobalTableStatus = GlobalTableStatus;
    this._GlobalTableName = GlobalTableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalTableDescription o = (GlobalTableDescription)other;
    return true && java.util.Objects.equals(this._ReplicationGroup, o._ReplicationGroup) && java.util.Objects.equals(this._GlobalTableArn, o._GlobalTableArn) && java.util.Objects.equals(this._CreationDateTime, o._CreationDateTime) && java.util.Objects.equals(this._GlobalTableStatus, o._GlobalTableStatus) && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicationGroup);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalTableDescription.GlobalTableDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ReplicationGroup));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalTableDescription> _TYPE = dafny.TypeDescriptor.<GlobalTableDescription>referenceWithInitializer(GlobalTableDescription.class, () -> GlobalTableDescription.Default());
  public static dafny.TypeDescriptor<GlobalTableDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalTableDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalTableDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaDescription>>Default(dafny.DafnySequence.<ReplicaDescription>_typeDescriptor(ReplicaDescription._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<GlobalTableStatus>Default(GlobalTableStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()));
  public static GlobalTableDescription Default() {
    return theDefault;
  }
  public static GlobalTableDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> ReplicationGroup, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<GlobalTableStatus> GlobalTableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName) {
    return new GlobalTableDescription(ReplicationGroup, GlobalTableArn, CreationDateTime, GlobalTableStatus, GlobalTableName);
  }
  public static GlobalTableDescription create_GlobalTableDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> ReplicationGroup, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<GlobalTableStatus> GlobalTableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName) {
    return create(ReplicationGroup, GlobalTableArn, CreationDateTime, GlobalTableStatus, GlobalTableName);
  }
  public boolean is_GlobalTableDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> dtor_ReplicationGroup() {
    return this._ReplicationGroup;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableArn() {
    return this._GlobalTableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDateTime() {
    return this._CreationDateTime;
  }
  public Wrappers_Compile.Option<GlobalTableStatus> dtor_GlobalTableStatus() {
    return this._GlobalTableStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
}
