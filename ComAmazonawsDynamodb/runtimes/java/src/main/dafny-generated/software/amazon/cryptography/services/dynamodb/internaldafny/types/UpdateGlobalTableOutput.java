// Class UpdateGlobalTableOutput
// Dafny class UpdateGlobalTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateGlobalTableOutput {
  public Wrappers_Compile.Option<GlobalTableDescription> _GlobalTableDescription;
  public UpdateGlobalTableOutput (Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    this._GlobalTableDescription = GlobalTableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateGlobalTableOutput o = (UpdateGlobalTableOutput)other;
    return true && java.util.Objects.equals(this._GlobalTableDescription, o._GlobalTableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateGlobalTableOutput.UpdateGlobalTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateGlobalTableOutput> _TYPE = dafny.TypeDescriptor.<UpdateGlobalTableOutput>referenceWithInitializer(UpdateGlobalTableOutput.class, () -> UpdateGlobalTableOutput.Default());
  public static dafny.TypeDescriptor<UpdateGlobalTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateGlobalTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateGlobalTableOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableOutput.create(Wrappers_Compile.Option.<GlobalTableDescription>Default(GlobalTableDescription._typeDescriptor()));
  public static UpdateGlobalTableOutput Default() {
    return theDefault;
  }
  public static UpdateGlobalTableOutput create(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return new UpdateGlobalTableOutput(GlobalTableDescription);
  }
  public static UpdateGlobalTableOutput create_UpdateGlobalTableOutput(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return create(GlobalTableDescription);
  }
  public boolean is_UpdateGlobalTableOutput() { return true; }
  public Wrappers_Compile.Option<GlobalTableDescription> dtor_GlobalTableDescription() {
    return this._GlobalTableDescription;
  }
}
