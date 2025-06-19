// Class __default
// Dafny class __default compiled into Java
package CMM_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean RequiredEncryptionContextKeys_q(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> requiredEncryptionContextKeys, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptionMaterials)
  {
    return ((dafny.Function2<Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, Boolean>)(_0_requiredEncryptionContextKeys, _1_encryptionMaterials) -> dafny.Helpers.Quantifier(((_0_requiredEncryptionContextKeys).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()))).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends java.lang.Byte> _forall_var_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends java.lang.Byte> _2_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_0;
      if (UTF8.ValidUTF8Bytes._Is(_2_k)) {
        return !(((_0_requiredEncryptionContextKeys).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()))).contains(_2_k)) || (((_1_encryptionMaterials).dtor_requiredEncryptionContextKeys()).contains(_2_k));
      } else {
        return true;
      }
    }))).apply(requiredEncryptionContextKeys, encryptionMaterials);
  }
  public static boolean EncryptionContextComplete(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials decryptionMaterials)
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_reproducedEncryptionContext = ((input).dtor_reproducedEncryptionContext()).UnwrapOr(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnyMap.fromElements());
    return ((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, Boolean>)(_1_reproducedEncryptionContext, _2_decryptionMaterials) -> dafny.Helpers.Quantifier((_1_reproducedEncryptionContext).keySet().Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends java.lang.Byte> _forall_var_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends java.lang.Byte> _3_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_0;
      return !((_1_reproducedEncryptionContext).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_3_k)) || ((((_2_decryptionMaterials).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_3_k)) && ((((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((_2_decryptionMaterials).dtor_encryptionContext()).get(_3_k)))).equals(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_1_reproducedEncryptionContext).get(_3_k))))));
    }))).apply(_0_reproducedEncryptionContext, decryptionMaterials);
  }
  public static boolean ReproducedEncryptionContext_q(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input) {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_reproducedEncryptionContext = ((input).dtor_reproducedEncryptionContext()).UnwrapOr(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnyMap.fromElements());
    return ((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput, Boolean>)(_1_reproducedEncryptionContext, _2_input) -> dafny.Helpers.Quantifier((_1_reproducedEncryptionContext).keySet().Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends java.lang.Byte> _forall_var_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends java.lang.Byte> _3_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_0;
      return !(((_1_reproducedEncryptionContext).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_3_k)) && (((_2_input).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_3_k))) || ((((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((_2_input).dtor_encryptionContext()).get(_3_k)))).equals(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_1_reproducedEncryptionContext).get(_3_k)))));
    }))).apply(_0_reproducedEncryptionContext, input);
  }
  @Override
  public java.lang.String toString() {
    return "CMM._default";
  }
}
