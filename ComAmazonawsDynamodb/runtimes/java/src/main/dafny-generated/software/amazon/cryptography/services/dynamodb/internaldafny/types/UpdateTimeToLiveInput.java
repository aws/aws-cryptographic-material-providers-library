// Class UpdateTimeToLiveInput
// Dafny class UpdateTimeToLiveInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTimeToLiveInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public TimeToLiveSpecification _TimeToLiveSpecification;
  public UpdateTimeToLiveInput (dafny.DafnySequence<? extends Character> TableName, TimeToLiveSpecification TimeToLiveSpecification) {
    this._TableName = TableName;
    this._TimeToLiveSpecification = TimeToLiveSpecification;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTimeToLiveInput o = (UpdateTimeToLiveInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._TimeToLiveSpecification, o._TimeToLiveSpecification);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeToLiveSpecification);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateTimeToLiveInput.UpdateTimeToLiveInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TimeToLiveSpecification));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTimeToLiveInput> _TYPE = dafny.TypeDescriptor.<UpdateTimeToLiveInput>referenceWithInitializer(UpdateTimeToLiveInput.class, () -> UpdateTimeToLiveInput.Default());
  public static dafny.TypeDescriptor<UpdateTimeToLiveInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTimeToLiveInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTimeToLiveInput theDefault = UpdateTimeToLiveInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), TimeToLiveSpecification.Default());
  public static UpdateTimeToLiveInput Default() {
    return theDefault;
  }
  public static UpdateTimeToLiveInput create(dafny.DafnySequence<? extends Character> TableName, TimeToLiveSpecification TimeToLiveSpecification) {
    return new UpdateTimeToLiveInput(TableName, TimeToLiveSpecification);
  }
  public static UpdateTimeToLiveInput create_UpdateTimeToLiveInput(dafny.DafnySequence<? extends Character> TableName, TimeToLiveSpecification TimeToLiveSpecification) {
    return create(TableName, TimeToLiveSpecification);
  }
  public boolean is_UpdateTimeToLiveInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public TimeToLiveSpecification dtor_TimeToLiveSpecification() {
    return this._TimeToLiveSpecification;
  }
}
