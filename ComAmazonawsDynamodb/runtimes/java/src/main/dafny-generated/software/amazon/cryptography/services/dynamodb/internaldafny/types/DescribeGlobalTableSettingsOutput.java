// Class DescribeGlobalTableSettingsOutput
// Dafny class DescribeGlobalTableSettingsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeGlobalTableSettingsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> _ReplicaSettings;
  public DescribeGlobalTableSettingsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    this._GlobalTableName = GlobalTableName;
    this._ReplicaSettings = ReplicaSettings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeGlobalTableSettingsOutput o = (DescribeGlobalTableSettingsOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeGlobalTableSettingsOutput.DescribeGlobalTableSettingsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaSettings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeGlobalTableSettingsOutput> _TYPE = dafny.TypeDescriptor.<DescribeGlobalTableSettingsOutput>referenceWithInitializer(DescribeGlobalTableSettingsOutput.class, () -> DescribeGlobalTableSettingsOutput.Default());
  public static dafny.TypeDescriptor<DescribeGlobalTableSettingsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeGlobalTableSettingsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeGlobalTableSettingsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableSettingsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaSettingsDescription>>Default(dafny.DafnySequence.<ReplicaSettingsDescription>_typeDescriptor(ReplicaSettingsDescription._typeDescriptor())));
  public static DescribeGlobalTableSettingsOutput Default() {
    return theDefault;
  }
  public static DescribeGlobalTableSettingsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    return new DescribeGlobalTableSettingsOutput(GlobalTableName, ReplicaSettings);
  }
  public static DescribeGlobalTableSettingsOutput create_DescribeGlobalTableSettingsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> ReplicaSettings) {
    return create(GlobalTableName, ReplicaSettings);
  }
  public boolean is_DescribeGlobalTableSettingsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsDescription>> dtor_ReplicaSettings() {
    return this._ReplicaSettings;
  }
}
