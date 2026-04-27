// Interface IKeyVectorsClient
// Dafny trait IKeyVectorsClient compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IKeyVectorsClient {
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Error> CreateTestVectorKeyring(TestVectorKeyringInput input);
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Error> CreateWrappedTestVectorKeyring(TestVectorKeyringInput input);
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, Error> CreateWrappedTestVectorCmm(TestVectorCmmInput input);
  public Wrappers_Compile.Result<GetKeyDescriptionOutput, Error> GetKeyDescription(GetKeyDescriptionInput input);
  public Wrappers_Compile.Result<SerializeKeyDescriptionOutput, Error> SerializeKeyDescription(SerializeKeyDescriptionInput input);
}
