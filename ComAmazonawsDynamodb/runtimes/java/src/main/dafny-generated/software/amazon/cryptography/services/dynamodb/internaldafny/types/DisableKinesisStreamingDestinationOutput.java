// Class DisableKinesisStreamingDestinationOutput
// Dafny class DisableKinesisStreamingDestinationOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DisableKinesisStreamingDestinationOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StreamArn;
  public Wrappers_Compile.Option<DestinationStatus> _DestinationStatus;
  public Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> _EnableKinesisStreamingConfiguration;
  public DisableKinesisStreamingDestinationOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    this._TableName = TableName;
    this._StreamArn = StreamArn;
    this._DestinationStatus = DestinationStatus;
    this._EnableKinesisStreamingConfiguration = EnableKinesisStreamingConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DisableKinesisStreamingDestinationOutput o = (DisableKinesisStreamingDestinationOutput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._StreamArn, o._StreamArn) && java.util.Objects.equals(this._DestinationStatus, o._DestinationStatus) && java.util.Objects.equals(this._EnableKinesisStreamingConfiguration, o._EnableKinesisStreamingConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EnableKinesisStreamingConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DisableKinesisStreamingDestinationOutput.DisableKinesisStreamingDestinationOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EnableKinesisStreamingConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DisableKinesisStreamingDestinationOutput> _TYPE = dafny.TypeDescriptor.<DisableKinesisStreamingDestinationOutput>referenceWithInitializer(DisableKinesisStreamingDestinationOutput.class, () -> DisableKinesisStreamingDestinationOutput.Default());
  public static dafny.TypeDescriptor<DisableKinesisStreamingDestinationOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DisableKinesisStreamingDestinationOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DisableKinesisStreamingDestinationOutput theDefault = DisableKinesisStreamingDestinationOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(StreamArn._typeDescriptor()), Wrappers_Compile.Option.<DestinationStatus>Default(DestinationStatus._typeDescriptor()), Wrappers_Compile.Option.<EnableKinesisStreamingConfiguration>Default(EnableKinesisStreamingConfiguration._typeDescriptor()));
  public static DisableKinesisStreamingDestinationOutput Default() {
    return theDefault;
  }
  public static DisableKinesisStreamingDestinationOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return new DisableKinesisStreamingDestinationOutput(TableName, StreamArn, DestinationStatus, EnableKinesisStreamingConfiguration);
  }
  public static DisableKinesisStreamingDestinationOutput create_DisableKinesisStreamingDestinationOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return create(TableName, StreamArn, DestinationStatus, EnableKinesisStreamingConfiguration);
  }
  public boolean is_DisableKinesisStreamingDestinationOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StreamArn() {
    return this._StreamArn;
  }
  public Wrappers_Compile.Option<DestinationStatus> dtor_DestinationStatus() {
    return this._DestinationStatus;
  }
  public Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> dtor_EnableKinesisStreamingConfiguration() {
    return this._EnableKinesisStreamingConfiguration;
  }
}
