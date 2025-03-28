// Class S3SseAlgorithm
// Dafny class S3SseAlgorithm compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class S3SseAlgorithm {
  public S3SseAlgorithm() {
  }
  private static final dafny.TypeDescriptor<S3SseAlgorithm> _TYPE = dafny.TypeDescriptor.<S3SseAlgorithm>referenceWithInitializer(S3SseAlgorithm.class, () -> S3SseAlgorithm.Default());
  public static dafny.TypeDescriptor<S3SseAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<S3SseAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final S3SseAlgorithm theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.S3SseAlgorithm.create_AES256();
  public static S3SseAlgorithm Default() {
    return theDefault;
  }
  public static S3SseAlgorithm create_AES256() {
    return new S3SseAlgorithm_AES256();
  }
  public static S3SseAlgorithm create_KMS() {
    return new S3SseAlgorithm_KMS();
  }
  public boolean is_AES256() { return this instanceof S3SseAlgorithm_AES256; }
  public boolean is_KMS() { return this instanceof S3SseAlgorithm_KMS; }
  public static java.util.ArrayList<S3SseAlgorithm> AllSingletonConstructors() {
    java.util.ArrayList<S3SseAlgorithm> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new S3SseAlgorithm_AES256());
    singleton_iterator.add(new S3SseAlgorithm_KMS());
    return singleton_iterator;
  }
}
