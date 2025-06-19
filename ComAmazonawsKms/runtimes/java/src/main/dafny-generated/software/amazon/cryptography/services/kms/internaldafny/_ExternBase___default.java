// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.services.kms.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static KMSClientConfigType DefaultKMSClientConfigType() {
    return KMSClientConfigType.create();
  }
  public static dafny.DafnySequence<? extends Character> DafnyUserAgentSuffix(dafny.DafnySequence<? extends Character> runtime) {
    dafny.DafnySequence<? extends Character> _0_version = dafny.DafnySequence.asString("1.0.1");
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("AwsCryptographicMPL/"), runtime), dafny.DafnySequence.asString("/")), _0_version);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.services.kms.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "Com.Amazonaws.Kms._default";
  }
}
