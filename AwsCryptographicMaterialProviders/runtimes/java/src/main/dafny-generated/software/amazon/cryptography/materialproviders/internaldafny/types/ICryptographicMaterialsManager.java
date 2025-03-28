// Interface ICryptographicMaterialsManager
// Dafny trait ICryptographicMaterialsManager compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface ICryptographicMaterialsManager {
  public Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error> GetEncryptionMaterials(GetEncryptionMaterialsInput input);
  public Wrappers_Compile.Result<GetEncryptionMaterialsOutput, Error> GetEncryptionMaterials_k(GetEncryptionMaterialsInput input);
  public Wrappers_Compile.Result<DecryptMaterialsOutput, Error> DecryptMaterials(DecryptMaterialsInput input);
  public Wrappers_Compile.Result<DecryptMaterialsOutput, Error> DecryptMaterials_k(DecryptMaterialsInput input);
}
