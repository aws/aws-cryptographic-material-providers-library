// Class UpdateContinuousBackupsInput
// Dafny class UpdateContinuousBackupsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateContinuousBackupsInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public PointInTimeRecoverySpecification _PointInTimeRecoverySpecification;
  public UpdateContinuousBackupsInput (dafny.DafnySequence<? extends Character> TableName, PointInTimeRecoverySpecification PointInTimeRecoverySpecification) {
    this._TableName = TableName;
    this._PointInTimeRecoverySpecification = PointInTimeRecoverySpecification;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateContinuousBackupsInput o = (UpdateContinuousBackupsInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._PointInTimeRecoverySpecification, o._PointInTimeRecoverySpecification);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PointInTimeRecoverySpecification);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateContinuousBackupsInput.UpdateContinuousBackupsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PointInTimeRecoverySpecification));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateContinuousBackupsInput> _TYPE = dafny.TypeDescriptor.<UpdateContinuousBackupsInput>referenceWithInitializer(UpdateContinuousBackupsInput.class, () -> UpdateContinuousBackupsInput.Default());
  public static dafny.TypeDescriptor<UpdateContinuousBackupsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateContinuousBackupsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateContinuousBackupsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContinuousBackupsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), PointInTimeRecoverySpecification.Default());
  public static UpdateContinuousBackupsInput Default() {
    return theDefault;
  }
  public static UpdateContinuousBackupsInput create(dafny.DafnySequence<? extends Character> TableName, PointInTimeRecoverySpecification PointInTimeRecoverySpecification) {
    return new UpdateContinuousBackupsInput(TableName, PointInTimeRecoverySpecification);
  }
  public static UpdateContinuousBackupsInput create_UpdateContinuousBackupsInput(dafny.DafnySequence<? extends Character> TableName, PointInTimeRecoverySpecification PointInTimeRecoverySpecification) {
    return create(TableName, PointInTimeRecoverySpecification);
  }
  public boolean is_UpdateContinuousBackupsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public PointInTimeRecoverySpecification dtor_PointInTimeRecoverySpecification() {
    return this._PointInTimeRecoverySpecification;
  }
}
