// Class EnableKinesisStreamingDestinationInput
// Dafny class EnableKinesisStreamingDestinationInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class EnableKinesisStreamingDestinationInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends Character> _StreamArn;
  public Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> _EnableKinesisStreamingConfiguration;
  public EnableKinesisStreamingDestinationInput (dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    this._TableName = TableName;
    this._StreamArn = StreamArn;
    this._EnableKinesisStreamingConfiguration = EnableKinesisStreamingConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EnableKinesisStreamingDestinationInput o = (EnableKinesisStreamingDestinationInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._StreamArn, o._StreamArn) && java.util.Objects.equals(this._EnableKinesisStreamingConfiguration, o._EnableKinesisStreamingConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EnableKinesisStreamingConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.EnableKinesisStreamingDestinationInput.EnableKinesisStreamingDestinationInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EnableKinesisStreamingConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EnableKinesisStreamingDestinationInput> _TYPE = dafny.TypeDescriptor.<EnableKinesisStreamingDestinationInput>referenceWithInitializer(EnableKinesisStreamingDestinationInput.class, () -> EnableKinesisStreamingDestinationInput.Default());
  public static dafny.TypeDescriptor<EnableKinesisStreamingDestinationInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<EnableKinesisStreamingDestinationInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EnableKinesisStreamingDestinationInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.EnableKinesisStreamingDestinationInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<EnableKinesisStreamingConfiguration>Default(EnableKinesisStreamingConfiguration._typeDescriptor()));
  public static EnableKinesisStreamingDestinationInput Default() {
    return theDefault;
  }
  public static EnableKinesisStreamingDestinationInput create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return new EnableKinesisStreamingDestinationInput(TableName, StreamArn, EnableKinesisStreamingConfiguration);
  }
  public static EnableKinesisStreamingDestinationInput create_EnableKinesisStreamingDestinationInput(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> StreamArn, Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> EnableKinesisStreamingConfiguration) {
    return create(TableName, StreamArn, EnableKinesisStreamingConfiguration);
  }
  public boolean is_EnableKinesisStreamingDestinationInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_StreamArn() {
    return this._StreamArn;
  }
  public Wrappers_Compile.Option<EnableKinesisStreamingConfiguration> dtor_EnableKinesisStreamingConfiguration() {
    return this._EnableKinesisStreamingConfiguration;
  }
}
