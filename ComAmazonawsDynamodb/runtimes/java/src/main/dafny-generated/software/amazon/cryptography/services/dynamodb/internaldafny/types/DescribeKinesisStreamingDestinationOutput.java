// Class DescribeKinesisStreamingDestinationOutput
// Dafny class DescribeKinesisStreamingDestinationOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeKinesisStreamingDestinationOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KinesisDataStreamDestination>> _KinesisDataStreamDestinations;
  public DescribeKinesisStreamingDestinationOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KinesisDataStreamDestination>> KinesisDataStreamDestinations) {
    this._TableName = TableName;
    this._KinesisDataStreamDestinations = KinesisDataStreamDestinations;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeKinesisStreamingDestinationOutput o = (DescribeKinesisStreamingDestinationOutput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._KinesisDataStreamDestinations, o._KinesisDataStreamDestinations);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KinesisDataStreamDestinations);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeKinesisStreamingDestinationOutput.DescribeKinesisStreamingDestinationOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KinesisDataStreamDestinations));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeKinesisStreamingDestinationOutput> _TYPE = dafny.TypeDescriptor.<DescribeKinesisStreamingDestinationOutput>referenceWithInitializer(DescribeKinesisStreamingDestinationOutput.class, () -> DescribeKinesisStreamingDestinationOutput.Default());
  public static dafny.TypeDescriptor<DescribeKinesisStreamingDestinationOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeKinesisStreamingDestinationOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeKinesisStreamingDestinationOutput theDefault = DescribeKinesisStreamingDestinationOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KinesisDataStreamDestination>>Default(dafny.DafnySequence.<KinesisDataStreamDestination>_typeDescriptor(KinesisDataStreamDestination._typeDescriptor())));
  public static DescribeKinesisStreamingDestinationOutput Default() {
    return theDefault;
  }
  public static DescribeKinesisStreamingDestinationOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KinesisDataStreamDestination>> KinesisDataStreamDestinations) {
    return new DescribeKinesisStreamingDestinationOutput(TableName, KinesisDataStreamDestinations);
  }
  public static DescribeKinesisStreamingDestinationOutput create_DescribeKinesisStreamingDestinationOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KinesisDataStreamDestination>> KinesisDataStreamDestinations) {
    return create(TableName, KinesisDataStreamDestinations);
  }
  public boolean is_DescribeKinesisStreamingDestinationOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KinesisDataStreamDestination>> dtor_KinesisDataStreamDestinations() {
    return this._KinesisDataStreamDestinations;
  }
}
