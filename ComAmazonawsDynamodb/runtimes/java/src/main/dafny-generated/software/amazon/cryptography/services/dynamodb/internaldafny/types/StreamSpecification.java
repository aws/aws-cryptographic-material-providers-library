// Class StreamSpecification
// Dafny class StreamSpecification compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class StreamSpecification {
  public boolean _StreamEnabled;
  public Wrappers_Compile.Option<StreamViewType> _StreamViewType;
  public StreamSpecification (boolean StreamEnabled, Wrappers_Compile.Option<StreamViewType> StreamViewType) {
    this._StreamEnabled = StreamEnabled;
    this._StreamViewType = StreamViewType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StreamSpecification o = (StreamSpecification)other;
    return true && this._StreamEnabled == o._StreamEnabled && java.util.Objects.equals(this._StreamViewType, o._StreamViewType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._StreamEnabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamViewType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.StreamSpecification.StreamSpecification");
    s.append("(");
    s.append(this._StreamEnabled);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamViewType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<StreamSpecification> _TYPE = dafny.TypeDescriptor.<StreamSpecification>referenceWithInitializer(StreamSpecification.class, () -> StreamSpecification.Default());
  public static dafny.TypeDescriptor<StreamSpecification> _typeDescriptor() {
    return (dafny.TypeDescriptor<StreamSpecification>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StreamSpecification theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamSpecification.create(false, Wrappers_Compile.Option.<StreamViewType>Default(StreamViewType._typeDescriptor()));
  public static StreamSpecification Default() {
    return theDefault;
  }
  public static StreamSpecification create(boolean StreamEnabled, Wrappers_Compile.Option<StreamViewType> StreamViewType) {
    return new StreamSpecification(StreamEnabled, StreamViewType);
  }
  public static StreamSpecification create_StreamSpecification(boolean StreamEnabled, Wrappers_Compile.Option<StreamViewType> StreamViewType) {
    return create(StreamEnabled, StreamViewType);
  }
  public boolean is_StreamSpecification() { return true; }
  public boolean dtor_StreamEnabled() {
    return this._StreamEnabled;
  }
  public Wrappers_Compile.Option<StreamViewType> dtor_StreamViewType() {
    return this._StreamViewType;
  }
}
