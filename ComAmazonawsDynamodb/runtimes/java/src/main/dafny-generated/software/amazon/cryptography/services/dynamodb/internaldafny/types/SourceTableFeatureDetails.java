// Class SourceTableFeatureDetails
// Dafny class SourceTableFeatureDetails compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SourceTableFeatureDetails {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>> _LocalSecondaryIndexes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<StreamSpecification> _StreamDescription;
  public Wrappers_Compile.Option<TimeToLiveDescription> _TimeToLiveDescription;
  public Wrappers_Compile.Option<SSEDescription> _SSEDescription;
  public SourceTableFeatureDetails (Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamDescription, Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription, Wrappers_Compile.Option<SSEDescription> SSEDescription) {
    this._LocalSecondaryIndexes = LocalSecondaryIndexes;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._StreamDescription = StreamDescription;
    this._TimeToLiveDescription = TimeToLiveDescription;
    this._SSEDescription = SSEDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SourceTableFeatureDetails o = (SourceTableFeatureDetails)other;
    return true && java.util.Objects.equals(this._LocalSecondaryIndexes, o._LocalSecondaryIndexes) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._StreamDescription, o._StreamDescription) && java.util.Objects.equals(this._TimeToLiveDescription, o._TimeToLiveDescription) && java.util.Objects.equals(this._SSEDescription, o._SSEDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LocalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TimeToLiveDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSEDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.SourceTableFeatureDetails.SourceTableFeatureDetails");
    s.append("(");
    s.append(dafny.Helpers.toString(this._LocalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TimeToLiveDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSEDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SourceTableFeatureDetails> _TYPE = dafny.TypeDescriptor.<SourceTableFeatureDetails>referenceWithInitializer(SourceTableFeatureDetails.class, () -> SourceTableFeatureDetails.Default());
  public static dafny.TypeDescriptor<SourceTableFeatureDetails> _typeDescriptor() {
    return (dafny.TypeDescriptor<SourceTableFeatureDetails>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SourceTableFeatureDetails theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.SourceTableFeatureDetails.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>>Default(dafny.DafnySequence.<LocalSecondaryIndexInfo>_typeDescriptor(LocalSecondaryIndexInfo._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>>Default(dafny.DafnySequence.<GlobalSecondaryIndexInfo>_typeDescriptor(GlobalSecondaryIndexInfo._typeDescriptor())), Wrappers_Compile.Option.<StreamSpecification>Default(StreamSpecification._typeDescriptor()), Wrappers_Compile.Option.<TimeToLiveDescription>Default(TimeToLiveDescription._typeDescriptor()), Wrappers_Compile.Option.<SSEDescription>Default(SSEDescription._typeDescriptor()));
  public static SourceTableFeatureDetails Default() {
    return theDefault;
  }
  public static SourceTableFeatureDetails create(Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamDescription, Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription, Wrappers_Compile.Option<SSEDescription> SSEDescription) {
    return new SourceTableFeatureDetails(LocalSecondaryIndexes, GlobalSecondaryIndexes, StreamDescription, TimeToLiveDescription, SSEDescription);
  }
  public static SourceTableFeatureDetails create_SourceTableFeatureDetails(Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamDescription, Wrappers_Compile.Option<TimeToLiveDescription> TimeToLiveDescription, Wrappers_Compile.Option<SSEDescription> SSEDescription) {
    return create(LocalSecondaryIndexes, GlobalSecondaryIndexes, StreamDescription, TimeToLiveDescription, SSEDescription);
  }
  public boolean is_SourceTableFeatureDetails() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexInfo>> dtor_LocalSecondaryIndexes() {
    return this._LocalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexInfo>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<StreamSpecification> dtor_StreamDescription() {
    return this._StreamDescription;
  }
  public Wrappers_Compile.Option<TimeToLiveDescription> dtor_TimeToLiveDescription() {
    return this._TimeToLiveDescription;
  }
  public Wrappers_Compile.Option<SSEDescription> dtor_SSEDescription() {
    return this._SSEDescription;
  }
}
