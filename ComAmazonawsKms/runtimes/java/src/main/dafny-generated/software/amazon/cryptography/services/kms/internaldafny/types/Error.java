// Class Error
// Dafny class Error compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Error {
  public Error() {
  }
  private static final dafny.TypeDescriptor<Error> _TYPE = dafny.TypeDescriptor.<Error>referenceWithInitializer(Error.class, () -> Error.Default());
  public static dafny.TypeDescriptor<Error> _typeDescriptor() {
    return (dafny.TypeDescriptor<Error>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Error theDefault = software.amazon.cryptography.services.kms.internaldafny.types.Error.create_AlreadyExistsException(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static Error Default() {
    return theDefault;
  }
  public static Error create_AlreadyExistsException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_AlreadyExistsException(message);
  }
  public static Error create_CloudHsmClusterInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CloudHsmClusterInUseException(message);
  }
  public static Error create_CloudHsmClusterInvalidConfigurationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CloudHsmClusterInvalidConfigurationException(message);
  }
  public static Error create_CloudHsmClusterNotActiveException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CloudHsmClusterNotActiveException(message);
  }
  public static Error create_CloudHsmClusterNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CloudHsmClusterNotFoundException(message);
  }
  public static Error create_CloudHsmClusterNotRelatedException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CloudHsmClusterNotRelatedException(message);
  }
  public static Error create_ConflictException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ConflictException(message);
  }
  public static Error create_CustomKeyStoreHasCMKsException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CustomKeyStoreHasCMKsException(message);
  }
  public static Error create_CustomKeyStoreInvalidStateException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CustomKeyStoreInvalidStateException(message);
  }
  public static Error create_CustomKeyStoreNameInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CustomKeyStoreNameInUseException(message);
  }
  public static Error create_CustomKeyStoreNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_CustomKeyStoreNotFoundException(message);
  }
  public static Error create_DependencyTimeoutException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_DependencyTimeoutException(message);
  }
  public static Error create_DisabledException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_DisabledException(message);
  }
  public static Error create_DryRunOperationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_DryRunOperationException(message);
  }
  public static Error create_ExpiredImportTokenException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_ExpiredImportTokenException(message);
  }
  public static Error create_IncorrectKeyException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_IncorrectKeyException(message);
  }
  public static Error create_IncorrectKeyMaterialException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_IncorrectKeyMaterialException(message);
  }
  public static Error create_IncorrectTrustAnchorException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_IncorrectTrustAnchorException(message);
  }
  public static Error create_InvalidAliasNameException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidAliasNameException(message);
  }
  public static Error create_InvalidArnException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidArnException(message);
  }
  public static Error create_InvalidCiphertextException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidCiphertextException(message);
  }
  public static Error create_InvalidGrantIdException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidGrantIdException(message);
  }
  public static Error create_InvalidGrantTokenException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidGrantTokenException(message);
  }
  public static Error create_InvalidImportTokenException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidImportTokenException(message);
  }
  public static Error create_InvalidKeyUsageException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidKeyUsageException(message);
  }
  public static Error create_InvalidMarkerException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_InvalidMarkerException(message);
  }
  public static Error create_KeyUnavailableException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_KeyUnavailableException(message);
  }
  public static Error create_KMSInternalException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_KMSInternalException(message);
  }
  public static Error create_KMSInvalidMacException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_KMSInvalidMacException(message);
  }
  public static Error create_KMSInvalidSignatureException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_KMSInvalidSignatureException(message);
  }
  public static Error create_KMSInvalidStateException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_KMSInvalidStateException(message);
  }
  public static Error create_LimitExceededException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_LimitExceededException(message);
  }
  public static Error create_MalformedPolicyDocumentException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_MalformedPolicyDocumentException(message);
  }
  public static Error create_NotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_NotFoundException(message);
  }
  public static Error create_TagException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_TagException(message);
  }
  public static Error create_UnsupportedOperationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_UnsupportedOperationException(message);
  }
  public static Error create_XksKeyAlreadyInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksKeyAlreadyInUseException(message);
  }
  public static Error create_XksKeyInvalidConfigurationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksKeyInvalidConfigurationException(message);
  }
  public static Error create_XksKeyNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksKeyNotFoundException(message);
  }
  public static Error create_XksProxyIncorrectAuthenticationCredentialException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyIncorrectAuthenticationCredentialException(message);
  }
  public static Error create_XksProxyInvalidConfigurationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyInvalidConfigurationException(message);
  }
  public static Error create_XksProxyInvalidResponseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyInvalidResponseException(message);
  }
  public static Error create_XksProxyUriEndpointInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyUriEndpointInUseException(message);
  }
  public static Error create_XksProxyUriInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyUriInUseException(message);
  }
  public static Error create_XksProxyUriUnreachableException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyUriUnreachableException(message);
  }
  public static Error create_XksProxyVpcEndpointServiceInUseException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyVpcEndpointServiceInUseException(message);
  }
  public static Error create_XksProxyVpcEndpointServiceInvalidConfigurationException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyVpcEndpointServiceInvalidConfigurationException(message);
  }
  public static Error create_XksProxyVpcEndpointServiceNotFoundException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    return new Error_XksProxyVpcEndpointServiceNotFoundException(message);
  }
  public static Error create_Opaque(Object obj) {
    return new Error_Opaque(obj);
  }
  public static Error create_OpaqueWithText(Object obj, dafny.DafnySequence<? extends Character> objMessage) {
    return new Error_OpaqueWithText(obj, objMessage);
  }
  public boolean is_AlreadyExistsException() { return this instanceof Error_AlreadyExistsException; }
  public boolean is_CloudHsmClusterInUseException() { return this instanceof Error_CloudHsmClusterInUseException; }
  public boolean is_CloudHsmClusterInvalidConfigurationException() { return this instanceof Error_CloudHsmClusterInvalidConfigurationException; }
  public boolean is_CloudHsmClusterNotActiveException() { return this instanceof Error_CloudHsmClusterNotActiveException; }
  public boolean is_CloudHsmClusterNotFoundException() { return this instanceof Error_CloudHsmClusterNotFoundException; }
  public boolean is_CloudHsmClusterNotRelatedException() { return this instanceof Error_CloudHsmClusterNotRelatedException; }
  public boolean is_ConflictException() { return this instanceof Error_ConflictException; }
  public boolean is_CustomKeyStoreHasCMKsException() { return this instanceof Error_CustomKeyStoreHasCMKsException; }
  public boolean is_CustomKeyStoreInvalidStateException() { return this instanceof Error_CustomKeyStoreInvalidStateException; }
  public boolean is_CustomKeyStoreNameInUseException() { return this instanceof Error_CustomKeyStoreNameInUseException; }
  public boolean is_CustomKeyStoreNotFoundException() { return this instanceof Error_CustomKeyStoreNotFoundException; }
  public boolean is_DependencyTimeoutException() { return this instanceof Error_DependencyTimeoutException; }
  public boolean is_DisabledException() { return this instanceof Error_DisabledException; }
  public boolean is_DryRunOperationException() { return this instanceof Error_DryRunOperationException; }
  public boolean is_ExpiredImportTokenException() { return this instanceof Error_ExpiredImportTokenException; }
  public boolean is_IncorrectKeyException() { return this instanceof Error_IncorrectKeyException; }
  public boolean is_IncorrectKeyMaterialException() { return this instanceof Error_IncorrectKeyMaterialException; }
  public boolean is_IncorrectTrustAnchorException() { return this instanceof Error_IncorrectTrustAnchorException; }
  public boolean is_InvalidAliasNameException() { return this instanceof Error_InvalidAliasNameException; }
  public boolean is_InvalidArnException() { return this instanceof Error_InvalidArnException; }
  public boolean is_InvalidCiphertextException() { return this instanceof Error_InvalidCiphertextException; }
  public boolean is_InvalidGrantIdException() { return this instanceof Error_InvalidGrantIdException; }
  public boolean is_InvalidGrantTokenException() { return this instanceof Error_InvalidGrantTokenException; }
  public boolean is_InvalidImportTokenException() { return this instanceof Error_InvalidImportTokenException; }
  public boolean is_InvalidKeyUsageException() { return this instanceof Error_InvalidKeyUsageException; }
  public boolean is_InvalidMarkerException() { return this instanceof Error_InvalidMarkerException; }
  public boolean is_KeyUnavailableException() { return this instanceof Error_KeyUnavailableException; }
  public boolean is_KMSInternalException() { return this instanceof Error_KMSInternalException; }
  public boolean is_KMSInvalidMacException() { return this instanceof Error_KMSInvalidMacException; }
  public boolean is_KMSInvalidSignatureException() { return this instanceof Error_KMSInvalidSignatureException; }
  public boolean is_KMSInvalidStateException() { return this instanceof Error_KMSInvalidStateException; }
  public boolean is_LimitExceededException() { return this instanceof Error_LimitExceededException; }
  public boolean is_MalformedPolicyDocumentException() { return this instanceof Error_MalformedPolicyDocumentException; }
  public boolean is_NotFoundException() { return this instanceof Error_NotFoundException; }
  public boolean is_TagException() { return this instanceof Error_TagException; }
  public boolean is_UnsupportedOperationException() { return this instanceof Error_UnsupportedOperationException; }
  public boolean is_XksKeyAlreadyInUseException() { return this instanceof Error_XksKeyAlreadyInUseException; }
  public boolean is_XksKeyInvalidConfigurationException() { return this instanceof Error_XksKeyInvalidConfigurationException; }
  public boolean is_XksKeyNotFoundException() { return this instanceof Error_XksKeyNotFoundException; }
  public boolean is_XksProxyIncorrectAuthenticationCredentialException() { return this instanceof Error_XksProxyIncorrectAuthenticationCredentialException; }
  public boolean is_XksProxyInvalidConfigurationException() { return this instanceof Error_XksProxyInvalidConfigurationException; }
  public boolean is_XksProxyInvalidResponseException() { return this instanceof Error_XksProxyInvalidResponseException; }
  public boolean is_XksProxyUriEndpointInUseException() { return this instanceof Error_XksProxyUriEndpointInUseException; }
  public boolean is_XksProxyUriInUseException() { return this instanceof Error_XksProxyUriInUseException; }
  public boolean is_XksProxyUriUnreachableException() { return this instanceof Error_XksProxyUriUnreachableException; }
  public boolean is_XksProxyVpcEndpointServiceInUseException() { return this instanceof Error_XksProxyVpcEndpointServiceInUseException; }
  public boolean is_XksProxyVpcEndpointServiceInvalidConfigurationException() { return this instanceof Error_XksProxyVpcEndpointServiceInvalidConfigurationException; }
  public boolean is_XksProxyVpcEndpointServiceNotFoundException() { return this instanceof Error_XksProxyVpcEndpointServiceNotFoundException; }
  public boolean is_Opaque() { return this instanceof Error_Opaque; }
  public boolean is_OpaqueWithText() { return this instanceof Error_OpaqueWithText; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_message() {
    Error d = this;
    if (d instanceof Error_AlreadyExistsException) { return ((Error_AlreadyExistsException)d)._message; }
    if (d instanceof Error_CloudHsmClusterInUseException) { return ((Error_CloudHsmClusterInUseException)d)._message; }
    if (d instanceof Error_CloudHsmClusterInvalidConfigurationException) { return ((Error_CloudHsmClusterInvalidConfigurationException)d)._message; }
    if (d instanceof Error_CloudHsmClusterNotActiveException) { return ((Error_CloudHsmClusterNotActiveException)d)._message; }
    if (d instanceof Error_CloudHsmClusterNotFoundException) { return ((Error_CloudHsmClusterNotFoundException)d)._message; }
    if (d instanceof Error_CloudHsmClusterNotRelatedException) { return ((Error_CloudHsmClusterNotRelatedException)d)._message; }
    if (d instanceof Error_ConflictException) { return ((Error_ConflictException)d)._message; }
    if (d instanceof Error_CustomKeyStoreHasCMKsException) { return ((Error_CustomKeyStoreHasCMKsException)d)._message; }
    if (d instanceof Error_CustomKeyStoreInvalidStateException) { return ((Error_CustomKeyStoreInvalidStateException)d)._message; }
    if (d instanceof Error_CustomKeyStoreNameInUseException) { return ((Error_CustomKeyStoreNameInUseException)d)._message; }
    if (d instanceof Error_CustomKeyStoreNotFoundException) { return ((Error_CustomKeyStoreNotFoundException)d)._message; }
    if (d instanceof Error_DependencyTimeoutException) { return ((Error_DependencyTimeoutException)d)._message; }
    if (d instanceof Error_DisabledException) { return ((Error_DisabledException)d)._message; }
    if (d instanceof Error_DryRunOperationException) { return ((Error_DryRunOperationException)d)._message; }
    if (d instanceof Error_ExpiredImportTokenException) { return ((Error_ExpiredImportTokenException)d)._message; }
    if (d instanceof Error_IncorrectKeyException) { return ((Error_IncorrectKeyException)d)._message; }
    if (d instanceof Error_IncorrectKeyMaterialException) { return ((Error_IncorrectKeyMaterialException)d)._message; }
    if (d instanceof Error_IncorrectTrustAnchorException) { return ((Error_IncorrectTrustAnchorException)d)._message; }
    if (d instanceof Error_InvalidAliasNameException) { return ((Error_InvalidAliasNameException)d)._message; }
    if (d instanceof Error_InvalidArnException) { return ((Error_InvalidArnException)d)._message; }
    if (d instanceof Error_InvalidCiphertextException) { return ((Error_InvalidCiphertextException)d)._message; }
    if (d instanceof Error_InvalidGrantIdException) { return ((Error_InvalidGrantIdException)d)._message; }
    if (d instanceof Error_InvalidGrantTokenException) { return ((Error_InvalidGrantTokenException)d)._message; }
    if (d instanceof Error_InvalidImportTokenException) { return ((Error_InvalidImportTokenException)d)._message; }
    if (d instanceof Error_InvalidKeyUsageException) { return ((Error_InvalidKeyUsageException)d)._message; }
    if (d instanceof Error_InvalidMarkerException) { return ((Error_InvalidMarkerException)d)._message; }
    if (d instanceof Error_KeyUnavailableException) { return ((Error_KeyUnavailableException)d)._message; }
    if (d instanceof Error_KMSInternalException) { return ((Error_KMSInternalException)d)._message; }
    if (d instanceof Error_KMSInvalidMacException) { return ((Error_KMSInvalidMacException)d)._message; }
    if (d instanceof Error_KMSInvalidSignatureException) { return ((Error_KMSInvalidSignatureException)d)._message; }
    if (d instanceof Error_KMSInvalidStateException) { return ((Error_KMSInvalidStateException)d)._message; }
    if (d instanceof Error_LimitExceededException) { return ((Error_LimitExceededException)d)._message; }
    if (d instanceof Error_MalformedPolicyDocumentException) { return ((Error_MalformedPolicyDocumentException)d)._message; }
    if (d instanceof Error_NotFoundException) { return ((Error_NotFoundException)d)._message; }
    if (d instanceof Error_TagException) { return ((Error_TagException)d)._message; }
    if (d instanceof Error_UnsupportedOperationException) { return ((Error_UnsupportedOperationException)d)._message; }
    if (d instanceof Error_XksKeyAlreadyInUseException) { return ((Error_XksKeyAlreadyInUseException)d)._message; }
    if (d instanceof Error_XksKeyInvalidConfigurationException) { return ((Error_XksKeyInvalidConfigurationException)d)._message; }
    if (d instanceof Error_XksKeyNotFoundException) { return ((Error_XksKeyNotFoundException)d)._message; }
    if (d instanceof Error_XksProxyIncorrectAuthenticationCredentialException) { return ((Error_XksProxyIncorrectAuthenticationCredentialException)d)._message; }
    if (d instanceof Error_XksProxyInvalidConfigurationException) { return ((Error_XksProxyInvalidConfigurationException)d)._message; }
    if (d instanceof Error_XksProxyInvalidResponseException) { return ((Error_XksProxyInvalidResponseException)d)._message; }
    if (d instanceof Error_XksProxyUriEndpointInUseException) { return ((Error_XksProxyUriEndpointInUseException)d)._message; }
    if (d instanceof Error_XksProxyUriInUseException) { return ((Error_XksProxyUriInUseException)d)._message; }
    if (d instanceof Error_XksProxyUriUnreachableException) { return ((Error_XksProxyUriUnreachableException)d)._message; }
    if (d instanceof Error_XksProxyVpcEndpointServiceInUseException) { return ((Error_XksProxyVpcEndpointServiceInUseException)d)._message; }
    if (d instanceof Error_XksProxyVpcEndpointServiceInvalidConfigurationException) { return ((Error_XksProxyVpcEndpointServiceInvalidConfigurationException)d)._message; }
    return ((Error_XksProxyVpcEndpointServiceNotFoundException)d)._message;
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
