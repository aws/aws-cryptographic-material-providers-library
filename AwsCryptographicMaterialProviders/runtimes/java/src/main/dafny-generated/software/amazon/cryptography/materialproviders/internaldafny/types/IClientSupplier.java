// Interface IClientSupplier
// Dafny trait IClientSupplier compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IClientSupplier {
  public Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error> GetClient(GetClientInput input);
  public Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error> GetClient_k(GetClientInput input);
}
