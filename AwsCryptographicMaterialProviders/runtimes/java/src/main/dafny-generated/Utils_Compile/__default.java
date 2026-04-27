// Class __default
// Dafny class __default compiled into Java
package Utils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey privateKey, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybePublicKey;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = (crypto).GetPublicKeyFromPrivateKey(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput.create(curveSpec, privateKey));
      _0_maybePublicKey = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.Default());
      _1_valueOrError0 = (_0_maybePublicKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_1_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        return res;
      }
      software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput _3_keyPairOutput;
      _3_keyPairOutput = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_3_keyPairOutput).dtor_publicKey());
    }
    return res;
  }
  @Override
  public java.lang.String toString() {
    return "Utils._default";
  }
}
