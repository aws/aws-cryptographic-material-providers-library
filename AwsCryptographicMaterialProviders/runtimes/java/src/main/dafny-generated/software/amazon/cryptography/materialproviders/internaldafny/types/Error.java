// Class Error
// Dafny class Error compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Error {
  public Error() {
  }
  private static final dafny.TypeDescriptor<Error> _TYPE = dafny.TypeDescriptor.<Error>referenceWithInitializer(Error.class, () -> Error.Default());
  public static dafny.TypeDescriptor<Error> _typeDescriptor() {
    return (dafny.TypeDescriptor<Error>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Error theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static Error Default() {
    return theDefault;
  }
  public static Error create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence<? extends Character> message) {
    return new Error_AwsCryptographicMaterialProvidersException(message);
  }
  public static Error create_EntryAlreadyExists(dafny.DafnySequence<? extends Character> message) {
    return new Error_EntryAlreadyExists(message);
  }
  public static Error create_EntryDoesNotExist(dafny.DafnySequence<? extends Character> message) {
    return new Error_EntryDoesNotExist(message);
  }
  public static Error create_InFlightTTLExceeded(dafny.DafnySequence<? extends Character> message) {
    return new Error_InFlightTTLExceeded(message);
  }
  public static Error create_InvalidAlgorithmSuiteInfo(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidAlgorithmSuiteInfo(message);
  }
  public static Error create_InvalidAlgorithmSuiteInfoOnDecrypt(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidAlgorithmSuiteInfoOnDecrypt(message);
  }
  public static Error create_InvalidAlgorithmSuiteInfoOnEncrypt(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidAlgorithmSuiteInfoOnEncrypt(message);
  }
  public static Error create_InvalidDecryptionMaterials(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidDecryptionMaterials(message);
  }
  public static Error create_InvalidDecryptionMaterialsTransition(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidDecryptionMaterialsTransition(message);
  }
  public static Error create_InvalidEncryptionMaterials(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidEncryptionMaterials(message);
  }
  public static Error create_InvalidEncryptionMaterialsTransition(dafny.DafnySequence<? extends Character> message) {
    return new Error_InvalidEncryptionMaterialsTransition(message);
  }
  public static Error create_AwsCryptographyKeyStore(software.amazon.cryptography.keystore.internaldafny.types.Error AwsCryptographyKeyStore) {
    return new Error_AwsCryptographyKeyStore(AwsCryptographyKeyStore);
  }
  public static Error create_AwsCryptographyPrimitives(software.amazon.cryptography.primitives.internaldafny.types.Error AwsCryptographyPrimitives) {
    return new Error_AwsCryptographyPrimitives(AwsCryptographyPrimitives);
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
  public boolean is_AwsCryptographicMaterialProvidersException() { return this instanceof Error_AwsCryptographicMaterialProvidersException; }
  public boolean is_EntryAlreadyExists() { return this instanceof Error_EntryAlreadyExists; }
  public boolean is_EntryDoesNotExist() { return this instanceof Error_EntryDoesNotExist; }
  public boolean is_InFlightTTLExceeded() { return this instanceof Error_InFlightTTLExceeded; }
  public boolean is_InvalidAlgorithmSuiteInfo() { return this instanceof Error_InvalidAlgorithmSuiteInfo; }
  public boolean is_InvalidAlgorithmSuiteInfoOnDecrypt() { return this instanceof Error_InvalidAlgorithmSuiteInfoOnDecrypt; }
  public boolean is_InvalidAlgorithmSuiteInfoOnEncrypt() { return this instanceof Error_InvalidAlgorithmSuiteInfoOnEncrypt; }
  public boolean is_InvalidDecryptionMaterials() { return this instanceof Error_InvalidDecryptionMaterials; }
  public boolean is_InvalidDecryptionMaterialsTransition() { return this instanceof Error_InvalidDecryptionMaterialsTransition; }
  public boolean is_InvalidEncryptionMaterials() { return this instanceof Error_InvalidEncryptionMaterials; }
  public boolean is_InvalidEncryptionMaterialsTransition() { return this instanceof Error_InvalidEncryptionMaterialsTransition; }
  public boolean is_AwsCryptographyKeyStore() { return this instanceof Error_AwsCryptographyKeyStore; }
  public boolean is_AwsCryptographyPrimitives() { return this instanceof Error_AwsCryptographyPrimitives; }
  public boolean is_ComAmazonawsDynamodb() { return this instanceof Error_ComAmazonawsDynamodb; }
  public boolean is_ComAmazonawsKms() { return this instanceof Error_ComAmazonawsKms; }
  public boolean is_CollectionOfErrors() { return this instanceof Error_CollectionOfErrors; }
  public boolean is_Opaque() { return this instanceof Error_Opaque; }
  public boolean is_OpaqueWithText() { return this instanceof Error_OpaqueWithText; }
  public dafny.DafnySequence<? extends Character> dtor_message() {
    Error d = this;
    if (d instanceof Error_AwsCryptographicMaterialProvidersException) { return ((Error_AwsCryptographicMaterialProvidersException)d)._message; }
    if (d instanceof Error_EntryAlreadyExists) { return ((Error_EntryAlreadyExists)d)._message; }
    if (d instanceof Error_EntryDoesNotExist) { return ((Error_EntryDoesNotExist)d)._message; }
    if (d instanceof Error_InFlightTTLExceeded) { return ((Error_InFlightTTLExceeded)d)._message; }
    if (d instanceof Error_InvalidAlgorithmSuiteInfo) { return ((Error_InvalidAlgorithmSuiteInfo)d)._message; }
    if (d instanceof Error_InvalidAlgorithmSuiteInfoOnDecrypt) { return ((Error_InvalidAlgorithmSuiteInfoOnDecrypt)d)._message; }
    if (d instanceof Error_InvalidAlgorithmSuiteInfoOnEncrypt) { return ((Error_InvalidAlgorithmSuiteInfoOnEncrypt)d)._message; }
    if (d instanceof Error_InvalidDecryptionMaterials) { return ((Error_InvalidDecryptionMaterials)d)._message; }
    if (d instanceof Error_InvalidDecryptionMaterialsTransition) { return ((Error_InvalidDecryptionMaterialsTransition)d)._message; }
    if (d instanceof Error_InvalidEncryptionMaterials) { return ((Error_InvalidEncryptionMaterials)d)._message; }
    if (d instanceof Error_InvalidEncryptionMaterialsTransition) { return ((Error_InvalidEncryptionMaterialsTransition)d)._message; }
    return ((Error_CollectionOfErrors)d)._message;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.Error dtor_AwsCryptographyKeyStore() {
    Error d = this;
    return ((Error_AwsCryptographyKeyStore)d)._AwsCryptographyKeyStore;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.Error dtor_AwsCryptographyPrimitives() {
    Error d = this;
    return ((Error_AwsCryptographyPrimitives)d)._AwsCryptographyPrimitives;
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
