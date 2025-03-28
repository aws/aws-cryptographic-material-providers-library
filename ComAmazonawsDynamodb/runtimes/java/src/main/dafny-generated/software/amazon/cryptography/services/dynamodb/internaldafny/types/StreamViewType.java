// Class StreamViewType
// Dafny class StreamViewType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class StreamViewType {
  public StreamViewType() {
  }
  private static final dafny.TypeDescriptor<StreamViewType> _TYPE = dafny.TypeDescriptor.<StreamViewType>referenceWithInitializer(StreamViewType.class, () -> StreamViewType.Default());
  public static dafny.TypeDescriptor<StreamViewType> _typeDescriptor() {
    return (dafny.TypeDescriptor<StreamViewType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StreamViewType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamViewType.create_NEW__IMAGE();
  public static StreamViewType Default() {
    return theDefault;
  }
  public static StreamViewType create_NEW__IMAGE() {
    return new StreamViewType_NEW__IMAGE();
  }
  public static StreamViewType create_OLD__IMAGE() {
    return new StreamViewType_OLD__IMAGE();
  }
  public static StreamViewType create_NEW__AND__OLD__IMAGES() {
    return new StreamViewType_NEW__AND__OLD__IMAGES();
  }
  public static StreamViewType create_KEYS__ONLY() {
    return new StreamViewType_KEYS__ONLY();
  }
  public boolean is_NEW__IMAGE() { return this instanceof StreamViewType_NEW__IMAGE; }
  public boolean is_OLD__IMAGE() { return this instanceof StreamViewType_OLD__IMAGE; }
  public boolean is_NEW__AND__OLD__IMAGES() { return this instanceof StreamViewType_NEW__AND__OLD__IMAGES; }
  public boolean is_KEYS__ONLY() { return this instanceof StreamViewType_KEYS__ONLY; }
  public static java.util.ArrayList<StreamViewType> AllSingletonConstructors() {
    java.util.ArrayList<StreamViewType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new StreamViewType_NEW__IMAGE());
    singleton_iterator.add(new StreamViewType_OLD__IMAGE());
    singleton_iterator.add(new StreamViewType_NEW__AND__OLD__IMAGES());
    singleton_iterator.add(new StreamViewType_KEYS__ONLY());
    return singleton_iterator;
  }
}
