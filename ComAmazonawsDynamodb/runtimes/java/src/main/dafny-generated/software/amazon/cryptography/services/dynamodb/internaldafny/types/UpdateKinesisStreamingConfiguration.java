// Class UpdateKinesisStreamingConfiguration
// Dafny class UpdateKinesisStreamingConfiguration compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateKinesisStreamingConfiguration {
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> _ApproximateCreationDateTimePrecision;
  public UpdateKinesisStreamingConfiguration (Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    this._ApproximateCreationDateTimePrecision = ApproximateCreationDateTimePrecision;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateKinesisStreamingConfiguration o = (UpdateKinesisStreamingConfiguration)other;
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
    s.append("ComAmazonawsDynamodbTypes.UpdateKinesisStreamingConfiguration.UpdateKinesisStreamingConfiguration");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ApproximateCreationDateTimePrecision));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateKinesisStreamingConfiguration> _TYPE = dafny.TypeDescriptor.<UpdateKinesisStreamingConfiguration>referenceWithInitializer(UpdateKinesisStreamingConfiguration.class, () -> UpdateKinesisStreamingConfiguration.Default());
  public static dafny.TypeDescriptor<UpdateKinesisStreamingConfiguration> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateKinesisStreamingConfiguration>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateKinesisStreamingConfiguration theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingConfiguration.create(Wrappers_Compile.Option.<ApproximateCreationDateTimePrecision>Default(ApproximateCreationDateTimePrecision._typeDescriptor()));
  public static UpdateKinesisStreamingConfiguration Default() {
    return theDefault;
  }
  public static UpdateKinesisStreamingConfiguration create(Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return new UpdateKinesisStreamingConfiguration(ApproximateCreationDateTimePrecision);
  }
  public static UpdateKinesisStreamingConfiguration create_UpdateKinesisStreamingConfiguration(Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return create(ApproximateCreationDateTimePrecision);
  }
  public boolean is_UpdateKinesisStreamingConfiguration() { return true; }
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> dtor_ApproximateCreationDateTimePrecision() {
    return this._ApproximateCreationDateTimePrecision;
  }
}
