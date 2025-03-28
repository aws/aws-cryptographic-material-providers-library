// Class KinesisDataStreamDestination
// Dafny class KinesisDataStreamDestination compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KinesisDataStreamDestination {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _StreamArn;
  public Wrappers_Compile.Option<DestinationStatus> _DestinationStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _DestinationStatusDescription;
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> _ApproximateCreationDateTimePrecision;
  public KinesisDataStreamDestination (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DestinationStatusDescription, Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    this._StreamArn = StreamArn;
    this._DestinationStatus = DestinationStatus;
    this._DestinationStatusDescription = DestinationStatusDescription;
    this._ApproximateCreationDateTimePrecision = ApproximateCreationDateTimePrecision;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KinesisDataStreamDestination o = (KinesisDataStreamDestination)other;
    return true && java.util.Objects.equals(this._StreamArn, o._StreamArn) && java.util.Objects.equals(this._DestinationStatus, o._DestinationStatus) && java.util.Objects.equals(this._DestinationStatusDescription, o._DestinationStatusDescription) && java.util.Objects.equals(this._ApproximateCreationDateTimePrecision, o._ApproximateCreationDateTimePrecision);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationStatusDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ApproximateCreationDateTimePrecision);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.KinesisDataStreamDestination.KinesisDataStreamDestination");
    s.append("(");
    s.append(dafny.Helpers.toString(this._StreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationStatusDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ApproximateCreationDateTimePrecision));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KinesisDataStreamDestination> _TYPE = dafny.TypeDescriptor.<KinesisDataStreamDestination>referenceWithInitializer(KinesisDataStreamDestination.class, () -> KinesisDataStreamDestination.Default());
  public static dafny.TypeDescriptor<KinesisDataStreamDestination> _typeDescriptor() {
    return (dafny.TypeDescriptor<KinesisDataStreamDestination>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KinesisDataStreamDestination theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.KinesisDataStreamDestination.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(StreamArn._typeDescriptor()), Wrappers_Compile.Option.<DestinationStatus>Default(DestinationStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ApproximateCreationDateTimePrecision>Default(ApproximateCreationDateTimePrecision._typeDescriptor()));
  public static KinesisDataStreamDestination Default() {
    return theDefault;
  }
  public static KinesisDataStreamDestination create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DestinationStatusDescription, Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return new KinesisDataStreamDestination(StreamArn, DestinationStatus, DestinationStatusDescription, ApproximateCreationDateTimePrecision);
  }
  public static KinesisDataStreamDestination create_KinesisDataStreamDestination(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> StreamArn, Wrappers_Compile.Option<DestinationStatus> DestinationStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DestinationStatusDescription, Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> ApproximateCreationDateTimePrecision) {
    return create(StreamArn, DestinationStatus, DestinationStatusDescription, ApproximateCreationDateTimePrecision);
  }
  public boolean is_KinesisDataStreamDestination() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_StreamArn() {
    return this._StreamArn;
  }
  public Wrappers_Compile.Option<DestinationStatus> dtor_DestinationStatus() {
    return this._DestinationStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_DestinationStatusDescription() {
    return this._DestinationStatusDescription;
  }
  public Wrappers_Compile.Option<ApproximateCreationDateTimePrecision> dtor_ApproximateCreationDateTimePrecision() {
    return this._ApproximateCreationDateTimePrecision;
  }
}
