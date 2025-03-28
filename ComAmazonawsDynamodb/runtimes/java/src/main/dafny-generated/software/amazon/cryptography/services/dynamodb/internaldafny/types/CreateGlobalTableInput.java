// Class CreateGlobalTableInput
// Dafny class CreateGlobalTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateGlobalTableInput {
  public dafny.DafnySequence<? extends Character> _GlobalTableName;
  public dafny.DafnySequence<? extends Replica> _ReplicationGroup;
  public CreateGlobalTableInput (dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends Replica> ReplicationGroup) {
    this._GlobalTableName = GlobalTableName;
    this._ReplicationGroup = ReplicationGroup;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateGlobalTableInput o = (CreateGlobalTableInput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName) && java.util.Objects.equals(this._ReplicationGroup, o._ReplicationGroup);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicationGroup);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateGlobalTableInput.CreateGlobalTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicationGroup));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateGlobalTableInput> _TYPE = dafny.TypeDescriptor.<CreateGlobalTableInput>referenceWithInitializer(CreateGlobalTableInput.class, () -> CreateGlobalTableInput.Default());
  public static dafny.TypeDescriptor<CreateGlobalTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateGlobalTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateGlobalTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateGlobalTableInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Replica> empty(Replica._typeDescriptor()));
  public static CreateGlobalTableInput Default() {
    return theDefault;
  }
  public static CreateGlobalTableInput create(dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends Replica> ReplicationGroup) {
    return new CreateGlobalTableInput(GlobalTableName, ReplicationGroup);
  }
  public static CreateGlobalTableInput create_CreateGlobalTableInput(dafny.DafnySequence<? extends Character> GlobalTableName, dafny.DafnySequence<? extends Replica> ReplicationGroup) {
    return create(GlobalTableName, ReplicationGroup);
  }
  public boolean is_CreateGlobalTableInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public dafny.DafnySequence<? extends Replica> dtor_ReplicationGroup() {
    return this._ReplicationGroup;
  }
}
