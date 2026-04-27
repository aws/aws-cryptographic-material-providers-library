// Class S3Bucket
// Dafny class S3Bucket compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class S3Bucket {
  public S3Bucket() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends Character> __source) {
    dafny.DafnySequence<? extends Character> _36_x = __source;
    return __default.IsValid__S3Bucket(_36_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends Character>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
