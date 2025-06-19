// Class UpdateGlobalTableSettingsOutput
// Dafny class UpdateGlobalTableSettingsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateGlobalTableSettingsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> _ReplicaSettings;
  public UpdateGlobalTableSettingsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    this._GlobalTableName = GlobalTableName;
    this._ReplicaSettings = ReplicaSettings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateGlobalTableSettingsOutput o = (UpdateGlobalTableSettingsOutput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName) && java.util.Objects.equals(this._ReplicaSettings, o._ReplicaSettings);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaSettings);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateGlobalTableSettingsOutput.UpdateGlobalTableSettingsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaSettings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateGlobalTableSettingsOutput> _TYPE = dafny.TypeDescriptor.<UpdateGlobalTableSettingsOutput>referenceWithInitializer(UpdateGlobalTableSettingsOutput.class, () -> UpdateGlobalTableSettingsOutput.Default());
  public static dafny.TypeDescriptor<UpdateGlobalTableSettingsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateGlobalTableSettingsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateGlobalTableSettingsOutput theDefault = UpdateGlobalTableSettingsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaSettingsDescription>>Default(dafny.DafnySequence.<ReplicaSettingsDescription>_typeDescriptor(ReplicaSettingsDescription._typeDescriptor())));
  public static UpdateGlobalTableSettingsOutput Default() {
    return theDefault;
  }
  public static UpdateGlobalTableSettingsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    return new UpdateGlobalTableSettingsOutput(GlobalTableName, ReplicaSettings);
  }
  public static UpdateGlobalTableSettingsOutput create_UpdateGlobalTableSettingsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    return create(GlobalTableName, ReplicaSettings);
  }
  public boolean is_UpdateGlobalTableSettingsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> dtor_ReplicaSettings() {
    return this._ReplicaSettings;
  }
}
