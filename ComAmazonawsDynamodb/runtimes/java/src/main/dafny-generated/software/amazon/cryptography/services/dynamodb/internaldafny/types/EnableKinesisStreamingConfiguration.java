// Class EnableKinesisStreamingConfiguration
// Dafny class EnableKinesisStreamingConfiguration compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EnableKinesisStreamingConfiguration {
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> _ApproximateCreationDateTimePrecision;
  public EnableKinesisStreamingConfiguration (Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    this._ApproximateCreationDateTimePrecision = ApproximateCreationDateTimePrecision;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EnableKinesisStreamingConfiguration o = (EnableKinesisStreamingConfiguration)other;
    return true && java.util.Objects.equals(this._ApproximateCreationDateTimePrecision, o._ApproximateCreationDateTimePrecision);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ApproximateCreationDateTimePrecision);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.EnableKinesisStreamingConfiguration.EnableKinesisStreamingConfiguration");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ApproximateCreationDateTimePrecision));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EnableKinesisStreamingConfiguration> _TYPE = dafny.TypeDescriptor.<EnableKinesisStreamingConfiguration>referenceWithInitializer(EnableKinesisStreamingConfiguration.class, () -> EnableKinesisStreamingConfiguration.Default());
  public static dafny.TypeDescriptor<EnableKinesisStreamingConfiguration> _typeDescriptor() {
    return (dafny.TypeDescriptor<EnableKinesisStreamingConfiguration>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EnableKinesisStreamingConfiguration theDefault = EnableKinesisStreamingConfiguration.create(Wrappers_Compile.Option.<ApproximateCreationDateTimePrecision>Default(ApproximateCreationDateTimePrecision._typeDescriptor()));
  public static EnableKinesisStreamingConfiguration Default() {
    return theDefault;
  }
  public static EnableKinesisStreamingConfiguration create(Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return new EnableKinesisStreamingConfiguration(ApproximateCreationDateTimePrecision);
  }
  public static EnableKinesisStreamingConfiguration create_EnableKinesisStreamingConfiguration(Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return create(ApproximateCreationDateTimePrecision);
  }
  public boolean is_EnableKinesisStreamingConfiguration() { return true; }
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> dtor_ApproximateCreationDateTimePrecision() {
    return this._ApproximateCreationDateTimePrecision;
  }
}
