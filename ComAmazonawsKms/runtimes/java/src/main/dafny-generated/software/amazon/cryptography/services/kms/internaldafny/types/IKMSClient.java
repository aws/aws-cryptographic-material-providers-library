// Interface IKMSClient
// Dafny trait IKMSClient compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface IKMSClient {
  public Wrappers_Compile.Result<CancelKeyDeletionResponse, Error> CancelKeyDeletion(CancelKeyDeletionRequest input);
  public Wrappers_Compile.Result<ConnectCustomKeyStoreResponse, Error> ConnectCustomKeyStore(ConnectCustomKeyStoreRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> CreateAlias(CreateAliasRequest input);
  public Wrappers_Compile.Result<CreateCustomKeyStoreResponse, Error> CreateCustomKeyStore(CreateCustomKeyStoreRequest input);
  public Wrappers_Compile.Result<CreateGrantResponse, Error> CreateGrant(CreateGrantRequest input);
  public Wrappers_Compile.Result<CreateKeyResponse, Error> CreateKey(CreateKeyRequest input);
  public Wrappers_Compile.Result<DecryptResponse, Error> Decrypt(DecryptRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DeleteAlias(DeleteAliasRequest input);
  public Wrappers_Compile.Result<DeleteCustomKeyStoreResponse, Error> DeleteCustomKeyStore(DeleteCustomKeyStoreRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DeleteImportedKeyMaterial(DeleteImportedKeyMaterialRequest input);
  public Wrappers_Compile.Result<DeriveSharedSecretResponse, Error> DeriveSharedSecret(DeriveSharedSecretRequest input);
  public Wrappers_Compile.Result<DescribeCustomKeyStoresResponse, Error> DescribeCustomKeyStores(DescribeCustomKeyStoresRequest input);
  public Wrappers_Compile.Result<DescribeKeyResponse, Error> DescribeKey(DescribeKeyRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DisableKey(DisableKeyRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DisableKeyRotation(DisableKeyRotationRequest input);
  public Wrappers_Compile.Result<DisconnectCustomKeyStoreResponse, Error> DisconnectCustomKeyStore(DisconnectCustomKeyStoreRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> EnableKey(EnableKeyRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> EnableKeyRotation(EnableKeyRotationRequest input);
  public Wrappers_Compile.Result<EncryptResponse, Error> Encrypt(EncryptRequest input);
  public Wrappers_Compile.Result<GenerateDataKeyResponse, Error> GenerateDataKey(GenerateDataKeyRequest input);
  public Wrappers_Compile.Result<GenerateDataKeyPairResponse, Error> GenerateDataKeyPair(GenerateDataKeyPairRequest input);
  public Wrappers_Compile.Result<GenerateDataKeyPairWithoutPlaintextResponse, Error> GenerateDataKeyPairWithoutPlaintext(GenerateDataKeyPairWithoutPlaintextRequest input);
  public Wrappers_Compile.Result<GenerateDataKeyWithoutPlaintextResponse, Error> GenerateDataKeyWithoutPlaintext(GenerateDataKeyWithoutPlaintextRequest input);
  public Wrappers_Compile.Result<GenerateMacResponse, Error> GenerateMac(GenerateMacRequest input);
  public Wrappers_Compile.Result<GenerateRandomResponse, Error> GenerateRandom(GenerateRandomRequest input);
  public Wrappers_Compile.Result<GetKeyPolicyResponse, Error> GetKeyPolicy(GetKeyPolicyRequest input);
  public Wrappers_Compile.Result<GetKeyRotationStatusResponse, Error> GetKeyRotationStatus(GetKeyRotationStatusRequest input);
  public Wrappers_Compile.Result<GetParametersForImportResponse, Error> GetParametersForImport(GetParametersForImportRequest input);
  public Wrappers_Compile.Result<GetPublicKeyResponse, Error> GetPublicKey(GetPublicKeyRequest input);
  public Wrappers_Compile.Result<ImportKeyMaterialResponse, Error> ImportKeyMaterial(ImportKeyMaterialRequest input);
  public Wrappers_Compile.Result<ListAliasesResponse, Error> ListAliases(ListAliasesRequest input);
  public Wrappers_Compile.Result<ListGrantsResponse, Error> ListGrants(ListGrantsRequest input);
  public Wrappers_Compile.Result<ListKeyPoliciesResponse, Error> ListKeyPolicies(ListKeyPoliciesRequest input);
  public Wrappers_Compile.Result<ListKeyRotationsResponse, Error> ListKeyRotations(ListKeyRotationsRequest input);
  public Wrappers_Compile.Result<ListKeysResponse, Error> ListKeys(ListKeysRequest input);
  public Wrappers_Compile.Result<ListResourceTagsResponse, Error> ListResourceTags(ListResourceTagsRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> PutKeyPolicy(PutKeyPolicyRequest input);
  public Wrappers_Compile.Result<ReEncryptResponse, Error> ReEncrypt(ReEncryptRequest input);
  public Wrappers_Compile.Result<ReplicateKeyResponse, Error> ReplicateKey(ReplicateKeyRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> RetireGrant(RetireGrantRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> RevokeGrant(RevokeGrantRequest input);
  public Wrappers_Compile.Result<RotateKeyOnDemandResponse, Error> RotateKeyOnDemand(RotateKeyOnDemandRequest input);
  public Wrappers_Compile.Result<ScheduleKeyDeletionResponse, Error> ScheduleKeyDeletion(ScheduleKeyDeletionRequest input);
  public Wrappers_Compile.Result<SignResponse, Error> Sign(SignRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> TagResource(TagResourceRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UntagResource(UntagResourceRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UpdateAlias(UpdateAliasRequest input);
  public Wrappers_Compile.Result<UpdateCustomKeyStoreResponse, Error> UpdateCustomKeyStore(UpdateCustomKeyStoreRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UpdateKeyDescription(UpdateKeyDescriptionRequest input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UpdatePrimaryRegion(UpdatePrimaryRegionRequest input);
  public Wrappers_Compile.Result<VerifyResponse, Error> Verify(VerifyRequest input);
  public Wrappers_Compile.Result<VerifyMacResponse, Error> VerifyMac(VerifyMacRequest input);
}
