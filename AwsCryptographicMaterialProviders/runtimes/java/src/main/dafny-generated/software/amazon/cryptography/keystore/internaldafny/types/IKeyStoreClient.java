// Interface IKeyStoreClient
// Dafny trait IKeyStoreClient compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IKeyStoreClient {
  public Wrappers_Compile.Result<GetKeyStoreInfoOutput, Error> GetKeyStoreInfo();
  public Wrappers_Compile.Result<CreateKeyStoreOutput, Error> CreateKeyStore(CreateKeyStoreInput input);
  public Wrappers_Compile.Result<CreateKeyOutput, Error> CreateKey(CreateKeyInput input);
  public Wrappers_Compile.Result<VersionKeyOutput, Error> VersionKey(VersionKeyInput input);
  public Wrappers_Compile.Result<GetActiveBranchKeyOutput, Error> GetActiveBranchKey(GetActiveBranchKeyInput input);
  public Wrappers_Compile.Result<GetBranchKeyVersionOutput, Error> GetBranchKeyVersion(GetBranchKeyVersionInput input);
  public Wrappers_Compile.Result<GetBeaconKeyOutput, Error> GetBeaconKey(GetBeaconKeyInput input);
}
