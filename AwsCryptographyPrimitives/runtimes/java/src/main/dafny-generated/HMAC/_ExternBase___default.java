// Class _ExternBase___default
// Dafny class __default compiled into Java
package HMAC;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static Wrappers_Compile.Result<HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateHMacSuccess(HMac hmac) {
    return Wrappers_Compile.Result.<HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), hmac);
  }
  public static Wrappers_Compile.Result<HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateHMacFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateDigestSuccess(dafny.DafnySequence<? extends java.lang.Byte> bytes) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), bytes);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateDigestFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "HMAC._default";
  }
}
