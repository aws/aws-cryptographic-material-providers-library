// Class TableAutoScalingDescription
// Dafny class TableAutoScalingDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TableAutoScalingDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<TableStatus> _TableStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>> _Replicas;
  public TableAutoScalingDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>> Replicas) {
    this._TableName = TableName;
    this._TableStatus = TableStatus;
    this._Replicas = Replicas;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableAutoScalingDescription o = (TableAutoScalingDescription)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._TableStatus, o._TableStatus) && java.util.Objects.equals(this._Replicas, o._Replicas);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Replicas);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableAutoScalingDescription.TableAutoScalingDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Replicas));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TableAutoScalingDescription> _TYPE = dafny.TypeDescriptor.<TableAutoScalingDescription>referenceWithInitializer(TableAutoScalingDescription.class, () -> TableAutoScalingDescription.Default());
  public static dafny.TypeDescriptor<TableAutoScalingDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableAutoScalingDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableAutoScalingDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TableAutoScalingDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<TableStatus>Default(TableStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>>Default(dafny.DafnySequence.<ReplicaAutoScalingDescription>_typeDescriptor(ReplicaAutoScalingDescription._typeDescriptor())));
  public static TableAutoScalingDescription Default() {
    return theDefault;
  }
  public static TableAutoScalingDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>> Replicas) {
    return new TableAutoScalingDescription(TableName, TableStatus, Replicas);
  }
  public static TableAutoScalingDescription create_TableAutoScalingDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>> Replicas) {
    return create(TableName, TableStatus, Replicas);
  }
  public boolean is_TableAutoScalingDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<TableStatus> dtor_TableStatus() {
    return this._TableStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingDescription>> dtor_Replicas() {
    return this._Replicas;
  }
}
