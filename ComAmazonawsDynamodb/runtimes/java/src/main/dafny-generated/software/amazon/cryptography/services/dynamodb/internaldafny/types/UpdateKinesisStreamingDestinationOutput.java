// Class UpdateKinesisStreamingDestinationOutput
// Dafny class UpdateKinesisStreamingDestinationOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateKinesisStreamingDestinationOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StreamArn;
  public Wrappers_Compile.Option<DestinationStatus> _DestinationStatus;
  public Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> _UpdateKinesisStreamingConfiguration;
  public UpdateKinesisStreamingDestinationOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    this._TableName = TableName;
    this._StreamArn = StreamArn;
    this._DestinationStatus = DestinationStatus;
    this._UpdateKinesisStreamingConfiguration = UpdateKinesisStreamingConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateKinesisStreamingDestinationOutput o = (UpdateKinesisStreamingDestinationOutput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._StreamArn, o._StreamArn) && java.util.Objects.equals(this._DestinationStatus, o._DestinationStatus) && java.util.Objects.equals(this._UpdateKinesisStreamingConfiguration, o._UpdateKinesisStreamingConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UpdateKinesisStreamingConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateKinesisStreamingDestinationOutput.UpdateKinesisStreamingDestinationOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UpdateKinesisStreamingConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateKinesisStreamingDestinationOutput> _TYPE = dafny.TypeDescriptor.<UpdateKinesisStreamingDestinationOutput>referenceWithInitializer(UpdateKinesisStreamingDestinationOutput.class, () -> UpdateKinesisStreamingDestinationOutput.Default());
  public static dafny.TypeDescriptor<UpdateKinesisStreamingDestinationOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateKinesisStreamingDestinationOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateKinesisStreamingDestinationOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingDestinationOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(StreamArn._typeDescriptor()), Wrappers_Compile.Option.<DestinationStatus>Default(DestinationStatus._typeDescriptor()), Wrappers_Compile.Option.<UpdateKinesisStreamingConfiguration>Default(UpdateKinesisStreamingConfiguration._typeDescriptor()));
  public static UpdateKinesisStreamingDestinationOutput Default() {
    return theDefault;
  }
  public static UpdateKinesisStreamingDestinationOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    return new UpdateKinesisStreamingDestinationOutput(TableName, StreamArn, DestinationStatus, UpdateKinesisStreamingConfiguration);
  }
  public static UpdateKinesisStreamingDestinationOutput create_UpdateKinesisStreamingDestinationOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    return create(TableName, StreamArn, DestinationStatus, UpdateKinesisStreamingConfiguration);
  }
  public boolean is_UpdateKinesisStreamingDestinationOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StreamArn() {
    return this._StreamArn;
  }
  public Wrappers_Compile.Option<DestinationStatus> dtor_DestinationStatus() {
    return this._DestinationStatus;
  }
  public Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> dtor_UpdateKinesisStreamingConfiguration() {
    return this._UpdateKinesisStreamingConfiguration;
  }
}
