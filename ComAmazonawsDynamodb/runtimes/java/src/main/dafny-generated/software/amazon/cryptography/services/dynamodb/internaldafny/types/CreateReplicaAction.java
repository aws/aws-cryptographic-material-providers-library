// Class CreateReplicaAction
// Dafny class CreateReplicaAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateReplicaAction {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public CreateReplicaAction (dafny.DafnySequence<? extends Character> RegionName) {
    this._RegionName = RegionName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateReplicaAction o = (CreateReplicaAction)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateReplicaAction.CreateReplicaAction");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateReplicaAction> _TYPE = dafny.TypeDescriptor.<CreateReplicaAction>referenceWithInitializer(CreateReplicaAction.class, () -> CreateReplicaAction.Default());
  public static dafny.TypeDescriptor<CreateReplicaAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateReplicaAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateReplicaAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateReplicaAction.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateReplicaAction Default() {
    return theDefault;
  }
  public static CreateReplicaAction create(dafny.DafnySequence<? extends Character> RegionName) {
    return new CreateReplicaAction(RegionName);
  }
  public static CreateReplicaAction create_CreateReplicaAction(dafny.DafnySequence<? extends Character> RegionName) {
    return create(RegionName);
  }
  public boolean is_CreateReplicaAction() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
}
