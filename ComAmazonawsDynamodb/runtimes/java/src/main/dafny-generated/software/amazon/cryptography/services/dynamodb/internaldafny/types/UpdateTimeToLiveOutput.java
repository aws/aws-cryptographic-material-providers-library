// Class UpdateTimeToLiveOutput
// Dafny class UpdateTimeToLiveOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTimeToLiveOutput {
  public Wrappers_Compile.Option<TimeToLiveSpecification> _TimeToLiveSpecification;
  public UpdateTimeToLiveOutput (Wrappers_Compile.Option<TimeToLiveSpecification> TimeToLiveSpecification) {
    this._TimeToLiveSpecification = TimeToLiveSpecification;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTimeToLiveOutput o = (UpdateTimeToLiveOutput)other;
    return true && java.util.Objects.equals(this._TimeToLiveSpecification, o._TimeToLiveSpecification);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeToLiveSpecification);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateTimeToLiveOutput.UpdateTimeToLiveOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TimeToLiveSpecification));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTimeToLiveOutput> _TYPE = dafny.TypeDescriptor.<UpdateTimeToLiveOutput>referenceWithInitializer(UpdateTimeToLiveOutput.class, () -> UpdateTimeToLiveOutput.Default());
  public static dafny.TypeDescriptor<UpdateTimeToLiveOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTimeToLiveOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTimeToLiveOutput theDefault = UpdateTimeToLiveOutput.create(Wrappers_Compile.Option.<TimeToLiveSpecification>Default(TimeToLiveSpecification._typeDescriptor()));
  public static UpdateTimeToLiveOutput Default() {
    return theDefault;
  }
  public static UpdateTimeToLiveOutput create(Wrappers_Compile.Option<TimeToLiveSpecification> TimeToLiveSpecification) {
    return new UpdateTimeToLiveOutput(TimeToLiveSpecification);
  }
  public static UpdateTimeToLiveOutput create_UpdateTimeToLiveOutput(Wrappers_Compile.Option<TimeToLiveSpecification> TimeToLiveSpecification) {
    return create(TimeToLiveSpecification);
  }
  public boolean is_UpdateTimeToLiveOutput() { return true; }
  public Wrappers_Compile.Option<TimeToLiveSpecification> dtor_TimeToLiveSpecification() {
    return this._TimeToLiveSpecification;
  }
}
