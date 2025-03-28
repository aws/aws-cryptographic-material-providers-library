// Class UpdateKinesisStreamingDestinationInput
// Dafny class UpdateKinesisStreamingDestinationInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateKinesisStreamingDestinationInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends Character> _StreamArn;
  public Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> _UpdateKinesisStreamingConfiguration;
  public UpdateKinesisStreamingDestinationInput (dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    this._TableName = TableName;
    this._StreamArn = StreamArn;
    this._UpdateKinesisStreamingConfiguration = UpdateKinesisStreamingConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateKinesisStreamingDestinationInput o = (UpdateKinesisStreamingDestinationInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._StreamArn, o._StreamArn) && java.util.Objects.equals(this._UpdateKinesisStreamingConfiguration, o._UpdateKinesisStreamingConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UpdateKinesisStreamingConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateKinesisStreamingDestinationInput.UpdateKinesisStreamingDestinationInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UpdateKinesisStreamingConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateKinesisStreamingDestinationInput> _TYPE = dafny.TypeDescriptor.<UpdateKinesisStreamingDestinationInput>referenceWithInitializer(UpdateKinesisStreamingDestinationInput.class, () -> UpdateKinesisStreamingDestinationInput.Default());
  public static dafny.TypeDescriptor<UpdateKinesisStreamingDestinationInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateKinesisStreamingDestinationInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateKinesisStreamingDestinationInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingDestinationInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<UpdateKinesisStreamingConfiguration>Default(UpdateKinesisStreamingConfiguration._typeDescriptor()));
  public static UpdateKinesisStreamingDestinationInput Default() {
    return theDefault;
  }
  public static UpdateKinesisStreamingDestinationInput create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    return new UpdateKinesisStreamingDestinationInput(TableName, StreamArn, UpdateKinesisStreamingConfiguration);
  }
  public static UpdateKinesisStreamingDestinationInput create_UpdateKinesisStreamingDestinationInput(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> UpdateKinesisStreamingConfiguration) {
    return create(TableName, StreamArn, UpdateKinesisStreamingConfiguration);
  }
  public boolean is_UpdateKinesisStreamingDestinationInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_StreamArn() {
    return this._StreamArn;
  }
  public Wrappers_Compile.Option<UpdateKinesisStreamingConfiguration> dtor_UpdateKinesisStreamingConfiguration() {
    return this._UpdateKinesisStreamingConfiguration;
  }
}
