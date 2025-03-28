// Interface IBranchKeyIdSupplier
// Dafny trait IBranchKeyIdSupplier compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IBranchKeyIdSupplier {
  public Wrappers_Compile.Result<GetBranchKeyIdOutput, Error> GetBranchKeyId(GetBranchKeyIdInput input);
  public Wrappers_Compile.Result<GetBranchKeyIdOutput, Error> GetBranchKeyId_k(GetBranchKeyIdInput input);
}
