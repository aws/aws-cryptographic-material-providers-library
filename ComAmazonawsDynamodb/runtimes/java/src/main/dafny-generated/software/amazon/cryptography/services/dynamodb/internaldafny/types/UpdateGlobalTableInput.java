// Class UpdateGlobalTableInput
// Dafny class UpdateGlobalTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateGlobalTableInput {
  public dafny.DafnySequence<? extends Character> _GlobalTableName;
  public dafny.DafnySequence<? extends ReplicaUpdate> _ReplicaUpdates;
  public UpdateGlobalTableInput (dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends ReplicaUpdate> ReplicaUpdates) {
    this._GlobalTableName = GlobalTableName;
    this._ReplicaUpdates = ReplicaUpdates;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateGlobalTableInput o = (UpdateGlobalTableInput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName) && java.util.Objects.equals(this._ReplicaUpdates, o._ReplicaUpdates);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaUpdates);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateGlobalTableInput.UpdateGlobalTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaUpdates));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateGlobalTableInput> _TYPE = dafny.TypeDescriptor.<UpdateGlobalTableInput>referenceWithInitializer(UpdateGlobalTableInput.class, () -> UpdateGlobalTableInput.Default());
  public static dafny.TypeDescriptor<UpdateGlobalTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateGlobalTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateGlobalTableInput theDefault = UpdateGlobalTableInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<ReplicaUpdate> empty(ReplicaUpdate._typeDescriptor()));
  public static UpdateGlobalTableInput Default() {
    return theDefault;
  }
  public static UpdateGlobalTableInput create(dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends ReplicaUpdate> ReplicaUpdates) {
    return new UpdateGlobalTableInput(GlobalTableName, ReplicaUpdates);
  }
  public static UpdateGlobalTableInput create_UpdateGlobalTableInput(dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends ReplicaUpdate> ReplicaUpdates) {
    return create(GlobalTableName, ReplicaUpdates);
  }
  public boolean is_UpdateGlobalTableInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public dafny.DafnySequence<? extends ReplicaUpdate> dtor_ReplicaUpdates() {
    return this._ReplicaUpdates;
  }
}
