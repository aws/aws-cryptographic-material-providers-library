// Interface IKeyring
// Dafny trait IKeyring compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IKeyring {
  public Wrappers_Compile.Result<OnEncryptOutput, Error> OnEncrypt(OnEncryptInput input);
  public Wrappers_Compile.Result<OnEncryptOutput, Error> OnEncrypt_k(OnEncryptInput input);
  public Wrappers_Compile.Result<OnDecryptOutput, Error> OnDecrypt(OnDecryptInput input);
  public Wrappers_Compile.Result<OnDecryptOutput, Error> OnDecrypt_k(OnDecryptInput input);
}
