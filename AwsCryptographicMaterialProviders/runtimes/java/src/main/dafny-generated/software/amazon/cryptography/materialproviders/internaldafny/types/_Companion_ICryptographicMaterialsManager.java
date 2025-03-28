// Interface ICryptographicMaterialsManager
// Dafny trait ICryptographicMaterialsManager compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_ICryptographicMaterialsManager {
  public _Companion_ICryptographicMaterialsManager() {
  }
  private static final dafny.TypeDescriptor<ICryptographicMaterialsManager> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(ICryptographicMaterialsManager.class, () -> null);
  public static dafny.TypeDescriptor<ICryptographicMaterialsManager> _typeDescriptor() {
    return (dafny.TypeDescriptor<ICryptographicMaterialsManager>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error> GetEncryptionMaterials(ICryptographicMaterialsManager _this, GetEncryptionMaterialsInput input)
  {
    Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error> output = (Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error>)null;
    if(true) {
      Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error> _out0;
      _out0 = (_this).GetEncryptionMaterials_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<DecryptMaterialsOutput, Error> DecryptMaterials(ICryptographicMaterialsManager _this, DecryptMaterialsInput input)
  {
    Wrappers_Compile.Result<DecryptMaterialsOutput, Error> output = (Wrappers_Compile.Result<DecryptMaterialsOutput, Error>)null;
    if(true) {
      Wrappers_Compile.Result<DecryptMaterialsOutput, Error> _out0;
      _out0 = (_this).DecryptMaterials_k(input);
      output = _out0;
    }
    return output;
  }
}
