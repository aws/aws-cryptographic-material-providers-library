// Class AwsKmsIdentifierString
// Dafny class AwsKmsIdentifierString compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsIdentifierString {
  public AwsKmsIdentifierString() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends Character> __source) {
    dafny.DafnySequence<? extends Character> _2_s = __source;
    return (__default.IsAwsKmsIdentifierString(_2_s)).is_Success();
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends Character>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Character>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
