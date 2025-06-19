// Class Error
// Dafny class Error compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Error {
  public Error() {
  }
  private static final dafny.TypeDescriptor<Error> _TYPE = dafny.TypeDescriptor.<Error>referenceWithInitializer(Error.class, () -> Error.Default());
  public static dafny.TypeDescriptor<Error> _typeDescriptor() {
    return (dafny.TypeDescriptor<Error>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Error theDefault = Error.create_KeyStoreException(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static Error Default() {
    return theDefault;
  }
  public static Error create_KeyStoreException(dafny.DafnySequence<? extends Character> message) {
    return new Error_KeyStoreException(message);
  }
  public static Error create_ComAmazonawsDynamodb(software.amazon.cryptography.services.dynamodb.internaldafny.types.Error ComAmazonawsDynamodb) {
    return new Error_ComAmazonawsDynamodb(ComAmazonawsDynamodb);
  }
  public static Error create_ComAmazonawsKms(software.amazon.cryptography.services.kms.internaldafny.types.Error ComAmazonawsKms) {
    return new Error_ComAmazonawsKms(ComAmazonawsKms);
  }
  public static Error create_CollectionOfErrors(dafny.DafnySequence<? extends Error> list, dafny.DafnySequence<? extends Character> message) {
    return new Error_CollectionOfErrors(list, message);
  }
  public static Error create_Opaque(Object obj) {
    return new Error_Opaque(obj);
  }
  public static Error create_OpaqueWithText(Object obj, dafny.DafnySequence<? extends Character> objMessage) {
    return new Error_OpaqueWithText(obj, objMessage);
  }
  public boolean is_KeyStoreException() { return this instanceof Error_KeyStoreException; }
  public boolean is_ComAmazonawsDynamodb() { return this instanceof Error_ComAmazonawsDynamodb; }
  public boolean is_ComAmazonawsKms() { return this instanceof Error_ComAmazonawsKms; }
  public boolean is_CollectionOfErrors() { return this instanceof Error_CollectionOfErrors; }
  public boolean is_Opaque() { return this instanceof Error_Opaque; }
  public boolean is_OpaqueWithText() { return this instanceof Error_OpaqueWithText; }
  public dafny.DafnySequence<? extends Character> dtor_message() {
    Error d = this;
    if (d instanceof Error_KeyStoreException) { return ((Error_KeyStoreException)d)._message; }
    return ((Error_CollectionOfErrors)d)._message;
  }
  public software.amazon.cryptography.services.dynamodb.internaldafny.types.Error dtor_ComAmazonawsDynamodb() {
    Error d = this;
    return ((Error_ComAmazonawsDynamodb)d)._ComAmazonawsDynamodb;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.Error dtor_ComAmazonawsKms() {
    Error d = this;
    return ((Error_ComAmazonawsKms)d)._ComAmazonawsKms;
  }
  public dafny.DafnySequence<? extends Error> dtor_list() {
    Error d = this;
    return ((Error_CollectionOfErrors)d)._list;
  }
  public Object dtor_obj() {
    Error d = this;
    if (d instanceof Error_Opaque) { return ((Error_Opaque)d)._obj; }
    return ((Error_OpaqueWithText)d)._obj;
  }
  public dafny.DafnySequence<? extends Character> dtor_objMessage() {
    Error d = this;
    return ((Error_OpaqueWithText)d)._objMessage;
  }
}
