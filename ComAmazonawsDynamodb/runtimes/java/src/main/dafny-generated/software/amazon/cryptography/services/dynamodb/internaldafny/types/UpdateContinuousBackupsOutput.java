// Class UpdateContinuousBackupsOutput
// Dafny class UpdateContinuousBackupsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateContinuousBackupsOutput {
  public Wrappers_Compile.Option<ContinuousBackupsDescription> _ContinuousBackupsDescription;
  public UpdateContinuousBackupsOutput (Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    this._ContinuousBackupsDescription = ContinuousBackupsDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateContinuousBackupsOutput o = (UpdateContinuousBackupsOutput)other;
    return true && java.util.Objects.equals(this._ContinuousBackupsDescription, o._ContinuousBackupsDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ContinuousBackupsDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateContinuousBackupsOutput.UpdateContinuousBackupsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ContinuousBackupsDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateContinuousBackupsOutput> _TYPE = dafny.TypeDescriptor.<UpdateContinuousBackupsOutput>referenceWithInitializer(UpdateContinuousBackupsOutput.class, () -> UpdateContinuousBackupsOutput.Default());
  public static dafny.TypeDescriptor<UpdateContinuousBackupsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateContinuousBackupsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateContinuousBackupsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContinuousBackupsOutput.create(Wrappers_Compile.Option.<ContinuousBackupsDescription>Default(ContinuousBackupsDescription._typeDescriptor()));
  public static UpdateContinuousBackupsOutput Default() {
    return theDefault;
  }
  public static UpdateContinuousBackupsOutput create(Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    return new UpdateContinuousBackupsOutput(ContinuousBackupsDescription);
  }
  public static UpdateContinuousBackupsOutput create_UpdateContinuousBackupsOutput(Wrappers_Compile.Option<ContinuousBackupsDescription> ContinuousBackupsDescription) {
    return create(ContinuousBackupsDescription);
  }
  public boolean is_UpdateContinuousBackupsOutput() { return true; }
  public Wrappers_Compile.Option<ContinuousBackupsDescription> dtor_ContinuousBackupsDescription() {
    return this._ContinuousBackupsDescription;
  }
}
