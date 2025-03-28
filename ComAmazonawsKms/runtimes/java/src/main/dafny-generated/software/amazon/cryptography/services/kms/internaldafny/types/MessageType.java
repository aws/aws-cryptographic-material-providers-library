// Class MessageType
// Dafny class MessageType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class MessageType {
  public MessageType() {
  }
  private static final dafny.TypeDescriptor<MessageType> _TYPE = dafny.TypeDescriptor.<MessageType>referenceWithInitializer(MessageType.class, () -> MessageType.Default());
  public static dafny.TypeDescriptor<MessageType> _typeDescriptor() {
    return (dafny.TypeDescriptor<MessageType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MessageType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.MessageType.create_RAW();
  public static MessageType Default() {
    return theDefault;
  }
  public static MessageType create_RAW() {
    return new MessageType_RAW();
  }
  public static MessageType create_DIGEST() {
    return new MessageType_DIGEST();
  }
  public boolean is_RAW() { return this instanceof MessageType_RAW; }
  public boolean is_DIGEST() { return this instanceof MessageType_DIGEST; }
  public static java.util.ArrayList<MessageType> AllSingletonConstructors() {
    java.util.ArrayList<MessageType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new MessageType_RAW());
    singleton_iterator.add(new MessageType_DIGEST());
    return singleton_iterator;
  }
}
