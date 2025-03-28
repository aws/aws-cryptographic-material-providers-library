// Interface IKeyring
// Dafny trait IKeyring compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_IKeyring {
  public _Companion_IKeyring() {
  }
  private static final dafny.TypeDescriptor<IKeyring> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(IKeyring.class, () -> null);
  public static dafny.TypeDescriptor<IKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<IKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<OnEncryptOutput, Error> OnEncrypt(IKeyring _this, OnEncryptInput input)
  {
    Wrappers_Compile.Result<OnEncryptOutput, Error> output = (Wrappers_Compile.Result<OnEncryptOutput, Error>)null;
    if(true) {
      Wrappers_Compile.Result<OnEncryptOutput, Error> _out0;
      _out0 = (_this).OnEncrypt_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<OnDecryptOutput, Error> OnDecrypt(IKeyring _this, OnDecryptInput input)
  {
    Wrappers_Compile.Result<OnDecryptOutput, Error> output = (Wrappers_Compile.Result<OnDecryptOutput, Error>)null;
    if(true) {
      Wrappers_Compile.Result<OnDecryptOutput, Error> _out0;
      _out0 = (_this).OnDecrypt_k(input);
      output = _out0;
    }
    return output;
  }
}
