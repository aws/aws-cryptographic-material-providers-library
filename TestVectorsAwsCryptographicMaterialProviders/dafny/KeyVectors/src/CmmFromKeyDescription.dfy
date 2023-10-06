// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTestVectorKeysTypes.dfy"
  // Yes this is including from somewhere else.
include "../../TestVectorsAwsCryptographicMaterialProviders/src/LibraryIndex.dfy"
include "KeyringFromKeyDescription.dfy"
include "CreateStaticCMCs.dfy"

module {:options "-functionSyntax:4"} CmmFromKeyDescription {
  import opened Types = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import MPL = AwsCryptographyMaterialProvidersTypes
  import opened Wrappers
  import KeyringFromKeyDescription
  import CreateStaticCMCs
  import UTF8

  method ToCmm(
    mpl: MPL.IAwsCryptographicMaterialProvidersClient,
    info: KeyringFromKeyDescription.KeyringInfo,
    forOperation: CmmOperation
  )
    returns (output: Result<MPL.ICryptographicMaterialsManager, Error>)
    requires mpl.ValidState()
    modifies mpl.Modifies
    decreases info.description
    ensures mpl.ValidState()
    ensures output.Success? ==>
              && output.value.ValidState()
              && fresh(output.value.Modifies - mpl.Modifies)
              && output.value.Modifies !! {mpl.History}
  {
    var KeyringInfo(description, material) := info;

    match description
    case RequiredEncryptionContext(cmm) => {
      var underlying :- ToCmm(mpl, info.( description := cmm.underlying ), forOperation);
      var output' := mpl
      .CreateRequiredEncryptionContextCMM(
        MPL.CreateRequiredEncryptionContextCMMInput(
          underlyingCMM := Some(underlying),
          keyring := None,
          requiredEncryptionContextKeys := cmm.requiredEncryptionContextKeys
        )
      );
      output := output'.MapFailure(e => Types.AwsCryptographyMaterialProviders(e));
    }
    case Caching(cmm) => {

      var identifier := if cmm.getEntryIdentifier.Some? && cmm.putEntryIdentifier.Some? then
        Some(CreateStaticCMCs.Identifiers(
               getIdentifier := cmm.getEntryIdentifier.value,
               putIdentifier := cmm.putEntryIdentifier.value
             ))
      else if cmm.getEntryIdentifier.Some? then
        Some(CreateStaticCMCs.Identifier.GetIdentifier(
               identifier := cmm.getEntryIdentifier.value
             ))
      else if cmm.getEntryIdentifier.Some? then
        Some(CreateStaticCMCs.PutIdentifier(
               identifier := cmm.putEntryIdentifier.value
             ))
      else
        None;

      :- Need(identifier.Some? ==> material.Some? && material.value.StaticMaterial?,
              KeyVectorException( message := "CachingCMM only supports StaticMaterial."));
      var underlying :- ToCmm(mpl, info.( description := cmm.underlying ), forOperation);



      var entry := if identifier.Some? then
        match forOperation
        case ENCRYPT() =>
          Some(CreateStaticCMCs.StaticCMCEntry(
                 materials := MPL.Materials.Encryption(
                   MPL.EncryptionMaterials(
                     algorithmSuite := material.value.algorithmSuite,
                     encryptedDataKeys := material.value.encryptedDataKeys,
                     encryptionContext := material.value.encryptionContext,
                     requiredEncryptionContextKeys := material.value.requiredEncryptionContextKeys,
                     plaintextDataKey := material.value.plaintextDataKey,
                     signingKey := material.value.signingKey,
                     symmetricSigningKeys := material.value.symmetricSigningKeys
                   )),
                 identifier := identifier.value
               ))
        case DECRYPT() =>
          Some(CreateStaticCMCs.StaticCMCEntry(
                 materials := MPL.Materials.Decryption(
                   MPL.DecryptionMaterials(
                     algorithmSuite := material.value.algorithmSuite,
                     encryptionContext := material.value.encryptionContext,
                     requiredEncryptionContextKeys := material.value.requiredEncryptionContextKeys,
                     plaintextDataKey := material.value.plaintextDataKey,
                     verificationKey := material.value.verificationKey,
                     symmetricSigningKey := None // need to pass one vs many :(
                   )),
                 identifier := identifier.value
               ))
      else
        None;

      var underlyingCMC := CreateStaticCMCs.CreateStaticCMC(entry);
      var partitionKey :- expect UTF8.Encode("asdf");

      var createCachingCMMInput
        := MPL.CreateCachingCMMInput(
        underlyingCMM := Some(underlying),
        keyring := None,
        underlyingCMC := underlyingCMC,
        cacheLimitTtlSeconds := cmm.cacheLimitTtlSeconds,
        partitionKey := Some(partitionKey), // String "asdf" in UTF8 bytes
        limitBytes := cmm.limitBytes,
        limitMessages := cmm.limitMessages
      );

      var output' := mpl.CreateCachingCMM(createCachingCMMInput);
      output := output'.MapFailure(e => Types.AwsCryptographyMaterialProviders(e));

      assert createCachingCMMInput.underlyingCMC is CreateStaticCMCs.StaticCMC;
    }
    case _ => {
      var keyring :- KeyringFromKeyDescription.ToKeyring(mpl, info);
      var output' := mpl
      .CreateDefaultCryptographicMaterialsManager(
        MPL.CreateDefaultCryptographicMaterialsManagerInput( keyring := keyring )
      );
      output := output'.MapFailure(e => Types.AwsCryptographyMaterialProviders(e));
    }
  }

}
