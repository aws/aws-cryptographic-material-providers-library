// Class __default
// Dafny class __default compiled into Java
package WrappedHMAC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Digest(software.amazon.cryptography.primitives.internaldafny.types.HMacInput input) {
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (((long) ((input).dtor_key()).cardinalityInt()) == 0 ? 0 : 1) == 1, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Key MUST NOT be 0 bytes.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) ((input).dtor_message()).cardinalityInt(), (StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()).longValue()) < 0, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Message over INT32_MAX_LIMIT")));
      if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
        return (_1_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError2 = HMAC.__default.Digest(input);
        if ((_2_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
          return (_2_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        } else {
          dafny.DafnySequence<? extends java.lang.Byte> _3_value = (_2_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
          return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _3_value);
        }
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "WrappedHMAC._default";
  }
}
