// Class KinesisStreamingDestinationOutput
// Dafny class KinesisStreamingDestinationOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KinesisStreamingDestinationOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StreamArn;
  public Wrappers_Compile.Option<DestinationStatus> _DestinationStatus;
  public Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> _EnableKinesisStreamingConfiguration;
  public KinesisStreamingDestinationOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
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
    KinesisStreamingDestinationOutput o = (KinesisStreamingDestinationOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.KinesisStreamingDestinationOutput.KinesisStreamingDestinationOutput");
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
  private static final dafny.TypeDescriptor<KinesisStreamingDestinationOutput> _TYPE = dafny.TypeDescriptor.<KinesisStreamingDestinationOutput>referenceWithInitializer(KinesisStreamingDestinationOutput.class, () -> KinesisStreamingDestinationOutput.Default());
  public static dafny.TypeDescriptor<KinesisStreamingDestinationOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<KinesisStreamingDestinationOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KinesisStreamingDestinationOutput theDefault = KinesisStreamingDestinationOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(StreamArn._typeDescriptor()), Wrappers_Compile.Option.<DestinationStatus>Default(DestinationStatus._typeDescriptor()), Wrappers_Compile.Option.<EnableKinesisStreamingConfiguration>Default(EnableKinesisStreamingConfiguration._typeDescriptor()));
  public static KinesisStreamingDestinationOutput Default() {
    return theDefault;
  }
  public static KinesisStreamingDestinationOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return new KinesisStreamingDestinationOutput(TableName, StreamArn, DestinationStatus, EnableKinesisStreamingConfiguration);
  }
  public static KinesisStreamingDestinationOutput create_KinesisStreamingDestinationOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return create(TableName, StreamArn, DestinationStatus, EnableKinesisStreamingConfiguration);
  }
  public boolean is_KinesisStreamingDestinationOutput() { return true; }
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
